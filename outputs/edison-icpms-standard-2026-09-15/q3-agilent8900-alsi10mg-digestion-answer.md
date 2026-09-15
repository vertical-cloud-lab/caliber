# q3-agilent8900-alsi10mg-digestion

## Query

Best practices for quantifying Si (~9-11 wt%), Mg (~0.2-0.5 wt%), Fe, Cu, Zn, Mn, Ti, and trace elements in an AlSi10Mg aluminum alloy by ICP-MS on an Agilent 8900 triple-quadrupole instrument: (1) acid digestion protocols for aluminum-silicon alloys - is HF required for complete Si dissolution, what is the risk of Si loss as volatile SiF4 or of silicic acid precipitation, and are alternatives like NaOH fusion used; (2) differences in digestion completeness, speed, or contamination between fine gas-atomized powder and solid pieces cut from a consolidated part; (3) spectral interference management for 24Mg, 27Al, 28Si (e.g., 12C12C+, 14N14N+) using He KED or H2/O2 reaction gas in MS/MS mode, and required dilution factors for percent-level analytes; (4) whether ICP-OES is preferable to ICP-MS for the major elements Al and Si, with ICP-MS reserved for minor and trace elements; (5) achievable accuracy and precision for major and minor elements in metal alloy digests.

## Answer

# Best-practice strategy for AlSi10Mg

## Executive recommendation

Use **one validated total-dissolution stock digest**, but measure it through at least two dilution streams:

1. **ICP-OES:** Al, Si, and usually Mg, plus higher-level Fe/Cu/Mn/Zn/Ti.
2. **Agilent 8900 ICP-MS/MS:** minor and trace constituents, using substantially greater dilution, internal standards, and analyte-specific gas modes.

For defensible total Si at 9–11 wt%, do **not** rely on HCl/HNO₃ dissolution alone. Use closed-vessel HNO₃–HF digestion in fluoropolymer vessels, followed by controlled fluoride complexation with boric acid, or validate an alkaline dissolution/fusion independently. Acid-only aluminum-alloy studies show severe Si under-recovery at much lower Si contents: one CRM gave 0.144% versus 0.415% certified, and another 0.474% versus 0.64%, while Fe, Cu, Mn, Mg, Zn, and Ti generally agreed much better. The same interlaboratory work placed the practical upper Si level for its simple acid-only procedure near 0.03%, far below AlSi10Mg composition. (uemoto2018determinationofminor pages 2-3, uemoto2018determinationofminor pages 5-6, uemoto2018determinationofminor pages 3-5, uemoto2018determinationofminor pages 1-2)

