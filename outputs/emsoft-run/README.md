# EMsoft + EMsoftOO: compiled and run on Linux (dynamical EBSD physics)

Issue #9 asked to *actually attempt compilation and running of EMsoft and EMsoftOO*.
Both were built from source **and run** on an Ubuntu 24.04 GitHub Actions runner
(gfortran 13.3, cmake 3.31, 4 cores, 15 GB RAM, **no GPU**), addressing the note in
issue #8 that EMsoft "never actually ran" on Linux and needs "one afternoon of build pain."

Reproduce with [`scripts/build_emsoft_linux.sh`](../../scripts/build_emsoft_linux.sh).

## What was built

| Package | Version | Result | Programs |
|---|---|---|---|
| EMsoft SDK superbuild | 6.3-dev | HDF5 1.12.2, FFTW 3.3.8, JsonFortran 4.3, CLFortran, nlopt 2.10, bcls | — |
| **EMsoft** | 5.0.x | 687 targets, 4m41s, 0 errors | 98 `EM*` |
| **EMsoftOO** | 6.0.0 | 590 targets, 0 errors | 108 `EM*` |

## Key fixes to make it build + run on a headless CPU-only Linux box

1. **No GPU → POCL CPU OpenCL runtime.** Installed `libpocl-dev`; POCL exposes the CPU
   as an OpenCL 3.0 device.
2. **Device-type patch.** Both codebases hard-code `CL_DEVICE_TYPE_GPU` in their OpenCL
   init (`CLsupport.f90` / `mod_GPUsupport.f90`), so they abort with `CL_DEVICE_NOT_FOUND`
   on a CPU-only host. Patched to `CL_DEVICE_TYPE_ALL`.
3. **EMsoftOO extra dependency:** built `bspline-fortran` (not in the v5 SDK); exposed its
   private `set_extrap_flag` (EMsoftOO calls it directly).
4. **gfortran-13 strictness:** fixed a mixed-length character array constructor in
   EMsoftOO `mod_symmetry.f90` (`'3'` → `' 3'`).

## Physics actually run (Ni, FCC, space group 225)

Full EMsoft pipeline, end to end, on the POCL CPU device:

- **`EMMCOpenCL`** — Monte Carlo electron transport, 2,000,000 incident electrons at
  20 keV / 70° tilt → **1,151,576 backscattered, yield 0.576** (physically reasonable
  for Ni), 92 s.
- **`EMEBSDmaster`** — **dynamical Bloch-wave many-beam** master pattern with Bethe
  perturbation, 11 energy bins (10–20 keV), 20,302 beam directions each, ~46–48 strong
  beams per direction, 719 s. Output: `masterSPNH` (11, 401, 401).
- EMsoftOO reproduced the identical Monte Carlo result (yield 0.576), confirming the v6
  codebase runs correctly too.

See `ni_dynamical_master_pattern.png` (the dynamical Kikuchi master pattern — cubic
symmetry, excess/deficiency band contrast, zone axes, HOLZ rings), `ni_run_metadata.json`,
and the `namelists/` used.

## Bottom line

Dynamical EBSD simulation — the "catch is the physics" — **does** run from source on
Linux. It just needs the SDK build, a CPU OpenCL runtime, and a few one-line patches.
The companion Edison literature review of the state of the art is in
[`../edison-simulation-physics/`](../edison-simulation-physics/answer.md).
