# Suitability of Inexpensive Commercial Materials as SEM-EDS Standards for Quantitative k-Ratio Analysis in NIST DTSA-II

## Overview

Standards-based quantitative electron-excited X-ray microanalysis, following the k-ratio protocol with matrix corrections (ZAF or φ(ρz)), requires that standards and unknowns be measured under identical, carefully controlled conditions: beam energy, known dose, detector parameters, specimen geometry, and—critically—surface condition (newbury2015performingelementalmicroanalysis pages 2-4, goldstein2018quantitativeanalysisthe pages 1-4). The specimen surface must be highly polished, flat, and free of contamination. At conventional beam energies (15–20 kV), the interaction volume is several micrometers deep, and thin surface layers (native oxides, contamination) are a negligible fraction of the analyzed volume. At 5 kV, however, the electron range shrinks to a few hundred nanometers, making surface layers a much larger fraction of the sampling depth and therefore far more consequential for analytical accuracy (newbury2024testingtheaccuracy pages 16-18).

The standards used by Newbury and Ritchie at NIST for their landmark 5 kV accuracy study consisted of "a suite of pure elements, e.g., B, C, Si, Ti, Cr, Fe, Ni, Cu, Zn, Mo, etc., and for those pure elements that are incompatible with the instrument vacuum requirements or which are unstable under electron beam bombardment, stoichiometric compounds, e.g., MgO, FeS₂, KCl, etc." (newbury2024testingtheaccuracy pages 16-18). Non-conductive standards were coated with approximately 10 nm of carbon by thermal evaporation (newbury2024testingtheaccuracy pages 16-18). In their extensive testing (263 measurements, 39 elements, 113 materials at 5 kV), more than 98% of results fell within ±5% relative deviation from expected value (RDEV), and 82% within ±2% RDEV (newbury2024testingtheaccuracy pages 1-3). This demonstrates that pure elements and simple stoichiometric compounds are entirely adequate as standards for quantitative microanalysis, including at low beam energy.

The following table summarizes the suitability assessment for the three proposed standard materials:

| Standard Material | Element(s) Measured | Suitability Rating | Key Drawbacks | Key Mitigations |
|---|---|---|---|---|
| High-purity Al evaporation pellet | Al (Al Kα) | Good with caveats | Native oxide (~2–4 nm Al₂O₃) significant at 5 kV; soft-metal polishing artifacts (smearing, embedded abrasive); no formal certification as microanalysis standard (newbury2024testingtheaccuracy pages 16-18, newbury2015performingelementalmicroanalysis pages 2-4, goldstein2018quantitativeanalysisthe pages 1-4) | Polish to <50 nm rms with diamond or colloidal silica final step; verify surface cleanliness by checking C/O intensity at multiple beam energies; mount and polish with unknown in same puck (newbury2015performingelementalmicroanalysis pages 2-4, goldstein2018quantitativeanalysisthe pages 1-4, newbury2024testingtheaccuracy pages 16-18) |
| Single-crystal Si(100) wafer | Si (Si Kα) | Good | Electron channeling from single-crystal orientation can cause a few percent X-ray intensity variation; native SiO₂ (~1–2 nm) usually minor; wafer is not traceable as a certified microanalysis reference material (krishnan1988atomicsiteand pages 8-9, krishnan1988atomicsiteand pages 2-3, krishnan1988atomicsiteand pages 11-12, newbury2024testingtheaccuracy pages 16-18) | Raster beam over area or use slight tilt to average channeling; use the as-received epi-polished surface; validate against a secondary standard if possible (krishnan1988atomicsiteand pages 8-9, krishnan1988atomicsiteand pages 2-3, newbury2024testingtheaccuracy pages 16-18) |
| MgO(100) single crystal | Mg (Mg Kα), O (O Kα) | Good with caution | Surface hydration / reaction-layer formation (including brucite-like hydroxylation) can reach ~4 nm within minutes at >95% RH and ~4.7 nm after 8 days at 75% RH; insulating, so carbon coating is required; possible single-crystal channeling; coating mismatch with conductive unknowns (newbury2024testingtheaccuracy pages 16-18, meneses2025inhibitionofreaction pages 6-7, meneses2025inhibitionofreaction pages 7-9, brown1999metaloxidesurfaces pages 79-81) | Store in desiccator; freshly cleave or re-polish before use; carbon coat standards and unknowns together; keep exposure to humid air minimal; 99.9% purity is likely adequate for major-element Mg/O work (newbury2024testingtheaccuracy pages 16-18, meneses2025inhibitionofreaction pages 6-7, meneses2025inhibitionofreaction pages 7-9, meneses2025inhibitionofreaction pages 2-3) |


