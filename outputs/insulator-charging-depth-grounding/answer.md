# Electron-Beam Charging Physics of Bulk Insulators in SEM/EPMA: A Literature Review with Application to Uncoated MgO at 5 keV

---

## 1. Depth of Electron Penetration and Trapped Charge in Charging Insulators

### 1a. Implantation Depth versus Beam Energy (Electron Range Scaling)

The maximum penetration depth (range) R of primary electrons in a solid target follows a power-law dependence on beam energy E₀. Cazaux (2006) gives the widely used form:

**R(nm) = C · E₀ⁿ (keV)**

where n ≈ 1.35 for E₀ < 5 keV, with C = 115/ρ_m (ρ_m in g/cm³). Fitting (1974) proposed a similar expression with n = 1.3 and C = 90/ρ_m^0.8 (cazaux2006charginginscanning pages 2-3). The Kanaya–Okayama formula is another standard parameterization widely referenced in the literature. Most expressions converge to give R ~ 1 µm at approximately 10 keV for a material with ρ_m ~ 2.5 g/cm³ (cazaux2006charginginscanning pages 2-3). For MgO (ρ_m ≈ 3.58 g/cm³) at E₀ = 5 keV, these relations yield R on the order of ~100–200 nm.

### 1b. Depth Distribution of Trapped Charge: The Dynamic Double Layer

The peer-reviewed literature consistently describes the trapped-charge distribution in electron-irradiated bulk insulators as a **dynamic electrostatic double layer**:

- **Thin positive surface layer:** Secondary electrons (SEs) escape from a shallow surface region of approximate thickness s, comparable to the SE escape depth (variously given as ~3λ, where λ is the SE mean free path, or ~50 nm in insulators—far larger than the ~5 nm in metals due to the absence of conduction-electron scattering) (cazaux2006charginginscanning pages 3-5, rau2008mechanismsofcharging pages 7-8, rau2008mechanismsofcharging pages 2-3, rau2008mechanismsofcharging pages 1-2, cazaux2006charginginscanning pages 2-3). The escape of these SEs leaves behind uncompensated positive charge (holes).

- **Deeper negative space-charge layer:** Incident primary electrons that do not escape are transported deeper and become trapped, producing an excess negative space-charge region extending toward the end of the primary-electron range R. Rau et al. (2008) place the centroid of this negative layer at approximately 0.4R₀ (rau2008mechanismsofcharging pages 7-8). The negative layer extends from approximately s < z < R.

- **Dipolar potential profile:** Even when the integrated positive and negative charges are equal, their spatial separation creates a dipole and a nonzero, often positive, surface potential with an S-shaped depth profile (cazaux2006charginginscanning pages 3-5, cazaux2006charginginscanning pages 6-7).

This model was developed by Cazaux in a series of papers (J. Appl. Phys. 59:1418, 1986; J. Electron Spectrosc. 105:155, 1999; Scanning 26:181, 2006), described as the "dynamic double layer" by Melchinger & Hofmann (J. Appl. Phys. 78:6224, 1995), and further refined by Rau et al. (2008) (rau2008mechanismsofcharging pages 7-8, rau2008mechanismsofcharging pages 2-3, rau2008mechanismsofcharging pages 1-2). Self-consistent charge-transport simulations, such as the flight–drift model of Touzin, Goeuriot, Guerret-Piécourt, Juvé, Tréheux & Fitting (J. Appl. Phys. 99:114110, 2006), and Monte Carlo simulations by Fitting, Schreiber, and collaborators (cazaux2006charginginscanning pages 2-3), have confirmed and extended this picture by computing self-consistent charge distributions, internal fields, and SE yields in SiO₂ and Al₂O₃.

### 1c. Self-Regulation of Landing Energy toward E₂

