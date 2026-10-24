Question: What are the open-source, Python-native software packages for electron backscatter diffraction (EBSD) post-processing that serve as alternatives to the MATLAB-based MTEX toolbox? Focus on capabilities for grain reconstruction/segmentation from orientation maps, crystallographic texture analysis (ODF, pole figures, inverse pole figures), and misorientation-derived metrics such as kernel average misorientation (KAM) and geometrically necessary dislocation (GND) density. Discuss packages such as kikuchipy, orix, DefDAP, DREAM.3D/DREAM3D-NX (simplnx), pyxem, and any others, including their maturity, peer-reviewed references, and how their grain-reconstruction and texture-analysis capabilities compare with MTEX. Context: an automated Python pipeline (indexing via kikuchipy/PyEBSDIndex on additively manufactured AlSi10Mg) that needs the downstream grain-characterization stage to run without MATLAB.

# Open-source Python options for EBSD post-processing

## Executive conclusion

There is currently **no single Python-native package that reproduces the full integrated scope and maturity of MTEX**. The most credible MATLAB-free solution is a composed stack:

1. **kikuchipy + PyEBSDIndex** for pattern processing and indexing;
2. **DREAM3D-NX through `simplnx`** for reproducible grain segmentation, cleanup, grain statistics, and especially 3D-capable workflows;
3. **orix** as the crystallographic orientation, symmetry, misorientation, IPF, and pole-figure layer;
4. optionally **DefDAP** for convenient 2D grain/deformation-map analysis;
5. a separately tested module for **KAM**, and especially for **GND-density inversion**.

For the proposed automated AlSi10Mg pipeline, DREAM3D-NX/`simplnx` is the strongest grain-characterization backend, while orix is the best Python-native crystallographic foundation. kikuchipy itself is not a downstream replacement for MTEX, and pyxem is primarily a diffraction-microscopy/4D-STEM package rather than a conventional SEM-EBSD grain-analysis suite.

