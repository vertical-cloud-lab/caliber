# EDS parameter series — consolidated data and findings

Working reference for **Parameter #3 (Beam Current)**. This document pulls together the
measured data, computed predictions, program decisions, and literature artifacts produced
under issue #1 across PR #6 (EDS DAQ), PR #11 (EDS parameter 1 — Beam Energy), and
PR #13 (EDS parameter 2 — Counts/Acquisition Time), so the beam-current work starts from
one branch that contains everything. Sources are linked throughout; nothing here is new
analysis.

## 1. Data inventory on this branch

| Path | Origin | Contents |
|---|---|---|
| [`docs/eds_daq.md`](eds_daq.md) | PR #6 (`5505f54`) | The acquisition chain (SDD → pulse processor → MCA) and how process time, dead time, pile-up, and live time arise from it |
| [`docs/eds_voltage_series_plan.md`](eds_voltage_series_plan.md) | PR #13 (`a68e0c6`) | Pre-registered 5/10/15/20 kV test of the voltage criterion: predictions P1–P7, protocol, decision rules H1–H3 |
| [`scripts/AlSi10Mg_EDS_Map_1.csv`](../scripts/AlSi10Mg_EDS_Map_1.csv) | PR #11 (`e61f5d9`) | The real Aug 5 kV Apreo map-sum spectrum (4096 channels) |
| [`scripts/eds_kfactor_quant.py`](../scripts/eds_kfactor_quant.py) + [figure](../scripts/eds_kfactor_quant.png) | PR #11 | Poisson-weighted model fit of that spectrum: net intensities, Currie 3σ detection, k-factor calibration |
| [`scripts/eds_voltage_predictions.py`](../scripts/eds_voltage_predictions.py) + [CSV](../scripts/eds_voltage_predictions.csv) + [figure](../scripts/eds_voltage_predictions.png) | PR #13 | Independent recomputation of the voltage criterion (xraydb MACs, Kanaya–Okayama depths, Philibert f(χ)) |
| [`scripts/eds_mg_quant_demo.py`](../scripts/eds_mg_quant_demo.py) + [`synthetic_AlSi10Mg.msa`](../scripts/synthetic_AlSi10Mg.msa) | issue #1 branch (`ef72e46`) | Synthetic demo of the background failure mode: naive windows 1.65% "Mg" vs 0.41% fitted (true 0.50%) |
| [`outputs/issue-1-eds-parameters/`](../outputs/issue-1-eds-parameters/answer.md) | PR #11 | Edison: how the standard EDS parameter recommendations were originally derived |
| [`outputs/eds-standards/`](../outputs/eds-standards/answer.md) | PR #11 | Edison: what a standard spectrum is, metadata it must carry, k-ratio protocol |
| [`outputs/eds-standards-best-practices/`](../outputs/eds-standards-best-practices/answer.md) | PR #11 | Edison: archived-standard reuse, QC protocol, dead-time guidance |
| [`outputs/eds-standards-material-vetting/`](../outputs/eds-standards-material-vetting/answer.md) | PR #11 | Edison: vetting of the purchased Al / Si / MgO standard materials |
| [`outputs/eds-sem-reading-list/`](../outputs/eds-sem-reading-list/answer.md) | PR #11 | Edison: 8-tier annotated curriculum for quantitative bulk SEM-EDS |
| [`outputs/insulator-charging-depth-grounding/`](../outputs/insulator-charging-depth-grounding/answer.md) | PR #11 | Edison: charging physics of uncoated MgO at 5 keV |
| [`outputs/vpsem-low-vacuum-eds/`](../outputs/vpsem-low-vacuum-eds/answer.md) | PR #11 | Edison: VPSEM beam-skirt physics — why low-vacuum mode is not a quant substitute for coating |
| [`outputs/edison_eds_tools_comparison/`](../outputs/edison_eds_tools_comparison/answer.md) | PR #6 | Edison: eXSpy vs DTSA-II vs CalcZAF comparison |
| [`outputs/issue-1-mg-evaporation/`](../outputs/issue-1-mg-evaporation/answer.md) | issue #1 branch (`e6227c8`) | Edison: Mg evaporation loss in LPBF — near-complete retention (0–10% relative) under Ar |

