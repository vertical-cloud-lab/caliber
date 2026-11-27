# q2_sharpness

**Query:** In wedge or knife-edge cleaving of brittle ionic single crystals such as MgO, LiF, NaCl and mica, what makes a blade or crack starter 'sharp' enough to initiate cleavage? Give quantitative criteria where available: the edge (tip) radius of new versus used single-edge steel razor blades (in nm or um), wedge/bevel angle, how the edge radius compares with the critical flaw size from fracture mechanics (K_IC, Griffith), and how a blunted edge or a blunt saw notch changes the load needed and the tendency to indent or plastically deform the crystal instead of cleaving it. How does a sawn notch root radius compare with the notch tip radius required for valid fracture toughness tests of ceramics (e.g., SEVNB, ISO 23146, ASTM C1421)? Is a hardened steel razor blade hard enough relative to single-crystal MgO to act as a crack initiator without its edge dulling or deforming?

Question: In wedge or knife-edge cleaving of brittle ionic single crystals such as MgO, LiF, NaCl and mica, what makes a blade or crack starter 'sharp' enough to initiate cleavage? Give quantitative criteria where available: the edge (tip) radius of new versus used single-edge steel razor blades (in nm or um), wedge/bevel angle, how the edge radius compares with the critical flaw size from fracture mechanics (K_IC, Griffith), and how a blunted edge or a blunt saw notch changes the load needed and the tendency to indent or plastically deform the crystal instead of cleaving it. How does a sawn notch root radius compare with the notch tip radius required for valid fracture toughness tests of ceramics (e.g., SEVNB, ISO 23146, ASTM C1421)? Is a hardened steel razor blade hard enough relative to single-crystal MgO to act as a crack initiator without its edge dulling or deforming?

## Sharpness Criteria for Wedge or Knife-Edge Cleaving of Brittle Ionic Single Crystals

### 1. Edge (Tip) Radius of Razor Blades: New Versus Used

The sharpness of a blade or crack starter is fundamentally governed by the radius of curvature at the cutting edge tip. Commercially manufactured new razor blades can achieve edge tip radii as sharp as approximately 50 nm (0.05 μm) (koppaka2025characterizationof3d pages 1-4). Electrochemical sharpening processes have demonstrated even finer radii of approximately 40 nm on razor blade edges (stone2016electrosharpeningoftungsten pages 1-6). In contrast, used or worn blades exhibit dramatically larger edge radii due to rolling, chipping, and abrasive wear. Rolled or dull edges have been measured at approximately 20–24 μm, and SEM comparisons have shown that a dull boning-knife edge radius is approximately 30 times larger than the corresponding sharp edge radius (dredge2018opticalmeasurementof pages 33-43, dredge2018opticalmeasurementof pages 27-33). This represents a degradation from the sub-100 nm scale to the tens-of-micrometers scale—a factor of several hundred in tip radius.

### 2. Wedge/Bevel Angle

Razor blades and scalpels typically have a double-bevel (included) angle of approximately 15°, which produces an extremely acute wedge geometry that concentrates stress at the tip (dredge2018opticalmeasurementof pages 13-19). For crystal cleaving applications, the included angle may be larger; for example, the in-situ UHV crystal cleaver described by Schmid et al. uses a cutting angle φ_cut ≈ 42° with a clearance angle φ_clear ≈ −6° (schmid2006deviceforin pages 1-5). This design introduces the cleavage force at a single point rather than along a line, producing a highly localized stress field that facilitates cleavage even in hard materials such as NiO (schmid2006deviceforin pages 1-5). Sharpness studies indicate that while bevel angle influences the overall blade geometry and durability, edge-tip radius is the dominant parameter controlling the stress intensity at the crack initiation site (dredge2018opticalmeasurementof pages 19-27, woerden2016astudyof pages 8-14).

### 3. Cleavage Fracture Toughness and Comparison with Blade Tip Radius

The cleavage fracture toughness (K_IC) values for the ionic single crystals of interest, all on their {100} cleavage planes, are:

