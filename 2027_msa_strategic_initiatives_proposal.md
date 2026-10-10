# 2027 MSA Strategic Initiatives — CALIBER Proposal (Draft)

Working draft for the [MSA Strategic Initiatives program](https://microscopy.org/strategic-initiatives), 2027 call. The submission package (cover page, three-page narrative, budget justification) sits between the `submission` markers below and is rendered in the [PDF](2027_msa_strategic_initiatives_proposal.pdf) to MSA's format rules: Times-metric 12 pt, single spaced, 1 in margins, US Letter. The budget must also be entered in MSA's Excel template. Citations draw on the Edison research reports in [`outputs/msa_2027_strategic_initiatives/`](outputs/msa_2027_strategic_initiatives/).

## Call requirements (verified)

- **Deadline:** 11:59 PM Eastern, November 1, 2026 (a Sunday), per MSA's 2027 announcement email; the lab is targeting October 30 (see the checklist below)
- **Funding:** up to $15,000 for one year or $20,000 total over two years; a two-year budget must state the amount for each year, and Year 2 is contingent on Year 1 progress, so Year 1 needs substantive, attainable goals; 3–4 awards expected; funding begins in the spring after MSA's Winter Council meeting
- **Eligibility:** the primary applicant must be a current MSA member
- **Package:** (1) cover page with the title, project leader(s) and full contact information, names, affiliations, and contact information of other key personnel, and an executive summary of six sentences or fewer; (2) narrative of no more than three pages under four required headers: *Strategic Area Being Addressed and Justification*, *Details of the Proposal*, *Innovation and Impact*, *Plan for Long-Term Support*; (3) budget justification, line by line (two pages maximum in the 2025 guidelines; a 2026 revision reportedly cuts this to one page, so this draft keeps it to one); (4) budget in MSA's Excel template, as other formats are not accepted. Submitted through MSA's online form.
- **Format:** single spaced; margins of at least 0.5 in; no more than 15 characters per inch (e.g., Times New Roman 12 pt); no more than 64 lines per page; non-conforming applications may be rejected
- **Review weights:** alignment with the areas of emphasis (30%), importance to MSA's mission and vision (30%), innovativeness (30%), feasibility and continued support beyond the award (10%). Bold, higher-risk proposals are favored over safe, low-impact ones. The budget is reviewed separately and does not affect the merit score; salary support meant to replace volunteer effort is discouraged.
- **Areas targeted:** Area 2 (MSA-branded open-source tools) and Area 6 (collection, preservation, and dissemination of microscopy information) as primary; Areas 1 (students), 3 (member benefits), and 5 (partnerships) as secondary

Sources: the program page (2026 call, archived April 11, 2026), MSA's *Strategic Initiatives Submission Guidelines* (August 2025), and the 2027 announcement email quoted in PR #14. microscopy.org refuses connections from the CI runner, so check the live 2027 guidelines and template before submitting.

---

<!-- submission:start -->

<div class="cover">

# The MSA Microanalysis Parameter Commons

<p class="subtitle">MSA-branded open-source tools and a preserved knowledge base for choosing high-fidelity SEM, EDS, EBSD, and XRF acquisition parameters</p>

<p class="meta">MSA Strategic Initiatives Program, 2027 · Request: $20,000 over two years (Year 1: $9,000; Year 2: $11,000)</p>

## Project leader

Sterling G. Baird, Assistant Professor, Department of Mechanical Engineering, Brigham Young University, 350-Q EB, Provo, UT 84602 · sterling.baird@byu.edu

## Key personnel

- **Ronnie Guymon**, undergraduate researcher, Department of Mechanical Engineering, Brigham Young University: student lead for the curation corps and validation benchmark · `[email]`
- **Mike Standing**, BYU Electron Microscopy Facility: expert review of SEM, EDS, and EBSD records; benchmark instrument sessions · `[email]`
- **Prof. Ashley Spear**, Department of Mechanical Engineering, University of Utah: laser powder bed fusion specimens for the benchmark · `[email]`
- **Prof. Devin Rappleye**, Department of Chemical Engineering, Brigham Young University: ICP-MS ground-truth composition · `[email]`
- **Kevin Rey**, Department of Geological Sciences, Brigham Young University: WDXRF ground truth and XRF records · `[email]`

## Executive summary

Quantitative SEM, EDS, EBSD, and XRF results depend on acquisition parameters, yet the reasoning behind "recommended" settings is scattered across decades of literature, vendor software, and the memories of senior microscopists. We propose the MSA Microanalysis Parameter Commons: an MSA-branded, open-source release of CALIBER, a literature-grounded, uncertainty-aware recommender for acquisition parameters, paired with a curated, versioned, DOI-citable knowledge base that records *why* each setting is chosen and links to MSA's own archives. An open, ground-truthed benchmark on additively manufactured aluminum alloys will fill a documented gap, since no controlled acquisition-parameter study exists for this material class. Undergraduate MSA student members will curate records under expert review, and results will reach members and adjacent communities through open webinars, an M&M tutorial, and *Microscopy Today*. Year 1 delivers the open-source release, 50 reviewed records, and the first benchmark campaign; Year 2 delivers version 1.0, 150 or more records, the public benchmark dataset, and a governance handoff to MSA's EM Data Analysis and Management Focused Interest Group. The initiative addresses Areas 2 and 6 directly and serves MSA's mission of fostering research, innovation, advancement, and promotion of microscopy.

</div>

<!-- narrative:start -->

## Strategic Area Being Addressed and Justification

This initiative targets **Area 2** (MSA-branded development and dissemination of open-source tools for microscopy, microanalysis, and data management) and **Area 6** (collection, preservation, and dissemination of technical procedures, basic theory, and MSA archived material). It also involves students (Area 1), adds a recurring member benefit (Area 3), and builds academic partnerships (Area 5).

**Parameters decide fidelity.** Standards-based SEM-EDS can reach about ±5% relative uncertainty, while standardless analysis can err by ±30%, and normalized totals hide the error [1]. Raising EBSD collection speed from 54 to 154 patterns/s cut correct indexing from 34.9% to 9.3% [2], and a 12-phase candidate list in place of the correct two yielded *zero* correct assignments despite ideal beam settings [3]. XRF has over-reported trace Mg in aluminum by 5000% relative [4]. Our own work on laser powder bed fusion (LPBF) AlSi10Mg shows the same thing: standardless EDS reported 0.94–1.64 wt% Mg, depending on beam energy, for an alloy expected near 0.5–0.7 wt%, and the fraction of reliably indexed EBSD points rose from about 40% to 77% after a beam-current correction alone.

**The reasons behind settings are poorly preserved.** Standards such as ISO 22309 and ASTM E1508 give operating thresholds (overvoltage ≥ 1.8, take-off near 35°) but not the derivations or validation data needed to adapt them to a given detector, alloy, and goal; vendor-constrained algorithms left one comparison unable even to explain why two standardless systems disagreed [1]. FAIR metadata schemas record acquisition context but, by design, not the rationale for it [5], and practical expertise demonstrably leaves science when practitioners retire [6]. Open tools such as HyperSpy, kikuchipy, EMsoft, and napari analyze data after acquisition; none recommends settings, cites its sources, or reports its own uncertainty [7,8]. And much of the source knowledge is already MSA's: the strongest parameter studies and ecosystem papers sit in *Microscopy and Microanalysis* and the M&M proceedings [3,8,9], where they are hard to find and act on.

## Details of the Proposal

**O1 — MSA-branded open-source CALIBER.** A permissively licensed release of the recommender, the uncertainty-aware feedback loop that updates recommendations as measurements arrive, and corpus-building tools, with an install-free web demo. It interoperates with HyperSpy and kikuchipy data models and NeXus metadata [5] rather than replacing them. Branding and hosting are agreed with Council at the start.

**O2 — The Parameter Commons.** A public, versioned knowledge base of rationale records (per modality × parameter × material class: recommended range, governing physics, primary sources, known failure modes), released with DOIs, with a contribution and review workflow and links into M&M proceedings and *Microscopy Today*. Seed parameters: EDS accelerating voltage, acquisition time (total counts), and beam current; EBSD beam current, voltage, and phase list; a baseline SEM imaging set.

**O3 — Open validation benchmark.** A pre-registered, ground-truthed parameter study on LPBF Al-Si specimens: 5/10/15/20 kV voltage series, beam-current and dead-time mapping, and count-level stopping rules for EDS; beam current and phase-list tests for EBSD; ICP-MS and WDXRF as independent composition references. Raw spectra and patterns are archived and re-analyzed outside vendor software, so recommended and naive settings can be compared by anyone.

**O4 — Students, training, and promotion.** A corps of 8 undergraduate MSA student members curates records with bounded tasks, mentored review, and visible credit on each DOI'd release [10]. Two open webinars through MSA's online channels (open to non-members), course-ready tutorial notebooks, an M&M tutorial, and a *Microscopy Today* article carry the work to members and to the additive manufacturing, materials, and geoscience communities that use these instruments daily but rarely engage with MSA.

| | Year 1 goals (basis for Year 2 continuation) | Year 2 goals |
|---|---|---|
| Q1–Q2 | Branding and hosting agreement; record schema; CALIBER v0.1 release; 50 reviewed seed records; 4 curators recruited | Benchmark dataset released with DOI and FAIR metadata; contribution workflow opens to members; CALIBER v1.0 with XRF coverage |
| Q3–Q4 | First benchmark campaign run and analyzed; public beta; first webinar; M&M 2028 tutorial proposal; *Microscopy Today* draft | 150+ records; second webinar; M&M 2028 tutorial; governance handoff; final report to Council |

**Measuring success.** We will report against fixed targets: published records (50 in Year 1, 150 in Year 2); records linked to MSA archived material (25, 75); student curators trained (4, 8); webinar attendance, including the non-member share (target 40% non-members); web-demo sessions and repository downloads; benchmark dataset downloads; and, from an opt-in survey at demo sign-up and webinar registration, how many users are MSA members and how many joined after using the resource. Year 1 succeeds if v0.1, 50 reviewed records, and the first campaign are public; the initiative succeeds if the Commons is self-sustaining under MSA governance at the end of Year 2.

## Innovation and Impact

**Innovation.** CALIBER is the first open tool that works *before* acquisition: it retrieves the literature, applies physics models, and states its uncertainty for a given sample and goal, then updates as measurements arrive. Existing autonomous-microscopy work is task-specific and policy-driven rather than literature-grounded [7]. The Commons is also new in kind: protocol repositories keep the procedural *what*, while the Commons keeps the expert *why* (alternatives considered, failure modes, stopping criteria), each claim tied to a primary source and, where possible, to an open benchmark result. The benchmark is pre-registered, so the recommendations can be shown wrong; that risk is deliberate and is what makes the records trustworthy.

**Impact on MSA's strategic goals.** The initiative serves each part of MSA's mission. It *fosters research* with benchmark data the literature lacks and with more defensible measurements in every lab that adopts validated settings. It is an *innovation* in open microscopy infrastructure that connects the existing ecosystem instead of duplicating it. It *advances* practice by turning retirement-vulnerable expertise into citable, versioned records [6]. And it *promotes microscopy* by carrying MSA's name, and the case for rigorous microanalysis, to students and adjacent communities through tools whose every suggestion cites the microscopy literature. Members gain a recurring benefit: faster, more reliable data on unfamiliar samples. MSA becomes the recognized home of preserved, citable microanalysis practice, as rOpenSci and MolSSI became for their communities [10,11].

## Plan for Long-Term Support

This activity does not require financial support from MSA after the end of the Strategic Initiative funding. In Year 2, governance passes to MSA's EM Data Analysis and Management Focused Interest Group under a lightweight editor-plus-reviewers model, with a liaison to the Microanalysis Society's microanalytical-standards group (FIGMAS) for EDS records. This follows the precedent literature: society-branded resources survive when a trusted organization governs them, they are integrated with existing community activities (here, M&M and *Microscopy Today*), and contributors receive credit, and they fail when they rest on volunteers alone, detached from established infrastructure [10,11]. Ongoing costs are small (a static site, a public repository, and free DOI archiving), and the Vertical Cloud Lab will cover hosting and model-inference costs from its own funds. Curation continues through the BYU student pipeline and member contributions credited on each release.

<div class="refs">

**References.** [1] V. Tong, K. Mingard, NPL Report MAT 135 (2026). [2] S. I. Wright et al., *Ultramicroscopy* 159, 81 (2015). [3] K. Kaufmann, K. S. Vecchio, *Microsc. Microanal.* 27, 776 (2021). [4] P. Seidel et al., *Metals* 11, 736 (2021). [5] J. A. Taillon et al., *MRS Bull.* 50, 793 (2025). [6] P. F. Rainford et al., *Nat. Commun.* (2026). [7] S. V. Kalinin et al., *ACS Nano* 15, 12604 (2021). [8] J. Wei et al., *Microsc. Microanal.* 28 (2022). [9] M. Kühbach et al., *Microsc. Microanal.* 28 (2022). [10] D. S. Katz et al., *Comput. Sci. Eng.* 21, 8 (2019). [11] C. M. Schweik, in *Understanding Knowledge as a Commons* (MIT Press, 2007).

</div>

<!-- narrative:end -->

<div class="budget">

## Budget Justification

| Line item | Year 1 | Year 2 | Total |
|---|---|---|---|
| Student curator stipends | $4,000 | $4,000 | $8,000 |
| Instrument time for the open benchmark | $3,500 | $1,000 | $4,500 |
| Compute and hosting | $1,000 | $1,000 | $2,000 |
| Webinars and tutorial notebooks | $500 | $500 | $1,000 |
| M&M 2028 tutorial: student curator travel | — | $2,500 | $2,500 |
| Open-access publication of the benchmark | — | $2,000 | $2,000 |
| **Total requested** | **$9,000** | **$11,000** | **$20,000** |

- **Student curator stipends ($8,000).** Eight undergraduate MSA student members (four per year) at $1,000 each, about 60 hours of mentored curation apiece: extracting sources, drafting records, and revising them after expert review. These are training stipends that bring students into quantitative microanalysis (Area 1); they replace no volunteer effort. Expert review by members and all faculty effort remain volunteer contributions.
- **Instrument time ($4,500).** SEM, EDS, and EBSD sessions at the BYU Electron Microscopy Facility for the pre-registered benchmark in Year 1, and WDXRF sessions for XRF coverage in Year 2. Every session produces data released publicly. The Vertical Cloud Lab covers the remaining instrument time, specimens, standards, and sample preparation.
- **Compute and hosting ($2,000).** Language-model inference for the public web demo and cloud hosting for the demo and Commons site; DOI archiving through Zenodo is free.
- **Webinars and tutorial notebooks ($1,000).** Recording, captioning, and editing for two open webinars delivered through MSA's online channels, and packaging of course-ready notebooks.
- **M&M 2028 tutorial ($2,500).** Registration and travel for two student curators to co-present the tutorial and the benchmark results.
- **Open-access publication ($2,000).** Article processing charges so the benchmark paper is freely readable alongside its open dataset.

No indirect costs, faculty salary, or equipment purchases are requested. Year 2 funds are requested only on demonstrating the Year 1 goals.

</div>

<!-- submission:end -->

---

## Budget check against the call (working notes)

| Check | Status |
|---|---|
| Within the suggested ceiling for two years ($20,000) | Yes: $20,000 |
| Amount stated for each year (required for two-year proposals) | Added: Year 1 $9,000, Year 2 $11,000. The earlier draft gave only a total. |
| Substantive, fundable Year 1 goals (Year 2 is contingent) | Yes: v0.1, 50 records, first benchmark campaign, first webinar |
| Salary meant to replace volunteer effort (discouraged) | No faculty or staff salary. Student stipends are framed and capped as training stipends, and member review stays volunteer. |
| Not funding the institution's primary research mission | Instrument time cut from $6,000 to $4,500, limited to sessions whose data are released publicly, with the rest cost-shared by the lab. This was the line most likely to read as funding lab research. |
| Indirect costs | None requested. Confirm that BYU will accept a society award without indirect costs (see checklist). |
| Line items match MSA's Excel template | Transfer the table above into the official template. Other formats are rejected. |
| Budget justification length | One page, which meets either the two-page (2025) or one-page (2026) limit |

Changes from the September draft: the "M&M tutorial/workshop materials" line ($2,500) is now travel for student co-presenters, since M&M runs tutorials through its own program; the "dissemination" line ($1,500) is split into webinar production and an open-access charge for the benchmark paper; the "hosting, compute, and DOI" line no longer budgets for DOIs, which Zenodo issues free.

## Submission checklist

The hard deadline is 11:59 PM ET on Sunday, November 1, 2026. These dates work back from a submission target of Friday, October 30, which also meets an October 31 internal deadline.

| By | Owner | Task |
|---|---|---|
| Mon Oct 12 | Sterling | **Join MSA** as a regular member ($70; dues run January–December and are not pro-rated, so renew in January 2027 and 2028 to stay current through the award). This is required of the primary applicant. |
| Mon Oct 12 | Ronnie | **Join MSA** as a student member ($20). This is required for the scholarship anyway and lets the proposal count him as a student member. |
| Mon Oct 12 | Ronnie | From the live page, download the 2027 guidelines and the **budget Excel template**; check whether the page limits, deadline, or budget-justification length changed from the 2025 guidelines |
| Wed Oct 14 | Sterling | Ask the five collaborators to confirm their role, and get each one's email for the cover page. **Remove anyone who has not confirmed by Oct 23.** |
| Wed Oct 14 | Sterling | Email the EM-DAM FIG chair about the Year 2 governance handoff, and email strategic_initiatives@microscopy.org to confirm the 2027 deadline and MSA's branding and hosting expectations |
| Fri Oct 16 | Sterling | Check BYU's sponsored-research routing for a society award with no indirect costs, including any internal lead time |
| Fri Oct 23 | Ronnie | Enter the budget into the Excel template; finalize the cover page (fill each `[email]`) |
| Tue Oct 27 | Both | Final read: narrative within 3 pages, budget justification within 1 page, at most 64 lines per page, 12 pt, margins at least 0.5 in |
| Fri Oct 30 | Sterling | **Submit** through MSA's online form: cover page, narrative, and budget justification as one PDF, plus the Excel template |
| ~Feb 2027 | — | Decision after MSA's Winter Council meeting; funding begins in spring 2027 |

## Full references

1. Tong, V. & Mingard, K. *Measurement uncertainties of energy dispersive X-ray spectroscopy in the scanning electron microscope (SEM-EDX/EDS)*. National Physical Laboratory report MAT 135 (2026). https://doi.org/10.47120/npl.mat135
2. Wright, S. I. et al. Introduction and comparison of new EBSD post-processing methodologies. *Ultramicroscopy* 159, 81–94 (2015). https://doi.org/10.1016/j.ultramic.2015.08.001
3. Kaufmann, K. & Vecchio, K. S. An acquisition parameter study for machine-learning-enabled electron backscatter diffraction. *Microscopy and Microanalysis* 27, 776–793 (2021). https://doi.org/10.1017/s1431927621000556
4. Seidel, P. et al. Comparison of elemental analysis techniques for the characterization of commercial alloys. *Metals* 11, 736 (2021). https://doi.org/10.3390/met11050736
5. Taillon, J. A. et al. MaRDA FAIR materials microscopy and LIMS data working groups' community recommendations. *MRS Bulletin* 50, 793–804 (2025). https://doi.org/10.1557/s43577-025-00882-2
6. Rainford, P. F. et al. Knowledge preservation in the era of big science and AI: strategies for sustainable scientific research. *Nature Communications* (2026). https://doi.org/10.1038/s41467-026-72667-3
7. Kalinin, S. V. et al. Automated and autonomous experiments in electron and scanning probe microscopy. *ACS Nano* 15, 12604–12627 (2021). https://doi.org/10.1021/acsnano.1c02104
8. Wei, J. et al. Infrastructure for analysis of large microscopy and microanalysis data sets. *Microscopy and Microanalysis* 28 (2022). https://doi.org/10.1017/s1431927622011539
9. Kühbach, M. et al. Community-driven methods for open and reproducible software tools for analyzing datasets from atom probe microscopy. *Microscopy and Microanalysis* 28 (2022). https://doi.org/10.1017/s1431927621012241
10. Katz, D. S. et al. Community organizations: changing the culture in which research software is developed and sustained. *Computing in Science & Engineering* 21, 8–24 (2019). https://doi.org/10.48550/arxiv.1811.08473
11. Schweik, C. M. Free/open-source software as a framework for establishing commons in science. In *Understanding Knowledge as a Commons* (MIT Press, 2007). https://doi.org/10.7551/mitpress/6980.003.0014

Sources cited in earlier versions of this draft and still supported by the Edison reports, but cut to fit the three-page narrative: Singh et al. 2018 (low-kV EBSD), Bichlmeier et al. 2001 and Flude et al. 2017 (micro-XRF), Ghiringhelli et al. 2023 (shared metadata), Pratiush et al. 2025 (Mic-hackathon), Gammon et al. 2023 (imaging-protocol repository), and Toelch & Ostwald 2018 (teaching open-science tools).

## Appendix: supporting research artifacts

Full Edison reports backing this draft, in [`outputs/msa_2027_strategic_initiatives/`](outputs/msa_2027_strategic_initiatives/):

- [`need_evidence_answer.md`](outputs/msa_2027_strategic_initiatives/need_evidence_answer.md): quantitative evidence report with a proposal-ready needs statement, including the evidence table ([`need_evidence_artifact-00.md`](outputs/msa_2027_strategic_initiatives/need_evidence_artifact-00.md))
- [`deep_landscape_answer.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_answer.md): landscape review with ten distilled gap statements ([`deep_landscape_artifact-00.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_artifact-00.md)) and a tool-by-tool gap table ([`deep_landscape_artifact-01.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_artifact-01.md))
