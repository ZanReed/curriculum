"""chain.geom.parallel-lines (713-): angles where lines meet, and parallel lines crossed by a transversal.

Figures for the chain's activities, defined from their intended measurements. Built by
tools/figs/build.py; see tools/figs/core.py.
"""
import math

from core import FIGS, ANS, P, f, fig  # noqa: F401



# ---- activity 01: lines through a point O --------------------------------------------
def straight(name, alt, base, ray, given, x_label="x", letters="ABC", answers=None):
    """Straight line through O at direction `base`; a ray from O at base+ray.
    The given angle is between the line's forward end and the ray; x is the other one."""
    a, b, c = letters
    lines = [f'point {f(P(4, base + 180))} "{a}"', 'point (0,0) "O"', f'point {f(P(4, base))} "{b}"',
             f'point {f(P(4, base + ray))} "{c}"', f"segment {a} {b}", f"segment O {c}",
             f"angle {b}O{c} {given}°", f'angle {c}O{a} "{x_label}"']
    fig(name, alt, lines, answers or {x_label: 180 - ray})


def crossing(name, alt, base, cross, labels, letters="ABCD", answers=None):
    """Two straight lines through O: A-B at direction base, C-D at base+cross.
    labels maps an angle name (e.g. 'BOC') to a label string."""
    a, b, c, d = letters
    lines = [f'point {f(P(4, base + 180))} "{a}"', f'point {f(P(4, base))} "{b}"',
             f'point {f(P(4, base + cross))} "{c}"', f'point {f(P(4, base + cross + 180))} "{d}"',
             'point (0,0) "O"', f"segment {a} {b}", f"segment {c} {d}"]
    lines += [f"angle {k} {v}" for k, v in labels.items()]
    fig(name, alt, lines, answers)


def right_split(name, alt, base, part, letters="ABC", answers=None):
    """A right angle AOB at O (OA at base, OB at base+90), split by OC at base+part."""
    a, b, c = letters
    lines = ['point (0,0) "O"', f'point {f(P(4, base))} "{a}"', f'point {f(P(4, base + 90))} "{b}"',
             f'point {f(P(4, base + part))} "{c}"', f"segment O {a}", f"segment O {b}", f"segment O {c}",
             f"angle {a}O{b} right", f"angle {a}O{c} {part}°", f'angle {c}O{b} "x"']
    fig(name, alt, lines, answers or {"x": 90 - part})


def scale_angle(deg):
    return [f"segment (0,0) (4,0)", f"segment (0,0) {f(P(4, deg))}",
            f"angle (4,0) (0,0) {f(P(4, deg))}", "to scale"]


# ---- activity 02: a transversal crossing two lines ------------------------------------
POS = {"RA": ("D", "Q", "E"), "LA": ("C", "Q", "E"), "LB": ("C", "Q", "P"), "RB": ("D", "Q", "P")}
POSP = {"RA": ("B", "P", "Q"), "LA": ("A", "P", "Q"), "LB": ("A", "P", "F"), "RB": ("B", "P", "F")}


def angle_name(at, pos):
    return "".join((POS if at == "Q" else POSP)[pos])


def size(phi, pos):
    return phi if pos in ("RA", "LB") else 180 - phi


def transversal(name, alt, phi, labels, tilt=0.0, marked=True, extra=(), answers=None):
    """CD at y = 3 (top), AB through P = (3.5, 0) at direction `tilt` (bottom);
    the transversal crosses AB at P and CD at Q, rising at phi degrees.
    labels: list of (crossing 'Q'|'P', position 'RA'|'LA'|'LB'|'RB', label)."""
    p = (3.5, 0.0)
    q = (round(3.5 + 3 / math.tan(math.radians(phi)), 2), 3.0)
    e = P(1.6, phi, *q)
    fpt = P(1.6, phi + 180, *p)
    a = P(3.5, 180 + tilt, *p)
    b = P(6.5, tilt, *p)
    lines = ['point (0,3) "C"', 'point (10,3) "D"', f'point {f(a)} "A"', f'point {f(b)} "B"',
             f'point {f(q)} "Q"', f'point {f(p)} "P"', f'point {f(e)} "E"', f'point {f(fpt)} "F"',
             "segment C D", "segment A B", "segment E F"]
    if marked:
        lines.append("parallel CD AB")
    lines += [f"angle {angle_name(at, pos)} {lab}" for at, pos, lab in labels]
    fig(name, alt, lines, answers, extra)