- **NaCl**: K_IC ≈ 0.17 MPa·m^(1/2) (schultz1994singlecrystalcleavage pages 11-13, gao2601cleavagetoughnessof pages 2-3)
- **LiF**: K_IC ≈ 0.31–0.50 MPa·m^(1/2) (schultz1994singlecrystalcleavage pages 11-13, schultz1994singlecrystalcleavage pages 9-11)
- **MgO**: K_IC ≈ 0.81 MPa·m^(1/2) (schultz1994singlecrystalcleavage pages 11-13)

The intrinsic surface energy of MgO is 1.15 ± 0.08 J/m² (1150 ± 80 erg/cm²), with cleavage-associated plastic work adding only several percent at room temperature—substantially less than the corresponding effect in LiF (futagami1973studyonthe pages 16-19).

The Griffith relation K_IC = √(2E′γ) connects fracture toughness to surface energy and elastic modulus (schultz1994singlecrystalcleavage pages 9-11). From fracture mechanics, the critical flaw size for crack initiation under a given applied stress σ is a_c = (1/π)(K_IC/σ)². For these very low-toughness single crystals, the critical flaw sizes under typical cleavage stresses are on the order of micrometers to tens of micrometers. A new razor blade with a tip radius of ~50 nm is therefore substantially smaller than the critical flaw size regime, meaning it can act as an effective stress concentrator to nucleate a cleavage crack. This is a key criterion: **the blade edge radius must be comparable to or smaller than the critical flaw size** dictated by the crystal's K_IC and the local stress field, so that the stress intensity at the blade tip reaches K_IC before the crystal yields plastically.

### 4. Effect of Blunted Edges and Blunt Notches

When the blade or notch root radius exceeds a critical value ρ_c, two consequences arise:

**Increased load requirement**: In the fracture mechanics framework developed by Damani et al. (1996), a small crack at the tip of a blunt notch experiences a shielded stress field. The ratio of the true stress intensity factor seen by the crack to the nominal value calculated for a sharp crack is given by a weighting function X = tanh(2Y√(δa/ρ)), where δa is the small crack length, Y is a geometric factor, and ρ is the notch root radius. When ρ is large relative to δa, this ratio X << 1, meaning that significantly higher applied loads are required to reach K_IC at the crack tip (damani1996criticalnotchrootradius pages 2-3, damani1996criticalnotchrootradius pages 3-5). Experimentally, measured fracture toughness increases systematically with notch root radius once ρ exceeds the material-specific critical value ρ_c (damani1996criticalnotchrootradius pages 1-2, damani1996criticalnotchrootradius pages 6-7).

**Transition from cleavage to indentation/plastic deformation**: A blunt edge distributes the applied force over a larger contact area, creating predominantly compressive and shear stresses rather than the tensile (mode I) stress needed for cleavage. In MgO, this manifests as Vickers-type indentation producing characteristic "picture frame" slip line patterns on {110} planes and associated {110} and {100} cracks radiating from indentation corners (everitt1990indentationcreepand pages 68-74, everitt1990indentationcreepand pages 74-81). Cleavage-associated dislocation generation occurs only in the immediate vicinity of a moving crack tip and adds only several percent to the effective surface energy in MgO at room temperature (futagami1973studyonthe pages 16-19, futagami1973studyonthe pages 1-5). However, when the contact is blunt and compressive, extensive plastic deformation via dislocation multiplication on {110}⟨110⟩ slip systems occurs instead, and the crystal is indented rather than cleaved.

Schmid et al. (2006) demonstrated this principle by showing that applying the cleavage force at a single point (wire-cutter principle) facilitates cleavage even of hard crystals like NiO, whereas applying a blade parallel to the crystal surface along a line makes cleavage "rather difficult" because multiple competing initiation sites produce poor surface quality (schmid2006deviceforin pages 1-5).

### 5. Sawn Notch Root Radius Versus SEVNB/ISO 23146/ASTM C1421 Requirements

