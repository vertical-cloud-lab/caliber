# Data Acquisition (DAQ) During EDS

This document explains what actually happens between an X-ray photon entering the detector and a count appearing in a spectrum channel, and why each stage of that chain dictates the acquisition parameters we set (process time, dead-time target, count rate, live time). It complements the discussion of *analytical* parameter selection (kV, current, geometry, standards) in issue No. 1.

## 1. The signal chain

```
photon → SDD crystal → charge cloud → anode → FET/preamp (charge → voltage step)
       → digitizer → fast channel (timing/pile-up)  ┐
                   → slow channel (energy filtering) ┴→ peak height → MCA bin → spectrum
```

1. **Photon absorption.** An X-ray photon absorbed in the silicon drift detector (SDD) creates electron–hole pairs, ~1 pair per 3.6 eV of photon energy. A 6.4 keV Fe Kα photon therefore yields only ~1,800 electrons — a femtocoulomb-scale charge that everything downstream is built to measure precisely.
2. **Charge collection.** The SDD's ring-electrode field drifts electrons to a tiny central anode. The small anode capacitance is *the* reason SDDs replaced Si(Li) detectors: lower capacitance → lower series noise → good energy resolution even at short shaping times, i.e. at high count rates ([Amptek AN-SDD-003](https://www.amptek.com/-/media/ametekamptek/documents/resources/amptek-silicon-drift-detectors.pdf)).
3. **Preamplifier.** A charge-sensitive preamp integrates the charge into a voltage step; the step height is proportional to photon energy.
4. **Digital pulse processor (DPP).** Modern systems digitize the preamp output immediately and do all shaping in firmware, in two parallel channels ([Amptek AN-DPP-001, *Digital Pulse Processors Theory of Operation*](https://www.amptek.com/-/media/ametekamptek/documents/resources/dpp_theory.pdf)):
   - a **slow channel** with a long trapezoidal filter that averages noise to measure pulse height (energy) accurately, and
   - a **fast channel** with a very short filter that timestamps arrivals and counts the *true* input rate.
5. **MCA.** Each accepted pulse height is binned into a multichannel-analyzer channel (typically 5 or 10 eV/channel), building the spectrum.

## 2. Process time: the resolution ↔ throughput trade-off

The slow channel's **process time** (peaking/shaping time, vendor names vary: "process time 1–6", "time constant") sets how long each pulse is averaged.

- **Longer process time** → more noise averaging → better energy resolution (narrower peaks, e.g. better separation of overlapping lines like S Kα / Mo Lα or the Al/Si/Mg region relevant to AlSi10Mg) — but each photon occupies the processor longer, so maximum throughput drops.
- **Shorter process time** → higher throughput, worse resolution.

Electronic (series) noise dominates at short peaking times, which is why the achievable resolution degrades as you shorten the filter; SDDs push the noise floor low enough that even ~1 µs peaking times give usable resolution ([Amptek, *Understanding Digital Pulse Processors*](https://atomfizika.elte.hu/muszerek/Amptek/Documentation/Application%20Notes%20and%20FAQs/Amptek%20Digital%20Pulse%20Processors/Understanding%20digital%20pulse%20processors.pdf)).

**Rule:** pick the longest process time whose throughput still lets you reach your target counts in acceptable wall-clock time; drop to shorter process times only for high-rate mapping where per-pixel dwell is the bottleneck.

## 3. Dead time, live time, and the throughput curve

While the processor is measuring one pulse it cannot accept another; the busy fraction is the **dead time**. Two consequences:

- **Live time vs. real time.** Acquisitions are specified in *live* time — the clock only runs while the system can accept events — so Poisson statistics stay valid regardless of rate. A 60 s live-time acquisition at 30% dead time takes ~86 s of real time ([Amptek, *Acquisition Time, Live Time, and All That*](https://atomfizika.elte.hu/muszerek/Amptek/Documentation/Application%20Notes%20and%20FAQs/Amptek%20DPPMCA%20Software/Count%20Rate%20Example.pdf)).
- **Paralyzable throughput curve.** Output rate = input rate × e^(−input rate × dead-time-per-event). Output *peaks* and then falls as input rate keeps rising — turning up the beam current past the optimum yields *fewer* stored counts, not more.

**Why the ~20–40% dead-time target exists:** it sits below the throughput peak with margin, keeps pile-up (below) manageable, and vendors recommend staying ≤50%. Beam current is the knob used to land in this band, given the chosen process time.

## 4. Pile-up: where sum peaks come from

If two photons arrive within the slow channel's resolving time, their steps merge and the processor would record one event at the *summed* energy. The fast channel exists to catch this: it detects the two distinct arrivals and vetoes the corrupted slow-channel measurement (**pile-up rejection**). Rejection fails when the second photon arrives within the *fast* channel's resolving time (~100 ns class), so residual **sum peaks** (e.g. 2×Al Kα at 2.98 keV, masquerading near Ag Lα) still appear at high rates and can be misidentified as trace elements. Running in the recommended dead-time band keeps the sum-peak fraction negligible; software corrections (e.g. in [NIST DTSA-II](https://www.nist.gov/services-resources/software/nist-dtsa-ii)) can model the remainder.

## 5. Detector-response artifacts baked into the spectrum

The DAQ chain also imprints artifacts that quantification software must model:

- **Si escape peaks** — a Si Kα photon (1.74 keV) generated in the detector escapes, leaving a peak at (parent − 1.74) keV.
- **Incomplete charge collection (ICC)** — events near the entrance window lose charge, producing low-energy tails on peaks.
- **Si internal fluorescence peak** — a small spurious Si peak from the detector's own dead layer.
- **Energy calibration & channel width** — gain drift shifts peak positions; routine calibration on known lines (e.g. Cu Kα/L) keeps the eV-per-channel mapping honest.

These are why "the same sample on the same SEM" can quantify differently across detectors/processors: the response function belongs to the DAQ chain, not the sample.

## 6. Counting statistics: how long to acquire

Every channel's content is Poisson-distributed: for N counts, σ = √N.

- ~10,000 net counts in a peak → ~1% relative precision on that intensity.
- Detection limit: a peak is detectable at 3σ when net counts > 3·√(2·background under the peak).

So the acquisition endpoint is not a fixed time — it is *"enough live time (at the achievable output rate) for the smallest peak of interest to hit its target precision."* Trace-element work (the several-fold Mg over-report in AlSi10Mg cited in the [CALIBER abstract](../README.md)) is exactly the regime where insufficient counts plus standardless deconvolution multiply into large errors; measured standards and adequate statistics recover WDS-class accuracy ([Newbury & Ritchie, *J. Mater. Sci.* 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4555346/); [Newbury, Swyt & Myklebust, *Anal. Chem.* 1995](https://pubs.acs.org/doi/10.1021/ac00107a017)).

## 7. Practical DAQ checklist

| Parameter | Set by | Typical choice |
|---|---|---|
| Process time | Needed peak separation vs. throughput | Longest that meets time budget; short only for fast mapping |
| Beam current | Target dead time at chosen process time | Lands dead time at ~20–40% (≤50%) |
| Live time | Poisson precision of smallest peak of interest | Until ~10 k net counts (majors) or detection-limit criterion (traces) |
| MCA range/channels | Highest line of interest at chosen kV | 0–10 or 0–20 keV, 5–10 eV/channel |
| Calibration | Gain drift | Verify on known lines before quantitative work |
| Pile-up check | Sum peaks at high rate | Inspect for 2×major-line energies before assigning trace peaks |

## Further reading

- Goldstein, Newbury, Michael, Ritchie, Scott & Joy, *Scanning Electron Microscopy and X-Ray Microanalysis*, 4th ed., Springer ([doi:10.1007/978-1-4939-6676-9](https://doi.org/10.1007/978-1-4939-6676-9)) — chapters on EDS detectors, pulse processing, and quantification.
- Newbury & Ritchie, ["Is SEM/EDS Quantitative?"](https://onlinelibrary.wiley.com/doi/abs/10.1002/sca.21041), *Scanning* 35 (2013) 141–168.
- [NIST DTSA-II](https://www.nist.gov/services-resources/software/nist-dtsa-ii) — open-source spectrum simulation and k-ratio quantification; useful for testing how DAQ settings propagate into quantification error.
