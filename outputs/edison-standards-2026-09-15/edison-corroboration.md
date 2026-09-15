# Edison Scientific corroboration queries — EDS standards (issue #12)

Submitted 2026-09-15T08:16Z, job type LITERATURE. Six literature queries corroborating the standards discussion in vertical-cloud-lab/caliber#12. Full trajectories in the per-query JSON files.

## q1-carbon-coated-mgo

**Task ID:** `5b6199cc-5a44-48bd-89b6-bb7161008f18`  |  **Status:** success

**Query:** In SEM-EDS / EPMA microanalysis, MgO (periclase) is used as a standard for Mg and O. If the MgO standard must be carbon-coated for conductivity: (1) does the coating itself add a C K-alpha peak to every spectrum, making a coated sample unusable as a carbon standard or for measuring sample carbon? (2) Roughly how much are O K-alpha (0.525 keV) and Mg K-alpha (1.254 keV) intensities attenuated by a 10-25 nm evaporated carbon coat at a 35-40 degree take-off angle? (3) What is best practice when the standard is coated but the unknowns are uncoated conductive metals - match the coating, or correct for it in software such as NIST DTSA-II?

Question: In SEM-EDS / EPMA microanalysis, MgO (periclase) is used as a standard for Mg and O. If the MgO standard must be carbon-coated for conductivity: (1) does the coating itself add a C K-alpha peak to every spectrum, making a coated sample unusable as a carbon standard or for measuring sample carbon? (2) Roughly how much are O K-alpha (0.525 keV) and Mg K-alpha (1.254 keV) intensities attenuated by a 10-25 nm evaporated carbon coat at a 35-40 degree take-off angle? (3) What is best practice when the standard is coated but the unknowns are uncoated conductive metals - match the coating, or correct for it in software such as NIST DTSA-II?

## Conclusion

**Yes:** an evaporated carbon film is itself excited by the electron beam and contributes a C Kα peak near 0.277 keV. **For a 10–25 nm film, O Kα is attenuated by a few percent—roughly 2–8% over that thickness range—whereas Mg Kα attenuation is usually well below 1%.** For rigorous standard-based work, matching the coatings remains the safest practice; when standards and unknowns cannot be matched, the known coating should be handled explicitly as a surface layer.

### 1. Carbon peak and carbon analysis

A carbon-coated MgO standard will normally show coating-derived C Kα in every spectrum acquired from its coated surface. Carbonaceous surface films are documented both to produce their own carbon X-rays and to absorb X-rays emitted by the underlying material. Treating surface-film carbon as though it were uniformly distributed through a bulk specimen gives incorrect carbon concentrations and propagates errors into the matrix correction (gopon2017ultra‐reducedphasesin pages 6-8, graser2008electronprobemicroanalysis pages 2-3).

Consequently:

- The coated MgO remains usable as an **Mg and O standard**, provided coating absorption is canceled by matching or is corrected.
- It is **not a clean bulk-carbon standard**. A thin carbon film does not have the geometry or electron/X-ray generation behavior of a bulk carbon standard.
- Ordinary bulk EDS/EPMA cannot uniquely distinguish carbon in the coating from carbon in the specimen because both contribute at C Kα. Thus, a coated unknown is generally unsuitable for direct intrinsic-carbon determination unless coating thickness is independently known and a validated layered-film model, blank/differential measurement, or another analytical strategy is used.
- Beam-induced hydrocarbon deposition adds a further, time-dependent carbon contribution, so clean vacuum practice, plasma cleaning/cold trapping, and time-dependent checks matter for carbon work (gopon2017ultra‐reducedphasesin pages 8-9).

### 2. Approximate attenuation

For a planar film of normal thickness *t* and take-off angle θ measured from the specimen surface, substrate X-ray transmission is approximately

**T = exp[−(μ/ρ)ρt/sin θ]**, with attenuation **A = 1 − T**.

At θ = 35–40°, the X-ray path through the film is about **1.56–1.74 times** its normal thickness. Published EDS calculations report approximately **4–6% attenuation for low-energy O Kα through a 15–20 nm carbon coat**, and emphasize that oxygen is particularly sensitive to uncertainty in coating thickness (ohfuji2015edsquantificationof pages 3-5, ohfuji2015edsquantificationof pages 2-3).

| Carbon thickness (nm) | Effective path, *t*/sin θ (nm), θ = 35–40° | O Kα attenuation at 0.525 keV (%) | Mg Kα attenuation at 1.254 keV (%) |
|---:|---:|---:|---:|
| 10 | 15.6–17.4 | ≈2–3 | ≈0.1–0.2 |
| 15 | 23.3–26.2 | ≈4–5 | ≈0.2–0.3 |
| 20 | 31.1–34.9 | ≈5–6 | ≈0.2–0.4 |
| 25 | 38.9–43.6 | ≈6–8 | ≈0.3–0.6 |


*Table: Estimated attenuation by an evaporated carbon coat at a 35–40° take-off angle. O Kα values are anchored to the published 4–6% attenuation for 15–20 nm carbon and scaled by Beer–Lambert optical depth (ohfuji2015edsquantificationof pages 3-5, ohfuji2015edsquantificationof pages 2-3); Mg Kα values are rough coefficient-based estimates and depend on film density and the attenuation database.*

These numbers should be treated as practical estimates, not universal constants. They vary with the actual film mass thickness—density × thickness—carbon-film porosity/contamination, take-off angle, and the attenuation-coefficient database. The **O estimates are literature-anchored**. The **Mg estimates are coefficient-based order-of-magnitude values**; because 1.254-keV Mg Kα is much less strongly absorbed by carbon than 0.525-keV O Kα, its loss through this thickness range should ordinarily be only a few tenths of a percent.

The coating can also alter electron energy and X-ray generation slightly, although for 10–25 nm carbon at conventional SEM/EPMA voltages, absorption is the principal line-specific effect under discussion. Complete multilayer models account for electron scattering/energy loss as well as X-ray absorption and fluorescence (armstrong2009useofmultilayer pages 1-2).

### 3. Coated standard versus uncoated conductive metals

**Preferred metrological practice:** put the same coating material and approximately the same mass thickness on standards and unknowns, preferably coating them together. EPMA teaching guidance explicitly recommends equal coating thickness, commonly around 250 Å (25 nm) for conventional analysis (chatterjee2012electronmicroprobeanalysis pages 36-39). Matching causes most coating effects to cancel in the measured unknown/standard intensity ratio.

If the conductive metal unknowns must remain uncoated, do **not** simply combine their uncoated intensities with an uncorrected coated-MgO standard. The coating suppresses the standard’s O and Mg intensities, especially O. For an uncoated unknown, this makes the corresponding measured k-ratio too large and therefore tends to bias the reported concentration upward—by approximately the coating attenuation before nonlinear matrix-correction effects. For example, 5% suppression of the standard’s O intensity increases the raw O k-ratio by about 1/0.95 − 1 = **5.3%**.

The alternatives, in preferred order, are:

1. **Use an uncoated, conductive standard** appropriate for the relevant element and line, if available and suitably characterized.
2. **Match the coatings**, even though the unknown metal does not require one electrically. This is generally simplest and least model-dependent.
3. **Measure the carbon-film mass thickness and apply a validated coating/multilayer correction** to the coated standard. Armstrong reports that multilayer correction substantially improved analyses with differing carbon coatings, while warning that uncorrected coating differences can produce errors exceeding 5–10% in some cases (armstrong2009useofmultilayer pages 1-2).

For **NIST DTSA-II**, use this third route only if the specific quantification workflow explicitly represents the carbon as a film over the standard and applies that geometry consistently when predicting the standard intensity or k-ratio. Enter carbon as an overlayer with measured thickness/density—not as carbon dissolved in bulk MgO. A generic bulk ZAF/φ(ρz) correction, or merely including C in the fitted composition, is not equivalent to a layered correction. Layered programs can correctly model carbon as a surface film rather than substrate carbon (gopon2017ultra‐reducedphasesin pages 6-8).

Because the retrieved literature establishes the validity of multilayer corrections but does not document a particular DTSA-II interface or version-specific command, the correction should be validated experimentally—for example, by comparing coated and uncoated measurements of a conductive reference. If DTSA-II’s workflow cannot explicitly model the asymmetry of a coated standard and uncoated unknown, matching coatings or using an uncoated standard is preferable to an ad hoc intensity correction.

References

1. (gopon2017ultra‐reducedphasesin pages 6-8): Phillip Gopon, Michael J. Spicuzza, Thomas F. Kelly, David Reinhard, Ty J. Prosa, and John Fournelle. Ultra‐reduced phases in apollo 16 regolith: combined field emission electron probe microanalysis and atom probe tomography of submicron fe‐si grains in apollo 16 sample 61500. Meteoritics & Planetary Science, 52:1941-1962, Sep 2017. URL: https://doi.org/10.1111/maps.12899, doi:10.1111/maps.12899. This article has 30 citations and is from a peer-reviewed journal.

2. (graser2008electronprobemicroanalysis pages 2-3): Giles DROOP. David Plant Gräser, Peter, M. J. Rigby, Giles Droop, and Peter Gräser. Electron probe micro-analysis of oxygen in cordierite : potential implications for the analysis of volatiles in minerals. South African Journal of Geology, 111:239-250, Sep 2008. URL: https://doi.org/10.2113/gssajg.111.2-3.239, doi:10.2113/gssajg.111.2-3.239. This article has 15 citations and is from a peer-reviewed journal.

3. (gopon2017ultra‐reducedphasesin pages 8-9): Phillip Gopon, Michael J. Spicuzza, Thomas F. Kelly, David Reinhard, Ty J. Prosa, and John Fournelle. Ultra‐reduced phases in apollo 16 regolith: combined field emission electron probe microanalysis and atom probe tomography of submicron fe‐si grains in apollo 16 sample 61500. Meteoritics & Planetary Science, 52:1941-1962, Sep 2017. URL: https://doi.org/10.1111/maps.12899, doi:10.1111/maps.12899. This article has 30 citations and is from a peer-reviewed journal.

4. (ohfuji2015edsquantificationof pages 3-5): Hiroaki OHFUJI and Masashi YAMAMOTO. Eds quantification of light elements using osmium surface coating. Journal of Mineralogical and Petrological Sciences, 110:189-195, Jan 2015. URL: https://doi.org/10.2465/jmps.141126, doi:10.2465/jmps.141126. This article has 30 citations and is from a peer-reviewed journal.

5. (ohfuji2015edsquantificationof pages 2-3): Hiroaki OHFUJI and Masashi YAMAMOTO. Eds quantification of light elements using osmium surface coating. Journal of Mineralogical and Petrological Sciences, 110:189-195, Jan 2015. URL: https://doi.org/10.2465/jmps.141126, doi:10.2465/jmps.141126. This article has 30 citations and is from a peer-reviewed journal.

