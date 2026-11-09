# 2027 MSA Undergraduate Research Scholarship — CALIBER Proposal (Draft)

Working draft for the [MSA Undergraduate Research Scholarship Program](https://microscopy.org/undergraduate-research-scholarship-program). The research proposal (between the horizontal rules below) is held to the program's **3-page limit**; the [PDF render](2027_msa_undergraduate_research_scholarship_proposal.pdf) uses Carlito, which has the same letter widths as Calibri, at 11 pt with 1-inch margins on US Letter, references included, so it should stay within 3 pages when pasted into Word in Calibri 11 pt. The [Word version](2027_msa_undergraduate_research_scholarship_proposal.docx) has the proposal (pages 1–3, numbered "1 of 3" and so on), the Expenditure of Funds, and the CV in Calibri 11 pt, each part starting on a new page. The only bracketed items left are the applicant's own details (SEM course, graduation date, contact information). The Expenditure of Funds and CV are separate documents and do not count toward the limit.

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

# Testing Physics-Based Rules for Accurate SEM-EDS of Magnesium in Additively Manufactured AlSi10Mg

<p class="meta"><strong>Applicant:</strong> Ronnie Guymon, junior in Mechanical Engineering, Brigham Young University</p>
<p class="meta"><strong>Supervisor:</strong> Prof. Sterling G. Baird, BYU · <strong>Period:</strong> January to December 2027 · <strong>Request:</strong> $3,000</p>
<p class="meta"><strong>Facility:</strong> BYU Electron Microscopy Facility (Thermo Fisher Apreo SEM, EDAX Octane Plus EDS)</p>

## 1. Introduction

Quantitative energy-dispersive X-ray spectroscopy (EDS) in a scanning electron microscope (SEM) is only as good as the settings used to collect the spectrum. Beam energy, beam current, and acquisition time control how many X-rays the sample produces, how many are absorbed before they leave it, and how many artifacts the detector adds. With measured standards, EDS can reach about 5% relative uncertainty. Standardless analysis can be off by 30%, and normalizing the total to 100% hides the error [1]. Most operators use general defaults, such as 15 to 20 kV and "enough" counts, that were not designed for light, low-concentration elements in new alloys.

Our group is building CALIBER, a software tool that recommends SEM, EDS, EBSD, and XRF settings for a given sample and measurement goal. It combines the published literature, physics models, and our own measurements, and it updates its recommendations as new data come in. Its first test material is AlSi10Mg made by laser powder bed fusion (LPBF). Magnesium makes up less than 1 wt% of this alloy, yet it controls precipitation hardening, and its X-ray peak sits on the shoulder of an aluminum peak more than 100 times stronger. Our literature review found no controlled study of SEM-EDS settings for Mg in LPBF AlSi10Mg that was checked against an independent bulk analysis. The settings in published work are examples, not tested choices.

My first measurements show that the problem is real (Table 1). The vendor's standardless software reported 1.64 wt% Mg at 15 kV and 0.94 wt% at 5 kV, both well above the 0.20 to 0.45 wt% that the powder supplier specifies. At 5 kV the Mg peak is clearly detected, about 10σ above background, but its net intensity changes by about 30% depending on how the aluminum tail and background beneath it are modeled, three times its counting error. When I ran the vendor's k-ratios through the independent matrix correction in NIST DTSA-II [2], Mg still came out at 0.90 wt%. The error is in the measured peak intensities, not the correction, so more counts alone will not fix it. The 15 kV result also failed a physics check: from 5 to 15 kV the Mg-to-Al intensity ratio rose by a factor of 1.52, where X-ray generation and absorption predict a drop to 0.86. Since September I have measured the probe current with a Faraday cup and collected 5 kV spectra from 0.77 to 5.6 million counts, including eight replicates of 1 million counts each. In November, on a newly polished sample, the C and O peaks were clear at 5 kV, only a small O peak remained at 10 kV, and both were nearly gone at 20 kV, as expected for a thin surface film.

<p class="caption"><strong>Table 1.</strong> Preliminary EDS of one LPBF AlSi10Mg sample (vendor standardless quantification, normalized to 100%).</p>

| Session | Beam energy | Total counts | Live time | Mg (wt%) | Si (wt%) | O (wt%) |
|---|---|---|---|---|---|---|
| April 30, 2026 | 15 kV | 4.44 million | 461 s | 1.64 | 9.47 | 8.10 |
| August 2026 | 5 kV | 0.65 million | 328 s | 0.94 | 11.15 | 1.68 |
| Powder specification | | | | 0.20–0.45 | 9.0–11.0 | |

To explain these results, I proposed a rule for choosing beam energy, which we then refined together. X-rays made deep in the sample leave along a slanted path to the detector that is 1.74 times their depth at our 35.1° take-off angle, and some are absorbed on the way out. The rule says a line can be quantified reliably only if this exit path, measured from the deepest point where the line is produced [3], is shorter than one attenuation length for that X-ray. For AlSi10Mg, Si Kα sets the limit at 7.6 kV. Of the 5, 10, 15, and 20 kV settings in routine use, only 5 kV should give clean results for Al, Si, and Mg. O Kα fails at all four, in line with long-standing advice not to quantify lines below 1 keV [4]. Related rules for beam current and acquisition time follow from dead time and counting statistics [5, 6]. This project tests these rules against an independent measurement of the true composition and turns the results into CALIBER's first validated recommendations.

## 2. Goals

1. **Measure the true composition.** Measure Mg in the printed sample and in its starting powder by ICP-MS, so EDS accuracy is judged against a measurement instead of a nominal value. Comparing the two also shows whether Mg evaporated during printing.
2. **Test the voltage rule.** Collect standards-based, un-normalized EDS at 5, 10, 15, and 20 kV and choose among three outcomes written down in advance: the rule holds, the rule is too strict, or the rule needs a correction for surface oxide and contamination, which matter most at 5 kV.
3. **Find the usable beam current.** Measure the actual probe current, dead time, and pulse pile-up at each current setting, and choose the dead-time range from data. This settles the gap between the 10% or less that NIST recommends for trace work [6] and the 25 to 30% often used for speed.
4. **Find when longer acquisition stops helping.** Find the count level where the scatter between replicate spectra grows larger than their counting error, so more time no longer improves accuracy, while tracking carbon buildup.
5. **Validate and share.** Enter each tested rule into CALIBER with its measured uncertainty, release the spectra, scripts, and session records openly, and present the results at M&M 2027.

## 3. Methods

**Samples and reference composition.** I will section, mount, and polish LPBF AlSi10Mg printed from virgin powder on the University of Utah's Aconity MIDI printer (Prof. Ashley Spear's group). I will record the final polishing step, because embedded colloidal silica would read as Si and O in the top 0.4 µm that the beam samples at 5 kV, and I will store polished samples in a vacuum desiccator and plasma-clean them before each session. For the reference composition, I will work with Prof. Devin Rappleye's group (BYU Chemical Engineering) to digest offcuts of the printed sample and the powder and analyze them by ICP-MS (Agilent 8900). Acid-only digestion does not fully recover Si, so Si will come from wavelength-dispersive XRF (Rigaku Primus II, BYU Geological Sciences) or a digestion that includes hydrofluoric acid.