| Package / ecosystem | Python-native status | Grain reconstruction / segmentation | Texture ODF / PF / IPF | KAM / GND | Maturity / reference status | Recommended role |
|---|---|---|---|---|---|---|
| MTEX | No; MATLAB-based | **Strong** for symmetry-aware 2D grain detection/reconstruction; advanced specialized workflows documented | **Strong**; benchmark for ODF, pole figures, IPF, texture components (folwarczny2026accurategrainboundary pages 5-9, savage2021anautomatedprocedure pages 1-2, savage2021anautomatedprocedure pages 3-4) | **Strong** in the MTEX ecosystem; widely treated as benchmark | Very mature, heavily cited benchmark; peer-reviewed advanced EBSD workflows documented (savage2021anautomatedprocedure pages 1-2, savage2021anautomatedprocedure pages 3-4) | Functional benchmark and validation target, but not MATLAB-free |
| kikuchipy | Yes | **Absent / not core** for downstream grain reconstruction; primarily EBSD pattern processing/indexing support | **Partial / custom** via interoperability, not a full texture-analysis suite | **Absent / not core** | Open-source Python EBSD toolbox with literature record, but not a complete post-processing replacement in the retrieved evidence | Upstream pattern handling, preprocessing, indexing, data I/O; pair with orix and/or DREAM3D-NX |
| orix | Yes | **Partial / custom**; orientation objects and misorientation logic support custom grain segmentation, but not MTEX-level turnkey reconstruction | **Strong / near-benchmark for orientation visualization**; IPF/PF native, ODF possible but typically less turnkey than MTEX | **Partial / custom**; KAM-like metrics and curvature workflows need user implementation/validation | Peer-reviewed library record available; positioned as crystallographic orientation library rather than full EBSD suite | Core Python orientation engine for custom EBSD post-processing and visualization |
| DefDAP | Yes | **Partial**; useful 2D deformation/EBSD map grain analysis, but narrower than MTEX | **Partial**; some crystallographic plotting/analysis, not a full MTEX texture environment | **Partial**; deformation-oriented metrics are a strength, GND generally custom/limited | Open-source Python project with software-release citation; maturity moderate, community smaller than MTEX/DREAM3D | Good lightweight Python choice for 2D grain/deformation analysis after indexing |
| DREAM3D-NX / simplnx | Yes (Python API around DREAM3D-NX) | **Strong**; mature pipeline-based segmentation/reconstruction, especially for 2D/3D EBSD and batch automation (polonsky2019threedimensionalanalysisand pages 1-2, polonsky2019threedimensionalanalysisand pages 13-14, polonsky2019threedimensionalanalysisand pages 2-5, yi2025rapidgrainsegmentation pages 4-7, stanek2020comparisonofsegmentation pages 1-2) | **Partial**; some crystallographic statistics, but not as texture-centric or interactive as MTEX (yi2025rapidgrainsegmentation pages 4-7) | **Partial / custom**; not typically the first choice for KAM/GND-centric analysis | Mature EBSD/microstructure pipeline ecosystem with peer-reviewed reconstruction studies (polonsky2019threedimensionalanalysisand pages 1-2, polonsky2019threedimensionalanalysisand pages 13-14, polonsky2019threedimensionalanalysisand pages 2-5) | Best Python-accessible option for robust automated grain segmentation/statistics in a MATLAB-free pipeline |
| pyxem | Yes | **Absent / not core for SEM-EBSD**; focused on diffraction microscopy in TEM/4D-STEM, not a direct MTEX replacement | **Partial** for orientation mapping/visualization in diffraction-microscopy contexts | **Absent / not core** | Mature open-source microscopy library, but its center of gravity is 4D-STEM/SPED rather than conventional SEM-EBSD post-processing | Use only if your workflow spans diffraction microscopy; not recommended as primary EBSD grain-texture backend |
| PyMicro | Yes | **Partial / custom**; useful microstructure data structures and crystallography, but less turnkey for EBSD grain reconstruction | **Partial / custom** | **Partial / custom** | Useful research software ecosystem, but less established as a mainstream EBSD post-processing stack in the retrieved evidence | Supporting library for custom workflows, data models, simulation coupling |
| OpenXY / research scripts / pyEBSD-style code | Yes, but heterogeneous | **Partial / custom** to **strong in isolated tasks**; highly variable and often method-specific | **Partial / custom** | **Partial / custom**, including possible GND research implementations | Lowest standardization; often lacks broad peer-reviewed software validation or stable APIs | Fill specific gaps such as KAM/GND or custom segmentation, but validate carefully against MTEX/DREAM3D outputs |
| Practical no-MATLAB stack for AM AlSi10Mg | Yes | **Strong overall** if composed as: kikuchipy/PyEBSDIndex + DREAM3D-NX for segmentation + orix/DefDAP for orientation/statistics | **Partial-to-strong overall**; strongest with orix plus custom ODF tooling | **Partial / custom overall**; KAM feasible, GND should be a separately validated module | Most realistic MATLAB-free path based on current open-source ecosystem and evidence balance (polonsky2019threedimensionalanalysisand pages 1-2, polonsky2019threedimensionalanalysisand pages 13-14, polonsky2019threedimensionalanalysisand pages 2-5) | Recommended integrated pipeline rather than searching for a single Python package that fully replaces MTEX |


*Table: This table compares major open-source Python-native or Python-accessible EBSD post-processing options against MTEX for grain reconstruction, texture analysis, and misorientation-derived metrics. It is designed to help choose a MATLAB-free downstream pipeline for automated EBSD workflows.*

## The MTEX benchmark

MTEX combines, in one environment, symmetry-aware EBSD import and manipulation, grain reconstruction, grain and boundary objects, texture estimation and plotting, misorientation statistics, KAM/GROD-type measures, and curvature/dislocation-density workflows. Its texture functionality includes ODF estimation, pole and inverse-pole figures, texture components, fibres, and quantitative texture measures. Published applications use MTEX for IPF maps, ODF-derived pole figures, grain-size and grain-shape statistics, and grain-boundary analysis. (folwarczny2026accurategrainboundary pages 5-9)

MTEX also supports sophisticated extensions beyond simple threshold segmentation. A peer-reviewed workflow built on MTEX and MATLAB graph tools reconstructed deformation-twin hierarchies, grouped deformed fragments into parent families, treated missing relationships, and identified third-generation twins in heavily twinned α-Ti. (savage2021anautomatedprocedure pages 1-2) This illustrates the principal gap in Python: individual Python libraries provide many underlying operations, but MTEX supplies a more coherent grain/boundary/texture abstraction and a larger collection of specialized reconstruction workflows.