6. (armstrong2009useofmultilayer pages 1-2): J. Armstrong. Use of multilayer correction procedures to improve the quantitative electron microprobe analyses of coated insulating specimens. Microscopy and Microanalysis, 15:514-515, Jul 2009. URL: https://doi.org/10.1017/s1431927609098857, doi:10.1017/s1431927609098857. This article has 3 citations and is from a peer-reviewed journal.

7. (chatterjee2012electronmicroprobeanalysis pages 36-39): N Chatterjee. Electron microprobe analysis course 12.141. Unknown journal, 2012.

---

## q2-powder-epoxy-standards

**Task ID:** `2ff80981-d967-430f-89c7-db36779a1ba8`  |  **Status:** success

**Query:** Is it accepted practice in SEM-EDS / electron microprobe analysis to prepare quantification standards by mounting high-purity metal powders or granules in epoxy and polishing cross-sections? How large must particles be relative to the electron interaction volume at 15-20 kV, and what artifacts limit accuracy compared with bulk polished standards (surface oxide films at particle boundaries, porosity, smearing of soft metals such as tin, edge effects)?

Question: Is it accepted practice in SEM-EDS / electron microprobe analysis to prepare quantification standards by mounting high-purity metal powders or granules in epoxy and polishing cross-sections? How large must particles be relative to the electron interaction volume at 15-20 kV, and what artifacts limit accuracy compared with bulk polished standards (surface oxide films at particle boundaries, porosity, smearing of soft metals such as tin, edge effects)?

# Epoxy-mounted metal powders as SEM-EDS/EPMA standards

## Conclusion

**Yes—with qualifications.** Embedding high-purity metal grains or fragments in epoxy and polishing through them is an established and technically valid way to make a **working SEM-EDS or EPMA standard mount**. The epoxy itself is not disqualifying if the exposed metallic cross-section is flat, homogeneous, electrically grounded, and sufficiently large that the analyzed point behaves as a semi-infinite bulk specimen. Standards may be co-mounted or kept on a separate mount, and pure elements are acceptable k-ratio standards when their composition and surface condition are known. However, standards practice favors large, independently characterized fragments—approximately millimetre-sized material rather than 10-µm grains—and a mounted powder should not automatically be treated as metrologically equivalent to a certified bulk polished coupon. (carpenter2008epmastandardsthe pages 1-2, newbury2015performingelementalmicroanalysis pages 11-13, newbury2015performingelementalmicroanalysis pages 1-2)

For high-accuracy work, both standard and unknown must be highly polished and unetched, homogeneous on the micrometre scale, and measured at the same beam energy, dose, incidence/take-off geometry, detector conditions, and preferably matched coating thickness. Under such controls, standards-based SEM-EDS can produce approximately 1–3% relative errors in favorable major-element cases and routinely target ±5% for major constituents; nonideal geometry can instead produce errors from tens of percent to nearly an order of magnitude. (newbury2015performingelementalmicroanalysis pages 2-4, newbury2015performingelementalmicroanalysis pages 23-25, newbury2015performingelementalmicroanalysis pages 6-7, newbury2015performingelementalmicroanalysis pages 4-5)

## Required particle size

There is **no universal minimum diameter**. It depends on beam energy, atomic number, density, X-ray line, detector geometry, and whether secondary fluorescence matters. The Kanaya–Okayama electron-range estimate is

\[
R_{KO}(\mu\mathrm{m})=\frac{0.0276\,A\,E_0^{1.67}}{Z^{0.89}\rho},
\]

where \(A\) is atomic mass, \(Z\) atomic number, \(\rho\) density in g cm⁻³, and \(E_0\) beam energy in keV. It estimates maximum electron penetration, not the exact X-ray generation diameter. (humphreys2006simsinvestigationof pages 7-8)

Representative Kanaya–Okayama ranges calculated from that equation are:

| Metal | 15 kV | 20 kV |
|---|---:|---:|
| Al | ~2.9 µm | ~4.7 µm |
| Fe | ~1.1 µm | ~1.7 µm |
| Cu | ~1.0 µm | ~1.6 µm |
| Sn | ~1.4 µm | ~2.2 µm |
| Au | ~0.8 µm | ~1.3 µm |

These are approximate maximum-depth scales; the lateral and useful X-ray generation dimensions must be checked by Monte Carlo simulation for the actual material and lines. Published microanalysis guidance places the 20-keV interaction scale broadly around 1–5 µm and notes that primary X-ray production in bulk SEM-EDS commonly spans approximately 0.5–10 µm. (newbury2006quantitativeelectronprobe pages 2-3, goldstein2018quantitativeanalysisthe pages 1-4)

A conservative practical criterion is therefore:

* use a polished metallic cross-section **at least 5–10 times the largest primary interaction dimension**;
* place the beam **at least 2–3 interaction-volume radii from every metal–epoxy boundary, pore, oxide rim, or neighboring particle**;
* at 15–20 kV, prefer exposed sections **≥20–50 µm across** for routine major-element standardization; larger is better, and approximately 1-mm fragments are preferable where available;
* regard **~10-µm particles as marginal, especially at 20 kV**, for low-density metals such as Al, for points not exactly centered, or where polishing has left only a shallow cap;
* verify adequacy experimentally by moving the beam toward the edge and by comparing 15- and 20-kV results. A stable central plateau is required.

The 5–10× rule is a conservative engineering recommendation rather than a formal universal standard. It is consistent with experiments that used 20–200 µm particles explicitly larger than the interaction volume and found that an ~80-µm particle was effectively flat only near its top center. Conventional matrix corrections did not remove errors caused by curvature, edge position, or altered absorption paths. (newbury2006quantitativeelectronprobe pages 3-4, newbury2006quantitativeelectronprobe pages 4-5, newbury2006quantitativeelectronprobe pages 5-6)

A second, longer length scale applies to **secondary X-ray fluorescence**, which can extend roughly 10–100 µm. Consequently, a 20–50 µm grain may be adequate for major-element k-ratios yet still be imperfect for trace analysis if adjacent particles, metal-filled resin, the mount, or oxide-rich boundaries contain interfering elements. (newbury2006quantitativeelectronprobe pages 6-8, goldstein2018quantitativeanalysisthe pages 1-4)

## Accuracy-limiting artifacts

The main limitations and controls are summarized below.

| Artifact | Mechanism in an epoxy-mounted metal particle | Expected EDS/EPMA bias | Mitigation; comparison with bulk standard |
|---|---|---|---|
| Finite particle / edge effects | If the beam is too close to the particle–epoxy boundary, electrons and generated X-rays escape the metal, while backscattered electrons may excite the epoxy or neighboring material. Local edge slope also changes take-off angle and absorption path. | Reduced metal intensity, low analytical totals, apparent C/O or neighboring-element signal, and line-dependent errors—usually greatest for low-energy X-rays. Normalizing to 100% can hide the problem. (newbury2006quantitativeelectronprobe pages 1-2, newbury2006quantitativeelectronprobe pages 2-3, newbury2015performingelementalmicroanalysis pages 23-25) | Use grains many times larger than the full interaction region; analyze only the broad, flat center, at least several interaction-volume radii from every visible boundary. Confirm by line scans or measurements at increasing edge distance. A large bulk polished standard effectively eliminates finite-size edges. |
| Native oxide shell at particle–epoxy boundary | Powder’s original external oxide becomes an internal rim around the polished metal cross-section; polishing may also form a new oxide film on the exposed face. Small grains have high oxide-to-metal volume and boundary ratios. | O signal and depressed apparent metal concentration if the interaction volume intersects the rim; beam-energy-dependent results; low-energy metal lines may be attenuated. Different oxide thicknesses on standard and unknown invalidate ideal k-ratio cancellation. (remond2002implicationsofpolishing pages 21-22, remond2002implicationsofpolishing pages 14-15, newbury2015performingelementalmicroanalysis pages 4-5) | Select coarse, freshly cleaned granules; measure well inside the metallic core; repolish immediately before use and store dry/inert where warranted. Map O and reject rim-affected grains. Bulk metal has far less boundary oxide per usable area, although its exposed face can still oxidize. |
| Pores, pull-out, and epoxy intrusion | Poor wetting, trapped air, particle packing, or grinding pull-out leaves voids and resin-filled fissures beside or beneath the apparent metal surface. | Loss of metal X-ray yield, C/O contribution, charging, abnormal continuum, low totals, and irreproducible results as the beam overlaps hidden resin or voids. Geometry and specimen-size defects can cause large concentration shifts. (newbury2015performingelementalmicroanalysis pages 6-7, newbury2015performingelementalmicroanalysis pages 5-6) | Vacuum-impregnate with low-viscosity epoxy, disperse particles rather than allowing contact, grind deeply enough to expose sound interiors, and reject grains showing pores in BSE imaging. Dense bulk standards largely avoid resin intrusion and pull-out. |
| Polishing relief, scratches, or rounded edges | Large hardness contrast between metal and epoxy produces differential wear; abrasive polishing may round particle margins, plough grooves, or leave scratches comparable to the X-ray generation depth. | Changed electron scattering and X-ray escape paths; strongly absorbed low-energy lines may vary by several percent to orders of magnitude. Even residual scratches can create outlying analyses. (remond2002implicationsofpolishing pages 7-9, newbury2006quantitativeelectronprobe pages 3-4, newbury2015performingelementalmicroanalysis pages 6-7, newbury2013quantitativesemedsstep pages 1-2) | Use rigid, low-nap cloths, light loads, progressively fine abrasives, and a suitable final polish; verify flatness by SE/BSE imaging and avoid all relief and scratches. Bulk pieces are easier to polish coplanar and provide much larger relief-free areas. |
| Smearing / plastic flow of soft Sn | Tin deforms and ploughs rather than cutting cleanly; polishing can drag Sn across epoxy, pores, oxide rims, or adjacent standards and can fold altered surface material over the exposed core. | Locally elevated Sn outside the grain; variable Sn/O/C within it; concealed pores or oxide; an unrepresentative mechanically worked surface and poor repeatability. Micro-ploughing and wear-debris transfer are recognized preparation artifacts. (remond2002implicationsofpolishing pages 21-22, remond2002implicationsofpolishing pages 3-4) | Use minimal force and heat, sharp fine abrasives, short polishing times, rigid support, and a validated Sn-specific metallographic procedure; clean between stages and inspect maps for Sn tails. A larger bulk Sn coupon is better supported but remains susceptible to smearing. |
| Contamination or embedded abrasive | Diamond, alumina, colloidal silica, lubricant, wear debris, or metal transferred from neighboring standards can lodge in scratches, pores, or the soft metal surface. | Spurious C, O, Al, Si, or neighboring-metal peaks; diluted metal concentration; heterogeneous spot results. Polishing discs contaminated by wear debris can transfer reaction products or material between phases. (remond2002implicationsofpolishing pages 21-22, remond2002implicationsofpolishing pages 19-21, remond2002implicationsofpolishing pages 12-14) | Use dedicated clean consumables, thorough ultrasonic or solvent cleaning where chemically safe, and separate polishing of easily cross-contaminating metals. Screen by maps and reject inclusions. Bulk standards reduce boundary trapping but still require contamination control. |
| Poor electrical grounding / unequal coating | Isolated metal grains may not contact the conductive mount because epoxy surrounds them; charging changes landing energy and beam position. A carbon or metal coating also absorbs X-rays if its thickness differs between standard and unknown. | Count-rate instability, peak shifts, beam drift, altered effective overvoltage, and systematic low-energy-line errors; unequal coating thickness prevents cancellation in the k-ratio. (newbury2015performingelementalmicroanalysis pages 2-4, newbury2015performingelementalmicroanalysis pages 11-13, newbury2015performingelementalmicroanalysis pages 4-5) | Provide a conductive path with carbon paint or a metal-filled mounting route where appropriate; coat standard and unknown together or to matched, monitored thickness. Bulk metal is readily grounded and often needs no coating. |
| Secondary fluorescence / remote excitation | Characteristic or continuum X-rays and backscattered electrons can excite adjacent particles, mounting hardware, or epoxy additives outside the primary electron interaction volume; the fluorescence range can reach tens of micrometres. | False trace/minor peaks or elevated intensities from nearby materials even when the primary interaction volume remains inside the target grain. Bulk-specimen guidance gives typical secondary-fluorescence dimensions of roughly 10–100 µm. (newbury2006quantitativeelectronprobe pages 6-8, goldstein2018quantitativeanalysisthe pages 1-4) | Space grains and unlike standards widely, avoid metal-filled epoxy unless modeled, analyze central regions, and check suspect elements against blank epoxy and isolated grains. A large isolated bulk standard minimizes neighboring-material fluorescence but does not eliminate chamber or holder contributions. |