Charging is **self-regulating**: as negative surface potential builds, it decelerates incoming primary electrons, reducing their landing energy E_L from the nominal E₀. This reduces the penetration depth and increases the SE yield δ toward unity. The system evolves toward a steady state in which the charge-balance condition δ_s + η_s = 1 is satisfied (cazaux2006charginginscanning pages 6-7, cazaux1996electronprobemicroanalysis pages 12-13). The equilibrium surface potential is approximately V_S = E₀ − E₂C (in the zero-leakage limit), where E₂C is the **second crossover energy under charging conditions**—distinct from (and generally much lower than) the uncharged pulse-measured E₂ (rau2008mechanismsofcharging pages 2-3, rau2008mechanismsofcharging pages 6-7).

Critically, the literature emphasizes that the relevant crossover energies are governed by the charged-specimen yield curves rather than the nominal uncharged curves (cazaux1996electronprobemicroanalysis pages 12-13). Rau et al. (2008) showed experimentally that E₂C ranges from 1 to 3 keV for common insulators (PMMA: ~1 keV; p-SiO₂: ~2 keV; p-Al₂O₃: ~3 keV; soda-lime glass: ~1.4 keV), whereas uncharged E₂ values are typically above 10 keV (rau2008secondcrossoverenergy pages 1-2, rau2008secondcrossoverenergy pages 2-4, rau2008secondcrossoverenergy pages 6-7, rau2008secondcrossoverenergy pages 7-9). The landing energy at steady state E_SL equals E₂C only when the leakage current I_L is negligible; with leakage, E_SL > E₂C (rau2008mechanismsofcharging pages 6-7, rau2008secondcrossoverenergy pages 6-7).

### 1d. Experimental Methods for Measuring Trapped-Charge Depth and Surface Potential

Several methods have been used to measure surface potential or trapped-charge depth in electron-irradiated insulators:

- **Electron mirror method:** A pre-charged insulator surface reflects a subsequent low-energy probe beam, forming a "mirror" image. The mirror effect threshold and image properties yield the surface potential. This is well documented by Belhaj et al. (Scanning 22:352, 2000) and Rau and colleagues (rau2008secondcrossoverenergy pages 1-2).

- **Toroidal electron spectrometer:** Rau et al. (2008) used a toroidal spectrometer to directly measure the SE peak energy shift, which gives V_S. For p-Al₂O₃ irradiated at 14 keV with 2 nA beam current, V_S reached saturation over tens of seconds (rau2008secondcrossoverenergy pages 6-7).

- **X-ray bremsstrahlung / Duane–Hunt limit:** The high-energy cutoff of the bremsstrahlung spectrum shifts by eV_S, providing an in-situ measurement of landing energy (discussed in detail in Section 4).

- **Displacement current and induced-charge method:** Jbara et al. (2004) measured charge induced on a metallic specimen holder during irradiation, enabling determination of trapped charge QT and its time evolution for both bare and ground-coated insulators (jbara2004chargeimplantationmeasurement pages 1-2).

- **Kelvin probe:** Non-contact surface-potential measurements before and after irradiation. Hodges et al. (IEEE Trans. Plasma Sci. 42:255, 2014) demonstrated in-situ surface voltage measurements of dielectrics under electron beam irradiation, observing charge dissipation to grounded substrates.

Quantitative examples from the Boughariou et al. (2005) study on MgO (100) single crystal: at 1.1 keV irradiation (low current density), maximum trapped charge Q_Tmax = 706 pC/cm², producing a positive surface potential V_Smax = 16 V; at 5 keV, Q_Tmax = 374 pC/cm², V_Smax = 8.7 V (boughariou2005effectofcurrent pages 3-5, boughariou2005effectofcurrent pages 5-7).

---

## 2. Grounding from Below: Conductive Layer Under a Thin Insulator

### 2a. Capacitive Scaling of Surface Potential with Dielectric Thickness