| Task / analyte group | Recommended sample preparation | Recommended instrument / mode | Key interference or bias | Practical QC |
|---|---|---|---|---|
| Total dissolution, including Si (~9–11 wt%) | Digest a representative portion with HNO₃–HF in a closed fluoropolymer vessel. After cooling, add boric acid to complex residual fluoride. Optimize the acid charge and microwave program specifically for AlSi10Mg. (wang2025determinationofsilicon pages 1-2, wang2025determinationofsilicon pages 5-8, pansu2006analysisofextractable pages 14-18) | ICP-OES for routine total Si; use HF-resistant introduction or verify complete fluoride complexation before conventional quartz introduction. | HNO₃/HCl alone can leave elemental Si or Si-rich phases and cause severe low bias. Open HF digestion or evaporation risks volatile SiF₄ loss; drying can also insolubilize analytes. (uemoto2018determinationofminor pages 2-3, uemoto2018determinationofminor pages 5-6, lotter2008identificationandquantification pages 47-52) | Process an Al–Si alloy CRM with every batch; inspect for residue; analyze independent portions and verify Si recovery before reporting. |
| Optional alkaline dissolution or fusion | Use a validated NaOH dissolution or borate/metaborate fusion when HF is undesirable. Keep the solution alkaline until dissolution is complete, then acidify carefully and dilute promptly. | Prefer ICP-OES; high flux concentrations generally make fusion solutions unattractive for trace ICP-MS. | Acidification can precipitate hydrated silica. Flux adds dissolved solids and Na, Li, or B contamination, can attack crucibles, and requires greater dilution. (pansu2006analysisofextractable pages 11-14, lotter2008identificationandquantification pages 47-52, wang2025determinationofsilicon pages 1-2) | Run flux and crucible blanks plus a fused CRM; monitor solution clarity; matrix-match standards or use standard additions. |
| Al, Si, and Mg at alloy levels | Use the complete digest and a dedicated moderate-to-large dilution into a matched acid and boric-acid matrix. | ICP-OES preferred; use suitable wavelengths and viewing geometry to prevent saturation or self-absorption. | Percent-level analytes are poorly suited to a trace ICP-MS method. Incomplete Si dissolution, matrix effects, and dilution error usually dominate. | Use bracketing checks, duplicate dilutions, an alloy CRM, and two Si lines where feasible. |
| Minor Fe, Cu, Zn, Mn, Ti, and trace elements | Prepare a separate, substantially greater dilution of the complete digest; keep total dissolved solids low and matrix composition consistent. | Agilent 8900 ICP-MS/MS: use He KED for multielement screening and analyte-specific MS/MS reaction modes where validation demonstrates a benefit. | Residual Al and Si cause space-charge suppression, deposits, and polyatomic ions; excessive dilution can compromise trace detection. (pansu2006analysisofextractable pages 45-49, balaram2023advancesinanalytical pages 13-15, uemoto2018determinationofminor pages 2-3) | Use internal standards, preparation blanks, continuing calibration checks, spikes, dilution checks, and alternate isotopes or modes for Fe and Ti. |
| ²⁸Si by ICP-MS/MS, if required | Use a high-dilution aliquot, minimize carbon contamination, and matrix-match the calibration solutions. | H₂ on-mass MS/MS, Q1→Q2 = 28→28. A documented Agilent 8900 starting condition is 5.0 mL/min H₂, but it must be retuned and validated locally. (takahashiUnknownyearsiliconwaferanalysis pages 44-46, shimamura2022multielementnanoparticleanalysis pages 44-46) | ¹⁴N₂⁺, ¹²C¹⁶O⁺, and carbon hydrides overlap ²⁸Si. H₂ removes N₂⁺ and CO⁺ through reaction while Si⁺ remains on-mass. He KED is less selective; O₂ 28→44 produced poorer BEC and detection limits in one 8900 study. (yamanaka2018determinationoftrace pages 41-44, golik2013usinghighresolution pages 2-3) | Challenge the method with C- and N-containing matrices; monitor BEC and blanks; compare results with ICP-OES or another Si isotope. |
| ²⁴Mg and ²⁷Al by ICP-MS/MS, if required | Use a dedicated very-high dilution to keep count rates within the calibrated detector range and minimize matrix loading. | Evaluate no-gas and He KED modes experimentally; retain ICP-OES as the primary assay for alloy-level Al and Mg. | Possible low-mass polyatomics affect m/z 24 and 27, but detector saturation, matrix suppression, and dilution error are often more important. | Verify serial-dilution agreement, alternate Mg isotopes, and operation within the validated pulse/analog range. |
| Separate dilution tiers | From one complete stock digest, prepare an OES aliquot for major elements, a high-dilution ICP-MS/MS aliquot for minor and trace elements, and an even higher dilution if measuring Al or Mg by ICP-MS. | Use ICP-OES and ICP-MS/MS as complementary methods rather than forcing one compromise dilution. | One dilution either overloads ICP-MS with Al and Si or unnecessarily weakens trace-element signals. | Prepare large dilution factors gravimetrically or by calibrated serial dilution; compare independent dilution chains after back-calculation. |
| Fine gas-atomized powder | Homogenize without grinding where possible; weigh by difference under low-static conditions and add acid slowly before sealing the vessel. | Same final methods as above. | High surface area causes faster, potentially vigorous digestion. Oxide-rich fines, particle-size segregation, static loss, and airborne contamination can bias results. | Analyze multiple representative portions; document particle-size sampling; include handling blanks. |
| Solid pieces from a consolidated part | Remove surface oxide, coating, coolant, and oil; cut representative interior coupons with clean tools, degrease, rinse, and dry. | Same final methods as above. | Digestion is slower, and Si-rich residue may persist. Saws, abrasives, and cutting fluids can introduce Fe, Cu, Zn, Mn, or Ti. | Use sacrificial cuts or tool blanks; avoid target-element-bearing abrasives; digest coupons from several part locations to assess heterogeneity. |