**Instrument, standards, and quality checks.** All EDS work uses the Apreo SEM and EDAX Octane Plus silicon-drift detector at the 10 mm analytical working distance. The lab has already bought pure standards: 99.99% Al, a Si wafer, and an MgO crystal, which we section and polish without water because it would not cleave. I will give the standards the same thin carbon coat as the sample and collect them in the same session at every voltage. The pure Al spectrum also gives the real shape of the Al tail under the Mg peak. Each session starts with quality checks: energy calibration, detector resolution, counts per nA·s on the Si wafer, and a Duane–Hunt check for charging [5]. I will read the probe current on the Faraday cup before and after every spectrum and record it with the spectrum, because the k-ratio depends on electron dose.

**Experiment 1: voltage series (Goal 2).** I will analyze the same marked region at 5, 10, 15, and 20 kV, keeping the amplifier time fixed and adjusting the probe current to hold dead time constant. Replicate scans on nearby areas will add up to about 3% counting precision on Mg, or about 7 million counts at 5 kV. We wrote down seven predictions before collecting data. For example, standards-based Si and Mg should hold steady within counting error at 5 kV and drift in the order the rule predicts at higher voltages. Apparent C and O should fall about tenfold from 5 to 20 kV as a surface film becomes a smaller part of the analyzed volume.