The notch sharpness requirements for valid fracture toughness testing of ceramics provide a useful quantitative framework for understanding what constitutes a "sharp" crack starter:

- **Diamond-saw-cut notch root radius**: Typically 20–100+ μm, depending on blade thickness and grit size. Even with a 50 μm saw blade, the effective root radius is on the order of tens of micrometers (morrell1999precrackingtestpiecesof pages 3-6, damani1996criticalnotchrootradius pages 6-7).
- **Razor blade + diamond paste sharpening (SEVNB method)**: Produces V-notch root radii of approximately 2–15 μm depending on material grain size and paste fineness. In fine-grained ceramics, radii as small as ~2 μm are achievable; in medium-grained alumina, ~15 μm is typical (morrell1999precrackingtestpiecesof pages 3-6, rocha2006effectofnotchroot pages 1-2).
- **Laser notching**: Can produce tip radii below 1 μm (e.g., ~0.7 μm), without root microcracking (wang2021standardizationofthe pages 8-12).

The critical notch radius ρ_c below which measured K_IC becomes independent of notch geometry is material-dependent. The general SEVNB guideline is ρ < 3d (three times the average grain size), but this can be overly strict or insufficient depending on the ceramic. Reported ρ_c values include: ~1.5 μm for fine-grained 5Y-TZP, ~9 μm for polycrystalline alumina with ~1 μm grains, <10 μm for zirconia, <15 μm for hot-pressed silicon nitride, ~20 μm for sintered SiC, and up to ~61 μm for some coarser aluminas (wang2021standardizationofthe pages 12-15, wang2021standardizationofthe pages 8-12, wang2021standardizationofthe pages 4-8). ISO 23146 additionally specifies that the V-notch angle should be less than 30° (wang2021standardizationofthe pages 21-25). A notch-root radius below ~10 μm was found to behave equivalently to a sharp crack in Si₃N₄ ceramics (rocha2006effectofnotchroot pages 1-2).

Thus, an ordinary diamond saw cut (ρ ≈ 20–100+ μm) is far too blunt for valid fracture toughness testing of fine-grained ceramics—and, by analogy, far too blunt to serve as an effective crack starter for cleaving single crystals with their very low K_IC values. Razor blade honing or laser notching is required to reach the sub-10 μm regime.

### 6. Hardness of Steel Razor Blades Versus Single-Crystal MgO

MgO single crystals exhibit pronounced hardness anisotropy on cleaved (001) surfaces. Knoop hardness at room temperature (100 g load) is approximately 4.5 ± 0.5 GPa for the ⟨110⟩ indenter orientation and 11.0 ± 0.5 GPa for the ⟨100⟩ orientation (everitt1990indentationcreepand pages 74-81). Hardened martensitic steel razor blades, typically heat-treated to HRC 58–64, have Vickers hardness approximately 630–800 HV, corresponding to roughly 6–8 GPa (kundig2006mechanicalengineershandbook pages 22-26).

This comparison reveals that a hardened steel razor blade is:
- **Harder than** the softer crystallographic orientations of MgO (~4.5 GPa on ⟨110⟩)
- **Comparable to or softer than** the harder orientations (~11 GPa on ⟨100⟩)

Consequently, a steel razor blade edge may **deform or dull** when pressed against the harder orientations of MgO. However, three factors mitigate this concern for cleavage initiation:

1. **Wedge geometry**: The blade acts as a stress concentrator, not a flat indenter. Even modest penetration generates sufficient tensile stress to initiate a cleavage crack on the very low-toughness {100} planes.
2. **Very low K_IC**: MgO's cleavage toughness of only 0.81 MPa·m^(1/2) means that extremely small flaws or stress concentrations suffice to trigger catastrophic fracture (schultz1994singlecrystalcleavage pages 11-13, schultz1994singlecrystalcleavage pages 1-3).
3. **Single-use expectation**: In practice, razor blades used as crystal crack starters are treated as consumable items. Even if the edge blunts after one use, the initial ~50 nm tip radius is adequate for the first cleavage event.