*Table: Compact workflow for complete dissolution, technique selection, interference control, dilution, and quality assurance when analyzing AlSi10Mg by ICP-OES and Agilent 8900 ICP-MS/MS.*

## 1. Digestion and quantitative Si recovery

### Preferred total-dissolution approach

A suitable development starting point is:

- Weigh approximately **0.10–0.20 g** of representative alloy into a cleaned PFA/PTFE closed vessel.
- Add HNO₃ cautiously first, especially for powder, then a controlled amount of HF sufficient for the approximately 10–20 mg Si present per 0.10–0.20 g sample.
- Allow the initial reaction to moderate before sealing. Apply a validated closed-vessel microwave or heated-vessel program.
- Cool fully before opening. Inspect the vessel and solution for metallic or dark Si-rich residue.
- Add a validated excess of high-purity boric acid to bind residual fluoride; reheat mildly if required by the validated procedure, cool, and dilute gravimetrically.

This is a **method-development template**, not a transferable certified acid recipe for AlSi10Mg. Acid quantity, vessel headspace, pressure limits, and boric-acid dose must be established through stoichiometry, vessel-manufacturer guidance, spike recovery, and an Al–Si CRM.

The supporting closed-digestion study used 0.2000 g sample, 5 mL HNO₃, 2 mL HF, 30 minutes of sealed heating, followed by 10 mL of 50 g/L boric acid. It achieved complete silica dissolution, certified-material relative errors no greater than 3.61%, and RSDs generally 0.21–1.60%; real-sample RSDs were no greater than 3.04%. Because this was fluorite rather than AlSi10Mg, its reagent proportions should demonstrate the chemical principle, not be copied without alloy validation. (wang2025determinationofsilicon pages 1-2, wang2025determinationofsilicon pages 8-10)

### Is HF required?

For **quantitative total Si by acid digestion**, effectively yes. HCl/HNO₃ readily dissolves the Al matrix and many metallic constituents, but elemental Si, Si-rich eutectic phases, oxide films, and silica-bearing residue are not reliably brought into solution. HF converts oxidized silicon to soluble fluorosilicate species; an HF/HNO₃ alloy digestion has been described as forming H₂SiF₆, with the dissolution rate controlled by HF availability. (brown1999rapidaluminumalloy pages 46-50, li2014boronandphosphorus pages 86-91)

HF is not necessary if an independently validated **alkaline dissolution or fusion** is used. Alkali addition converts Si compounds to soluble silicate, and aluminum-alloy interlaboratory procedures explicitly identify alkali dissolution for Si. (uemoto2018determinationofminor pages 3-5, uemoto2018determinationofminor pages 5-6)

### SiF₄ loss and silicic-acid precipitation

The main rules are:

- **Keep HF digestion closed.** Silicon-fluoride species, particularly SiF₄, may volatilize in open vessels. Closed vessels retain volatile products, reduce contamination and reagent evaporation, and permit higher temperature and pressure. (wang2025determinationofsilicon pages 1-2, pansu2006analysisofextractable pages 14-18, lotter2008identificationandquantification pages 47-52)
- **Do not evaporate an HF digest to dryness when Si is an analyte.** Dry evaporation can remove silicon as volatile fluoride or produce insoluble material; such workflows are explicitly unsuitable for silica quantification. (pansu2006analysisofextractable pages 14-18)
- **Do not remove the lid while the digest is hot or actively reacting.** Cool completely before opening and transfer quantitatively.
- **Complex residual fluoride rather than evaporating it.** Boric acid forms fluoroborate species, protects quartz components, and reduces residual-fluoride effects. Calibration solutions must contain the same boric-acid/acid matrix because boric acid itself can influence Si response. (wang2025determinationofsilicon pages 8-10, wang2025determinationofsilicon pages 5-8)
- **Avoid uncontrolled acidification of silicate solutions.** Acidifying alkaline silicate can polymerize hydrated silica/silicic acid and form an inconspicuous gel or precipitate. Fusion literature documents silica separation upon acid dissolution for some sodium fluxes, whereas lithium metaborate is less prone to this behavior. (lotter2008identificationandquantification pages 47-52, wang2025determinationofsilicon pages 1-2)

### Alkaline alternatives

NaOH dissolution or alkali/borate fusion can retain Si and achieve near-total decomposition without volatile Si loss. However, fusion commonly needs a large flux-to-sample ratio and introduces Na, Li, or B, high total dissolved solids, crucible-derived contaminants, and greater dilution. These factors make it more appropriate for **ICP-OES Si assay** than for broad ultra-trace ICP-MS. Strong fusion heating can also lose volatile trace elements. (pansu2006analysisofextractable pages 11-14, lotter2008identificationandquantification pages 47-52, pansu2006analysisofextractable pages 18-21)

If fusion is selected, use a separate aliquot for Si and perhaps Al rather than assuming it is optimal for trace elements. Run a flux blank, crucible blank, fused alloy CRM, and acidification/recovery study. Avoid a Li flux if Li is reportable and a borate flux if B is reportable.

## 2. Powder versus consolidated solid

No directly comparable study was found that digested composition-matched gas-atomized AlSi10Mg powder and consolidated coupons under identical conditions. The following differences are therefore physically grounded method recommendations rather than head-to-head performance claims.

**Gas-atomized powder** reacts faster and potentially much more vigorously because of its high area. Add oxidizing acid slowly, allow cold predigestion, use small initial masses, and never seal during uncontrolled gas evolution. Powder can suffer particle-size segregation, oxide-rich fines, static loss, airborne contamination, and nonrepresentative scooping. Homogenize gently, sample across the container, weigh by difference, and analyze at least three independent portions.

**Solid pieces** usually digest more slowly; persistent Si-rich residue is easier to overlook. Sample several interior locations because additive-manufactured or consolidated material can be spatially heterogeneous. Use clean cutting tools, remove coolant/oil, degrease, rinse, and dry. Saw blades, abrasive papers, wire EDM, and cutting fluids can add Fe, Cu, Zn, Mn, Ti, Ni, or Cr. Do not grind with media containing reportable elements. A documented rapid HCl procedure dissolved small aluminum pins within about an hour at room temperature, but HCl alone was inadequate for quantitative Si and potentially Cu; faster disappearance of the Al substrate is therefore not proof of complete digestion. (brown1999rapidaluminumalloy pages 55-59, brown1999rapidaluminumalloy pages 46-50)

## 3. Agilent 8900 interference management and dilution

### ²⁸Si

Major nominal-mass interferences include **¹⁴N₂⁺, ¹²C¹⁶O⁺, and carbon hydride ions**. These are unresolved by ordinary unit-resolution quadrupole ICP-MS. (golik2013usinghighresolution pages 2-3, golik2013usinghighresolution pages 1-2)

The best-supported Agilent 8900 mode is **H₂ on-mass MS/MS**:

- Q1 = 28
- cell gas = H₂
- Q2 = 28
- documented starting flow = **5.0 mL/min H₂**

