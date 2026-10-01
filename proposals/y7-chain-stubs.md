# Y7 chain stubs, all six strands (proposal)

`status: draft`. Written 29 Sep 2026. Decision input, not a decision: nothing here is in the
graph until it lands in a repo commit.

**Sources.** Fetched from `main` on 29 Sep: `README.md`, `thread-01-rate-of-change.json`,
`authoring-principles.md` and `decision-log-additions.md`. Y7 content comes from the
Phase 3 compression in `drafts/y7-13-requirements.md` (held in the Claude project, not in this repo) §2 (read from Tāhūrangi 25 Sep).

> **Branch copy.** The repo copy of this file lives on the draft PR #4 branch
> (`proposals-y7-stubs-threads`), last known head `919c092` (1 Oct). The repo side may edit
> it there. Before exporting again: get the current branch copy from Zan and edit that, or
> send only the changed lines.
>
> **D35 and D39 confirmed verbatim from the local clone at `f1faa07` (29 Sep).** Earlier note:
> repo reads from this session are partly stale. PR #2 (D40 glossary)
> is merged into `main`, and `glossary.md` fetches. But `README.md` and
> `decision-log-additions.md` come back as older copies: no glossary rows, and the log ends
> at D30. So the earlier "D31–D39 aren't on `main`" flag was a stale read, not missing
> commits. `curriculum-graph.json` returns 404, which matches the 25 Sep brief: the D39
> migration hasn't landed yet. This draft uses D35/D38/D39 **as described in the project**.
> Check the field names below against the actual D39 text before committing.

---

## Conventions used

