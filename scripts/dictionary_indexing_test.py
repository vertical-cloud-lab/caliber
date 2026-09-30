# Dictionary indexing test on AlSi10Mg Area 2, first 25 map rows (4,900 patterns).
#
# Compares Hough indexing (PyEBSDIndex) against dictionary indexing + orientation
# refinement (kikuchipy, EMsoft-simulated master patterns from Zenodo), and runs
# an Al-vs-Si dictionary phase-discrimination test that Hough cannot do.
#
# Free stack: pip install kikuchipy pyebsdindex orix matplotlib
#
# Data: EDAX .up2 v3, 42-byte header, 111x111 px patterns, 196x446 map, 2 um step.
# Only the first 25 rows are fetched (HTTP range request against the public Box share).

import gzip
import json
import shutil
import time
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import kikuchipy as kp
from orix import io, plot, sampling
from orix.crystal_map import CrystalMap
from orix.quaternion import Orientation, Rotation, symmetry

N_ROWS, N_COLS, PAT = 25, 196, 111
OUT = Path(__file__).resolve().parents[1] / "example" / "area2-results" / "dictionary-indexing"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- 1. get the patterns
UP2_URL = (
    "https://byu.app.box.com/index.php?rm=box_download_shared_file"
    "&shared_name=hz48nsx7ciln1jifm3u0yo5vqpge2lma&file_id=f_2371754519702"
)
slice_file = Path("/tmp/area2_slice.bin")
if not slice_file.exists():
    n_bytes = 42 + N_ROWS * N_COLS * PAT * PAT * 2
    req = urllib.request.Request(UP2_URL, headers={"Range": "bytes=0-%d" % (n_bytes - 1)})
    with urllib.request.urlopen(req) as r, open(slice_file, "wb") as f:
        shutil.copyfileobj(r, f)

raw = np.fromfile(slice_file, dtype=np.uint16, offset=42).reshape(N_ROWS, N_COLS, PAT, PAT)

# ---------------------------------------------------------------- 2. background correction
s = kp.signals.EBSD(raw.copy())
s.static_background = raw.mean(axis=(0, 1)).astype(np.uint16)  # .up2 stores no flat-field
s.remove_static_background(operation="subtract", show_progressbar=False)
s.remove_dynamic_background(show_progressbar=False)
corrected = s.data.copy()

# ---------------------------------------------------------------- 3. Hough baseline (TEAM-style)
al_mp = kp.data.ebsd_master_pattern(
    "al", allow_download=True, show_progressbar=False,
    projection="lambert", energy=20, hemisphere="upper",
)
si_mp = kp.data.ebsd_master_pattern(
    "si", allow_download=True, show_progressbar=False,
    projection="lambert", energy=20, hemisphere="upper",
)

from orix.crystal_map import PhaseList

al_phases = PhaseList(al_mp.phase)
det0 = kp.detectors.EBSDDetector((PAT, PAT), sample_tilt=70.0)
indexer = det0.get_indexer(al_phases, nBands=9, tSigma=2, rSigma=2)
s_grid, _ = s.extract_grid((5, 5), return_indices=True)
det = s_grid.hough_indexing_optimize_pc(
    pc0=[0.5, 0.5, 0.6], indexer=indexer, batch=False, method="PSO", search_limit=0.2
)
indexer = det.get_indexer(al_phases, nBands=9, tSigma=2, rSigma=2)
t0 = time.time()
xmap_hough = s.hough_indexing(phase_list=al_phases, indexer=indexer, verbose=0)
t_hough = time.time() - t0
g_hough = xmap_hough.rotations  # flat, map (row-major) order

# ---------------------------------------------------------------- 4. boost SNR for DI
# Patterns are too noisy for per-pixel cross-correlation; average each pattern
# with its neighbours (grains are tens of pixels, so no orientation mixing).
s.average_neighbour_patterns(show_progressbar=False)

signal_mask = ~kp.filters.Window("circular", (PAT, PAT)).astype(bool)  # True = excluded

