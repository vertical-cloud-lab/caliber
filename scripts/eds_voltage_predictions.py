"""Physics predictions for the AlSi10Mg 5/10/15/20 kV EDS voltage series (issue #1).

Independently recomputes the CALIBER voltage-selection criterion from PR #11
(slant X-ray production depth must not exceed the line's 1/e attenuation length,
equivalently f(chi) >~ 0.75 for every quantified line) and tabulates the
falsifiable predictions the microscope sessions will test.
"""

import csv

import numpy as np
import xraydb
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

COMP = {"Al": 0.895, "Si": 0.100, "Mg": 0.005}  # DIN EN 1706 nominal, wt fractions
RHO = 2.67  # g/cm3
PSI = np.radians(35.1)  # EDAX take-off angle used throughout the issue-1 thread
CSC = 1.0 / np.sin(PSI)
E0S = [5.0, 10.0, 15.0, 20.0]  # kV

A_BAR = sum(w * xraydb.atomic_mass(el) for el, w in COMP.items())
Z_BAR = sum(w * xraydb.atomic_number(el) for el, w in COMP.items())
KO = 0.0276 * A_BAR / (Z_BAR**0.89 * RHO)  # Kanaya-Okayama prefactor, um per keV^1.67
H_PHIL = 1.2 * A_BAR / Z_BAR**2  # Philibert h for the matrix

lines = {}
for el in ["O", "Mg", "Al", "Si", "Fe"]:
    e_line = xraydb.xray_lines(el)["Ka1"].energy / 1000.0  # keV
    e_c = xraydb.xray_edge(el, "K").energy / 1000.0  # critical excitation, keV
    mu = sum(w * xraydb.mu_elam(m, e_line * 1000.0) for m, w in COMP.items())  # cm2/g
    lam = 1e4 / (mu * RHO)  # 1/e attenuation length in the alloy, um
    lines[f"{el} Ka"] = (e_line, e_c, mu, lam)

egrid = np.arange(1.0, 30.0001, 0.01)
caps = {}
for name, (e_line, e_c, mu, lam) in lines.items():
    slant = KO * np.clip(egrid**1.67 - e_c**1.67, 0, None) * CSC
    ok = egrid[slant <= lam]
    caps[name] = ok.max()

rows = []
for E0 in E0S:
    for name, (e_line, e_c, mu, lam) in lines.items():
        U = E0 / e_c
        if U <= 1.0:
            rows.append([E0, name, U] + [np.nan] * 7 + ["not excited"])
            continue
        depth = KO * (E0**1.67 - e_c**1.67)
        slant = depth * CSC
        sigma = 4.5e5 / (E0**1.65 - e_c**1.65)
        f_lo, f, f_hi = sorted(
            1.0 / ((1 + chi / sigma) * (1 + H_PHIL / (1 + H_PHIL) * chi / sigma))
            for chi in (mu * 0.8 * CSC, mu * CSC, mu * 1.2 * CSC)
        )
        verdict = "pass" if slant <= lam else "FAIL"
        rows.append([E0, name, U, depth, slant, lam, slant / lam, f, f_lo, f_hi, verdict])

header = ["E0_kV", "line", "overvoltage_U0", "prod_depth_um", "slant_path_um",
          "atten_len_um", "criterion_ratio", "f_chi", "f_chi_-20%MAC",
          "f_chi_+20%MAC", "criterion"]
with open("scripts/eds_voltage_predictions.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(header)
    w.writerows([[f"{v:.4g}" if isinstance(v, float) else v for v in r] for r in rows])

print(f"matrix: A_bar={A_BAR:.2f}  Z_bar={Z_BAR:.2f}  rho={RHO}  h={H_PHIL:.3f}  "
      f"csc(psi)={CSC:.3f}")
print(f"Kanaya-Okayama full range R_KO: "
      + "  ".join(f"{E0:g} kV -> {KO * E0**1.67:.2f} um" for E0 in E0S))
print()
print(f"{'E0':>4} {'line':<6} {'U0':>5} {'depth':>6} {'slant':>6} {'1/e len':>8} "
      f"{'ratio':>6} {'f(chi)':>7} {'f range (+/-20% MAC)':>21}  criterion")
for r in rows:
    if r[-1] == "not excited":
        print(f"{r[0]:>4g} {r[1]:<6} {r[2]:>5.2f} {'-':>6} {'-':>6} {'-':>8} "
              f"{'-':>6} {'-':>7} {'-':>21}  not excited (U0 <= 1)")
    else:
        print(f"{r[0]:>4g} {r[1]:<6} {r[2]:>5.2f} {r[3]:>6.2f} {r[4]:>6.2f} "
              f"{r[5]:>8.2f} {r[6]:>6.2f} {r[7]:>7.2f} "
              f"{f'{r[8]:.2f}-{r[9]:.2f}':>21}  {r[10]}")
print()
print("criterion cap per line (max E0 with slant depth <= 1/e attenuation length):")
for name, cap in caps.items():
    print(f"  {name:<6} E0 <= {cap:.1f} kV")
print(f"alloy cap = min over quantified metal lines (Mg, Al, Si): "
      f"{min(caps[n] for n in ['Mg Ka', 'Al Ka', 'Si Ka']):.1f} kV")

# ---- figure ----------------------------------------------------------------
SURFACE, INK, INK2, MUTED, GRID, AXIS = ("#fcfcfb", "#0b0b0b", "#52514e",
                                         "#898781", "#e1e0d9", "#c3c2b7")
COLORS = {"Si Ka": "#2a78d6", "Mg Ka": "#eb6834", "Al Ka": "#1baf7a",
          "O Ka": "#eda100", "Fe Ka": "#e87ba4"}
LABELS = {"O Ka": "O Kα", "Mg Ka": "Mg Kα", "Al Ka": "Al Kα",
          "Si Ka": "Si Kα", "Fe Ka": "Fe Kα"}

fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9), dpi=150, facecolor=SURFACE)
for ax in axes:
    ax.set_facecolor(SURFACE)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=MUTED, labelsize=8.5)
    ax.set_xticks(E0S)
    ax.set_xlim(4, 23.5)
    ax.set_xlabel("beam energy E₀ (kV)", color=MUTED, fontsize=9)