N₂⁺ and CO⁺ react to form hydrogenated products, while Si⁺ remains at m/z 28. Q1 prevents unrelated precursor masses from entering the cell and generating new product-ion overlaps. Local tuning and matrix challenges remain mandatory. (takahashiUnknownyearsiliconwaferanalysis pages 44-46, shimamura2022multielementnanoparticleanalysis pages 44-46)

**He KED** is useful as a robust multielement screening mode, but it discriminates by collisional energy rather than selective chemistry and may not suppress the intense m/z-28 background sufficiently. **O₂ mass shift**, ²⁸Si⁺ → ²⁸Si¹⁶O⁺ and measurement at 28→44, is chemically possible, but one 8900 comparison found H₂ MS/MS much better: H₂ 28→28 gave BEC 2.17 µg/L and DL 0.03 µg/L, whereas O₂ 28→44 gave BEC 85.54 µg/L and DL 28.21 µg/L. O₂ should therefore be treated as an alternative to validate, not the default. (yamanaka2018determinationoftrace pages 41-44)

For a 10 wt% Si alloy, ICP-MS/MS adds little value for the bulk assay: digestion and dilution uncertainty dominate, while ICP-OES is simpler.

### ²⁴Mg and ²⁷Al

For these isotopes, first test no-gas and He-KED methods with single-element standards, acid/boric-acid blanks, and matrix-matched solutions. Potential low-mass overlaps exist, but at alloy concentrations the dominant problems are usually detector saturation, abundance sensitivity, space-charge suppression, deposition, and dilution error—not detection capability. Check ²⁴Mg against ²⁵Mg or ²⁶Mg after correcting applicable overlaps. Because Al is monoisotopic, verify ²⁷Al through serial dilution, spike recovery, and preferably ICP-OES rather than isotope agreement.

### Practical dilution tiers

Suppose **0.1000 g** alloy is diluted to **100.0 mL**. The stock digest contains approximately:

- Al: 800–900 mg/L
- Si: 90–110 mg/L
- Mg: 2–5 mg/L

A further 100-fold dilution gives approximately 8–9 mg/L Al, 0.9–1.1 mg/L Si, and 20–50 µg/L Mg. This may be reasonable for OES and selected ICP-MS work but can still overload a sensitive ICP-MS method for Al and Si. A 1,000-fold post-digest dilution gives approximately 0.8–0.9 mg/L Al and 90–110 µg/L Si; even larger dilution may be needed for ²⁷Al depending on detector mode and tuning.

Thus, do not prescribe one universal factor. Establish dilution from the highest calibrated concentration, detector count-rate limits, and a serial-dilution test. Keep the final dissolved-solid matrix conservatively low—commonly at or below approximately 0.1–0.2% for routine trace ICP-MS unless the installed introduction system has been validated for more. Prepare large factors gravimetrically or through two calibrated serial steps. Analyze at least two dilutions; agreement after back-calculation is a key matrix-effect check.

For trace constituents, balance lower matrix against detection capability. ICP-MS benefits from ng/L sensitivity but remains susceptible to spectral and matrix effects, so internal standards, matrix matching, standard additions, aerosol dilution, or reaction-cell chemistry may be required. (smanova2026ecologicalsignificancesources pages 12-13, balaram2023advancesinanalytical pages 13-15)

## 4. ICP-OES versus ICP-MS

**ICP-OES is preferable for Al and Si**, and generally for Mg at 0.2–0.5 wt%. It tolerates higher analyte concentrations, offers suitable emission lines and viewing geometries, and avoids forcing enormous dilutions merely to keep the mass spectrometer within range. ICP-OES has demonstrated practical multielement determination in aluminum alloys using matrix-matched calibration and CRM validation. (uemoto2018determinationofminor pages 2-3, uemoto2018determinationofminor pages 1-2)

Use the 8900 for Fe, Cu, Zn, Mn, Ti, and other elements when their concentrations require ICP-MS sensitivity. Some of these may still be high enough for OES, so the best division is concentration-dependent:

- **Major:** Al, Si → ICP-OES.
- **Upper minor:** Mg and often Fe/Cu/Mn/Zn/Ti → ICP-OES, with ICP-MS as confirmation if useful.
- **Low minor/trace:** ICP-MS/MS.

ICP-OES random error in classical major-element work is reported around 2%, improving to approximately 0.5% in favorable major-element methods with effective internal-standard correction. Its sensitivity is lower than ICP-MS, while both techniques remain vulnerable to high dissolved solids and matrix mismatch. (pansu2006analysisofextractable pages 45-49)

## 5. Realistic accuracy and precision

With complete digestion, CRM-based calibration verification, and controlled dilution, reasonable laboratory targets are:

- **Al and Si:** repeatability about 0.5–2% RSD; full-method relative error about 1–3%.
- **Mg and other established minor alloying elements:** about 1–3% RSD and 1–5% relative error.
- **Low trace elements:** commonly 2–5% RSD; near the LOQ, 5–10% or greater may be realistic.

These are validation targets rather than instrument specifications. In an ICP-OES validation, Mg repeatability was approximately 0.72–1%, while Fe, Cu, Mn, Mg, and Zn reported CVs ranged from 1% to 8%, depending on element and level. Expanded relative uncertainty contributions for these elements were several percent. (alegria2025validationanduncertainty pages 15-18, alegria2025validationanduncertainty pages 6-9)

The aluminum-alloy interlaboratory study illustrates the distinction between instrumental precision and preparation bias. For one CRM, Fe, Cu, Mn, Mg, Zn, and Ti measurements were close to certified values, whereas acid-only Si was 0.144% against 0.415% certified. Thus, an apparently precise Si result can still be grossly wrong if dissolution is incomplete. (uemoto2018determinationofminor pages 5-6)

Minimum validation should include an Al–Si alloy CRM near 10% Si, full procedural blanks, triplicate independent digestions, duplicate dilution chains, continuing calibration verification, internal-standard recovery, matrix spikes, and a residue check. Establish uncertainty from weighing, final volume or gravimetric dilution, calibration, repeatability, between-digestion variability, CRM bias, and sample heterogeneity. Acceptance should be based on CRM recovery and dilution agreement rather than solution clarity alone.

## References

1. (uemoto2018determinationofminor pages 2-3): Michihisa Uemoto, Masanori Makino, Yuji Ota, Hiromi Sakaguchi, Yukari Shimizu, and Kazuhiro Sato. Determination of minor and trace metals in aluminum and aluminum alloys by icp-aes; evaluation of the uncertainty and limit of quantitation from interlaboratory testing. Jun 2018. URL: https://doi.org/10.2116/analsci.18sbp14, doi:10.2116/analsci.18sbp14. This article has 16 citations and is from a peer-reviewed journal.

2. (uemoto2018determinationofminor pages 5-6): Michihisa Uemoto, Masanori Makino, Yuji Ota, Hiromi Sakaguchi, Yukari Shimizu, and Kazuhiro Sato. Determination of minor and trace metals in aluminum and aluminum alloys by icp-aes; evaluation of the uncertainty and limit of quantitation from interlaboratory testing. Jun 2018. URL: https://doi.org/10.2116/analsci.18sbp14, doi:10.2116/analsci.18sbp14. This article has 16 citations and is from a peer-reviewed journal.

3. (uemoto2018determinationofminor pages 3-5): Michihisa Uemoto, Masanori Makino, Yuji Ota, Hiromi Sakaguchi, Yukari Shimizu, and Kazuhiro Sato. Determination of minor and trace metals in aluminum and aluminum alloys by icp-aes; evaluation of the uncertainty and limit of quantitation from interlaboratory testing. Jun 2018. URL: https://doi.org/10.2116/analsci.18sbp14, doi:10.2116/analsci.18sbp14. This article has 16 citations and is from a peer-reviewed journal.

