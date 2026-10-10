"""Check every figure in a draft against what its labels claim.

Rebuilt 2026-10-07 for the angle chains; extended 2026-10-08 for chain.measure.area-volume with
length checks. For each ```figure fence and each `figure:` column:
- every line is one the shipped grammar knows (a mistyped line refuses the whole file);
- alt: is present;
- angles: a degree label is drawn within 1° of its value; `right` within 1° of 90°; a quoted
  label is checked against ANSWERS.json when the figure's alt is a key there;
- ticks with the same count mark equal lengths; `parallel` marks really parallel segments;
- SIDE LABELS (new): every `side XY "<number> <unit>"` label is in proportion: drawn length
  divided by the labelled number is the same for every numeric side label in the figure, within
  1%. A side with a quoted letter label ("a", "?") is checked against ANSWERS.json: drawn length
  divided by the figure's scale must equal the answer within 1%;
- TEXT LENGTHS (new): a `text (x,y) "<number> <unit>"` label beside a dashed segment is matched to
  the nearest dashed segment and checked against the same scale (this is how a triangle's height
  is labelled, since a side label on an inside segment is placed away from the centroid);
- CUBOIDS: dimensions are positive, whole numbers when `units` is on, at most 12 each;
- no ^\\circ anywhere in a figure.

Moved into the repo 2026-10-10 (tools/): a lettered label ("x", "a") with no answers listed is
now a failure, not a note; the line kinds mirror the platform's figure grammar
(packages/app/src/lib/figureFence.ts LINE_KINDS, plus the show: lines a figure falls back to:
line, curve and ray), and `expression` is refused, as the importer refuses it (B-140). The list
is a copy until the platform publishes the grammar as data (filed on its side).

Usage: python3 tools/check_figures.py DRAFT.md [ANSWERS.json]
"""
import json
import math
import re
import sys
from pathlib import Path

TOK = re.compile(r'\(\s*-?[\d.]+\s*,\s*-?[\d.]+\s*\)|"[^"]*"|\S+')
# Mirrors figureFence.ts LINE_KINDS plus the show: fallback (line, curve, ray): B-140.
KNOWN = ("alt:", "caption:", "point", "polygon", "region", "segment", "side", "angle", "ticks",
         "parallel", "text", "cuboid", "to scale", "plane:", "axes:", "hidden:",
         "line ", "curve ", "ray ")
NUM = re.compile(r'^"(\d+(?:\.\d+)?)\s*(mm|cm|m|km)"$')


def blocks(md):
    for m in re.finditer(r"^```figure\n(.*?)^```", md, re.M | re.S):
        yield m.group(1).splitlines()
    for m in re.finditer(r"^```columns\n(.*?)^```", md, re.M | re.S):
        for col in re.split(r"^---$", m.group(1), flags=re.M):
            lines = col.strip("\n").splitlines()
            if lines and lines[0].startswith("figure:"):
                yield lines[1:]


def pt(tok, names):
    if tok.startswith("("):
        x, y = tok.strip("()").split(",")
        return float(x), float(y)
    return names[tok]


def pair(tok, names, rest):
    """'AB' -> two points; or two coordinate tokens; or 'A B'."""
    if tok.startswith("("):
        return pt(tok, names), pt(rest.pop(0), names)
    if len(tok) == 2:
        return names[tok[0]], names[tok[1]]
    return names[tok], pt(rest.pop(0), names)


def ang(p, v, q):
    a = math.degrees(math.atan2(p[1] - v[1], p[0] - v[0]) - math.atan2(q[1] - v[1], q[0] - v[0])) % 360
    return min(a, 360 - a)


def direction(a, b):
    return math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 180


def seg_dist(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / (dx * dx + dy * dy)))
    return math.dist(p, (ax + t * dx, ay + t * dy))