by_line = {name: [r for r in rows if r[1] == name] for name in lines}


def draw(ax, name, ys, log=False):
    xs = [r[0] for r in by_line[name] if r[-1] != "not excited"]
    ax.plot(xs, ys, color=COLORS[name], linewidth=2, marker="o",
            markersize=6, markeredgecolor=SURFACE, markeredgewidth=1.2)
    ax.annotate(LABELS[name], (xs[-1], ys[-1]), xytext=(6, 0),
                textcoords="offset points", va="center", fontsize=8.5, color=INK2)


for name in ["Si Ka", "Mg Ka", "Al Ka", "O Ka"]:
    draw(axes[0], name, [r[7] for r in by_line[name] if r[-1] != "not excited"])
    draw(axes[1], name, [r[6] for r in by_line[name] if r[-1] != "not excited"])
for name in lines:
    draw(axes[2], name, [r[2] for r in by_line[name] if r[-1] != "not excited"])

axes[0].set_title("escape fraction f(χ)", color=INK, fontsize=10)
axes[0].set_ylim(0, 1.02)
axes[0].axhline(0.75, color=MUTED, linewidth=1, linestyle=(0, (4, 3)))
axes[0].annotate("f(χ) ≥ 0.75 target", (12.5, 0.75), xytext=(0, -11),
                 textcoords="offset points", ha="center", fontsize=8, color=MUTED)

axes[1].set_title("criterion ratio: slant production depth ÷ 1/e attenuation length",
                  color=INK, fontsize=10)
axes[1].set_yscale("log")
axes[1].axhline(1.0, color=MUTED, linewidth=1, linestyle=(0, (4, 3)))
axes[1].annotate("criterion limit (≤1 passes)", (4.2, 1.0), xytext=(0, 4),
                 textcoords="offset points", fontsize=8, color=MUTED)

axes[2].set_title("overvoltage U₀ = E₀ / $E_\\mathrm{c}$", color=INK, fontsize=10)
axes[2].set_yscale("log")
for y, lbl in [(1.0, "U₀ = 1: no excitation"), (2.0, "U₀ ≈ 2: adequate yield")]:
    axes[2].axhline(y, color=MUTED, linewidth=1, linestyle=(0, (4, 3)))
    axes[2].annotate(lbl, (4.2, y), xytext=(0, 4), textcoords="offset points",
                     fontsize=8, color=MUTED)

handles = [plt.Line2D([], [], color=COLORS[n], linewidth=2, marker="o",
                      markersize=6, markeredgecolor=SURFACE, label=LABELS[n])
           for n in ["O Ka", "Mg Ka", "Al Ka", "Si Ka", "Fe Ka"]]
fig.legend(handles=handles, loc="upper right", ncol=5, frameon=False,
           fontsize=8.5, labelcolor=INK2, bbox_to_anchor=(0.995, 1.0))
fig.suptitle("AlSi10Mg SEM-EDS: what each beam voltage does to each analytical line",
             color=INK, fontsize=11.5, x=0.01, ha="left")
fig.text(0.01, 0.895, "matrix Al 89.5 / Si 10 / Mg 0.5 wt%,  ρ = 2.67 g/cm³,  "
         "take-off 35.1°  —  predictions for the 5/10/15/20 kV series",
         color=MUTED, fontsize=8.5)
fig.tight_layout(rect=(0, 0, 1, 0.86))
fig.savefig("scripts/eds_voltage_predictions.png", facecolor=SURFACE,
            bbox_inches="tight")
print("\nwrote scripts/eds_voltage_predictions.csv and scripts/eds_voltage_predictions.png")
