# MgO cube standard (SPI 01845-AB)

Single-crystal MgO is the Mg (and O) EDS standard picked in the
[PR #11 thread](https://github.com/vertical-cloud-lab/caliber/pull/11#issuecomment-5484274140).
The plan was to cleave a fresh {100} face right before each session, which would avoid
polishing entirely. The first cleave attempt failed, so the plan is now diamond saw →
Bakelite → water-free polish.

| Item | Value |
|---|---|
| Part | [SPI 01845-AB](https://www.2spi.com/category/magnesium-oxide-substrates/): MgO single-crystal cube, 10 × 10 × 10 mm, cleaved (100), purity > 99.9%, $50 |
| Received | 2026-09-29 ([#12](https://github.com/vertical-cloud-lab/caliber/issues/12#issuecomment-5900698315)) |
| Vendor note | [Cleaving and Polishing MgO Crystal Substrates](https://www.2spi.com/catalog/documents/MgO_substrates_cleaving.pdf) (SPI, rev. 2/16) |

## 1. Cleave attempt (reported 2026-10-07)

- Razor blade placed on a {100} face, struck with a hammer: no cleave.
- A short sawed notch to start the crack: no change.
- Video: [MgO cube splitting fail](https://youtu.be/TNEI0Uvtbqg)

SPI's procedure for this crystal: a single-edge GEM-type razor blade (or a small knife)
and a small hammer, on a clean, lint-free work surface in a relatively dry room. Place the
blade parallel to an existing edge and tap lightly. From the note:

> the only time there is a problem is when the razor blade being used gets dull (it should
> be changed after every several cleavings). In practical terms, a 2 mm thick slab is
> probably the lower limit in thickness that can be obtained this way.

> obtaining a perfectly cleaved (100) block is not easy without first some practice and
> certainly it is not easy doing the cleaving without generating at least some "chips".

Likely contributors (inferred, not confirmed):

1. **Blade edge.** Periclase (MgO) is [Mohs 6](http://webmineral.com/data/Periclase.shtml),
   about as hard as the steel blade, so sawing a notch with a steel edge dulls it quickly
   and leaves a blunt groove rather than a sharp crack starter. A dull blade is the one
   failure mode SPI names.
2. **Slab thickness.** The earlier advice in #12 was to take off a 1–2 mm slab per cleave.
   SPI puts 2 mm as the practical minimum. With the blade near an edge, the crack tends to
   curve out to the near face and chip; splitting the cube in half keeps the loading
   symmetric so the crack runs straight.
3. **Support.** A compliant support absorbs a light tap. If the strike was on the textured
   rubber bench mat seen in the video, much of the tap went into the mat.

If one more try is wanted before sawing (a fresh blade and a few minutes): new GEM blade
(not the one used for the notch), hard flat bench with a lint-free wipe, blade across the
middle of a face parallel to an edge, one light tap.

## 2. Plan: diamond saw → Bakelite → water-free polish

This follows the
[byu-vcl polishing SOP](https://github.com/vertical-cloud-lab/byu-vcl/issues/110#issuecomment-5736363939),
with changes for MgO. SPI: "For polishing or repolishing MgO, non-aqueous media should be
used at all times", and for storage "it should always be kept in a desiccator cabinet".

| SOP step | Change for MgO |
|---|---|
| 1. Diamond saw (water coolant) | Optional: the cube already matches the SOP's 1 cm³ target size. Saw only to keep a spare half, then rinse with ethanol and dry right away |
| 2. Bakelite mount | Put an undamaged original face down as the analysis face, not the hammer-struck face or a saw-cut face. A cleaved face has far less damage to grind off |
| 3. Belt sander (water) | Skip. Open the face on SiC paper instead (next row) |
| 4. SiC 320–1200, 1 µm alumina, DI-water rinses | Every step water-free: ethanol/IPA in small squirts (flammable) or a glycol lubricant (e.g., Allied GreenLube, hexylene glycol) on the SiC paper, starting at 600 grit; diamond suspension in a non-aqueous carrier for polishing, down to 1 µm (0.25 µm if available); ethanol rinses instead of water. Use a dedicated, labeled MgO pad: MgO carried onto an AlSi10Mg pad would add Mg to the unknowns |
| 5. Ethanol clean, methanol ultrasonic bath | No change; keep the bath water out of the dish |
| 6. Vibratory polish | Skip. Colloidal silica is aqueous and leaves Si residue |

After polishing:

- Dry with compressed air, store in the desiccator or under vacuum, and carbon-coat soon.
  Per SPI, a white haze appears after about three days in air, and sooner in humid air.
- Bakelite and MgO are both insulators. After coating, run a strip of carbon tape from the
  coated face to the stub or holder.
- Enter the coating in DTSA-II (Properties → coating), as in the cleave plan.
- If haze appears later, repolish lightly with non-aqueous media and recoat.
