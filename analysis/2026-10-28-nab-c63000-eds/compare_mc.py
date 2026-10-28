# Compare the measured spectra with the DTSA-II Monte Carlo spectra of nominal C63000 (bulk, spheres
# on carbon, raster over a sphere), line by line, and draw the summary figures.
# Inputs: outputs/dtsa2_kratios.csv, outputs/dtsa2_quant.csv,
#         outputs/exspy_mc_standard_quant.csv, outputs/mc/*.msa and the measured .msa files.
# Usage: python compare_mc.py /tmp/nab-staging/files/eds
import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

dataDir = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "outputs")
files = {10: "10kV 3_2nA_1.msa", 15: "15kV 3_2nA_1.msa", 20: "20kV 3_2 nA  USE THIS ONE_1.msa"}
geoms = ["bulk", "sphere25", "sphere50", "raster25"]
geomLabel = {"measured": "measured", "bulk": "MC flat bulk", "sphere25": "MC 50 um sphere, top", "sphere50": "MC 100 um sphere, top",
             "raster25": "MC 50 um sphere, raster"}
rois = {"Al K": "Al All", "Mn Ka": "Mn Kα", "Fe Ka": "Fe Kα", "Ni Ka": "Ni Kα", "Cu Ka": "Cu Kα",
        "Fe L": "Fe L-family", "Ni L": "Ni L-family", "Cu L": "Cu L-family", "C K": "C K-L2", "O K": "O All"}

k = pd.read_csv(os.path.join(out, "dtsa2_kratios.csv")).rename(columns={"source": "geometry"})
k = k[k.transition_set.isin(rois.values())]
k["line"] = k.transition_set.map({v: n for n, v in rois.items()})
kt = k.pivot_table(index=["kV", "geometry"], columns="line", values="k")
kt.round(5).to_csv(os.path.join(out, "kratios_measured_vs_mc.csv"))

# Ratios of k-ratios (each k is relative to the same simulated pure-element standard, so detector efficiency
# and dose cancel): low-energy lines against K lines, and the absolute Cu Ka intensity against MC bulk.
ratios = pd.DataFrame({"Al K / Cu Ka": kt["Al K"] / kt["Cu Ka"], "Cu L / Cu Ka": kt["Cu L"] / kt["Cu Ka"],
                       "Ni L / Ni Ka": kt["Ni L"] / kt["Ni Ka"], "Fe L / Fe Ka": kt["Fe L"] / kt["Fe Ka"],
                       "Al K / Cu L": kt["Al K"] / kt["Cu L"], "Fe Ka / Cu Ka": kt["Fe Ka"] / kt["Cu Ka"],
                       "Ni Ka / Cu Ka": kt["Ni Ka"] / kt["Cu Ka"]})
ratios["Cu Ka vs MC bulk"] = kt["Cu Ka"] / kt.xs("bulk", level="geometry")["Cu Ka"].reindex(kt.index.get_level_values(0)).values
ratios.round(4).to_csv(os.path.join(out, "line_ratios.csv"))
rel = ratios.copy()
for kv in files:
    for g in rel.loc[kv].index:
        rel.loc[(kv, g)] = ratios.loc[(kv, g)] / ratios.loc[(kv, "bulk")]
rel.round(3).to_csv(os.path.join(out, "line_ratios_relative_to_mc_bulk.csv"))
print(ratios.round(4).to_string(), "\n", rel.round(3).to_string())


def read_msa(path, measured):
    lines = open(path, encoding="latin-1").read().splitlines()
    i0 = next(i for i, l in enumerate(lines) if l.startswith("#SPECTRUM"))
    vals = [l.split(",") for l in lines[i0 + 1:] if l.strip() and not l.startswith("#")]
    return np.array([float(v[1] if measured else v[0]) for v in vals])


cal = pd.read_csv(os.path.join(out, "energy_calibration.csv"), index_col="kV")
spec = {}
for kv, f in files.items():
    e = (cal.loc[kv, "dtsa2_zero_offset_eV"] + (np.arange(4096) + 0.5) * cal.loc[kv, "dtsa2_ch_width_eV"]) / 1000
    spec[(kv, "measured")] = (e, read_msa(os.path.join(dataDir, f), True))
    for g in geoms:
        spec[(kv, g)] = (e, read_msa(os.path.join(out, "mc", "%s_%dkV.msa" % (g, kv)), False))


def cu_ka_net(e, c):
    m = (e > 7.93) & (e < 8.16)
    side = ((e > 7.75) & (e < 7.85)) | ((e > 8.55) & (e < 8.65))
    return c[m].sum() - np.polyval(np.polyfit(e[side], c[side], 1), e[m]).sum()


ink, c1, c2, c3 = "#0b0b0b", "#2a78d6", "#eb6834", "#1baf7a"
gcol = {"measured": ink, "bulk": c1, "raster25": c2, "sphere25": c3}
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})

# Spectra of every voltage, scaled to the same Cu Ka net counts, so L lines and Al K read against Cu Ka
fig, axs = plt.subplots(3, 2, figsize=(12, 10.5), layout="constrained", gridspec_kw={"width_ratios": [1.3, 1]})
for i, kv in enumerate(files):
    ref = cu_ka_net(*spec[(kv, "measured")])
    for j, (lo, hi) in enumerate([(0.15, 2.2), (5.6, 9.4)]):
        ax = axs[i, j]
        for g in ("bulk", "raster25", "sphere25", "measured"):
            e, c = spec[(kv, g)]
            m = (e > lo) & (e < hi)
            ax.semilogy(e[m], np.maximum(c[m] * ref / cu_ka_net(e, c), 0.5), lw=0.9 if g == "measured" else 1.2,
                        color=gcol[g], label=geomLabel[g], alpha=1 if g == "measured" else 0.85)
        ax.set(xlim=(lo, hi), title="%d kV, scaled to equal Cu Ka" % kv, xlabel="Energy (keV)")
        if j == 0:
            ax.set_ylabel("counts per 5 eV")
