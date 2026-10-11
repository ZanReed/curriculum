"""chain.geom.nets (715-): nets of cubes, cuboids, prisms and pyramids.

Every net is defined as a list of flat faces (polygons in the net's plane), and every claim the
activity makes about a net is checked here by FOLDING it, at build time: fold() maps each face
across its hinges (the sides it shares with a neighbouring face) onto the faces of the actual
solid, and a net folds only when every face of the solid is covered exactly once, with the side
lengths matching where faces meet. Each figure states what it claims ("folds", "overlap" or
"missing"), and define() fails if the fold disagrees. The checker is proved at import against
the known count: exactly 11 of the 35 shapes made of six squares fold into a cube.

Solids have no figure primitive except the cuboid, so prisms and pyramids are named in words;
only their nets, which are flat, are drawn. Faces are drawn as separate polygons, so the fold
lines show as the lines between them. Built by tools/figs/build.py; see tools/figs/core.py.
"""
import math
from collections import deque

from core import FIGS, ANS, P, f, fig  # noqa: F401

EPS = 0.02  # net coordinates are rounded to 2 places by f(); 1-unit faces need this slack


# ---- solids, as outward-facing 3D face cycles ---------------------------------------------
def _oriented(face, centre):
    """Return the 3D cycle ordered anticlockwise as seen from outside (away from centre)."""
    a, b, c = face[0], face[1], face[2]
    u = [b[i] - a[i] for i in range(3)]
    v = [c[i] - a[i] for i in range(3)]
    n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    out = [a[i] - centre[i] for i in range(3)]
    return list(face) if sum(n[i] * out[i] for i in range(3)) > 0 else list(reversed(face))


def _solid(faces):
    pts = [p for fc in faces for p in fc]
    centre = tuple(sum(p[i] for p in pts) / len(pts) for i in range(3))
    return [_oriented(fc, centre) for fc in faces]


def cuboid(l, w, h):
    v = {(x, y, z): (x * l, y * w, z * h) for x in (0, 1) for y in (0, 1) for z in (0, 1)}
    quads = [
        [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],
        [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)], [(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)],
        [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)], [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)],
    ]
    return _solid([[v[k] for k in q] for q in quads])


def prism(end, length):
    """end: the end polygon in 2D; the prism runs `length` along z."""
    bottom = [(x, y, 0.0) for x, y in end]
    top = [(x, y, float(length)) for x, y in end]
    n = len(end)
    sides = [[bottom[i], bottom[(i + 1) % n], top[(i + 1) % n], top[i]] for i in range(n)]
    return _solid([bottom, top] + sides)


def pyramid(base, slant_height):
    """base: a regular polygon in 2D, centred on the origin; slant_height: the height of each
    triangular face, measured on the face (what the net shows)."""
    n = len(base)
    inr = math.dist((0, 0), ((base[0][0] + base[1][0]) / 2, (base[0][1] + base[1][1]) / 2))
    h = math.sqrt(slant_height ** 2 - inr ** 2)
    apex = (0.0, 0.0, h)
    b3 = [(x, y, 0.0) for x, y in base]
    tris = [[b3[i], b3[(i + 1) % n], apex] for i in range(n)]
    return _solid([b3] + tris)


def regular(n, side, start_deg=-90):
    """A regular n-gon with the given side, centred on the origin, one side along the bottom."""
    r = side / (2 * math.sin(math.pi / n))
    first = start_deg - 180 / n
    return [P(r, first + 360 * k / n) for k in range(n)]


# ---- folding ------------------------------------------------------------------------------
def _ccw(poly):
    area = sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1]
               for i in range(len(poly)))
    return list(poly) if area > 0 else list(reversed(poly))


def _key(p):
    return (round(p[0], 2), round(p[1], 2))


def _congruent(flat, solid_face, offset):
    k = len(flat)
    if len(solid_face) != k:
        return False
    for i in range(k):
        for j in range(i + 1, k):
            d2 = math.dist(flat[i], flat[j])
            d3 = math.dist(solid_face[(i + offset) % k], solid_face[(j + offset) % k])
            if abs(d2 - d3) > EPS:
                return False
    return True


