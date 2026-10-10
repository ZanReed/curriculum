"""chain.geom.transformations (714-): translations, reflections and rotations on a coordinate grid.

Figures for the chain's activities, defined from the object's coordinates and the transformation,
never from typed image coordinates: every image is computed by the functions below, so a drawn
image can't drift from the transformation the text describes. Built by tools/figs/build.py; see
tools/figs/core.py.

The same functions are what the builder's graded-graph check uses to recompute each `answer:` and
`mistake:` image, so a figure and a graded item can't disagree about what a transformation does.
"""
import math
import re

from core import FIGS, ANS, P, f, fig  # noqa: F401

PRIME = "′"


# ---- the transformations ------------------------------------------------------------------
def translate(pts, dx, dy):
    return [(x + dx, y + dy) for x, y in pts]


def reflect(pts, mirror):
    """mirror: ('x', a) for the line x = a; ('y', b) for y = b; 'y=x'; 'y=-x'."""
    if mirror == "y=x":
        return [(y, x) for x, y in pts]
    if mirror == "y=-x":
        return [(-y, -x) for x, y in pts]
    axis, v = mirror
    if axis == "x":
        return [(2 * v - x, y) for x, y in pts]
    return [(x, 2 * v - y) for x, y in pts]


def rotate(pts, centre, quarter_turns_clockwise):
    """Rotate about centre by a multiple of 90°, clockwise for positive counts."""
    cx, cy = centre
    out = []
    for x, y in pts:
        a, b = x - cx, y - cy
        for _ in range(quarter_turns_clockwise % 4):
            a, b = b, -a  # a quarter turn clockwise: right -> down, up -> right
        out.append((cx + a, cy + b))
    return out


def swap(pts):
    """Each point written (y, x): mis.coord.axes-swapped."""
    return [(y, x) for x, y in pts]


# ---- drawing helpers ----------------------------------------------------------------------
def shape(pts, letters, prime=False):
    """Named points and the polygon through them."""
    names = [c + (PRIME if prime else "") for c in letters]
    lines = [f'point {f(p)} "{n}"' for p, n in zip(pts, names)]
    lines.append("polygon " + " ".join(names))
    return lines


def unnamed(pts):
    return ["polygon " + " ".join(f(p) for p in pts)]


def shaded(pts):
    return ["region " + " ".join(f(p) for p in pts)]


def window(lines, include=()):
    """An axes window round everything drawn, padded by one square and always including the
    origin. The platform's auto-fit hugs the drawing, so without this a grid can leave out both
    axes, and the coordinates the text refers to can't be read."""
    xs, ys = [0.0], [0.0]
    for m in re.finditer(r"\((-?[\d.]+),(-?[\d.]+)\)", " ".join(lines) + " " + " ".join(f(p) for p in include)):
        xs.append(float(m.group(1)))
        ys.append(float(m.group(2)))
    lo = lambda v: math.floor(min(v)) - 1  # noqa: E731
    hi = lambda v: math.ceil(max(v)) + 1  # noqa: E731
    return f"axes: {lo(xs)}..{hi(xs)}, {lo(ys)}..{hi(ys)}"


def grid(name, alt, lines, caption=None, include=()):
    """A coordinate figure. A choice figure (with a caption) is read by counting squares, since
    three or four to a row show no axis numbers, so it keeps the platform's auto-fit."""
    extra = ["plane: on"]
    if caption:
        extra.insert(0, f"caption: {caption}")
    else:
        extra.append(window(lines, include))
    fig(name, alt, lines, extra=extra)


def arrow(a, b):
    return f"segment {f(a)} {f(b)} arrow"


def mirror_line(mirror, lo=-8, hi=8):
    """A mirror line drawn as a dashed segment across the window (a figure has no infinite line)."""
    if mirror == "y=x":
        return f"segment {f((lo, lo))} {f((hi, hi))} dashed"
    if mirror == "y=-x":
        return f"segment {f((lo, -lo))} {f((hi, -hi))} dashed"
    axis, v = mirror
    if axis == "x":
        return f"segment {f((v, lo))} {f((v, hi))} dashed"
    return f"segment {f((lo, v))} {f((hi, v))} dashed"