*Table: Preparation and geometry artifacts that can bias quantitative SEM-EDS or EPMA of epoxy-mounted pure-metal particles, with practical controls and the advantages of bulk polished standards.*

### Surface oxide films

Powders have much more original surface area than bulk coupons. Their native oxide becomes a circumferential internal rim when the grain is sectioned, while polishing and subsequent air exposure can create a new altered film on the exposed face. Polishing-induced metal oxides can range from a few nanometres to hundreds of nanometres. If the interaction volume intersects an oxide rim, the result contains O, gives depressed metal intensity, and no longer represents the nominal pure metal. Differences in native-oxide thickness between standard and unknown also defeat ideal k-ratio cancellation. (remond2002implicationsofpolishing pages 21-22, remond2002implicationsofpolishing pages 14-15, newbury2015performingelementalmicroanalysis pages 4-5)

A nanometre-scale oxide on the central face may have little effect at 15–20 kV for hard metal K lines, but it can matter for oxygen measurement and low-energy metal L/M lines. A micrometre-scale oxidized particle boundary is unacceptable if sampled. Use coarse freshly cleaned granules, map O, analyze only the metallic core, repolish shortly before use, and store oxidation-sensitive standards dry or inert.

### Porosity, pull-out, and epoxy intrusion

Entrapped air, inadequate resin infiltration, agglomerated powder, or grinding pull-out can leave resin-filled pores or subsurface voids. These reduce metal X-ray production, add C/O, alter the continuum, cause charging, and can produce low totals even when the surface appears metallic. Shape, holes, chips, shards, and voids are documented causes of large and scattered SEM-EDS errors. (newbury2015performingelementalmicroanalysis pages 6-7, newbury2015performingelementalmicroanalysis pages 5-6)

Vacuum impregnation with low-viscosity epoxy, widely separated grains, sufficiently deep sectioning, and BSE inspection are necessary. Reject any particle whose central analytical region contains pores, cracks, resin tongues, or pull-out.

### Relief, scratches, and particle edges

The metal–epoxy hardness contrast promotes differential polishing relief and rounded margins. Local slope changes electron backscattering, detector take-off angle, and X-ray absorption path. Effects are strongest for soft X-rays: rough Cu–Au surfaces produced Cu-L/Cu-K errors from −92% to +42%, and even ~100-nm relief can affect O-K and Fe-L intensities by at least 5%. Relief below approximately 20 nm reduced the modeled contribution below 1%; rigorous practical guidance calls for roughly 50-nm-rms or better surfaces for low-energy analysis. (newbury2006quantitativeelectronprobe pages 3-4, newbury2015performingelementalmicroanalysis pages 11-13, newbury2013quantitativesemedsstep pages 1-2)

Near a particle edge, electrons can leave the metal and excite epoxy or nearby phases, and X-rays may experience abnormal escape or absorption paths. Remote excitation by backscattered electrons may also generate apparently real minor or trace peaks outside the intended interaction region. Conventional ZAF or φ(ρz) corrections assume flat bulk geometry and do not correct these effects automatically. (newbury2006quantitativeelectronprobe pages 1-2, newbury2006quantitativeelectronprobe pages 11-12, newbury2006quantitativeelectronprobe pages 6-8)

### Smearing of soft metals, especially tin

Sn is mechanically soft and prone to plastic flow. Under excessive load or a compliant cloth it can plough and smear rather than cut cleanly, dragging Sn across epoxy, oxide rims, pores, or adjacent standards and folding altered material over the metallic core. The general polishing literature documents micro-ploughing, wear-debris transfer, and disproportionate deformation of soft phases; these mechanisms directly explain the familiar Sn-preparation problem, although the cited evidence does not establish a universal numerical Sn error. (remond2002implicationsofpolishing pages 21-22, remond2002implicationsofpolishing pages 3-4)

Use rigid low-nap support, low force and heat, fresh sharp fine abrasive, short polishing steps, thorough cleaning between stages, and an Sn-validated metallographic procedure. Inspect Sn and O maps for tails or films outside the nominal grain. A bulk Sn coupon is better supported and offers a larger clean area, but it too can smear.

## Recommended acceptance test

An epoxy-mounted granular standard should be accepted only after it passes the following checks:

1. **Pedigree:** documented purity and impurity inventory, preferably independently characterized rather than assigned solely by EDS/EPMA. High nominal purity does not establish homogeneity or absence of oxide. (carpenter2008epmastandardsthe pages 1-2, newbury2015performingelementalmicroanalysis pages 1-2)
2. **Geometry:** a flat, unetched central area ≥5–10 interaction dimensions across, with no edge, pore, crack, or second phase within at least 2–3 interaction radii.
3. **Preparation:** minimal relief and scratches; matched conductive coating and reliable grounding. Standards and unknowns should be prepared and measured comparably. (newbury2015performingelementalmicroanalysis pages 2-4, newbury2015performingelementalmicroanalysis pages 11-13)
4. **Imaging/maps:** BSE plus O, C, and target-metal maps to identify oxide rims, epoxy intrusion, polishing debris, and smearing.
5. **Repeatability:** multiple central points on several particles should agree within counting statistics and the laboratory’s control limits. Do not normalize away poor analytical totals; totals are a diagnostic for geometry and contamination. (newbury2015performingelementalmicroanalysis pages 23-25, newbury2015performingelementalmicroanalysis pages 5-6)
6. **Voltage/edge test:** compare central results at 15 and 20 kV and acquire an edge-distance profile. Systematic voltage dependence or drift toward the edge indicates finite size, oxide, porosity, or layered-surface effects.
7. **Traceability:** compare the mounted-particle standard against a validated bulk polished standard. If major-element ratios differ by more than the intended uncertainty—typically a few percent for rigorous standards-based work—the granular mount should be treated only as qualitative or semiquantitative. (newbury2015performingelementalmicroanalysis pages 2-4, newbury2015performingelementalmicroanalysis pages 4-5)

Thus, **coarse epoxy-mounted granules are accepted as practical working standards when validated**, but fine powders are a compromise. For the most accurate EPMA/SEM-EDS calibration—particularly low-energy lines, oxygen, trace constituents, or interlaboratory work—large, dense, polished bulk standards remain preferable because they provide much more edge-free area and reduce oxide-boundary, porosity, resin, relief, grounding, and secondary-fluorescence artifacts.

References

1. (carpenter2008epmastandardsthe pages 1-2): PK Carpenter. Epma standards: the good, the bad, and the ugly. Microscopy and Microanalysis, 14:530-531, Aug 2008. URL: https://doi.org/10.1017/s1431927608088740, doi:10.1017/s1431927608088740. This article has 17 citations and is from a peer-reviewed journal.

2. (newbury2015performingelementalmicroanalysis pages 11-13): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

3. (newbury2015performingelementalmicroanalysis pages 1-2): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

4. (newbury2015performingelementalmicroanalysis pages 2-4): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

5. (newbury2015performingelementalmicroanalysis pages 23-25): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

6. (newbury2015performingelementalmicroanalysis pages 6-7): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

7. (newbury2015performingelementalmicroanalysis pages 4-5): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

8. (humphreys2006simsinvestigationof pages 7-8): M. C.S. Humphreys, S. L. Kearns, and J. D. Blundy. Sims investigation of electron-beam damage to hydrous, rhyolitic glasses: implications for melt inclusion analysis. American Mineralogist, 91:667-679, Apr 2006. URL: https://doi.org/10.2138/am.2006.1936, doi:10.2138/am.2006.1936. This article has 138 citations and is from a peer-reviewed journal.

9. (newbury2006quantitativeelectronprobe pages 2-3): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

10. (goldstein2018quantitativeanalysisthe pages 1-4): Joseph I. Goldstein, Dale E. Newbury, Joseph R. Michael, Nicholas W. M. Ritchie, John Henry J. Scott, and David C. Joy. Quantitative analysis: the sem/eds elemental microanalysis k-ratio procedure for bulk specimens, step-by-step. ArXiv, pages 309-339, Nov 2018. URL: https://doi.org/10.1007/978-1-4939-6676-9\_20, doi:10.1007/978-1-4939-6676-9\_20. This article has 10 citations.

11. (newbury2006quantitativeelectronprobe pages 3-4): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

12. (newbury2006quantitativeelectronprobe pages 4-5): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

13. (newbury2006quantitativeelectronprobe pages 5-6): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

14. (newbury2006quantitativeelectronprobe pages 6-8): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

15. (newbury2006quantitativeelectronprobe pages 1-2): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

16. (remond2002implicationsofpolishing pages 21-22): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

17. (remond2002implicationsofpolishing pages 14-15): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

18. (newbury2015performingelementalmicroanalysis pages 5-6): Dale E. Newbury and Nicholas W. M. Ritchie. Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive x-ray spectrometry (sem/sdd-eds). Journal of Materials Science, 50:493-518, Nov 2015. URL: https://doi.org/10.1007/s10853-014-8685-2, doi:10.1007/s10853-014-8685-2. This article has 630 citations and is from a peer-reviewed journal.

19. (remond2002implicationsofpolishing pages 7-9): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