def _hinges(faces):
    """(face a, side index i, face b, side index j) for every side two faces share."""
    edges = {}
    for a, fc in enumerate(faces):
        for i in range(len(fc)):
            edges.setdefault((_key(fc[i]), _key(fc[(i + 1) % len(fc)])), []).append((a, i))
    out = []
    for (p, q), owners in edges.items():
        for a, i in owners:
            for b, j in edges.get((q, p), []):
                if a < b:
                    out.append((a, i, b, j))
    return out


def _attempt(faces, solid, start_face, start_offset):
    """BFS from face 0 placed on solid face start_face. Returns (status, mapping)."""
    mapping = {0: (start_face, start_offset)}
    used = {start_face: 0}
    hinges = _hinges(faces)
    adj = {}
    for a, i, b, j in hinges:
        adj.setdefault(a, []).append((i, b, j))
        adj.setdefault(b, []).append((j, a, i))
    q = deque([0])
    while q:
        a = q.popleft()
        sa, oa = mapping[a]
        k = len(faces[a])
        for i, b, j in adj.get(a, []):
            # a's side i runs P -> Q; on the solid that is A -> B; b's side j runs Q -> P
            A = solid[sa][(i + oa) % k]
            B = solid[sa][(i + 1 + oa) % k]
            target = None
            for s, sf in enumerate(solid):
                if s == sa:
                    continue
                m = len(sf)
                for t in range(m):
                    if sf[t] == B and sf[(t + 1) % m] == A:
                        target = (s, (t - j) % m)
            if target is None:
                return "overlap", mapping
            if not _congruent(faces[b], solid[target[0]], target[1]):
                return "overlap", mapping
            if b in mapping:
                if mapping[b] != target:
                    return "overlap", mapping
                continue
            if target[0] in used:
                return "overlap", mapping
            mapping[b] = target
            used[target[0]] = b
            q.append(b)
    if len(mapping) < len(faces):
        return "overlap", mapping  # a face not joined to the rest: not one net
    if len(mapping) < len(solid):
        return "missing", mapping
    return "folds", mapping


def fold(faces, solid):
    """'folds' if the net folds into the solid; 'missing' if it folds without overlap but leaves
    faces of the solid uncovered; 'overlap' if two faces land on the same place (or a side
    meets a side of a different length)."""
    faces = [_ccw(fc) for fc in faces]
    results = set()
    for orient in (solid, [list(reversed(fc)) for fc in solid]):
        for s, sf in enumerate(orient):
            for o in range(len(sf)):
                if _congruent(faces[0], sf, o):
                    status, _ = _attempt(faces, orient, s, o)
                    if status == "folds":
                        return "folds"
                    results.add(status)
    if len(faces) > len(solid):
        return "overlap"
    return "missing" if results == {"missing"} else "overlap"


# ---- the self-test: 11 cube nets among the 35 hexominoes -------------------------------------
def squares(cells, size=1.0, origin=(0.0, 0.0)):
    ox, oy = origin
    return [[(ox + x * size, oy + y * size), (ox + (x + 1) * size, oy + y * size),
             (ox + (x + 1) * size, oy + (y + 1) * size), (ox + x * size, oy + (y + 1) * size)]
            for x, y in cells]


def _canon(cells):
    best = None
    for _ in range(2):
        for _ in range(4):
            cells = [(y, -x) for x, y in cells]
            mx, my = min(c[0] for c in cells), min(c[1] for c in cells)
            norm = tuple(sorted((x - mx, y - my) for x, y in cells))
            best = norm if best is None or norm < best else best
        cells = [(-x, y) for x, y in cells]
    return best


def _hexominoes():
    shapes = {_canon([(0, 0)])}
    for _ in range(5):
        grown = set()
        for s in shapes:
            for x, y in s:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (x + dx, y + dy)
                    if c not in s:
                        grown.add(_canon(list(s) + [c]))
        shapes = grown
    return shapes


def _self_test():
    hexes = _hexominoes()
    cube = cuboid(1, 1, 1)
    good = [h for h in hexes if fold(squares(h), cube) == "folds"]
    assert len(hexes) == 35 and len(good) == 11, (len(hexes), len(good))