For softer crystals such as NaCl (K_IC ≈ 0.17 MPa·m^(1/2)) and LiF (K_IC ≈ 0.31–0.50 MPa·m^(1/2)), the hardness mismatch is less critical because their cleavage toughnesses are even lower and their hardnesses are well below that of hardened steel (Mohs ~2.5 for NaCl, ~3 for LiF versus ~6.5 for hardened steel). Mica, being a layered silicate with very weak interlayer bonding, cleaves readily under minimal wedge force with essentially no risk of blade deformation.

The summary of all quantitative parameters is presented in the following table:

| Parameter | Value | Source/Notes |
|---|---:|---|
| New commercial razor-blade tip radius | ≈50 nm (0.05 μm) | Reported achievable radius for commercial razor blades (koppaka2025characterizationof3d pages 1-4) |
| Electrosharpened razor-blade edge radius | ≈40 nm (0.04 μm) | Demonstrated on electrochemically sharpened blades; not necessarily representative of ordinary single-edge utility blades (stone2016electrosharpeningoftungsten pages 1-6) |
| Used/worn or rolled edge | ≈20–24 μm reported rolled-edge scale; dull edge ≈30 times the sharp-edge radius in one SEM comparison | Wear is nonuniform, so no universal used-blade radius exists; rolling, chipping, and abrasion may dominate rather than simple circular rounding (dredge2018opticalmeasurementof pages 33-43, dredge2018opticalmeasurementof pages 27-33) |
| Razor/scalpel double-bevel angle | ≈15° total included angle | A thin, delicate cutting geometry; angle alone does not define sharpness because apex radius remains decisive (dredge2018opticalmeasurementof pages 13-19) |
| Typical meat/kitchen-knife double-bevel angle | ≈40° total included angle | More durable but less acute than a razor or scalpel (dredge2018opticalmeasurementof pages 13-19) |
| Hard-crystal cleaver cutting angle | φcut ≈42° | Schmid cleaver also used φclear ≈−6°; point contact rather than full-line contact facilitated cleavage (schmid2006deviceforin pages 1-5) |
| KIC, NaCl {100} | ≈0.17 MPa·m^1/2 | Very low cleavage toughness (schultz1994singlecrystalcleavage pages 11-13, gao2601cleavagetoughnessof pages 2-3) |
| KIC, LiF {100} | ≈0.31–0.50 MPa·m^1/2 | Literature values vary with specimen and method; {100} is the preferred cleavage plane (schultz1994singlecrystalcleavage pages 11-13, schultz1994singlecrystalcleavage pages 9-11) |
| KIC, MgO {100} | ≈0.81 MPa·m^1/2 | Higher than NaCl and LiF but still characteristic of easy single-crystal cleavage (schultz1994singlecrystalcleavage pages 11-13) |
| MgO intrinsic surface energy | 1.15 ± 0.08 J·m^−2 | Converted from 1150 ± 80 erg·cm^−2; cleavage-associated plastic work adds only several percent at room temperature (futagami1973studyonthe pages 16-19) |
| MgO room-temperature Knoop hardness, reported orientation 1 | 4.5 ± 0.5 GPa | Strongly orientation- and load-dependent; source reports the value for one in-plane indenter orientation on cleaved (001) MgO (everitt1990indentationcreepand pages 74-81) |
| MgO room-temperature Knoop hardness, reported orientation 2 | 11.0 ± 0.5 GPa | Demonstrates large indentation anisotropy; check the original source before assigning these two values to a specific crystallographic direction (everitt1990indentationcreepand pages 74-81) |
| Hardened martensitic razor-steel hardness | Common engineering estimate ≈6–8 GPa, roughly 600–800 HV or HRC ≈58–64 | Retrieved source verifies that razor blades use very hard, brittle quenched martensite but does not supply a blade-specific numerical hardness; this range is an approximate conversion (kundig2006mechanicalengineershandbook pages 22-26) |
| Diamond-wheel or sawn-notch root scale | ≈20 μm for a specially dressed wheel; ordinary saw-cut roots commonly tens of μm and may be substantially larger | A 50 μm saw-blade width is not automatically a 50 μm root radius; broad starter notches 0.1–0.2 mm wide were subsequently sharpened (morrell1999precrackingtestpiecesof pages 3-6, damani1996criticalnotchrootradius pages 6-7, rocha2006effectofnotchroot pages 1-2) |
| Razor blade plus diamond-paste notch radius | ≈2 μm in favorable fine-grained material; ≈15 μm reported for medium-grained alumina | Much sharper than the starter saw cut, but limited by abrasive size and microstructure (morrell1999precrackingtestpiecesof pages 3-6, rocha2006effectofnotchroot pages 1-2) |
| Laser-produced V-notch radius | <1 μm; representative values ≈0.5–0.8 μm | Approximately 0.7 μm was produced without observed root microcracking in one study (wang2021standardizationofthe pages 8-12, wang2021standardizationofthe pages 4-8) |
| SEVNB critical notch radius, ρc | Material-dependent; reported range ≈1.5–61 μm | Below ρc, measured toughness becomes effectively radius-independent; above it, apparent KIC rises. Examples include ≈1.5 μm for fine 5Y-TZP and much larger values for some aluminas (wang2021standardizationofthe pages 12-15, wang2021standardizationofthe pages 8-12, wang2021standardizationofthe pages 4-8) |
| General SEVNB sharpness guideline | ρ < 3d, where d is mean grain size; preferably also ρ < ac, the material's critical flaw size | The 3d rule may be overly restrictive or insufficient depending on strength, toughness, R-curve behavior, and microstructure; ISO-related guidance also specifies a V-notch angle below about 30° (wang2021standardizationofthe pages 12-15, wang2021standardizationofthe pages 21-25, wang2021standardizationofthe pages 4-8) |