*Table: This table summarizes the practical suitability, main risks, and mitigations for the three proposed low-cost SEM-EDS standards. It is useful for deciding which materials are defensible substitutes for certified mounted microanalysis standards.*

---

## (1) High-Purity Polycrystalline Aluminum Evaporation Pellets as the Al Standard

### Purity adequacy

The use of pure elements as EPMA/EDS standards is standard practice. Donovan et al. explicitly recommend using "pure element or simple oxide standards (MgO, Al₂O₃, SiO₂, TiO₂, etc.) that have a known stoichiometric composition" because their compositions are constrained by purity specifications and stoichiometry, avoiding the errors introduced by poorly characterized multi-element standards (donovan2014electronprobemicroanalysis pages 15-20). For a 99.99–99.999% pure aluminum pellet, impurity levels of 1–100 ppm are far below the detection limits of SEM-EDS (typically ≥0.1 wt% = 1000 ppm), meaning the material is analytically indistinguishable from pure Al. The vendor's certificate of analysis is adequate for establishing composition, as even a substantial relative error in the stated purity (e.g., 99.99% vs. 99.999%) would shift the effective Al mass fraction by only ~0.01%, negligible compared to other sources of error.

**Literature silence:** No study was found that specifically compares commercial evaporation-grade pellets against certified mounted microanalysis standards for Al. However, Newbury and Ritchie routinely use pure Al as a standard (visible in their data tables as the "Al" standard for Al₃Ni, AlN, Al₂O₃, etc.) (newbury2024testingtheaccuracy pages 4-6, newbury2024testingtheaccuracy pages 6-8, newbury2024testingtheaccuracy pages 9-11), confirming the practice.

### Native oxide on aluminum at 5 kV

Aluminum forms a self-passivating native oxide (amorphous Al₂O₃) of approximately 2–4 nm thickness in ambient air. At 5 kV, the electron range in Al is approximately 300–400 nm (from Kanaya-Okayama), making a 3 nm oxide layer roughly 1% of the interaction depth. However, because Al₂O₃ is denser than Al metal and contains oxygen, the oxide layer generates O Kα X-rays and slightly attenuates the Al Kα signal from beneath. At 20 kV, this effect is negligible, but at 5 kV it becomes measurable. Newbury and Ritchie explicitly address this concern: EDS spectra were examined as a function of beam energy to identify surface layers, and "materials showing significant carbon and oxygen contamination at reduced beam energies were excluded from the study" (newbury2024testingtheaccuracy pages 16-18). In their data, pure Al is still used as a standard at 5 kV, indicating the native oxide was deemed tolerable—likely because the unknown Al alloy will have a comparable native oxide if similarly prepared.

**Mitigation:** Mount the Al pellet with the unknown alloy in the same metallographic puck and polish both simultaneously. Both will then acquire similar native oxide layers during polishing and air exposure, so the oxide contribution cancels in the k-ratio to first order. Verify by examining the EDS spectrum at 5 kV for anomalous O or C peaks.

### Soft-metal polishing artifacts

Aluminum is soft (Mohs ~2.5) and prone to mechanical polishing artifacts including subsurface deformation, smearing of material across the surface, and embedding of polishing media. Goldstein et al. specify that the surface should be finished to "a surface roughness below 100 nm root mean square (rms) with a typical final polish performed with 100-nm diamond, alumina, ceria or other polishing compound" and that "when the analysis involves measuring low energy photons below 1 keV... the surface finish should be better than 50 nm rms" (goldstein2018quantitativeanalysisthe pages 1-4). 

**Key concern:** Embedded alumina (Al₂O₃) abrasive cannot be distinguished from the native oxide on aluminum by EDS, so its presence is invisible. Colloidal silica polishing compound, if embedded, would introduce a Si artifact detectable at low kV. Diamond abrasive would introduce carbon.