MTEX is not immune to methodological choices. Strong textures and low-angle boundaries can cause under-segmentation or chains of crystallographically similar regions; one MTEX study deliberately biased reconstruction toward over-segmentation and used 1–2° tolerances for its particular material. (savage2021anautomatedprocedure pages 3-4) More generally, grain counts and geometry depend strongly on the selected threshold, connectivity, cleanup, and minimum-grain-size rules. A conventional 5° threshold is common but is not universally valid. (stanek2020comparisonofsegmentation pages 1-2)

## Package assessment

### 1. kikuchipy

**Role.** kikuchipy is the natural upstream package in the proposed workflow. It is designed around EBSD patterns: vendor-file access, lazy handling of large pattern arrays, detector and projection geometry, background correction, pattern processing, simulation-related operations, and indexing interoperability. Its data model uses the HyperSpy ecosystem and orix crystallographic objects.

**Grains and texture.** It should not be selected as the principal grain-reconstruction engine. Once indexing has produced orientation, phase, quality, and coordinate arrays, downstream segmentation and grain statistics generally require another package or custom code. Likewise, kikuchipy is not a comprehensive ODF/texture-analysis system and does not offer an MTEX-equivalent grain/boundary object model.

**KAM/GND.** Neither is a core turnkey kikuchipy capability. KAM can be calculated from its output arrays with orix/NumPy-style operations, but masking, symmetry reduction, neighborhood definition, and exclusion of high-angle boundaries remain the pipeline developer’s responsibility. GND inversion is substantially further outside its main scope.

**Maturity.** kikuchipy is a well-developed, domain-specific open-source project with a software paper titled *kikuchipy: an open-source toolbox for analysis of electron backscatter diffraction patterns*. Its maturity is strongest for pattern-space operations, not for post-indexing microstructure analysis.

### 2. orix

**Role.** orix is the most important Python-native crystallographic foundation. It supplies rotations and orientations, crystal and specimen symmetry, fundamental-zone reduction, symmetry-aware misorientation, orientation colours, inverse-pole-figure colour keys, pole-figure-style projections, and orientation clustering. Its peer-reviewed methodological reference is Johnstone et al., *Density-based clustering of crystal (mis)orientations and the orix Python library*, *Journal of Applied Crystallography* 53 (2020), 1293–1298, DOI 10.1107/S1600576720011103.

**Grain reconstruction.** orix contains the primitives needed to compare neighboring orientations and cluster orientation data, but it is not yet an MTEX-like turnkey EBSD topology package. A production grain segmenter still needs scan-grid connectivity, phase masks, confidence masks, flood-fill or graph labeling, small-region handling, and grain-property aggregation. Those steps can be implemented with NumPy, SciPy, scikit-image, xarray, and networkx, but then the laboratory owns validation and maintenance.

**Texture.** orix is strong for IPF colouring, stereographic projections, symmetry handling, and discrete orientation distributions. It is suitable for PF/IPF visualization and custom orientation-density estimation. Nevertheless, MTEX remains substantially richer and more established for quantitative ODF estimation, kernel-selection conventions, harmonic representations, fibres/components, uncertainty-aware texture workflows, and publication-ready texture analysis. An ODF reconstructed from discrete EBSD orientations is also parameter-dependent; published work notes sensitivity to ODF computation settings in MTEX itself, so Python/MTEX agreement requires matching kernels, bandwidths, symmetry, weights, and normalization. A modern EBSD texture study used pole figures to characterize weak texture and illustrates the need to retain a statistically representative orientation population. (wanni2024machinelearningenhanced pages 1-2)

**KAM/GND.** orix is a good basis for KAM because it provides symmetry-aware misorientation operations. It does not, by itself, turn KAM into a one-call validated EBSD workflow. GND requires spatial orientation gradients, reference-frame consistency, Burgers vectors/slip-system assumptions, Nye-tensor construction, and an underdetermined inversion; this remains custom research code rather than an MTEX-equivalent orix feature.

### 3. DefDAP

**Role.** DefDAP—Deformation Data Analysis in Python—is a Python package aimed at combining EBSD with deformation measurements such as high-resolution digital image correlation. Its citable software release is Atkinson et al., *DefDAP: Deformation Data Analysis in Python* (2020), DOI 10.5281/zenodo.3688097.

