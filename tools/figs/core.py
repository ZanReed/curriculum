"""Shared figure-generator core for catalogue drafts (moved from the builder's per-chain
generators, 2026-10-10).

A chain module (tools/figs/<chain>.py) defines its figures by calling fig() inside its own
define(). build() turns a chain's source file into its catalogue draft: @@FENCE name@@ becomes a
```figure fence, @@COL name@@ becomes the lines of a `figure:` column (no fence), and the answers
map the figure checker reads (alt text -> {label: value}) is written alongside. Answers are a
build output; they are never committed.
"""
import json
import math
import re

FIGS, ANS = {}, {}


def P(r, deg, cx=0.0, cy=0.0):
    """A point at distance r and angle deg (degrees) from (cx, cy), rounded to 2 places."""
    t = math.radians(deg)
    return round(cx + r * math.cos(t), 2), round(cy + r * math.sin(t), 2)


def f(p):
    return f"({p[0]:g},{p[1]:g})"


def fig(name, alt, lines, answers=None, extra=()):
    assert name not in FIGS, f"duplicate figure name {name}"
    FIGS[name] = [f"alt: {alt}", *extra, *lines]
    if answers:
        ANS[alt] = answers


def reset():
    FIGS.clear()
    ANS.clear()


def build_text(define, text):
    """Return (draft text, answers used) for a source text, defining the chain's figures once."""
    if not FIGS:
        define()

    def fence(m):
        return "```figure\n" + "\n".join(FIGS[m.group(1)]) + "\n```"

    def col(m):
        return "\n".join(FIGS[m.group(1)])

    text = re.sub(r"@@FENCE ([\w-]+)@@", fence, text)
    text = re.sub(r"@@COL ([\w-]+)@@", col, text)
    assert "@@" not in text, "unreplaced placeholder"
    used = {a: v for a, v in ANS.items() if a in text}
    return text, used


def build(define, src, out, answers_out):
    text, used = build_text(define, open(src, encoding="utf-8").read())
    open(out, "w", encoding="utf-8").write(text)
    with open(answers_out, "w", encoding="utf-8") as fh:
        json.dump(used, fh, indent=1, ensure_ascii=False)
