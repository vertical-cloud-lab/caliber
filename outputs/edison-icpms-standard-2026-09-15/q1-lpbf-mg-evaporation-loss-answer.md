# q1-lpbf-mg-evaporation-loss

## Query

In laser powder bed fusion (LPBF / selective laser melting) of AlSi10Mg, how does the chemical composition of the as-built part differ from the feedstock powder composition? Specifically: what magnitude of magnesium loss by selective evaporation during laser melting has been reported (absolute wt% or relative %), how does it depend on process parameters such as volumetric energy density, and are silicon or aluminum contents measurably changed? Cite quantitative studies that measured both the powder and the as-built chemical composition (e.g., by ICP-OES, ICP-MS, or wet chemistry). Is Zn also lost? Given this, can the feedstock powder composition be assumed identical to the printed part composition for calibration or reference-material purposes at the 0.05 wt% level?

## Answer

## Conclusion

The feedstock composition should **not** be assumed to survive LPBF unchanged. The best parameter-resolved powder/part comparison found shows selective Mg depletion of **0.084–0.168 wt% Mg**, corresponding to **19–38% of the Mg initially present**. Loss increased with laser energy input and was especially sensitive to scan speed. By contrast, the retrieved literature does not demonstrate a comparable bulk loss of Si or Al in AlSi10Mg, and it does not provide convincing paired quantitative evidence for Zn loss. Consequently, powder composition is not an adequate surrogate for printed-part composition at the **0.05 wt%** level, principally because of Mg.

| Study | Comparison / analytical method | Process condition | Quantitative composition result | Interpretation / limitation |
|---|---|---|---|---|
| Liu & Gibbons (2023), low-energy extreme | Feedstock powder: EDX; as-built cylinders: spark OES, with 12 readings per parameter set | 370 W, 2300 mm/s, 0.19 mm hatch, 30 µm layer; **84.67 J/cm²**, an areal energy metric, not volumetric J/mm³ | Powder Mg **0.440 ± 0.010 wt%**; as-built Mg **0.356 wt%**; loss **0.084 wt%**, or **19.1% relative**. Powder also contained Si 9.75 ± 0.03, Al 89.67 ± 0.04, and Fe 0.14 ± 0.03 wt%; corresponding as-built values were not reported. (liu2023controllingchemicalcomposition pages 1-4, liu2023controllingchemicalcomposition pages 4-7) | Even the lowest reported Mg loss exceeds 0.05 wt%. This porous condition was outside the optimized process window; comparing powder EDX with part spark OES is an additional metrological limitation. (liu2023controllingchemicalcomposition pages 4-7) |
| Liu & Gibbons (2023), high-energy extreme | Same paired powder-EDX and as-built-spark-OES comparison | 370 W, 700 mm/s, 0.14 mm hatch, 30 µm layer; **377.55 J/cm²**, an areal energy metric, not volumetric J/mm³ | Powder Mg **0.440 ± 0.010 wt%**; as-built Mg **0.272 wt%**; loss **0.168 wt%**, or **38.2% relative**. Across the tested range, as-built Mg varied by **0.084 wt%**, from 0.356 to 0.272 wt%. (liu2023controllingchemicalcomposition pages 1-4, liu2023controllingchemicalcomposition pages 4-7) | Mg loss increased with energy density. Slower scanning had the strongest effect; higher power and smaller hatch spacing caused smaller additional losses. The authors implicated both peak temperature and hot-exposure time. This extreme was also porous and outside the optimized window; best density occurred near 203.3 J/cm². (liu2023controllingchemicalcomposition pages 4-7, liu2023controllingchemicalcomposition pages 7-11) |
| Macías et al. (2020) | As-built LPBF parts measured by **ICP-OES** at two platform temperatures | EOS M290; optimized manufacturer parameters; platform temperatures **35°C and 200°C** | The authors reported similar compositions for the two built conditions and concluded that raising platform temperature caused no loss of alloying elements. (macias2020influenceonmicrostructure pages 5-9) | Evidence that platform temperature alone did not measurably change part composition under these conditions, but the retrieved text lacked the numerical Table 1 and a paired feedstock-powder assay; it is therefore not a quantitative powder-to-part comparison. (macias2020influenceonmicrostructure pages 5-9) |
| Marola et al. (2018/2020) | Commercial EOS powder used for LPBF; microscopy/EDX, XRD, and DSC emphasized microstructure rather than paired bulk assays | EOSINT M270; the 2020 Cu-mixing study used 180 W, 700 mm/s, 0.14 mm hatch, and 30 µm layers | Only supplier ranges were given: Si **9–11**, Mg **0.20–0.45**, Zn **≤0.10**, Fe **≤0.55 wt%**, and Al balance. No paired quantitative as-built bulk assay of Mg, Si, Al, or Zn was reported. (marola2020alloyingalsi10mgand pages 2-3, marola2018acomparisonof pages 1-6) | These studies cannot quantify selective evaporation. Supplier ranges are specifications, not measurements of the powder lot. Observed changes in phase distribution or supersaturation do not establish a change in bulk elemental composition. (marola2020alloyingalsi10mgand pages 3-5, marola2018acomparisonof pages 6-11) |
| Raza et al. (2021) | Virgin versus long-reused **powder** examined by XPS, STEM-EDX, SEM/TEM, and bulk oxygen analysis; no as-built-part bulk assay | Concept Laser XLINE 2000R; powder reused for up to **30 months** | Nominal powder contained Si **10.1**, Mg **0.4**, and Fe **0.11 wt%**, with Al balance. Spatter fraction reached **3.15%**; mean oxide thickness increased from about **4 nm** to **38 nm**, with MgAl₂O₄/Al₂O₃ enrichment and individual spatter oxide scales as thick as **125 nm**. (raza2021degradationofalsi10mg pages 1-2, raza2021degradationofalsi10mg pages 2-3, raza2021degradationofalsi10mg pages 6-8) | Demonstrates Mg-bearing surface oxidation and powder evolution during reuse, not powder-to-part bulk-composition loss. It cannot establish bulk Mg, Si, Al, or Zn evaporation from printed material. (raza2021degradationofalsi10mg pages 4-6, raza2021degradationofalsi10mg pages 6-8) |