def check(lines, answers):
    names, problems, report = {}, [], []
    alt = None
    segs, dashed, parallels, texts, ticks = [], [], [], {}, {}
    sides_num, sides_txt, text_lengths = [], {}, []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if "\\circ" in line:
            problems.append(f"^\\circ in figure line {line!r}")
        if line.startswith("expression"):
            problems.append(f"expression is refused in a figure (it needs the calculator): {line!r}")
            continue
        if not line.startswith(KNOWN):
            problems.append(f"unknown figure line {line!r}")
            continue
        if line.startswith("alt:"):
            alt = line[4:].strip()
            continue
        if line.startswith(("caption:", "to scale", "plane:", "axes:", "hidden:", "line ", "curve ", "ray ")):
            continue
        t = TOK.findall(line)
        try:
            if t[0] == "point":
                names[t[2].strip('"')] = pt(t[1], names)
            elif t[0] == "segment":
                rest = t[1:]
                a = pt(rest.pop(0), names)
                b = pt(rest.pop(0), names)
                segs.append((a, b))
                if rest and rest[0] == "dashed":
                    dashed.append((a, b))
            elif t[0] in ("polygon", "region"):
                pts = [pt(x, names) for x in t[1:]]
                for i in range(len(pts)):
                    segs.append((pts[i], pts[(i + 1) % len(pts)]))
            elif t[0] == "side":
                rest = t[2:]
                a, b = pair(t[1], names, rest)
                lab = rest[-1]
                d = math.dist(a, b)
                m = NUM.match(lab)
                if m:
                    sides_num.append((float(m.group(1)), d, lab))
                else:
                    sides_txt[lab.strip('"')] = d
            elif t[0] == "text":
                p = pt(t[1], names)
                m = NUM.match(t[2])
                if m:
                    text_lengths.append((p, float(m.group(1)), t[2]))
            elif t[0] == "cuboid":
                dims = [float(x) for x in t[1:4]]
                units = "units" in t[4:]
                if any(x <= 0 for x in dims):
                    problems.append(f"cuboid dimension not positive: {line}")
                if units and any(x != int(x) or x > 12 for x in dims):
                    problems.append(f"cuboid units needs whole numbers up to 12: {line}")
                report.append(f"cuboid {dims}")
            elif t[0] == "angle":
                if t[1].startswith("("):
                    p, v, q = pt(t[1], names), pt(t[2], names), pt(t[3], names)
                    lab = t[4] if len(t) > 4 else None
                else:
                    p, v, q = (names[c] for c in t[1])
                    lab = t[2] if len(t) > 2 else None
                a = ang(p, v, q)
                if lab and lab.endswith("°"):
                    want = float(lab[:-1])
                    if abs(a - want) > 1:
                        problems.append(f"angle {t[1]} labelled {lab} but drawn {a:.1f}°")
                elif lab == "right":
                    if abs(a - 90) > 1:
                        problems.append(f"angle {t[1]} marked right but drawn {a:.1f}°")
                elif lab and lab.startswith('"'):
                    texts[lab.strip('"')] = a
                    report.append(f'{lab}={a:.1f}°')
                elif lab:
                    problems.append(f"angle label {lab!r} is not a degree value, right, or quoted text")
            elif t[0] == "ticks":
                rest = t[2:]
                a, b = pair(t[1], names, rest)
                n = rest[-1]
                ticks.setdefault(n, []).append(math.dist(a, b))
            elif t[0] == "parallel":
                rest = t[2:]
                a, b = pair(t[1], names, rest)
                c, d = pair(rest.pop(0), names, rest)
                parallels.append(((a, b), (c, d)))
                diff = abs(direction(a, b) - direction(c, d))
                if min(diff, 180 - diff) > 0.5:
                    problems.append(f"parallel {t[1]} {t[2]} marks lines {min(diff, 180 - diff):.1f}° apart")
        except (KeyError, IndexError, ValueError) as e:
            problems.append(f"could not read {line!r} ({e})")
    if not alt:
        problems.append("no alt:")
    for n, lens in ticks.items():
        if max(lens) - min(lens) > 0.02:
            problems.append(f"ticks {n} mark lengths {[round(x, 2) for x in lens]}")
    marked = {frozenset(s) for pr in parallels for s in pr}
    # length scale from numeric side labels
    scale = None
    if sides_num:
        ratios = [d / v for v, d, _ in sides_num]
        scale = ratios[0]
        for (v, d, lab), r in zip(sides_num, ratios):
            if abs(r - scale) / scale > 0.01:
                problems.append(f"side {lab} drawn {d:.2f}, out of proportion (scale {scale:.3f}, this {r:.3f})")
        report.append(f"{len(sides_num)} side labels in proportion")
    for p, v, lab in text_lengths:
        if not dashed:
            problems.append(f"text length {lab} with no dashed segment to measure")
            continue
        near = min(dashed, key=lambda s: seg_dist(p, *s))
        d = math.dist(*near)
        if scale is None:
            problems.append(f"text length {lab}: no side label to set the scale")
        elif abs(d / v - scale) / scale > 0.01:
            problems.append(f"text {lab} labels a dashed segment drawn {d:.2f} (expected {v * scale:.2f})")
        else:
            report.append(f"height {lab} ok")
    if alt in answers:
        for lab, want in answers[alt].items():
            if lab in texts:
                if abs(texts[lab] - want) > 1:
                    problems.append(f'"{lab}" drawn {texts[lab]:.1f}°, answer {want}°')
            elif lab in sides_txt:
                if scale is None:
                    problems.append(f'"{lab}": no numeric side label to set the scale')
                elif abs(sides_txt[lab] / scale - want) / want > 0.01:
                    problems.append(f'"{lab}" drawn {sides_txt[lab] / scale:.2f}, answer {want}')
            else:
                problems.append(f'answer for "{lab}" given but no such label')
        report.append("answers checked")
    elif texts or sides_txt:
        problems.append(f"lettered labels {sorted(texts) + sorted(sides_txt)} but no answers listed")
    return alt, problems, report


def main(path, answers_path=None):
    md = Path(path).read_text(encoding="utf-8")
    answers = json.loads(Path(answers_path).read_text()) if answers_path else {}
    figs = list(blocks(md))
    bad = 0
    seen = set()
    for lines in figs:
        alt, problems, report = check(lines, answers)
        seen.add(alt)
        flag = "FAIL" if problems else "ok  "
        bad += bool(problems)
        print(f"{flag} {alt}  {' '.join(report)}")
        for p in problems:
            print(f"     - {p}")
    for a in answers:
        if a not in seen:
            print(f"FAIL answers file names a figure that isn't in the draft: {a}")
            bad += 1
    print(f"{path}: {len(figs)} figures, {bad} with problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