# ---------------------------------------------------------------- 5. dictionary indexing, Al and Si
R = sampling.get_sample_fundamental(method="cubochoric", resolution=2.5, point_group=symmetry.Oh)
yy, xx = np.indices((N_ROWS, N_COLS))
results = {}
for name, mp in [("al", al_mp), ("si", si_mp)]:
    t0 = time.time()
    sim = mp.get_patterns(
        rotations=R, detector=det, energy=20, compute=True,
        show_progressbar=False, dtype_out=np.float32,
    )
    t_proj = time.time() - t0
    t0 = time.time()
    xmap_di = s.dictionary_indexing(sim, metric="ncc", keep_n=5, signal_mask=signal_mask)
    t_di = time.time() - t0
    xmap_best = CrystalMap(
        rotations=Rotation(xmap_di.rotations[:, 0].data),
        x=xx.ravel().astype(float), y=yy.ravel().astype(float),
        phase_list=xmap_di.phases,
    )
    t0 = time.time()
    xmap_ref = s.refine_orientation(
        xmap=xmap_best, detector=det, master_pattern=mp, energy=20,
        signal_mask=signal_mask, method="minimize", trust_region=[2, 2, 2],
    )
    t_ref = time.time() - t0
    results[name] = {
        "xmap_di": xmap_di, "xmap_ref": xmap_ref,
        "t_proj": t_proj, "t_di": t_di, "t_ref": t_ref,
    }
    del sim

ncc_al_di = results["al"]["xmap_di"].scores[:, 0]
ncc_al = results["al"]["xmap_ref"].scores.flatten()
ncc_si = results["si"]["xmap_ref"].scores.flatten()
g_di = results["al"]["xmap_ref"].rotations

# ---------------------------------------------------------------- 6. compare with Hough
O_h = Orientation(g_hough, symmetry.Oh)
O_d = Orientation(g_di, symmetry.Oh)
misori = O_h.angle_with(O_d, degrees=True)
ci = xmap_hough.cm
fit = xmap_hough.fit
low_ci = ci < 0.1

stats = {
    "n_patterns": int(misori.size),
    "dictionary_size": int(R.size),
    "dictionary_resolution_deg": 2.5,
    "pc_bruker": [round(float(v), 4) for v in det.pc_average],
    "hough": {
        "s_per_map": round(t_hough, 1),
        "ci_gt_0.1": round(float((ci > 0.1).mean()), 4),
        "median_ci": round(float(np.median(ci)), 3),
        "median_fit_deg": round(float(np.median(fit)), 3),
    },
    "di_al": {
        "s_projection": round(results["al"]["t_proj"], 1),
        "s_indexing": round(results["al"]["t_di"], 1),
        "s_refinement": round(results["al"]["t_ref"], 1),
        "median_ncc_di": round(float(np.median(ncc_al_di)), 3),
        "median_ncc_refined": round(float(np.median(ncc_al)), 3),
    },
    "agreement_hough_vs_di": {
        "median_misorientation_deg": round(float(np.median(misori)), 2),
        "frac_within_2deg": round(float((misori < 2).mean()), 3),
        "frac_within_5deg": round(float((misori < 5).mean()), 3),
        "median_misori_where_ci_lt_0.1": round(float(np.median(misori[low_ci])), 2) if low_ci.any() else None,
        "n_ci_lt_0.1": int(low_ci.sum()),
    },
    "phase_test_al_vs_si": {
        "median_ncc_al": round(float(np.median(ncc_al)), 3),
        "median_ncc_si": round(float(np.median(ncc_si)), 3),
        "frac_al_wins": round(float((ncc_al > ncc_si).mean()), 4),
        "median_delta_ncc": round(float(np.median(ncc_al - ncc_si)), 3),
    },
}
(OUT / "stats.json").write_text(json.dumps(stats, indent=2))
print(json.dumps(stats, indent=2))

