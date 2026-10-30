---
status: draft for Zan's ratification (2026-10-30). Applied to the catalogue bank only after the ruling.
fixes: 801/03's DoL binds mis.proportional.one-pair-assumed-constant, which rate.proportional-graph's bank does not bind (TP-8; C-167, B-217)
---

# 801/03 DoL binding fix

## 1. Graph (this PR, v0.19.4)

`rate.proportional-graph.misconceptions` gains `mis.proportional.one-pair-assumed-constant`. §7: a
misconception attaches to every skill that can elicit it, and 801/03's DoL distractor shows this
one does ("one visit costs $15, so k = 15"). It stays attached to
`rate.constant-of-proportionality` too.

## 2. Bank: `banks/801-chain.rate.proportional/rate.proportional-graph.md`

Meta lines change to:

```
x_templates: t1 fee at zero, t2 points on the line, t3 doubling (proportional), t4 crossing point, t5 draw it (fixed), t6 pick the graph (fixed), t7 one point is not enough
x_misconceptions: mis.proportional.line-misses-origin (t1, t4, t5, t6), mis.proportional.one-pair-assumed-constant (t7)
```

Four lines join the seed fence:

```
pm: int 2..5
pc: int 1..6
p1: = pm + pc
p2: = 2 * pm + pc
```

New template:

````md
## t7

Sam reads one point off a straight-line graph, (1, {p1}), and says: "y ÷ x = {p1}, so k = {p1} and the relationship is proportional." The same line passes through (2, {p2}). At that point, y ÷ x = {{=p2/2 | !p1 :: That's the ratio at the first point. Divide the y-value at the second point by 2. :: mis.proportional.one-pair-assumed-constant}}. Is the relationship proportional? {{no | !yes :: One point gives one ratio, and the second point gives a different one, so there is no single k. A proportional graph gives the same y ÷ x at every point, because it passes through (0, 0). :: mis.proportional.one-pair-assumed-constant}}
````

How it plays: the line is y = pm·x + pc, which always misses the origin, so the answer is always
"no". The first blank asks for y ÷ x at the second point; copying the first ratio is the
misconception, and it's bound. There are 24 rows and the answers run from 2.5 to 8. The mistake
never equals the answer, because pc ≥ 1.

## Checks run (scratch copy)

- `check_bank.py --graph`: 0 problems (t7: 24 of 24 combinations).
- `lint_draft.py`: 0 problems.
- 801/03 with the marker added in a scratch copy, `lint_draft.py --banks`: 0 problems. It gave 1 before
  the fix.
- `build_drafts.py --check` against the catalogue: OK. The current catalogue bank still passes
  `check_bank.py` against the new graph, so the merge order doesn't break our checks.

## Order

1. Zan ratifies t7.
2. A notice goes to the platform before the merge (the attachment is mirrored by id).
3. This PR merges.
4. t7 is applied to the catalogue bank.
5. The next `--strict` import carries both.
6. Only then may 801/03 get `{checkpoint dol}`. It must be seeded first (C-163), and that is not
   part of this fix.
