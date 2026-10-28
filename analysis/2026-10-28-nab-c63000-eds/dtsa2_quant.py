# -*- coding: utf-8 -*-
# NIST DTSA-II (Jython 2.7) script: quantify the three NAB powder spectra against simulated
# pure-element standards (DTSA-II's analytical spectrum simulator, same detector model and dose).
# Peaks are fit with DTSA-II's filter fit (k-ratios for every line family of every element),
# then the metal k-ratios go through the XPP matrix correction. C and O are fit but kept out
# of the matrix: C is the tape, O is surface oxide/contamination.
# Run:  NAB_DATA=/tmp/nab-staging/files/eds NAB_OUT=outputs ./run_dtsa2.sh dtsa2_quant.py
import os, codecs
import java.lang as jl
import java.io as jio
import gov.nist.microanalysis.EPQLibrary as epq
import gov.nist.microanalysis.EPQLibrary.Detector as epd

dataDir = os.environ["NAB_DATA"]
outDir = os.path.abspath(os.environ["NAB_OUT"])
log = codecs.open(os.path.join(outDir, "dtsa2_quant.log"), "w", "utf-8")
try:
    # EDAX Octane Plus as recorded in the .spc headers: 4096 x 5 eV, 127.9 eV at Mn Ka, elevation 35 deg,
    # 40 nm Al, 0.085 um dead layer, 0.45 mm Si. The sample sat at WD 10.89 mm against a 10.00 mm
    # intersection, which TEAM reports as a 36.03 deg take-off angle (it implies about 40 mm
    # sample-detector distance). Area 30 mm2 and the Moxtek AP3.3 polymer window are assumptions.
    dp = epd.DetectorProperties.getDefaultSDDProperties(epd.ElectronProbe("Apreo C"), "EDAX Octane Plus (model)", 4096)
    sp = dp.getProperties()
    sp.setDetectorPosition(jl.Math.toRadians(36.03), 0.0, 40.0e-3, 10.89e-3)
    sp.setNumericProperty(epq.SpectrumProperties.DetectorArea, 30.0)
    sp.setNumericProperty(epq.SpectrumProperties.AluminumLayer, 40.0)
    sp.setNumericProperty(epq.SpectrumProperties.DeadLayer, 0.085)
    sp.setNumericProperty(epq.SpectrumProperties.DetectorThickness, 0.45)
    sp.setWindow(epd.XRayWindowFactory.createWindow(epd.XRayWindowFactory.Moxtek_AP3_3_Model))
    calib = epd.SDDCalibration(5.0, 0.0, 127.9)
    calib.makeBaseCalibration()
    det = epd.EDSDetector.createDetector(dp, calib)
    det.writeXML(jio.File(os.path.join(outDir, "octane_plus_model.xml")))

    spectra = {10: "10kV 3_2nA_1.msa", 15: "15kV 3_2nA_1.msa", 20: "20kV 3_2 nA  USE THIS ONE_1.msa"}
    # Standards: pure elements (O from Al2O3), simulated noise-free at a large dose.
    stdMats = {"C": ("C", 2.26), "O": ("Al2O3", 3.95), "Al": ("Al", 2.70), "Si": ("Si", 2.33), "Mn": ("Mn", 7.21),
               "Fe": ("Fe", 7.87), "Ni": ("Ni", 8.90), "Cu": ("Cu", 8.96), "Zn": ("Zn", 7.13), "W": ("W", 19.25)}
    fitElms = {10: ["C", "O", "Al", "Si", "Mn", "Fe", "Ni", "Cu", "W"],
               15: ["C", "O", "Al", "Si", "Mn", "Fe", "Ni", "Cu", "Zn", "W"],
               20: ["C", "O", "Al", "Si", "Mn", "Fe", "Ni", "Cu", "Zn", "W"]}
    # Line families used for the matrix correction. "K" uses K lines for the transition metals,
    # "L" uses L lines for Fe, Ni and Cu (Al K in both). Mn is quantified from Mn K where it is fit.
    lineSets = {"K": {"Al": "K", "Mn": "K", "Fe": "K", "Ni": "K", "Cu": "K"},
                "L": {"Al": "K", "Fe": "L", "Ni": "L", "Cu": "L"},
                "best10": {"Al": "K", "Mn": "K", "Fe": "K", "Ni": "L", "Cu": "L"}}
    useSets = {10: ["K", "L", "best10"], 15: ["K", "L"], 20: ["K", "L"]}
    families = {"K": epq.AtomicShell.KFamily, "L": epq.AtomicShell.LFamily, "M": epq.AtomicShell.MFamily}
    probeCurrent = 3.2  # nA, as set on the Apreo

    kfile = codecs.open(os.path.join(outDir, "dtsa2_kratios.csv"), "w", "utf-8")
    kfile.write("kV,transition_set,element,family,k,k_sigma\n")
    qfile = codecs.open(os.path.join(outDir, "dtsa2_quant.csv"), "w", "utf-8")
    qfile.write("kV,line_set,element,family,k,k_sigma,wt_pct_raw,wt_pct_raw_sigma,wt_pct_norm,wt_pct_norm_sigma,analytical_total_pct\n")
    for e0 in sorted(spectra.keys()):
        unk = readSpectrum(os.path.join(dataDir, spectra[e0]), det=det)
        unk.getProperties().setNumericProperty(epq.SpectrumProperties.ProbeCurrent, probeCurrent)
        unk.getProperties().setNumericProperty(epq.SpectrumProperties.FaradayBegin, probeCurrent)
        unk.getProperties().setNumericProperty(epq.SpectrumProperties.FaradayEnd, probeCurrent)
        qus = epq.QuantifyUsingStandards(det, epq.ToSI.keV(e0), True, True)
        for name in fitElms[e0]:
            formula, rho = stdMats[name]
            mat = material(formula, rho)
            std = simulate(mat, det, float(e0), 1.0e4, False)
            std.getProperties().setNumericProperty(epq.SpectrumProperties.FaradayBegin, 1.0)
            std.getProperties().setNumericProperty(epq.SpectrumProperties.FaradayEnd, 1.0)
            qus.addStandard(element(name), mat, std)
        res = qus.compute(unk)
        krs = unk.getProperties().getKRatioProperty(epq.SpectrumProperties.KRatios)
        byFamily = {}
        for xrts in krs.getTransitions():
            kr = krs.getKRatioU(xrts)
            elm = xrts.getElement().toAbbrev()
            fam = xrts.getWeighiestTransition().getFamily()
            famName = [f for f, v in families.items() if v == fam]
            famName = famName[0] if famName else str(xrts)
            kfile.write(u"%d,\"%s\",%s,%s,%.6g,%.3g\n" % (e0, xrts, elm, famName, kr.doubleValue(), kr.uncertainty()))
            # keep the family k-ratio with the largest signal-to-noise
            key = (elm, famName)
            if (key not in byFamily) or (kr.doubleValue() / max(kr.uncertainty(), 1e-12) > byFamily[key][1].doubleValue() / max(byFamily[key][1].uncertainty(), 1e-12)):
                byFamily[key] = (xrts, kr)
        resid = res.getResidual()
        rfile = codecs.open(os.path.join(outDir, "dtsa2_residual_%dkV.csv" % e0), "w", "utf-8")
        rfile.write("keV,measured,residual\n")
        for ch in range(unk.getChannelCount()):
            rfile.write("%.4f,%.1f,%.3f\n" % (epq.SpectrumUtils.minEnergyForChannel(unk, ch) / 1000.0 + 0.0025, unk.getCounts(ch), resid.getCounts(ch)))
        rfile.close()
        for setName in useSets[e0]:
            kdict = {}
            for elm, fam in lineSets[setName].items():
                if (elm, fam) in byFamily and byFamily[(elm, fam)][1].doubleValue() > 0.0:
                    kdict[byFamily[(elm, fam)][0]] = byFamily[(elm, fam)][1]
            cfk = epq.CompositionFromKRatios()
            krsIn = epq.KRatioSet()
            props = epq.SpectrumProperties()
            props.setNumericProperty(epq.SpectrumProperties.BeamEnergy, float(e0))
            props.addAll(det.getProperties())
            for xrts, kr in kdict.items():
                cfk.addStandard(xrts, material(xrts.getElement().toAbbrev(), stdMats[xrts.getElement().toAbbrev()][1]), props)
                krsIn.addKRatio(xrts, kr)
            comp = cfk.compute(krsIn, props)
            total = comp.sumWeightFraction() * 100.0
            for xrts, kr in sorted(kdict.items(), key=lambda t: t[0].getElement().getAtomicNumber()):
                elm = xrts.getElement()
                raw = comp.weightFractionU(elm, False)
                nrm = comp.weightFractionU(elm, True)
                qfile.write(u"%d,%s,%s,%s,%.6g,%.3g,%.3f,%.3f,%.3f,%.3f,%.2f\n" % (e0, setName, elm.toAbbrev(), lineSets[setName][elm.toAbbrev()], kr.doubleValue(), kr.uncertainty(),
                            100.0 * raw.doubleValue(), 100.0 * raw.uncertainty(), 100.0 * nrm.doubleValue(), 100.0 * nrm.uncertainty(), total))
            log.write(u"%d kV %s: %s (total %.1f%%)\n" % (e0, setName, comp.toString(), total))
        log.write(u"%d kV warning: %s\n" % (e0, res.getWarningMessage()))
    kfile.close()
    qfile.close()
except Exception, e:
    import traceback
    log.write(u"ERROR %s\n%s\n" % (e, traceback.format_exc()))
except jl.Throwable, e:
    log.write(u"JAVA ERROR %s\n" % e)
log.close()
jl.System.exit(0)