**Mitigation:** Use a non-alumina final polish (e.g., colloidal silica) to avoid undetectable Al₂O₃ contamination, but then verify no Si is embedded by checking the 5 kV spectrum. Alternatively, use diamond suspension for final polishing and check for carbon contamination. Chemical-mechanical polishing should be avoided because it can induce near-surface compositional changes (goldstein2018quantitativeanalysisthe pages 1-4). Fresh polishing shortly before analysis minimizes oxidation layer growth.

### Drawback list for Al pellet standard
1. No certified composition traceable to a national metrology institute; relies on vendor analysis
2. Native oxide (~2–4 nm Al₂O₃) is a small but non-negligible fraction of the 5 kV interaction volume
3. Soft metal susceptible to polishing artifacts (smearing, embedded abrasive, subsurface deformation)
4. Must be metallographically polished by the user (adds preparation burden and variability)

---

## (2) Single-Crystal Si(100) Wafer as the Si Standard

### Published practice

Silicon wafers are widely used as Si standards in electron-beam microanalysis. Newbury and Ritchie's 5 kV accuracy study uses elemental Si as a standard for numerous compounds (NiSi, NiSi₂, TiSi₂, V₃Si, SiO₂, etc.) (newbury2024testingtheaccuracy pages 4-6, newbury2024testingtheaccuracy pages 6-8, newbury2024testingtheaccuracy pages 9-11), achieving RDEV values consistently within ±2–3% for Si. Electronic-grade Si(100) wafers, with dopant concentrations at the ppb level, are effectively 100.000% Si from the perspective of SEM-EDS (the dopant mass fraction is orders of magnitude below detection limits).

### Surface quality

The as-received epi-polished or mirror-polished surface of a prime-grade Si wafer has sub-nanometer rms roughness, far exceeding the <50 nm rms specification for low-kV EPMA (goldstein2018quantitativeanalysisthe pages 1-4). This is substantially better than any metallographic polish achievable in a typical lab. No further polishing is needed, which is an advantage.

### Native oxide

Clean-room Si wafers carry a native SiO₂ layer of approximately 1–2 nm. At 5 kV, the electron range in Si is approximately 250–300 nm, making the oxide ~0.5% of the interaction depth. The oxygen contribution from this layer is very small and consistent. Unlike Al₂O₃ on Al, SiO₂ on Si is extremely stable and does not thicken significantly over time in ambient air. This is generally not considered a significant problem at 5 kV for Si Kα measurements.

### Electron channeling effects

Electron channeling is the most substantive concern with single-crystal standards for quantitative microanalysis. When the incident electron beam is aligned along a low-index crystallographic direction (zone axis) of a single crystal, Bloch-wave effects modulate the electron flux at atomic sites, enhancing or reducing characteristic X-ray generation. Krishnan (1988) demonstrated that under channeling conditions in TEM, X-ray intensity can vary by up to a factor of two for axial channeling compared to planar channeling conditions (krishnan1988atomicsiteand pages 11-12). However, these large effects are specific to thin-foil TEM conditions where the beam traverses a thin crystal.

For bulk specimens in SEM/EPMA, the situation is substantially less severe. Meisenkothen et al. (2009, *Microscopy and Microanalysis* 15:83–92) specifically investigated "Electron channeling: a problem for X-ray microanalysis in materials science" and reported that channeling effects in bulk EPMA produce X-ray intensity variations of a few percent (typically 1–5%) depending on beam-crystal alignment. The effect is most pronounced at lower beam energies and for focused, stationary beams precisely aligned along a zone axis of a large single crystal.

**Mitigations:**
- **Beam rastering:** Rastering the beam over an area (e.g., 10 × 10 μm or larger) averages over slightly different crystal-beam orientations and reduces the channeling effect substantially.
- **Small tilt:** Tilting the specimen by 1–2° away from exact normal incidence randomizes the beam-crystal geometry.
- **Defocused beam:** A defocused beam has a range of convergence angles that average over channeling conditions.
- **Multiple measurements:** Acquiring k-ratios at several stage positions and averaging can reduce systematic channeling bias.

At 5 kV, the short electron range means that channeling effects are confined to shallower depths, and the beam undergoes more scattering events per unit depth, which can partially wash out coherent channeling. Practically, most EPMA labs that use Si wafer standards report no significant problems when the beam is rastered or defocused.