_self_test()

CUBE = cuboid(1, 1, 1)


# ---- drawing ------------------------------------------------------------------------------
def centroid(poly):
    return (round(sum(p[0] for p in poly) / len(poly), 2), round(sum(p[1] for p in poly) / len(poly), 2))


def draw(faces, labels=None, shaded=(), sides=()):
    """Each face as a polygon (so the fold lines are the lines between faces); optional text in
    each face; shaded: extra regions (candidate positions, a "?" face) with their text; sides:
    [((x,y), (x,y), "3 cm")]."""
    lines = ["polygon " + " ".join(f(p) for p in fc) for fc in faces]
    for fc, lab in zip(faces, labels or []):
        if lab:
            lines.append(f'text {f(centroid(fc))} "{lab}"')
    for poly, lab in shaded:
        lines.append("region " + " ".join(f(p) for p in poly))
        lines.append(f'text {f(centroid(poly))} "{lab}"')
    for p, q, lab in sides:
        lines.append(f'side {f(p)} {f(q)} "{lab}"')
    return lines


def net(name, alt, faces, solid, claim, labels=None, shaded=(), sides=(), extra=()):
    got = fold(faces, solid)
    assert got == claim, f"{name}: claimed {claim}, folds as {got}"
    fig(name, alt, draw(faces, labels, shaded, sides), extra=extra)


def choice(name, letter, alt, faces, solid, claim):
    """A net in a `figure: X` column (no caption: line; the column's own letter is the caption)."""
    got = fold(faces, solid)
    assert got == claim, f"{name}: claimed {claim}, folds as {got}"
    FIGS[name] = [f"alt: {alt}", *draw(faces)]
    FIGS[name + "@letter"] = letter


def completes(name, partial, candidate, solid, claim):
    """Check one candidate position for the missing face of a partial net."""
    got = fold(partial + [candidate], solid)
    assert got == claim, f"{name}: candidate claimed {claim}, folds as {got}"


# ---- nets used by the activity --------------------------------------------------------------
CROSS = [(1, 3), (1, 2), (1, 1), (1, 0), (0, 2), (2, 2)]  # column of four, arms on the 2nd from top
ROW = [(i, 0) for i in range(6)]


def tri_up(a, b, height):
    """An isosceles triangle on side a -> b, with its point `height` to the left of a -> b."""
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    return [a, b, (round(mx + nx * height, 2), round(my + ny * height, 2))]


def rect(x0, y0, w, h):
    return [(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)]


EQ = round(math.sqrt(3), 2)  # height of an equilateral triangle with side 2


