"""DREAM3D-NX (simplnx) grain reconstruction parameter sweeps on the Area 2 map.

Input: example/area2-results/area2_full.ang (gunzip area2_full.ang.gz first).
The kikuchipy .ang writer zeroed the CI/IQ columns, so the pre-segmentation
quality filter gates on the pattern fit column (degrees; lower is better).

Run inside the conda env:
  conda create -y -n nx -c bluequartzsoftware -c conda-forge python=3.12 dream3dnx numpy matplotlib-base
  conda run -n nx python scripts/dream3dnx_grain_reconstruction.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import simplnx as nx
import orientationanalysis as oa

ANG = Path("example/area2-results/area2_full.ang")
OUT = Path("example/area2-results/grain-reconstruction")
OUT.mkdir(parents=True, exist_ok=True)

GEOM = nx.DataPath("Geom")
CELL = "Geom/Cell Data/"
STEP_UM = 2.0  # map step size -> each pixel is 2x2 um


def reconstruct(mis_tol=5.0, min_size=10, fit_max=1.4, erode_iters=0, fill_defect=0):
    """One DREAM3D-NX reconstruction; returns the FeatureIds image and stats."""
    ds = nx.DataStructure()

    # 1. Read orientations from the .ang produced by the kikuchipy Hough run
    oa.ReadAngDataFilter.execute(
        data_structure=ds, input_file=str(ANG), output_image_geometry_path=GEOM)

    # 2. Pre-segmentation quality filter: keep pixels with fit < fit_max (deg)
    if fit_max is not None:
        t = nx.ArrayThreshold()
        t.array_path = nx.DataPath(CELL + "Fit")
        t.comparison = nx.ArrayThreshold.ComparisonType.LessThan
        t.value = fit_max
        ts = nx.ArrayThresholdSet()
        ts.thresholds = [t]
        nx.MultiThresholdObjectsFilter.execute(
            data_structure=ds, array_thresholds_object=ts,
            created_mask_type=nx.DataType.boolean, output_data_array_name="Mask")

    # 3. Euler angles -> quaternions (what the segmenter compares)
    oa.ConvertOrientationsFilter.execute(
        data_structure=ds,
        input_orientation_array_path=nx.DataPath(CELL + "EulerAngles"),
        input_representation_index=0,  # Euler
        output_orientation_array_name="Quats",
        output_representation_index=2)  # Quaternion

    # 4. Grain segmentation: flood-fill, boundary = misorientation > mis_tol
    res = oa.EBSDSegmentFeaturesFilter.execute(
        data_structure=ds,
        input_image_geometry_path=GEOM,
        cell_quats_array_path=nx.DataPath(CELL + "Quats"),
        cell_phases_array_path=nx.DataPath(CELL + "Phases"),
        crystal_structures_array_path=nx.DataPath("Geom/Cell Ensemble Data/CrystalStructures"),
        cell_mask_array_path=nx.DataPath(CELL + "Mask"),
        use_mask=fit_max is not None,
        misorientation_tolerance=mis_tol,
        randomize_features=True)

    assert not res.errors, res.errors
    fids_path = nx.DataPath(CELL + "FeatureIds")
    n_raw_grains = int(ds[fids_path].store.npview().max())

    # 5. Minimum-points-per-grain cutoff (needs NumElements per feature first)
    if min_size > 1:
        nx.ComputeFeatureSizesFilter.execute(
            data_structure=ds, input_image_geometry_path=GEOM,
            feature_ids_path=fids_path,
            feature_attribute_matrix_path=nx.DataPath("Geom/Cell Feature Data"))
        res = nx.RequireMinimumSizeFeaturesFilter.execute(
            data_structure=ds, input_image_geometry_path=GEOM,
            feature_ids_path=fids_path,
            num_cells_path=nx.DataPath("Geom/Cell Feature Data/NumElements"),
            min_allowed_features_size=min_size)
        assert not res.errors, res.errors  # errors at e.g. cutoff > largest grain

    unassigned_before_cleanup = float(
        (ds[fids_path].store.npview() == 0).mean())

    # 6. Cleanup: erode bad data (operation_index 1) grows grains into holes;
    #    FillBadData replaces enclosed hole regions smaller than fill_defect px
    if erode_iters > 0:
        nx.ErodeDilateBadDataFilter.execute(
            data_structure=ds, input_image_geometry_path=GEOM,
            feature_ids_path=fids_path,
            num_iterations=erode_iters, operation_index=1)
    if fill_defect > 0:
        nx.FillBadDataFilter.execute(
            data_structure=ds, input_image_geometry_path=GEOM,
            feature_ids_path=fids_path,
            cell_phases_array_path=nx.DataPath(CELL + "Phases"),
            min_allowed_defect_size=fill_defect)

    fids = ds[fids_path].store.npview()[0, :, :, 0].copy()

    sizes_px = np.bincount(fids.ravel())[1:]  # id 0 = unassigned
    sizes_px = sizes_px[sizes_px > 0]
    eq_diam_um = 2.0 * np.sqrt(sizes_px * STEP_UM**2 / np.pi)
    stats = {
        "n_raw_grains": n_raw_grains,
        "n_grains": int(sizes_px.size),
        "retained_frac": float((fids > 0).mean()),
        "cleanup_altered_frac": float(unassigned_before_cleanup - (fids == 0).mean()),
        "mean_diam_um": float(eq_diam_um.mean()),
        "area_weighted_mean_diam_um": float((sizes_px * eq_diam_um).sum() / sizes_px.sum()),
        "speckle_grain_frac": float((sizes_px < 10).mean()),
        "largest_grain_px": int(sizes_px.max()),
    }
    return fids, stats


def render(panels, fname, suptitle):
    """panels: list of (featureIds image, title)."""
    rng = np.random.default_rng(7)
    fig, axes = plt.subplots(1, len(panels), figsize=(3.1 * len(panels), 7.5))
    for ax, (fids, title) in zip(np.atleast_1d(axes), panels):
        colors = rng.uniform(0.15, 1.0, (fids.max() + 1, 3))
        colors[0] = 0.0  # unassigned pixels = black
        ax.imshow(colors[fids], interpolation="nearest")
        ax.set_title(title, fontsize=9)
        ax.set_xticks([]), ax.set_yticks([])
    fig.suptitle(suptitle, fontsize=11, y=0.995)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT / fname, dpi=150)
    plt.close(fig)


CONFIGS = {
    # baseline
    "baseline": dict(mis_tol=5.0, min_size=10, fit_max=1.4),
    # A: misorientation threshold defining a boundary
    "tol_1deg": dict(mis_tol=1.0, min_size=10, fit_max=1.4),
    "tol_2deg": dict(mis_tol=2.0, min_size=10, fit_max=1.4),
    "tol_15deg": dict(mis_tol=15.0, min_size=10, fit_max=1.4),
    # B: minimum-points-per-grain cutoff
    "min_1px": dict(mis_tol=5.0, min_size=1, fit_max=1.4),
    "min_100px": dict(mis_tol=5.0, min_size=100, fit_max=1.4),
    # note: cutoffs above the largest raw feature (493 px) error out and no-op
    "min_400px": dict(mis_tol=5.0, min_size=400, fit_max=1.4),
    # C: pre-segmentation quality filter (pattern fit, degrees)
    "filter_none": dict(mis_tol=5.0, min_size=10, fit_max=None),
    "filter_strict": dict(mis_tol=5.0, min_size=10, fit_max=0.5),
    # D: cleanup passes on the strict-filter map (half the pixels are holes)
    "strict_erode2": dict(mis_tol=5.0, min_size=10, fit_max=0.5, erode_iters=2),
    "strict_erode10": dict(mis_tol=5.0, min_size=10, fit_max=0.5, erode_iters=10),
    "strict_fill": dict(mis_tol=5.0, min_size=10, fit_max=0.5, fill_defect=1000),
    # worse-then-better demonstration
    "worst": dict(mis_tol=1.0, min_size=1, fit_max=None),
    "recovered": dict(mis_tol=5.0, min_size=10, fit_max=1.4, erode_iters=2),
}

results, images = {}, {}
for name, cfg in CONFIGS.items():
    fids, stats = reconstruct(**cfg)
    results[name] = {"config": {k: (v if v is not None else "off") for k, v in cfg.items()}, **stats}
    images[name] = fids
    print(f"{name:16s} grains={stats['n_grains']:6d} retained={stats['retained_frac']:.3f} "
          f"mean_d={stats['mean_diam_um']:.1f}um speckle={stats['speckle_grain_frac']:.2f}")

with open(OUT / "stats.json", "w") as f:
    json.dump(results, f, indent=2)


def title(name, label):
    s = results[name]
    return (f"{label}\n{s['n_raw_grains']:,} raw / {s['n_grains']:,} kept grains\n"
            f"retained {s['retained_frac']:.0%} | mean {s['mean_diam_um']:.1f} um | "
            f"AW {s['area_weighted_mean_diam_um']:.0f} um")


render([(images[n], title(n, l)) for n, l in
        [("tol_1deg", "1 deg"), ("tol_2deg", "2 deg"), ("baseline", "5 deg (baseline)"), ("tol_15deg", "15 deg")]],
       "sweep_misorientation_tolerance.png",
       "Misorientation tolerance (min 10 px, fit < 1.4 deg, no cleanup)")

render([(images[n], title(n, l)) for n, l in
        [("min_1px", "1 px (off)"), ("baseline", "10 px (baseline)"), ("min_100px", "100 px"), ("min_400px", "400 px")]],
       "sweep_min_grain_size.png",
       "Minimum-points-per-grain cutoff (5 deg, fit < 1.4 deg, no cleanup)")

render([(images[n], title(n, l)) for n, l in
        [("filter_none", "no filter"), ("baseline", "fit < 1.4 deg (baseline)"), ("filter_strict", "fit < 0.5 deg")]],
       "sweep_quality_filter.png",
       "Pre-segmentation quality filter (5 deg, min 10 px, no cleanup)")

render([(images[n], title(n, l)) for n, l in
        [("filter_strict", "no cleanup"), ("strict_erode2", "erode bad data x2"),
         ("strict_erode10", "erode bad data x10"), ("strict_fill", "fill defects < 1000 px")]],
       "sweep_cleanup.png",
       "Cleanup passes on the fit < 0.5 deg map (49% of pixels start as holes)")

render([(images[n], title(n, l)) for n, l in
        [("worst", "WORST: 1 deg, no min size,\nno filter, no cleanup"),
         ("baseline", "baseline: 5 deg, min 10 px,\nfit < 1.4 deg"),
         ("recovered", "recovered: baseline\n+ erode bad data x2")]],
       "worse_then_better.png",
       "Deliberately degraded vs recovered reconstruction")

print("done ->", OUT)