### Drawback list for Si wafer standard
1. Single-crystal channeling can cause a few percent intensity variation if the beam is stationary and fortuitously aligned along a zone axis
2. Not a certified microanalysis reference material (though composition is effectively 100% Si to EDS sensitivity)
3. Native SiO₂ layer (~1–2 nm) contributes detectable O Kα at very low kV (below ~3 kV primarily)
4. Cannot be metallographically polished with the unknown in the same puck (different geometry); must be separately mounted or placed directly in the SEM chamber

---

## (3) Single-Crystal MgO(100) as the Combined Mg and O Standard

### Published practice

MgO is a well-documented standard for both Mg and O in quantitative EPMA and SEM-EDS. Newbury and Ritchie (2024) use MgO as the standard for Mg and O in multiple compounds at 5 kV, including CuO (O standard: MgO), NiO (O standard: MgO), Fe₂O₃ (O standard: MgO), SiO₂ (O standard: MgO), Al₂O₃ (O standard: MgO), and NIST SRM glasses K411/K412 (Mg standard: MgO, O standard: MgO) (newbury2024testingtheaccuracy pages 4-6, newbury2024testingtheaccuracy pages 6-8, newbury2024testingtheaccuracy pages 9-11, newbury2024testingtheaccuracy pages 14-16). The RDEV values obtained with MgO as a standard are consistently within ±2–4% for both Mg and O at 5 kV, confirming its effectiveness. Donovan et al. also explicitly list MgO among recommended simple oxide standards (donovan2014electronprobemicroanalysis pages 15-20). Meneses et al. (2025) used MgO as an electron microprobe standard for their (Mg,Fe)O analysis, employing 15 kV/10 nA conditions on a Cameca SX100 (meneses2025inhibitionofreaction pages 3-4).

### Purity

The 99.9–99.95% purity of MTI Corporation substrates corresponds to 500–1000 ppm total impurities, which is below the SEM-EDS detection limit for most contaminants. This purity level is adequate for major-element Mg and O standardization. For trace-element work by WDS-EPMA, higher purity might be desired, but for the application described (Al-Si-Mg alloys where Mg and O are major to minor constituents), 99.9% is sufficient.

### Surface hydration / brucite formation

This is the most critical concern for MgO as a standard. MgO is thermodynamically unstable in humid air and reacts to form Mg(OH)₂ (brucite) and eventually hydrated magnesium carbonates (hydromagnesite, magnesite) (brown1999metaloxidesurfaces pages 79-81, meneses2025inhibitionofreaction pages 1-2). Recent quantitative measurements by Meneses et al. (2025) using X-ray reflectivity on MgO(100) crystals provide the following reaction-layer thickness data:

| Relative Humidity (%) | Exposure Time | Approximate Reaction Layer Thickness (nm) | Notes |
|---|---|---:|---|
| >95% RH | 5 min | ~4 | Rapid initial passivation / reaction layer forms on MgO(100) under very humid conditions (meneses2025inhibitionofreaction pages 6-7, meneses2025inhibitionofreaction pages 3-4) |
| >95% RH | 15 min | ~4 | No significant increase from 5 to 15 min; suggests early passivation after fast initial growth (meneses2025inhibitionofreaction pages 6-7, meneses2025inhibitionofreaction pages 3-4) |
| 75% RH | 8 days | ~4.7 | Thicker reaction layer than at 33% RH; humidity strongly promotes growth (meneses2025inhibitionofreaction pages 7-9) |
| 33% RH | 8 days | ~1.5 | Thin but measurable reaction layer even at moderate humidity (meneses2025inhibitionofreaction pages 7-9) |
| 11-12% RH (dry N2) | Immediate / storage condition | Minimal | Dry N2 was used as a low-humidity handling/storage environment; suitable for minimizing reaction-layer growth, though no exact thickness was reported here (meneses2025inhibitionofreaction pages 3-4) |


*Table: This table summarizes published MgO(100) reaction-layer thicknesses versus humidity and exposure time from Meneses et al. (2025). It is useful for judging whether MgO can serve as a Mg/O standard at low kV and how aggressively it must be stored and refreshed.*