**Grains.** DefDAP is useful for 2D EBSD maps, grain finding and grain-level analysis, crystallographic slip/twinning interpretation, boundary overlays, and linking deformation fields to grains. For a conventional single-phase 2D Al EBSD map it may be the quickest lightweight route from an orientation map to grains and grain-wise quantities.

**Texture and misorientation metrics.** Its emphasis is local deformation and grain-scale mechanics, not comprehensive quantitative texture. It is less complete than MTEX for ODFs, texture components, and generalized boundary/reconstruction operations. KAM-like local misorientation calculations can be added or may be available through map-level operations depending on release, but GND-density inversion should not be assumed to be a complete, standardized capability without checking the exact version and validating the implementation.

**Maturity.** DefDAP has been used in peer-reviewed deformation studies, but its community, documentation breadth, and EBSD feature coverage are smaller than MTEX or DREAM.3D. It is best regarded as a focused 2D deformation-analysis package rather than a universal EBSD backend.

### 4. DREAM.3D and DREAM3D-NX/`simplnx`

**Role and architecture.** Legacy DREAM.3D is an established C++/Qt microstructure-analysis platform. DREAM3D-NX is its current-generation successor; `simplnx` provides Python bindings and pipeline construction. Thus, it is **Python-accessible and scriptable**, although not pure Python internally. This distinction is normally beneficial for large EBSD maps because segmentation and feature-statistics filters execute in compiled code.

**Grain reconstruction.** This is the strongest open-source alternative for automated grain segmentation. DREAM.3D uses pipeline filters for data import, masking, cleanup, symmetry-aware misorientation segmentation, feature identification, neighbor lists, grain morphology, crystallographic statistics, boundary meshes, and, where applicable, 3D reconstruction. Published work describes DREAM.3D as a unified data structure aggregating community-developed algorithms, with reconstruction pipelines commonly containing more than a dozen parameterized steps. (polonsky2019threedimensionalanalysisand pages 1-2)

Its `Segment Features (Misorientation)` workflow has been used to compare 2D and 3D segmentation across several misorientation thresholds. (stanek2020comparisonofsegmentation pages 2-7) Published AM/TriBeam workflows reconstructed serial EBSD slices, segmented grains using explicit misorientation tolerances, removed features below specified voxel counts, filled gaps, and automated parameter sweeps. (polonsky2019threedimensionalanalysisand pages 2-5) Cloud integration further demonstrated parallel parameter studies, provenance tracking, and grain-size comparisons between 2D and 3D AM datasets. (polonsky2019threedimensionalanalysisand pages 1-2, polonsky2019threedimensionalanalysisand pages 13-14)

**Texture.** DREAM.3D calculates crystallographic feature statistics and supports orientation-distribution data used in synthetic microstructure generation, but it is not as strong as MTEX for interactive quantitative texture analysis. PF/IPF maps and basic orientation statistics are feasible; sophisticated ODF reconstruction and texture-component analysis are better handled in orix plus custom numerical code—or validated against MTEX. Published workflows frequently use DREAM.3D for microstructure generation/reconstruction and MTEX for detailed ODF/PF analysis, reflecting this division of strengths. (folwarczny2026accurategrainboundary pages 5-9)

**KAM/GND.** DREAM3D-NX should not be selected primarily for KAM or GND. Depending on installed plugins and version, local orientation filters may cover some neighborhood measures, but these capabilities are less central and less transparent than its feature segmentation/statistics pipeline. A NumPy/orix KAM stage is easier to audit. GND remains a specialist calculation.

**Cautions.** Segmentation is not parameter-free. The same threshold can produce different 2D and 3D connectivity, especially for nonconvex grains or paths connected outside the selected plane. (stanek2020comparisonofsegmentation pages 1-2, stanek2020comparisonofsegmentation pages 2-7) Minimum feature size and cleanup can also shift the measured grain-size distribution. Consequently, pipeline JSON, threshold, neighborhood convention, phase mask, and deleted/fill operations should be retained as provenance.

### 5. pyxem

pyxem is an open-source Python ecosystem for multidimensional diffraction microscopy, built around HyperSpy and commonly used for scanning/precession electron diffraction and 4D-STEM. It is valuable for virtual diffraction imaging, diffraction-vector analysis, orientation mapping, and related TEM workflows.