20. (newbury2013quantitativesemedsstep pages 1-2): D.E. Newbury and N.W. Ritchie. Quantitative sem/eds, step 1: what constitutes a sufficiently flat specimen? Microscopy and Microanalysis, 19:1244-1245, Aug 2013. URL: https://doi.org/10.1017/s1431927613008210, doi:10.1017/s1431927613008210. This article has 20 citations and is from a peer-reviewed journal.

21. (remond2002implicationsofpolishing pages 3-4): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

22. (remond2002implicationsofpolishing pages 19-21): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

23. (remond2002implicationsofpolishing pages 12-14): G. Rémond, C. Nockolds, M. Phillips, and C. Roques-carmes. Implications of polishing techniques in quantitative x-ray microanalysis. Journal of Research of the National Institute of Standards and Technology, 107:639-662, Nov 2002. URL: https://doi.org/10.6028/jres.107.052, doi:10.6028/jres.107.052. This article has 34 citations and is from a peer-reviewed journal.

24. (newbury2006quantitativeelectronprobe pages 11-12): Dale E. Newbury. Quantitative electron probe microanalysis of rough targets: testing the peak-to-local background method. Scanning, 26 3:103-14, Dec 2006. URL: https://doi.org/10.1002/sca.4950260302, doi:10.1002/sca.4950260302. This article has 24 citations.

---

## q3-zr-ce-li-problem-elements

**Task ID:** `dd9eb478-85bc-4dcc-b4e0-1ded9c026db2`  |  **Status:** success

**Query:** For pure-element X-ray microanalysis (EDS/WDS) standards: (a) commercial zirconium is typically Grade 702 containing up to about 4.5 wt% hafnium - does this Hf content introduce significant quantification error when used as a Zr standard, and is low-Hf (crystal bar) zirconium required? (b) Is cerium metal practical as a microanalysis standard given its rapid oxidation in air, or is CeO2 the preferred Ce standard? (c) Can lithium be detected or quantified with conventional silicon drift detector EDS using polymer windows, and what techniques are actually required to measure Li in aluminum alloys?

Question: For pure-element X-ray microanalysis (EDS/WDS) standards: (a) commercial zirconium is typically Grade 702 containing up to about 4.5 wt% hafnium - does this Hf content introduce significant quantification error when used as a Zr standard, and is low-Hf (crystal bar) zirconium required? (b) Is cerium metal practical as a microanalysis standard given its rapid oxidation in air, or is CeO2 the preferred Ce standard? (c) Can lithium be detected or quantified with conventional silicon drift detector EDS using polymer windows, and what techniques are actually required to measure Li in aluminum alloys?

## Conclusions

**(a) Grade 702 zirconium is not an acceptable *nominally pure* Zr standard if its Hf is ignored, but low-Hf crystal-bar Zr is not intrinsically required.** A specimen containing 4.5 wt% Hf contains only about 95.5 wt% Zr. If its Zr intensity is assigned to 100 wt% Zr, the first-order bias in subsequently measured Zr is approximately

\[
\frac{1}{0.955}-1=0.047,
\]

or **+4.7% relative**. That is significant for quantitative WDS/standard-based EDS, although the exact error differs somewhat because Hf changes electron stopping, backscatter, absorption, and fluorescence.

Grade 702 can nevertheless be used as a **Zr–Hf alloy standard** if the actual, homogeneous, lot-specific Zr and Hf concentrations are known and entered into software that supports non-pure standards and full matrix correction. Merely selecting “pure Zr” and measuring Grade 702 is not equivalent. Crystal-bar or otherwise certified low-Hf Zr is preferable for a true pure-element standard, highest-accuracy work, interlaboratory traceability, or characterization of Zr/Hf spectral overlaps; it is not mandatory for routine Zr calibration when a certified alloy composition is handled correctly. The quoted 4.5 wt% should also not be assumed for every specimen: an allowable maximum is not a certificate value.

**(b) Ce metal is generally unsuitable as a routine exposed microanalysis standard; CeO₂ is the practical choice.** The relevant issue is not merely bulk oxidation but whether the electron-excited volume has a stable, known composition. Ce metal develops an oxide/tarnish in air, so a polished mount may no longer present a reproducible metallic-Ce matrix. Reliable metallic Ce would require inert storage and preparation, protected or vacuum transfer, and preferably fresh in-vacuum surface preparation followed by verification that the analyzed volume is oxide-free.

A dense, polished, homogeneous, phase-pure and stoichiometrically verified **CeO₂** standard is much easier to maintain. It must be defined as a compound standard, not as pure Ce. Stoichiometric CeO₂ contains

\[
\frac{140.116}{140.116+2(15.999)}=0.8141,
\]

or **81.41 wt% Ce and 18.59 wt% O**. Matrix corrections must therefore use CeO₂ composition. Possible nonstoichiometry (CeO₂₋ₓ), porosity, polishing relief, charging, contamination, or mixed phases should be checked; a well-characterized natural Ce mineral can also be used when closer matrix matching is advantageous.

**(c) Conventional polymer-window SDD-EDS cannot usefully detect or quantify Li.** Li K radiation is only about **55 eV**, is produced weakly, and is strongly self-absorbed. Published EDX measurements accordingly report no visible Li peak and attribute this to the ultrasoft ~55 eV Li K radiation, low production, and high absorption probability (homad2023synthesisandcharacterization pages 3-6). Detector entrance structures also attenuate X-rays, while ordinary polymer windows include a support grid and light-blocking/protective layers; even work on advanced windows treats roughly 50–1000 eV as the challenging low-energy regime (rowley2021sp2bondedcarbon pages 11-16, rowley2021sp2bondedcarbon pages 25-30). A polymer-window SDD therefore has essentially no useful transmission at the Li line. Absence of a Li peak is not evidence that Li is absent, and standardless EDS totals must not be used to infer Li by difference.

Specialized **windowless, ultra-low-energy EDS** can sometimes demonstrate Li K emission under favorable conditions, but surface films, hydrocarbon contamination, oxidation, detector entrance layers, chemical-state-dependent line shape and extremely low count rates make routine accurate quantification difficult. Conventional crystal WDS is also not automatically a solution: ordinary analyzing crystals and proportional-counter windows do not efficiently handle 55 eV radiation. Only specialized ultrasoft-X-ray spectrometers—such as grazing-incidence or multilayer/soft-X-ray emission systems with windowless detection—are relevant.

For Al–Li alloys, the practical methods are:

- **Nuclear-reaction analysis or nuclear microprobe/ion-beam analysis:** preferred for defensible quantitative Li concentration and, with suitable beam-energy analysis, depth profiles. It requires calibrated reaction yields, stopping powers, geometry, and appropriate standards.
- **SIMS/ToF-SIMS:** highly sensitive Li mapping and depth profiling, but quantitative work requires matrix-matched standards because ion yields are strongly matrix dependent. Retrieved literature identifies SIMS specifically as a route for local Li measurement (zhang2025atomicscaledamageinduced pages 226-228).
- **TEM-EELS or ionization-energy-loss spectroscopy:** suitable for nanoscale Li analysis in thin foils and has been applied specifically to Al–Li alloys; thickness, plural scattering, standards/cross-sections, beam damage, and specimen oxidation must be controlled.
- **Atom-probe tomography:** three-dimensional near-atomic-scale Li partitioning in precipitates and interfaces, with field-evaporation and specimen-preparation biases assessed.
- For a **bulk alloy certificate value** rather than spatial microanalysis, validated wet-chemical or mass-spectrometric analysis is normally preferable.

The resulting practical decisions are summarized below.

| Question | Practical conclusion | Quantitative or physical basis | Recommended practice |
|---|---|---|---|
| **Grade 702 Zr containing up to 4.5 wt% Hf** | It is not a pure-Zr standard if Hf is ignored, but it can be a valid **composition-certified Zr–Hf standard**. Low-Hf crystal-bar Zr is not routinely required. | At 4.5 wt% Hf, the material contains about **95.5 wt% Zr**. Treating its measured Zr intensity as though it represented 100 wt% Zr would give a first-order relative high bias of approximately **1/0.955 − 1 = 4.7%** in an unknown. The exact error also depends on line choice and matrix corrections. | Enter the certified Zr, Hf, and other significant constituents and apply the normal alloy/compound-standard matrix correction. Use homogeneous crystal-bar Zr when a genuinely pure-element standard, the highest accuracy, or uncontaminated Zr/Hf spectral characterization is required. |
| **Ce metal versus CeO₂** | Exposed Ce metal is inconvenient and unreliable for routine microanalysis because its analyzed surface oxidizes. **CeO₂ is generally the preferred practical Ce standard.** | Oxidation changes the surface composition and therefore the X-ray-generating matrix. Stoichiometric CeO₂ contains **140.116/(140.116 + 2×15.999) = 81.41 wt% Ce**; it must not be entered as 100% Ce. | Use dense, polished, homogeneous, phase-pure, and stoichiometrically verified CeO₂, entered as **81.41 wt% Ce and 18.59 wt% O**. Metallic Ce is suitable only with inert storage/transfer and fresh preparation—preferably in vacuum—plus verification that the analyzed volume is oxide-free. |
| **Li in Al alloys with polymer-window SDD-EDS** | Conventional polymer-window SDD-EDS cannot reliably detect or quantify Li. Specialized windowless ultra-low-energy EDS may sometimes detect Li, but it is not a routine robust quantitative method. | Li K emission is only about **55 eV**, with low production and severe self-absorption; detector windows, contamination, and entrance/dead layers remove most or all of the signal. Published EDX observations likewise report no evident Li peak because the ~55 eV radiation produces an extremely weak emitted signal (homad2023synthesisandcharacterization pages 3-6). Detector-front materials and windows attenuate X-rays, while ordinary polymer windows also contain supporting and light-blocking layers (rowley2021sp2bondedcarbon pages 11-16, rowley2021sp2bondedcarbon pages 25-30). | For Al–Li alloys use **nuclear-reaction analysis (NRA)/ion-beam analysis** for quantitative concentration or depth profiles; **SIMS** for sensitive lateral/depth mapping; **TEM-EELS/ionization-energy-loss spectroscopy** for nanoscale analysis; or **atom-probe tomography (APT)** for three-dimensional near-atomic-scale distributions. Treat windowless EDS as specialized, condition-dependent detection rather than the default quantitative Li method. |


*Table: Practical choices and limitations for Zr–Hf, Ce, and Li microanalysis, including the magnitude of uncorrected Zr bias and the techniques appropriate for measuring Li in aluminum alloys.*

In short: **do not call Hf-bearing Grade 702 “pure Zr”; use it only with its certified composition. Use characterized CeO₂ rather than air-exposed Ce metal. Do not expect polymer-window SDD-EDS—or ordinary WDS—to measure Li; use nuclear methods for quantitative concentration/depth information and SIMS, EELS, or atom probe when spatial resolution is required.**

References