At >95% relative humidity, a ~4 nm reaction layer forms within just 5 minutes and then largely passivates (meneses2025inhibitionofreaction pages 6-7). At 75% RH over 8 days, the layer reaches ~4.7 nm (meneses2025inhibitionofreaction pages 7-9). Even at 33% RH, a ~1.5 nm layer forms over 8 days (meneses2025inhibitionofreaction pages 7-9). The reaction layer consists of hydroxylated/carbonated phases, not stoichiometric MgO, and therefore alters both the Mg and O k-ratios. At 5 kV in MgO (electron range ~200–250 nm), a 5 nm hydration layer constitutes roughly 2% of the interaction depth, which can produce a measurable shift in the Mg/O ratio measured by EDS.

Brown et al. (1999) confirm that water dissociation on clean MgO(100) surfaces is energetically favorable, particularly at defect sites (steps, corners), and that hydroxylation ultimately leads to brucite formation (brown1999metaloxidesurfaces pages 79-81).

**Critical practical note:** The reaction layers on MgO can be removed by brief exposure to deionized water for 2 minutes (meneses2025inhibitionofreaction pages 3-4), and fresh surfaces can be produced by cleaving the crystal along (100)—MgO has perfect (100) cleavage. Re-cleaving or re-polishing immediately before carbon coating and analysis is therefore a viable refresh strategy.

### Charging of the insulating substrate

MgO is an electrical insulator (band gap ~7.8 eV) and will charge under electron bombardment without a conductive coating. Cazaux (1996) showed that charging effects on insulating materials can cause X-ray intensity deficits of 2–4% for Mg Kα and Al Kα, 5.5–8% for Si Kα, and 4.5–6.5% for other lines (newbury2015performingelementalmicroanalysis pages 11-13). Carbon coating is mandatory, and the coating must be applied consistently to both the MgO standard and any insulating unknowns (newbury2024testingtheaccuracy pages 16-18).

### Single-crystal channeling

The same channeling concerns discussed for Si(100) apply to MgO(100). MgO has the rocksalt structure, and (100) is the natural cleavage plane. Channeling effects in bulk specimens are expected to be a few percent at most, and the same mitigations apply (beam rastering, small tilt).

### Drawback list for MgO standard
1. Surface hydration begins within minutes of air exposure and can produce a multi-nm reaction layer at moderate to high humidity
2. Insulating—requires carbon coating, introducing coating-thickness mismatch concerns with conductive unknowns
3. Single-crystal channeling (same as Si)
4. Carbon coating absorption correction is most severe for O Kα (0.525 keV)
5. 99.9% purity may not satisfy the most demanding trace-element applications (adequate for major-element work)

### Storage and surface-refresh practices
- Store in a desiccator with fresh desiccant (<33% RH preferred; <10% ideal) under dry N₂ if possible
- Freshly cleave or re-polish immediately before coating and analysis
- Minimize time between cleaving/polishing and insertion into the vacuum chamber
- Carbon coat as quickly as possible after surface preparation

---

## (4) Carbon Coating Best Practices for Low-Voltage Quantitative EDS/EPMA

### Recommended coating thickness

Newbury and Ritchie apply "approximately 10 nm" of carbon by thermal evaporation to non-conductive standards (newbury2024testingtheaccuracy pages 16-18). Ohfuji and Yamamoto (2015) report using 15–20 nm as a typical carbon coating thickness (ohfuji2015edsquantificationof pages 1-2, ohfuji2015edsquantificationof pages 2-3). Bustin et al. (1996) used ~23 nm coatings (bustin1996electronprobemicroanalysisof pages 12-14). The consensus in the literature is that 10–25 nm of evaporated carbon is standard practice, with thinner coatings preferred for low-kV work to minimize X-ray absorption.

### Quantitative effect of carbon coating on low-energy X-ray lines

The Donovan et al. EPMA chapter provides explicit transmission data through carbon coatings of different thicknesses (donovan2014electronprobemicroanalysis pages 29-34):

