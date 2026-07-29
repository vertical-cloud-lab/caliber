#!/usr/bin/env bash
# Reproducible Linux build + dynamical-physics run of EMsoft (v5) and EMsoftOO (v6).
#
# Verified 2026-07-29 on an Ubuntu 24.04 GitHub Actions runner
# (gfortran 13.3, cmake 3.31, 4 cores, 15 GB RAM, no GPU) in ~15 min wall clock.
#
# EMsoft's OpenCL kernels normally require a GPU. This runner has none, so we use
# POCL (a CPU OpenCL runtime) and patch EMsoft's device query from
# CL_DEVICE_TYPE_GPU to CL_DEVICE_TYPE_ALL so kernels run on the CPU device.
set -euo pipefail

WORK=${WORK:-/tmp/emsoft-build}
SDK=${SDK:-/opt/EMsoft_SDK}
mkdir -p "$WORK"

# 1. Dependencies (Dockerfile recipe + POCL CPU OpenCL runtime)
sudo apt-get update -qq
sudo apt-get install -y -qq \
  git cmake gfortran gcc g++ ninja-build build-essential \
  libopenblas-dev opencl-headers ocl-icd-opencl-dev libpocl-dev clinfo

# 2. Clone sources (siblings, as EMsoft requires)
cd "$WORK"
for repo in EMsoftSuperbuild EMsoft EMsoftData EMsoftOO; do
  [ -d "$repo" ] || git clone --depth 1 "https://github.com/EMsoft-org/$repo.git"
done

# 3. Build the SDK superbuild (HDF5, FFTW, Eigen, JsonFortran, CLFortran, nlopt, bcls)
sudo mkdir -p "$SDK" && sudo chown -R "$(whoami)" "$SDK"
mkdir -p EMsoftSuperbuild/Release && cd EMsoftSuperbuild/Release
cmake -DEMsoft_SDK="$SDK" -DCMAKE_BUILD_TYPE=Release ../ -G Ninja
ninja   # NOTE: HDF5 is the slow component; run to completion in the foreground

# 4. Patch OpenCL device filter GPU -> ALL so kernels run on the POCL CPU device
cd "$WORK"
sed -i '520,700 s/CL_DEVICE_TYPE_GPU/CL_DEVICE_TYPE_ALL/g' \
  EMsoft/Source/EMOpenCLLib/CLsupport.f90

# 5. Build EMsoft (v5) -> 98 EM* programs
mkdir -p EMsoftBuild/Release && cd EMsoftBuild/Release
cmake -DCMAKE_BUILD_TYPE=Release -DEMsoft_SDK="$SDK" -G Ninja ../../EMsoft
ninja
cd "$WORK"

# 6. EMsoftOO (v6) extra dependency: bspline-fortran.
#    Two upstream patches are needed against current bspline-fortran + gfortran 13:
#      (a) expose set_extrap_flag (EMsoftOO calls it directly)
#      (b) EMsoftOO mod_symmetry.f90 has a mixed-length character array constructor
git clone --depth 1 https://github.com/jacobwilliams/bspline-fortran.git || true
sed -i 's/procedure,non_overridable :: set_extrap_flag/procedure,public,non_overridable :: set_extrap_flag/' \
  bspline-fortran/src/bspline_oo_module.f90
mkdir -p bspline-fortran/build && cd bspline-fortran/build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="$SDK/bspline-fortran-Release" \
  -DBUILD_SHARED_LIBS=OFF -G Ninja ..
ninja install
cd "$WORK"

# EMsoftOO SDK cmake: reuse the generated EMsoft SDK, add bspline paths
cp "$SDK/EMsoft_SDK.cmake" "$SDK/EMsoftOO_SDK.cmake"
cat >> "$SDK/EMsoftOO_SDK.cmake" <<EOF
set(BSPLINEFORTRAN_INSTALL "$SDK/bspline-fortran-Release" CACHE PATH "")
set(BSPLINEFORTRAN_DIR "$SDK/bspline-fortran-Release/lib" CACHE PATH "")
EOF

# gfortran-13 strictness fix + OpenCL device patch for EMsoftOO
sed -i "s/' 3','32','3','32'/' 3','32',' 3','32'/" \
  EMsoftOO/Source/EMsoftOOLib/mod_symmetry.f90
sed -i '1000,1200 s/CL_DEVICE_TYPE_GPU/CL_DEVICE_TYPE_ALL/g' \
  EMsoftOO/Source/EMOpenCLLib/mod_GPUsupport.f90

mkdir -p EMsoftOOBuild/Release && cd EMsoftOOBuild/Release
cmake -DCMAKE_BUILD_TYPE=Release -DEMsoftOO_SDK="$SDK" -DBUILD_SHARED_LIBS=OFF -G Ninja ../../EMsoftOO
ninja   # -> 108 EM* programs

echo "Done. EMsoft Bin: $WORK/EMsoftBuild/Release/Bin ; EMsoftOO Bin: $WORK/EMsoftOOBuild/Release/Bin"
