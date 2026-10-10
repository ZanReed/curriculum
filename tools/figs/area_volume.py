"""chain.measure.area-volume (710-): perimeter, area and volume figures.

Coordinates are in the shape's own units (1 graph unit = 1 cm or 1 m), so every side label
equals its drawn length and the checker's proportion test is exact. Heights of triangles are
dashed segments with a right-angle mark at the foot and a `text` length label, because a `side`
label on an inside segment is pushed away from the named points' centroid (figure-marks.ts) and
can land on a slanted side.

Figures for the chain's activities, defined from their intended measurements. Built by
tools/figs/build.py; see tools/figs/core.py.
"""
import math

from core import FIGS, ANS, P, f, fig  # noqa: F401


def runs(values):
    """Group sorted ints into maximal consecutive runs [(start, end_exclusive)]."""
    out = []
    for v in sorted(values):
        if out and out[-1][1] == v:
            out[-1][1] = v + 1
        else:
            out.append([v, v + 1])
    return out


def tiles(name, alt, outline, cells, labels=(), extra=("to scale",)):
    """A shape made of 1 x 1 tiles. outline: vertex list (in order); cells: set of (x, y) lower-left
    corners. Internal grid lines are drawn as maximal runs between two cells of the set."""
    cells = set(cells)
    lines = ["polygon " + " ".join(f(p) for p in outline)]
    xs = sorted({c[0] for c in cells})
    ys = sorted({c[1] for c in cells})
    for k in range(min(xs) + 1, max(xs) + 1):
        ys_here = [y for y in ys if (k - 1, y) in cells and (k, y) in cells]
        for a, b in runs(ys_here):
            lines.append(f"segment {f((k, a))} {f((k, b))}")
    for k in range(min(ys) + 1, max(ys) + 1):
        xs_here = [x for x in xs if (x, k - 1) in cells and (x, k) in cells]
        for a, b in runs(xs_here):
            lines.append(f"segment {f((a, k))} {f((b, k))}")
    for (p, q, lab) in labels:
        lines.append(f'side {f(p)} {f(q)} "{lab}"')
    fig(name, alt, lines, extra=extra)


def edge_count(cells):
    cells = set(cells)
    return sum(1 for (x, y) in cells
               if any(n not in cells for n in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))))


def rect_cells(w, h):
    return {(x, y) for x in range(w) for y in range(h)}


def poly(name, alt, pts, sides=None, rights=(), dashed=(), texts=(), answers=None, extra=(),
         letters=True, ticks=(), right_coords=()):
    """pts: list of (letter, (x, y)). sides: {"AB": label}. rights: ["DAB", ...] (vertex in the
    middle). dashed: [((x,y),(x,y))]. texts: [((x,y), label)]."""
    lines = []
    names = {}
    for letter, p in pts:
        names[letter] = p
        if letters:
            lines.append(f'point {f(p)} "{letter}"')
    if letters:
        lines.append("polygon " + " ".join(l for l, _ in pts))
    else:
        lines.append("polygon " + " ".join(f(p) for _, p in pts))
    for a, b in dashed:
        lines.append(f"segment {f(a)} {f(b)} dashed")
    for k, lab in (sides or {}).items():
        if letters:
            lines.append(f'side {k} "{lab}"')
        else:
            lines.append(f'side {f(names[k[0]])} {f(names[k[1]])} "{lab}"')
    for k, n in ticks:
        lines.append(f"ticks {k} {n}" if letters else f"ticks {f(names[k[0]])} {f(names[k[1]])} {n}")
    for r in rights:
        lines.append(f"angle {r} right")
    for (p, v, q) in right_coords:
        lines.append(f"angle {f(p)} {f(v)} {f(q)} right")
    for p, lab in texts:
        lines.append(f'text {f(p)} "{lab}"')
    fig(name, alt, lines, answers, extra)


def rect(name, alt, w, h, unit, letters="ABCD", label_all=False, extra=()):
    a, b, c, d = letters
    sides = {f"{a}{b}": f"{w} {unit}", f"{d}{a}": f"{h} {unit}"}
    if label_all:
        sides.update({f"{b}{c}": f"{h} {unit}", f"{c}{d}": f"{w} {unit}"})
    poly(name, alt, [(a, (0, 0)), (b, (w, 0)), (c, (w, h)), (d, (0, h))], sides,
         rights=[f"{d}{a}{b}", f"{a}{b}{c}", f"{b}{c}{d}", f"{c}{d}{a}"], extra=extra)


