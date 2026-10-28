# Second-tool cross-check with HyperSpy/exspy: Gaussian-line model fits (polynomial background) of the
# measured spectra and of the DTSA-II Monte Carlo spectra of nominal C63000, then a matrix-matched
# quantification that uses the MC spectrum as a virtual standard:
#   C_X = C_X,nominal * (I_X / I_Cu)_measured / (I_X / I_Cu)_MC, normalized over Al, Fe, Ni, Cu.
# This shares no fitting code and no matrix correction with dtsa2_quant.py (only the physics in the MC).
# Usage: python exspy_crosscheck.py /tmp/nab-staging/files/eds
import os
import sys
import logging
import warnings
import numpy as np
import pandas as pd
import exspy

warnings.filterwarnings("ignore")
logging.getLogger("hyperspy").setLevel(logging.ERROR)
logging.getLogger("exspy").setLevel(logging.ERROR)
dataDir = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "outputs")
files = {10: "10kV 3_2nA_1.msa", 15: "15kV 3_2nA_1.msa", 20: "20kV 3_2 nA  USE THIS ONE_1.msa"}
cal = pd.read_csv(os.path.join(out, "energy_calibration.csv"), index_col="kV")
nominal = {"Al": 10.0, "Fe": 3.0, "Ni": 5.0, "Cu": 82.0}

rows = []
for kv, fname in files.items():
    sources = {"measured": os.path.join(dataDir, fname)}
    sources.update({g: os.path.join(os.environ.get("NAB_MC_DIR", os.path.join(out, "mc")), "%s_%dkV.msa" % (g, kv)) for g in ("bulk", "sphere25", "sphere50", "raster25")})
    for src, path in sources.items():
        lines = open(path, encoding="latin-1").read().splitlines()
        i0 = next(i for i, l in enumerate(lines) if l.startswith("#SPECTRUM"))
        vals = [l.split(",") for l in lines[i0 + 1:] if l.strip() and not l.startswith("#")]
        counts = np.array([float(v[1] if src == "measured" else v[0]) for v in vals])
        s = exspy.signals.EDSSEMSpectrum(counts)
        ax = s.axes_manager.signal_axes[0]
        ax.name, ax.units = "Energy", "keV"
        ax.scale = cal.loc[kv, "dtsa2_ch_width_eV"] / 1000
        ax.offset = (cal.loc[kv, "dtsa2_zero_offset_eV"] + 0.5 * cal.loc[kv, "dtsa2_ch_width_eV"]) / 1000
        s.set_microscope_parameters(beam_energy=kv, live_time=1.0, elevation_angle=36.03, azimuth_angle=0.0, tilt_stage=0.0,
                                    energy_resolution_MnKa=127.9)
        elements = ["Al", "Si", "Mn", "Fe", "Ni", "Cu"] + (["Zn", "W"] if kv > 10 else ["W"])
        s.add_elements(elements)
        lines_used = ["Al_Ka", "Si_Ka", "Mn_Ka", "Fe_Ka", "Ni_Ka", "Cu_Ka"] + (["Zn_Ka", "W_La"] if kv > 10 else ["W_Ma"])
        s.add_lines(lines_used)
        hi = min(kv - 0.3, 10.4)
        sc = s.isig[1.25:hi]
        m = sc.create_model(auto_background=False, auto_add_lines=True)
        m.add_polynomial_background(order=6)
        m.fit(bounded=True)
        m.calibrate_energy_axis(calibrate="resolution")
        m.fit(bounded=True)
        for comp in m:
            if comp.name in lines_used:
                rows.append(dict(kV=kv, source=src, line=comp.name, intensity=comp.A.value,
                                 sigma=comp.A.std if comp.A.std is not None else np.nan))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(out, "exspy_intensities.csv"), index=False)

# Matrix-matched quantification against each MC geometry used as the standard
q = []
for kv in files:
    meas = df[(df.kV == kv) & (df.source == "measured")].set_index("line")
    for std in ("bulk", "sphere25", "raster25"):
        mc = df[(df.kV == kv) & (df.source == std)].set_index("line")
        raw = {}
        for el in nominal:
            line = el + "_Ka"
            r_meas = meas.loc[line, "intensity"] / meas.loc["Cu_Ka", "intensity"]
            r_mc = mc.loc[line, "intensity"] / mc.loc["Cu_Ka", "intensity"]
            rel = np.hypot(meas.loc[line, "sigma"] / meas.loc[line, "intensity"], meas.loc["Cu_Ka", "sigma"] / meas.loc["Cu_Ka", "intensity"]) if el != "Cu" else 0.0
            raw[el] = (nominal[el] * r_meas / r_mc, rel)
        tot = sum(v[0] for v in raw.values())
        for el, (v, rel) in raw.items():
            q.append(dict(kV=kv, mc_standard=std, element=el, wt_pct=100 * v / tot, sigma_counting=100 * v / tot * rel))
q = pd.DataFrame(q)
q.round(3).to_csv(os.path.join(out, "exspy_mc_standard_quant.csv"), index=False)
print(df.pivot_table(index=["kV", "line"], columns="source", values="intensity").round(1).to_string())
print(q.pivot_table(index=["kV", "element"], columns="mc_standard", values="wt_pct").round(2).to_string())
