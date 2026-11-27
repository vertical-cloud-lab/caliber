"""3D-printable storage insert for SEM pin stubs, sized to drop into the base of a
standard 100 mm polystyrene Petri dish (a chem-stores staple).

Regenerate the STL/STEP after changing parameters:
    pip install cadquery
    python cad/stub_storage_insert.py
"""

import math
from pathlib import Path

import cadquery as cq

# Ted Pella 16111 pin stub: Ø12.7 mm head, Ø3.2 mm x 8 mm pin
head_d = 12.7
pin_d = 3.2
pin_len = 8.0

# Measure the dish's inner base diameter and set insert_d ~1.5 mm smaller.
insert_d = 84.0        # typical 100 mm Petri dish inner base is ~85.5-88 mm
plate_t = 9.2          # leaves a ~0.7 mm floor under the deepest pin
hole_d = pin_d + 0.3   # slip fit; FDM holes print slightly undersized
hole_depth = pin_len + 0.5
csk_d = hole_d + 1.6   # chamfered lead-in for gloved/tweezer loading
pitch = 15.0           # ~2.3 mm gap between head rims for the groove-gripper tweezers
edge_margin = 0.8      # head rim to insert rim
notch_d = 14.0         # fingertip scallop on the rim for lifting the insert out
notch_x = insert_d / 2 + 2.0

# Hex-packed hole centers, keeping every head inside the rim and clear of the notch
row_h = pitch * math.sqrt(3) / 2
max_r = insert_d / 2 - head_d / 2 - edge_margin
n = int(max_r // row_h) + 2
points = []
for j in range(-n, n + 1):
    y = j * row_h
    x0 = pitch / 2 if j % 2 else 0.0
    for i in range(-n, n + 1):
        x = i * pitch + x0
        if math.hypot(x, y) > max_r:
            continue
        if math.hypot(x - notch_x, y) < (notch_d + head_d) / 2 + 0.5:
            continue
        points.append((x, y))

insert = (
    cq.Workplane("XY")
    .circle(insert_d / 2)
    .extrude(plate_t)
    .faces(">Z")
    .workplane()
    .pushPoints(points)
    .cskHole(hole_d, csk_d, 90, depth=hole_depth)
    .cut(
        cq.Workplane("XY")
        .workplane(offset=-1.0)
        .center(notch_x, 0)
        .circle(notch_d / 2)
        .extrude(plate_t + 2.0)
    )
)

out = Path(__file__).parent
cq.exporters.export(insert, str(out / "stub_storage_insert.stl"), tolerance=1e-3)
cq.exporters.export(insert, str(out / "stub_storage_insert.step"))
print(f"{len(points)} stub positions, insert Ø{insert_d} x {plate_t} mm")
