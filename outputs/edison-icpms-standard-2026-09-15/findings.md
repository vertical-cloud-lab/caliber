# ICP-MS sample for the AlSi10Mg EDS standard: powder or printed specimen?

Edison Scientific literature research (3 LITERATURE queries, 2026-09-15) for
vertical-cloud-lab/caliber issue 12. Question: should the sample sent for ICP-MS
certification of the matrix-matched AlSi10Mg EDS standard be virgin stock powder
or material from the 3D-printed (LPBF) specimen? Instrument: Agilent 8900
triple-quadrupole ICP-MS.

Full answers with references: `q1-lpbf-mg-evaporation-loss-answer.md`,
`q2-which-sample-to-certify-answer.md`, `q3-agilent8900-alsi10mg-digestion-answer.md`.
Full trajectories: corresponding `.json` files. Task IDs: `_task_ids.json`.

## Verdict

Certify the **printed specimen**, not the powder. The certified composition must
describe the exact material the electron beam will probe — the mounted, polished
print — and LPBF measurably changes the composition of AlSi10Mg relative to the
feedstock, specifically for Mg, the element the standard exists to pin down.

## Key evidence

1. **Mg evaporates during printing.** The one parameter-resolved paired
   powder/part study found (Liu & Gibbons 2023, doi:10.26153/tsw/50945): powder
   0.440 ± 0.010 wt% Mg → as-built 0.356 wt% (lowest energy input) to 0.272 wt%
   (highest), i.e. **19–38% relative Mg loss**, increasing with energy input and
   most sensitive to scan speed. Even the smallest observed offset (0.084 wt%)
   exceeds a 0.05 wt% tolerance. Si and Al show no demonstrated bulk change; Zn
   loss is physically expected (b.p. 907 °C < Mg 1090 °C) but unquantified.
2. **Metrology.** Reference-material values are matrix- and material-specific
   (NIST guidance): a powder assay documents the feedstock, it cannot assign the
   printed solid's Mg content. The loss is process-parameter-dependent, so no
   fixed correction transfers between builds.
3. **Practical sampling favors the solid too.** Melting integrates
   particle-to-particle variation; powder grab-sampling has its own
   representativeness problems (size segregation, oxide-rich fines, spatter in
   reused powder).

## Handoff recommendations (for Dr. Rappleye's student)

- Give offcuts of the **same build/coupon** as the mounted standard — interior
  material, sacrificial first cut discarded, clean sectioning (steel tools can
  add Fe, which is an analyte; carbide adds W/Co). Degrease and rinse.
- **≥3 independent digestions** (~0.1–0.5 g each), not 3 readings of one
  solution. If material allows, pieces from more than one location to check
  homogeneity (Mg gradients along build height are plausible, not guaranteed).
- Optionally add the virgin powder as a second, supplementary digest: it
  quantifies the Mg evaporation loss for our process — useful for predicting
  printed compositions from powder blends in the alloy campaign — but it is not
  the certified value for the standard.

## Digestion / instrument cautions

- **Si (~10 wt%) is the hard part, not Mg.** HCl/HNO₃-only digests of Al alloys
  grossly under-recover Si (interlab CRM example: 0.144% measured vs 0.415%
  certified) because Si-rich phases don't dissolve; Mg, Fe, Cu, Zn, Mn, Ti
  recover well in the same digests. Quantitative total Si needs closed-vessel
  HNO₃–HF + boric-acid complexation (no evaporation to dryness; SiF₄ is
  volatile) or a validated alkaline fusion. Ask whether the lab's workflow
  permits HF; if not, the Mg number (the one we actually need) is still good
  from an acid digest, but the Si number will be badly low — treat Si as
  nominal or handle it separately.
- **Agilent 8900 fit:** minor/trace elements are its sweet spot (He KED
  multielement; H₂ on-mass MS/MS for ²⁸Si vs N₂⁺/CO⁺ if Si by MS is attempted).
  Percent-level Al/Si (and arguably Mg at 0.2–0.5 wt%) are better served by
  ICP-OES; on the 8900 they need very large, carefully verified dilution tiers.
  Realistic full-method accuracy: ~1–3% relative for majors, 1–5% for Mg-level
  minors — ample for an EDS standard.

## Caveats

- The 19–38% Mg-loss figures come from one conference study whose extremes were
  outside the optimized process window and which used EDX (powder) vs spark OES
  (part); the direction and order of magnitude are robust, the exact numbers are
  process-specific — which is itself the argument for assaying our own print.
- ICP certifies the bulk; EDS samples µm³ of a two-phase alloy. As established
  earlier in issue 12, use large rasters / many random points on the standard so
  the probed mean represents the certified bulk.
