# Energy-scale check and peak identification for the three NAB (C63000) powder spectra.
# Writes outputs/energy_calibration.csv (read by the DTSA-II scripts), outputs/peak_check.csv,
# outputs/count_rates.csv and figures/peak_id.png.
# Usage: python eds_peaks.py /tmp/nab-staging/files/eds
import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from rsciio.edax._api import get_spc_dtype_list

dataDir = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
files = {10: "10kV 3_2nA", 15: "15kV 3_2nA", 20: "20kV 3_2 nA  USE THIS ONE"}
spectra = {}
for kv, stem in files.items():
    lines = open(os.path.join(dataDir, stem + "_1.msa"), encoding="latin-1").read().splitlines()
    i0 = next(i for i, l in enumerate(lines) if l.startswith("#SPECTRUM"))
    data = np.array([[float(x) for x in l.split(",")[:2]] for l in lines[i0 + 1:] if l and not l.startswith("#")])
    raw = open(os.path.join(dataDir, stem + ".spc"), "rb").read()
    dt = np.dtype(get_spc_dtype_list(load_all=True, version=0.7))
    hdr = np.frombuffer(raw[:dt.itemsize], dtype=dt)[0]
    # DTSA-II convention: channel i spans [5i, 5i + 5) eV, so channel centres sit 2.5 eV above the listed energy
    spectra[kv] = dict(e=data[:, 0] / 1000 + 0.0025, c=data[:, 1], lt=float(hdr["liveTime"]), preset=float(hdr["preset"]),
                       toa=float(hdr["takeoff"]), amp_us=7.68)

# Energy scale: centroids of well-separated lines (doublet centroids weighted 2:1 for Ka1:Ka2)
ref = {"Al Ka": 1.4865, "Fe Ka": 6.3995, "Ni Ka": 7.4724, "Cu Ka": 8.0413, "Cu Kb": 8.9053, "C K": 0.2774, "Cu La": 0.9297}
gauss = lambda x, a, mu, s, b0, b1: a * np.exp(-0.5 * ((x - mu) / s) ** 2) + b0 + b1 * (x - mu)
rows, cal = [], []
for kv, s in spectra.items():
    for name, x0 in ref.items():
        w = 0.06 if x0 < 1.2 else 0.12
        m = (s["e"] > x0 - w) & (s["e"] < x0 + w)
        if s["c"][m].max() - s["c"][m].min() < 150:
            continue
        p, cov = curve_fit(gauss, s["e"][m], s["c"][m], p0=[s["c"][m].max(), x0, 0.05, s["c"][m].min(), 0], maxfev=20000)
        rows.append(dict(kV=kv, line=name, ref_keV=x0, fit_keV=p[1], fit_sigma_keV=np.sqrt(cov[1, 1]), shift_eV=1000 * (p[1] - x0), fwhm_eV=2354.8 * abs(p[2])))
    df = pd.DataFrame([r for r in rows if r["kV"] == kv and r["ref_keV"] > 1.2])
    b, a = np.polyfit(df.ref_keV, df.fit_keV, 1, w=1 / df.fit_sigma_keV)
    cal.append(dict(kV=kv, offset_eV=1000 * a, gain=b, dtsa2_zero_offset_eV=-1000 * a / b, dtsa2_ch_width_eV=5.0 / b))
pd.DataFrame(rows).round(5).to_csv(os.path.join(here, "outputs", "energy_lines.csv"), index=False)
cal = pd.DataFrame(cal).set_index("kV")
cal.round(6).to_csv(os.path.join(here, "outputs", "energy_calibration.csv"))

# Count rates. Real time is not in the files; dead time is bracketed two ways: (a) a paralyzable
# model with tau = amp time, and (b) reading the .spc "preset" field as clock seconds.
cr = []
for kv, s in spectra.items():
    ocr = s["c"].sum() / s["lt"]
    x = 0.0
    for _ in range(100):
        x = ocr * s["amp_us"] * 1e-6 * np.exp(x)
    cr.append(dict(kV=kv, live_time_s=s["lt"], total_counts=int(s["c"].sum()), ocr_cps=round(ocr), spc_preset=s["preset"],
                   dead_time_pct_tau_amp=round(100 * (1 - np.exp(-x)), 1), dead_time_pct_if_preset_is_clock=round(100 * (1 - s["lt"] / s["preset"]), 1)))
cr = pd.DataFrame(cr)
cr.to_csv(os.path.join(here, "outputs", "count_rates.csv"), index=False)

