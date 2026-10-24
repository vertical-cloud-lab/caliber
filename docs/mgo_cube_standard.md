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

Likely contributors (not confirmed; the video can't be played from the agent runner):

1. **Blade edge.** A dull blade is the one failure mode SPI names. This cube is harder than
   the blade: SPI lists [Vickers 910, Mohs 5.8](https://www.2spi.com/item/01845-ab/), and
   razor steel is about 620–850 HV ([US5433801A](https://patents.google.com/patent/US5433801A/en),
   [US9032628B2](https://patents.google.com/patent/US9032628B2/en)). A blade that has been
   struck on, scraped across, or used to saw MgO is no longer sharp.
2. **Line contact on a hard oxide.** Two vacuum-cleaver papers favor loading a single point
   over a straight edge for hard rock-salt oxides: Schmid 2006 found razor-blade line contact
   on NiO "rather difficult", and Sander 2022 says point loading suits MgO and needs less
   force (table below).
3. **The notch.** A sawed groove is blunt (root tens to hundreds of µm), not crack-like. It
   only helps once its root is sharpened (see "What sharp means").
4. **Geometry.** SPI gives 2 mm as the practical slab limit for its razor method; Futagami &
   Akashi took 1 mm slabs off 7 mm blocks with a chisel. Splitting in half is the most
   forgiving: "the pressure is distributed equally to both parts of the crystal"
   ([McCrone, on KBr](https://www.mccrone.com/how-to-cleave-polish-use-kbr-crystals/)).
5. **Support.** SPI asks for a clean, lint-free surface; Langdon & Pask (via Edison) cleave
   MgO "on a soft pad of tissue paper" to avoid micro-cracks. That a thick rubber mat soaks
   up the tap is inference only.

### Sources

| Source | What it says |
|---|---|
| [SPI note](https://www.2spi.com/catalog/documents/MgO_substrates_cleaving.pdf) (rev. 2/16) | Quoted above; the only vendor procedure found |
| Futagami & Akashi, [Rep. Res. Inst. Appl. Mech. Kyushu Univ. 20, 21 (1973)](https://doi.org/10.5109/7172625) | 7 mm MgO blocks "cleaved into specimens of 1 mm thickness at room temperature by a chisel with a sharp knife edge", by "a blow on the chisel" |
| Schmid, Renner & Giessibl, [Rev. Sci. Instrum. 77, 036101 (2006)](https://doi.org/10.1063/1.2166670) ([arXiv](https://arxiv.org/abs/cond-mat/0511325)) | "cleaving NiO with a razor blade that touches the sample along a line is rather difficult, while cleaving it with a wire cutter is simple and requires little force even for large cross sections" (2 × 4 mm²) |
| Sander et al., [Rev. Sci. Instrum. 93, 053703 (2022)](https://doi.org/10.1063/5.0088802) ([accepted ms](https://zenodo.org/record/6510004)) | A 30° tungsten carbide blade loads a single point, "more suitable for cleaving hard crystals such as MgO ... the cleavage requires less force" (crystals of a few mm) |
| Yang et al., [Environ. Sci. Technol. 59, 3484 (2025)](https://www.osti.gov/servlets/purl/2538136) | SPI MgO "cleaved with a razor blade along the (100) surface immediately before reaction"; debris blown off with N2 |
| Langdon & Pask (1968); Preuss et al., [J. Eur. Ceram. Soc. 46, 117905 (2026)](https://doi.org/10.1016/j.jeurceramsoc.2025.117905) | Edison citations, not read: tissue-paper pad; diamond-wire notches in MgO sharpened "using a sharp razor blade and 1 µm diamond paste" |

### What "sharp" means

No standard defines it for cleaving. Reference numbers:

- **New blades:** SEM edge width of a Gillette razor blade 0.35–0.45 µm
  ([Verhoeven 2004](https://northarmknives.com/wp-content/uploads/2016/01/knifeshexps.pdf));
  utility blades, including Olfa, under 200 nm
  ([Science of Sharp](https://scienceofsharp.com/2014/05/28/a-comparison-of-several-manufactured-blades/));
  an unused scalpel about 1 µm radius, with > 5 µm called "unrealistically blunt"
  ([McCarthy et al. 2010](https://northarmknives.com/wp-content/uploads/2016/09/gilchrist_part2.pdf)).
  No measurement of GEM blades was found.
- **Dull blades:** edges fail mostly by chipping, not uniform rounding
  ([MIT News 2020](https://news.mit.edu/2020/why-shaving-dulls-razors-0806), on Roscioli et
  al., *Science*).
- **Notches:** in ceramic fracture tests, a notch acts like a crack only when its root is
  below about 10–20 µm ([Kübler 2000](https://gruppofrattura.it/ocs/index.php/esis/ECF13/paper/download/8516/4958),
  [NASA/TM-2006-214090](https://ntrs.nasa.gov/api/citations/20060007571/downloads/20060007571.pdf)).
  Diamond-disk and diamond-wire notches measured 250 and 70–80 µm; a razor blade with
  diamond paste brought them to 5–7 µm
  ([Palacios et al.](https://scipub.euro-fusion.org/wp-content/uploads/eurofusion/WPMATPR15_13757_submitted.pdf), in tungsten).

Practical check: hold the blade edge-on under a bright lamp. A sharp edge is "an almost
invisibly smooth black line", and any glints are "dull, bent or chipped areas"
([Peachey 2016](https://jeffpeachey.com/2016/10/04/twelve-ways-of-testing-knife-sharpness/)).
A 10–50× loupe shows chips and rolled spots. Blades are cheap: use one straight from the pack
for every attempt.

### Edison check

Two `LITERATURE_HIGH` queries; answers, tables, and trajectories are in
[`outputs/edison_mgo_cleaving/`](../outputs/edison_mgo_cleaving/).

- [Procedure](../outputs/edison_mgo_cleaving/q1_procedure/answer.md): blade (or chisel) and tap is
  standard practice for MgO and "generally reliable" for a 10 mm cube, since the {100} cleavage
  toughness is low (0.81 MPa·m½, [Schultz et al. 1994](https://doi.org/10.1007/bf00012370)).
  It is not guaranteed: chips, steps from several crack origins, slip under a blunt edge, and
  subgrains. Recommends a fresh blade, a split near the middle, one light sharp tap, and a
  thin compliant pad.
- [Sharpness](../outputs/edison_mgo_cleaving/q2_sharpness/answer.md): the edge radius is what
  matters; a steel edge can dull on MgO, so treat blades as consumables; sawed notches are
  too blunt to act as cracks.
- Caveats: Edison found no success rate for 10 mm cubes, and its claim that pre-scoring
  "generally helps" rests on notches that were then sharpened.

### Video and SOP

- **Video:** none found of MgO being cleaved (YouTube searched in English, Japanese, Chinese,
  and German; also Vimeo, JoVE, and paper supplements). Closest:
  - Schmid et al. (2006) published movies of KBr and NiO cleaving with their point-contact
    cleaver (EPAPS E-RSINAK-77-209602, not opened).
  - Blade-and-hammer demos on rock salt (NaCl), the same method on a crystal that cleaves
    far more easily (0.17 vs. 0.81 MPa·m½): [Science Museum, Tokyo](https://www.youtube.com/watch?v=EUjdhXIKVUY),
    [ASNR](https://www.youtube.com/watch?v=Znv1LMo2ffw). Checked by title and thumbnails only.
- **SOP:** none found for MgO cubes beyond SPI's note. The SPI note and the Futagami & Akashi
  methods paragraph are the closest; the steps below combine them.

### If trying again before sawing

1. Single-edge blade straight from the pack, checked edge-on under a lamp. A new blade for
   each try, never one that has touched MgO.
2. Hard, flat bench with a lint-free wipe as the pad, not the rubber mat.
3. Blade across the middle of an undamaged face, parallel to an edge, so the cube splits in half.
4. One light, sharp tap with a small hammer.
5. If line contact keeps failing, point contact is what worked in the hard-oxide papers
   (wire cutter, single-point blade). Those cleaved cross sections of a few mm; this cube is
   10 × 10 mm.

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