- **Misconception attachments now drive AI grading (PR #5, 1 Oct).** A skill's
  `misconceptions` list is what the grader watches for on that skill's written-answer
  items, via the generated `misconception-attachments.txt`. So an id is attached only
  where students working on *that* skill really make the error, and wherever they do.
  The audit of 1 Oct:
  - removed `mis.notation.juxtaposition-as-digits` from `algebra.notation.write` (it is a
    substitution error; it stays on `algebra.expressions.substitute`);
  - on `pattern.linear.graph`, replaced `mis.pattern.step-as-rule` with
    `mis.pattern.first-term-as-constant`, the error students actually make when reading a
    graph;
  - added `mis.coord.axes-swapped` to the four skills that plot points (the pattern graph
    and the three transformations);
  - added `mis.time.decimal-hours` to `measure.time.timetables`;
  - added `mis.percent.decimal-shift` to `prob.theoretical.equally-likely`.

  `mis.area.same-perimeter-same-area` stays on both the perimeter and area skills under
  the pair rule. It is the one attachment where the pair rule and the grading rule could
  pull apart, so check it at screening.

- Ids follow the graph's pattern: `domain.sub.skill` for skills and `chain.domain.name` for
  chains. Skill ids are new; none collide with the 47 existing skills.
- Only `band_nz: Y7` is filled. `band_us` and `ccss`/`teks` stay empty (NZ-first).
  `nzc_phase` pointers need filling by someone with the Phase 3 page open.
- `thread`: set on each chain, using the ids in `proposals/threads-registry.md`
  (approved by Zan 30 Sep). Headings below keep §5's numbers for readability:
  - 02 `thread.number-proportion`
  - 03 `thread.algebra-equations`
  - 04 `thread.measurement`
  - 05 `thread.geometry-trig`
  - 06 `thread.statistical-enquiry`
  - 07 `thread.probability`
- **Misconception ids are all proposals.** The principles say "Use only ids that exist in
  the registry. Never invent one inline", so these go through screening like
  `misconception-proposals-ten-skills.md` before any activity uses them. Prefixes split by
  error kind (D21).
- Activity counts: `p` = part, `c` = consolidation (D24). A consolidation is proposed only
  where two skills in the chain are confusable, and the confusion is named.
- `calculator: off` for every Y7 chain (Phase 3 Number is non-calculator work).
- Hooks: none yet. The Y7 hook concept bank is the next step (D42 in `decision-log-additions.md`).

## Summary

| thread | chains | skills | activities (p + c) |
|---|---|---|---|
| 02 Number | 6 | 14 | 17 + 1 = 18 |
| 03 Algebra | 3 | 9 | 11 + 0 = 11 |
| 04 Measurement | 2 | 6 | 6 + 1 = 7 |
| 05 Geometry | 4 | 9 | 9 + 1 = 10 |
| 06 Statistics | 2 | 8 | 8 + 1 = 9 |
| 07 Probability | 2 | 5 | 6 + 1 = 7 |
| **Y7 total** | **19** | **51** | **57 + 5 = 62** |

At about 24 minutes an activity, that is roughly 25 hours: one or two activities a week
across a school year, alongside teacher-led lessons.

---

## Thread 02: Number

### `chain.number.place-value`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.place-value.decimals` | Read, write, compare and order decimals to thousandths using place value | `ext.arith.whole-ops` | `mis.place-value.longer-is-larger` (0.45 > 0.5) | 1 |
| `number.place-value.powers-of-ten` | Multiply and divide by 10, 100, 1000 as a shift in place value | `number.place-value.decimals` | `mis.place-value.append-zero` (3.4 × 10 = 3.40) | 1 |
| `number.round.cash` | Round to a given place, including NZ cash rounding to the nearest 10c | `number.place-value.decimals` | `mis.round.cash-per-item` (rounds each item, not the total); `mis.round.truncates` | 1 |

### `chain.number.powers`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.exponents.evaluate` | Evaluate positive whole-number powers as repeated multiplication; powers of 10 | `ext.arith.times-tables`, `number.place-value.powers-of-ten` | `mis.exponent.multiplies-base` (3⁴ = 12) | 1 |
| `number.roots.square` | Know square numbers to 12² and square roots to √144 | `number.exponents.evaluate` | `mis.root.halves` (√64 = 32) | 1 |

### `chain.number.order-of-operations`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.operations.order` | Apply the order of operations (GEMA), including grouping and exponents | `number.exponents.evaluate` | `mis.order.left-to-right`; `mis.order.multiply-before-divide` (treats M strictly before D) | 2 |

### `chain.number.factors`: 4 activities (4p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.primes.classify` | Classify whole numbers as prime or composite | `ext.arith.times-tables` | `mis.primes.one-is-prime`; `mis.primes.odd-means-prime` (9, 15, 21) | 1 |
| `number.divisibility.rules` | Use divisibility tests for 2, 3, 4, 5, 6, 9 and 10 | `number.primes.classify` | `mis.divisibility.last-digit-for-3` | 1 |
| `number.factors.hcf-lcm` | Find the highest common factor and lowest common multiple of two numbers | `number.divisibility.rules` | `mis.factors.hcf-lcm-swapped`; `mis.factors.lcm-is-product` | 2 |

### `chain.number.integers`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.integers.number-line` | Place, order and compare integers on a number line | `ext.arith.whole-ops` | `mis.integers.larger-digit-larger` (−8 > −3) | 1 |
| `number.integers.additive-inverse` | Use the additive inverse to add and subtract integers on a number line | `number.integers.number-line` | `mis.integers.subtract-always-smaller`; `mis.integers.sign-ignored` | 2 |

*Verify:* Y8 lists "operations with negatives". Check with the Phase 3 page open that Y7
covers adding and subtracting integers on the number line and not only the inverse as an idea.

### `chain.number.fractions`: 4 activities (3p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.fractions.equivalent` | Generate equivalent fractions and write fractions in simplest form | `number.factors.hcf-lcm` | `mis.fractions.add-same` (2/3 = 4/5) | 1 |
| `number.fractions.to-decimal` | Convert fractions to decimals by division and from known benchmarks | `number.fractions.equivalent`, `number.place-value.decimals` | `mis.fractions.digits-as-decimal` (3/5 = 3.5) | 1 |
| `number.percent.hundredths` | Understand percentages as hundredths; convert between fraction, decimal and percentage | `number.fractions.to-decimal` | `mis.percent.decimal-shift` (0.5 = 5%) | 1 |

**Consolidation** (terminal skill `number.percent.hundredths`), earned by confusability: the
three conversions are practised in isolation and then mixed up. Students apply the digits
rule from one conversion to another.

---

## Thread 03: Algebra

### `chain.algebra.expressions`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `algebra.notation.write` | Write expressions from words using algebraic conventions (3n, n + 5, n/2) | `ext.arith.whole-ops` | `mis.notation.letter-as-object` (a = apples) | 1 |
| `algebra.expressions.substitute` | Evaluate an expression by substituting values | `algebra.notation.write`, `number.operations.order` | `mis.notation.juxtaposition-as-digits` | 1 |
| `algebra.expressions.like-terms` | Collect like terms | `algebra.notation.write` | `mis.like-terms.combine-unlike` (2a + 3b = 5ab); `mis.like-terms.adds-to-power` (x + x = x²) | 1 |

### `chain.algebra.equations`: 4 activities (4p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `algebra.equations.one-step` | Solve one-step linear equations with integer solutions and check by substituting | `algebra.expressions.substitute` | `mis.equations.same-operation` (x + 5 = 12 → x = 17) | 1 |
| `algebra.equations.two-step` | Solve two-step linear equations with integer solutions and check by substituting | `algebra.equations.one-step` | `mis.equations.undo-order` (divides before subtracting); `mis.equations.one-side-only` | 2 |
| `algebra.formulae.rearrange` | Rearrange a simple formula to make another letter the subject (P = 4s → s = P/4) | `algebra.equations.two-step` | `mis.equations.same-operation` | 1 |

### `chain.pattern.linear`: 4 activities (4p). `thread.algebra-equations` (ruled 30 Sep)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `coord.four-quadrant` | Plot and read points in all four quadrants | `number.integers.number-line` | `mis.coord.axes-swapped` | 1 |
| `pattern.linear.rule` | Find the rule t = a × n + d for a linear pattern from a sequence or table | `algebra.expressions.substitute` | `mis.pattern.step-as-rule` ("add 3" written as t = n + 3); `mis.pattern.first-term-as-constant` (t = 3n + 5 when the first term is 5) | 2 |
| `pattern.linear.graph` | Graph a linear pattern and connect the step to the steepness and d to the start | `pattern.linear.rule`, `coord.four-quadrant` | `mis.pattern.first-term-as-constant` (reads the start d off the point at n = 1); `mis.coord.axes-swapped` | 1 |

**Thread: algebra (Zan, 30 Sep).** It follows the NZ curriculum, which places linear
patterns in Y7 Algebra. The chain is still the Y7 root of the gradient spine: the step
becomes the unit rate at Y8 and m at Y9. The prereq edges carry that connection across
threads, so `thread.rate-of-change` starts at Y8.

---

## Thread 04: Measurement

### `chain.measure.area-volume`: 5 activities (4p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `measure.perimeter.polygons` | Find the perimeter of polygons, including missing side lengths | `ext.measure.metric-units` | `mis.perimeter.counts-squares`; `mis.area.same-perimeter-same-area` | 1 |
| `measure.area.rect-triangle` | Find the area of rectangles, squares and triangles in square units | `measure.perimeter.polygons` | `mis.area.triangle-no-half`; `mis.area.slant-as-height`; `mis.units.area-as-linear` (cm, not cm²); `mis.area.same-perimeter-same-area` (assumes equal perimeters mean equal areas) | 1 |
| `measure.area.composite` | Find the area of a composite shape by decomposing it | `measure.area.rect-triangle` | `mis.area.composite-overlap` (double-counts a region) | 1 |
| `measure.volume.cuboid` | Find the volume of cubes and cuboids in cubic units, as layers of unit cubes | `measure.area.rect-triangle` | `mis.units.volume-as-square`; `mis.volume.adds-dimensions` | 1 |

**Consolidation** (terminal skill `measure.volume.cuboid`), earned by confusability: perimeter
vs area vs volume, and their units. This is the classic Y7 mix-up.

`mis.area.same-perimeter-same-area` was added 30 Sep, from the hook bank. It names a
confusion between two skills, so it attaches to both, per the principles.

### `chain.measure.time`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `measure.time.duration` | Calculate time durations across hour boundaries, in 12- and 24-hour time | `ext.time.read-clock` | `mis.time.decimal-hours` (1:30 treated as 1.30 h; 13:20 − 10:45 = 2.75) | 1 |
| `measure.time.timetables` | Read and use timetables to plan and compare journeys | `measure.time.duration` | `mis.time.24h-convert` (15:00 = 5 pm); `mis.time.decimal-hours` | 1 |

---

## Thread 05: Geometry

### `chain.geom.triangles-polygons`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.triangles.classify` | Classify triangles by sides and by angles | `ext.geom.angle-measure` | `mis.triangle.orientation-matters` (a "tilted" triangle isn't isosceles) | 1 |
| `geom.angles.triangle-quad-sum` | Use the angle sums of a triangle (180°) and a quadrilateral (360°) to find missing angles | `geom.triangles.classify` | `mis.angles.sum-depends-on-size` | 1 |
| `geom.angles.polygon-sums` | Find interior angle sums, 180(n − 2), and use the exterior angle sum of 360° | `geom.angles.triangle-quad-sum` | `mis.polygon.n-times-180`; `mis.polygon.exterior-grows-with-n` | 1 |

### `chain.geom.parallel-lines`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.angles.line-point-vertical` | Use angles on a line, at a point and vertically opposite | `ext.geom.angle-measure` | `mis.angles.vertical-as-supplementary` | 1 |
| `geom.angles.parallel-transversal` | Find angles where a transversal crosses parallel lines | `geom.angles.line-point-vertical` | `mis.parallel.all-equal`; `mis.parallel.assumed` (applies the rules to non-parallel lines) | 1 |

*Verify:* whether angles on a line, at a point and vertically opposite are Y7 statements or
earlier. If earlier, `geom.angles.line-point-vertical` becomes an external (`ext.geom.angle-facts`)
and the chain drops to one skill. Y9 names corresponding, alternate and co-interior angles
formally, so keep the Y7 skill to finding angles, not naming the pairs.

### `chain.geom.transformations`: 4 activities (3p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.transform.reflect` | Reflect a shape in a horizontal, vertical or diagonal mirror line | `coord.four-quadrant` | `mis.reflect.translates` (slides instead of flipping); `mis.reflect.diagonal-as-vertical`; `mis.coord.axes-swapped` | 1 |
| `geom.transform.rotate` | Rotate a shape by 90°, 180° or 270° about a given centre | `coord.four-quadrant` | `mis.rotate.centre-ignored`; `mis.coord.axes-swapped` | 1 |
| `geom.transform.translate` | Translate a shape by a given vector or description | `coord.four-quadrant` | `mis.translate.counts-gaps`; `mis.coord.axes-swapped` | 1 |

**Consolidation** (terminal skill `geom.transform.translate`), earned by confusability:
identifying *which* single transformation maps one shape to another. Reflection vs 180°
rotation is the mix-up.

### `chain.geom.nets`: 1 activity (1p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.nets.identify` | Identify and complete nets of cubes, prisms and pyramids | `ext.geom.shape-names` | `mis.nets.any-six-squares` (every arrangement of six squares folds into a cube) | 1 |

This is the only one-activity chain. It could instead sit as the first skill of
`chain.measure.area-volume` (nets → faces → cuboids), which would make that chain five skills.

---

## Thread 06: Statistics

### `chain.stats.data-displays`: 4 activities (4p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `stats.variables.classify` | Classify variables as categorical, discrete numerical or continuous numerical | — | `mis.stats.digits-are-numerical` (postcodes, jersey numbers) | 1 |
| `stats.display.categorical` | Read, draw and choose bar graphs, including stacked and clustered bars | `stats.variables.classify` | `mis.bar.order-meaningful` (reads a trend across categories) | 1 |
| `stats.display.dot-plot` | Read and draw dot plots for numerical data | `stats.variables.classify` | `mis.dotplot.uneven-scale` | 1 |
| `stats.display.time-series` | Read and draw time-series graphs and describe the change over time | `coord.four-quadrant` | `mis.timeseries.joins-categories` (line graph for categorical data) | 1 |

### `chain.stats.summaries`: 5 activities (4p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `stats.summary.mean` | Calculate and interpret the mean | `ext.arith.whole-ops`, `stats.display.dot-plot` | `mis.mean.drops-zeros` | 1 |
| `stats.summary.median-mode` | Find the median and mode, including an even number of values | `stats.display.dot-plot` | `mis.median.unsorted`; `mis.median.even-count` | 1 |
| `stats.summary.range` | Find and interpret the range as a measure of spread | `stats.summary.median-mode` | `mis.range.as-interval` (writes "3–12", or gives the largest value) | 1 |
| `stats.summary.outlier-effect` | Identify outliers and explain their effect on the mean vs the median | `stats.summary.mean`, `stats.summary.median-mode` | `mis.outlier.affects-median-equally` | 1 |

**Consolidation** (terminal skill `stats.summary.outlier-effect`), earned by confusability:
mean, median, mode and range get swapped for each other.

*Platform note:* Y7 data sets are small (≤ 20 values) and fit inline in a prompt, so this
chain does **not** wait on the dataset primitive. It does need bar charts, dot
plots and time-series graphs rendered in prompts. Check whether the graph mechanism the
linear drafts use can draw them.

---

## Thread 07: Probability

### `chain.prob.theoretical`: 4 activities (4p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `prob.sample-space.list` | List a sample space systematically using lists, tables and tree diagrams | — | `mis.prob.order-ignored` (HT and TH counted once) | 2 |
| `prob.theoretical.equally-likely` | Find the probability of an event with equally likely outcomes, as a fraction, decimal or percentage | `prob.sample-space.list`, `number.percent.hundredths` | `mis.prob.equiprobability` (sum of two dice: 2 as likely as 7); `mis.percent.decimal-shift` (0.05 written as 50%) | 1 |
| `prob.complement` | Use P(not A) = 1 − P(A) | `prob.theoretical.equally-likely` | `mis.prob.complement-as-reciprocal` | 1 |

### `chain.prob.experimental`: 3 activities (2p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `prob.experimental.relative-frequency` | Estimate a probability as a relative frequency from trial results | `number.fractions.to-decimal` | `mis.prob.small-sample-exact` (expects exactly 5 heads in 10) | 1 |
| `prob.experimental.large-numbers` | Compare experimental and theoretical probability as the number of trials grows | `prob.experimental.relative-frequency`, `prob.theoretical.equally-likely` | `mis.prob.gamblers-fallacy` ("due" for a head) | 1 |

**Consolidation** (terminal skill `prob.experimental.large-numbers`), earned by
confusability: experimental vs theoretical probability, and when each one answers the question.

*Platform note:* trial results can be given as tables. A live simulation primitive would
help but isn't required at Y7.

---

## New external prereqs (pre-Y7)

`ext.arith.whole-ops`, `ext.arith.times-tables`, `ext.measure.metric-units`,
`ext.time.read-clock`, `ext.geom.angle-measure`, `ext.geom.shape-names`.

## Cross-thread consequences (follow-ups, not part of this stub)

- Three existing externals now have internal Y7 skills behind them:
  - `ext.arith.fractions` → `number.fractions.*`
  - `ext.arith.signed` → `number.integers.*`
  - `ext.geom.coordinate-plane` → `coord.four-quadrant`

  Whether thread-01's prereqs get re-pointed (and those externals retired) is a separate
  ruling, and a platform-visible change.
- `pattern.linear.graph` → `rate.unit-rate` is a candidate edge: the step as a rate.

## Open questions this raises

1. **Thread ids.** D39 (confirmed from `f1faa07`) sets the shape: a `thread` field on each
   `chunking_plan` chain, and a top-level `threads` registry. It doesn't name ids. The
   proposal is in `proposals/threads-registry.md`.
2. ~~Y7 DoL default~~ **Ruled 29 Sep: D35 extends to Y7 as written.** Recorded as D41 in
   `decision-log-additions.md`.
3. ~~`chain.pattern.linear` thread tag~~ **Ruled 30 Sep: `thread.algebra-equations`**, following the NZ curriculum.
4. **`chain.geom.nets`:** keep as a one-activity chain or fold into area-volume.
5. **Figure/chart primitive.** Five of the 19 chains need labelled figures in prompts
   (the geometry chains, area-volume and nets), and two statistics chains need charts. That
   is 7 of 19 Y7 chains, so this goes to the platform page **now**, as a pointer.

## Y7 DoL default (ruled 29 Sep, extended as written)

**D35 extends to Y7 as written:** auto-scored items plus one error-analysis item (§16), with
rubric justification at chain finals and consolidations.

- D35's reasons hold more strongly at Y7. The nearest real assessment for a Y7 learner in
  2026 is the numeracy co-requisite, then the Foundational Award, which is procedural and
  auto-scorable. Y7 is also where activity volume is highest.
- A Y7 written justification also tests writing as much as maths, which is a reason not to
  make it the default.

**Cost to check.** Y7 chains are short, so "chain final" is a large share: all 19 chain
finals (5 of them consolidations) would be rubric-graded, which is 19 of 62 activities.
Chain 1 at Y8 has 1 rubric DoL in 4. If that marking load is too high, the alternative is
rubric justification only at consolidations and at the finals of chains with 3 or more
activities. That gives 14 of 62: it drops powers, order of operations, time, parallel lines
and nets.

## Before this goes near the graph

- [ ] Zan reads it end-to-end (drafts stay `status: draft` until then).
- [ ] Phase 3 page open: confirm the two *Verify* items and fill `nzc_phase` per skill.
- [ ] Misconception proposals screened.
- [x] Thread ids approved (30 Sep, `proposals/threads-registry.md`). The D39 migration still lands first.
- [x] Y7 DoL default ruled (29 Sep): D41 in `decision-log-additions.md`.