# ---- activity 01: translation --------------------------------------------------------------
TRI = [(1, 1), (3, 2), (1, 4)]  # the worked examples' triangle ABC


def a1():
    grid("a1-r2", "A grid with one point P marked", ['point (4,-2) "P"'])

    img = translate(TRI, 5, 0)
    grid("a1-w1", "Triangle ABC and its image A′B′C′, with arrows from A to A′ and from C to C′",
         shape(TRI, "ABC") + shape(img, "ABC", prime=True)
         + [arrow(TRI[0], img[0]), arrow(TRI[2], img[2])])

    img = translate(TRI, 5, 3)
    grid("a1-w2", "Triangle ABC and its image A′B′C′, with an arrow from A to A′",
         shape(TRI, "ABC") + shape(img, "ABC", prime=True) + [arrow(TRI[0], img[0])])

    img = translate(TRI, -4, -2)
    grid("a1-w3", "Triangle ABC and its image A′B′C′ below and to the left of it",
         shape(TRI, "ABC") + shape(img, "ABC", prime=True))

    pqr = [(1, -3), (4, -3), (4, -1)]
    grid("a1-f1", "Triangle PQR, with an arrow from P to its image P′",
         shape(pqr, "PQR") + [f'point {f(translate(pqr, -2, 4)[0])} "P{PRIME}"',
                              arrow(pqr[0], translate(pqr, -2, 4)[0])], include=translate(pqr, -2, 4))

    klm = [(-4, 3), (-2, 3), (-4, 6)]
    grid("a1-f2", "Triangle KLM on a grid", shape(klm, "KLM"), include=translate(klm, 3, -5))

    wxyz = [(-5, 1), (-3, 1), (-3, 2), (-5, 2)]
    grid("a1-f3", "Rectangle WXYZ and its image W′X′Y′Z′ below and to the right of it",
         shape(wxyz, "WXYZ") + shape(translate(wxyz, 5, -3), "WXYZ", prime=True))

    rect = [(-6, 1), (-3, 1), (-3, 3), (-6, 3)]
    grid("a1-p5", "Rectangle DEFG and its image D′E′F′G′ to the right of it",
         shape(rect, "DEFG") + shape(translate(rect, 7, 0), "DEFG", prime=True))

    tri = [(-4, 2), (-2, 2), (-4, 5)]
    grid("a1-d1", "Triangle RST and its image R′S′T′ below and to the right of it",
         shape(tri, "RST") + shape(translate(tri, 4, -3), "RST", prime=True))


def slide(pts, mirror):
    """The image a student gets by sliding the shape to where its reflection belongs, without
    flipping it (mis.reflect.translates): the translation that gives the true image's extent."""
    axis, v = mirror
    if axis == "x":
        xs = [x for x, _ in pts]
        return translate(pts, 2 * v - min(xs) - max(xs), 0)
    ys = [y for _, y in pts]
    return translate(pts, 0, 2 * v - min(ys) - max(ys))


def label(mirror, at):
    """The mirror line's equation as free text beside it, with a true minus sign."""
    if isinstance(mirror, str):
        text = mirror.replace("=", " = ")
    else:
        text = f"{mirror[0]} = {mirror[1]}"
    text = text.replace("-", "\u2212")  # outside the f-string, so Python before 3.12 parses it
    return f'text {f(at)} "{text}"'


# ---- activity 02: reflection ---------------------------------------------------------------
TRI2 = [(-3, 1), (-1, 1), (-3, 5)]  # the worked examples' triangle ABC: scalene, and y - x even at
# every corner so diagonal steps to y = x come out whole


