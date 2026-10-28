# EDS of the first NAB (C63000) powder: DTSA-II quantification, Monte Carlo and acquisition advice

Issue #27. The powder is code `k7m2q9`: wrought 630 bronze rod (UNS C63000, a nickel-aluminum bronze,
nominally 82Cu-10Al-5Ni-3Fe), ultrasonically atomized on Oct 27, 2026. The SEM/EDS session was the same
day on the BYU Apreo C with an EDAX Octane Plus (TEAM 4.5.1). The powder was on carbon tape.

**Provenance.** The data come from `sgbaird/agent-staging` at commit `3c25afa`, folder
`for/vertical-cloud-lab/caliber/2026-10-28-nab-c63000-sem-eds/`. All 20 files matched the sha256 list in
the drop's `MANIFEST.md`. The raw spectra and images are not committed here; `fetch_data.sh` fetches
and checks them. Everything below is derived from the three `.msa` spectra (10, 15 and 20 kV at
3.2 nA), the `.spc` headers and the TIFF metadata.

__SUMMARY__

## Files

| File | What it does |
|---|---|
| `fetch_data.sh` | Fetches the drop into `/tmp/nab-staging` and checks every sha256 against `MANIFEST.md` |
| `run_dtsa2.sh` | Runs a DTSA-II Jython script with no display: NIST DTSA-II Polaris (2026-09-10, epq 15.1.57) started with `--script` under Xvfb on a Java 26 runtime. It installs both on first use and pre-sets the report folder so no first-run dialog blocks |
| `eds_peaks.py` | Energy-scale check, peak checks (pile-up, escape, W, Mn, Zn), count rates and dead time → `outputs/energy_calibration.csv`, `peak_check.csv`, `count_rates.csv`, `figures/peak_id.png` |
| `dtsa2_quant.py` | DTSA-II: detector model, simulated pure-element standards, filter fit, XPP matrix correction, for the measured and the Monte Carlo spectra → `outputs/dtsa2_kratios.csv`, `dtsa2_quant.csv`, `dtsa2_residual_*kV.csv`, `octane_plus_model_*kV.xml` |
| `dtsa2_mc.py` | DTSA-II NISTMonte (Gen 3) spectra of nominal C63000: flat bulk, 50 and 100 µm spheres on carbon, and a raster over a 50 µm sphere → `outputs/mc/*.msa` |
| `exspy_crosscheck.py` | HyperSpy/exspy Gaussian fits of the measured and MC spectra, and a quantification that uses the MC spectrum as a matrix-matched standard → `outputs/exspy_*.csv` |
| `compare_mc.py` | Measured against MC line by line → `outputs/line_ratios*.csv`, `kratios_measured_vs_mc.csv`, `figures/summary.png`, `figures/mc_vs_measured_spectra.png` |

Run order:

```bash
GH_READ_PAT_STAGING=... ./fetch_data.sh                    # data -> /tmp/nab-staging
python eds_peaks.py /tmp/nab-staging/files/eds             # needs numpy scipy pandas matplotlib rosettasciio
NAB_DATA=/tmp/nab-staging/files/eds NAB_OUT=outputs ./run_dtsa2.sh dtsa2_quant.py
NAB_OUT=outputs NAB_NTRAJ=3000 NAB_RASTER_GRID=10 ./run_dtsa2.sh dtsa2_mc.py   # about 12 min on 4 cores
NAB_DATA=/tmp/nab-staging/files/eds NAB_OUT=outputs ./run_dtsa2.sh dtsa2_quant.py   # again, now with the MC spectra
python exspy_crosscheck.py /tmp/nab-staging/files/eds      # hyperspy 2.5, exspy 0.3
python compare_mc.py /tmp/nab-staging/files/eds
```