It is **not a direct downstream package for conventional SEM-EBSD orientation maps**. Grain segmentation from vendor-style EBSD grids, quantitative EBSD texture analysis, KAM, and GND are not its central abstractions. Its shared ecosystem with kikuchipy/orix can be useful if the project later combines EBSD with scanning electron diffraction, but pyxem should not be the primary AlSi10Mg grain-analysis backend.

### 6. PyMicro

PyMicro provides Python classes and algorithms for crystallography, microstructure representation, grains, orientations, meshes, and links to simulation and tomography. It can import or represent EBSD-like microstructures and is useful for custom data integration, synthetic microstructures, and computational-mechanics coupling.

For this task, its limitations are that conventional EBSD segmentation, comprehensive ODF analysis, KAM, and GND are not offered with the same turnkey breadth or community validation as MTEX. It is better viewed as an extensible microstructure framework than as a drop-in EBSD analysis application.

### 7. OpenXY and other research code

OpenXY is associated mainly with high-angular-resolution EBSD cross-correlation and strain/rotation analysis. It addresses a different problem from ordinary Hough-indexed orientation-map characterization and is not a complete grain/texture package. Some Python ports and research repositories calculate lattice curvature or GND density, but their conventions, slip-system bases, regularization, and maintenance vary.

Other small packages carrying names such as `pyebsd`, custom scikit-image segmenters, or laboratory scripts can calculate IPF colours, KAM, or threshold-connected grains. They can be useful building blocks, but package names are sometimes ambiguous, releases may be unmaintained, and peer-reviewed software references are often absent. They should not be treated as equivalent to MTEX merely because they produce an IPF or KAM image.

## Recommended pipeline for AM AlSi10Mg

### Data contract after indexing

Export or retain the following arrays and metadata:

- quaternion or rotation matrix per scan point—preferably not only Euler angles;
- phase ID, indexed/unindexed mask, confidence or match score, and pattern quality;
- physical `x`, `y` coordinates and step size;
- scan shape and rectangular/hexagonal topology;
- crystal symmetry and lattice parameters for fcc Al;
- detector/sample/reference-frame conventions;
- indexing dictionary or phase-library version.

AlSi10Mg is commonly dominated in EBSD by fcc α-Al, while the fine Si network may be incompletely indexed at ordinary step sizes. Do not let unindexed Si-rich pixels automatically split Al grains: establish an explicit phase/mask and cleanup policy and report it.

### Grain stage

Use **DREAM3D-NX/`simplnx`** for the production pipeline:

1. construct the image geometry and load quaternion, phase, mask, and quality arrays;
2. remove only demonstrably unreliable points;
3. segment same-phase connected pixels with a documented disorientation threshold;
4. calculate feature centroids, equivalent diameters, areas, aspect ratios, mean orientations, neighbors, and boundary misorientations;
5. retain both the raw feature labels and any post-cleanup labels;
6. sweep plausible thresholds rather than fixing one unexamined value.

For AM AlSi10Mg, evaluate at least a low-angle-sensitive threshold and a conventional grain threshold—for example, a controlled sweep around 2–5°—because cellular/subgrain orientation gradients may be physically meaningful. This is not a recommendation to choose a universal value; published work demonstrates that changing tolerance can radically alter segmentation and that 2D and 3D results are not automatically equivalent. (polonsky2019threedimensionalanalysisand pages 2-5, stanek2020comparisonofsegmentation pages 1-2, stanek2020comparisonofsegmentation pages 2-7)

If only modest 2D maps are involved and direct Python object manipulation is more important than DREAM3D-NX pipelines, **DefDAP** is a reasonable alternative. A fully custom orix/scikit-image segmenter is defensible only if regression-tested against DREAM3D-NX or MTEX.

### Texture stage

Use **orix** for orientation conversion, symmetry reduction, IPF maps, pole figures, and discrete orientation statistics. For ODF estimation:

- weight points or grains deliberately; pixel-weighted and one-orientation-per-grain ODFs answer different questions;
- state the kernel and half-width/bandwidth;
- enforce cubic crystal symmetry and the intended specimen symmetry;
- normalize PF/ODF intensities consistently, usually in multiples of random distribution;
- validate against a known texture or a small MTEX reference dataset.