4. (uemoto2018determinationofminor pages 1-2): Michihisa Uemoto, Masanori Makino, Yuji Ota, Hiromi Sakaguchi, Yukari Shimizu, and Kazuhiro Sato. Determination of minor and trace metals in aluminum and aluminum alloys by icp-aes; evaluation of the uncertainty and limit of quantitation from interlaboratory testing. Jun 2018. URL: https://doi.org/10.2116/analsci.18sbp14, doi:10.2116/analsci.18sbp14. This article has 16 citations and is from a peer-reviewed journal.

5. (wang2025determinationofsilicon pages 1-2): Xiao Wang, Liming Gan, Jiu-Fen Liu, Xin Wei, Xi Wang, Tao He, and Na Guo. Determination of silicon dioxide in fluorite by icp oes with closed digestion and boric acid complex reaction. PLOS One, 20(12):e0338898, Dec 2025. URL: https://doi.org/10.1371/journal.pone.0338898, doi:10.1371/journal.pone.0338898. This article has 0 citations and is from a peer-reviewed journal.

6. (wang2025determinationofsilicon pages 5-8): Xiao Wang, Liming Gan, Jiu-Fen Liu, Xin Wei, Xi Wang, Tao He, and Na Guo. Determination of silicon dioxide in fluorite by icp oes with closed digestion and boric acid complex reaction. PLOS One, 20(12):e0338898, Dec 2025. URL: https://doi.org/10.1371/journal.pone.0338898, doi:10.1371/journal.pone.0338898. This article has 0 citations and is from a peer-reviewed journal.

7. (pansu2006analysisofextractable pages 14-18): M Pansu and J Gautheyrou. Analysis of Extractable and Total Elements, pages 895-974. Springer Berlin Heidelberg, Jan 2006. URL: https://doi.org/10.1007/978-3-540-31211-6\_31, doi:10.1007/978-3-540-31211-6\_31. This article has 3022 citations.

8. (lotter2008identificationandquantification pages 47-52): SJ Lötter. Identification and quantification of impurities in zircon, pdz and other relevant zirconium products. Unknown journal, 2008.

9. (pansu2006analysisofextractable pages 11-14): M Pansu and J Gautheyrou. Analysis of Extractable and Total Elements, pages 895-974. Springer Berlin Heidelberg, Jan 2006. URL: https://doi.org/10.1007/978-3-540-31211-6\_31, doi:10.1007/978-3-540-31211-6\_31. This article has 3022 citations.

10. (pansu2006analysisofextractable pages 45-49): M Pansu and J Gautheyrou. Analysis of Extractable and Total Elements, pages 895-974. Springer Berlin Heidelberg, Jan 2006. URL: https://doi.org/10.1007/978-3-540-31211-6\_31, doi:10.1007/978-3-540-31211-6\_31. This article has 3022 citations.

11. (balaram2023advancesinanalytical pages 13-15): V. Balaram. Advances in analytical techniques and applications in exploration, mining, extraction, and metallurgical studies of rare earth elements. Minerals, Jul 2023. URL: https://doi.org/10.3390/min13081031, doi:10.3390/min13081031. This article has 70 citations.

12. (takahashiUnknownyearsiliconwaferanalysis pages 44-46): J Takahashi. Silicon wafer analysis by icp-qqq: determination of phosphorus and titanium in a high silicon matrix. Unknown journal, Unknown year.

13. (shimamura2022multielementnanoparticleanalysis pages 44-46): Y Shimamura and D Hsu. Multielement nanoparticle analysis of semiconductor process chemicals using spicp-qqq. Unknown journal, 2022.

14. (yamanaka2018determinationoftrace pages 41-44): M Yamanaka and K Yamanaka. Determination of trace elements in ultrapure semiconductor grade sulfuric acid using the agilent 8900 icp-qqq in ms/ms mode. Unknown journal, 2018.

