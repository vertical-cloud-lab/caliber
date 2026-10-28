# -*- coding: utf-8 -*-
# NIST DTSA-II (Jython 2.7) script: NISTMonte (Gen 3) spectra of nominal C63000 (82Cu-10Al-5Ni-3Fe wt%,
# 7.58 g/cm3) at 10, 15 and 20 kV, with characteristic and continuum secondary fluorescence:
#   bulk      flat bulk, beam normal to the surface
#   sphere25  50 um diameter sphere on carbon, beam on the top centre
#   sphere50  100 um diameter sphere on carbon, beam on the top centre
#   raster25  50 um sphere on carbon, beam rastered over the square around it (an area scan of one
#             particle with the tape showing in the corners); symmetric in y, so y >= 0 only
# Doses match the measured spectra (3.2 nA x live time). Each energy uses the detector (and energy
# calibration) that dtsa2_quant.py wrote; rerun dtsa2_quant.py afterwards to fit and quantify these
# spectra with the same simulated standards as the measured ones.
# Run:  NAB_OUT=outputs ./run_dtsa2.sh dtsa2_mc.py   (NAB_NTRAJ: trajectories per simulation)
import os, codecs, time
import java.lang as jl
import java.io as jio
import gov.nist.microanalysis.EPQLibrary as epq
import gov.nist.microanalysis.EPQLibrary.Detector as epd
import dtsa2.mcSimulate3 as mc3

outDir = os.path.abspath(os.environ["NAB_OUT"])
nTraj = int(os.environ.get("NAB_NTRAJ", "4000"))
nGrid = int(os.environ.get("NAB_RASTER_GRID", "10"))
mcDir = os.path.join(outDir, "mc")
if not os.path.isdir(mcDir):
    os.makedirs(mcDir)
log = codecs.open(os.path.join(outDir, "dtsa2_mc.log"), "w", "utf-8")
try:
    nab = mixture({"Cu": 0.82, "Al": 0.10, "Ni": 0.05, "Fe": 0.03}, 7.58, "C63000 nominal")
    carbon = material("C", 1.8)
    doses = {10: 3.2 * 55.381, 15: 3.2 * 31.715, 20: 3.2 * 24.409}
    for e0 in (10, 15, 20):
        det = epd.EDSDetector.readXML(jio.File(os.path.join(outDir, "octane_plus_model_%dkV.xml" % e0)))
        sims = {}
        t0 = time.time()
        sims["bulk"] = mc3.simulate(nab, det, e0=float(e0), dose=doses[e0], withPoisson=False, nTraj=nTraj, sf=True, bf=True)
        log.write(u"%d kV bulk: %.0f s\n" % (e0, time.time() - t0))
        log.flush()
        for name, r in (("sphere25", 25.0e-6), ("sphere50", 50.0e-6)):
            t0 = time.time()
            sims[name] = mc3.sphere(nab, r, det, e0=float(e0), withPoisson=False, nTraj=nTraj, dose=doses[e0], sf=True, bf=True, substrate=carbon)
            log.write(u"%d kV %s: %.0f s\n" % (e0, name, time.time() - t0))
            log.flush()
        t0 = time.time()
        r = 25.0e-6
        step = 2.0 * r / nGrid
        nPos = nGrid * (nGrid // 2)
        raster = None
        for i in range(nGrid):
            for j in range(nGrid // 2):
                x, y = -r + (i + 0.5) * step, (j + 0.5) * step
                xp = mc3.configureBeam(x, y, -0.099, 10.0)
                s = mc3.sphere(nab, r, det, e0=float(e0), withPoisson=False, nTraj=max(nTraj // nPos * 4, 50), dose=doses[e0] / nPos,
                               sf=True, bf=True, substrate=carbon, xtraParams=xp)
                raster = s if raster is None else raster + s
        raster.rename("MC raster over a 50 um C63000 sphere on C at %d kV" % e0)
        sims["raster25"] = raster
        log.write(u"%d kV raster25 (%d positions): %.0f s\n" % (e0, nPos, time.time() - t0))
        log.flush()
        for name, s in sims.items():
            s.getProperties().setNumericProperty(epq.SpectrumProperties.BeamEnergy, float(e0))
            s.save(os.path.join(mcDir, "%s_%dkV.msa" % (name, e0)))
except Exception, e:
    import traceback
    log.write(u"ERROR %s\n%s\n" % (e, traceback.format_exc()))
except jl.Throwable, e:
    log.write(u"JAVA ERROR %s\n" % e)
log.close()
jl.System.exit(0)
