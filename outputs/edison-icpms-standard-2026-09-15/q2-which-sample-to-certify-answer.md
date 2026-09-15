# q2-which-sample-to-certify

## Query

A laboratory is creating a matrix-matched SEM-EDS quantification standard from AlSi10Mg: a laser powder bed fusion (3D printed) specimen will be mounted, polished, and used as the standard, and its bulk composition will be certified by ICP-MS. Should the ICP-MS analysis be performed on (a) the virgin gas-atomized AlSi10Mg feedstock powder, or (b) material sectioned from the printed specimen itself? Discuss: the metrological principle that a reference material's certified composition must correspond to the exact material that will be analyzed; bulk homogeneity of LPBF builds (e.g., composition gradients along build height due to Mg evaporation) versus particle-to-particle composition variation in gas-atomized powder; representative sampling and recommended sample mass and replicates for solid alloy versus powder digestion; and contamination risks when sectioning solid samples (e.g., Fe pickup from cutting or grinding tools).

## Answer

# Recommendation

Perform the certification analysis on **(b) material sectioned from the LPBF-printed specimen itself**. The virgin powder may also be analyzed as a useful process-control comparator, but its composition should not be assigned as the certified bulk composition of the mounted print.

The decisive issue is not whether powder and print nominally satisfy the same AlSi10Mg specification. It is whether the assigned value describes the **actual material population represented by the mounted, polished SEM-EDS standard**. Reference-material values are measurand-, matrix-, procedure-, and sample-intake-specific; homogeneity must be demonstrated at the minimum relevant intake, and values should not be transferred merely because another material appears similar. Commutability likewise depends on interactions between the matrix and the measurement procedure. (beauchamp2021metrologicaltoolsfor pages 21-23, beauchamp2021metrologicaltoolsfor pages 50-52, beauchamp2021metrologicaltoolsfor pages 10-12, beauchamp2021metrologicaltoolsfor pages 19-21, beauchamp2021metrologicaltoolsfor pages 40-42)