def a2():
    m = ("x", 0)
    grid("a2-w1", "Triangle ABC, a vertical dashed mirror line x = 0, and the image A′B′C′",
         shape(TRI2, "ABC") + shape(reflect(TRI2, m), "ABC", prime=True)
         + [mirror_line(m, -1, 6), label(m, (0.6, 6.4))])
    m = ("y", 0)
    grid("a2-w2", "Triangle ABC, a horizontal dashed mirror line y = 0, and the image A′B′C′",
         shape(TRI2, "ABC") + shape(reflect(TRI2, m), "ABC", prime=True)
         + [mirror_line(m, -6, 2), label(m, (1.2, 0.5))])
    m = "y=x"
    grid("a2-w3", "Triangle ABC, a diagonal dashed mirror line y = x, and the image A′B′C′",
         shape(TRI2, "ABC") + shape(reflect(TRI2, m), "ABC", prime=True)
         + [mirror_line(m, -5, 6), label(m, (6.3, 5.6))])

    pqr = [(1, 2), (4, 2), (1, 4)]
    m = ("x", -1)
    grid("a2-f1", "Triangle PQR and a vertical dashed mirror line x = −1",
         shape(pqr, "PQR") + [mirror_line(m, 0, 5), label(m, (-0.4, 5.4))], include=reflect(pqr, m))
    klm = [(-2, -1), (1, -1), (-2, -3)]
    m = ("y", 1)
    grid("a2-f2", "Triangle KLM and a horizontal dashed mirror line y = 1",
         shape(klm, "KLM") + [mirror_line(m, -4, 3), label(m, (3.6, 1))], include=reflect(klm, m))
    d = [(3, 1), (5, 1), (3, -3)]
    grid("a2-f3", "Triangle DEF and a diagonal dashed mirror line y = x",
         shape(d, "DEF") + [mirror_line("y=x", -4, 6), label("y=x", (5.6, 6.4))], include=reflect(d, "y=x"))

    tuv = [(-4, 1), (-2, 1), (-4, 4)]
    m = ("x", 0)
    grid("a2-p4", "Triangle TUV, a vertical dashed line x = 0, and a second triangle T′U′V′ to the right of the line",
         shape(tuv, "TUV") + shape(slide(tuv, m), "TUV", prime=True)
         + [mirror_line(m, 0, 5), label(m, (0.6, 5.4))])

    abc = [(-4, 0), (-2, 0), (-4, 4)]
    grid("a2-d1", "Triangle ABC, a diagonal dashed line y = x, and Tom's triangle A′B′C′",
         shape(abc, "ABC") + shape(reflect(abc, ("x", 0)), "ABC", prime=True)
         + [mirror_line("y=x", -5, 5), label("y=x", (4.6, 5.4))])


# ---- activity 03: rotation -----------------------------------------------------------------
TRI3 = [(2, 1), (4, 1), (2, 2)]  # the worked examples' triangle ABC
CEN3 = (1, 0)                    # their centre of rotation, P


def centre(c, name="P"):
    return f'point {f(c)} "{name}"'


def a3():
    for name, q, alt in (("a3-w1", 2, "a half turn"), ("a3-w2", 1, "a quarter turn clockwise"),
                         ("a3-w3", 3, "a quarter turn anticlockwise")):
        img = rotate(TRI3, CEN3, q)
        lines = shape(TRI3, "ABC") + shape(img, "ABC", prime=True) + [centre(CEN3)]
        lines += [f"segment P A dashed", f"segment P A{PRIME} dashed"]
        if q == 2:  # the same half turn about corner B, shaded: a different centre, a different place
            lines += shaded(rotate(TRI3, TRI3[1], 2))
        if q != 2:  # by coordinates: the figure checker reads a name like APA′ one letter at a time
            lines.append(f"angle {f(TRI3[0])} {f(CEN3)} {f(img[0])} right")
        extra_alt = ", and a shaded triangle, the same half turn about B" if q == 2 else ""
        grid(name, f"Triangle ABC, the centre P, and the image A′B′C′ after {alt} about P, "
                   f"with dashed lines from P to A and from P to A′{extra_alt}", lines)

    for name, letters, o, c, q in (("a3-f1", "KLM", [(2, 3), (4, 3), (2, 5)], (1, 1), 2),
                                   ("a3-f2", "TUV", [(0, 1), (2, 1), (0, 3)], (-1, 0), 1),
                                   ("a3-f3", "GHJ", [(-3, 1), (-3, 3), (-2, 1)], (-1, -1), 3)):
        grid(name, f"Triangle {letters} and the centre of rotation P", shape(o, letters) + [centre(c)],
             include=rotate(o, c, q))

    abc = [(-4, 1), (-2, 1), (-4, 3)]
    grid("a3-p5", "Triangle ABC, the centre of rotation P, and Liam's triangle",
         shape(abc, "ABC") + [centre((-1, 0))] + unnamed(rotate(abc, abc[0], 2)))

    abc = [(-3, 2), (-1, 2), (-3, 3)]
    grid("a3-d1", "Triangle ABC, the centre of rotation P, and Kiri's triangle A′B′C′",
         shape(abc, "ABC") + [centre((-2, 0))] + shape(rotate(abc, (0, 0), 1), "ABC", prime=True))