*Table: Quantitative comparison of blade geometry, ionic-crystal fracture properties, hardness, and ceramic-notch sharpness. The table distinguishes directly reported measurements from approximate engineering estimates and material-dependent criteria.*

### Synthesis

A blade or crack starter is "sharp enough" to initiate cleavage in brittle ionic single crystals when its edge tip radius is comparable to or smaller than the critical flaw size implied by the crystal's fracture toughness and the applied stress field. For crystals with K_IC values of 0.17–0.81 MPa·m^(1/2), this means tip radii in the sub-micrometer to low-micrometer range are desirable. A new single-edge steel razor blade with a tip radius of ~50 nm is approximately two to three orders of magnitude sharper than a used blade (~20–24 μm) and well within the sharpness regime needed for cleavage initiation. The bevel angle (~15° for razors) determines the wedge geometry and stress distribution, but tip radius is the dominant factor. A blunted edge or sawn notch (root radius 20–100+ μm) distributes the load over too large an area, raising the force required and favoring plastic indentation over cleavage. The SEVNB ceramic testing standards formalize this understanding through material-specific critical notch radii (ρ_c ≈ 1.5–61 μm). While hardened steel (~6–8 GPa) is comparable in hardness to MgO and may dull against its harder crystallographic orientations, the very low cleavage toughness of MgO ensures that even modest stress concentration from a slightly deformed blade edge is sufficient to nucleate a cleavage crack on {100} planes.

References

1. (koppaka2025characterizationof3d pages 1-4): Saisneha Koppaka, David Doan, Wei Cai, X. Wendy Gu, and Sindy K.Y. Tang. Characterization of 3d printed micro-blades for cutting tissue-embedding material. Extreme Mechanics Letters, 75:102288, Mar 2025. URL: https://doi.org/10.1016/j.eml.2024.102288, doi:10.1016/j.eml.2024.102288. This article has 3 citations and is from a peer-reviewed journal.

2. (stone2016electrosharpeningoftungsten pages 1-6): RFL Stone. Electrosharpening of tungsten probes for arc discharge assembly of carbon nanotubes. Unknown journal, 2016.

