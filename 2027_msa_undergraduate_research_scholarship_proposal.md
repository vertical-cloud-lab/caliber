# 2027 MSA Undergraduate Research Scholarship — CALIBER Proposal (Draft)

Working draft for the [MSA Undergraduate Research Scholarship Program](https://microscopy.org/undergraduate-research-scholarship-program). The two remaining bracketed items (SEM course number, career-goals statement) need the applicant's own input. The research proposal (between the horizontal rules below) is held to the program's **3-page limit**; the [PDF render](2027_msa_undergraduate_research_scholarship_proposal.pdf) shows it at 11 pt, 1-inch margins, US Letter, references included. Budget, CV, and letters are separate documents and do not count toward the limit.

## Program requirements

- **Deadline:** 11:59 PM Eastern, Tuesday, December 1, 2026; awards announced around February 15, 2027, and the funds must be spent within one year of the award date
- **Award:** up to $3,000. MSA generally approves student stipends and supplies, and occasionally limited travel essential to the study. Instrument-use fees, extensive travel, and laboratory equipment count as the institution's or advisor's commitment, and the budget must name those other funding sources.
- **Eligibility:** full-time undergraduate with junior or senior standing by the time the work begins; current MSA member; not previously funded by this program. The research must be finished before graduation (by prior agreement, one extra summer is allowed).
- **Application packet (official page):**
  1. Completed submission form
  2. Research proposal of **no more than three pages**, including at minimum an introduction, a methods section, and a description and itemization of the study's goals
  3. Budget showing how the award will be spent, with other funding sources named
  4. CV including education and/or training in microscopy, plus a brief statement of career goals
- **Letters:** the official page (archived March 8, 2026) lists no letters. Secondary listings ([SmartScholar](https://www.smartscholar.com/scholarship/microscopy-society-of-america-msa-scholarships-for-undergraduate-research/), [Appily](https://www.appily.com/scholarships/msa-undergraduate-research-scholarship-program)) ask for two reference letters, a letter from the lab supervisor, and a letter from an MSA member, which can be combined. The plan below covers all of them, since the submission form may still ask.
- **Encouraged:** awardees are encouraged to present a two-page paper or a post-deadline poster at M&M.

No font or margin rules are given beyond the three-page limit. microscopy.org refuses connections from the CI runner, so these requirements come from the archived page.

---

<!-- proposal:start -->

# Ground-Truthing Physics-Based Acquisition Rules for Quantitative SEM-EDS of Additively Manufactured AlSi10Mg

<p class="meta"><strong>Applicant:</strong> Ronnie Guymon, Brigham Young University · <strong>Supervisor:</strong> Prof. Sterling G. Baird, Mechanical Engineering, BYU</p>
<p class="meta"><strong>Facility:</strong> BYU Electron Microscopy Facility (Thermo Fisher Apreo SEM, EDAX Octane Plus EDS) · <strong>Period:</strong> January–December 2027 · <strong>Request:</strong> $3,000</p>

## 1. Introduction

Every quantitative SEM-EDS result depends on choices made before the first X-ray is counted. Accelerating voltage, beam current, and acquisition time set how many X-rays are generated, how many are absorbed on their way out of the sample, and how many artifacts the detector electronics add. Standards-based EDS can reach about ±5% relative uncertainty, while standardless analysis can err by ±30%, and normalizing totals to 100% hides the error [1]. In practice, operators fall back on generic defaults (15–20 kV, "enough" counts) whose derivations are rarely written down and were not designed for light minor elements in new alloys.

Our lab is building **CALIBER**, an AI-enabled platform that recommends SEM, EDS, EBSD, and XRF acquisition parameters for a given sample and analysis goal. It couples the characterization literature (through retrieval-augmented generation), physics models, and a growing in-house dataset, and an uncertainty-aware feedback loop revises its recommendations as measurements arrive. Its first test case is laser powder bed fusion (LPBF) AlSi10Mg, in which under 1 wt% Mg controls precipitation hardening but must be measured in the shoulder of an Al Kα peak more than 100 times stronger. Our literature review found no controlled SEM-EDS parameter study for Mg in LPBF AlSi10Mg checked against an independent bulk analysis, so the settings in published work are examples rather than validated optima. Our lab's EBSD work shows the same sensitivity: on this alloy, the fraction of reliably indexed points rose from about 40% to 77% when the beam current was raised fourfold.

Preliminary sessions on one LPBF AlSi10Mg sample show that the EDS problem is real and systematic (Table 1). Vendor standardless quantification reported 1.64 wt% Mg at 15 kV and 0.94 wt% at 5 kV, both above the 0.5–0.7 wt% on record for the powder, itself above the 0.20–0.45 wt% alloy specification. At 5 kV the Mg peak is clearly detected (about 10σ above background), but its net intensity shifts by roughly ±30% depending on how the Al Kα tail and background beneath it are modeled, about three times its counting error. When I passed the vendor's k-ratios through the independent matrix correction in NIST DTSA-II [2], Mg still came out at 0.90 wt%: the bias sits in the measured intensities, not the matrix correction, and more counts alone will not remove it. The 15 kV result also failed a physics consistency check: from 5 to 15 kV the Mg/Al net-intensity ratio rose ×1.52 where X-ray generation and absorption predict ×0.86, and 8.1 wt% apparent oxygen soaked up mass in the normalization. In September I began the current and counting work at 5 kV: Faraday-cup readings of 3.24–3.31 nA against a 3.2 nA set point, 29–30% dead time, spectra from 0.77 to about 5.6 million counts (Mg peak-to-background steady at 0.22–0.25 while signal-to-noise rose from about 11 to 30, as counting statistics predict), and eight replicate 1-million-count spectra.

<p class="caption"><strong>Table 1.</strong> Preliminary EDS of one LPBF AlSi10Mg sample (Apreo + EDAX Octane Plus, take-off 35.1°; vendor standardless eZAF, normalized).</p>

| Session | Beam energy | Total counts | Live time | Mg (wt%) | Si (wt%) | O (wt%) |
|---|---|---|---|---|---|---|
| Apr 30, 2026 | 15 kV | 4.44 M | 461 s | 1.64 | 9.47 | 8.10 |
| August 2026 | 5 kV | 0.65 M | 328 s | 0.94 | 11.15 | 1.68 |
| Powder record; spec. | — | — | — | 0.5–0.7; 0.20–0.45 | 9–11 | — |

To explain these results I proposed a voltage rule from absorption physics, which we then refined: a line is quantifiable only if its deepest X-ray production depth [3], lengthened 1.74× by the slanted 35.1° exit path to the detector, stays within its 1/e attenuation length — equivalently, an absorption factor f(χ) ≥ 0.75. For AlSi10Mg the binding line is Si Kα, which caps the beam energy at 7.6 kV, so of the 5/10/15/20 kV settings in routine use only 5 kV should quantify Al, Si, and Mg cleanly (O Kα fails at all four, consistent with long-standing advice not to quantify lines below 1 keV [4]). Companion rules for beam current and acquisition time follow from dead-time and counting statistics [5,6]. These rules are falsifiable. This project tests them against an independent measurement of the true composition and turns the outcome into CALIBER's first validated recommendations.

## 2. Goals

1. **Ground truth.** Measure Mg in the printed specimen, and in its powder (which also reveals any Mg lost to evaporation during printing), by ICP-MS after acid digestion, so EDS accuracy is judged against a measurement rather than a nominal value.
2. **Test the voltage rule.** Run a pre-registered 5/10/15/20 kV series with standards-based, un-normalized quantification, and decide among three outcomes written down in advance: the rule holds (H1), it is too conservative (H2), or it needs a surface-film term because shallow 5 kV sampling is biased by oxide and contamination (H3).
3. **Map beam current and dead time.** Measure delivered probe current per setting, dead time versus current, and the onset of pulse pile-up, then choose the dead-time band from data — settling the tension between the ≤10% that the NIST protocol recommends for trace work [6] and the 25–30% band that favors throughput.
4. **Set acquisition time by a stopping rule.** Find the count level at which scatter between replicate spectra exceeds the counting error they predict — the point where more time stops improving accuracy — while tracking carbon contamination.
5. **Validate and share.** Enter each tested rule into CALIBER with its measured uncertainty, release spectra, scripts, and session metadata openly, and present the results at M&M 2027.

## 3. Methods

**Samples and ground truth.** LPBF AlSi10Mg printed from virgin powder on the University of Utah's Aconity MIDI (Prof. Ashley Spear's group) is sectioned, mounted, and polished; the final polish is recorded because embedded colloidal silica reads as Si + O within the 0.4 µm sampling depth at 5 kV. Polished samples are stored in a vacuum desiccator and plasma-cleaned before each session. Offcuts of the printed specimen and the powder are digested and analyzed by ICP-MS (Agilent 8900, BYU) with Prof. Devin Rappleye's group (BYU Chemical Engineering); because acid-only digests under-recover Si, Si is taken from WDXRF (Rigaku Primus II, BYU Geology) or an HF-assisted digest. Once certified this way, the alloy also serves as a matrix-matched secondary standard.

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

**Expected outcomes.** (1) The first ground-truthed SEM-EDS acquisition study for LPBF AlSi10Mg, filling the gap our literature review identified; (2) validated or corrected rules for beam energy, current, and acquisition time, each with a measured uncertainty; (3) an open dataset and analysis scripts any EDS user can rerun; and (4) CALIBER's first experimentally validated recommendations, which the lab will extend to its alloy roadmap (Mn, Cr, Zr, Cu, Ti, Fe, Ni, Sc, Zn, and others). I will prepare the samples, run the sessions, and carry out the analysis, which trains me in standards-based quantitative microanalysis.

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

## Budget (separate document; $3,000)

| Item | Amount |
|---|---|
| Student research stipend: about 125 hours, February–August 2027, paid through BYU student payroll | $2,000 |
| Supplies for the ICP-MS ground truth: digestion acids and certified Mg, Al, and Si calibration solutions | $250 |
| Supplies for sample preparation and standards: polishing consumables, carbon-coating supplies, stubs, and a certified Al-Si-Mg reference material as an independent accuracy check | $350 |
| Travel to present the results at M&M 2027, Pittsburgh (student registration and part of the airfare) | $400 |
| **Total** | **$3,000** |

**Other funding sources (the program asks for these):** SEM/EDS instrument time at the BYU Electron Microscopy Facility, the Al, Si, and MgO standards already purchased (order 13279), and laboratory equipment are covered by Prof. Baird's laboratory funds. ICP-MS access is through Prof. Devin Rappleye's group (BYU Chemical Engineering), and WDXRF through Kevin Rey (BYU Geological Sciences). Remaining M&M travel costs will be sought from MSA's student travel awards. DTSA-II, HyperSpy/eXSpy, and the lab's analysis scripts are free and open source.

**Budget check against the program rules.** The September draft budgeted ICP-MS "instrument fees" and Zr and Ce standards for the lab's *next* alloys. MSA treats instrument fees as an institutional commitment, and a reviewer would see standards for other alloys as outside this project. Both lines are gone; the money moved to the stipend and to supplies this study uses. Travel is held to $400, inside "limited travel essential to the study". No equipment or instrument fees are requested.

## CV notes (separate document)

Microscopy education and training to list, drawn from issues #1, #2, #12, and #16 and PRs #6, #8, #11, and #13:

- SEM course, BYU, fall 2026 `[course number]`; EDS training with Mike Standing, BYU Electron Microscopy Facility (July 27, 2026)
- Coordinated printing of the LPBF AlSi10Mg specimens on the University of Utah's Aconity MIDI (April 2026)
- SEM/EDS of the printed alloy: 15 kV session with Gage Erickson (April 30, 2026); 5 kV sessions (August 2026); Faraday-cup current measurement, dead-time control, and replicate-spectrum acquisition (September 16, 23, and 30, 2026)
- Quantitative EDS analysis: NIST DTSA-II (detector definition, k-ratio quantification, standards workflow) and HyperSpy/eXSpy scripting in Python (August–September 2026)
- Proposed the absorption-based beam-voltage criterion, the U₀ ≥ 1.5 overvoltage floor, and the 1-million-count doubling ladder used in CALIBER's EDS plan (August–September 2026)
- Sourced EDS standards (Al, Si, MgO; order 13279, September 2026); arranged ICP-MS ground-truth analysis and a trial acid digestion of AlSi10Mg powder (September 2026)
- Metallographic preparation, ultrasonic cleaning of stubs, and vacuum-desiccator storage of polished samples (September 2026)
- EBSD: loaded and explored saved-pattern data in kikuchipy, and designed the phase-list, dictionary-indexing, and grain-reconstruction tests run on it (July 2026)
- Introductions to ICP-MS (Agilent 8900, BYU) and to WDXRF and handheld XRF (Kevin Rey, BYU Geological Sciences, July 2026)
- MSA student member (joining October 2026)

**Statement of career goals:** `[Ronnie writes this: 3–4 sentences in his own words, e.g., graduate study or industry work in materials characterization and the role microscopy will play]`

## Letters (separate documents)

- **Supervisor letter** confirming that the applicant and project are acceptable: Prof. Sterling G. Baird. Once he joins MSA (needed for the Strategic Initiatives proposal by October 12), this letter also serves as the **MSA-member letter**.
- **Two reference letters** from scientists or faculty familiar with the applicant's work:
  1. Mike Standing, BYU Electron Microscopy Facility, who trained the applicant on EDS and reviewed the measurement approach in September
  2. The instructor of the applicant's fall 2026 SEM course, who can speak to his microscopy coursework (alternates: Prof. Devin Rappleye or Kevin Rey)

## Submission checklist

The deadline is 11:59 PM ET on Tuesday, December 1, 2026. These dates work back from a Tuesday, November 24 submission, ahead of the Thanksgiving week.

| By | Owner | Task |
|---|---|---|
| Mon Oct 12 | Ronnie | **Join MSA** as a student member ($20). Dues run January–December and are not pro-rated, so **renew in January 2027** to stay a current member through the award. |
| Wed Oct 14 | Ronnie | Confirm eligibility: full-time, junior or senior standing by January 2027, and expected graduation after December 2027, or arrange the one-summer exception |
| Fri Oct 16 | Ronnie | **Request letters** (supervisor and MSA member: Sterling; references: Mike Standing and the SEM course instructor), attaching the draft proposal and CV, with a due date of Nov 20 |
| Fri Oct 16 | Ronnie, Gage | Request the powder's certificate of analysis from the supplier, to settle the 0.5–0.7 vs. 0.20–0.45 wt% Mg question |
| Fri Oct 23 | Ronnie | Confirm the surface of the April 30 run: the byu-vcl PR 95 table calls it "non-flat". If it was a fracture surface, swap Table 1's 15 kV row for the polished May 22 runs (1.42–1.43 wt% Mg) and drop the ×1.52 consistency check, which assumes a flat sample. |
| Fri Oct 30 | Ronnie | **CV** with the SEM course number and the career-goals statement |
| Fri Nov 6 | Sterling | Confirm the stipend rate and hours (BYU student payroll) and that lab funds cover instrument time; get a quote for the certified reference material |
| Fri Nov 20 | Ronnie | If the voltage series has run (the carbon coater returns at the end of October), move its results into the preliminary data and shift the timeline toward Goals 3–5 |
| Fri Nov 20 | Ronnie | Letters received; final PDF within 3 pages; check the live form for letter uploads and any format rules |
| Tue Nov 24 | Ronnie | **Submit** the form, proposal, budget, CV, and any letters the form requests |
| ~Feb 15, 2027 | — | Awards announced; spend funds within one year; M&M 2027 abstracts are typically due in mid-February (check the date) |

## Sources

- Program page: [microscopy.org/undergraduate-research-scholarship-program](https://microscopy.org/undergraduate-research-scholarship-program), read from the Internet Archive copy of March 8, 2026 because the site refuses connections from the CI runner; dues from [Join MSA](https://microscopy.org/Join-MSA)
- Printing and the April 30 session: byu-vcl issue 77 and PR 95
- Lab data and plans: [`docs/eds_parameter_summary.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_parameter_summary.md) and [`docs/eds_voltage_series_plan.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_voltage_series_plan.md) on the beam-current branch (PR #15); issues #1, #12, and #16; PRs #8, #11, and #13
- Literature-gap statement: [`outputs/msa_2027_strategic_initiatives/need_evidence_answer.md`](outputs/msa_2027_strategic_initiatives/need_evidence_answer.md)