The literature clearly establishes that **surface potential scales with insulating film thickness** for a given trapped areal charge density when a grounded conductor is underneath. Cazaux & Lehuede (1992) explicitly noted that for a thin insulator on a conducting substrate (e.g., SiO₂ on Si), even with an internal field as high as 10⁵ V/cm, a 100 Å (10 nm) film would exhibit only a ~0.1 V surface potential drop—too small to measure by conventional means despite significant local fields (cazaux1992somephysicaldescriptions pages 4-6).

Rau et al. (2008) included sample thickness h in the denominator of the surface-potential expression, with the dielectric permittivity ε₀·ε_r appearing as a factor (ε_r(SiO₂) = 3.9), confirming capacitive scaling: V_S ∝ Q·h/(ε₀·ε_r) for a parallel-plate geometry (rau2008mechanismsofcharging pages 7-8). Cazaux (1996) similarly described the voltage drop across a thin film as ΔV ≈ F·d, where F is the internal field and d is the film thickness, showing that thinner layers produce proportionally smaller surface potentials for a given field (cazaux1996electronprobemicroanalysis pages 12-13).

### 2b. Radiation-Induced Conductivity and Charge Leakage to Substrate

When the electron beam range R approaches or exceeds the insulating film thickness, deposited charge can leak to the grounded substrate through several mechanisms:

- **Radiation-induced conductivity (RIC):** The internal electric field from the charge double layer drives radiation-induced bipolar currents that redistribute carriers between the charged region and the grounded substrate (rau2008mechanismsofcharging pages 7-8). The total current balance I₀ = I_σ + I_Q + I_L explicitly includes leakage I_L to ground.

- **Electron-beam-induced conductivity (EBIC):** Arat et al. (2019) incorporated EBIC into Monte Carlo charging simulations, finding that it smooths charge distributions and provides better agreement with experiment for insulating layers on substrates.

- **Zhang et al. (2012) simulated leakage currents** in SiO₂ thin films on grounded conductive substrates irradiated by non-penetrating focused electron beams, finding that the substrate proximity significantly affects charge evolution.

### 2c. Evidence from SEM/EPMA Practice and E-beam Lithography

- **SiO₂ on Si:** Cazaux (1996) specifically noted that thin dielectric coatings on grounded conducting substrates may show positive charging over a wide primary-energy range, because many incident electrons pass through the thin film into the substrate and are evacuated to ground (cazaux1996electronprobemicroanalysis pages 12-13). Ding et al. (2021) modeled SiO₂ films on Au substrates, showing thickness-dependent charging behavior (ding2021chargingeffectinduced pages 20-22).

- **Electron-beam lithography:** Insulating resist films (typically 0.1–1 µm PMMA, HSQ, etc.) on grounded silicon wafers are routinely exposed at keV energies without catastrophic charging. The grounded Si substrate serves as the charge drain, and the thin film thickness ensures the beam range reaches or approaches the conductor.

- **Capacitive contrast imaging:** Zhang et al. (2004) described how the effective capacitance between an irradiated surface point and a buried grounded substrate determines the local charging and SE signal, with different buried structures (conductors vs. insulators) producing different effective capacitances—this is the "static capacitance contrast" mechanism used to image buried structures through insulating overlayers (zhang2004utilizingthecharging pages 11-14).

### 2d. Failure Modes

The literature identifies several artifacts when analyzing thin insulating films on conductive substrates:

- **Substrate X-ray fluorescence:** X-rays generated in the insulating overlayer can fluoresce the buried conductive substrate, contributing unwanted characteristic lines to the spectrum. This is a standard thin-film matrix correction concern.

- **Backscattering from the substrate:** When the beam range reaches the conductive substrate, backscattered electrons from the higher-Z substrate alter the BSE coefficient and the depth distribution of X-ray generation, requiring thin-film (rather than bulk) matrix corrections.

- **Internal field-driven migration:** Even when the surface potential is small, the internal field F can be very large (up to ~10⁵ V/cm in thin films), potentially driving mobile ion migration (e.g., Na⁺ in glass) toward interfaces (cazaux1992somephysicaldescriptions pages 4-6, cazaux1996electronprobemicroanalysis pages 12-13).