3. (dredge2018opticalmeasurementof pages 33-43): D Dredge. Optical measurement of blade edge sharpness. Unknown journal, 2018.

4. (dredge2018opticalmeasurementof pages 27-33): D Dredge. Optical measurement of blade edge sharpness. Unknown journal, 2018.

5. (dredge2018opticalmeasurementof pages 13-19): D Dredge. Optical measurement of blade edge sharpness. Unknown journal, 2018.

6. (schmid2006deviceforin pages 1-5): Martin Schmid, Andreas Renner, and Franz J. Giessibl. Device for in situ cleaving of hard crystals. Text, Jan 2006. URL: https://doi.org/10.5283/epub.25318, doi:10.5283/epub.25318. This article has 12 citations and is from a peer-reviewed journal.

7. (dredge2018opticalmeasurementof pages 19-27): D Dredge. Optical measurement of blade edge sharpness. Unknown journal, 2018.

8. (woerden2016astudyof pages 8-14): S van Woerden. A study of non-contact knife sharpness analysis: a thesis presented in partial fulfilment of the requirements for the degree of master of engineering in product …. Unknown journal, 2016.

9. (schultz1994singlecrystalcleavage pages 11-13): Richard A. Schultz, Martin C. Jensen, and Richard C. Bradt. Single crystal cleavage of brittle materials. International Journal of Fracture, 65:291-312, Feb 1994. URL: https://doi.org/10.1007/bf00012370, doi:10.1007/bf00012370. This article has 126 citations and is from a peer-reviewed journal.

10. (gao2601cleavagetoughnessof pages 2-3): Faming Gao. Cleavage toughness of single crystals. ArXiv, Jan 2601. URL: https://doi.org/10.48550/arxiv.2601.03886, doi:10.48550/arxiv.2601.03886. This article has 0 citations.

11. (schultz1994singlecrystalcleavage pages 9-11): Richard A. Schultz, Martin C. Jensen, and Richard C. Bradt. Single crystal cleavage of brittle materials. International Journal of Fracture, 65:291-312, Feb 1994. URL: https://doi.org/10.1007/bf00012370, doi:10.1007/bf00012370. This article has 126 citations and is from a peer-reviewed journal.

12. (futagami1973studyonthe pages 16-19): Koji FUTAGAMI and Yoshito AKASHI. Study on the plastic deformation during cleavage on mgo single crystals. Reports of Research Institute for Applied Mechanics, 20:21-35, Jan 1973. URL: https://doi.org/10.5109/7172625, doi:10.5109/7172625. This article has 1 citations.

13. (damani1996criticalnotchrootradius pages 2-3): R. Damani, R. Gstrein, and R. Danzer. Critical notch-root radius effect in senb-s fracture toughness testing. Journal of The European Ceramic Society, 16:695-702, Jan 1996. URL: https://doi.org/10.1016/0955-2219(95)00197-2, doi:10.1016/0955-2219(95)00197-2. This article has 264 citations and is from a domain leading peer-reviewed journal.

14. (damani1996criticalnotchrootradius pages 3-5): R. Damani, R. Gstrein, and R. Danzer. Critical notch-root radius effect in senb-s fracture toughness testing. Journal of The European Ceramic Society, 16:695-702, Jan 1996. URL: https://doi.org/10.1016/0955-2219(95)00197-2, doi:10.1016/0955-2219(95)00197-2. This article has 264 citations and is from a domain leading peer-reviewed journal.

15. (damani1996criticalnotchrootradius pages 1-2): R. Damani, R. Gstrein, and R. Danzer. Critical notch-root radius effect in senb-s fracture toughness testing. Journal of The European Ceramic Society, 16:695-702, Jan 1996. URL: https://doi.org/10.1016/0955-2219(95)00197-2, doi:10.1016/0955-2219(95)00197-2. This article has 264 citations and is from a domain leading peer-reviewed journal.