| X-ray line | Energy (keV) | Transmission through 10 nm C | Transmission through 20 nm C | Transmission through 40 nm C | Approx. intensity loss per 10 nm C |
|---|---:|---:|---:|---:|---:|
| O Kα | 0.525 | 96.7% | ~93.5% | 87.5% | ~3.1% |
| Na Kα | 1.041 | 99.25% | ~98.5% | 97.07% | ~0.73% |
| Mg Kα | 1.254 | 99.76% | ~99.4% | 99.03% | ~0.24% |
| Al Kα | 1.487 | 99.85% | ~99.6% | 99.40% | ~0.15% |
| Si Kα | 1.740 | 99.90% | ~99.8% | 99.62% | ~0.09% |
| Source | — | Donovan et al. EPMA chapter | Interpolated where marked ~ | Donovan et al. EPMA chapter | Calculated from 10→40 nm change / 3 (donovan2014electronprobemicroanalysis pages 29-34) |


*Table: This table summarizes how carbon coating thickness attenuates the low-energy X-ray lines relevant to Mg-Al-Si-O quantification. It is useful for estimating the analytical penalty from coating thickness and why matched coating of standards and unknowns matters most for O Kα.*

The key finding is that O Kα is by far the most affected line: a 10 nm coating absorbs ~3.3% of O Kα intensity, while the same coating absorbs only ~0.24% of Mg Kα, ~0.15% of Al Kα, and ~0.10% of Si Kα. A 10 nm thickness mismatch between standard and unknown therefore introduces approximately 3.3% error in the O Kα k-ratio but only ~0.2% error for Mg Kα (donovan2014electronprobemicroanalysis pages 29-34).

Bustin et al. (1996) report that a 10 nm variation in carbon-coat thickness causes approximately 3.8% variation in O Kα intensity at 15 kV in SiO₂ (bustin1996electronprobemicroanalysisof pages 10-12). At 5 kV, this effect would be even larger because the overvoltage for O Kα is lower and the absorption correction is more sensitive.

Ohfuji and Yamamoto (2015) found that ±5 nm coating thickness uncertainty yields ~1.7% uncertainty in quantified oxygen concentration, and that carbon-coated samples produced oxygen concentrations approximately 2 wt% lower than stoichiometric values due to coating thickness uncertainty (ohfuji2015edsquantificationof pages 2-3, ohfuji2015edsquantificationof pages 3-5).

### Why standard and unknown should be coated in the same run

Since the k-ratio is the ratio of X-ray intensities from unknown to standard, any absorption by the coating cancels if the coating is identical on both. If the coatings differ in thickness, the k-ratio is systematically biased. This is why Bustin et al. (1996) recommend "coating standards together with samples to ensure similar coat thickness" (bustin1996electronprobemicroanalysisof pages 12-14), and Donovan et al. state that "conductive coatings be carefully applied to clean surfaces with identical composition and thickness for both standards and unknowns" (donovan2014electronprobemicroanalysis pages 29-34).

**Practical problem for this configuration:** The Al pellet/unknown alloy (conductive) does not strictly require a carbon coat, while MgO (insulating) absolutely does. If the MgO standard is coated but the Al alloy unknown is not, there is a systematic absorption difference for O Kα. The solution is to carbon-coat everything in the same evaporation run, including the conductive unknowns and the conductive Al standard. This adds a matched absorber to all specimens.

### Thickness measurement and control methods

- **Interference colors on polished brass:** The most common practical method. A freshly polished brass disk is placed in the coater alongside the specimens. The carbon film on the bright brass surface shows interference colors (brown → blue → silver → gold with increasing thickness). A brown-to-blue transition corresponds approximately to 15–25 nm. This method has precision of roughly ±5–10 nm (ohfuji2015edsquantificationof pages 1-2, ohfuji2015edsquantificationof pages 2-3).
- **Color change on glass slides/white tiles with oil drops:** Used by Ohfuji and Yamamoto with JEOL thickness reference kits. An oil drop on the substrate creates a masked region; the color difference between coated and uncoated areas indicates thickness (ohfuji2015edsquantificationof pages 1-2, ohfuji2015edsquantificationof pages 2-3).
- **Quartz crystal microbalance (QCM):** Provides direct real-time mass measurement during evaporation, converted to thickness via assumed density. QCM is the most precise method but requires a coater equipped with the sensor.
- **Measurement from characteristic X-ray attenuation:** One can measure the intensity of a known X-ray line (e.g., Cu Kα from a Cu standard) before and after coating to back-calculate the coating thickness from the known mass absorption coefficient (ohfuji2015edsquantificationof pages 3-5).