1. (homad2023synthesisandcharacterization pages 3-6): H. T. Homad, N. M. Ali, O. A. Al-Jubouri, and M. H. Al-Timimi. Synthesis and characterization of lico1-xnixo2 nanoparticles by urea route as cathode for lithium-ion battery. Journal of Ovonic Research, 19(6):783-791, Dec 2023. URL: https://doi.org/10.15251/jor.2023.196.783, doi:10.15251/jor.2023.196.783. This article has 8 citations and is from a peer-reviewed journal.

2. (rowley2021sp2bondedcarbon pages 11-16): JT Rowley. Sp2 bonded carbon for soft x-ray detector windows. Unknown journal, 2021.

3. (rowley2021sp2bondedcarbon pages 25-30): JT Rowley. Sp2 bonded carbon for soft x-ray detector windows. Unknown journal, 2021.

4. (zhang2025atomicscaledamageinduced pages 226-228): W Zhang. Atomic-scale damage induced in zirconium alloys by neutron irradiation, and the effect on in-reactor corrosion. Unknown journal, 2025.

---

## q4-vpsem-quant

**Task ID:** `a8ede654-3ad7-4b0a-8ae3-434ae052639b`  |  **Status:** success

**Query:** In variable-pressure (low-vacuum / environmental) SEM, how do chamber gas and water vapor affect quantitative EDS analysis: electron beam skirt formation, spurious oxygen signal, and absorption of soft X-rays by the gas? Can EDS standards measured under variable pressure be transferred to high-vacuum analyses, or must standards and unknowns be measured under the same vacuum conditions?

Question: In variable-pressure (low-vacuum / environmental) SEM, how do chamber gas and water vapor affect quantitative EDS analysis: electron beam skirt formation, spurious oxygen signal, and absorption of soft X-rays by the gas? Can EDS standards measured under variable pressure be transferred to high-vacuum analyses, or must standards and unknowns be measured under the same vacuum conditions?

## Conclusion

Chamber gas in variable-pressure/environmental SEM changes both **electron excitation** and **X-ray transmission**. It is therefore not merely a charge-neutralizing background. It can broaden the electron excitation footprint, add gas-derived characteristic radiation, reduce specimen-generated counts, and preferentially attenuate low-energy X-rays. These effects can invalidate ordinary high-vacuum EDS assumptions unless pressure, gas path, geometry, and calibration are tightly controlled.

| Effect | Physical origin | Spectral/quantitative bias | Controlling variables | Practical control |
|---|---|---|---|---|
| Electron beam skirt | Elastic scattering of primary electrons by chamber-gas molecules spreads part of the focused probe over a broad area. | X-rays arise tens–hundreds of micrometres from the intended point; heterogeneous specimens yield composite spectra, false neighboring-phase elements, poorer spatial resolution, and higher detection limits. | Gas species and scattering cross-section; pressure; beam gas-path length; accelerating voltage; temperature; pressure-limiting-aperture design. | Use the lowest pressure that neutralizes charge, shortest gas path/working distance, low-scattering gas, and adequate beam energy; analyze large homogeneous regions or isolate particles from surrounding material. |
| Water-vapor-derived spurious oxygen | Beam excitation or ionization of H₂O molecules produces chamber-gas O K X-rays that can reach the detector. | Adds oxygen not originating in the specimen, causing false O detection or positive bias—especially in weak-O, small-particle, or trace analyses. | Water-vapor pressure; electron path through gas; beam energy/current; detector collimation and view of the gas-excitation region; acquisition geometry. | Measure a gas/blank spectrum under identical conditions; minimize pressure and gas path; treat oxygen cautiously; use another gas when quantitative oxygen is essential. |
| Gas absorption of soft X-rays | Specimen X-rays traverse gas before reaching the detector and undergo energy-dependent attenuation. | Preferentially suppresses low-energy lines, underestimating light elements and distorting line ratios; hard X-rays are affected much less. | X-ray energy; gas composition, density, and pressure; specimen-to-detector path length; detector geometry and take-off angle. | Minimize gas pressure and X-ray path length; maintain fixed geometry; apply validated gas-absorption corrections or calibrate empirically under matched conditions. |
| Standards transfer/matching rule | Variable pressure changes excitation, transmitted probe current, gas-generated radiation, charging, and energy-dependent X-ray transmission relative to high vacuum. | Unmatched standards give biased k-ratios and concentrations; a variable-pressure calibration is not directly transferable to high-vacuum unknowns, or vice versa. | Vacuum mode; gas species and pressure; gas paths to specimen and detector; working distance; beam energy/current; detector geometry; charging state. | Measure standards and unknowns under the same gas, pressure, geometry, beam, and acquisition conditions. Transfer only with a validated physical correction demonstrating equivalence; otherwise acquire separate high-vacuum and variable-pressure standards. |


*Table: Summary of the principal chamber-gas effects on quantitative EDS and the resulting standards-matching requirement.*

## 1. Electron-beam skirt

Primary electrons undergo elastic collisions with chamber-gas molecules. The beam arriving at the specimen consequently consists of an unscattered central probe plus a broad population of scattered electrons—the **electron skirt**. Scattering may also begin in the gas plume above the pressure-limiting aperture, so the effective gas mass thickness is instrument- and aperture-design-dependent, not simply chamber pressure multiplied by the nominal working distance. Danilatos and colleagues showed that this can cause substantial probe-current loss and that the skirt can seriously degrade X-ray microanalysis even when the central spot still gives an apparently sharp electron image. (danilatos2001electronbeamcurrent pages 1-2, danilatos2001electronbeamcurrent pages 2-4, danilatos2001electronbeamcurrent pages 4-6)

The relevant collision probability scales approximately with gas number density, gas scattering cross-section, and beam gas-path length. Thus skirt severity generally increases with:

- chamber pressure;
- beam gas-path length or working distance;
- gas scattering cross-section/atomic number;
- unfavorable pressure-limiting-aperture geometry;
- decreasing accelerating voltage.

It decreases with lower pressure, shorter gas path, a lower-scattering gas, higher electron energy, and—in the basic density relationship—higher gas temperature. (spinkaUnknownyearx–raymicroanalysisin pages 1-4, khouchaf2012gaseousscanningelectron pages 5-10)

The analytical consequence is more serious than simple loss of counts. Skirt electrons retain enough energy to excite characteristic X-rays over an area potentially tens or hundreds of micrometres across. The measured spectrum can therefore include surrounding phases, substrate, mounting medium, or particles that were never under the nominal probe. The spectrum becomes a spatially weighted composite whose skirt component generally cannot be separated from the central-probe component by ordinary peak fitting. This raises detection limits and compromises both spatial attribution and composition. (spinkaUnknownyearx–raymicroanalysisin pages 1-4, khouchaf2012gaseousscanningelectron pages 5-10)

An experimental example involved 10–40 µm smalt grains surrounded by lead white. Although the smalt contained no lead, VP-EDS returned Pb because skirt electrons excited adjacent lead white; water vapor and a 1 mm beam gas-path length minimized this false contribution under the conditions tested. Thus changing the gas can improve one application, but does not remove the fundamental skirt problem. (kugler2013quantitativesemedxanalysis pages 1-2)

The low-voltage penalty can be extreme. Simulations in water vapor at 5 kV gave an unscattered fraction of about 93.2% and a 12 µm skirt radius at 70 Pa and 1 mm gas path, but about 47% and 109.3 µm at 350 Pa and 2 mm. Quantitative EDS under VP conditions is consequently most defensible at the lowest pressure needed for charge control and the shortest practicable gas path, on areas large and homogeneous relative to the skirt. (khouchaf2012gaseousscanningelectron pages 5-10)

## 2. Spurious oxygen with water vapor

There are two distinct ways in which water vapor can produce an apparent oxygen excess:

1. **Direct gas excitation.** Inelastic electron collisions with chamber gas generate characteristic and bremsstrahlung radiation. Because water vapor contains oxygen, excitation of H₂O can contribute an O K signal that originates in the chamber gas rather than the specimen. The literature explicitly identifies gas-generated characteristic X-rays as part of the ESEM analytical blank. (spinkaUnknownyearx–raymicroanalysisin pages 1-4)
2. **Skirt excitation of oxygen-bearing surroundings.** The skirt may excite oxides, hydrated phases, resin, contamination, or neighboring material outside the intended analysis point. That oxygen is real X-ray emission from solids, but it is spatially spurious for the selected feature. (spinkaUnknownyearx–raymicroanalysisin pages 1-4, kugler2013quantitativesemedxanalysis pages 1-2)

A detected O peak under water vapor must therefore not automatically be assigned wholly to the specimen, especially for oxygen-poor specimens, weak O signals, small particles, interfaces, or heterogeneous fields. A gas/holder/substrate blank acquired with the same pressure and geometry helps characterize the irreducible background, but blank subtraction cannot generally reconstruct an unknown, composition-dependent skirt contribution. The most reliable controls are minimum pressure and gas path, restricted detector view of gas-excited regions where instrument design permits, isolation of the feature from surrounding oxygen-bearing material, and use of a non-oxygen-containing gas when accurate oxygen measurement is central.

## 3. Absorption of soft X-rays by chamber gas

Specimen-generated X-rays must pass through chamber gas on their way to the EDS detector. Gas therefore lowers the specimen count rate; the retrieved ESEM literature explicitly reports both gas-generated X-rays and a fall in specimen-derived spectral counts. (spinkaUnknownyearx–raymicroanalysisin pages 1-4)

This attenuation is energy-dependent. **Soft, low-energy X-rays are affected much more strongly than hard X-rays**, so the effect is not a common multiplicative loss that disappears merely by normalizing the spectrum. It can suppress lines used for light elements and low-energy L or M families, change measured line ratios, and bias concentrations downward if the quantification model assumes the high-vacuum detector response. The transmission has the generic form

\[
T(E)=\exp[-\mu(E)\rho L_X],
\]

where \(\mu(E)\) is the energy- and gas-dependent mass attenuation coefficient, \(\rho\) is gas density, and \(L_X\) is the specimen-to-detector X-ray path through the gas. Pressure, gas composition, specimen height, take-off angle, detector position, and path length therefore matter. This X-ray path is conceptually distinct from the **beam gas path** controlling electron scattering, although changing specimen position can alter both.

The retrieved sources establish the count loss but did not provide validated numerical gas-absorption coefficients for specific EDS lines. Accordingly, line-specific correction should use instrument-appropriate attenuation data or empirical calibration rather than a universal pressure correction.

## 4. Can VP standards be transferred to high vacuum?

**Not directly. For standards-based quantitative EDS, standards and unknowns should be measured under the same vacuum and gas conditions unless a validated physical correction explicitly accounts for all differences.**

The reason is that the standard-to-unknown intensity ratio is reliable only when both measurements share the same measurement transfer function. Switching between VP and high vacuum changes several terms simultaneously:

- fraction and spatial distribution of electron current reaching the specimen;
- skirt excitation and the surrounding-material contribution;
- gas-generated characteristic radiation and continuum;
- energy-dependent X-ray attenuation;
- charging and effective landing energy;
- potentially the instrumental gas plume and aperture contribution.

These effects depend strongly on pressure, gas identity, beam and X-ray path lengths, accelerating voltage, specimen geometry, and instrument design. The literature documents both this condition dependence and the restrictive conditions required for quantitative ESEM work. (staniewicz2012transmissionmodeimagingin pages 43-48, danilatos2001electronbeamcurrent pages 1-2, spinkaUnknownyearx–raymicroanalysisin pages 1-4, khouchaf2012gaseousscanningelectron pages 5-10)

Accordingly:

- A standard measured in VP mode should not ordinarily calibrate a high-vacuum unknown.
- A high-vacuum standard should not ordinarily calibrate a VP unknown.
- Merely matching accelerating voltage and nominal beam current is insufficient.
- For VP quantification, match gas species, chamber pressure, beam gas-path length/working distance, specimen height and take-off geometry, detector configuration, accelerating voltage, probe-current measurement method, acquisition settings, and—so far as practicable—feature size and surrounding geometry.
- Separate high-vacuum and VP calibrations are the safest protocol.

Transfer is defensible only if the VP effects are demonstrated to be negligible for the particular lines and geometry, or if independently validated corrections model electron transmission/skirt excitation, gas fluorescence, charging, and line-specific gas absorption. Even then, heterogeneous specimens smaller than the skirt remain intrinsically problematic because their unwanted contribution depends on the unknown local surroundings rather than on a universal instrumental factor.

Thus, the practical rule is: **measure standards and unknowns under matched conditions. Vacuum mode is part of the analytical condition, not an interchangeable sample-handling choice.**

References

1. (danilatos2001electronbeamcurrent pages 1-2): Gerasimos D. Danilatos, Matthew R. Phillips, and John V. Nailon. Electron beam current loss at the high-vacuum– high-pressure boundary in the environmental scanning electron microscope. Sep 2001. URL: https://doi.org/10.1007/s10005-001-0008-0, doi:10.1007/s10005-001-0008-0. This article has 30 citations and is from a peer-reviewed journal.

2. (danilatos2001electronbeamcurrent pages 2-4): Gerasimos D. Danilatos, Matthew R. Phillips, and John V. Nailon. Electron beam current loss at the high-vacuum– high-pressure boundary in the environmental scanning electron microscope. Sep 2001. URL: https://doi.org/10.1007/s10005-001-0008-0, doi:10.1007/s10005-001-0008-0. This article has 30 citations and is from a peer-reviewed journal.

3. (danilatos2001electronbeamcurrent pages 4-6): Gerasimos D. Danilatos, Matthew R. Phillips, and John V. Nailon. Electron beam current loss at the high-vacuum– high-pressure boundary in the environmental scanning electron microscope. Sep 2001. URL: https://doi.org/10.1007/s10005-001-0008-0, doi:10.1007/s10005-001-0008-0. This article has 30 citations and is from a peer-reviewed journal.

4. (spinkaUnknownyearx–raymicroanalysisin pages 1-4): J Špinka and J Jirák. X–ray microanalysis in esem. Unknown journal, Unknown year.

5. (khouchaf2012gaseousscanningelectron pages 5-10): Lahcen Khouchaf. Gaseous scanning electron microscope (gsem): applications and improvement. ArXiv, Mar 2012. URL: https://doi.org/10.5772/34930, doi:10.5772/34930. This article has 6 citations.

6. (kugler2013quantitativesemedxanalysis pages 1-2): V Kugler, M Spring, and J Hudson. Quantitative sem-edx analysis of smalt pigment under variable pressure conditions. Unknown journal, 2013.

7. (staniewicz2012transmissionmodeimagingin pages 43-48): Transmission-mode imaging in the environmental scanning electron microscope (ESEM) This article has 1 citations.

---

## q5-dtsa2-map-standard-snr

**Task ID:** `975a2688-dbc1-4013-8ece-fbf8569bcae7`  |  **Status:** success

**Query:** In NIST DTSA-II, creating a quantification standard from a measured EDS spectrum requires adequate counting statistics. Why would a spectrum extracted or summed from an EDS spectrum-image (X-ray map) of an AlSi10Mg alloy fail signal-to-noise or precision checks even for major elements like Al and Si? What total counts or dose are recommended for standard spectra, and is the recommended practice to acquire several long point/raster spectra (e.g. four 60-second acquisitions), check for outliers, and sum them?

Question: In NIST DTSA-II, creating a quantification standard from a measured EDS spectrum requires adequate counting statistics. Why would a spectrum extracted or summed from an EDS spectrum-image (X-ray map) of an AlSi10Mg alloy fail signal-to-noise or precision checks even for major elements like Al and Si? What total counts or dose are recommended for standard spectra, and is the recommended practice to acquire several long point/raster spectra (e.g. four 60-second acquisitions), check for outliers, and sum them?

## Conclusion

Yes. A spectrum summed or extracted from an AlSi10Mg spectrum-image can fail DTSA-II quality checks even though Al and Si are major constituents, because **major concentration is not equivalent to adequate counting statistics or a valid standard measurement**. The relevant quantities are the recorded counts—especially net characteristic counts above continuum—in a spectrum acquired with known dose, stable conditions, and representative geometry.

### Why a map-derived spectrum can fail

1. **Spectrum-images are commonly dose-starved.** Mapping divides the available dose among many pixels with short dwell times. A NIST example contained only about **10–100 integrated counts per pixel**, enough for fast visualization of abundant elements but severely limiting gray-level and spectral statistics. An extracted region may therefore still contain too few total or net peak counts for reliable background subtraction and peak fitting. Summing does not manufacture information; Poisson relative uncertainty scales approximately as \(1/\sqrt{N}\). (newbury2019electronexcitedxraymicroanalysis pages 20-22)

2. **The continuum and fitting uncertainty still matter.** DTSA-II fits measured peak shapes against the characteristic signal plus bremsstrahlung background. Even a visually prominent Al or Si peak may have inadequate *net* counts, or enough background covariance, to fail a requested precision threshold. Quantitative EDS requires statistically sufficient counts for background subtraction and composition calculation. (teng2020highresolutionxraya pages 21-27, ritchie2018exploringthelimits pages 1-4)

3. **AlSi10Mg is heterogeneous.** A map may combine an Al-rich matrix, Si-rich eutectic/particles, Mg-bearing regions, pores, oxide, contamination, edges, or relief. The sum is then an area-weighted mixture rather than a spectrum of one homogeneous standard composition. Composition-dependent matrix corrections and varying take-off geometry make indiscriminate summation particularly problematic. NIST identifies roughness, inhomogeneity, and surface contamination as common reasons nominal replicate spectra disagree beyond Poisson statistics. (teng2020highresolutionxraya pages 21-27, ritchie2022strategiesforstandardizing pages 1-3)

4. **A hyperspectral sum may carry acquisition defects.** Drift, changing illuminated phases, beam-current instability, charging, contamination growth, detector dead time, and pileup can change spectrum shape or intensity during a map. At high count rate, coincidence events can produce sum peaks and correction artifacts; reliable standards also require correct beam-current/live-time information because intensity scales with dose only while other conditions remain constant. (newbury2019electronexcitedxraymicroanalysis pages 28-29, teng2020highresolutionxraya pages 27-31)

5. **Metadata can be unsuitable after extraction/export.** NIST defines probe dose as **probe current × live time**. If an extracted map spectrum has missing, ambiguous, or incorrectly aggregated live-time/current metadata, DTSA-II cannot reliably normalize it as a measured standard. The displayed map duration or total counts over the entire cube is not necessarily the effective dose for the selected region. (ritchie2018exploringthelimits pages 1-4, ritchie2022strategiesforstandardizing pages 1-3)

Thus, the problem is not that DTSA-II “does not recognize” strong Al and Si peaks. It is that the spectrum may not support the required statistical precision, may not represent one homogeneous material, or may lack trustworthy dose and acquisition information.

## Counts and dose

NIST’s standardization paper does **not prescribe one universal total-count target, acquisition time, or current–time dose**. It emphasizes known probe dose, spectral consistency, and acquisition validity. Acquisition time alone is not transferable between instruments because recorded counts depend on current, detector solid angle and efficiency, processing time, dead time, geometry, and composition. (ritchie2022strategiesforstandardizing pages 1-3)

A useful empirical benchmark from a quantitative SEM–EDS validation study is:

- approximately **0.5 × 10⁶ total counts** could give major-element precision below 2% RSD under that system’s conditions;
- approximately **1–1.5 × 10⁶ total recorded counts** was the practical baseline;
- diminishing returns generally began beyond **1–1.5 × 10⁶**, although increasing toward **2.5 × 10⁶** continued to help some minor constituents;
- its 1.5-million-count baseline was obtained in about 35 s live time at 2.2 nA, corresponding to about **77 nA·s = 77 nC** incident charge, but this is an instrument-specific example—not a universal DTSA-II dose requirement. (andersenUnknownyearascanningelectron pages 4-6)

| Topic | Evidence-based guidance | Interpretation |
|---|---|---|
| NIST formal target | NIST does **not** prescribe one universal count total or acquisition time. It defines probe dose as **beam current × live time** and emphasizes spectral consistency and valid acquisition conditions. (ritchie2022strategiesforstandardizing pages 1-3) | Specify and preserve current, live time, detector conditions, and resulting counts rather than treating “60 s” alone as a sufficient dose specification. |
| Empirical count guidance | Instrument-specific testing found that about **0.5 million total counts** could give **<2% RSD for major elements**; **1–1.5 million** was a practical baseline, with diminishing returns above this range. Counts up to **2.5 million** still improved some minor-element results. (andersenUnknownyearascanningelectron pages 4-6) | Aim initially for roughly **1–1.5 million recorded total counts per final standard**, then validate on the actual SEM–EDS system; increase toward 2.5 million when minor constituents require it and the specimen tolerates the dose. |
| Replicate workflow | Split the intended total acquisition into multiple nominally identical spectra; compare them with the dose-independent mean reduced **χ²** metric, for which values near **1** indicate differences consistent with Poisson statistics. Check each spectrum’s **Duane–Hunt limit**, reject anomalous spectra iteratively, and sum the consistent subset. (ritchie2022strategiesforstandardizing pages 1-3) | Replicates expose contamination, roughness, inhomogeneity, charging, beam-energy errors, and other failures that a single long spectrum can conceal. |
| Four 60-second acquisitions | **Four × 60 s** is a reasonable implementation of the replicate-and-sum strategy, but it is **not a NIST-mandated recipe**; earlier NIST work suggested approximately **5–10** subdivisions as another implementation. (ritchie2022strategiesforstandardizing pages 1-3, ritchie2018exploringthelimits pages 4-5) | Use four acquisitions only if they produce adequate counts and mutually consistent spectra. Verify current and live time, acceptable dead time/pileup, homogeneous raster placement, absence of drift or contamination, and no beam-induced damage before summing. |