15. (golik2013usinghighresolution pages 2-3): V. M. Golik, N. V. Kuz’mina, A. V. Saprygin, and S. A. Trepachev. Using high resolution and dynamic reaction cell for the improvement of the sensitivity of direct silicon determination in uranium materials by inductively coupled plasma mass spectrometry. Journal of Analytical Chemistry, 68:1142-1150, Dec 2013. URL: https://doi.org/10.1134/s1061934813130066, doi:10.1134/s1061934813130066. This article has 5 citations.

16. (wang2025determinationofsilicon pages 8-10): Xiao Wang, Liming Gan, Jiu-Fen Liu, Xin Wei, Xi Wang, Tao He, and Na Guo. Determination of silicon dioxide in fluorite by icp oes with closed digestion and boric acid complex reaction. PLOS One, 20(12):e0338898, Dec 2025. URL: https://doi.org/10.1371/journal.pone.0338898, doi:10.1371/journal.pone.0338898. This article has 0 citations and is from a peer-reviewed journal.

17. (brown1999rapidaluminumalloy pages 46-50): EA Brown. Rapid aluminum alloy analysis utilizing inductively coupled plasma atomic emission spectrometry. Unknown journal, 1999.

18. (li2014boronandphosphorus pages 86-91): MX Li. Boron and phosphorus removal from si-cu alloy using cao-sio 2-na2o-al2o3 slag. Unknown journal, 2014.

19. (pansu2006analysisofextractable pages 18-21): M Pansu and J Gautheyrou. Analysis of Extractable and Total Elements, pages 895-974. Springer Berlin Heidelberg, Jan 2006. URL: https://doi.org/10.1007/978-3-540-31211-6\_31, doi:10.1007/978-3-540-31211-6\_31. This article has 3022 citations.

20. (brown1999rapidaluminumalloy pages 55-59): EA Brown. Rapid aluminum alloy analysis utilizing inductively coupled plasma atomic emission spectrometry. Unknown journal, 1999.

21. (golik2013usinghighresolution pages 1-2): V. M. Golik, N. V. Kuz’mina, A. V. Saprygin, and S. A. Trepachev. Using high resolution and dynamic reaction cell for the improvement of the sensitivity of direct silicon determination in uranium materials by inductively coupled plasma mass spectrometry. Journal of Analytical Chemistry, 68:1142-1150, Dec 2013. URL: https://doi.org/10.1134/s1061934813130066, doi:10.1134/s1061934813130066. This article has 5 citations.

22. (smanova2026ecologicalsignificancesources pages 12-13): Z Smanova, D Azimova, and J Todjiev. Ecological significance, sources, and analytical determination methods of chromium and zinc in environmental objects: a critical review. Unknown journal, 2026.

23. (alegria2025validationanduncertainty pages 15-18): Rodrigo Martínez-Peñuñuri, Alejandro Monserrat GarcÍa Alegria, Paulina Vázquez-Bustamante, Marcela Montoya-Blumenkron, Dayana Itzajara Estrada-Gonzalez, Ana María Avilés Figueroa, Trinidad Quizan-Plata, and Karla Denisse Murillo-Castillo. Validation and uncertainty estimation for multielement determination using icp-oes according to the astm e2941-14 standard. Jun 2025. URL: https://doi.org/10.25135/jcm.112.2502.3435, doi:10.25135/jcm.112.2502.3435. This article has 4 citations.

24. (alegria2025validationanduncertainty pages 6-9): Rodrigo Martínez-Peñuñuri, Alejandro Monserrat GarcÍa Alegria, Paulina Vázquez-Bustamante, Marcela Montoya-Blumenkron, Dayana Itzajara Estrada-Gonzalez, Ana María Avilés Figueroa, Trinidad Quizan-Plata, and Karla Denisse Murillo-Castillo. Validation and uncertainty estimation for multielement determination using icp-oes according to the astm e2941-14 standard. Jun 2025. URL: https://doi.org/10.25135/jcm.112.2502.3435, doi:10.25135/jcm.112.2502.3435. This article has 4 citations.