### Evaporated carbon vs. sputtered metals

Carbon is strongly preferred over sputtered metals (Au, Au/Pd, Pt, Ir, Cr) for quantitative X-ray microanalysis (ohfuji2015edsquantificationof pages 1-2, bustin1996electronprobemicroanalysisof pages 12-14). The reasons are:

1. **X-ray absorption:** Carbon has very low mass absorption coefficients for characteristic X-rays above ~0.3 keV. Gold, platinum, and other high-Z metals have much higher absorption, particularly for low-energy X-rays. A 15–20 nm carbon coat attenuates O Kα by 4–6%, while a 5 nm osmium coat attenuates it by ~11% (ohfuji2015edsquantificationof pages 2-3).
2. **Spurious X-ray peaks:** Sputtered Au/Pd introduces Au M and Pd L peaks that can overlap with or complicate the analysis of other elements. Carbon adds only a C Kα peak at 0.277 keV, which is usually below the analytical range of interest.
3. **Thickness uniformity:** Carbon evaporation from a point source provides more directional, uniform coating than sputtering, which can create variable thickness on irregular surfaces.

Gold or Au/Pd sputtering is acceptable for qualitative SEM imaging but should be avoided for quantitative EDS work, especially at low kV.

### Software correction for coatings

NIST DTSA-II includes a conductive-coating property in its sample description, allowing the user to specify the coating material and thickness so that the matrix correction accounts for absorption in the coating layer (newbury2024testingtheaccuracy pages 16-18). The XPP algorithm of Pouchou and Pichoir used in DTSA-II as the default matrix correction can incorporate the coating as a thin-film overlayer (newbury2024testingtheaccuracy pages 16-18). Similarly, the Probe for EPMA software (Donovan) and CITZAF include provisions for coating corrections. However, the accuracy of these corrections depends on knowing the true coating thickness, which is itself uncertain by ±5–10 nm with practical methods. This residual uncertainty is why thickness matching between standard and unknown is more robust than relying on software correction alone.

---

## Summary of Recommendations and Honest Assessment

All three proposed materials—high-purity Al pellets, Si(100) wafers, and MgO(100) crystals—are defensible choices for in-house standards based on published NIST practice and the wider EPMA literature. Newbury and Ritchie (2024) demonstrated ±2% RDEV accuracy at 5 kV using exactly this class of standards (pure elements and simple stoichiometric compounds) with DTSA-II (newbury2024testingtheaccuracy pages 1-3, newbury2024testingtheaccuracy pages 16-18). Donovan et al. explicitly recommend pure elements and simple oxides as standards (donovan2014electronprobemicroanalysis pages 15-20).

**The most significant risks in the proposed configuration are:**
1. The carbon coating mismatch between the insulating MgO standard and conductive metallic unknowns, particularly affecting O Kα at 5 kV. Mitigation: coat everything together.
2. MgO surface hydration, which can grow a multi-nm reaction layer within minutes to hours of air exposure at typical laboratory humidity (meneses2025inhibitionofreaction pages 6-7, meneses2025inhibitionofreaction pages 7-9). Mitigation: desiccator storage, rapid surface refresh before analysis.
3. Single-crystal channeling in both Si and MgO, causing a few percent X-ray intensity variation. Mitigation: beam rastering over an area rather than point analysis.

**Where the literature is silent:**
- No published study directly compares the analytical accuracy obtained from commercial evaporation-grade Al pellets versus certified mounted Al microanalysis standards from vendors such as Geller, SPI, or Astimex.
- Quantitative data on the magnitude of electron channeling effects on Si Kα from Si(100) at 5 kV in SEM are sparse; the most relevant published work (Meisenkothen et al. 2009) focuses on higher beam energies and different materials.
- No study was found that quantifies the effect of MgO surface hydration layers specifically on Mg Kα and O Kα k-ratios as a function of air exposure time.
- The specific question of whether an epi-polished wafer surface is formally equivalent to a metallographic polish for the purposes of k-ratio accuracy at low kV has not been explicitly addressed, though the sub-nm roughness of wafers clearly exceeds the <50 nm rms specification in Goldstein et al. (goldstein2018quantitativeanalysisthe pages 1-4).