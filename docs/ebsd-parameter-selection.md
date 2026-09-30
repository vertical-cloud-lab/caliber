# How EBSD Parameters Are Decided

This note explains *why* the acquisition parameters recommended for Electron
Backscatter Diffraction (EBSD) take the values they do — the physics and
statistics that fixed the settled optima recorded in standards such as
ASTM E2627 and ISO 13067, rather than simply pointing at those standards.

Every EBSD parameter is a point on an explicit trade-off curve balancing
**pattern signal/contrast** vs. **spatial resolution** vs. **angular precision**
vs. **acquisition speed** vs. **statistical representativeness**. The underlying
physics (backscatter yield, interaction volume, `λ ∝ 1/√V`, `SNR ∝ √N`, gnomonic
projection geometry) fixes the *shape* of each curve; sampling and confidence
statistics fix *how far along* it you need to go.

> Note on provenance: the reasoning below is derived from established EBSD
> physics and metrology. It was **not** produced via Edison Scientific — that
> path is currently blocked by an empty `EDISON_PLATFORM_API_KEY` in CI. Once a
> non-empty key is provided, the same query can be re-run through the
> `LITERATURE_HIGH` (paperqa3-high) job to produce a fully citation-grounded
> version, and the trajectory artifacts committed alongside this document.
> Verify the exact numeric clauses of ASTM E2627 / ISO 13067 against current
> published editions before using them for compliance.

## 1. Specimen tilt ≈ 70°

The backscatter coefficient η rises steeply with tilt, and — more importantly —
the *fraction* of backscattered electrons that retain coherent diffraction
information (the Kikuchi signal, versus diffuse background) peaks in roughly the
60–75° range. Tilting shortens the escape depth normal to the surface, so the
emerging electrons sample a thin near-surface layer where their exit
trajectories still carry channeling/diffraction contrast. Above ~70° the pattern
contrast keeps improving marginally, but the projected beam footprint elongates
(spatial resolution becomes strongly anisotropic), geometric
foreshortening/distortion grows, and shadowing worsens. **70° is the empirical
optimum** balancing Kikuchi-band contrast against spatial resolution and
geometric distortion — that is why the standards fixed on it, not the reverse.

## 2. Accelerating voltage (typ. 10–30 kV, 20 kV default)

Two competing physics chains set this:

- **Signal / pattern sharpness:** electron wavelength `λ ∝ 1/√V`, and Kikuchi
  band width scales as `~2λ/d` (Bragg angle). Higher kV → shorter λ → thinner,
  sharper bands and higher BSE yield → better statistics and, if the detector
  can resolve the thinner bands, better angular precision.
- **Spatial resolution:** higher kV enlarges the interaction/excitation volume
  (deeper, wider), degrading resolution and blurring measurements near
  boundaries.

So 20 kV is a general-purpose compromise; you drop to ~10 kV for nanoscale
features, thin films, or beam-sensitive/low-Z materials (smaller interaction
volume), and push to 30 kV for weakly scattering light-element phases that need
more signal. Low-Z elements have low BSE yield → need higher kV/current; high-Z
phases scatter strongly → tolerate lower kV.

## 3. Beam / probe current

Pattern SNR `∝ √N` (electrons per pattern), so more current gives cleaner
patterns and shorter exposure (faster maps). The cost is probe size: for a given
column, higher current means a larger probe → worse spatial resolution (less
severe on FEG than thermionic sources). You raise current for speed/SNR on
coarse microstructures and lower it (small probe) to resolve fine grains and
boundaries.

## 4. Step size — the "≥ ~10 points per grain" rule