| Issue | Virgin AlSi10Mg powder | Actual LPBF printed specimen | Metrological implication / recommended action |
|---|---|---|---|
| Matrix identity | Represents the feedstock before melting, vaporization, oxidation, spatter formation, and solidification; it is not the mounted SEM-EDS standard. | Same processed material, metallurgical matrix, and thermal history as the mounted and polished standard. | Certified values should characterize the actual material supplied and analyzed, with fitness for the intended procedure and homogeneity at the relevant intake; values should not be transferred merely because another material appears similar. Certify the print. (beauchamp2021metrologicaltoolsfor pages 21-23, beauchamp2021metrologicaltoolsfor pages 50-52, beauchamp2021metrologicaltoolsfor pages 10-12, beauchamp2021metrologicaltoolsfor pages 40-42) |
| LPBF Mg evaporation and build-height risk | Cannot reveal composition changes introduced during LPBF. | Captures the net composition after LPBF. Mg-sensitive oxidation and chemically modified spatter show that processing can alter chemistry; a build-height Mg gradient is plausible but must be measured rather than presumed. (pal2022linkingpowderproperties pages 4-7, luttergunther2018spatterformationduring pages 1-2) | Sample the printed build at several heights and lateral positions. If differences are insignificant relative to the target uncertainty, assign a build-wide value; otherwise certify separate strata or restrict the standard to the characterized region. |
| Powder particle-population heterogeneity | A single scoop may misrepresent particle-size fractions, satellites, oxide-bearing particles, or chemically modified particles. Powder evolution can include fine-particle loss and oxygen pickup; spatter can carry Mg-rich oxide patches. (pal2022linkingpowderproperties pages 4-7, luttergunther2018spatterformationduring pages 1-2, pal2022linkingpowderproperties pages 2-4) | Particle-to-particle variation is largely integrated during melting, although pores, inclusions, and microsegregation can remain. | If powder is analyzed as a process-control comparator, collect increments across the container or stream, combine and mix them, then use riffle or rotary splitting—not grab sampling. Powder certification does not substitute for print certification. |
| Solid spatial homogeneity | Does not establish homogeneity of the build or of the mounted face. | May vary among bottom, middle, and top regions or laterally; microscopic Si/Mg segregation is distinct from a bulk composition gradient. | Conduct a designed between-location homogeneity study. The ICP bulk value supports SEM-EDS calibration only if its uncertainty includes relevant spatial heterogeneity and the mounted region belongs to the certified population. (beauchamp2021metrologicaltoolsfor pages 21-23, sega2021referencematerialspreparation pages 4-6, beauchamp2021metrologicaltoolsfor pages 19-21) |
| Representative sampling, mass, and replicates | **Fit-for-purpose recommendation, not a universal standard:** create a **10–50 g composite laboratory sample**, mix and split it reproducibly, then prepare **≥3 independent 0.2–0.5 g digestions**. Retain particle-size proportions. | **Fit-for-purpose recommendation, not a universal standard:** take material from multiple mapped locations in each spatial stratum and prepare **≥3 independent 0.2–0.5 g digestions per stratum**; combine equal masses only when estimating a defined build-wide mean. | Independent digestions—not repeated readings from one solution—estimate sampling plus preparation variability. Published alloy examples use approximately 0.5–1 g and duplicate/triplicate runs, so final mass must be validated for complete dissolution, precision, and homogeneity rather than treated as universally prescribed. (beauchamp2021metrologicaltoolsfor pages 21-23, uemoto2011instrumentalchemicalanalysis pages 8-10, hubau2019recyclingorientedmethodologyto pages 2-3, hubau2019recyclingorientedmethodologyto pages 3-5, yken2021acomparisonof pages 18-19) |
| Sectioning contamination | Usually avoids sawing the consolidated specimen, although scoops, splitters, and containers can still contaminate powder. | Steel saws or abrasives can plausibly add Fe/Cr; carbide tools can add W/Co; grinding media, coolant, and handling can add other contaminants. Direct AlSi10Mg pickup must be evaluated experimentally. | Use documented low-contamination tooling; make a sacrificial cut; remove the cut-affected surface with clean, composition-compatible tooling; clean and rinse thoroughly; run reagent and preparation blanks; and compare differently prepared aliquots. Monitor Fe/Cr or W/Co as tool tracers. Non-contaminating preparation media are preferred. (yken2021acomparisonof pages 16-18, lotter2008identificationandquantification pages 61-67) |
| Final decision | Useful only as a separate feedstock certificate or as evidence of powder-to-part change. | Correct primary material for assigning the SEM-EDS standard’s bulk certified composition. | Choose **(b), material sectioned from the printed specimen itself**. Preserve a paired virgin-powder analysis as supplementary process information, but do not use it as the certified value for the printed SEM-EDS standard unless a statistically adequate equivalence and homogeneity study demonstrates transferability. |


*Table: Decision table showing why the actual LPBF specimen should provide the certified composition for a matrix-matched SEM-EDS standard. It also gives fit-for-purpose sampling, replication, spatial-homogeneity, and contamination-control recommendations.*

## Why certifying the powder is insufficient

LPBF changes the material from discrete, oxide-coated gas-atomized particles into a rapidly melted and solidified alloy. During this transformation, volatile-element loss, oxidation, spatter formation, inclusion incorporation, and microsegregation may occur. AlSi10Mg spatter has been reported to differ chemically from virgin feedstock and to contain Mg-rich oxide patches; powder reuse also changes particle populations and oxygen content. Consequently, feedstock composition does not prove printed-part composition. (pal2022linkingpowderproperties pages 4-7, luttergunther2018spatterformationduring pages 1-2)

Magnesium is particularly important because its nominal concentration is small—commonly about 0.25–0.45 wt.% in AlSi10Mg powder—and a modest absolute change can be a substantial relative change. The retrieved evidence did **not**, however, establish that every AlSi10Mg build has a monotonic Mg gradient with height. Such a gradient is a credible, process-dependent possibility arising from vaporization, changing thermal conditions, gas flow, and spatter/recycling behavior, but it must be measured in the particular build rather than assumed. (luttergunther2018spatterformationduring pages 1-2, pal2022linkingpowderproperties pages 2-4)