This distinction matters in AM material: pixel weighting emphasizes large columnar grains, whereas grain weighting describes the population of grains. A recent study highlights the importance of preserving the full orientation distribution when reducing EBSD orientation datasets and uses PF maps to assess texture strength. (wanni2024machinelearningenhanced pages 1-2)

### KAM

KAM is straightforward to implement but easy to define inconsistently. For each indexed point, compute the mean symmetry-reduced disorientation to valid neighbors, while specifying:

- first-, second-, or higher-order neighborhood;
- whether diagonals are included;
- maximum included disorientation, often chosen to exclude grain boundaries;
- treatment of phase boundaries, map edges, and unindexed pixels;
- degrees versus radians;
- whether the map has been denoised before calculation.

Use orix for disorientation and NumPy/SciPy for neighborhood operations. Store the number of valid neighbors along with KAM; otherwise values near pores, Si particles, and map boundaries are misleading. KAM should not be interpreted directly as dislocation density.

### GND density

GND is the least turnkey part of a MATLAB-free pipeline. A defensible calculation needs orientation gradients in physical units, lattice curvature, an explicit Nye-tensor convention, Burgers-vector/slip-system definitions, and a solution to an underdetermined inversion—commonly L1 or L2 minimization. Report whether the result is total scalar GND density, a lower bound, or slip-system-resolved density.

For conventional EBSD, noise and angular resolution strongly affect spatial derivatives. The result also scales with step size and preprocessing. Therefore:

1. preserve orientations at full precision;
2. estimate angular noise on an undeformed/reference region;
3. document derivative stencil and smoothing;
4. perform step-size or downsampling sensitivity tests;
5. benchmark synthetic rotation-gradient fields with known curvature;
6. compare a representative map against an established MTEX or HR-EBSD implementation.

No named Python package in this comparison offers a broadly validated, turnkey GND workflow matching MTEX’s integration. Treat GND as an independently versioned scientific module, not as a plotting option attached to the grain segmenter.

## Practical ranking

- **Best production grain segmentation and statistics:** DREAM3D-NX/`simplnx`.
- **Best Python crystallographic foundation and PF/IPF layer:** orix.
- **Best upstream pattern/indexing integration:** kikuchipy + PyEBSDIndex.
- **Best lightweight 2D grain/deformation package:** DefDAP.
- **Best for TEM diffraction-microscopy integration, not SEM-EBSD post-processing:** pyxem.
- **Best custom microstructure/simulation framework:** PyMicro.
- **No fully satisfactory turnkey Python winner for GND:** implement and validate separately.

Accordingly, the recommended deployable stack is **kikuchipy/PyEBSDIndex → DREAM3D-NX/`simplnx` → orix-based texture and KAM → validated custom GND module**. This removes MATLAB from routine production while retaining MTEX only as an optional one-time validation reference. DREAM.3D’s documented use on complex additively manufactured 3D EBSD datasets, including automated parameter studies and explicit misorientation segmentation, makes this architecture substantially lower-risk than building the entire downstream stage directly from NumPy/orix primitives. (polonsky2019threedimensionalanalysisand pages 1-2, polonsky2019threedimensionalanalysisand pages 13-14, polonsky2019threedimensionalanalysisand pages 2-5)

References

1. (folwarczny2026accurategrainboundary pages 5-9): Martin Folwarczny, Ao Li, Rushvi Shah, Aaron Chote, Alexandra C. Austin, Yimin Zhu, Gregory S. Rohrer, Michael A. Jackson, Souhardh Kotakadi, and Katharina Marquardt. Accurate grain boundary plane distributions for textured microstructures from stereological analysis of orthogonal two-dimensional electron backscatter diffraction orientation maps. Ultramicroscopy, 280:114262, Feb 2026. URL: https://doi.org/10.1016/j.ultramic.2025.114262, doi:10.1016/j.ultramic.2025.114262. This article has 0 citations and is from a peer-reviewed journal.

2. (savage2021anautomatedprocedure pages 1-2): Daniel J. Savage, Rodney J. McCabe, and Marko Knezevic. An automated procedure built on mtex for reconstructing deformation twin hierarchies from electron backscattered diffraction datasets of heavily twinned microstructures. Materials Characterization, 171:110808, Jan 2021. URL: https://doi.org/10.1016/j.matchar.2020.110808, doi:10.1016/j.matchar.2020.110808. This article has 20 citations and is from a peer-reviewed journal.

