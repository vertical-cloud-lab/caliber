# Headless DTSA-II (EPQ engine) proof: programmatic standards-based EDS quantification.
# Jython 2.7 syntax. Install DTSA-II and invoke this via scripts/dtsa2_headless_setup.sh,
# or directly:
#   java -Dpython.cachedir.skip=false -Dpython.cachedir=/tmp/jython-cache \
#        -Djava.awt.headless=true -cp "<dtsa2-install-dir>/*" \
#        org.python.util.jython scripts/dtsa2_headless_demo.py [spectrum.msa]
import sys

import java.io as jio
import java.lang as jl
import java.util as ju
import gov.nist.microanalysis.EPQLibrary as epq
import gov.nist.microanalysis.EPQLibrary.Detector as epd
import gov.nist.microanalysis.EPQTools as ept

MSA_PATH = sys.argv[1] if len(sys.argv) > 1 else "scripts/synthetic_AlSi10Mg.msa"

pkg = epq.Element.Al.getClass().getPackage()
print "Java        :", jl.System.getProperty("java.version")
print "EPQ library :", pkg.getImplementationTitle(), pkg.getImplementationVersion()
print "Jython      :", sys.version.replace("\n", " ")
print "Headless    :", jl.System.getProperty("java.awt.headless")
print

# --- 1. Read an EMSA/MAS spectrum file --------------------------------------
spec = ept.EMSAFile(jio.File(MSA_PATH))
props = spec.getProperties()
print "Loaded       :", MSA_PATH
print "Channels     :", spec.getChannelCount(), "x", spec.getChannelWidth(), "eV"
print "Beam energy  :", props.getNumericWithDefault(epq.SpectrumProperties.BeamEnergy, -1.0), "keV"
print "Live time    :", props.getNumericWithDefault(epq.SpectrumProperties.LiveTime, -1.0), "s"
print "Total counts :", int(epq.SpectrumUtils.totalCounts(spec, True))
print

# --- 2. Detector and simulated standards suite ------------------------------
E0 = 20.0  # keV, matches the .msa header
det = epd.EDSDetector.createSDDDetector(2000, 10.0, 130.0)

AL, SI, MG = epq.Element.Al, epq.Element.Si, epq.Element.Mg
true_unk = epq.Composition([AL, SI, MG], [0.885, 0.105, 0.010], "AlSi10Mg-nominal")
std_mats = {AL: epq.MaterialFactory.createPureElement(AL),
            SI: epq.MaterialFactory.createPureElement(SI),
            MG: epq.MaterialFactory.createCompound("MgO")}

def simulate(comp, dose_nAs):
    # Same call sequence as simulate() in DTSA-II's bundled Lib/dtsa2/__init__.py
    sp = epq.SpectrumProperties()
    sp.setDetector(det)
    sp.setNumericProperty(epq.SpectrumProperties.BeamEnergy, E0)
    sp.setNumericProperty(epq.SpectrumProperties.ProbeCurrent, 1.0)
    sp.setNumericProperty(epq.SpectrumProperties.LiveTime, dose_nAs)
    bulk = epq.SpectrumSimulator.Basic.generateSpectrum(comp, sp, True)
    return epq.SpectrumUtils.addNoiseToSpectrum(bulk, 1.0)

stds = dict((elm, simulate(mat, 600.0)) for elm, mat in std_mats.items())
unknown = simulate(true_unk, 120.0)

# --- 3. Standards-based quantification (same engine as the DTSA-II GUI) -----
qus = epq.QuantifyUsingStandards(det, epq.ToSI.keV(E0), False, True)
for elm, mat in std_mats.items():
    qus.addStandard(elm, mat, ju.Collections.EMPTY_SET, stds[elm])

res = qus.compute(unknown)
comp = res.getComposition()
print "Standards-based quant of a simulated AlSi10Mg unknown at %.0f kV" % E0
print "(standards: pure Al, pure Si, MgO for Mg)"
print "  %-4s %10s %12s" % ("Elm", "true wt%", "quant wt%")
for elm in (AL, SI, MG):
    print "  %-4s %10.3f %12.3f" % (elm.toAbbrev(),
                                    100.0 * true_unk.weightFraction(elm, False),
                                    100.0 * comp.weightFraction(elm, False))
print "  analytical total: %.2f wt%%" % (100.0 * comp.sumWeightFraction())
if res.getWarningMessage():
    print "  warnings:", res.getWarningMessage()
print

# --- 4. Push the repo spectrum through the same pipeline ---------------------
# The .msa peaks were synthesized by hyperspy, not EPQ physics, and its absolute
# dose is arbitrary, so only the normalized ratios are meaningful here; this step
# demonstrates file-based quant plumbing, not an accuracy claim.
props.setDetector(det)
props.setNumericProperty(epq.SpectrumProperties.ProbeCurrent, 1.0)
res2 = qus.compute(spec)
comp2 = res2.getComposition()
print "Same pipeline applied to %s" % MSA_PATH
print "  %-4s %12s %16s" % ("Elm", "raw wt%", "normalized wt%")
for elm in (AL, SI, MG):
    print "  %-4s %12.3f %16.3f" % (elm.toAbbrev(),
                                    100.0 * comp2.weightFraction(elm, False),
                                    100.0 * comp2.weightFraction(elm, True))
print
print "DTSA-II headless run complete."