# ---- activity 04: which transformation? ----------------------------------------------------
TRI4 = [(1, 1), (3, 1), (1, 2)]  # the worked examples' triangle ABC (scalene: no line of symmetry)


def choice(name, caption, alt, obj, img):
    """A choice figure: the object outlined, its image shaded, no labels (read by counting squares)."""
    grid(name, alt, unnamed(obj) + shaded(img), caption=caption)


def a4():
    grid("a4-w1", "Triangle ABC above the x-axis and triangle A′B′C′ below it",
         shape(TRI4, "ABC") + shape(reflect(TRI4, ("y", 0)), "ABC", prime=True))
    grid("a4-w2", "Triangle ABC above the x-axis, triangle A′B′C′ below it, and the point P between them",
         shape(TRI4, "ABC") + shape(rotate(TRI4, (2, 0), 2), "ABC", prime=True) + [centre((2, 0))])
    grid("a4-w3", "Triangle ABC and triangle A′B′C′ to the right of it",
         shape(TRI4, "ABC") + shape(translate(TRI4, 4, -1), "ABC", prime=True))

    o = [(-4, 1), (-2, 1), (-4, 2)]
    grid("a4-f1", "Triangle ABC on the left of the y-axis and triangle A′B′C′ on the right of it",
         shape(o, "ABC") + shape(reflect(o, ("x", 0)), "ABC", prime=True))
    o = [(1, 2), (3, 2), (1, 3)]
    grid("a4-f2", "Triangle ABC, triangle A′B′C′ below and to the left of it, and the point P between them",
         shape(o, "ABC") + shape(rotate(o, (0, 1), 2), "ABC", prime=True) + [centre((0, 1))])
    o = [(-3, -1), (-1, -1), (-3, 1)]
    grid("a4-f3", "Triangle ABC and triangle A′B′C′ above and to the right of it",
         shape(o, "ABC") + shape(translate(o, 5, 2), "ABC", prime=True))

    o = [(0, 1), (3, 1), (0, 2)]
    choice("a4-p1-A", "A", "An outlined triangle and a shaded triangle directly below it, diagram A",
           o, reflect(o, ("y", 0)))
    choice("a4-p1-B", "B", "An outlined triangle and a shaded triangle directly below it, diagram B",
           o, rotate(o, (1.5, 0), 2))
    choice("a4-p1-C", "C", "An outlined triangle and a shaded triangle directly below it, diagram C",
           o, translate(o, 0, -3))

    o = [(1, 1), (3, 1), (1, 2)]
    grid("a4-p2", "Triangle ABC, the point P, and triangle A′B′C′ below it",
         shape(o, "ABC") + [centre((0, 0))] + shape(rotate(o, (0, 0), 1), "ABC", prime=True))

    o = [(-4, 1), (-2, 1), (-4, 3)]
    grid("a4-p5", "Triangle ABC, the point P, and triangle A′B′C′ below and to the right of it",
         shape(o, "ABC") + [centre((-1, 0))] + shape(rotate(o, (-1, 0), 2), "ABC", prime=True))

    o = [(1, 1), (1, 3), (2, 1)]
    choice("a4-p7-A", "A", "An outlined triangle and a shaded triangle to the left of it, diagram A",
           o, reflect(o, ("x", 0)))
    choice("a4-p7-B", "B", "An outlined triangle and a shaded triangle to the left of it, diagram B",
           o, rotate(o, (0, 2), 2))
    choice("a4-p7-C", "C", "An outlined triangle and a shaded triangle to the left of it, diagram C",
           o, translate(o, -3, 0))

    o = [(-3, 1), (-1, 1), (-3, 2)]
    grid("a4-d1", "Triangle ABC, the point P, and triangle A′B′C′ below it",
         shape(o, "ABC") + [centre((-1, 0))] + shape(rotate(o, (-1, 0), 3), "ABC", prime=True))


def define():
    a1()
    a2()
    a3()
    a4()