fig.legend(*axs[0, 0].get_legend_handles_labels(), loc="outside upper center", ncol=4, frameon=False)
fig.savefig(os.path.join(here, "figures", "mc_vs_measured_spectra.png"), dpi=120)

# Main summary figure
q = pd.read_csv(os.path.join(out, "dtsa2_quant.csv"))
x = pd.read_csv(os.path.join(out, "exspy_mc_standard_quant.csv"))
spec_range = {"Al": (9.0, 11.0), "Fe": (2.0, 4.0), "Ni": (4.0, 5.5), "Cu": None, "Mn": (0.0, 1.5)}
nominal = {"Al": 10.0, "Fe": 3.0, "Ni": 5.0, "Cu": 82.0, "Mn": None}
fig = plt.figure(figsize=(13, 8.6), layout="constrained")
gs = fig.add_gridspec(2, 5, height_ratios=[1.15, 1])
ax = fig.add_subplot(gs[0, :3])
ref = cu_ka_net(*spec[(20, "measured")])
for g in ("bulk", "raster25", "measured"):
    e, c = spec[(20, g)]
    m = (e > 0.15) & (e < 10)
    ax.semilogy(e[m], np.maximum(c[m] * ref / cu_ka_net(e, c), 0.5), lw=0.8 if g == "measured" else 1.1, color=gcol[g], label=geomLabel[g])
for n, xx in {"C K": 0.277, "O K": 0.525, "Cu L": 0.93, "Al K": 1.487, "Fe Ka": 6.404, "Ni Ka": 7.478, "Cu Ka": 8.048, "Cu Kb": 8.905}.items():
    ax.text(xx, 1.6e5, n, rotation=90, fontsize=7, ha="center", va="top", color="0.3")
ax.set(xlim=(0.15, 10), ylim=(20, 2e5), xlabel="Energy (keV)", ylabel="counts per 5 eV (MC scaled to measured Cu Ka)",
       title="A. 20 kV: measured vs DTSA-II Monte Carlo of nominal C63000")
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.24, 0.86))
ax = fig.add_subplot(gs[0, 3:])
show = ["Al K / Cu Ka", "Cu L / Cu Ka", "Ni L / Ni Ka"]
for ii, r in enumerate(show):
    for g, ls, mkr in (("measured", "-", "o"), ("raster25", ":", "s")):
        yv = [rel.loc[(kv, g), r] for kv in files]
        ax.plot(np.array(list(files)) + (ii - 1) * 0.3, yv, marker=mkr, ls=ls, lw=1.2, color=[c1, c2, c3][ii], markersize=6,
                markerfacecolor="white" if g != "measured" else [c1, c2, c3][ii], label=r if g == "measured" else None)
ax.axhline(1, color="0.6", lw=0.8)
ax.set(xticks=list(files), xlabel="Beam energy (kV)", ylabel="ratio / same ratio in MC flat bulk",
       title="B. Low-energy line vs K line, relative to flat bulk")
h1 = ax.legend(frameon=False, loc="upper left", fontsize=8)
ax.add_artist(h1)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], color="0.3", marker="o", ls="-", label="measured"),
                   Line2D([], [], color="0.3", marker="s", ls=":", markerfacecolor="white", label="MC raster, 50 um sphere")],
          frameon=False, loc="lower right", fontsize=8)
for j, el in enumerate(["Al", "Fe", "Ni", "Cu", "Mn"]):
    ax = fig.add_subplot(gs[1, j])
    if spec_range[el] is not None:
        ax.axhspan(*spec_range[el], color="0.9", zorder=0, label="C63000 limits")
    if nominal[el] is not None:
        ax.axhline(nominal[el], color="0.45", lw=1, ls="--", label="nominal")
    cats, vals, errs, cols = [], [], [], []
    for kv in files:
        r = q[(q.kV == kv) & (q.source == "measured") & (q.line_set == "K") & (q.element == el)]
        if len(r):
            cats.append("%d kV" % kv)
            vals.append(r.wt_pct_norm.iloc[0])
            errs.append(r.wt_pct_norm_sigma.iloc[0])
            cols.append(c1)
    for std, lab in (("bulk", "MC\nbulk"), ("raster25", "MC\nraster")):
        r = x[(x.kV == 20) & (x.mc_standard == std) & (x.element == el)]
        if len(r):
            cats.append(lab)
            vals.append(r.wt_pct.iloc[0])
            errs.append(r.sigma_counting.iloc[0])
            cols.append(c2)
    xs = np.arange(len(cats))
    for xi, v, er, cc in zip(xs, vals, errs, cols):
        ax.errorbar(xi, v, yerr=er, fmt="o", color=cc, ms=6, capsize=3, lw=1.2)
    ax.set_xticks(xs, cats, fontsize=7)
    ax.set_xlim(-0.6, len(cats) - 0.4)
    ax.set_title(("C. " if j == 0 else "") + "%s (wt%%)%s" % (el, ", balance" if el == "Cu" else ""))
    if j == 0:
        ax.set_ylabel("wt%, normalized to 100% metals")
        ax.errorbar([], [], yerr=[], fmt="o", color=c1, label="DTSA-II, simulated stds (1 sigma)")
        ax.errorbar([], [], yerr=[], fmt="o", color=c2, label="exspy, MC spectrum as std, 20 kV")
        ax.set_ylim(5, 13.5)
        ax.legend(frameon=False, fontsize=7, loc="upper left")
fig.savefig(os.path.join(here, "figures", "summary.png"), dpi=130)