# ---------------------------------------------------------------- 7. plots
mis2d = misori.reshape(N_ROWS, N_COLS)
ncc2d = ncc_al.reshape(N_ROWS, N_COLS)

fig, ax = plt.subplots(2, 2, figsize=(14, 5.2))
im = ax[0, 0].imshow(ncc_al_di.reshape(N_ROWS, N_COLS), cmap="viridis")
ax[0, 0].set_title("DI best NCC (before refinement)")
fig.colorbar(im, ax=ax[0, 0], shrink=0.8)
im = ax[0, 1].imshow(ncc2d, cmap="viridis")
ax[0, 1].set_title("NCC after refinement")
fig.colorbar(im, ax=ax[0, 1], shrink=0.8)
im = ax[1, 0].imshow(mis2d, cmap="inferno", vmax=10)
ax[1, 0].set_title("misorientation DI vs Hough (deg, capped 10)")
fig.colorbar(im, ax=ax[1, 0], shrink=0.8)
im = ax[1, 1].imshow(ci.reshape(N_ROWS, N_COLS), cmap="viridis")
ax[1, 1].set_title("Hough CI")
fig.colorbar(im, ax=ax[1, 1], shrink=0.8)
for a in ax.ravel():
    a.set_xticks([]), a.set_yticks([])
plt.tight_layout()
plt.savefig(OUT / "di_quality_maps.png", dpi=130)

ckey = plot.IPFColorKeyTSL(symmetry.Oh)
fig, ax = plt.subplots(2, 1, figsize=(14, 4.6))
ax[0].imshow(ckey.orientation2color(O_h).reshape(N_ROWS, N_COLS, 3))
ax[0].set_title("IPF-Z, Hough")
ax[1].imshow(ckey.orientation2color(O_d).reshape(N_ROWS, N_COLS, 3))
ax[1].set_title("IPF-Z, dictionary indexing + refinement")
for a in ax:
    a.set_xticks([]), a.set_yticks([])
plt.tight_layout()
plt.savefig(OUT / "ipf_hough_vs_di.png", dpi=130)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].hist(ncc_al_di, bins=80, alpha=0.6, label="DI (2.5 deg dictionary)")
ax[0].hist(ncc_al, bins=80, alpha=0.6, label="after refinement")
ax[0].set_xlabel("NCC"), ax[0].legend(), ax[0].set_title("Al: match quality")
ax[1].hist(ncc_al - ncc_si, bins=80, color="tab:green")
ax[1].axvline(0, color="k", lw=0.8)
ax[1].set_xlabel("NCC(Al) - NCC(Si)")
ax[1].set_title("phase discrimination: Al vs Si dictionaries")
plt.tight_layout()
plt.savefig(OUT / "ncc_histograms.png", dpi=130)

# example pattern: raw vs averaged vs best-match simulation
r, c = 10, 100
i = r * N_COLS + c
best_sim = al_mp.get_patterns(
    rotations=Rotation(g_di[i].data), detector=det, energy=20,
    compute=True, show_progressbar=False, dtype_out=np.float32,
).data[0]
fig, ax = plt.subplots(1, 4, figsize=(16, 4.2))
for a, (im_, t) in zip(ax, [
    (raw[r, c], "raw pattern (%d,%d)" % (r, c)),
    (corrected[r, c], "background-corrected"),
    (s.data[r, c], "+ neighbour averaging"),
    (best_sim, "best-match simulation\nNCC=%.2f" % ncc_al[i]),
]):
    a.imshow(im_, cmap="gray"), a.set_title(t), a.axis("off")
plt.tight_layout()
plt.savefig(OUT / "pattern_vs_simulation.png", dpi=130)

# ---------------------------------------------------------------- 8. export refined map
ang_path = OUT / "area2_slice_di_refined.ang"
io.save(str(ang_path), results["al"]["xmap_ref"], overwrite=True)
with open(ang_path, "rb") as f_in, gzip.open(str(ang_path) + ".gz", "wb") as f_out:
    shutil.copyfileobj(f_in, f_out)
ang_path.unlink()
