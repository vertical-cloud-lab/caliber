# 2027 MSA Undergraduate Research Scholarship — CALIBER Proposal (Draft)

Working draft for the [MSA Undergraduate Research Scholarship Program](https://microscopy.org/undergraduate-research-scholarship-program). Bracketed `[TODO]` items need applicant or lab input before submission. The research proposal (between the horizontal rules below) is held to the program's **3-page limit**; the [PDF render](2027_msa_undergraduate_research_scholarship_proposal.pdf) shows it at 11 pt, 1-inch margins, US Letter, references included. Budget, CV, and letters are separate documents and do not count toward the limit.

## Program requirements

- **Deadline:** December 1, 2026, for use during 2027 (awardees announced around February 15)
- **Award:** up to $3,000, for student stipend, supplies, and limited travel associated with the research; the budget must name the source(s) of other funding for instrument use, laboratory equipment, etc.
- **Eligibility:** full-time undergraduate at a university or four-year college, with junior or senior standing by the time the work begins; current MSA member (student membership); not previously funded by this program
- **Application packet:**
  1. Completed submission form
  2. Research proposal of **no more than three pages**, including at minimum an introduction, a methods section, and a description and itemization of the study's goals
  3. Budget showing how the award will be spent
  4. CV including education and/or training in microscopy, plus a brief statement of career goals
  5. Two letters of reference from scientists or university faculty familiar with the applicant's capabilities
  6. Letter from the supervisor of the lab where the research will be done, confirming that the applicant and project are acceptable
  7. Letter of recommendation from an MSA member (may be combined with one of the letters above)

Items 5–7 come from secondary listings of the program; microscopy.org refuses connections from the CI runner, so `[TODO: confirm the letter requirements and any font/margin rules on the live application form]`.

---

<!-- proposal:start -->

# Ground-Truthing Physics-Based Acquisition Rules for Quantitative SEM-EDS of Additively Manufactured AlSi10Mg

<p class="meta"><strong>Applicant:</strong> Ronnie Guymon, Brigham Young University <code>[TODO: major; class standing]</code> · <strong>Supervisor:</strong> Prof. Sterling G. Baird, Mechanical Engineering, BYU</p>
<p class="meta"><strong>Facility:</strong> BYU Electron Microscopy Facility (Thermo Fisher Apreo SEM, EDAX Octane Plus EDS) · <strong>Period:</strong> January–December 2027 · <strong>Request:</strong> $3,000</p>

## 1. Introduction

Every quantitative SEM-EDS result depends on choices made before the first X-ray is counted. Accelerating voltage, beam current, and acquisition time set how many X-rays are generated, how many are absorbed on their way out of the sample, and how many artifacts the detector electronics add. Standards-based EDS can reach about ±5% relative uncertainty, while standardless analysis can err by ±30%, and normalizing totals to 100% hides the error [1]. In practice, operators fall back on generic defaults (15–20 kV, "enough" counts) whose derivations are rarely written down and were not designed for light minor elements in new alloys.

Our lab is building **CALIBER**, an AI-enabled platform that recommends SEM, EDS, EBSD, and XRF acquisition parameters for a given sample and analysis goal. It couples the characterization literature (through retrieval-augmented generation), physics models, and a growing in-house dataset, and an uncertainty-aware feedback loop revises its recommendations as measurements arrive. Its first test case is laser powder bed fusion (LPBF) AlSi10Mg, in which under 1 wt% Mg controls precipitation hardening but must be measured in the shoulder of an Al Kα peak more than 100 times stronger. Our literature review found no controlled SEM-EDS parameter study for Mg in LPBF AlSi10Mg checked against an independent bulk analysis, so the settings in published work are examples rather than validated optima. Our lab's EBSD work shows the same sensitivity: on this alloy, the fraction of reliably indexed points rose from about 40% to 77% once beam current and the phase model were corrected.

Preliminary sessions on one LPBF AlSi10Mg sample show that the EDS problem is real and systematic (Table 1). Vendor standardless quantification reported 1.64 wt% Mg at 15 kV and 0.94 wt% at 5 kV, both above the 0.5–0.7 wt% expected for the powder. At 5 kV the Mg peak is clearly detected (about 10σ above background), but its net intensity shifts by roughly ±30% depending on how the Al Kα tail and background beneath it are modeled, about three times its counting error. When I passed the vendor's k-ratios through the independent matrix correction in NIST DTSA-II [2], Mg still came out at 0.90 wt%: the bias sits in the measured intensities, not the matrix correction, and more counts alone will not remove it. The 15 kV result also failed a physics consistency check: from 5 to 15 kV the Mg/Al net-intensity ratio rose ×1.52 where X-ray generation and absorption predict ×0.86, and 8.1 wt% apparent oxygen soaked up mass in the normalization. In September I began the current and counting work at 5 kV: Faraday-cup readings of 3.24–3.31 nA against a 3.2 nA set point, 29–30% dead time, spectra from 0.77 to about 5.6 million counts (Mg peak-to-background steady at 0.22–0.25 while signal-to-noise rose from about 11 to 30, as counting statistics predict), and eight replicate 1-million-count spectra.

<p class="caption"><strong>Table 1.</strong> Preliminary EDS of one LPBF AlSi10Mg sample (Apreo + EDAX Octane Plus, take-off 35.1°; vendor standardless eZAF, normalized).</p>

| Session | Beam energy | Total counts | Live time | Mg (wt%) | Si (wt%) | O (wt%) |
|---|---|---|---|---|---|---|
| April 2026 | 15 kV | 4.44 M | 461 s | 1.64 | 9.47 | 8.10 |
| August 2026 | 5 kV | 0.65 M | 328 s | 0.94 | 11.15 | 1.68 |
| Expected (powder) | — | — | — | 0.5–0.7 | 9–11 | — |

To explain these results I proposed a voltage rule from absorption physics, which we then refined: a line is quantifiable only if its deepest X-ray production depth [3], lengthened 1.74× by the slanted 35.1° exit path to the detector, stays within its 1/e attenuation length — equivalently, an absorption factor f(χ) ≥ 0.75. For AlSi10Mg the binding line is Si Kα, which caps the beam energy at 7.6 kV, so of the 5/10/15/20 kV settings in routine use only 5 kV should quantify Al, Si, and Mg cleanly (O Kα fails at all four, consistent with long-standing advice not to quantify lines below 1 keV [4]). Companion rules for beam current and acquisition time follow from dead-time and counting statistics [5,6]. These rules are falsifiable. This project tests them against an independent measurement of the true composition and turns the outcome into CALIBER's first validated recommendations.

## 2. Goals

1. **Ground truth.** Measure Mg in the printed specimen, and in its powder (which also reveals any Mg lost to evaporation during printing), by ICP-MS after acid digestion, so EDS accuracy is judged against a measurement rather than a nominal value.
2. **Test the voltage rule.** Run a pre-registered 5/10/15/20 kV series with standards-based, un-normalized quantification, and decide among three outcomes written down in advance: the rule holds (H1), it is too conservative (H2), or it needs a surface-film term because shallow 5 kV sampling is biased by oxide and contamination (H3).
3. **Map beam current and dead time.** Measure delivered probe current per setting, dead time versus current, and the onset of pulse pile-up, then choose the dead-time band from data — settling the tension between the ≤10% that the NIST protocol recommends for trace work [6] and the 25–30% band that favors throughput.
4. **Set acquisition time by a stopping rule.** Find the count level at which scatter between replicate spectra exceeds the counting error they predict — the point where more time stops improving accuracy — while tracking carbon contamination.
5. **Validate and share.** Enter each tested rule into CALIBER with its measured uncertainty, release spectra, scripts, and session metadata openly, and present the results at M&M 2027.

## 3. Methods

**Samples and ground truth.** LPBF AlSi10Mg printed from virgin powder `[TODO: printer/partner]` is sectioned, mounted, and polished; the final polish is recorded because embedded colloidal silica reads as Si + O within the 0.4 µm sampling depth at 5 kV. Polished samples are stored under vacuum in a desiccator (verified to hold vacuum for more than two weeks) and plasma-cleaned before each session. Offcuts of the printed specimen and the powder are digested and analyzed by ICP-MS (Agilent 8900, BYU) with Prof. Devin Rappleye's group (BYU Chemical Engineering); because acid-only digests under-recover Si, Si is taken from WDXRF (Rigaku Primus II, BYU Geology) or an HF-assisted digest. Once certified this way, the alloy also serves as a matrix-matched secondary standard.

**Instrument, standards, and quality control.** All EDS work uses the Apreo SEM with an EDAX Octane Plus silicon-drift detector (take-off 35.1°) at its 10 mm analytical working distance. Standards already purchased by the lab — 99.99% Al, a Si wafer, and a freshly cleaved MgO crystal — receive the same thin carbon coat as the specimen and are acquired in the same session as the unknown at every voltage; the pure-Al spectrum supplies the measured Al Kα tail shape beneath Mg Kα. Each session opens with quality control: energy calibration, detector resolution, counts per nA·s on a Si wafer, and a Duane–Hunt endpoint check for charging [5]. Probe current is read on the Faraday cup with a picoammeter before and after every acquisition and recorded with the spectrum, because the k-ratio divides by electron dose.

**Experiment 1 — voltage series (Goal 2).** The same fiducial-marked region is analyzed at 5, 10, 15, and 20 kV with amplifier time fixed and probe current adjusted to hold dead time constant, using replicate scans on adjacent areas that total enough counts for about ±3% counting precision on Mg (about 7 million counts at 5 kV). Seven predictions were fixed before data collection, for example: standards-based Si and Mg should be voltage-invariant within counting error at 5 kV and drift in the graded order the rule predicts at higher kV; Fe Kα must be absent at 5 kV (overvoltage 0.70); apparent C and O should fall roughly tenfold from 5 to 20 kV as a fixed surface film is diluted; and the Mg/Al ratio should fall ×0.86 from 5 to 15 kV.

**Experiment 2 — beam current and dead time (Goal 3).** At 5 kV I step through the current settings, recording measured current, dead time, count rate, the Al + Al sum peak at 2.97 keV, and the Mg/Al net-intensity ratio. The working dead-time band ends where that ratio departs from its low-dead-time value by more than counting error. Repeated before-and-after cup readings chart probe-current drift per hour.

**Experiment 3 — acquisition time (Goal 4).** Extending the September replicates, five or more spectra per count level on fresh adjacent areas are compared with the counting error each predicts; one long acquisition is compared with replicates of equal total live time; and the growth of C Kα, and any drift in Mg per total count, with dose sets a per-spot dose limit.

**Analysis.** Spectra are fit with our Poisson-weighted peak model (net intensities and Currie detection limits [7]) and quantified against same-session standards in DTSA-II with a φ(ρz) matrix correction [2]. Un-normalized analytical totals (98–102% as a health check) are reported beside vendor standardless results, and each condition's error against the ICP-MS value is split into counting and systematic parts. Each outcome maps onto the pre-written decision rules, and the resulting rule enters CALIBER with its measured uncertainty — the first full pass of CALIBER's feedback loop.

## 4. Timeline, outcomes, and significance

| Months (2027) | Work |
|---|---|
| Jan–Feb | Standards mounted and coated; ICP-MS ground truth; QC baseline; M&M 2027 abstract |
| Mar–Apr | Experiment 1: voltage series (four sessions plus standards) |
| May–Jun | Experiment 2: beam current, dead time, and pile-up |
| Jul | Experiment 3: acquisition time; CALIBER entries |
| Aug | Present at M&M 2027 |
| Sep–Dec | Journal manuscript and open data release; extension to the lab's next alloys |

**Expected outcomes.** (1) The first ground-truthed SEM-EDS acquisition study for LPBF AlSi10Mg, filling the gap our literature review identified; (2) validated or corrected rules for beam energy, current, and acquisition time, each with a measured uncertainty; (3) an open dataset and analysis scripts any EDS user can rerun; and (4) CALIBER's first experimentally validated recommendations, which the lab will extend to its alloy roadmap (Mn, Cr, Zr, Cu, Ti, Fe, Ni, Sc, Zn, and others). I will prepare the samples, run the sessions, and carry out the analysis, which trains me in standards-based quantitative microanalysis — the foundation for the career in microscopy that I am pursuing `[TODO: tie to career-goals statement]`.

<div class="refs">

**References**

1. Tong, V. & Mingard, K. *Measurement uncertainties of energy dispersive X-ray spectroscopy in the SEM (SEM-EDX/EDS)*. NPL Report MAT 135 (2026). https://doi.org/10.47120/npl.mat135
2. Ritchie, N. W. M. Spectrum simulation in DTSA-II. *Microsc. Microanal.* 15, 454–468 (2009). https://doi.org/10.1017/S1431927609990407
3. Kanaya, K. & Okayama, S. Penetration and energy-loss theory of electrons in solid targets. *J. Phys. D* 5, 43–58 (1972). https://doi.org/10.1088/0022-3727/5/1/308
4. Statham, P. J. Limitations to accuracy in extracting characteristic line intensities from X-ray spectra. *J. Res. NIST* 107, 531–546 (2002). https://doi.org/10.6028/jres.107.045
5. Goldstein, J. I. et al. *Scanning Electron Microscopy and X-Ray Microanalysis*, 4th ed. (Springer, 2018).
6. Newbury, D. E. & Ritchie, N. W. M. Performing elemental microanalysis with high accuracy and high precision by SEM/SDD-EDS. *J. Mater. Sci.* 50, 493–518 (2015). https://doi.org/10.1007/s10853-014-8685-2
7. Currie, L. A. Limits for qualitative detection and quantitative determination. *Anal. Chem.* 40, 586–593 (1968). https://doi.org/10.1021/ac60259a007

</div>

<!-- proposal:end -->

---

## Budget (separate document; draft — $3,000)

| Item | Amount |
|---|---|
| Student research stipend `[TODO: hours × rate]` | $1,500 |
| ICP-MS ground truth: digestion reagents, calibration solutions, any instrument fees `[TODO: quote; currently arranged as a one-time favor — reallocate if free]` | $400 |
| Standards and sample preparation: Zr and Ce standards for the next alloys (quoted at $175–440 in issue #12), polishing media, carbon coating, stubs | $400 |
| Travel to M&M 2027 (student registration and partial travel) | $700 |
| **Total** | **$3,000** |

**Other funding sources (the program asks for these):** SEM/EDS instrument time at the BYU Electron Microscopy Facility, the Al/Si/MgO standards already purchased (order 13279), and laboratory equipment are covered by the Vertical Cloud Lab `[TODO: funding source, e.g., startup funds]`. DTSA-II, HyperSpy/eXSpy, and the lab's analysis scripts are free and open source.

## CV notes (separate document)

Microscopy education and training to list, drawn from issues #1, #12, and #16 and PRs #6, #8, #11, and #13 `[TODO: add dates, verify wording]`:

- SEM course `[TODO: course number]`; EDS training with Mike Standing, BYU Electron Microscopy Facility
- EDS sessions on the Apreo at 5 kV: Faraday-cup current measurement, dead-time control, replicate-spectrum acquisition
- Quantitative EDS analysis: NIST DTSA-II (detector definition, k-ratio quantification, standards workflow) and HyperSpy/eXSpy scripting in Python
- Proposed the absorption-based beam-voltage criterion, the U₀ ≥ 1.5 overvoltage floor, and the 1-million-count doubling ladder used in CALIBER's EDS plan
- Sourced EDS standards (Al, Si, MgO); arranged ICP-MS ground-truth analysis; trial acid digestion of AlSi10Mg powder
- Metallographic preparation, ultrasonic cleaning of stubs, and vacuum-desiccator storage of polished samples
- EBSD: loaded and explored saved-pattern data in kikuchipy, and designed the phase-list, dictionary-indexing, and grain-reconstruction tests run on it
- Introductions to ICP-MS (BYU) and WDXRF / handheld XRF (Kevin Rey, BYU Geology)
- MSA student membership `[TODO: date joined]`

**Statement of career goals:** `[TODO: a few sentences in the applicant's own words — e.g., graduate study or industry work in materials characterization, and the role microscopy will play]`

## Letters (separate documents)

- **Supervisor letter** confirming that the applicant and project are acceptable: Prof. Sterling G. Baird
- **Two reference letters** from scientists or faculty familiar with the applicant's work: `[TODO: choose — e.g., Mike Standing (BYU Electron Microscopy Facility), Prof. Devin Rappleye (BYU Chemical Engineering), Kevin Rey (BYU Geology)]`
- **MSA-member letter** (may be one of the above): `[TODO: confirm which writer is a current MSA member]`

## Open items before submission

- Confirm the expected Mg against the powder lot's certificate of analysis. The draft uses the lab's 0.5–0.7 wt% value, but the AlSi10Mg specification (DIN EN 1706 / ASTM F3318) is 0.20–0.45 wt% Mg, and a reviewer may notice the difference.
- If the voltage series runs before December 1, move its results into the preliminary data and shift the 2027 timeline toward Goals 3–5.
- Fill in the applicant's major and class standing (junior or senior by the start of the work), the printer/partner for the LPBF material, and the career-goals sentence.
- Confirm the operator and date of the April 15 kV session before it is presented as lab data.
- Check the live application form for page-format rules (font, margins, whether references count) and for the current letter requirements.

## Sources

- Program page: [microscopy.org/undergraduate-research-scholarship-program](https://microscopy.org/undergraduate-research-scholarship-program), read via search snippets because the site refuses connections from the CI runner
- Lab data and plans: [`docs/eds_parameter_summary.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_parameter_summary.md) and [`docs/eds_voltage_series_plan.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_voltage_series_plan.md) on the beam-current branch (PR #15); issues #1, #12, and #16; PRs #8, #11, and #13
- Literature-gap statement: [`outputs/msa_2027_strategic_initiatives/need_evidence_answer.md`](outputs/msa_2027_strategic_initiatives/need_evidence_answer.md)