# Peak checks: net counts and centroid of the bump at 1.7-2.0 keV (Si Ka 1.740, W Ma 1.775, Cu L + Cu L 1.86),
# Cu L sum-peak scaling (area / (Cu L rate^2 * live time) is constant for pile-up), and windows for
# W La, Mn Ka, Zn Ka and the Cu Ka escape peak against a local linear background.
chk = []
for kv, s in spectra.items():
    e, c = s["e"], s["c"]
    m = (e > 1.62) & (e < 2.15)
    bgm = m & ((e < 1.68) | (e > 2.02))
    bg = np.polyval(np.polyfit(e[bgm], c[bgm], 1), e)
    pk = (e > 1.68) & (e < 2.02)
    net = c[pk] - bg[pk]
    p, cov = curve_fit(lambda x, a, mu, sg: a * np.exp(-0.5 * ((x - mu) / sg) ** 2), e[pk], net, p0=[net.max(), 1.82, 0.04])
    cul = (e > 0.86) & (e < 1.0)
    cul_rate = c[cul].sum() / s["lt"]
    area = net.sum()
    chk.append(dict(kV=kv, feature="1.7-2.0 keV bump", centroid_keV=round(p[1], 4), centroid_sigma_keV=round(np.sqrt(cov[1, 1]), 4),
                    fwhm_eV=round(2354.8 * abs(p[2])), net_counts=round(area), pileup_norm=area / (cul_rate ** 2 * s["lt"])))
    for name, x0, half in [("W La", 8.398, 0.07), ("W Lb1", 9.672, 0.07), ("Mn Ka", 5.899, 0.07), ("Zn Ka", 8.638, 0.06),
                           ("Cu Ka escape", 6.308 + 0.010, 0.04), ("Cu Ka + Cu Ka", 16.09, 0.10), ("Al K + Cu L", 2.417, 0.06)]:
        if x0 > kv:
            continue
        win = (e > x0 - half) & (e < x0 + half)
        side = ((e > x0 - 3 * half) & (e < x0 - 1.5 * half)) | ((e > x0 + 1.5 * half) & (e < x0 + 3 * half))
        b = np.polyval(np.polyfit(e[side], c[side], 1), e[win]).sum()
        chk.append(dict(kV=kv, feature=name, centroid_keV=x0, net_counts=round(c[win].sum() - b), bg_counts=round(b), three_sigma=round(3 * np.sqrt(b))))
chk = pd.DataFrame(chk)
chk.to_csv(os.path.join(here, "outputs", "peak_check.csv"), index=False)
print(cal.round(5).to_string(), cr.to_string(), chk.to_string(), sep="\n\n")

# Figure: 20 kV spectrum (log) with identified lines, plus zooms on the 1.7-2.0 keV bump and the W L / Zn K region
fig = plt.figure(figsize=(12, 7.5), constrained_layout=True)
gs = fig.add_gridspec(2, 3)
ax = fig.add_subplot(gs[0, :])
colors = {10: "#4C78A8", 15: "#F58518", 20: "#222222"}
for kv in (10, 15, 20):
    s = spectra[kv]
    ax.semilogy(s["e"], np.maximum(s["c"] / s["lt"] / 3.2, 1e-3), lw=0.7, color=colors[kv], label="%d kV" % kv)
labels = {"C K": 0.277, "O K": 0.525, "Fe L": 0.705, "Ni L": 0.851, "Cu L": 0.930, "Al K": 1.487, "Mn Ka": 5.899, "Fe Ka": 6.404,
          "Fe Kb": 7.058, "Ni Ka": 7.478, "Cu Ka": 8.048, "Cu Kb": 8.905}
for n, x in labels.items():
    ax.axvline(x, color="0.75", lw=0.5, zorder=0)
    ax.text(x, 120, n, rotation=90, fontsize=7, ha="right", va="top")
ax.set(xlim=(0, 20.2), ylim=(2e-3, 150), xlabel="Energy (keV)", ylabel="counts / (s nA) per 5 eV channel",
       title="NAB (C63000) powder on C tape, 3.2 nA: counts per live second per nA")
ax.legend(loc="upper right", frameon=False)
zooms = [(1.55, 2.25, "1.7-2.0 keV: Si Ka / W Ma / Cu L+Cu L", {"Si Ka": 1.740, "W Ma": 1.775, "W Mb": 1.835, "2 x Cu L": 1.86}),
         (5.6, 6.7, "Mn Ka and Cu Ka escape", {"Mn Ka": 5.899, "Cu Ka esc": 6.308, "Fe Ka": 6.404, "Mn Kb": 6.490}),
         (8.1, 10.0, "W L and Zn K", {"Ni Kb": 8.265, "W La": 8.398, "Zn Ka": 8.638, "Cu Kb": 8.905, "Cu Ka + Cu L": 8.98, "W Lb": 9.672})]
for j, (lo, hi, title, mk) in enumerate(zooms):
    ax = fig.add_subplot(gs[1, j])
    for kv in (15, 20) if lo > 5 else (10, 15, 20):
        s = spectra[kv]
        m = (s["e"] > lo) & (s["e"] < hi)
        ax.plot(s["e"][m], s["c"][m] / s["lt"] / 3.2, lw=0.8, color=colors[kv], label="%d kV" % kv)
    for n, x in mk.items():
        ax.axvline(x, color="0.6", lw=0.6, ls="--")
        ax.text(x, ax.get_ylim()[1], n, rotation=90, fontsize=7, ha="right", va="top")
    ax.set(xlim=(lo, hi), xlabel="Energy (keV)", title=title)
    if lo > 8:
        ax.set_ylim(0, 0.5)
    ax.title.set_fontsize(9)
fig.savefig(os.path.join(here, "figures", "peak_id.png"), dpi=130)
