"""Pure-Python (kinematical) vs EMsoft (dynamical) master patterns for Al.

Computes a kinematical EBSD master pattern for fcc Al entirely in Python
(kikuchipy + diffsims, no Fortran), downloads the EMsoft-simulated dynamical
master pattern from Zenodo, and compares both on the sphere and projected
onto the Area 2 detector geometry for the same orientation.

Run: python scripts/master_pattern_python_test.py
Requires: pip install kikuchipy diffsims matplotlib
"""

import time

import matplotlib.pyplot as plt
import numpy as np
from diffpy.structure import Atom, Lattice, Structure
from diffsims.crystallography import ReciprocalLatticeVector
from orix.crystal_map import Phase
from orix.quaternion import Rotation
import kikuchipy as kp

OUT_DIR = "example/area2-results/master-pattern-comparison"

# --- Kinematical master pattern, pure Python -------------------------------
phase = Phase(
    name="al",
    space_group=225,
    structure=Structure(
        atoms=[Atom("Al", [0, 0, 0])],
        lattice=Lattice(4.05, 4.05, 4.05, 90, 90, 90),
    ),
)
t0 = time.time()
ref = ReciprocalLatticeVector.from_min_dspacing(phase, 0.7)
ref.sanitise_phase()
ref.calculate_structure_factor()
ref.calculate_theta(20e3)
simulator = kp.simulations.KikuchiPatternSimulator(ref)
mp_kin = simulator.calculate_master_pattern(half_size=200, hemisphere="upper")
t_kin = time.time() - t0
print(f"Kinematical master pattern: {ref.size} reflectors, {t_kin:.1f} s")

# --- Dynamical master pattern, EMsoft via Zenodo ---------------------------
mp_dyn = kp.data.ebsd_master_pattern(
    "al", allow_download=True, projection="stereographic", energy=20,
    hemisphere="upper",
)

# --- Project both onto the Area 2 detector for one orientation -------------
det = kp.detectors.EBSDDetector(
    (111, 111), sample_tilt=70.0, pc=(0.518, 0.336, 0.753), convention="edax",
)
rot = Rotation.from_euler(np.deg2rad([30, 45, 60]))

mp_dyn_lam = kp.data.ebsd_master_pattern(
    "al", allow_download=True, projection="lambert", energy=20,
    hemisphere="upper",
)
mp_dyn_lam.phase = phase
pat_dyn = mp_dyn_lam.get_patterns(rot, det, energy=20, compute=True)

mp_kin_lam = mp_kin.as_lambert()
mp_kin_lam.phase = phase
pat_kin = mp_kin_lam.get_patterns(rot, det, energy=20, compute=True)

# --- Figure ----------------------------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(16, 4.4))
panels = [
    (mp_dyn.data, "Dynamical master pattern\n(EMsoft, Zenodo download)"),
    (mp_kin.data, f"Kinematical master pattern\n(pure Python, {t_kin:.0f} s)"),
    (pat_dyn.data.squeeze(), "Detector pattern, dynamical\n(Area 2 geometry)"),
    (pat_kin.data.squeeze(), "Detector pattern, kinematical\n(same orientation)"),
]
for ax, (img, title) in zip(axes, panels):
    ax.imshow(img, cmap="gray")
    ax.set_title(title, fontsize=10)
    ax.axis("off")
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/kinematical_vs_dynamical_al.png", dpi=150,
            bbox_inches="tight")
print(f"Saved {OUT_DIR}/kinematical_vs_dynamical_al.png")