This comes from sampling statistics, not convention. If a grain is covered by N
measurement points, the fractional error in its reconstructed area/diameter from
pixel discretization falls roughly as `~1/√N`, and boundary/grain-count
reconstruction becomes unreliable when the smallest grains contain only a
handful of points. Choosing step ≤ (smallest grain of interest)/10 puts ≥ ~10
points across a grain, bringing pixelation error down to a few percent and
letting a grain-reconstruction algorithm (misorientation-threshold flood fill,
typ. 5°) distinguish real grains from noise. **ASTM E2627** codifies exactly this
logic (minimum points-per-grain and a misorientation threshold for defining a
grain) so that grain-size measurements are reproducible. The lower bound on step
size is physical: nothing is gained by stepping below the effective spatial
resolution (~20–50 nm for FEG at 20 kV) or below what intragranular-gradient
(GND) sensitivity requires.

## 5. Working distance, detector distance, and pattern centre

WD (~15–20 mm) is set so the tilted region of interest projects onto the phosphor
with correct geometry. Detector insertion distance trades **angular capture**
against **gnomonic magnification**: a closer detector captures a wider slice of
the diffraction sphere (more bands → more over-determined, more robust indexing)
but lower magnification per band. The **pattern centre** must be calibrated
because indexing solves orientation from band positions *relative to the PC* — a
PC error maps almost linearly into an orientation error, which is why
calibration (known-orientation standard, moving-screen, or iterative refinement)
is mandatory rather than optional.

## 6. Camera binning, exposure, gain

Detector pixel count sets the ceiling on angular resolution: band-position
precision improves with more pixels across the pattern, so orientation precision
does too — but at lower per-pixel SNR and slower readout. **Binning** (4×4, 8×8)
sums pixels for higher SNR and frame rate at the cost of angular resolution:
heavy binning for fast mapping, low/no binning for high-precision or HR-EBSD
(resolving <0.1° misorientations). Exposure/frame-averaging improves SNR as
`~√(frames)`, sharpening Hough peaks and indexing reliability; you set it to the
minimum that reliably meets your indexing-quality target (CI/MAD) at the desired
speed. Gain amplifies signal *and* noise, so it doesn't substitute for real
exposure.

## 7. Hough transform parameters

More detected bands over-determine the orientation fit → higher precision and
fewer misindexes, with diminishing returns and slower indexing (typ. 7–12
bands). Finer Hough (θ, ρ) binning improves band-position precision (→ better
angular resolution) but is noisier and slower; the butterfly-mask size is tuned
to the expected band width, which itself depends on kV and detector distance.
These are chosen to sit at the knee of the speed / indexing-success / precision
trade-off for the material.

## 8. Minimum grains / scan area for representative statistics

The counts in standards are confidence-interval arithmetic. The standard error
of the mean grain size `∝ σ/√(n_grains)`, so to bound the mean to ±X% at 95%
confidence you need `n ≥ (1.96·σ / (X·mean))²` grains — a few hundred to a few
thousand depending on size spread. Texture (ODF) representativeness is stronger
still (typically thousands of grains for a stable ODF, more for weak/random
textures). The required scan area then follows from
(grains needed) × (mean grain area), subject to the step-size constraint — which
is what ultimately sets map size and acquisition time.

## 9. CI / MAD / band-contrast thresholds for clean-up

These cutoffs were set empirically by correlating each metric against
independently confirmed correct indexing:

- **Confidence Index** (TSL) `= (V₁−V₂)/V_ideal` from the band-voting scheme;
  **CI > 0.1** is the conventional "reliable" line because, across many
  materials, >99% of points above it index correctly.
- **MAD** (mean angular deviation, Oxford) is the mean misfit between detected
  and simulated bands; **MAD < ~1°** marks a good fit.
- **Band-contrast / image-quality** thresholds separate poorly diffracting
  points (boundaries, deformed regions, unindexed phases).

Clean-up routines (neighbour-orientation correlation, grain dilation) use these
thresholds to drop/replace unreliable points — and standards require reporting
the clean-up because over-aggressive filtering biases grain-size and texture
results.

## Summary

The through-line is that every EBSD parameter sits on a physics- and
statistics-defined trade-off curve. The physics fixes the shape of the curve;
sampling and confidence statistics fix how far along it you must go. The
standards simply record the settled optima of those curves for common materials
— which is exactly the reasoning CALIBER aims to make explicit and
sample-specific when recommending baseline acquisition parameters.