*Table: The table distinguishes true powder-to-part measurements from studies reporting only part composition, supplier ranges, or reused-powder oxidation. The parameter-resolved paired dataset shows Mg depletion exceeding 0.05 wt%.*

## Quantitative Mg loss

Liu and Gibbons measured their Carpenter AlSi10Mg powder by EDX as **0.440 ± 0.010 wt% Mg**, together with **9.75 ± 0.03 wt% Si**, **89.67 ± 0.04 wt% Al**, and **0.14 ± 0.03 wt% Fe**. They then measured as-built cylinders by spark optical-emission spectroscopy, using six positions on each of two replicate cylinders per parameter set. Thus, this is a genuine measured powder/part comparison, although it uses different analytical techniques for the two forms rather than ICP on both. (liu2023controllingchemicalcomposition pages 1-4, liu2023controllingchemicalcomposition pages 4-7)

At their lowest energy input, **84.67 J/cm²**, Mg decreased from 0.440 to **0.356 wt%**: an absolute loss of **0.084 wt% Mg**, or **19.1% relative**. At the highest input, **377.55 J/cm²**, Mg decreased to **0.272 wt%**: an absolute loss of **0.168 wt%**, or **38.2% relative**. The retained Mg therefore varied by **0.084 wt%** across the tested parameter range. (liu2023controllingchemicalcomposition pages 4-7)