3. (savage2021anautomatedprocedure pages 3-4): Daniel J. Savage, Rodney J. McCabe, and Marko Knezevic. An automated procedure built on mtex for reconstructing deformation twin hierarchies from electron backscattered diffraction datasets of heavily twinned microstructures. Materials Characterization, 171:110808, Jan 2021. URL: https://doi.org/10.1016/j.matchar.2020.110808, doi:10.1016/j.matchar.2020.110808. This article has 20 citations and is from a peer-reviewed journal.

4. (polonsky2019threedimensionalanalysisand pages 1-2): Andrew T. Polonsky, Christian A. Lang, Kristian G. Kvilekval, Marat I. Latypov, McLean P. Echlin, B. S. Manjunath, and Tresa M. Pollock. Three-dimensional analysis and reconstruction of additively manufactured materials in the cloud-based bisque infrastructure. Integrating Materials and Manufacturing Innovation, 8:37-51, Mar 2019. URL: https://doi.org/10.1007/s40192-019-00126-7, doi:10.1007/s40192-019-00126-7. This article has 31 citations and is from a peer-reviewed journal.

5. (polonsky2019threedimensionalanalysisand pages 13-14): Andrew T. Polonsky, Christian A. Lang, Kristian G. Kvilekval, Marat I. Latypov, McLean P. Echlin, B. S. Manjunath, and Tresa M. Pollock. Three-dimensional analysis and reconstruction of additively manufactured materials in the cloud-based bisque infrastructure. Integrating Materials and Manufacturing Innovation, 8:37-51, Mar 2019. URL: https://doi.org/10.1007/s40192-019-00126-7, doi:10.1007/s40192-019-00126-7. This article has 31 citations and is from a peer-reviewed journal.

6. (polonsky2019threedimensionalanalysisand pages 2-5): Andrew T. Polonsky, Christian A. Lang, Kristian G. Kvilekval, Marat I. Latypov, McLean P. Echlin, B. S. Manjunath, and Tresa M. Pollock. Three-dimensional analysis and reconstruction of additively manufactured materials in the cloud-based bisque infrastructure. Integrating Materials and Manufacturing Innovation, 8:37-51, Mar 2019. URL: https://doi.org/10.1007/s40192-019-00126-7, doi:10.1007/s40192-019-00126-7. This article has 31 citations and is from a peer-reviewed journal.

7. (yi2025rapidgrainsegmentation pages 4-7): Yu-Tsen Yi, Junwon Seo, Kevin Murphy, and Anthony D. Rollett. Rapid grain segmentation of heat-treated and annealed lpbf haynes 282 using an unsupervised learning-based computer vision approach. Integrating Materials and Manufacturing Innovation, Jan 2025. URL: https://doi.org/10.1007/s40192-024-00390-2, doi:10.1007/s40192-024-00390-2. This article has 6 citations and is from a peer-reviewed journal.

8. (stanek2020comparisonofsegmentation pages 1-2): J. Stanek, J. Kopeček, P. Král, I. Karafiátová, F. Seitl, and V. Beneš. Comparison of segmentation of 2d and 3d ebsd measurements in polycrystalline materials. Metallic Materials, 58:301-319, Jan 2020. URL: https://doi.org/10.4149/km\_2020\_5\_301, doi:10.4149/km\_2020\_5\_301. This article has 4 citations.

9. (wanni2024machinelearningenhanced pages 1-2): J. Wanni, C. A. Bronkhorst, and D. J. Thoma. Machine learning enhanced analysis of ebsd data for texture representation. npj Computational Materials, 10:1-11, Jun 2024. URL: https://doi.org/10.1038/s41524-024-01324-4, doi:10.1038/s41524-024-01324-4. This article has 14 citations and is from a peer-reviewed journal.

10. (stanek2020comparisonofsegmentation pages 2-7): J. Stanek, J. Kopeček, P. Král, I. Karafiátová, F. Seitl, and V. Beneš. Comparison of segmentation of 2d and 3d ebsd measurements in polycrystalline materials. Metallic Materials, 58:301-319, Jan 2020. URL: https://doi.org/10.4149/km\_2020\_5\_301, doi:10.4149/km\_2020\_5\_301. This article has 4 citations.