def a1():
    # ---- review: name the shape (polygons that nets are made of) ----
    for name, letter, n, alt in (("a1-r-A", "A", 6, "A shape with six equal straight sides"),
                                 ("a1-r-B", "B", 5, "A shape with five equal straight sides"),
                                 ("a1-r-C", "C", 4, "A shape with four equal straight sides and four square corners")):
        FIGS[name] = [f"alt: {alt}", "polygon " + " ".join(f(p) for p in regular(n, 2))]
        FIGS[name + "@letter"] = letter

    # ---- worked 1 and 2: the hook's pair ----
    net("a1-w1", "Six squares numbered 1 to 6: a column of four (1 at the top, then 2, 3 and 4), "
        "with square 5 on the left of square 2 and square 6 on its right",
        squares(CROSS), CUBE, "folds", labels=["1", "2", "3", "4", "5", "6"])
    net("a1-w2", "Six squares numbered 1 to 6 in one long row",
        squares(ROW), CUBE, "overlap", labels=["1", "2", "3", "4", "5", "6"])

    # ---- worked 3: triangular prism (rectangles 2 by 4, equilateral ends of side 2) ----
    band = [rect(0, 0, 2, 4), rect(2, 0, 2, 4), rect(4, 0, 2, 4)]
    ends = [[(2, 4), (4, 4), (3, round(4 + EQ, 2))], [(2, 0), (3, round(-EQ, 2)), (4, 0)]]
    tprism = prism([(0, 0), (2, 0), (1, EQ)], 4)
    net("a1-w3", "Three rectangles side by side, each 2 cm wide and 4 cm tall, with a triangle "
        "on the top of the middle rectangle and another on its bottom",
        band + ends, tprism, "folds",
        sides=[((0, 0), (0, 4), "4 cm"), ((0, 4), (2, 4), "2 cm"),
               ((4, 4), (3, round(4 + EQ, 2)), "2 cm")])

    # ---- worked 4: square-based pyramid (square side 2, triangles of height 2 on the face) ----
    sq = rect(0, 0, 2, 2)
    tris = [[(0, 0), (1, -2), (2, 0)], [(2, 0), (4, 1), (2, 2)], [(2, 2), (1, 4), (0, 2)],
            [(0, 2), (-2, 1), (0, 0)]]
    spyr = pyramid(regular(4, 2, start_deg=-90), 2)
    net("a1-w4", "A square with a triangle on each of its four sides, all four triangles the same",
        [sq] + tris, spyr, "folds", labels=["", "", "", "", ""])

    # ---- faded 1: complete a cube net (positions A to D for the sixth square) ----
    part = [(1, 3), (1, 2), (1, 1), (1, 0), (0, 2)]
    cand = {"A": (2, 1), "B": (1, 4), "C": (-1, 2), "D": (0, 0)}
    claims = {"A": "folds", "B": "overlap", "C": "overlap", "D": "overlap"}
    for k, c in cand.items():
        completes(f"a1-f1 {k}", squares(part), squares([c])[0], CUBE, claims[k])
    net("a1-f1", "Five squares: a column of four, with one more square on the left of the second "
        "square from the top, and four shaded squares lettered A, B, C and D around them",
        squares(part), CUBE, "missing",
        shaded=[(squares([c])[0], k) for k, c in cand.items()])

    # ---- faded 2: complete a cuboid net (cuboid 3 by 2 by 1; the missing face is 2 by 1) ----
    cub = [rect(0, 0, 3, 2), rect(0, -1, 3, 1), rect(0, 2, 3, 1), rect(0, 3, 3, 2), rect(-1, 0, 1, 2)]
    hole = rect(3, 0, 1, 2)
    C321 = cuboid(3, 2, 1)
    fig("a1-f2c", "A cuboid 3 cm long, 2 cm wide and 1 cm high", ["cuboid 3 2 1 cm"])
    completes("a1-f2 hole", cub, hole, C321, "folds")
    completes("a1-f2 3x1", cub, rect(3, 0, 1, 3), C321, "overlap")  # a 3 by 1 piece doesn't fit
    net("a1-f2", "Five rectangles of a net, with a shaded gap marked ? on the right of the "
        "3 cm by 2 cm rectangle in the middle",
        cub, C321, "missing", shaded=[(hole, "?")],
        sides=[((0, -1), (3, -1), "3 cm"), ((-1, 0), (-1, 2), "2 cm"), ((0, -1), (0, 0), "1 cm")])

    # ---- faded 3: a pentagonal prism net with a rectangle missing ----
    s = 1.5
    pent = regular(5, s)
    pp = prism(pent, 3)
    band = [rect(i * s, 0, s, 3) for i in range(4)]
    # the pentagon on the top of the second rectangle, and on the bottom of the same rectangle
    top = _place_polygon(pent, (s, 3), (2 * s, 3))
    bot = _place_polygon(pent, (2 * s, 0), (s, 0))
    net("a1-f3", "Four rectangles side by side, each 1.5 cm wide and 3 cm tall, with a pentagon "
        "on the top of the second rectangle and another on its bottom",
        band + [top, bot], pp, "missing")

    # ---- independent 1: select all that fold into a cube ----
    pick = {
        "A": ([(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)], "folds"),   # column of four, arms opposite ends
        "B": ([(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)], "overlap"),  # 2 by 3 block
        "C": ([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)], "folds"),   # staircase of twos
        "D": ([(1, 0), (1, 1), (1, 2), (1, 3), (0, 0), (0, 3)], "overlap"),  # both arms on one side
    }
    alts = {
        "A": "Six squares: a column of four, with one square on the left of the bottom square and one on the right of the top square, diagram A",
        "B": "Six squares in a block, two rows of three, diagram B",
        "C": "Six squares in a staircase: three steps, each two squares wide, diagram C",
        "D": "Six squares: a column of four, with one square on the left of the bottom square and one on the left of the top square, diagram D",
    }
    for k, (cells, claim) in pick.items():
        choice(f"a1-p1-{k}", k, alts[k], squares(cells), CUBE, claim)

    # ---- independent 3: which is a triangular prism net? ----
    band3 = [rect(0, 0, 2, 4), rect(2, 0, 2, 4), rect(4, 0, 2, 4)]
    t_top = lambda x: [(x, 4), (x + 2, 4), (x + 1, round(4 + EQ, 2))]  # noqa: E731
    t_bot = lambda x: [(x, 0), (x + 1, round(-EQ, 2)), (x + 2, 0)]  # noqa: E731
    tp = {
        "A": (band3 + [t_top(0), t_bot(4)], "folds"),
        "B": (band3 + [t_top(0), t_top(4)], "overlap"),
        "C": (band3[:2] + [t_top(0), t_bot(2)], "missing"),
    }
    tp_alt = {
        "A": "Three rectangles side by side, a triangle on the top of the left rectangle and a triangle on the bottom of the right rectangle, diagram A",
        "B": "Three rectangles side by side, a triangle on the top of the left rectangle and a triangle on the top of the right rectangle, diagram B",
        "C": "Two rectangles side by side, a triangle on the top of the left rectangle and a triangle on the bottom of the right rectangle, diagram C",
    }
    for k, (fcs, claim) in tp.items():
        choice(f"a1-p3-{k}", k, tp_alt[k], fcs, tprism, claim)

    # ---- independent 4: the cuboid Ana's net is meant to make ----
    fig("a1-p4", "A cuboid 4 cm long, 3 cm wide and 2 cm high", ["cuboid 4 3 2 cm"])
    C432 = cuboid(4, 3, 2)
    good = [rect(0, 0, 4, 3), rect(0, -2, 4, 2), rect(0, 3, 4, 2), rect(0, 5, 4, 3),
            rect(-2, 0, 2, 3), rect(4, 0, 2, 3)]
    assert fold(good, C432) == "folds"
    ana = good[:4] + [rect(-1, 0, 1, 3), rect(4, 0, 1, 3)]  # her ends are 3 by 1
    assert fold(ana, C432) == "overlap", fold(ana, C432)

    # ---- independent 5: Tama's six squares (five in a column) ----
    tama = [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 2)]
    net("a1-p5", "Six squares: a column of five, with one more square on the left of the middle square",
        squares(tama), CUBE, "overlap")

    # ---- DoL: net P ----
    dolp = [(1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (2, 0)]
    net("a1-d1", "Net P: six squares, a column of four, with one square on the left of the top "
        "square and one on the right of the bottom square",
        squares(dolp), CUBE, "folds")
    # the counter-examples the rubric accepts, checked
    for cells in (ROW, [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)], tama):
        assert fold(squares(cells), CUBE) == "overlap"

    # ---- DoL review item: name the shape (an octagon) ----
    fig("a1-d2", "A shape with eight equal straight sides", ["polygon " + " ".join(f(p) for p in regular(8, 1.5))])


def _place_polygon(poly, a, b):
    """Copy a polygon so its first side lies on a -> b, with the polygon on the left of a -> b
    as it is in poly (poly anticlockwise, first side along the bottom)."""
    p0, p1 = poly[0], poly[1]
    ang0 = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    ang1 = math.atan2(b[1] - a[1], b[0] - a[0])
    t = ang1 - ang0
    out = []
    for x, y in poly:
        dx, dy = x - p0[0], y - p0[1]
        out.append((round(a[0] + dx * math.cos(t) - dy * math.sin(t), 2),
                    round(a[1] + dx * math.sin(t) + dy * math.cos(t), 2)))
    return out


def define():
    a1()
    # column figures carry their letter in the placeholder text, not in a caption: line
    for k in [k for k in FIGS if k.endswith("@letter")]:
        FIGS.pop(k)
