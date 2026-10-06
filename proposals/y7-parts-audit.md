# Y7 parts audit, against the parts rule

`status: encoded`. Ruled 6 Oct 2026 under D48 (parts rule) and D47 (32-minute budget). Landed
on `main` in graph v0.17.14 (checked against the synced repo, 6 Oct; §5). The graph is now the
edit surface for these skills; this file is the reasoning record.

**Source:** the repo copy of `proposals/y7-chain-stubs.md` pasted by Zan on 6 Oct
(`status: encoded`, in the graph from v0.17.0).

**Method.** Test 1 (one idea per part) and the size floor (ruling 8) are stubbing-time tests,
applied strictly here. Test 2 (budget fit) is a drafting-time test: where it looks likely to
fire, the row is flagged, not pre-split. Ruling 3 (the count runs both ways) means reductions
are made now.

**Rulings taken in this audit (Zan, 6 Oct):**
- **R1:** ideas that build on each other (one needs the other) are skills, not parts. Parts
  hold only ideas side by side with shared prerequisites, or one idea split by the budget.
- **Pairings:** LCM with HCF, complement with equally-likely probability, range with median and
  mode, rectangle area with triangle area. All four under ruling 8.

---

## 1. Changes

| skill | stub | ruled | basis | reason |
|---|---|---|---|---|
| `number.operations.order` | 2p | **1p** | test 1 | One idea: the order hierarchy, with left-to-right inside a rank as part of the rule. **Test 2 flag:** four contrasts (× before +, equal ranks, grouping, exponents) in one worked run. |
| `number.divisibility.rules` | 1p | **2p** | test 1 | Two side-by-side families: last-digits tests (2, 4, 5, 8, 10) and digit-sum tests (3, 9), with 6 combining them. Shared prereqs, neither needs the other, assessed together: parts. `mis.divisibility.last-digit-only` is exactly the confusion between the families. |
| `number.factors.hcf-lcm` | 2p | **1p** | ruling 8 | LCM of two numbers under 10 is too small for an activity. It is taught as the contrast inside the HCF sequence (common factor vs common multiple), where `mis.factors.hcf-lcm-swapped` belongs. Id and label unchanged. **Test 2 flag:** HCF to 100 plus the contrast. |
| `number.integers.additive-inverse` | 1 skill, 2p | **2 skills, 1p each:** `number.integers.add`, `number.integers.subtract` | R1 | Subtracting via the additive inverse needs integer addition. Both are big enough for an activity. |
| `algebra.equations.two-step` | 2p | **1p** | test 1 | One idea: undo in reverse order, to the whole side. Forms (ax + b, ax − b, x/a + b) are minimal pairs. |
| `pattern.linear.rule` | 2p | **1p** | test 1 | One idea: step → a, back-step to the zeroth term → d. Sequence and table are representations. Three misconceptions don't earn a part (rule 5). **Test 2 flag:** the back-step to d. |
| `measure.area.rect-triangle` | 1p | **1p (no change)** | ruling 8 | Two ideas, but rectangle area is likely Phase 2 review. **Check Phase 2**: if it is there, the label notes rectangle area as review and the triangle is the Y7 idea. Id and label otherwise unchanged. |
| `stats.summary.median-mode` | 1p | **1p, absorbs range** | ruling 8 | Mode and range are each too small for an activity. Label becomes: *Find the median, mode and range, including an even number of values; interpret the range as a measure of spread.* **Test 2 flag:** three measures in one sequence. |
| `stats.summary.range` | 1p | **retired, merged** | ruling 8 | Into `stats.summary.median-mode`. |
| `prob.theoretical.equally-likely` | 1p | **1p, absorbs complement** | ruling 8 | Label becomes: *Find the probability of an event with equally likely outcomes, as a fraction, decimal or percentage, and use P(not A) = 1 − P(A).* |
| `prob.complement` | 1p | **retired, merged** | ruling 8 | Into `prob.theoretical.equally-likely`. |
| `prob.sample-space.list` | 2p | **1p** | test 1 | One idea (systematic listing) in three representations. **Test 2 flag:** tree diagrams are a new tool; the likeliest row here to return to 2. |