An important notation point is that this paper calls its quantity “laser energy density,” but reports it in **J/cm²**. It is an areal/scan energy metric, not conventional volumetric energy density, VED = P/(vht), in J/mm³. Because layer thickness was fixed at 30 µm, its endpoints correspond arithmetically to approximately **28.2 and 125.9 J/mm³**, respectively, if converted by dividing by layer thickness. That conversion does not make energy density universally transferable between machines or scan strategies.

## Dependence on processing parameters

Mg retention fell systematically as energy input increased. Holding other variables approximately fixed:

- increasing laser power from 330 to 370 W caused a modest additional Mg loss;
- increasing hatch spacing from 0.14 to 0.24 mm reduced Mg loss slightly;
- changing scan speed produced the largest effect: slow scanning at 700 mm/s gave the greatest loss, whereas 2300 mm/s with a 0.19-mm hatch gave the least loss.

The authors attributed this behavior to both the maximum melt-pool temperature and residence time near high temperature; scan speed affects both. (liu2023controllingchemicalcomposition pages 4-7)

The extrema should not be mistaken for a normal qualified process window. Both the minimum- and maximum-energy specimens had substantial porosity, while the best density was obtained near **203.3 J/cm²**. The study nevertheless establishes that the powder-to-solid Mg offset is process dependent and can readily exceed 0.05 wt%. (liu2023controllingchemicalcomposition pages 4-7, liu2023controllingchemicalcomposition pages 7-11)

More generally, the literature describes volatilization rate as increasing with dissipated energy density and stresses that laser power, speed, hatch spacing, and layer thickness collectively control the thermal exposure. However, those general discussions are not substitutes for paired composition measurements. (fella2015selectivelaserbeam pages 46-50, fella2015selectivelaserbeam pages 50-53)

## Silicon and aluminum

The Liu–Gibbons study quantified Si and Al in the powder but reported only Mg for the printed cylinders, so it cannot prove numerical conservation of Si or Al. Its physical rationale is consistent with preferential Mg evaporation: Mg has a reported boiling point of about **1090°C**, compared with **2470°C for Al** and **3265°C for Si**. (liu2023controllingchemicalcomposition pages 1-4)

Macías et al. measured LPBF material by **ICP-OES** and found similar compositions for parts made at 35 and 200°C platform temperatures, concluding that the platform-temperature change did not cause alloying-element loss. That is useful evidence that platform preheat alone did not measurably alter composition under their optimized EOS conditions. It is not, however, a powder-to-part comparison in the retrieved text, and the numerical composition table was unavailable. (macias2020influenceonmicrostructure pages 5-9)

Accordingly, the defensible conclusion is:

- **Si:** no measurable selective bulk loss was demonstrated by the retrieved paired studies; microstructural redistribution, supersaturation, and Si precipitation must not be confused with a change in total Si. Marola et al., for example, documented changes in Si phase state and supersaturation rather than a bulk chemical loss. (marola2020alloyingalsi10mgand pages 3-5, marola2018acomparisonof pages 6-11)
- **Al:** no measured selective Al depletion was established for AlSi10Mg. Because compositions are normalized to 100%, removal of Mg produces a very small apparent increase in Al balance even if no Al is added or preferentially retained.

## Is Zn also lost?

Zn is physically expected to be at least as evaporation-prone as Mg: Liu and Gibbons list boiling points of approximately **907°C for Zn** and **1090°C for Mg**. They deliberately selected Mg because its concentration was high enough to measure and control; Zn was nominally only **≤0.10 wt%**, and they stated that its adjustable range was insufficient. They did not report powder or part Zn measurements. (liu2023controllingchemicalcomposition pages 1-4)

Thus, **Zn loss is plausible, but it was not quantitatively demonstrated for commercial AlSi10Mg by the retrieved paired-composition studies**. It would be inappropriate to report a numerical Zn-loss correction from these data. Evidence of Mg-rich oxides in reused powder likewise does not establish bulk Zn or Mg loss from the printed part: Raza et al. studied powder-surface oxidation and spatter, not paired powder/solid bulk composition. (raza2021degradationofalsi10mg pages 1-2, raza2021degradationofalsi10mg pages 6-8)