*Table: A compact distinction between formal NIST guidance, empirical count targets, and the recommended replicate-screen-and-sum workflow for measured EDS standards.*

## Recommended acquisition practice

The recommended NIST strategy is indeed to acquire **multiple nominally identical point or small-raster spectra**, rather than one uninterrupted long spectrum. Divide total intended time \(\tau\) among \(M\) acquisitions of approximately \(\tau/M\), compare them, reject anomalous members, and sum only the self-consistent subset. DTSA-II’s Spectrum Bundler implements this concept. NIST uses a dose-independent mean reduced-\(\chi^2\) comparison: values near unity indicate differences consistent with Poisson counting statistics; high-scoring spectra are removed iteratively. Every candidate should also pass a Duane–Hunt-limit check for beam-energy/charging problems. (ritchie2022strategiesforstandardizing pages 1-3)

Earlier NIST work suggested approximately **5–10 subdivisions**, but the principle—not a fixed replicate number—is important. (ritchie2018exploringthelimits pages 4-5)

Therefore, **four 60-s point/raster acquisitions, outlier checking, and summing are reasonable practice**, but “4 × 60 s” is not a NIST-prescribed recipe. It is appropriate only if:

- the retained sum reaches adequate recorded counts—practically, often around **1–1.5 million or more**;
- all spectra were collected at the same beam energy, geometry, detector settings, and controlled probe current;
- dead time and pileup remain acceptable;
- the raster lies wholly within a flat, homogeneous region representing the intended standard;
- no charging, drift, contamination, oxidation, or beam-induced compositional change occurs;
- individual live times/doses are correctly preserved and combined; and
- replicate spectra agree statistically before summation.

For heterogeneous AlSi10Mg, a bulk alloy spectrum is generally not an ideal element-specific measured standard unless its composition and homogeneity at the interaction-volume/raster scale are established. Pure Al, pure Si, or certified homogeneous compounds/alloys are preferable measured references; NIST authors prefer pure elements where practical and stable stoichiometric compounds when elemental standards are unsuitable. (newbury2019electronexcitedxraymicroanalysis pages 3-4)

References

1. (newbury2019electronexcitedxraymicroanalysis pages 20-22): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

2. (teng2020highresolutionxraya pages 21-27): C Teng. High resolution x-ray imaging and quantitative microanalysis in electron microscopy. Unknown journal, 2020.

3. (ritchie2018exploringthelimits pages 1-4): N W M Ritchie, D E Newbury, H Lowers, and M Mengason. Exploring the limits of eds microanalysis: rare earth element analyses. IOP Conference Series: Materials Science and Engineering, 304:012013, Aug 2018. URL: https://doi.org/10.1088/1757-899x/304/1/012013, doi:10.1088/1757-899x/304/1/012013. This article has 15 citations.

4. (ritchie2022strategiesforstandardizing pages 1-3): Nicholas W M Ritchie. Strategies for standardizing eds measurements. Aug 2022. URL: https://doi.org/10.1017/s143192762200263x, doi:10.1017/s143192762200263x. This article has 1 citations and is from a peer-reviewed journal.

5. (newbury2019electronexcitedxraymicroanalysis pages 28-29): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

6. (teng2020highresolutionxraya pages 27-31): C Teng. High resolution x-ray imaging and quantitative microanalysis in electron microscopy. Unknown journal, 2020.

7. (andersenUnknownyearascanningelectron pages 4-6): NL Andersen and H Winslow. A scanning electron microscope-energy dispersive spectrometry (sem-eds) method for the quantitative analysis of common volcanic phases. Unknown journal, Unknown year.

8. (ritchie2018exploringthelimits pages 4-5): N W M Ritchie, D E Newbury, H Lowers, and M Mengason. Exploring the limits of eds microanalysis: rare earth element analyses. IOP Conference Series: Materials Science and Engineering, 304:012013, Aug 2018. URL: https://doi.org/10.1088/1757-899x/304/1/012013, doi:10.1088/1757-899x/304/1/012013. This article has 15 citations.

9. (newbury2019electronexcitedxraymicroanalysis pages 3-4): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

---

## q6-matrix-matched-trace-mg

**Task ID:** `21ff2174-1cd3-4116-88b5-41fa5c2b8ae3`  |  **Status:** success

**Query:** For quantifying a minor element at 0.2-0.5 wt% (e.g. Mg in an Al-10Si-0.4Mg alloy, AlSi10Mg) by SEM-EDS, is a matrix-matched standard whose bulk composition was certified by ICP-MS preferable to pure-element standards? How large are matrix (ZAF) correction and standardless-quantification errors at such concentrations, and what accuracy and detection limits can standards-based EDS achieve for minor/trace elements?

Question: For quantifying a minor element at 0.2-0.5 wt% (e.g. Mg in an Al-10Si-0.4Mg alloy, AlSi10Mg) by SEM-EDS, is a matrix-matched standard whose bulk composition was certified by ICP-MS preferable to pure-element standards? How large are matrix (ZAF) correction and standardless-quantification errors at such concentrations, and what accuracy and detection limits can standards-based EDS achieve for minor/trace elements?

# Quantifying 0.2–0.5 wt% Mg by SEM–EDS

## Bottom line

**Yes—provided it is homogeneous on the SEM interaction-volume scale, a well-characterized Al–Si–Mg matrix-matched standard is preferable for quantifying approximately 0.2–0.5 wt% Mg in AlSi10Mg.** Its advantage is not specifically that ICP-MS was used, but that it combines a traceable assigned Mg concentration with a matrix sufficiently similar to the unknown that the unknown/standard matrix-correction ratio approaches unity. Matrix matching therefore suppresses uncertainty from backscattering/stopping power, Mg Kα absorption, and secondary fluorescence. A perfectly composition-matched standard has a correction ratio of 1.000; near matching allows uncertain physical parameters to cancel substantially. (ritchie2018exploringthelimits pages 4-5, donovan2014electronprobemicroanalysis pages 23-26)

However, **bulk ICP-MS certification alone is insufficient**. ICP-MS establishes the bulk mean after dissolution, whereas SEM–EDS samples a micrometre-scale volume. An AlSi10Mg reference may contain α-Al, Si-rich regions, Mg-bearing precipitates, segregation, or porosity. It is suitable as a direct calibrant only if Mg and the effective matrix are homogeneous at the chosen interaction volume, or if enough large-area/random measurements reproduce the certified bulk mean. Otherwise, use measured pure-element or simple-compound standards for primary k-ratios and treat the ICP-MS-certified alloy as an independent quality-control material.

| Approach or performance aspect | Quantitative evidence | Interpretation for Mg in AlSi10Mg |
|---|---|---|
| Matrix-matched, experimentally measured standard | For an exactly composition-matched standard, the unknown-to-standard matrix-correction ratio is 1.000; closely matched matrices keep it near unity. | Preferred when the certified value applies to the analyzed microscale volume. It minimizes dependence on absorption and atomic-number corrections. ICP-MS certifies bulk composition but does not prove micrometre-scale homogeneity. |
| Pure-element measured standards with ZAF or φ(ρz) correction | Experimental pure-element standards produced relative errors below 1% for major elements in a favorable alloy test; differences of 3–7% versus wet chemistry remained partly because of matrix corrections. These are general results, not AlSi10Mg-specific. | A rigorous and often excellent alternative. For Mg Kα in Al–Si, accuracy depends more strongly on the correction model, detector calibration, surface condition, and geometry than it does with a matrix-matched standard. |
| Vendor standardless quantification | Historical testing found that 95% of results were within approximately ±25% relative error. Performance varies with vendor, software version, energy calibration, and detector-efficiency model. This is a general literature result. | At 0.40 wt% Mg, ±25% relative equals approximately ±0.10 wt% absolute. It is useful for screening but not reliably for distinguishing 0.35 from 0.45 wt%. |
| Practical standards-based detection limit at about 1.5 million counts | At 15 kV and approximately 3 nA, reported 3σ limits were 0.04–0.08 wt% for lines at or below 3.69 keV and 0.09–0.19 wt% for higher-energy lines. This was a general silicate and oxide study. | Mg Kα at 1.25 keV belongs to the favorable low-energy group. Mg at 0.2–0.5 wt% should be detectable, although quantification uncertainty may remain much larger than the detection limit. |
| High-count standards-based detection limit | Without severe overlap, reported 3σ limits were 0.02–0.05 wt% with counting times below 500 s. In a 26.6-million-count glass spectrum, 0.097 wt% Mg had a critical detection limit of 0.019 wt%. These are general glass results. | Mg below 0.1 wt% can be detected under optimized conditions. Detector window, matrix, contamination, oxidation, and background fitting must be validated for AlSi10Mg. |
| Expected accuracy and precision near 0.2–0.5 wt% | In a standardized SEM-EDS method, relative error generally increased from about 5% at 1 wt% toward 30% at 0.1 wt%; RSD was about 30% at 0.15–0.2 wt% and improved with concentration. These are general mineral and glass results. | A reasonable routine expectation after validation is about 10–30% relative uncertainty near 0.2 wt% and potentially 5–15% near 0.4–0.5 wt%, not an automatic guarantee. At 0.40 wt%, that is approximately ±0.02–0.12 wt% absolute. |
| Matrix-correction magnitude versus correction uncertainty | ZAF corrections can be appreciable, but their magnitude is composition- and voltage-specific. In one general example, an approximately 20% difference in a Mg Kα mass-absorption coefficient changed calculated concentration by only about 1%. | There is no universal Mg ZAF error. Calculate the actual correction ratio for the chosen standards and conditions, then validate it with an independent Al–Si–Mg reference material. |


*Table: Comparison of calibration approaches and realistic performance near 0.2–0.5 wt% Mg. Values are general literature benchmarks unless explicitly interpreted for AlSi10Mg.*

## What “matrix correction” and “matrix-correction error” mean

Standards-based analysis measures a k-ratio and applies a ZAF or φ(ρz) correction for atomic-number effects, X-ray absorption, and fluorescence. The **size of that correction is not itself the error**. Even a sizable correction can be accurate; error arises from uncertain correction parameters, inappropriate geometry, detector response, or a nonrepresentative standard. EDS corrections also combine all transitions fitted within a peak family, which can matter near absorption edges. (ritchie2018exploringthelimits pages 4-5, donovan2014electronprobemicroanalysis pages 20-23)

There is therefore no defensible universal statement such as “the Mg ZAF correction in AlSi10Mg is 10%.” It depends on beam voltage, take-off angle, line family, compositions, and correction implementation. The correct procedure is to export the Mg k-ratio and calculated correction factor for the actual method and validate the result against an independent Al–Si–Mg material.