It is also essential to distinguish two scales of heterogeneity:

1. **Microscopic phase segregation**—for example, Si-rich regions or Mg associated with phases or oxides—affects individual SEM-EDS fields and is expected in a multiphase alloy.
2. **Bulk compositional heterogeneity**—different mean Mg, Si, Fe, or other concentrations at the bottom, middle, top, or across the build—determines whether one ICP value can be assigned to the complete standard.

A large digestion can average microscopic segregation while concealing a build-scale gradient. Therefore, one pooled specimen from an unspecified location is not an adequate homogeneity demonstration.

## Recommended solid-build sampling design

Before sacrificing material, map every ICP sample to the eventual mounted reference pieces. A practical design is:

1. Divide the build into at least **bottom, middle, and top height strata**. Include more strata for a tall build or if process monitoring indicates changing thermal or gas-flow conditions.
2. At each height, sample at least two lateral positions when geometry permits—for example, center and edge or gas-flow upstream and downstream.
3. Prepare **at least three independent digestions per stratum**. These must be independently weighed and digested portions, not three instrumental readings from one solution.
4. As a fit-for-purpose starting point, use approximately **0.2–0.5 g per digestion**, or the larger mass the digestion method can completely dissolve without excessive matrix loading. Published alloy procedures include 0.5–1 g portions and duplicate or triplicate runs; no universal 0.2–0.5 g requirement applies here. The selected minimum intake must be validated experimentally. (beauchamp2021metrologicaltoolsfor pages 21-23, uemoto2011instrumentalchemicalanalysis pages 8-10)
5. Analyze the strata separately first. Do not pool them before testing heterogeneity. If between-location differences are negligible relative to the target uncertainty, equal-mass portions may then be combined or statistically averaged to obtain a build-wide value. If a significant gradient exists, either certify separate height regions or restrict the standard’s certified use to the characterized region.
6. Include spatial heterogeneity, digestion repeatability, calibration, blank, recovery, and possible preparation contamination in the assigned uncertainty.

The mounted SEM-EDS coupon should preferably be adjacent to, or one member of the same mapped stratum as, the ICP portions. If only one small coupon will serve as the standard, the most defensible value is the value for that local characterized region—not necessarily the average of the entire build.

## Powder sampling, if analyzed as a comparator

Gas-atomized powder can be compositionally more uniform than a blended elemental powder because each droplet originates from an alloy melt, but it should not be assumed to be identical particle-to-particle. AlSi10Mg feedstock can span roughly 10–100 µm and contain satellites, oxide inclusions, and irregular particles. Reuse can preferentially remove fines, produce agglomerates, increase oxygen, and introduce chemically modified spatter. Thus, a single scoop may not preserve the lot’s particle-size and surface-chemistry distribution. (pal2022linkingpowderproperties pages 4-7, luttergunther2018spatterformationduring pages 1-2, pal2022linkingpowderproperties pages 2-4)

For a supplementary powder analysis:

- Take increments from multiple container depths or, preferably, from the moving powder stream during transfer.
- Combine and mix the increments into a **10–50 g laboratory composite**, then reduce it with a rotary or riffle splitter. This range is a practical recommendation, not a universal standard.
- Avoid cone-and-quarter procedures where segregation by particle size is likely.
- Prepare at least **three independent 0.2–0.5 g digestions** from separately split portions.
- Compare replicate and particle-size-fraction results. If variability exceeds the required uncertainty, increase the composite and digestion masses or analyze size fractions separately.

Studies of heterogeneous particulate materials show that small sub-gram portions can suffer representativeness problems and that larger, systematically divided parent samples and independent digestions reduce this risk. These studies are not AlSi10Mg-specific standards, but they support the sampling logic. (hubau2019recyclingorientedmethodologyto pages 2-3, hubau2019recyclingorientedmethodologyto pages 3-5, yken2021acomparisonof pages 8-12, yken2021acomparisonof pages 18-19)