**Experiment 2: beam current and dead time (Goal 3).** At 5 kV I will step through the current settings and record the measured current, dead time, count rate, the Al sum peak at 2.97 keV, and the Mg-to-Al intensity ratio. The usable dead-time range ends where that ratio moves away from its low-dead-time value by more than the counting error.

**Experiment 3: acquisition time (Goal 4).** Building on the September replicates, I will collect five or more spectra at each count level on fresh nearby areas and compare their scatter with the counting error each one predicts. I will also compare one long acquisition with several short ones of the same total live time. Tracking how the C peak grows, and whether Mg drifts, as the dose builds will set a dose limit for each spot.

**Analysis.** I will fit spectra with our Poisson-weighted peak model, which gives net intensities and Currie detection limits [7], and quantify them against same-session standards in DTSA-II with a φ(ρz) matrix correction [2]. I will report un-normalized totals, with 98 to 102% as a health check, next to the vendor's standardless results, and split each condition's error against the ICP-MS value into counting and systematic parts. I will judge each result against the rules written in advance and enter the tested rule into CALIBER with its measured uncertainty, completing the first full pass through CALIBER's feedback loop.

## 4. Timeline, outcomes, and significance

| 2027 | Work |
|---|---|
| Jan–Feb | Mount and coat standards; ICP-MS reference composition; quality checks; M&M 2027 abstract |
| Mar–Apr | Experiment 1: voltage series (four sessions plus standards) |
| May–Jun | Experiment 2: beam current, dead time, and pile-up |
| Jul | Experiment 3: acquisition time; enter results in CALIBER |
| Aug | Present at M&M 2027 |
| Sep–Dec | Journal manuscript, open data release, and extension to the lab's next alloys |

**Expected outcomes.** This project will produce (1) the first SEM-EDS settings study for LPBF AlSi10Mg checked against an independent composition measurement; (2) tested or corrected rules for beam energy, current, and acquisition time, each with a measured uncertainty; (3) an open dataset and analysis scripts that any EDS user can rerun; and (4) CALIBER's first experimentally validated recommendations, which our lab will extend to other alloys. I will prepare the samples, run the sessions, and analyze the data. This will train me in standards-based quantitative microanalysis, which I plan to use in a career developing and analyzing materials for aerospace applications.

<div class="refs">

**References**