## Implication for calibration and reference-material use

The powder and printed part cannot be treated as compositionally identical at **0.05 wt%** accuracy:

1. The smallest directly reported powder-to-part Mg difference was **0.084 wt%**, already 68% larger than a 0.05-wt% tolerance.
2. The process-induced range among printed conditions was itself **0.084 wt% Mg**.
3. The largest observed powder-to-part difference was **0.168 wt% Mg**.
4. The paired study used powder EDX and solid OES, introducing form- and method-dependent biases in addition to genuine evaporation.

For calibration or reference-material purposes, the printed lot should therefore be sampled and assayed directly—preferably by validated dissolution ICP-OES/ICP-MS or an appropriate wet-chemistry method—with homogeneity and uncertainty assessed on the printed material itself. A powder certificate or powder assay may document the starting material, but it cannot assign the Mg content of the printed solid to ±0.05 wt% unless a fixed process-specific transfer correction has been independently validated. Supplier specification ranges, such as Mg 0.20–0.45 wt%, are particularly unsuitable because they are neither lot-specific measurements nor powder-to-part transfer data. (marola2020alloyingalsi10mgand pages 2-3, pires2021investigationofthe pages 25-29)

## References

1. (liu2023controllingchemicalcomposition pages 1-4): Bochuan Liu and Gregory J. Gibbons. Controlling chemical composition changes in laser powder bed fusion of alsi10mg. ConferencePaper, Jan 2023. URL: https://doi.org/10.26153/tsw/50945, doi:10.26153/tsw/50945. This article has 1 citations.

2. (liu2023controllingchemicalcomposition pages 4-7): Bochuan Liu and Gregory J. Gibbons. Controlling chemical composition changes in laser powder bed fusion of alsi10mg. ConferencePaper, Jan 2023. URL: https://doi.org/10.26153/tsw/50945, doi:10.26153/tsw/50945. This article has 1 citations.

3. (liu2023controllingchemicalcomposition pages 7-11): Bochuan Liu and Gregory J. Gibbons. Controlling chemical composition changes in laser powder bed fusion of alsi10mg. ConferencePaper, Jan 2023. URL: https://doi.org/10.26153/tsw/50945, doi:10.26153/tsw/50945. This article has 1 citations.

4. (macias2020influenceonmicrostructure pages 5-9): Juan Guillermo Santos Macías, Thierry Douillard, Lv Zhao, Eric Maire, Grzegorz Pyka, and Aude Simar. Influence on microstructure, strength and ductility of build platform temperature during laser powder bed fusion of alsi10mg. Acta Materialia, 201:231-243, Dec 2020. URL: https://doi.org/10.1016/j.actamat.2020.10.001, doi:10.1016/j.actamat.2020.10.001. This article has 269 citations and is from a highest quality peer-reviewed journal.

5. (marola2020alloyingalsi10mgand pages 2-3): Silvia Marola, Dario Gianoglio, Federico Bosio, Alberta Aversa, Massimo Lorusso, Diego Manfredi, Mariangela Lombardi, and Livio Battezzati. Alloying alsi10mg and cu powders in laser single scan tracks, melt spinning, and laser powder bed fusion. Journal of Alloys and Compounds, 821:153538, Apr 2020. URL: https://doi.org/10.1016/j.jallcom.2019.153538, doi:10.1016/j.jallcom.2019.153538. This article has 37 citations and is from a peer-reviewed journal.

6. (marola2018acomparisonof pages 1-6): Silvia Marola, Diego Manfredi, Gianluca Fiore, Marco Gabriele Poletti, Mariangela Lombardi, Paolo Fino, and Livio Battezzati. A comparison of selective laser melting with bulk rapid solidification of alsi10mg alloy. Journal of Alloys and Compounds, 742:271-279, Apr 2018. URL: https://doi.org/10.1016/j.jallcom.2018.01.309, doi:10.1016/j.jallcom.2018.01.309. This article has 203 citations and is from a peer-reviewed journal.