As an illustration of scale—not an AlSi10Mg-specific result—an approximately 20% discrepancy between tabulated Mg Kα mass-absorption coefficients produced only about a 1% effect on calculated concentration in one EPMA example. This demonstrates why an uncertain physical coefficient cannot be equated directly with the concentration error. (donovan2014electronprobemicroanalysis pages 20-23)

Experimental pure-element standards can nevertheless perform very well. In a favorable Fe–Cr–Ni alloy test, experimental standards reduced relative errors below 1% against NIST EDS values, although discrepancies of 3–7% remained relative to wet chemistry and were attributed partly to matrix correction. Low-energy/light-element analyses were substantially less robust in a chemically mismatched matrix. (tong2026measurementuncertaintiesof pages 21-24)

## Standardless error at 0.2–0.5 wt%

Historical testing of standardless EDS against known materials found that 95% of results occupied a broad **±25% relative-deviation range**. Standardless results also normally require normalization to 100% because electron dose is not measured; normalization can conceal missing elements and systematic intensity errors. Vendor algorithms and detector-efficiency calibrations vary and are often incompletely documented. (newbury2019electronexcitedxraymicroanalysis pages 18-20)

Applied to 0.40 wt% Mg, ±25% relative corresponds to approximately **±0.10 wt% absolute**. Thus, standardless EDS may adequately establish “Mg is around 0.4 wt%,” but it should not be assumed capable of reliably distinguishing 0.35 from 0.45 wt% without local validation. This is a historical general-performance envelope, not a guaranteed error for every current system.

A recent standardized SEM–EDS study found that minor-element relative error generally increased from roughly 5% toward 30% as concentration decreased from 1 to 0.1 wt%; precision similarly deteriorated from about 3–5% RSD at 0.7–1 wt% to about 30% RSD at 0.15–0.2 wt%. Nearly all 0.1–1 wt% glass measurements were within 30% relative error. (andersenUnknownyearascanningelectron pages 10-12, andersenUnknownyearascanningelectron pages 12-15)

Accordingly, realistic routine targets after method validation are approximately:

- **At 0.4–0.5 wt% Mg:** often about 5–15% relative, or roughly ±0.02–0.08 wt% absolute.
- **At 0.2 wt% Mg:** often about 10–30% relative, or roughly ±0.02–0.06 wt% absolute.
- **Best-case high-count, well-matched work:** potentially a few percent relative, but this must be demonstrated with replicate standards and independent controls rather than assumed.

These ranges are practical inferences from concentration-dependent data, not an AlSi10Mg-specific certified uncertainty budget.

## Detection limits and standards-based capability

For peaks without serious interference, modern standards-based EDS has achieved **0.02–0.05 wt% 3σ detection limits** with counting times below 500 s. In a 26.6-million-count NIST glass spectrum, Mg at 0.097 wt% had a critical detection limit of 0.019 wt%. (newbury2019electronexcitedxraymicroanalysis pages 13-15, newbury2019electronexcitedxraymicroanalysis pages 18-20)

Under more routine conditions—15 kV, approximately 3 nA, and 1.5 million total counts—a recent study obtained detection limits of **0.04–0.08 wt% for lines at or below 3.69 keV** and 0.09–0.19 wt% for higher-energy lines. Mg Kα at approximately 1.25 keV belongs to the lower-energy category, although its actual limit in Al–Si must be measured. Increasing counts improved detection limits, but diminishing precision gains appeared above about 1–1.5 million total spectrum counts in that particular setup. (andersenUnknownyearascanningelectron pages 12-15, andersenUnknownyearascanningelectron pages 15-17)

Thus 0.2–0.5 wt% Mg is normally **well above the EDS detection limit**. Detection is not the primary problem; accurate background subtraction, calibration, matrix correction, and representative sampling are. Detection limit also should not be confused with quantification limit: a 3σ detection may be statistically real while still having large relative uncertainty.

State-of-the-art EDS can accurately analyze the upper trace interval of 0.1–1 wt%, while WDS retains an advantage at the lowest concentrations because its spectral resolution gives a better peak-to-background ratio. (ritchie2018exploringthelimits pages 1-4)

## Recommended AlSi10Mg protocol

1. **Qualify the alloy standard.** Confirm its ICP-MS value and uncertainty, but also assess micrometre-scale Mg homogeneity by many points/rasters across multiple fields. Examine whether individual interaction volumes intersect Si particles or Mg-rich precipitates.
2. **Prefer co-mounting.** Polish unknown and standard together, or reproduce geometry, take-off angle, coating, working distance, beam voltage, current, and detector settings exactly. Surface roughness, oxide films, and contamination particularly affect low-energy Mg Kα photons. Conventional standards-based analyses generally show sensible raw totals of about 98–102%; inspect rather than automatically normalize anomalous totals. (newbury2019electronexcitedxraymicroanalysis pages 3-4, tong2026measurementuncertaintiesof pages 8-11)
3. **Use true measured k-ratios.** Do not call a vendor’s remote factory library “standards-based” merely because standards generated that library. Measure the standard locally at the same beam energy and geometry.
4. **Retain pure/simple standards as a cross-check.** A strong design is local pure Al, Si, and Mg or suitable stable compounds for calibration, plus the ICP-MS-certified AlSi10Mg alloy as a secondary check. If both routes agree within the uncertainty target, confidence is substantially increased.
5. **Collect high-count replicate spectra.** Acquire approximately 5–10 measurements on each standard and multiple unknown fields; this identifies outliers and tests standard homogeneity. Counting statistics alone predict approximately 3.1%, 1%, 0.31%, and 0.1% precision for 10³, 10⁴, 10⁵, and 10⁶ net counts, respectively, but Mg net counts—not total spectrum counts—control Mg precision. (ritchie2018exploringthelimits pages 4-5, donovan2014electronprobemicroanalysis pages 20-23)
6. **Measure an empirical blank and LOD.** Use an Al–10Si material with negligible Mg, if available, and calculate the 3σ critical detection limit from the background beneath Mg Kα. Do not rely on a generic software LOD.
7. **Report uncertainty honestly.** Include standard-value uncertainty, replicate precision, between-field heterogeneity, blank/background uncertainty, correction-model validation, and beam-current stability. Report both unnormalized and normalized results and the raw total.
8. **Escalate when necessary.** If the required decision is tighter than approximately ±0.02–0.05 wt% Mg, or if microsegregation and peak/background limitations dominate, use EPMA-WDS or bulk ICP-OES/ICP-MS for the bulk alloy. SEM–EDS then remains valuable for spatial distributions rather than as the sole bulk-composition method.

## Conclusion

A demonstrably homogeneous, ICP-MS-value-assigned Al–Si–Mg standard is the preferred calibrant for 0.2–0.5 wt% Mg because matrix matching makes the correction ratio close to one. But **microhomogeneity and commutability are more important than the words “ICP-MS certified.”** Pure-element standards with validated ZAF/φ(ρz) correction remain rigorous and may be safer if the alloy reference is segregated. At 0.4 wt% Mg, unvalidated standardless analysis can plausibly incur errors near 0.1 wt% absolute, whereas optimized standards-based EDS should detect Mg readily and can often attain several-to-tens-of-percent relative accuracy, with approximately 0.02–0.08 wt% practical detection limits depending strongly on counts, matrix, and instrumentation.

References

1. (ritchie2018exploringthelimits pages 4-5): N W M Ritchie, D E Newbury, H Lowers, and M Mengason. Exploring the limits of eds microanalysis: rare earth element analyses. IOP Conference Series: Materials Science and Engineering, 304:012013, Aug 2018. URL: https://doi.org/10.1088/1757-899x/304/1/012013, doi:10.1088/1757-899x/304/1/012013. This article has 15 citations.

2. (donovan2014electronprobemicroanalysis pages 23-26): J. Donovan, J. Goldstein, D. Newbury, P. Echlin, D. Joy, C. Fiori, and E. Lifshin. Electron probe microanalysis ( epma ). The IUPAC Compendium of Chemical Terminology, Feb 2014. URL: https://doi.org/10.1351/goldbook.e02006, doi:10.1351/goldbook.e02006. This article has 1 citations.

3. (donovan2014electronprobemicroanalysis pages 20-23): J. Donovan, J. Goldstein, D. Newbury, P. Echlin, D. Joy, C. Fiori, and E. Lifshin. Electron probe microanalysis ( epma ). The IUPAC Compendium of Chemical Terminology, Feb 2014. URL: https://doi.org/10.1351/goldbook.e02006, doi:10.1351/goldbook.e02006. This article has 1 citations.

4. (tong2026measurementuncertaintiesof pages 21-24): V. Tong and K. Mingard. Measurement uncertainties of energy dispersive X-ray spectroscopy in the scanning electron microscope (SEM-EDX/EDS). National Physical Laboratory, Mar 2026. URL: https://doi.org/10.47120/npl.mat135, doi:10.47120/npl.mat135.

5. (newbury2019electronexcitedxraymicroanalysis pages 18-20): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

6. (andersenUnknownyearascanningelectron pages 10-12): NL Andersen and H Winslow. A scanning electron microscope-energy dispersive spectrometry (sem-eds) method for the quantitative analysis of common volcanic phases. Unknown journal, Unknown year.

7. (andersenUnknownyearascanningelectron pages 12-15): NL Andersen and H Winslow. A scanning electron microscope-energy dispersive spectrometry (sem-eds) method for the quantitative analysis of common volcanic phases. Unknown journal, Unknown year.

8. (newbury2019electronexcitedxraymicroanalysis pages 13-15): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

9. (andersenUnknownyearascanningelectron pages 15-17): NL Andersen and H Winslow. A scanning electron microscope-energy dispersive spectrometry (sem-eds) method for the quantitative analysis of common volcanic phases. Unknown journal, Unknown year.

10. (ritchie2018exploringthelimits pages 1-4): N W M Ritchie, D E Newbury, H Lowers, and M Mengason. Exploring the limits of eds microanalysis: rare earth element analyses. IOP Conference Series: Materials Science and Engineering, 304:012013, Aug 2018. URL: https://doi.org/10.1088/1757-899x/304/1/012013, doi:10.1088/1757-899x/304/1/012013. This article has 15 citations.

11. (newbury2019electronexcitedxraymicroanalysis pages 3-4): Dale E. Newbury and Nicholas W.M. Ritchie. Electron-excited x-ray microanalysis by energy dispersive spectrometry at 50: analytical accuracy, precision, trace sensitivity, and quantitative compositional mapping. Microscopy and Microanalysis, 25:1075-1105, Oct 2019. URL: https://doi.org/10.1017/s143192761901482x, doi:10.1017/s143192761901482x. This article has 75 citations and is from a peer-reviewed journal.

12. (tong2026measurementuncertaintiesof pages 8-11): V. Tong and K. Mingard. Measurement uncertainties of energy dispersive X-ray spectroscopy in the scanning electron microscope (SEM-EDX/EDS). National Physical Laboratory, Mar 2026. URL: https://doi.org/10.47120/npl.mat135, doi:10.47120/npl.mat135.

---
