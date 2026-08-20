# Calibrated k-factor quantification of a real AlSi10Mg SEM-EDS sum spectrum
# (Apreo SEM, EDAX Octane Plus, 5 kV, live time 327.7 s, takeoff 35.1 deg).
#
# k-factors are sensitivity factors valid ONLY for the exact acquisition
# conditions (kV, detector, geometry), the exact fitting procedure that
# produced the calibration intensities, AND compositions near the calibrant:
# on a bulk sample they embed its matrix (ZAF) effects, which change with
# composition, and eXSpy has no bulk matrix correction (quantification() is
# TEM-only; no ZAF/phi-rho-z). Calibrate them once against a spectrum of
# KNOWN composition, then reuse on other spectra measured the same way.
# Replace KNOWN_WT with certified-standard values for standards-based numbers;
# the vendor eZAF result is used here only as a placeholder reference.
import numpy as np
import matplotlib.pyplot as plt
import hyperspy.api as hs

CSV = "scripts/AlSi10Mg_EDS_Map_1.csv"
BEAM_KV, LIVE_TIME, TAKEOFF, RES_MNKA = 5.0, 327.7, 35.1, 127.9
ELEMENTS = ["Al", "C", "Mg", "O", "Si"]
# calibration composition for the SAME spectrum (EDAX eZAF, Report.pdf p.5)
KNOWN_WT = {"Al_Ka": 84.24, "C_Ka": 1.99, "Mg_Ka": 0.94, "O_Ka": 1.68, "Si_Ka": 11.15}

data = np.loadtxt(CSV, delimiter=",")
s = hs.signals.Signal1D(data[:, 1])
s.set_signal_type("EDS_SEM")
ax = s.axes_manager.signal_axes[0]
ax.name, ax.units, ax.scale, ax.offset = "Energy", "keV", data[1, 0] - data[0, 0], data[0, 0]
s.set_microscope_parameters(
    beam_energy=BEAM_KV, live_time=LIVE_TIME, elevation_angle=TAKEOFF,
    energy_resolution_MnKa=RES_MNKA,
)
s.add_elements(ELEMENTS)
s.add_lines()

# fit only the physical range: above the noise cutoff, below the Duane-Hunt limit (= beam kV)
s = s.isig[0.045:BEAM_KV]
s.estimate_poissonian_noise_variance()
variance = s.metadata.Signal.Noise_properties.variance
variance.data = np.clip(variance.data, 1, None)  # zero-count channels get infinite weight otherwise

m = s.create_model()
m.fit_background()
for c in m:
    if hasattr(c, "A"):
        c.A.bmin = 0.0  # forbid negative peak areas
m.fit(bounded=True)

fitted = m.get_lines_intensity()
counts = {f.metadata.Sample.xray_lines[0]: float(f.data.sum()) for f in fitted}

# component curves evaluated through the model's own path (component.function()
# evaluates against a different internal axis normalisation and gives wrong values)
for c in m:
    c.active = "background" in c.name
background = m.as_signal().data
for c in m:
    c.active = "background" in c.name or c.name == "Mg_Ka"
mg_curve = m.as_signal().data
for c in m:
    c.active = True

# Currie detection check: net counts vs 3*sqrt(2B) with B taken +/- 1.2 FWHM around the line
energy = s.axes_manager.signal_axes[0].axis
for ln in counts:
    comp = m[ln]
    window = np.abs(energy - comp.centre.value) < 1.2 * comp.fwhm
    B = float(background[window].sum())
    print(f"{ln}: net={counts[ln]:9.0f}  bg_under_peak={B:8.0f}  "
          f"significance={counts[ln] / np.sqrt(2 * B):7.1f} sigma  "
          f"(detected: {counts[ln] > 3 * np.sqrt(2 * B)})")

# calibrate k-factors (relative to Al) from the known composition, then apply.
# On the calibration spectrum this reproduces KNOWN_WT by construction; the value
# is reusing these k-factors on OTHER spectra taken under identical conditions.
used = [ln for ln in counts if counts[ln] > 0]
k = {ln: KNOWN_WT[ln] / counts[ln] for ln in used}
k = {ln: v / k["Al_Ka"] for ln, v in k.items()}
print("\ncalibrated k-factors (Al=1):", {ln: round(v, 3) for ln, v in k.items()})

total = sum(k[ln] * counts[ln] for ln in used)
wt = {ln: 100 * k[ln] * counts[ln] / total for ln in used}
print("wt% =", {ln: round(v, 2) for ln, v in wt.items()})

fig, axp = plt.subplots(figsize=(9, 5))
axp.plot(energy, s.data, color="#6b6b6b", lw=1, drawstyle="steps-mid", label="measured")
axp.plot(energy, m.as_signal().data, color="#0072B2", lw=2, label="model fit")
axp.plot(energy, background, color="#009E73", lw=2, ls="--", label="background")
axp.fill_between(energy, background, mg_curve, color="#D55E00", alpha=0.6, label="Mg K$\\alpha$")
for ln in counts:
    comp = m[ln]
    peak_top = s.data[np.abs(energy - comp.centre.value).argmin()]
    axp.annotate(ln.replace("_Ka", ""), (comp.centre.value, peak_top * 1.35),
                 ha="center", fontsize=9, color="#404040")
axp.set(xlim=(0.1, 2.5), yscale="log", ylim=(50, 1e5),
        xlabel="Energy (keV)", ylabel="Counts per 5 eV channel",
        title="AlSi10Mg sum spectrum, 5 kV — eXSpy model fit")
axp.legend(frameon=False, loc="upper right")
axp.grid(alpha=0.25)
fig.tight_layout()
fig.savefig("scripts/eds_kfactor_quant.png", dpi=150)