- **Conductive coating on top of insulator does not eliminate internal charging:** Jbara et al. (2004) and Ding et al. (2021) emphasized that while a grounded conductive coating eliminates external beam deflection, internal electric fields beneath the coating are actually reinforced, potentially reducing ionization and X-ray generation efficiency in EPMA (jbara2004chargeimplantationmeasurement pages 1-2, ding2021chargingeffectinduced pages 34-36).

---

## 3. MgO Specifically at Low Beam Energy

### 3a. Secondary Electron Yield Parameters for MgO

MgO has exceptionally high secondary electron yields—among the highest of any oxide material—which is precisely why it has been used in plasma display panels.

**Key measured values from the literature:**

From Cazaux (2006), Table I (short-pulse measurements, attributed to Whetten & Laponsky ["W and L"]):
- **δ_max ≈ 23** (maximum SE yield)
- **E_max (E_M) ≈ 1.2 keV** (energy at maximum yield)
- **E₂° >> 3.5 keV** (second crossover energy under non-charging conditions—the actual value was not precisely determined but greatly exceeds 3.5 keV) (cazaux2006charginginscanning pages 2-3)

For comparison, other insulators in the same table: NaCl (δ_M = 14–17, E₂° >> 6 keV), KCl (δ_M = 13, E₂° >> 6 keV), Al₂O₃ (δ_M = 12, E₂° ~ 20 keV), amorphous SiO₂ (δ_M = 4, E₂° > 3 keV) (cazaux2006charginginscanning pages 2-3).

The classic measurements by Whetten & Laponsky (J. Appl. Phys. 28:515, 1957; Phys. Rev. 120:801, 1960) on cleaved MgO single crystals reported these very high yields. Johnson & McKay (Phys. Rev. 91:582, 1953) performed earlier measurements. Joy's database of electron–solid interactions includes MgO data but cautions that "all SE yield results for insulators must be treated with caution unless details of the original measurement protocol are well documented."

### 3b. MgO at 5 keV: Above or Below Unity Total Yield?

**At E₀ = 5 keV, bulk single-crystal MgO sits well ABOVE unity total yield (σ₀ > 1), meaning it charges positively—a benign situation for EDS.**

The Boughariou et al. (2005) study directly measured MgO (100) single crystal SE yield at 5 keV:
- At low current density (J = 1.2 × 10⁴ pA/cm²), the intrinsic SE yield σ₀ ≈ **2.5** at 5 keV (boughariou2005effectofcurrent pages 5-7).
- The SE yield evolves from σ₀ toward unity (σ = 1) as positive charge accumulates—a **self-regulated regime** reached after a few pC of injected dose (boughariou2005effectofcurrent pages 3-5).
- The self-regulated equilibrium produces a **positive surface potential of only ~8.7 V** with maximum trapped charge Q_Tmax = 374 pC/cm² (boughariou2005effectofcurrent pages 3-5, boughariou2005effectofcurrent pages 5-7).
- At 30 keV, by contrast, σ₀ ≈ 0.6 (below unity)—the sample charges negatively (boughariou2005effectofcurrent pages 3-5).

This is critical for the user's application: at E₀ = 5 keV, MgO is far below its E₂ crossover, so it charges positively to only a few volts—a self-limiting, benign charging regime for quantitative EDS.

### 3c. Effect of Surface Contamination, Hydroxylation, and Beam Conditioning

The SE yield of MgO is highly sensitive to surface condition:

- **Crystalline state:** Cazaux (2006) emphasized that SE escape depth values—and consequently yield curves—are "very sensitive to the crystalline state and to the temperature of the specimen" due to vacancy, impurity, and dislocation interactions (cazaux2006charginginscanning pages 2-3).

- **Water/hydroxylation:** Ritz et al. (1992) found that UPS spectra of MgO films showed a feature near −7.5 eV attributable to chemisorbed water or hydroxyl (OH⁻), which was substantially reduced after intense electron-beam irradiation at 25 µA/cm² for 15 minutes (ritz1992performanceofmgoau pages 5-6).

