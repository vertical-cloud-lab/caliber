# 2027 MSA Strategic Initiatives — CALIBER Proposal (Draft)

Working draft for a proposal to the [MSA Strategic Initiatives program](https://microscopy.org/strategic-initiatives), 2027 call. Bracketed `[TODO]` items need lab input before submission. Citations are drawn from the Edison research reports in [`outputs/msa_2027_strategic_initiatives/`](outputs/msa_2027_strategic_initiatives/).

## Call constraints (2027 cycle)

- **Deadline:** 11:59 PM Eastern Time, November 1, 2026
- **Funding:** suggested level up to $15,000 for a one-year project or $20,000 total over two years; significantly higher possible for exceptional projects with major benefits to the Society; 3–4 awards expected
- **Eligibility:** primary applicant must be a current MSA member; detailed budget required
- **Scope:** bold, innovative *new* programs; not intended to sustain existing programs or the primary research/educational missions of institutions
- **Primary areas of emphasis targeted** (of the six listed in the call):
  - *Area 2:* MSA-branded development and dissemination of information and open source tools related to advances in microscopy, microanalysis, data management, and image analysis
  - *Area 6:* Collection, preservation, management, and dissemination of microscopy-related information, including technical procedures, basic theories, scientific backgrounds, MSA archived material, and related resources
- **Secondary areas touched:** student involvement (Area 1), member benefits (Area 3), academic/governmental/industrial partnerships (Area 5)

---

## Title

**The MSA Microanalysis Parameter Commons: MSA-branded open-source tools and a preserved knowledge base for selecting high-fidelity acquisition parameters, built on CALIBER**

*[Alternate: "CALIBER for the Community: An MSA-Branded Open Platform and Knowledge Commons for Microanalysis Acquisition Parameters"]*

## Applicant team

- **Principal applicant:** `[TODO: name — must be a current MSA member; confirm membership status]`
- **Co-applicants / advisors:** `[TODO: draw from the reviewer/collaborator shortlist — see issue 10]`
- **Host lab:** Vertical Cloud Lab `[TODO: institution details]`

## Requested support

$20,000 over two years *(scale to $15,000 / one year by dropping Year 2 items if preferred)*

## Summary

Quantitative microscopy lives or dies by acquisition parameters. Physical standards can hold SEM-EDS to roughly ±5% relative uncertainty while standardless analysis can err by ±30%, with normalization hiding the damage [1]; raising EBSD collection speed from 54 to 154 patterns per second dropped correct indexing from 34.9% to 9.3% [2]; and supplying a 12-phase candidate list instead of the correct two caused *zero* patterns to index correctly despite ideal beam settings [3]. Our own LPBF AlSi10Mg work mirrors this: standardless EDS over-reported trace Mg several-fold, and indexing yield swung from 40% to 80% on beam-current and phase-list corrections alone. The rationale behind "recommended" settings — why standards demand overvoltage ≥ 1.8, where defaults break down — is scattered across decades of literature, standards whose derivations are rarely documented, vendor-proprietary software, and the memory of senior microscopists; when they retire, it leaves with them [1,15].

We propose an MSA-branded **Microanalysis Parameter Commons**: (1) an open-source release of **CALIBER**, a retrieval-augmented, uncertainty-aware recommender that suggests literature- and physics-grounded SEM, EDS, EBSD, and XRF acquisition parameters for a stated sample and analysis goal, and (2) a curated, versioned, citable knowledge base that collects and preserves *why* parameters are chosen — technical procedures, underlying physics, and the derivations behind standard settings — cross-linked to MSA's own archives, where much of this knowledge already sits unorganized [12,13]. An open benchmark campaign on novel alloys fills a documented evidence gap (no controlled factorial acquisition studies exist for LPBF AlSi10Mg [1,3]), students earn stipends curating entries under expert review, and results flow through M&M tutorials, a Microscopy Today article, and MSA's web presence. The award funds a community resource, not our lab's research program.

## Alignment with the 2027 areas of emphasis

| Call area | How this initiative addresses it |
|---|---|
| **Area 2 — MSA-branded open source tools** (primary) | CALIBER's RAG pipeline, parameter recommender, and benchmark tooling released under a permissive license as an MSA-branded resource for microscopy, microanalysis, data management, and image analysis |
| **Area 6 — collection, preservation, dissemination of microscopy knowledge** (primary) | The Parameter Commons captures technical procedures, basic theory, and the scientific background behind acquisition settings in versioned, DOI-citable records, cross-linked to MSA archived material (M&M proceedings, Microscopy Today) |
| Area 1 — student involvement | Paid student curation corps; curation is a structured on-ramp into quantitative microanalysis |
| Area 3 — member benefits | Members get a practical tool that shortens time-to-good-data on unfamiliar samples; contributor recognition for members |
| Area 5 — partnerships | Academic and national-lab partners contribute validation datasets and expert review `[TODO: name partners]` |

## Background and need

- **Parameters determine fidelity, quantitatively.** Standards-based SEM-EDS can reach about ±5% relative uncertainty; standardless can reach ±30%, and normalized totals conceal errors [1]. EBSD throughput, frame averaging, voltage, binning, and above all phase-list selection each swing indexing success by tens of percentage points — one-frame patterns were almost entirely misclassified, and an over-inclusive 12-phase list produced zero correct assignments [2,3,4]. In XRF of Al alloys, minor Mg has been over-reported by 40% relative and trace Mg by 5000%, while matrix-matched calibration holds major elements below 5% error [5,6,7].
- **The "why" is sparsely documented and hard to access.** Standards such as ISO 22309 and ASTM E1508 supply operating thresholds (e.g., overvoltage ≥ 1.8, take-off near 35°) but not the derivations, uncertainty surfaces, or validation data needed to adapt them to a specific detector, alloy, and goal; investigators comparing two standardless systems could not even determine why their accuracies differed, because the algorithms and calibration databases were vendor-constrained [1]. Protocol repositories and methods sections preserve the procedural *what* but not the expert *why* — alternatives considered, failure modes, stopping criteria [8,11,14]. FAIR metadata schemas structure acquisition context but by design do not capture the causal rationale for choosing it [9,10]. And the practical expertise behind parameter choices demonstrably leaves science when experienced practitioners retire or move on [15].
- **Open tools stop short of guidance.** HyperSpy, kikuchipy, pyxem, EMsoft, DREAM.3D, ImageJ/Fiji, and napari are post-acquisition analyzers, simulators, or viewers; none recommends acquisition settings, grounds advice in citable literature, or quantifies its own uncertainty — and autonomous-microscopy work to date is task-specific and policy-driven rather than literature-grounded [8,11,13]. CALIBER is connective infrastructure over this ecosystem, not a duplicate of it.
- **The validation data don't exist yet.** No controlled, ground-truthed factorial study links acquisition settings to chemical and crystallographic fidelity for LPBF AlSi10Mg — published settings are examples, not validated optima [1,3,4]. The open benchmark in this initiative creates exactly that dataset, for the community.
- **Much of the source knowledge is already MSA's.** The strongest parameter studies and ecosystem papers appear in *Microscopy and Microanalysis* and M&M proceedings [3,12,13] — MSA archived material that the Commons would organize, cross-link, and make actionable (Area 6).

## Objectives and deliverables

1. **O1 — MSA-branded open-source CALIBER release.** Public repository (permissive license) containing the retrieval-augmented recommender, uncertainty-aware feedback loop, and corpus-building tools; MSA branding and hosting arrangement agreed with Council; built to interoperate with the existing open ecosystem (HyperSpy/kikuchipy data models, NeXus/NXem metadata [9]) rather than replace it. *Deliverables: v0.1 (Y1Q2), v1.0 (Y2Q2); documentation and install-free web demo.*
2. **O2 — The Microanalysis Parameter Commons.** A public, versioned knowledge base of parameter-rationale records (per modality × parameter × material class: the recommended range, the physics behind it, the primary sources, and known failure modes), with DOIs per release, a contribution/review workflow, and cross-links into MSA archives (M&M proceedings, Microscopy Today). *Deliverables: schema + 50 seed records (Y1Q2), 150+ records spanning SEM, EDS, EBSD, XRF (Y2Q4).*
3. **O3 — Open validation benchmark.** A published benchmark on novel alloy samples (laser powder bed fusion Al-Si and the broader alloy campaign) that fills the documented absence of controlled factorial acquisition studies [1,3]: raw spectra/patterns archived and re-analyzed offline outside vendor software, so recommended vs. naive parameters can be compared reproducibly; early-stopping quality heuristics (e.g., EBSD confidence-index screening after partial scans) evaluated and reported. *Deliverables: open dataset with FAIR metadata per MaRDA recommendations [9] (Y2Q1); benchmark report.*
4. **O4 — Dissemination and training.** M&M tutorial/workshop, a Microscopy Today article, and a student curation corps designed around what makes trainee curation sustainable: bounded tasks, structured mentorship and review, version control, and visible credit on DOI'd releases [15,16,17]. *Deliverables: workshop at M&M `[2027 and/or 2028]`; 6–10 student curators trained.*

## Work plan and timeline (two years)

| Period | Milestones |
|---|---|
| Y1 Q1 | MSA branding/hosting agreement; Commons record schema; seed extraction for the highest-impact parameters (EDS: accelerating voltage + `[TODO: second parameter under evaluation]`; EBSD: beam current, voltage, phase list; SEM imaging baseline set) |
| Y1 Q2 | CALIBER v0.1 open-source release; Commons alpha with 50 seed records; student curator recruitment |
| Y1 Q3 | Validation campaign 1 (LPBF Al-Si): archived raw data, offline re-analysis, uncertainty-aware feedback loop on recommended settings |
| Y1 Q4 | Public beta; M&M tutorial submission; Microscopy Today article draft |
| Y2 Q1 | Benchmark dataset release (FAIR metadata, DOI); community contribution workflow opens |
| Y2 Q2 | CALIBER v1.0; XRF modality coverage; 100+ records |
| Y2 Q3 | M&M workshop; assessment against success metrics |
| Y2 Q4 | 150+ records; sustainability handoff to `[TODO: MSA committee/FIG]`; final report to Council |

## Budget (draft — $20,000 over two years)

| Item | Amount |
|---|---|
| Student curation and development micro-stipends (6–10 curators × 2 yr) | $8,000 |
| Instrument time for the open validation benchmark (SEM/EDS/EBSD/XRF sessions) | $6,000 |
| Hosting, compute, and DOI/archiving costs (2 yr) | $2,000 |
| M&M tutorial/workshop materials and costs | $2,500 |
| Dissemination (open-access fees, Microscopy Today piece) | $1,500 |
| **Total** | **$20,000** |

`[TODO: adjust to institutional rates; confirm no overhead applies; detailed justification per MSA form]`

## Benefit to MSA and success metrics

- Positions MSA as the home of *preserved, citable* microanalysis practice — knowledge that currently evaporates with retirements [15] — under its own brand (Areas 2 and 6), following the model of societies that built trusted open resources (rOpenSci, MolSSI, ELIXIR) [16,18].
- A concrete, recurring member benefit: shorter time-to-reliable-data on unfamiliar samples.
- Metrics: number of published Commons records (target 150+); tool users/downloads and web-demo sessions; benchmark dataset downloads; workshop attendance; student curators trained; records cross-linked to MSA archived material; new/retained members reporting use `[TODO: baseline survey mechanism]`.

## Sustainability

Year 2 transitions governance to an MSA body `[TODO: identify committee or Focused Interest Group]` with a lightweight editor-plus-reviewers model. The precedent literature is specific about what makes society-branded resources survive — governance by a trusted organization, integration with existing community activities (here: M&M, Microscopy Today), contributor recognition, and maintenance capacity — and about the failure mode to avoid: volunteer-only efforts detached from established infrastructure [16,18]. Post-award hosting costs are minimal (static site + repository); curation continues through the student pipeline and member contributions credited on DOI'd releases.

## Team, partners, and reviewers

`[TODO: PI and co-applicants; partner labs and agencies (Area 5) — candidates from the byu-vcl shortlist; note the call excludes microscopy vendors as partners]`

## References

1. Tong, V. & Mingard, K. *Measurement uncertainties of energy dispersive X-ray spectroscopy in the scanning electron microscope (SEM-EDX/EDS)*. National Physical Laboratory report MAT 135 (2026). https://doi.org/10.47120/npl.mat135
2. Wright, S. I. et al. Introduction and comparison of new EBSD post-processing methodologies. *Ultramicroscopy* 159, 81–94 (2015). https://doi.org/10.1016/j.ultramic.2015.08.001
3. Kaufmann, K. & Vecchio, K. S. An acquisition parameter study for machine-learning-enabled electron backscatter diffraction. *Microscopy and Microanalysis* 27, 776–793 (2021). https://doi.org/10.1017/s1431927621000556
4. Singh, S. et al. High resolution low kV EBSD of heavily deformed and nanocrystalline aluminium by dictionary-based indexing. *Scientific Reports* 8 (2018). https://doi.org/10.1038/s41598-018-29315-8
5. Seidel, P. et al. Comparison of elemental analysis techniques for the characterization of commercial alloys. *Metals* 11, 736 (2021). https://doi.org/10.3390/met11050736
6. Bichlmeier, S. et al. Component selection for a compact micro-XRF spectrometer. *X-Ray Spectrometry* 30, 8–14 (2001). https://doi.org/10.1002/xrs.457
7. Flude, S., Haschke, M. & Storey, M. Application of benchtop micro-XRF to geological materials. *Mineralogical Magazine* 81, 923–948 (2017). https://doi.org/10.1180/minmag.2016.080.150
8. Kalinin, S. V. et al. Automated and autonomous experiments in electron and scanning probe microscopy. *ACS Nano* 15, 12604–12627 (2021). https://doi.org/10.1021/acsnano.1c02104
9. Taillon, J. A. et al. MaRDA FAIR materials microscopy and LIMS data working groups' community recommendations. *MRS Bulletin* 50, 793–804 (2025). https://doi.org/10.1557/s43577-025-00882-2
10. Ghiringhelli, L. M. et al. Shared metadata for data-centric materials science. *Scientific Data* 10 (2023). https://doi.org/10.34734/fzj-2023-03524
11. Pratiush, U. et al. Mic-hackathon 2024: hackathon on machine learning for electron and scanning probe microscopy. *Machine Learning: Science and Technology* 6, 040701 (2025). https://doi.org/10.1088/2632-2153/ae1f5d
12. Kühbach, M. et al. Community-driven methods for open and reproducible software tools for analyzing datasets from atom probe microscopy. *Microscopy and Microanalysis* 28 (2022). https://doi.org/10.1017/s1431927621012241
13. Wei, J. et al. Infrastructure for analysis of large microscopy and microanalysis data sets. *Microscopy and Microanalysis* 28 (2022). https://doi.org/10.1017/s1431927622011539
14. Gammon, S. T. et al. An online repository for pre-clinical imaging protocols (PIPs). *Tomography* 9, 750–758 (2023). https://doi.org/10.3390/tomography9020060
15. Rainford, P. F. et al. Knowledge preservation in the era of big science and AI: strategies for sustainable scientific research. *Nature Communications* (2026). https://doi.org/10.1038/s41467-026-72667-3
16. Katz, D. S. et al. Community organizations: changing the culture in which research software is developed and sustained. *Computing in Science & Engineering* 21, 8–24 (2018). https://doi.org/10.48550/arxiv.1811.08473
17. Toelch, U. & Ostwald, D. Digital open science — teaching digital tools for reproducible and transparent research. *PLOS Biology* 16 (2018). https://doi.org/10.1371/journal.pbio.2006022
18. Schweik, C. M. Free/open-source software as a framework for establishing commons in science. In *Understanding Knowledge as a Commons* (MIT Press, 2007). https://doi.org/10.7551/mitpress/6980.003.0014

## Appendix: supporting research artifacts

Full Edison reports backing this draft, in [`outputs/msa_2027_strategic_initiatives/`](outputs/msa_2027_strategic_initiatives/):

- [`need_evidence_answer.md`](outputs/msa_2027_strategic_initiatives/need_evidence_answer.md) — quantitative evidence report with a proposal-ready needs statement; includes the evidence table ([`need_evidence_artifact-00.md`](outputs/msa_2027_strategic_initiatives/need_evidence_artifact-00.md))
- [`deep_landscape_answer.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_answer.md) — landscape review with ten distilled gap statements ([`deep_landscape_artifact-00.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_artifact-00.md)) and a tool-by-tool gap table ([`deep_landscape_artifact-01.md`](outputs/msa_2027_strategic_initiatives/deep_landscape_artifact-01.md))
