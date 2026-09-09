# Demonstrates the eXSpy workflow for the AlSi10Mg trace-Mg problem:
# a synthetic 20 kV SEM-EDS spectrum with a true Mg content of 0.5 wt%,
# quantified three ways (naive window sum, background-corrected windows,
# model fit), plus the Currie 3-sigma detection test for the Mg K-alpha peak.
# Swap `synthetic_AlSi10Mg.msa` for a real exported .msa to reuse on session data.

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import hyperspy.api as hs

rng = np.random.default_rng(42)

# --- synthesize the spectrum: 10 eV channels, 0-20 keV, 20 kV beam ---
E = np.arange(0.0, 20.0, 0.01) + 0.005
E0 = 20.0

# SDD peak width vs energy: FWHM^2 grows linearly from 130 eV at Mn Ka
fwhm = np.sqrt(0.130**2 + 0.0025 * (E - 5.8987))
sigma = fwhm / 2.355

# bremsstrahlung continuum (Kramers) with soft-X-ray absorption roll-off
bg = 60.0 * np.clip(E0 - E, 0, None) / np.clip(E, 0.1, None) * (1 - np.exp(-E / 0.35))

# peak areas scaled to composition: Al 89.5 / Si 10 / Mg 0.5 wt%
lines = {"Al_Ka": (1.4865, 895_000), "Si_Ka": (1.7398, 100_000), "Mg_Ka": (1.2536, 5_000)}
model_counts = bg.copy()
for center, area in lines.values():
    s_line = np.interp(center, E, sigma)
    model_counts += area * np.exp(-((E - center) ** 2) / (2 * s_line**2)) / (s_line * np.sqrt(2 * np.pi)) * 0.01

data = rng.poisson(model_counts).astype(float)

s = hs.signals.Signal1D(data)
s.set_signal_type("EDS_SEM")
ax = s.axes_manager[0]
ax.name, ax.units, ax.scale, ax.offset = "Energy", "keV", 0.01, 0.005
s.set_microscope_parameters(beam_energy=20.0, live_time=60.0, energy_resolution_MnKa=130.0)
s.add_elements(["Al", "Si", "Mg"])
s.add_lines()
s.metadata.General.title = "Synthetic AlSi10Mg (true Mg = 0.5 wt%)"

s.save("scripts/synthetic_AlSi10Mg.msa", overwrite=True)
s = hs.load("scripts/synthetic_AlSi10Mg.msa", signal_type="EDS_SEM")
s.add_elements(["Al", "Si", "Mg"])
s.add_lines()

# Poisson weighting: without it the fit only "cares" about the huge Al/Si
# peaks and the trace Mg line is at the mercy of the background polynomial
v = s.deepcopy()
v.data = np.maximum(s.data, 1.0)
s.set_noise_variance(v)

# --- method 1: naive window sum (what inflates trace Mg) ---
naive = [i.data.item() for i in s.get_lines_intensity(background_windows=None)]

# --- method 2: window sum with interpolated background subtraction ---
bw = s.estimate_background_windows(line_width=[5.0, 7.0])
windowed = [i.data.item() for i in s.get_lines_intensity(background_windows=bw)]

# --- method 3: full model fit (background + Gaussian families, deconvolved) ---
m = s.create_model()
m.fit_background()
m.fit()
fitted = [i.data.item() for i in m.get_lines_intensity()]

line_names = [i.metadata.Sample.xray_lines[0] for i in s.get_lines_intensity()]
true_areas = {k: v[1] for k, v in lines.items()}
print(f"{'line':<8}{'true':>10}{'naive':>12}{'bg-window':>12}{'model fit':>12}")
for name, n, w, f in zip(line_names, naive, windowed, fitted):
    print(f"{name:<8}{true_areas[name]:>10}{n:>12.0f}{w:>12.0f}{f:>12.0f}")

for label, vals in [("naive", naive), ("bg-window", windowed), ("model fit", fitted)]:
    mg_frac = vals[line_names.index("Mg_Ka")] / sum(vals)
    print(f"apparent Mg intensity fraction ({label}): {100 * mg_frac:.2f}%")
print("true Mg intensity fraction: 0.50%")

# --- Currie detection test: is the Mg peak real? ---
mg_E, mg_fwhm = 1.2536, np.interp(1.2536, E, fwhm)
window = (E > mg_E - mg_fwhm) & (E < mg_E + mg_fwhm)  # 2*FWHM integration window
bg_component = m["background_order_6"]
B = bg_component.function(E[window]).sum() * 0.01  # function() is counts/keV; x0.01 keV channel width
N_net = fitted[line_names.index("Mg_Ka")]
L_C = 2.33 * np.sqrt(B)  # decision limit ("is anything there?")
L_D = 2.71 + 4.65 * np.sqrt(B)  # detection limit for experiment design
print(f"\nbackground under Mg Ka (2xFWHM window): B = {B:.0f} counts")
print(f"Currie decision limit L_C = 2.33*sqrt(B) = {L_C:.0f} counts")
print(f"Currie detection limit L_D = 2.71 + 4.65*sqrt(B) = {L_D:.0f} counts")
print(f"net Mg Ka counts from model fit: {N_net:.0f} -> "
      f"{'DETECTED' if N_net > L_C else 'not detected'} ({N_net / np.sqrt(B):.0f} sigma above background)")

# --- figure: full spectrum + zoom on the Mg/Al/Si region ---
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.5))
a1.semilogy(E, data, lw=0.5, color="#555")
a1.set(xlabel="Energy (keV)", ylabel="Counts / 10 eV", title="Synthetic AlSi10Mg, 20 kV, 60 s live", xlim=(0, 12))

zoom = (E > 0.8) & (E < 2.4)
a2.plot(E[zoom], data[zoom], ".", ms=2, color="#999", label="data")
a2.plot(E[zoom], m.as_signal().data[zoom], color="C3", label="model fit")
a2.plot(E[zoom], bg_component.function(E[zoom]) * 0.01, "--", color="C0", label="fitted background")
for name, (center, _) in lines.items():
    a2.axvline(center, color="k", lw=0.5, alpha=0.3)
    a2.annotate(name.replace("_", " "), (center, a2.get_ylim()[1]), ha="center", fontsize=8)
a2.set_yscale("log")
a2.set(xlabel="Energy (keV)", ylabel="Counts / 10 eV", title="Mg Ka sits on the Al Ka shoulder + continuum")
a2.legend(loc="upper right")
fig.tight_layout()
fig.savefig("scripts/eds_mg_quant_demo.png", dpi=150)
print("\nwrote scripts/eds_mg_quant_demo.png")