7. (marola2020alloyingalsi10mgand pages 3-5): Silvia Marola, Dario Gianoglio, Federico Bosio, Alberta Aversa, Massimo Lorusso, Diego Manfredi, Mariangela Lombardi, and Livio Battezzati. Alloying alsi10mg and cu powders in laser single scan tracks, melt spinning, and laser powder bed fusion. Journal of Alloys and Compounds, 821:153538, Apr 2020. URL: https://doi.org/10.1016/j.jallcom.2019.153538, doi:10.1016/j.jallcom.2019.153538. This article has 37 citations and is from a peer-reviewed journal.

8. (marola2018acomparisonof pages 6-11): Silvia Marola, Diego Manfredi, Gianluca Fiore, Marco Gabriele Poletti, Mariangela Lombardi, Paolo Fino, and Livio Battezzati. A comparison of selective laser melting with bulk rapid solidification of alsi10mg alloy. Journal of Alloys and Compounds, 742:271-279, Apr 2018. URL: https://doi.org/10.1016/j.jallcom.2018.01.309, doi:10.1016/j.jallcom.2018.01.309. This article has 203 citations and is from a peer-reviewed journal.

9. (raza2021degradationofalsi10mg pages 1-2): Ahmad Raza, Tobias Fiegl, Imran Hanif, Andreas MarkstrÖm, Martin Franke, Carolin Körner, and Eduard Hryha. Degradation of alsi10mg powder during laser based powder bed fusion processing. Materials & Design, 198:109358, Jan 2021. URL: https://doi.org/10.1016/j.matdes.2020.109358, doi:10.1016/j.matdes.2020.109358. This article has 93 citations and is from a highest quality peer-reviewed journal.

10. (raza2021degradationofalsi10mg pages 2-3): Ahmad Raza, Tobias Fiegl, Imran Hanif, Andreas MarkstrÖm, Martin Franke, Carolin Körner, and Eduard Hryha. Degradation of alsi10mg powder during laser based powder bed fusion processing. Materials & Design, 198:109358, Jan 2021. URL: https://doi.org/10.1016/j.matdes.2020.109358, doi:10.1016/j.matdes.2020.109358. This article has 93 citations and is from a highest quality peer-reviewed journal.

11. (raza2021degradationofalsi10mg pages 6-8): Ahmad Raza, Tobias Fiegl, Imran Hanif, Andreas MarkstrÖm, Martin Franke, Carolin Körner, and Eduard Hryha. Degradation of alsi10mg powder during laser based powder bed fusion processing. Materials & Design, 198:109358, Jan 2021. URL: https://doi.org/10.1016/j.matdes.2020.109358, doi:10.1016/j.matdes.2020.109358. This article has 93 citations and is from a highest quality peer-reviewed journal.

12. (raza2021degradationofalsi10mg pages 4-6): Ahmad Raza, Tobias Fiegl, Imran Hanif, Andreas MarkstrÖm, Martin Franke, Carolin Körner, and Eduard Hryha. Degradation of alsi10mg powder during laser based powder bed fusion processing. Materials & Design, 198:109358, Jan 2021. URL: https://doi.org/10.1016/j.matdes.2020.109358, doi:10.1016/j.matdes.2020.109358. This article has 93 citations and is from a highest quality peer-reviewed journal.

13. (fella2015selectivelaserbeam pages 46-50): E FELLA. Selective laser beam melting of alsi10mg alloy. Unknown journal, 2015.

14. (fella2015selectivelaserbeam pages 50-53): E FELLA. Selective laser beam melting of alsi10mg alloy. Unknown journal, 2015.

15. (pires2021investigationofthe pages 25-29): M Pires. Investigation of the selective laser melting process for alsi10mg and al-mg-si alloys fabricated at high laser power. Unknown journal, 2021.