16. (damani1996criticalnotchrootradius pages 6-7): R. Damani, R. Gstrein, and R. Danzer. Critical notch-root radius effect in senb-s fracture toughness testing. Journal of The European Ceramic Society, 16:695-702, Jan 1996. URL: https://doi.org/10.1016/0955-2219(95)00197-2, doi:10.1016/0955-2219(95)00197-2. This article has 264 citations and is from a domain leading peer-reviewed journal.

17. (everitt1990indentationcreepand pages 68-74): N Everitt and NM Everitt. Indentation creep and anisotropy in magnesium oxide and germanium. Unknown journal, 1990.

18. (everitt1990indentationcreepand pages 74-81): N Everitt and NM Everitt. Indentation creep and anisotropy in magnesium oxide and germanium. Unknown journal, 1990.

19. (futagami1973studyonthe pages 1-5): Koji FUTAGAMI and Yoshito AKASHI. Study on the plastic deformation during cleavage on mgo single crystals. Reports of Research Institute for Applied Mechanics, 20:21-35, Jan 1973. URL: https://doi.org/10.5109/7172625, doi:10.5109/7172625. This article has 1 citations.

20. (morrell1999precrackingtestpiecesof pages 3-6): R Morrell. Pre-cracking test-pieces of brittle materials for fracture toughness measurement. Unknown journal, 1999.

21. (rocha2006effectofnotchroot pages 1-2): Cláudio Vasconcelos Rocha and Célio Albano Da Costa. Effect of notch-root radius on the fracture toughness of composite si3n4 ceramics. Journal of Materials Engineering and Performance, 15:591-595, Oct 2006. URL: https://doi.org/10.1361/105994906x136106, doi:10.1361/105994906x136106. This article has 10 citations and is from a peer-reviewed journal.

22. (wang2021standardizationofthe pages 8-12): Anzhe Wang, Xinyuan Zhao, Mingxu Huang, Yehong Cheng, and Dongyang Zhang. Standardization of the laser notching method for measuring fracture toughness in structural ceramics. ArXiv, Jan 2021. URL: https://doi.org/10.21203/rs.3.rs-152425/v1, doi:10.21203/rs.3.rs-152425/v1. This article has 0 citations.

23. (wang2021standardizationofthe pages 12-15): Anzhe Wang, Xinyuan Zhao, Mingxu Huang, Yehong Cheng, and Dongyang Zhang. Standardization of the laser notching method for measuring fracture toughness in structural ceramics. ArXiv, Jan 2021. URL: https://doi.org/10.21203/rs.3.rs-152425/v1, doi:10.21203/rs.3.rs-152425/v1. This article has 0 citations.

24. (wang2021standardizationofthe pages 4-8): Anzhe Wang, Xinyuan Zhao, Mingxu Huang, Yehong Cheng, and Dongyang Zhang. Standardization of the laser notching method for measuring fracture toughness in structural ceramics. ArXiv, Jan 2021. URL: https://doi.org/10.21203/rs.3.rs-152425/v1, doi:10.21203/rs.3.rs-152425/v1. This article has 0 citations.

25. (wang2021standardizationofthe pages 21-25): Anzhe Wang, Xinyuan Zhao, Mingxu Huang, Yehong Cheng, and Dongyang Zhang. Standardization of the laser notching method for measuring fracture toughness in structural ceramics. ArXiv, Jan 2021. URL: https://doi.org/10.21203/rs.3.rs-152425/v1, doi:10.21203/rs.3.rs-152425/v1. This article has 0 citations.

26. (kundig2006mechanicalengineershandbook pages 22-26): BL Bramfitt. Mechanical engineers' handbook: materials and mechanical design. ArXiv, Feb 2006. URL: https://doi.org/10.1002/0471777447, doi:10.1002/0471777447. This article has 31 citations.

27. (schultz1994singlecrystalcleavage pages 1-3): Richard A. Schultz, Martin C. Jensen, and Richard C. Bradt. Single crystal cleavage of brittle materials. International Journal of Fracture, 65:291-312, Feb 1994. URL: https://doi.org/10.1007/bf00012370, doi:10.1007/bf00012370. This article has 126 citations and is from a peer-reviewed journal.