**Ids kept on merges.** The surviving skills keep their ids, with the labels widened. Keys are
authored and arbitrary (D18), and keeping them avoids retiring ids that the hook bank and the
misconception screening already reference.

### Prereqs, attachments and retirements

| skill | prereqs | misconceptions |
|---|---|---|
| `number.integers.add` (new) | `number.integers.number-line` | `mis.integers.sign-ignored` |
| `number.integers.subtract` (new) | `number.integers.add` | `mis.integers.subtract-always-smaller`, `mis.integers.sign-ignored` (it reappears once subtraction is rewritten as addition) |
| `stats.summary.median-mode` | `stats.variables.classify` (unchanged) | adds `mis.range.as-interval`; keeps `mis.median.unsorted`, `mis.median.even-count`, `mis.summary.measures-swapped` |
| `prob.theoretical.equally-likely` | unchanged | adds `mis.prob.complement-as-reciprocal`; keeps `mis.prob.equiprobability`, `mis.percent.decimal-shift` |

**Cross-thread edge:** `linear.slope.two-points` (D45 item 2) took `number.integers.additive-inverse`
as a prereq. It repoints to `number.integers.subtract`, which carries addition through its own
edge. (Done on `main`; §5.)

**Retired ids:** `number.integers.additive-inverse`, `stats.summary.range`, `prob.complement`,
via `skill-ids-retired.txt` (check 4 (J)).

**Builder's notice (B-7):** attachments move on four skills. The grader watches the same ids;
`mis.range.as-interval` and `mis.prob.complement-as-reciprocal` now fire on the merged skills'
items, and `mis.integers.sign-ignored` also fires on subtraction.

**Consolidations:** unchanged. `chain.stats.summaries` keeps its consolidation:
`mis.summary.measures-swapped` still spans `stats.summary.mean` and the merged median skill.
No new one is earned (the HCF/LCM consolidation considered earlier lapses, since they stay one
skill).

---

## 2. Unchanged (39 skills)

Checked and left at 1 part. Brief reasons where the call wasn't obvious:

- **Number:** `place-value.decimals`; `place-value.powers-of-ten` (multiply and divide are one shift, in two directions); `round.cash` (cash rounding is rounding a total to the tenth of a dollar: same procedure, NZ context); `exponents.evaluate`; `roots.square` (the facts themselves are fluency work, `fact.root.square`); `primes.classify`; `integers.number-line`; `fractions.equivalent`; `fractions.to-decimal` (benchmarks are fluency facts; division is the idea); `percent.hundredths`.
- **Algebra:** `notation.write`; `expressions.substitute`; `expressions.like-terms`; `equations.one-step`; `formulae.rearrange`; `coord.four-quadrant`; `pattern.linear.graph`.
- **Measurement:** `perimeter.polygons`; `area.composite`; `volume.cuboid`; `time.duration` (12- and 24-hour are representations); `time.timetables`.
- **Geometry:** `triangles.classify` (two criteria, one idea); `angles.triangle-quad-sum` (using 360° doesn't require deriving it from 180°); `angles.relationships` (four relationships, one procedure; mild test-2 watch); `angles.parallel-transversal`; `transform.reflect`; `transform.rotate`; `transform.translate`; `nets.identify`.
- **Statistics:** `variables.classify`; `display.categorical`; `display.dot-plot`; `display.time-series`; `summary.mean`; `summary.outlier-effect`.
- **Probability:** `experimental.relative-frequency`; `experimental.large-numbers`.

---

## 3. Totals

| thread | activities before | after |
|---|---|---|
| 02 Number | 18 | 17 |
| 03 Algebra | 11 | 9 |
| 04 Measurement | 7 | 7 |
| 05 Geometry | 9 | 9 |
| 06 Statistics | 9 | 8 |
| 07 Probability | 7 | 5 |
| **Y7** | **61** (50 skills) | **55** (49 skills) |

Six test-2 flags (order of operations, HCF/LCM, pattern rule, median-mode-range, sample space,
and a mild watch on angle relationships). If the five firm flags all split at drafting, Y7
returns to 60.

---

## 4. Open

1. **Phase 2 check: rectangle area.** Decides only the label note on
   `measure.area.rect-triangle`, not the count.
2. **Chain shape.** `chain.number.order-of-operations` is now one activity. `chain.geom.nets`
   sets the precedent that one-activity chains are fine, so no change is proposed.

---

## 5. Landing check against `main` (6 Oct 2026)

Checked against the synced `ZanReed/curriculum` `main`: `curriculum-graph.json` v0.17.14,
`misconception-attachments.txt`, `skill-ids-retired.txt`, `decision-log-additions.md`.

**Landed as ruled.**
- Every row in §1: part counts, the two integer skills with their labels and prereqs, both
  merges with the widened labels, and every attachment in the §1 table.
- Chain activity counts match §3 exactly: 55 Y7 activities across 49 skills (96 skills and
  128 projected activities in the whole graph).
- `linear.slope.two-points` already points at `number.integers.subtract`.
- `skill-ids-retired.txt` lists all three retired ids, with reasons.
- The regenerated `misconception-attachments.txt` carries none of the retired ids.
- D47 and D48 are in the decision log; §2, §5, §6, §10 and §17 of the principles are updated.

**Follow-ups found** (none blocks anything until the chains concerned are drafted):

1. **Hook concept bank: two `connects_to` values point at retired ids.**
   `proposals/y7-hook-concept-bank.md` on `main`:
   - `hook.integers.ohakune-morning` → `number.integers.additive-inverse`. Repoint to
     `number.integers.add`: −4 + 9 is addition, and the hook sets up `mis.integers.sign-ignored`,
     which sits on the add skill.
   - `hook.stats.pick-a-shooter` → `stats.summary.range`. Repoint to
     `stats.summary.median-mode`, which now teaches range.
   Check 4 (J) reads the graph, not the bank, so CI won't catch these.

2. **Hook minimum (D42 amendment, 3 Oct) after the split and merges.** The minimum is
   max(skills with an approved activity, ceil(approved activities / 2)), so it's owed once
   activities are approved, and a chain's concepts are finished before its drafting.
   - `chain.number.integers` now has 3 skills and the bank has 2 hooks (number line, add).
     It owes a concept for `number.integers.subtract`.
     `mis.integers.subtract-always-smaller` (5 − (−2) < 5) is the natural target.
   - `chain.stats.summaries`: after the repoint, both of its median-mode hooks sit on one
     skill and `stats.summary.mean` has none. It owes a mean concept.
     `mis.mean.drops-zeros` is the natural target. One of the two median-mode hooks could
     go, since quality beats coverage (§4).
   - `chain.prob.theoretical` (2 skills, 2 hooks) is unaffected. No hook was on
     `prob.complement`.

3. **`proposals/y7-chain-stubs.md` on `main` doesn't carry the dated note** pointing here.
   The changed lines are in the 6 Oct handoff (`04-y7-chain-stubs-note.md`), with the `D__`
   placeholders filled as D47 (budget) and D48 (parts rule).

4. **`y7-stubs-current.md` at the repo root is a pre-audit snapshot.** It still lists all three
   retired ids and the old part counts. Check 4 (J) doesn't read it either. Refresh it from the
   graph or remove it, whichever the repo side intended it for.

5. **The hook bank's per-chain headings** ("(2 → 1)" and similar) still give the 24-minute stub
   counts and the old pool sizes. Refresh them in the same edit as item 1. This doesn't affect
   which hooks are owed.

*Resolution of the §5 follow-ups (repo side, 6 Oct 2026).* The check above read the PR #44
branch, not `main`: #43 and #44 weren't merged yet, so "on `main`" means "in this PR". In
the same PR:
1. **Done.** Both hook-bank targets are repointed exactly as proposed, with a dated note in the bank.
2. **Open, builder work.** `chain.number.integers` owes a hook concept for
   `number.integers.subtract`; `chain.stats.summaries` owes one for `stats.summary.mean`. Both are
   due before those chains are drafted (D42 amendment).
3. **Done.** `proposals/y7-chain-stubs.md` carries both dated notes, with D47 and D48 filled in.
4. **Done.** `y7-stubs-current.md` was an untracked relay copy for the builder, never committed;
   it's deleted.
5. **Done.** The bank's chain headings now read "(activities → pool)" from the graph, with the
   pool at the D42 amendment's minimum, plus a dated note.