1. Tong, V. & Mingard, K. *Measurement uncertainties of energy dispersive X-ray spectroscopy in the SEM (SEM-EDX/EDS)*. NPL Report MAT 135 (2026). [doi:10.47120/npl.mat135](https://doi.org/10.47120/npl.mat135)
2. Ritchie, N. W. M. Spectrum simulation in DTSA-II. *Microsc. Microanal.* 15, 454–468 (2009). [doi:10.1017/S1431927609990407](https://doi.org/10.1017/S1431927609990407)
3. Kanaya, K. & Okayama, S. Penetration and energy-loss theory of electrons in solid targets. *J. Phys. D* 5, 43–58 (1972). [doi:10.1088/0022-3727/5/1/308](https://doi.org/10.1088/0022-3727/5/1/308)
4. Statham, P. J. Limitations to accuracy in extracting characteristic line intensities from X-ray spectra. *J. Res. NIST* 107, 531–546 (2002). [doi:10.6028/jres.107.045](https://doi.org/10.6028/jres.107.045)
5. Goldstein, J. I. et al. *Scanning Electron Microscopy and X-Ray Microanalysis*, 4th ed. (Springer, 2018).
6. Newbury, D. E. & Ritchie, N. W. M. Performing elemental microanalysis with high accuracy and high precision by SEM/SDD-EDS. *J. Mater. Sci.* 50, 493–518 (2015). [doi:10.1007/s10853-014-8685-2](https://doi.org/10.1007/s10853-014-8685-2)
7. Currie, L. A. Limits for qualitative detection and quantitative determination. *Anal. Chem.* 40, 586–593 (1968). [doi:10.1021/ac60259a007](https://doi.org/10.1021/ac60259a007)

</div>

<!-- proposal:end -->

---

## Expenditure of Funds (separate document; $3,000)

<!-- budget:start -->

Of the $3,000 requested, $2,000 will be used as my research stipend, and the remaining $1,000 will be used for sample production, polishing, and preparation. My supervisor's laboratory covers microscope time and equipment, as listed under other funding sources below.

| Item | Amount |
|---|---|
| Student research stipend: about 125 hours from February to August 2027, paid through BYU student payroll | $2,000 |
| Sample production, polishing, and preparation: materials for producing and sectioning the AlSi10Mg samples, mounting resin, grinding papers, polishing cloths and suspensions, carbon-coating supplies, and SEM stubs, for the samples and the Al, Si, and MgO standards | $1,000 |
| **Total** | **$3,000** |

**Other funding sources.** Prof. Baird's laboratory pays for SEM and EDS time at the BYU Electron Microscopy Facility, the Al, Si, and MgO standards it has already bought, and laboratory equipment. ICP-MS access is through Prof. Devin Rappleye's group (BYU Chemical Engineering), and WDXRF through Kevin Rey (BYU Geological Sciences). Travel to present at M&M 2027 is not part of this request; I will apply for MSA's student travel awards to cover it. DTSA-II, HyperSpy, and our analysis scripts are free and open source.

<!-- budget:end -->

**Why the award does not pay for microscope time.** MSA's program page says: "MSA scholarship funds are generally approved for student stipends, supplies, and occasionally for limited travel essential to proposed studies. Fees for use of instruments, extensive travel, or purchase of/or contribution toward purchase of, laboratory equipment are generally considered to be part of the institutional and/or advisor's commitment to the research project." A budget spent on instrument fees asks MSA for what it expects the advisor to provide, so microscope hours go under other funding sources. For the same reason, keep the $1,000 line to materials and consumables: if sample production means paying for time on the printer, MSA is likely to read that as an instrument fee too. Before submitting, confirm with Prof. Baird that the lab covers instrument time, and confirm the stipend rate.

## Curriculum vitae (separate document)

MSA asks for a CV "including details of education and/or training in microscopy, and a brief statement of career goals." Fill in the bracketed items, and keep it to one page.

<!-- cv:start -->

**Ronnie Guymon**\
`[email]` · `[phone]` · Brigham Young University, Provo, Utah

**Education**
- B.S. in Mechanical Engineering, Brigham Young University, expected `[month year]`; junior standing
- `[SEM course number and title]`, BYU, fall 2026

**Microscopy training**
- SEM, EDS, and EBSD training at the BYU Electron Microscopy Facility, including EDS training with Mike Standing (July 27, 2026)
- Introductions to ICP-MS (Agilent 8900, BYU) and to wavelength-dispersive and handheld XRF with Kevin Rey, BYU Geological Sciences (July 2026)

**Research experience:** undergraduate researcher, Vertical Cloud Lab (Prof. Sterling G. Baird), BYU, `[start month]` 2026 to present
- Coordinated printing of LPBF AlSi10Mg samples on the University of Utah's Aconity MIDI printer (April 2026)
- Collected SEM-EDS spectra of the printed alloy at 15 kV (April 30, 2026, with Gage Erickson) and 5 kV (August 2026), then measured probe current with a Faraday cup, controlled dead time, and collected replicate spectra (September 2026)
- Collected EDS spectra at Sobol-sampled combinations of beam energy, current, and count total to start the lab's optimization dataset (October and November 2026)
- Quantified spectra in NIST DTSA-II and wrote HyperSpy/eXSpy analysis scripts in Python (August to September 2026)
- Proposed the absorption-based beam-voltage rule tested in this proposal, the overvoltage floor (U₀ ≥ 1.5), and the 1-million-count doubling ladder in CALIBER's EDS plan (August to September 2026)
- Polished AlSi10Mg samples and began preparing pure-element standards; sourced the Al, Si, and MgO standards and a final-polish diamond suspension that the supplier confirmed is free of silica and alumina; arranged the ICP-MS analysis (September to November 2026)
- Explored saved EBSD patterns in kikuchipy and designed the phase-list and dictionary-indexing tests run on them (July 2026)

**Memberships:** Microscopy Society of America, student member (since `[month]` 2026)

**Statement of career goals.** I want a career in materials science, developing and analyzing materials for aerospace applications. Microscopy will be one of my main tools. Building my SEM and microanalysis skills will help me understand the materials I work with and how to modify and improve them to reach the properties a design needs. `[Optional: a sentence on graduate school or the kind of role you want.]`

<!-- cv:end -->

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
| Fri Oct 16 | Ronnie, Gage | Ask MSE Supplies for the certificate of analysis for our lot of MSE PRO AlSi10Mg (MP0203). MSE specifies 0.20–0.45 wt% Mg; the certificate gives the lot's actual value. |
| Fri Oct 23 | Ronnie | Confirm the surface of the April 30 run: the byu-vcl PR 95 table calls it "non-flat". If it was a fracture surface, swap Table 1's 15 kV row for the polished May 22 runs (1.42–1.43 wt% Mg) and drop the ×1.52 consistency check, which assumes a flat sample. |
| Fri Oct 30 | Ronnie | **CV** with the SEM course number and the career-goals statement |
| Fri Nov 6 | Sterling | Confirm the stipend rate and hours (BYU student payroll) and that lab funds cover instrument time |
| Fri Nov 20 | Ronnie | If the voltage series has run (the carbon coater returns at the end of October), move its results into the preliminary data and shift the timeline toward Goals 3–5 |
| Fri Nov 20 | Ronnie | Letters received; final PDF within 3 pages; check the live form for letter uploads and any format rules |
| Tue Nov 24 | Ronnie | **Submit** the form, proposal, budget, CV, and any letters the form requests |
| ~Feb 15, 2027 | — | Awards announced; spend funds within one year; M&M 2027 abstracts are typically due in mid-February (check the date) |

## Sources

- Program page: [microscopy.org/undergraduate-research-scholarship-program](https://microscopy.org/undergraduate-research-scholarship-program), read from the Internet Archive copy of March 8, 2026 because the site refuses connections from the CI runner; dues from [Join MSA](https://microscopy.org/Join-MSA)
- Printing and the April 30 session: byu-vcl issue 77 and PR 95
- Powder: MSE PRO AlSi10Mg, MP0203, 15–45 µm, ordered January 2026 (byu-vcl issue 8); composition from [MSE's product page](https://web.archive.org/web/20260626003458/https://www.msesupplies.com/products/mse-pro-alsi10mg-aluminum-based-metal-powder-for-additive-manufacturing-3d-printing) (Mg 0.2–0.45 wt%, Si 9.0–11.0 wt%)
- Since October 10: MgO cleave and polish plan (PR #20), Sobol-sampled data collection (#21, #24), and the November 5/10/20 kV observations (PR #6)
- Lab data and plans: [`docs/eds_parameter_summary.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_parameter_summary.md) and [`docs/eds_voltage_series_plan.md`](https://github.com/vertical-cloud-lab/caliber/blob/claude/issue-1-20260909-0027/docs/eds_voltage_series_plan.md) on the beam-current branch (PR #15); issues #1, #12, and #16; PRs #8, #11, and #13
- Literature-gap statement: [`outputs/msa_2027_strategic_initiatives/need_evidence_answer.md`](outputs/msa_2027_strategic_initiatives/need_evidence_answer.md)