def tri_height(name, alt, base, apex, unit, label_slants=("BC",), letters="ABC", answers=None):
    """Triangle A(0,0) B(base,0) C(apex). Height from C dashed to the foot on AB, with a right
    mark and a text label. Slant sides named in label_slants get their (integer) lengths."""
    a, b, c = letters
    A, B, C = (0, 0), (base, 0), apex
    H = (apex[0], 0)
    pts = {a: A, b: B, c: C}
    sides = {f"{a}{b}": f"{base} {unit}"}
    for s in label_slants:
        d = math.dist(pts[s[0]], pts[s[1]])
        assert abs(d - round(d)) < 1e-9, (name, s, d)
        sides[s] = f"{round(d)} {unit}"
    h = apex[1]
    # put the height label in the middle of the wider half of the triangle, at half height:
    # at y = h/2 the left half spans x from C.x/2 to H.x, the right half from H.x to (B.x + C.x)/2
    left_room, right_room = apex[0] / 2, (base - apex[0]) / 2
    text_at = (round(H[0] + right_room / 2, 2) if right_room >= left_room else round(H[0] - left_room / 2, 2),
               round(h / 2, 2))
    poly(name, alt, [(a, A), (b, B), (c, C)], sides, dashed=[(C, H)], texts=[(text_at, f"{h} {unit}")],
         right_coords=[(C, H, B if H != B else A)], answers=answers)


def right_tri(name, alt, base, height, unit, box=False, letters="ABC"):
    """Right-angled triangle A(0,0) B(base,0) C(base,height), right angle at B. box adds the
    dashed rectangle ABCD around it (D at (0, height))."""
    a, b, c = letters
    dashed = [((0, 0), (0, height)), ((0, height), (base, height))] if box else []
    poly(name, alt, [(a, (0, 0)), (b, (base, 0)), (c, (base, height))],
         {f"{a}{b}": f"{base} {unit}", f"{b}{c}": f"{height} {unit}"}, rights=[f"{a}{b}{c}"], dashed=dashed)


def L(name, alt, pts, sides, unit, answers=None, dashed=(), letters=True):
    """pts: six (letter, (x, y)). sides: {"AB": number or 'a'}."""
    lab = {k: (f"{v} {unit}" if isinstance(v, (int, float)) else v) for k, v in sides.items()}  # letters stay bare
    poly(name, alt, pts, lab, dashed=dashed, answers=answers, letters=letters)


def perim(pts):
    return sum(math.dist(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts)))


def shoelace(pts):
    return abs(sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                   for i in range(len(pts)))) / 2


def house(name, alt, w, wall, apex, unit, split=True, answers=None):
    """A rectangle w x wall with an isosceles triangle roof to total height apex.
    A(0,0) B(w,0) C(w,wall) D(w/2,apex) E(0,wall). Labels AB, BC and the slant CD; the total height
    is a dashed line from D to the base with a right mark and a text label; split adds a dashed EC."""
    half = w / 2
    slant = math.dist((w, wall), (half, apex))
    assert abs(slant - round(slant)) < 1e-9, (name, slant)
    A, B, C, D, E = (0, 0), (w, 0), (w, wall), (half, apex), (0, wall)
    foot = (half, 0)
    dashed = [(D, foot)] + ([(E, C)] if split else [])
    text_at = (round(half + 0.1 * max(w, apex), 2), round(wall / 2, 2))
    poly(name, alt, [("A", A), ("B", B), ("C", C), ("D", D), ("E", E)],
         {"AB": f"{w:g} {unit}", "BC": f"{wall:g} {unit}", "CD": f"{round(slant)} {unit}"},
         rights=["EAB", "ABC"], dashed=dashed, texts=[(text_at, f"{apex:g} {unit}")],
         right_coords=[(D, foot, B)], answers=answers)


def cuboid(name, alt, l, w, h, unit="cm", units=False, extra=()):
    fig(name, alt, [f"cuboid {l:g} {w:g} {h:g}" + (f" {unit}" if unit else "") + (" units" if units else "")],
        extra=extra)


