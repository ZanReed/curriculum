# Y7 parts audit, against the parts rule (draft)

`status: ruled and read end to end by Zan 6 Oct 2026; applied in the graph at v0.17.14 (D48)`. Written and ruled 6 Oct 2026, against
`02-decision-parts-rule.md` (rulings 1–8, agreed 6 Oct, not yet committed) and the
32-minute budget (`01-decision-activity-budget.md`).

**Source:** the repo copy of `proposals/y7-chain-stubs.md` pasted by Zan on 6 Oct
(`status: encoded`, in the graph from v0.17.0). **The graph is the edit surface for these
skills**, so every change below lands as a graph PR, not as an edit to the stubs file. The stubs
file gets a dated note pointing here, as its reasoning record (`04-y7-chain-stubs-note.md`).

**Order:** the budget decision and the parts-rule decision land first; this PR applies them.

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
misconception screening already reference. If you'd rather the ids match the labels, both
merged skills would need new ids and retirements.

### Prereqs, attachments and retirements

| skill | prereqs | misconceptions |
|---|---|---|
| `number.integers.add` (new) | `number.integers.number-line` | `mis.integers.sign-ignored` |
| `number.integers.subtract` (new) | `number.integers.add` | `mis.integers.subtract-always-smaller`, `mis.integers.sign-ignored` (it reappears once subtraction is rewritten as addition) |
| `stats.summary.median-mode` | `stats.variables.classify` (unchanged) | adds `mis.range.as-interval`; keeps `mis.median.unsorted`, `mis.median.even-count`, `mis.summary.measures-swapped` |
| `prob.theoretical.equally-likely` | unchanged | adds `mis.prob.complement-as-reciprocal`; keeps `mis.prob.equiprobability`, `mis.percent.decimal-shift` |

**Retired ids:** `number.integers.additive-inverse`, `stats.summary.range`, `prob.complement`.
All three are in the graph since v0.17.0, so they go through the retired-ids mechanism. No
activity uses them yet. Nothing in Y7 has a prereq edge to `stats.summary.range` or
`prob.complement` from outside its merged skill; check thread-01 and the Y8 stubs for any.

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
returns to 60. Either way the year now carries fewer, fuller activities at the 32-minute
budget.

The regenerated `sum(parts)` denominator is quoted in the PR, not hand-counted (D37).

---

## 4. Open

1. **Phase 2 check: rectangle area.** Decides only the label note on
   `measure.area.rect-triangle`, not the count.
2. **Chain shape.** `chain.number.order-of-operations` drops to one activity. `chain.geom.nets`
   sets the precedent that one-activity chains are fine, so no change is proposed. Flagged only
   because two short Number chains now sit side by side (powers 2, order 1).
3. **Cross-references to the retired ids.** Check the Y7 hook concept bank and the Y8 stubs for
   `stats.summary.range` and `prob.complement`, and repoint any `connects_to` before the PR.


*Applied 2026-10-06 (D48 note):* new skill labels (not specified above) are `number.integers.add` "Add integers, using the number line" and `number.integers.subtract` "Subtract integers by adding the additive inverse, using the number line"; both copy the retired skill's NZC alignment. Total parts regenerate to 102 (skill registry header).