## 2. Measured session data

Two EDS sessions exist on the same LPBF AlSi10Mg sample (EDAX Octane Plus SDD on the
Thermo Fisher Apreo, take-off 35.1°, TEAM software). Dates per
[PR #13 discussion](https://github.com/vertical-cloud-lab/caliber/pull/13#issuecomment-5547583835)
(the plan doc's "July" labels refer to these same runs):

| | Apr session | Aug session |
|---|---|---|
| Beam voltage | 15 kV | 5 kV |
| Total counts (map sum) | 4,435,734 | 652,397 |
| Live time | 460.8 s | 327.7 s |
| Counts per live second | 9,626 | 1,991 |
| Amp (process) time | 1.92 µs | 7.68 µs |
| FWHM at Mn Kα | — | 127.9 eV |
| Set probe current | — | 3.2 nA (set point, never cup-measured) |

Quantification results for the Aug 5 kV run:

- Vendor eZAF (standardless, normalized): **Mg 0.94 wt%** (5.8% relative 1σ counting error),
  Si 11.15, C 1.99, O 1.68 wt%. The "2% Mg" in the report is the map-legend count fraction,
  not a wt% — there was never a 2 wt% measurement to correct.
- Phase split (EDAX phase clustering): Si-rich phase 17.28 wt% Si / 1.15 Mg (120.8 s);
  Al-rich phase 7.46 wt% Si / 0.80 Mg (206.9 s) — Mg tracking Si is real LPBF
  microstructure (Mg segregates toward the eutectic Si network).
- Independent model fit ([script](../scripts/eds_kfactor_quant.py)): net counts
  Al Kα 416,217 / Si Kα 37,233 / Mg Kα 4,435 / O Kα 7,647; Mg Kα significance 28.2σ
  (detection is not the problem — quantification accuracy is); calibrated k-factors
  reproduce eZAF at Mg ≈ 0.96 wt%.
- Manual DTSA-II k-ratio pass by Ronnie: Mg ≈ 0.9 wt%.
- Mg Kα detection limit at this dose (Currie L_D): ≈0.06 wt%. Net-Mg counting error:
  ±0.055 wt% — small next to the ≈0.5 wt% systematic gap vs expectation.

The Apr 15 kV run reported Si 9.47, O 8.10, Mg 1.64 wt%. It **fails a physics consistency
check** ([PR #11 §3](https://github.com/vertical-cloud-lab/caliber/pull/11#issuecomment-5481281979)):
when only kV changes, net-intensity ratios must follow generation + absorption physics —
Si/Al did (×0.71 measured vs ×0.66 predicted) but Mg/Al rose ×1.52 where physics predicts
×0.86, and O/Al rose ×1.33 vs ×0.29 predicted. About half of the apparent 15 kV Si
"improvement" is the bogus 8.1 wt% O row soaking up mass in the normalization.
Note the original pile-up explanation was later weakened
([PR #13 analysis](https://github.com/vertical-cloud-lab/caliber/pull/13#issuecomment-5574393906)):
at the recorded count rates both sessions ran the pulse processor ≈97% idle, so the
earlier ≈49%/≈22% dead-time inferences from wall-clock memory cannot be processor dead
time. The ×1.52 anomaly may survive at controlled dead time — exactly what plan
prediction P7 tests.

Ground truth status: the powder certificate says **0.5–0.7 wt% Mg** (the earlier
0.05–0.07 figure was a typo; the Edison evaporation result — near-complete Mg retention
under Ar — scales unchanged, predicting ≈0.45–0.70 wt% as-built). A one-time **ICP-MS
measurement on the tensile sample** (with Gage and Dr. Rappeleye) will provide the truth
value that EDS optimization is judged against.

## 3. Parameter #1 — Beam Energy (PR #11)

**The CALIBER voltage criterion:** for every quantified line,
`(deepest X-ray production depth) × csc(take-off angle) ≤ (1/e attenuation length)` —
i.e. the worst-case photon's exit path must not exceed the length over which 63.2% of
photons are absorbed. The slant factor csc(35.1°) = 1.74 is load-bearing: with it the
Si Kα cap is **7.6 kV**; without it, 10.3 kV. Equivalent statement: f(χ) ≥ 0.75 for the
worst quantified line. Recomputed independently in
[`eds_voltage_predictions.py`](../scripts/eds_voltage_predictions.py) (values below from
its [CSV](../scripts/eds_voltage_predictions.csv); constants: alloy MAC for Si Kα
2836 cm²/g, ρ = 2.67 g/cm³, ψ = 35.1°):

| E₀ | Si Kα slant path (µm) | vs 1.32 µm atten. length | f(χ) Si Kα | avg Si Kα absorbed | criterion verdict (O / Si / Mg / Al / Fe) |
|---|---|---|---|---|---|
| 5 kV | 0.59 | pass | 0.87 | 11–13% (matches measured A = 0.9030) | FAIL / pass / pass / pass / not excited (U₀ = 0.70) |
| 10 kV | 2.17 | fail | 0.64 | 36% | FAIL / FAIL / pass / pass / pass |
| 15 kV | 4.41 | fail | 0.45 | 48–55% (matches A = 0.5925) | FAIL / FAIL / pass / pass / pass |
| 20 kV | 7.21 | fail | 0.32 | 65–70% | FAIL / FAIL / FAIL / pass / pass |

Key reasoning, in one place:

- **The criterion bounds correction uncertainty, not counts.** Escaped Si Kα per unit
  dose *rises* with kV (×3.6 at 10 kV, ×5.6 at 15, ×6.9 at 20 relative to 5 kV) — but the
  absorbed fraction is the part of the answer that is computed rather than measured, and
  a ±20% MAC error moves reported Si by 2.6% at 5 kV versus 16% at 20 kV. The lower the
  line energy, the shorter its attenuation length and the more the A factor magnifies
  MAC/model error (O Kα fails even at 5 kV — its cap is 4.6 kV — rediscovering Statham's
  advice not to quantify lines below 1 keV).
- **On the fixed 5/10/15/20 kV menu, only 5 kV complies for AlSi10Mg.** Whether the
  criterion captures the right physics is what the pre-registered voltage series
  ([plan](eds_voltage_series_plan.md), predictions P1–P7, decision rules H1/H2/H3) will
  decide. The graded stress test: at 10 kV only Si fails; at 15 kV Si fails hard and Mg
  turns marginal; at 20 kV both fail. Counter-pressures pushing against low kV are
  logged: surface-film weighting (C/O layers dominate the 0.42 µm sampling depth at
  5 kV), background mass fraction, peak crowding, and L-line-only access to heavier
  elements (trace heavy elements on Lα at 5 kV: detection limit of order 0.3–1 wt% —
  workable for minor, not trace).
- **Alloy roadmap:** planned alloying elements are Al, Mn, Cr, Zr, Mg, Si, Cu, Ti, Fe,
  Ni, Ce, Sc, Li, Er, Zn, Sn. Suggested long-term menu: a two-point 5 kV + 20 kV
  strategy (20 kV for transition-metal Kα, knowingly outside the absorption criterion),
  with an overvoltage floor near U₀ ≥ 1.5 as an added selection rule. Li Kα (52 eV) is
  unquantifiable by EDS.

**Standards program status** (the machinery parameter #3 plugs into):

- Purchased under **order 13279 (approved 2026-09-08)**: high-purity Al evaporation
  pellet (Kurt J. Lesker), Si chips (5×5 mm), MgO (100) wafer 10×10×0.5 mm 1-side
  polished (MTI 01841-AB). MgO and Si arrive polished; only the Al pellet needs
  polishing. Vetting: [`outputs/eds-standards-material-vetting/`](../outputs/eds-standards-material-vetting/answer.md).
- MgO is an insulator → needs a carbon coat; the BYU coater is in storage until end of
  October. VPSEM is **not** an acceptable workaround for quantitative work (beam skirt
  scatters a pressure-dependent current fraction hundreds of µm off-probe —
  [`outputs/vpsem-low-vacuum-eds/`](../outputs/vpsem-low-vacuum-eds/answer.md)).
- Reuse rules ([PR #11 discussion](https://github.com/vertical-cloud-lab/caliber/pull/11#issuecomment-5481703178)):
  a standard is defined by (element/line, kV, detector, process time) and is reusable
  across sessions and samples **indefinitely** given a per-session QC verification
  (energy calibration, FWHM, counts per nA·s on a QC material, Duane–Hunt endpoint).
  Parameters split into: *identical* (detector, kV set point, process time, geometry/
  working distance, coating scheme), *measured every acquisition* (probe current, live
  time — the dose), and *in range, not matched* (dead time, count rate).

## 4. Parameter #2 — Counts / Acquisition Time (PR #13)

- **What time buys and doesn't.** Peak and bremsstrahlung background grow at the same
  rate (both proportional to dose), so peak-to-background is fixed by kV and matrix;
  what improves with counting is significance and detection limit, as 1/√t. Benefit
  scales as √t while cost scales as t: halving the statistical error costs 4× the time.
  Stop rule candidate: σ_stat ≤ ⅓ σ_syst.
- **Count targets** (Goldstein 4th ed.; Guyett et al. 2024): >10⁶ total counts for
  major/minor accuracy even under severe peak interference — which Mg Kα under the
  Al Kα tail is, at a 100–200:1 concentration ratio; >10⁷ for clean 200-ppm trace work;
  >10⁸ for trace under interference. Neither session reached 10⁷ (best: 4.4M).
  Plan target ≥10⁴ net Mg Kα counts ⟺ ≈1.5M total counts at 5 kV ⟺ ≈12.5 min live at
  the Aug rate (2.0 kcps) — or **≈75 s at the rate a proper beam current would deliver**
  (see §5).
- **The Al Kα tail does not dilute away:** it is a fixed fraction of Al counts, so more
  time shrinks only random error; the tail-model bias is systematic. Counts under Mg Kα
  are continuum + incomplete-charge-collection tail, a peak-shape property — resolution
  slimming has no lever on it (Mg–Al separation is 3.2 Al-FWHM already).
- **Replicates over one long run:** 5 × 60 s summed is statistically identical to
  1 × 300 s (Poisson counts add), and retires the four real downsides of long
  acquisitions — systematic-error floor, probe-current drift, spatial drift
  (≈10 nm/min walks a 0.3 µm probe a full probe-width in 30 min), calibration drift.
  DTSA-II automates the whole replicate protocol: bundle wizard sums standards with
  correct dose bookkeeping (live times add, current becomes the live-time-weighted
  average) plus per-spectrum outlier score and Duane–Hunt charging check; the quant
  wizard hands back mean ± SD across unknown replicates. Multiple shorter scans on
  adjacent fresh areas is the adopted practice (also spreads carbon dose).
- **Carbon management** (Mike Standing): plasma cleaner + bake-out oven (2–3 h, load
  samples hot) make longer total acquisition viable; cleanliness discipline starts at
  polishing. Measure the carbon budget directly: consecutive short spectra on one spot,
  watch the C Kα slope and Mg/Al drift.
- **Amp time is not a standalone parameter** ([analysis](https://github.com/vertical-cloud-lab/caliber/pull/13#issuecomment-5593623759)):
  EDAX ladder 0.96/1.92/3.84/7.68 µs. Longer = slimmer peaks; EDAX's "under 4 eV"
  penalty at Mn Kα becomes +10 to +25% width at Mg Kα (69 → 76–86 eV) because
  electronic noise is a constant eV adder while the Fano floor shrinks with energy.
  Width barely touches the Mg problem; the real trade is the count-rate ceiling —
  at 25–30% dead time, ≈14 kcps stored at 7.68 µs vs ≈81 kcps at 0.96 µs (5.7×), with
  1.92 µs a good middle (+2 eV at Mg, 3.5× ceiling). Verdict: amp time is the partner
  knob of probe current — it only matters once current rises to feed it. A cheap A/B
  appendix block (predictions A1–A4: width transfer, dose-invariance of net Mg, tail
  flat-or-worse, ceiling ratio ≈5.7×) is pre-specified for the 5 kV session, kept out
  of the voltage series (which freezes amp time at 7.68 µs).
- **TEAM operation:** acquisition stop conditions are Limit By live time / clock time /
  ROI counts; Spectrum Only → Collect Spectrum appears to support a counts-based stop
  (possibly capped near 1.1M — Mike to confirm). Map duration is pixels × dwell ×
  frames, not a typed time.

## 5. What is already established for Parameter #3 — Beam Current

Everything below is in place from the prior PRs; the beam-current sessions turn it into
measured numbers on the Apreo.

**Role of the knob.** Counts track dose = current × live time. For a fixed count target
the dose is fixed — current only sets how fast it is delivered (real time =
live time / (1 − dead-time fraction)) and where the electronics operate. It is the knob
that lands dead time in the target band at fixed amp time; never trade amp time down to
rescue dead time, because that widens Mg Kα toward Al Kα.

**The dead-time question parameter #3 must settle.** The voltage-series plan operates at
**25–30% dead time** (P5 logs the current that achieves it per kV), while the NIST
standards-based protocol (Newbury & Ritchie 2015, in
[`outputs/eds-standards-best-practices/`](../outputs/eds-standards-best-practices/answer.md))
recommends **≤10%**, stricter for trace work, because coincidence/pile-up artifacts grow
above ≈15%. These are in genuine tension: the throughput argument says the Aug session
used a tenth of the detector's appetite (≥10⁴ net Mg in ≈75 s instead of ≈12 min at
10× the rate; 10⁷ total counts in ≈9 min instead of ≈84), and the artifact argument says
the cheapest insurance for a 0.5 wt% element under a major peak is a nearly idle
processor. Standards themselves don't need matched dead time (live-time clock corrects
it) — only in-range dead time. Measuring where pile-up actually bites on this detector
(Al Kα + Al Kα sum peak at 2.97 keV; any Mg/Al ratio shift vs dead time) picks the band
empirically and simultaneously adjudicates the P7 anomaly.

**Measured current, not displayed current.** The set point (e.g. "3.2 nA") is a knob
label. The Faraday cup + picoammeter (facility has both — Mike confirmed) measures what
was actually delivered; the routine
([PR #11](https://github.com/vertical-cloud-lab/caliber/pull/11#issuecomment-5484533976)):
park in cup → read → acquire → read again → close pair proves stability, average goes
into the spectrum's probe-current field (`#PROBECUR` in `.msa` / DTSA-II spectrum
properties). The k-ratio divides by recorded dose, so known current differences between
standard and unknown cancel exactly; unknown ones become full-size wt% errors. Warnings:
display vs cup off by tens of percent → aperture contamination / gun retune; before/after
differing >1% → source drifted during acquisition (use the mean; re-shoot standards).
Without a cup, a QC spectrum on a stable material (Si wafer) is the dose proxy via count
rate. Probe-current drift over long acquisitions is one of the four documented
long-acquisition downsides — bracketing each replicate bounds it. The SEM-class textbook
frames the same requirement: stable, high-integrated-count spectra are the foundation of
standards-based SDD-EDS accuracy.

**Carbon interacts with current only through dose per spot.** Dose for a target count is
fixed, so faster delivery does not add carbon — the levers are cleanliness (plasma clean,
bake-out) and fresh spots per acquisition; the dose-per-spot that keeps C Kα slope and
Mg/Al drift below counting error is a pre-registrable number.

**Open questions for the beam-current sessions:**

1. Map the Apreo's current ladder: cup-measured nA per preset, per menu kV (the set
   point has never been verified against the cup).
2. Dead time vs current curve at 5 kV, 7.68 µs: which preset lands 25–30%? Which lands
   ≤10%? Verify the predicted ≈10× rate headroom over the Aug session.
3. Pile-up onset: Al+Al sum-peak amplitude at 2.97 keV and Mg/Al net-ratio stability as
   dead time climbs — locate the artifact threshold for this detector and pick the
   CALIBER dead-time band from data.
4. Stability: bracketing cup readings around each replicate — drift magnitude per hour,
   per session (the free QC drift chart).
5. The amp-time A/B (A1–A4) as an appendix block, since amp time and current jointly set
   (dead time, resolution).
6. Candidate CALIBER rule to validate: *fix amp time at the resolution-friendly setting;
   set current to the empirically chosen dead-time band; measure it with the cup; record
   measured current × live time per spectrum.*

## 6. Cross-cutting program decisions

| Decision | Where |
|---|---|
| DTSA-II (native `.msa`, φ(ρz), bundle/quant wizards) replaces eXSpy for wt%; eXSpy had no bulk-SEM matrix correction. CalcZAF takes k-ratios, not spectra | issue #1 thread; [`outputs/edison_eds_tools_comparison/`](../outputs/edison_eds_tools_comparison/answer.md) |
| DTSA-II Polaris needs Java 24; runs after `cd` into install dir + `java -jar` | PR #11 thread |
| Standards-based, un-normalized quant is the program; standardless normalized output cannot adjudicate physics questions (normalization entangles all rows) | PR #11 §3 |
| Same working distance for standards and unknowns ("focusing to Z height") — take-off angle sets the absorption path | Mike's notes, issue #1 |
| A well-characterized same-alloy sample (via ICP-MS/XRF) can serve as a type standard afterward | Mike's notes |
| ICP-MS once on the tensile sample = ground truth for judging EDS optimization | issue #1 (2026-09-07) |
| Voltage series (parameter 1 test) awaits the standards + microscope sessions; data goes to `outputs/voltage-series/<E0>kV/` on PR #13 | [plan](eds_voltage_series_plan.md) |

## 7. Primary references

- Newbury & Ritchie (2015), SEM/SDD-EDS high-accuracy microanalysis, *J. Mater. Sci.*
  50:493 — [doi:10.1007/s10853-014-8685-2](https://doi.org/10.1007/s10853-014-8685-2)
  (the program's core protocol paper)
- Goldstein et al. (2018), *SEM and X-Ray Microanalysis*, 4th ed., Ch. 19–20 (k-ratio
  procedure), Ch. 16 (QC)
- Statham (2002), *J. Res. NIST* 107:531 — background/systematic-error limits —
  [open access](https://pmc.ncbi.nlm.nih.gov/articles/PMC4863855/)
- Currie (1968), detection-limit framework — [doi:10.1021/ac60259a007](https://doi.org/10.1021/ac60259a007)
- Ziebold (1967), precision vs counting time — [doi:10.1021/ac60252a028](https://doi.org/10.1021/ac60252a028)
- Kanaya & Okayama (1972) range equation, with the production-depth refinement
  E₀^1.67 → (E₀^1.67 − E_c^1.67) used in the criterion scripts
- Full annotated curriculum: [`outputs/eds-sem-reading-list/`](../outputs/eds-sem-reading-list/answer.md)