def define():
    # Activity 01 -------------------------------------------------------------------
    scale = ["segment (0,0) (4,0)", f"segment (0,0) {f(P(4, 145))}",
             f"angle (4,0) (0,0) {f(P(4, 145))}", "to scale"]
    fig("a1-review", "An angle drawn to scale, with one arm pointing right from its corner", scale)
    straight("a1-w1", "Straight line AB through O, with ray OC making an angle of 140° with OB and angle x with OA",
             0, 140, 140)
    crossing("a1-w2", "Straight lines AB and CD crossing at O, with angle BOC 40°, angle AOC marked y and angle AOD marked x",
             0, 40, {"BOC": "40°", "COA": '"y"', "AOD": '"x"'}, answers={"x": 40, "y": 140})
    right_split("a1-w3", "A right angle AOB split by ray OC into angle AOC 35° and angle COB marked x", 0, 35)
    straight("a1-f1", "Straight line JK through O, with ray OL making an angle of 115° with OK and angle x with OJ",
             0, 115, 115, letters="JKL")
    crossing("a1-f2", "Straight lines JK and LM crossing at O, with angle KOL 75°, angle JOL marked y and angle JOM marked x",
             0, 75, {"KOL": "75°", "LOJ": '"y"', "JOM": '"x"'}, letters="JKLM", answers={"x": 75, "y": 105})
    right_split("a1-f3", "A right angle JOK split by ray OL into angle JOL 62° and angle LOK marked x", 0, 62, letters="JKL")
    crossing("a1-p1", "Straight lines PQ and RS crossing at O, with angle QOR 72° and angle POS marked x",
             20, 72, {"QOR": "72°", "POS": '"x"'}, letters="PQRS", answers={"x": 72})
    straight("a1-p2", "Straight line PQ through O, with ray OR making an angle of 58° with OQ and angle x with OP",
             -15, 58, 58, letters="PQR")
    right_split("a1-p3", "A right angle POQ split by ray OR into angle POR 34° and angle ROQ marked x", 30, 34, letters="PQR")
    crossing("a1-p4", "Straight lines PQ and RS crossing at O, with angle QOR 110° and angle ROP marked x",
             0, 110, {"QOR": "110°", "ROP": '"x"'}, letters="PQRS", answers={"x": 70})
    crossing("a1-p6", "Straight lines PQ and RS crossing at O, with angle QOR 50° and angle POS marked x",
             0, 50, {"QOR": "50°", "POS": '"x"'}, letters="PQRS", answers={"x": 50})
    straight("a1-d1", "Straight line PQ through O, with ray OR making an angle of 65° with OQ and angle x with OP",
             0, 65, 65, letters="PQR")
    for cap, deg in (("A", 25), ("B", 45), ("C", 70)):
        fig(f"a1-d2-{cap}", f"Angle {cap}, drawn to scale, with one arm pointing right from its corner",
            scale_angle(deg))

    # Activity 02 -------------------------------------------------------------------
    crossing("a2-review", "Straight lines JK and LM crossing at O, with angle KOL 64°, angle JOM marked x and angle JOL marked y",
             0, 64, {"KOL": "64°", "JOM": '"x"', "LOJ": '"y"'}, letters="JKLM", answers={"x": 64, "y": 116})
    pos7 = [("Q", "LA", "m"), ("Q", "LB", "n"), ("Q", "RB", "r"), ("P", "RA", "s"), ("P", "LA", "t"),
            ("P", "LB", "u"), ("P", "RB", "v")]
    transversal("a2-w1", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 50° and the other seven angles marked m, n, r, s, t, u and v",
                50, [("Q", "RA", "50°")] + [(c, p, f'"{l}"') for c, p, l in pos7],
                answers={l: size(50, p) for _, p, l in pos7})
    transversal("a2-w2", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 70° and angle APQ marked x",
                70, [("Q", "RA", "70°"), ("P", "LA", '"x"')], answers={"x": 110})
    transversal("a2-w3", "Lines CD and AB, not marked parallel and closer together on the right, crossed by EF at Q and P, with angle DQE 70° and angle BPQ marked x",
                70, [("Q", "RA", "70°"), ("P", "RA", '"x"')], tilt=8, marked=False, extra=("to scale",),
                answers={"x": 62})
    transversal("a2-f1", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 65° and angle BPQ marked x",
                65, [("Q", "RA", "65°"), ("P", "RA", '"x"')], answers={"x": 65})
    transversal("a2-f2", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle CQE 120° and angle APF marked x",
                60, [("Q", "LA", "120°"), ("P", "LB", '"x"')], answers={"x": 60})
    transversal("a2-f3", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 55° and angle APF marked x",
                55, [("Q", "RA", "55°"), ("P", "LB", '"x"')], answers={"x": 55})
    transversal("a2-p1", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 72° and angle BPQ marked x",
                72, [("Q", "RA", "72°"), ("P", "RA", '"x"')], answers={"x": 72})
    transversal("a2-p2", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 68° and angle BPF marked x",
                68, [("Q", "RA", "68°"), ("P", "RB", '"x"')], answers={"x": 112})
    transversal("a2-p3", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 40° and angle CQP marked x",
                40, [("Q", "RA", "40°"), ("Q", "LB", '"x"')], answers={"x": 40})
    transversal("a2-p4", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle BPF 115° and angle DQE marked x",
                65, [("P", "RB", "115°"), ("Q", "RA", '"x"')], answers={"x": 65})
    transversal("a2-p5", "Lines CD and AB, with no arrows, crossed by EF at Q and P, with angle DQE 70° and angle BPQ marked x",
                70, [("Q", "RA", "70°"), ("P", "RA", '"x"')], tilt=5, marked=False, answers={"x": 65})
    pos7b = pos7
    transversal("a2-p6", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle DQE 60° and the other seven angles marked m, n, r, s, t, u and v",
                60, [("Q", "RA", "60°")] + [(c, p, f'"{l}"') for c, p, l in pos7b],
                answers={l: size(60, p) for _, p, l in pos7b})
    transversal("a2-d1", "Parallel lines CD and AB crossed by transversal EF at Q and P, with angle APQ 125° and angle CQP marked x",
                55, [("P", "LA", "125°"), ("Q", "LB", '"x"')], answers={"x": 55})
    fig("a2-d2", "An angle drawn to scale, with one arm pointing right from its corner", scale_angle(155))