- **Beam conditioning:** Bagraev & Borisov (1980) reported that MgO yields were stable during prolonged electron bombardment (7 hours at 900 eV), with no detectable influence from residual gases under their vacuum conditions (bagraev1980effectofcs pages 8-9, bagraev1980effectofcs pages 4-8).

- **Current density effects:** Boughariou et al. (2005) showed that at high current densities (J₀ > 10⁶ pA/cm²), elastic diffusion between primary and secondary electrons causes the measured σ to drop transiently below 1 even at energies where σ₀ > 1, before recovering to unity—a second type of self-regulated regime controlled by negative trapped charge (boughariou2005effectofcurrent pages 3-5, boughariou2005effectofcurrent pages 5-7).

- **Contamination generally degrades yield:** The very high δ_max values (20+) are for clean, well-prepared single crystals. Contaminated, hydroxylated, or disordered surfaces exhibit lower yields, and amorphous or polycrystalline forms show substantially reduced δ_max relative to single crystals (cazaux2006charginginscanning pages 2-3).

### 3d. Published SEM/EPMA of Uncoated MgO

Cazaux et al. (J. Appl. Phys. 70:960, 1991) directly studied charging effects of MgO under electron bombardment and the non-ohmic behavior of the induced specimen current. Boughariou et al. (2005) performed their entire study on uncoated MgO (100) single crystals in a SEM, using pulsed-beam techniques to control dose precisely (boughariou2005effectofcurrent pages 1-3, boughariou2005effectofcurrent pages 3-5).

---

## 4. The Duane–Hunt Endpoint as a Charging Gauge

### 4a. Physical Basis

The Duane–Hunt limit is the maximum photon energy in the bremsstrahlung continuum, corresponding to the kinetic energy of electrons striking the specimen. For a grounded conductor at nominal beam energy E₀, the endpoint equals E₀. For a charged insulator with surface potential V_S, the landing energy shifts to E_L = E₀ + eV_S (sign convention-dependent), and the bremsstrahlung endpoint shifts accordingly (newbury2000measuresforspectral pages 1-2, jbara2004chargeimplantationmeasurement pages 4-6, cazaux1996electronprobemicroanalysis pages 13-14, cazaux1996electronprobemicroanalysis pages 12-13).

Cazaux (1996) reported an example where the endpoint was observed near 5.9 keV instead of the expected 10 keV, consistent with a ~4.1 kV retarding surface potential (cazaux1996electronprobemicroanalysis pages 12-13). Rau et al. (2008) confirmed that the Duane–Hunt limit, measured by the "shift in high-energy cutoff in the X-ray bremsstrahlung spectra," provides E_SL, the landing energy at steady state—which equals E₂C when leakage is negligible (rau2008secondcrossoverenergy pages 6-7).

### 4b. Practical Use and Recommendations

Newbury (2000) identified the Duane–Hunt bremsstrahlung endpoint as a diagnostic for charging in low-voltage SEM/EDS, recommending:
- The endpoint should be determined by **extrapolating the continuous bremsstrahlung slope to zero counts**, not by taking the highest channel containing counts (newbury2000measuresforspectral pages 1-2).
- **Time-series measurements** (sequential short spectra) should be used rather than one long acquisition, to detect dynamic charging that might leave an apparently acceptable endpoint in an integrated spectrum (newbury2000measuresforspectral pages 7-7, newbury2000measuresforspectral pages 2-3).
- Monitoring both the endpoint and relative peak heights over time provides the most reliable charging diagnostic (newbury2000measuresforspectral pages 7-7).

### 4c. Limitations

The literature identifies several important limitations:

1. **Endpoint statistics:** The high-energy tail contains few counts, making the endpoint determination statistically difficult (newbury2000measuresforspectral pages 1-2).