def define():
    # ================= Activity 01: perimeter =================
    tiles("a1-w1", "A rectangular patio 6 paving stones long and 3 stones wide, with every stone drawn",
          [(0, 0), (6, 0), (6, 3), (0, 3)], rect_cells(6, 3))
    assert edge_count(rect_cells(6, 3)) == 14
    rect("a1-w2", "Rectangle ABCD with AB labelled 8 cm and DA labelled 5 cm", 8, 5, "cm")
    L("a1-w3", "An L-shape ABCDEF with AB 10 cm, BC 4 cm, EF 4 cm and FA 7 cm; CD is marked a and DE is marked b",
      [("A", (0, 0)), ("B", (10, 0)), ("C", (10, 4)), ("D", (4, 4)), ("E", (4, 7)), ("F", (0, 7))],
      {"AB": 10, "BC": 4, "CD": "a", "DE": "b", "EF": 4, "FA": 7}, "cm", answers={"a": 6, "b": 3})
    tiles("a1-f1", "A rectangular path 8 paving stones long and 2 stones wide, with every stone drawn",
          [(0, 0), (8, 0), (8, 2), (0, 2)], rect_cells(8, 2))
    assert edge_count(rect_cells(8, 2)) == 16
    rect("a1-f2", "Rectangle PQRS with PQ labelled 9 cm and SP labelled 3 cm", 9, 3, "cm", letters="PQRS")
    L("a1-f3", "An L-shape ABCDEF with AB 9 cm, BC 2 cm, EF 5 cm and FA 7 cm; CD is marked a and DE is marked b",
      [("A", (0, 0)), ("B", (9, 0)), ("C", (9, 2)), ("D", (5, 2)), ("E", (5, 7)), ("F", (0, 7))],
      {"AB": 9, "BC": 2, "CD": "a", "DE": "b", "EF": 5, "FA": 7}, "cm", answers={"a": 4, "b": 5})
    lcells = {(x, y) for x in range(7) for y in range(2)} | {(x, 2) for x in range(3)}
    tiles("a1-p1", "An L-shaped patio of square paving stones: two rows of 7 stones, with a row of 3 stones on top at the left, every stone drawn",
          [(0, 0), (7, 0), (7, 2), (3, 2), (3, 3), (0, 3)], lcells)
    assert edge_count(lcells) == 15 and perim([(0, 0), (7, 0), (7, 2), (3, 2), (3, 3), (0, 3)]) == 20
    hexa = [(round(7 * math.cos(math.radians(60 * k)), 2), round(7 * math.sin(math.radians(60 * k)), 2)) for k in range(6)]
    letters = "ABCDEF"
    poly("a1-p2", "A hexagon ABCDEF with all six sides marked equal and AB labelled 7 cm",
         list(zip(letters, hexa)), {"AB": "7 cm"}, ticks=[(letters[i] + letters[(i + 1) % 6], 1) for i in range(6)])
    L("a1-p5", "An L-shape ABCDEF with AB 12 cm, BC 5 cm, EF 7 cm and FA 9 cm; CD and DE are not labelled",
      [("A", (0, 0)), ("B", (12, 0)), ("C", (12, 5)), ("D", (7, 5)), ("E", (7, 9)), ("F", (0, 9))],
      {"AB": 12, "BC": 5, "EF": 7, "FA": 9}, "cm")
    assert perim([(0, 0), (12, 0), (12, 5), (7, 5), (7, 9), (0, 9)]) == 42
    rect("a1-p6-A", "Shape A, a rectangle with sides labelled 6 cm and 3 cm", 6, 3, "cm", label_all=True)
    lb = [(0, 0), (5, 0), (5, 2), (2, 2), (2, 4), (0, 4)]
    L("a1-p6-B", "Shape B, an L-shape with its six sides labelled 5 cm, 2 cm, 3 cm, 2 cm, 2 cm and 4 cm",
      list(zip("ABCDEF", lb)), {"AB": 5, "BC": 2, "CD": 3, "DE": 2, "EF": 2, "FA": 4}, "cm")
    assert perim(lb) == 18
    tiles("a1-d1", "A rectangular patio 7 paving stones long and 4 stones wide, with every stone drawn",
          [(0, 0), (7, 0), (7, 4), (0, 4)], rect_cells(7, 4))
    assert edge_count(rect_cells(7, 4)) == 18

    # ================= Activity 02: area of rectangles and triangles =================
    rect("a2-review", "Rectangle ABCD with AB labelled 11 m and DA labelled 4 m", 11, 4, "m")
    tiles("a2-w1", "A rectangle 7 cm long and 2 cm wide, divided into 1 cm squares",
          [(0, 0), (7, 0), (7, 2), (0, 2)], rect_cells(7, 2),
          labels=[((0, 0), (7, 0), "7 cm"), ((0, 2), (0, 0), "2 cm")])
    fig("a2-w2", "Two garden beds: a rectangle labelled 9 m by 1 m, and a square labelled 5 m by 5 m",
        ["polygon (0,0) (9,0) (9,1) (0,1)", 'side (0,0) (9,0) "9 m"', 'side (0,1) (0,0) "1 m"',
         "polygon (11,0) (16,0) (16,5) (11,5)", 'side (11,0) (16,0) "5 m"', 'side (16,0) (16,5) "5 m"'])
    right_tri("a2-w3", "Right-angled triangle ABC with AB 7 cm and BC 6 cm, inside a dashed rectangle", 7, 6, "cm", box=True)
    tri_height("a2-w4", "Triangle ABC with base AB 10 cm, side BC 13 cm, and a dashed height from C to AB of 12 cm",
               10, (5, 12), "cm")
    rect("a2-f1", "A rectangular deck ABCD with AB labelled 7 m and DA labelled 4 m", 7, 4, "m")
    right_tri("a2-f2", "Right-angled triangle ABC with AB 8 cm and BC 5 cm, inside a dashed rectangle", 8, 5, "cm", box=True)
    tri_height("a2-f3", "Triangle ABC with base AB 16 cm, side BC 10 cm, and a dashed height from C to AB of 6 cm",
               16, (8, 6), "cm")
    rect("a2-p1", "Rectangle ABCD with AB labelled 9 cm and DA labelled 7 cm", 9, 7, "cm")
    right_tri("a2-p2", "Right-angled triangle ABC with AB 10 cm and BC 7 cm", 10, 7, "cm")
    tri_height("a2-p3", "Triangle ABC with base AB 18 cm, side AC 15 cm, and a dashed height from C to AB of 12 cm",
               18, (9, 12), "cm", label_slants=("AC",))
    tri_height("a2-p6", "Triangle ABC with base AB 14 cm, sides AC 13 cm and BC 15 cm, and a dashed height from C to AB of 12 cm",
               14, (5, 12), "cm", label_slants=("AC", "BC"))
    right_tri("a2-d1", "Right-angled triangle ABC with AB 9 cm and BC 6 cm", 9, 6, "cm")

    # ================= Activity 03: composite area =================
    right_tri("a3-review", "Right-angled triangle ABC with AB 12 cm and BC 5 cm", 12, 5, "cm")
    L("a3-w1", "An L-shaped deck ABCDEF with AB 6 m, BC 2 m, EF 2 m and FA 5 m, split by a dashed line into two rectangles",
      [("A", (0, 0)), ("B", (6, 0)), ("C", (6, 2)), ("D", (2, 2)), ("E", (2, 5)), ("F", (0, 5))],
      {"AB": 6, "BC": 2, "EF": 2, "FA": 5}, "m", dashed=[((2, 2), (0, 2))])
    house("a3-w2", "A shape ABCDE: rectangle ABCE with a triangle CDE on top, AB 8 cm, BC 4 cm, CD 5 cm, a dashed line EC, and a dashed height from D to AB of 7 cm",
          8, 4, 7, "cm")
    L("a3-f1", "An L-shape ABCDEF with AB 9 cm, BC 2 cm, EF 3 cm and FA 8 cm, split by a dashed line into two rectangles",
      [("A", (0, 0)), ("B", (9, 0)), ("C", (9, 2)), ("D", (3, 2)), ("E", (3, 8)), ("F", (0, 8))],
      {"AB": 9, "BC": 2, "EF": 3, "FA": 8}, "cm", dashed=[((3, 2), (0, 2))])
    house("a3-f2", "A shape ABCDE: rectangle ABCE with a triangle CDE on top, AB 6 cm, BC 6 cm, CD 5 cm, a dashed line EC, and a dashed height from D to AB of 10 cm",
          6, 6, 10, "cm")
    L("a3-f3", "An L-shape ABCDEF with AB 11 m, BC 7 m, CD 4 m and FA 3 m, split by a dashed line into two rectangles",
      [("A", (0, 0)), ("B", (11, 0)), ("C", (11, 7)), ("D", (7, 7)), ("E", (7, 3)), ("F", (0, 3))],
      {"AB": 11, "BC": 7, "CD": 4, "FA": 3}, "m", dashed=[((7, 3), (11, 3))])
    L("a3-p1", "An L-shape ABCDEF with AB 11 cm, BC 4 cm, EF 6 cm and FA 9 cm",
      [("A", (0, 0)), ("B", (11, 0)), ("C", (11, 4)), ("D", (6, 4)), ("E", (6, 9)), ("F", (0, 9))],
      {"AB": 11, "BC": 4, "EF": 6, "FA": 9}, "cm")
    poly("a3-p2", "A shape ABCD: AB 10 cm along the bottom, DA 4 cm, DC 7 cm along the top and a slanted side BC 5 cm, with a dashed line from C down to AB",
         [("A", (0, 0)), ("B", (10, 0)), ("C", (7, 4)), ("D", (0, 4))],
         {"AB": "10 cm", "BC": "5 cm", "DC": "7 cm", "DA": "4 cm"}, rights=["DAB", "CDA"],
         dashed=[((7, 4), (7, 0))], right_coords=[((7, 4), (7, 0), (10, 0))])
    L("a3-p3", "An L-shaped playground ABCDEF with AB 12 m, BC 3 m, EF 4 m and FA 8 m",
      [("A", (0, 0)), ("B", (12, 0)), ("C", (12, 3)), ("D", (4, 3)), ("E", (4, 8)), ("F", (0, 8))],
      {"AB": 12, "BC": 3, "EF": 4, "FA": 8}, "m")
    house("a3-p4", "The front of a birdhouse ABCDE: rectangle ABCE with a triangle CDE on top, AB 16 cm, BC 9 cm, CD 10 cm, and a dashed height from D to AB of 15 cm",
          16, 9, 15, "cm", split=False)
    L("a3-p5", "An L-shape ABCDEF with AB 7 cm, BC 2 cm, EF 3 cm and FA 7 cm",
      [("A", (0, 0)), ("B", (7, 0)), ("C", (7, 2)), ("D", (3, 2)), ("E", (3, 7)), ("F", (0, 7))],
      {"AB": 7, "BC": 2, "EF": 3, "FA": 7}, "cm")
    house("a3-d1", "A shape ABCDE: rectangle ABCE with a triangle CDE on top, AB 12 cm, BC 6 cm, CD 10 cm, and a dashed height from D to AB of 14 cm",
          12, 6, 14, "cm", split=False)

    # ================= Activity 04: volume of cuboids =================
    L("a4-review", "An L-shape ABCDEF with AB 8 cm, BC 3 cm, EF 3 cm and FA 6 cm",
      [("A", (0, 0)), ("B", (8, 0)), ("C", (8, 3)), ("D", (3, 3)), ("E", (3, 6)), ("F", (0, 6))],
      {"AB": 8, "BC": 3, "EF": 3, "FA": 6}, "cm")
    cuboid("a4-w1", "A cuboid 4 cm long, 3 cm wide and 2 cm high, built from 1 cm cubes", 4, 3, 2, units=True)
    cuboid("a4-w2", "A cuboid 2 cm long, 2 cm wide and 5 cm high, built from 1 cm cubes", 2, 2, 5, units=True)
    cuboid("a4-w3-1", "Box 1, a cube 40 cm long, 40 cm wide and 40 cm high", 40, 40, 40)
    cuboid("a4-w3-2", "Box 2, a cuboid 80 cm long, 20 cm wide and 40 cm high", 80, 20, 40)
    cuboid("a4-f1", "A cuboid 6 cm long, 2 cm wide and 3 cm high, built from 1 cm cubes", 6, 2, 3, units=True)
    cuboid("a4-f2", "A cuboid 5 cm long, 4 cm wide and 3 cm high", 5, 4, 3)
    cuboid("a4-f3", "A cube 5 cm long, 5 cm wide and 5 cm high", 5, 5, 5)
    cuboid("a4-p1", "A cuboid 7 cm long, 2 cm wide and 4 cm high, built from 1 cm cubes", 7, 2, 4, units=True)
    cuboid("a4-p2", "A cuboid 8 cm long, 5 cm wide and 2 cm high", 8, 5, 2)
    cuboid("a4-p5", "A box 6 cm long, 5 cm wide and 2 cm high", 6, 5, 2)
    cuboid("a4-d1", "A box 4 cm long, 4 cm wide and 3 cm high", 4, 4, 3)

    # ================= Activity 05: consolidation =================
    cuboid("a5-review", "A cuboid 6 cm long, 4 cm wide and 5 cm high", 6, 4, 5)
    cuboid("a5-w1", "A gift box 20 cm long, 10 cm wide and 5 cm high", 20, 10, 5)
    cuboid("a5-f1", "A sandpit 3 m long, 2 m wide and 0.5 m deep", 3, 2, 0.5, unit="m")
    L("a5-p4", "An L-shaped room ABCDEF with AB 6 m, BC 3 m, EF 4 m and FA 5 m",
      [("A", (0, 0)), ("B", (6, 0)), ("C", (6, 3)), ("D", (4, 3)), ("E", (4, 5)), ("F", (0, 5))],
      {"AB": 6, "BC": 3, "EF": 4, "FA": 5}, "m")
    cuboid("a5-d1", "A fish tank 50 cm long, 30 cm wide and 40 cm high", 50, 30, 40)