## Sectioning and preparation contamination

Sampling the print introduces a different risk: tooling contamination. A steel saw, file, or abrasive can deposit **Fe and possibly Cr/Ni**; tungsten-carbide tooling can contribute **W and Co**; abrasive papers and grinding media can contribute Si, Al, or other constituents. This matters especially for trace Fe certification. Direct quantitative evidence for Fe pickup during AlSi10Mg sectioning was not identified in the retrieved literature, so the magnitude must be established by a preparation study rather than corrected by assumption. General analytical guidance favors non-contaminating preparation media and minimizing handling and transfer steps. (yken2021acomparisonof pages 16-18, lotter2008identificationandquantification pages 61-67)

Recommended controls are:

- Record blade, drill, grinding-medium, coolant, and container compositions.
- Use a low-contamination method such as EDM with a validated skim/removal step, or a dedicated clean abrasive saw; no cutting technique should be presumed contamination-free.
- Make the initial cut sacrificial and remove the mechanically or thermally affected surface before collecting analytical material.
- Prefer clean interior chips or coupons over visible saw swarf. Do not digest material containing embedded abrasive.
- Degrease and rinse samples using validated high-purity solvents/acids without selectively leaching an alloying element.
- Run reagent blanks, full preparation blanks where feasible, and a tool-contact control.
- Prepare matched aliquots by two different tools or preparation routes during validation. An Fe increase after steel-tool preparation, or W/Co after carbide preparation, is evidence of pickup.
- Verify complete dissolution and quantitatively inspect or analyze residues; incomplete dissolution can bias elemental totals. (yken2021acomparisonof pages 16-18, yken2021acomparisonof pages 18-19)

## Certification interpretation

ICP-MS determines the composition of the digested test portions; it does not by itself certify the entire print. A defensible in-house reference-material assignment therefore requires:

- a precisely defined measurand and material region;
- a validated digestion and ICP method with traceability and uncertainty;
- demonstrated within- and between-location homogeneity at the specified minimum sample mass;
- documented stability, storage, preparation, and use conditions; and
- instructions stating where SEM-EDS measurements may be made and how many fields should be averaged. (beauchamp2021metrologicaltoolsfor pages 21-23, sega2021referencematerialspreparation pages 4-6, beauchamp2021metrologicaltoolsfor pages 10-12)

Accordingly, the sound workflow is to **certify mapped material from the actual LPBF build**, retain the virgin-powder result as supplementary evidence of powder-to-part change, and assign either a build-wide or region-specific value only after the spatial-homogeneity study. Powder and print values could be treated as equivalent only if a statistically adequate, uncertainty-aware comparison demonstrated equivalence; nominal agreement with the alloy specification would not be sufficient.

## References

1. (beauchamp2021metrologicaltoolsfor pages 21-23): Metrological tools for the reference materials and reference instruments of the NIST Material Measurement Laboratory This article has 66 citations.

2. (beauchamp2021metrologicaltoolsfor pages 50-52): Metrological tools for the reference materials and reference instruments of the NIST Material Measurement Laboratory This article has 66 citations.

3. (beauchamp2021metrologicaltoolsfor pages 10-12): Metrological tools for the reference materials and reference instruments of the NIST Material Measurement Laboratory This article has 66 citations.

4. (beauchamp2021metrologicaltoolsfor pages 19-21): Metrological tools for the reference materials and reference instruments of the NIST Material Measurement Laboratory This article has 66 citations.

5. (beauchamp2021metrologicaltoolsfor pages 40-42): Metrological tools for the reference materials and reference instruments of the NIST Material Measurement Laboratory This article has 66 citations.

6. (pal2022linkingpowderproperties pages 4-7): Ritam Pal and Amrita Basak. Linking powder properties, printing parameters, post-processing methods, and fatigue properties in additive manufacturing of alsi10mg. Alloys, 1:149-179, Jul 2022. URL: https://doi.org/10.3390/alloys1020010, doi:10.3390/alloys1020010. This article has 41 citations.