2. **Pulse pile-up:** Detector artifacts (including pulse pile-up) can produce counts above the physical endpoint, mimicking an above-endpoint signal and confounding the measurement (newbury2000measuresforspectral pages 1-2).

3. **Time-varying potentials:** A satisfactory static Duane–Hunt limit does not rule out dynamic charging; time-dependent potentials can vary during spectral accumulation while leaving an apparently acceptable endpoint (newbury2000measuresforspectral pages 1-2, newbury2000measuresforspectral pages 2-3).

4. **Secondary-electron backscattering:** Jbara et al. (2004) cautioned that SEs and BSEs accelerated by the charged surface can backscatter from pole pieces and return to irradiate the sample/holder, producing additional bremsstrahlung sources that contaminate the measured spectrum (jbara2004chargeimplantationmeasurement pages 4-6).

5. **Pseudo-mirror effect:** In severely charged insulators, the pseudo-mirror effect can cause anomalous contrast and erroneous V_S measurements when the DHL method is used (jbara2004chargeimplantationmeasurement pages 1-2).

### 4d. Is "Check the Endpoint + Stable Count Rate" an Accepted Protocol?

The literature supports using the Duane–Hunt endpoint as an **important diagnostic** and as part of a quality-assurance workflow, but **not as a standalone accept/reject protocol**:

- Newbury (2000) recommends it as one element of spectral quality assessment alongside time-resolved spectra and energy-window monitoring, but does not establish it as a sufficient standalone validation criterion (newbury2000measuresforspectral pages 1-2, newbury2000measuresforspectral pages 7-7).
- Cazaux (1996) notes that the method can provide the magnitude and sign of charging potential and thereby partially correct charging-related errors in quantitative EPMA, but cautions that for thin insulating coatings on grounded substrates, the potential change may be too small to detect even when internal fields cause artifacts (cazaux1996electronprobemicroanalysis pages 13-14).
- Rau et al. (2008) showed that V_S = f(E₀) behavior is well-described by eV_S = E₀ − E₂C up to about 10 keV, validating the endpoint approach in this regime, but deviations from linearity at higher energies (due to leakage currents) mean the endpoint underestimates the total charging effect (rau2008secondcrossoverenergy pages 6-7).

**In practice**, the combination of (1) verifying the Duane–Hunt endpoint matches the set beam energy (within a few eV), (2) stable count rates across replicate short acquisitions, and (3) stable peak ratios, constitutes a reasonable operational protocol—widely recommended in textbooks such as Goldstein et al. (4th ed., Springer 2018) and used by practitioners. However, it should be recognized as a **necessary but not sufficient** condition: passing the test rules out gross negative charging (kilovolt-scale), but does not exclude small positive charging (a few volts), internal field-driven migration, or time-averaged artifacts from fluctuating potentials.

---

## Summary for the User's Specific Case: Uncoated MgO at 5 keV

For a bulk single-crystal MgO wafer at E₀ = 5 keV:

- The total SE yield is approximately **σ₀ ≈ 2.5** (well above unity), so the specimen charges **positively** (boughariou2005effectofcurrent pages 3-5, boughariou2005effectofcurrent pages 5-7).
- Positive charging is self-limiting to only **~8.7 V** at low current density, because the positive potential retards SE escape until σ → 1 (boughariou2005effectofcurrent pages 5-7).
- A few-volt positive surface potential causes negligible distortion of the EDS spectrum—the electrons are accelerated slightly rather than decelerated, and the bremsstrahlung endpoint shifts up by only a few eV.
- The Duane–Hunt endpoint check should show the endpoint at or very slightly above E₀ = 5 keV; stable count rates across replicates provide additional confirmation.
- Silver/carbon paint grounding at edges, combined with MgO's favorable positive-charging behavior at this energy, should permit quantitative k-ratio SEM-EDS without a conductive top coat.

The primary risk is at higher beam energies (approaching or exceeding E₂) where negative charging by kilovolts would occur—but at 5 keV, MgO is safely in the positive-charging, self-limiting regime.