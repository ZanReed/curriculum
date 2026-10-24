---
status: sent as C-163 (2026-10-24) for the platform's D65 design pass; updated to the ruled grammar (DL-17 \seed{} inside maths). Not for import.
activity: 904-chain.algebra.manipulation, activity 06 (algebra.factorise.common-factor), DoL section only
---

# D65 sample DoL: factorise by the highest common factor

Only the parts D65 needs are shown. The review and lesson sections are elided.

````md
```meta
key: act.algebra.factorise-common-factor
skill: algebra.factorise.common-factor
title: Factorising — Taking Out the Highest Common Factor
course: Year 9 Mathematics
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
dol_skills: algebra.factorise.common-factor, algebra.expressions.like-terms
```

…review, lesson…

## Check for understanding {checkpoint dol}

```seed
g: list 4, 6, 8, 9, 10, 12
a: int 2..7
b: int 1..7
p: = g * a
q: = g * b
h: = g / 2
where dol: gcd(a, b) == 1 and mod(g, 2) == 0
c: int 5..9
r: int 2..4
d: int 2..9
k: = c - r
```

Factorise fully: $\seed{p}x - \seed{q}$.

{p}x − {q} = {{=g | !h :: That's a common factor, but not the highest. Check the bracket: its two numbers still share a factor of 2, so take that out too. :: mis.factorise.not-highest}} ( {{=a}} x − {{=b}} )

Simplify $\seed{c}m + \seed{d}n - \seed{r}m$: {{=k}} m + {{=d}} n
````

## Answers to B-208

1. **The DoL is marked twice.** The checkpoint heading carries a `dol` flag: `## Check for understanding {checkpoint dol}`. The meta line `dol_skills:` is the real key replacing today's `x_dol_skills`, which the importer drops. Its order maps item to skill: the first skill is the primary item's skill.
2. **The parallel form is (a): the same items with fresh numbers.** A retake redraws every variable in the DoL's ```seed fence. No items are swapped, and nothing is authored a second time (D65: seeded).
3. **The primary item is the first one,** the one whose skill comes first in `dol_skills:`. The pass rule (C-151) reads that item only. If an item has more than one blank, as here, the item is right only when all its blanks are right.
4. **There are no rubric items in this sample.** When a DoL has one, it is re-asked unchanged, with the first answer hidden (C-151).
5. **This sample needs both derived values and `where:`, so it needs BE-2 lifted.**
   - `p`, `q`, `h` and `k` are derived.
   - `gcd(a, b) == 1` makes `g` the HIGHEST common factor; without it, "factorise fully" has a different answer.
   - `mod(g, 2) == 0` makes the not-highest mistake `h` exist and differ from `g`.
   - The `where` is scoped to the DoL as one unit (`where dol:`), because in an activity the DoL plays the part a bank's template heading plays.
6. **Misconception ids:**
   - the primary item binds `mis.factorise.not-highest`;
   - the review item binds nothing, because collecting errors don't land in a coefficient blank;
   - `algebra.factorise.common-factor`'s bank, when written, must bind `mis.factorise.not-highest` and `mis.algebra.cancelled-to-zero` in at least one template each. §17 already requires a bank to cover every misconception attached to its skill, so the B-198 requirement holds by rule.

**The carrier is a numeric blank, not `gap_equation`.** The blanks sit inside the target form, which is the D60 rule. They are `fill_blank` blanks in prose, because the pinned facts don't say whether a `gap_equation` gap accepts a seeded `{{=expr}}` answer with `!mistake` bindings. If it does, the same item would use `$$…\gap…$$` instead.