7. (luttergunther2018spatterformationduring pages 1-2): Max Lutter-Günther, M. Bröker, T. Mayer, S. Lizak, C. Seidel, and G. Reinhart. Spatter formation during laser beam melting of alsi10mg and effects on powder quality. Procedia CIRP, 74:33-38, Jan 2018. URL: https://doi.org/10.1016/j.procir.2018.08.008, doi:10.1016/j.procir.2018.08.008. This article has 83 citations and is from a peer-reviewed journal.

8. (pal2022linkingpowderproperties pages 2-4): Ritam Pal and Amrita Basak. Linking powder properties, printing parameters, post-processing methods, and fatigue properties in additive manufacturing of alsi10mg. Alloys, 1:149-179, Jul 2022. URL: https://doi.org/10.3390/alloys1020010, doi:10.3390/alloys1020010. This article has 41 citations.

9. (sega2021referencematerialspreparation pages 4-6): M Sega. Reference materials: preparation, homogeneity, stability and value assignment. Unknown journal, 2021.

10. (uemoto2011instrumentalchemicalanalysis pages 8-10): Michihisa Uemoto. Instrumental chemical analysis of magnesium and magnesium alloys. ArXiv, Jan 2011. URL: https://doi.org/10.5772/13727, doi:10.5772/13727. This article has 6 citations.

11. (hubau2019recyclingorientedmethodologyto pages 2-3): Agathe Hubau, Alexandre Chagnes, Michel Minier, Solène Touzé, Simon Chapron, and Anne-Gwénaëlle Guezennec. Recycling-oriented methodology to sample and characterize the metal composition of waste printed circuit boards. Waste management, 91:62-71, May 2019. URL: https://doi.org/10.1016/j.wasman.2019.04.041, doi:10.1016/j.wasman.2019.04.041. This article has 84 citations and is from a highest quality peer-reviewed journal.

12. (hubau2019recyclingorientedmethodologyto pages 3-5): Agathe Hubau, Alexandre Chagnes, Michel Minier, Solène Touzé, Simon Chapron, and Anne-Gwénaëlle Guezennec. Recycling-oriented methodology to sample and characterize the metal composition of waste printed circuit boards. Waste management, 91:62-71, May 2019. URL: https://doi.org/10.1016/j.wasman.2019.04.041, doi:10.1016/j.wasman.2019.04.041. This article has 84 citations and is from a highest quality peer-reviewed journal.

13. (yken2021acomparisonof pages 18-19): Jonovan Van Yken, Ka Yu Cheng, Naomi J. Boxall, Chris Sheedy, Aleksandar N. Nikoloski, Navid R. Moheimani, and Anna H. Kaksonen. A comparison of methods for the characterisation of waste-printed circuit boards. Metals, 11:1935, Nov 2021. URL: https://doi.org/10.3390/met11121935, doi:10.3390/met11121935. This article has 29 citations.

14. (yken2021acomparisonof pages 16-18): Jonovan Van Yken, Ka Yu Cheng, Naomi J. Boxall, Chris Sheedy, Aleksandar N. Nikoloski, Navid R. Moheimani, and Anna H. Kaksonen. A comparison of methods for the characterisation of waste-printed circuit boards. Metals, 11:1935, Nov 2021. URL: https://doi.org/10.3390/met11121935, doi:10.3390/met11121935. This article has 29 citations.

15. (lotter2008identificationandquantification pages 61-67): SJ Lötter. Identification and quantification of impurities in zircon, pdz and other relevant zirconium products. Unknown journal, 2008.

16. (yken2021acomparisonof pages 8-12): Jonovan Van Yken, Ka Yu Cheng, Naomi J. Boxall, Chris Sheedy, Aleksandar N. Nikoloski, Navid R. Moheimani, and Anna H. Kaksonen. A comparison of methods for the characterisation of waste-printed circuit boards. Metals, 11:1935, Nov 2021. URL: https://doi.org/10.3390/met11121935, doi:10.3390/met11121935. This article has 29 citations.
