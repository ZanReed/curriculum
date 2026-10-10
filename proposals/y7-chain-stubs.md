# Y7 chain stubs, all six strands (proposal)

`status: encoded` — in the graph from v0.17.0 (3 Oct 2026); the graph is now the edit surface for these skills and chains, and this file is the reasoning record. Written 29 Sep 2026. Decision input, not a decision: nothing here is in the
graph until it lands in a repo commit.

> **Parts audit, 6 Oct 2026.** The part counts and four skill rows below are superseded by the
> Y7 parts audit (`proposals/y7-parts-audit.md`), applied in the graph under D48 (parts rule).
> Y7 goes from 61 activities across 50 skills to 55 across 49. Changed rows:
> `number.operations.order`, `number.divisibility.rules`, `number.factors.hcf-lcm`,
> `number.integers.additive-inverse` (split into `number.integers.add` and
> `number.integers.subtract`), `algebra.equations.two-step`, `pattern.linear.rule`,
> `stats.summary.median-mode` (absorbs `stats.summary.range`),
> `prob.theoretical.equally-likely` (absorbs `prob.complement`), `prob.sample-space.list`.
> The tables below are kept as they were landed, as the record of the original stubbing.

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
  pull apart. **Ruled 1 Oct (Zan): keep it on both.**

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
| 05 Geometry | 4 | 8 | 8 + 1 = 9 |
| 06 Statistics | 2 | 8 | 8 + 1 = 9 |
| 07 Probability | 2 | 5 | 6 + 1 = 7 |
| **Y7 total** | **19** | **50** | **56 + 5 = 61** |

At about 24 minutes an activity, that is roughly 25 hours: one or two activities a week
across a school year, alongside teacher-led lessons.

*(6 Oct 2026: the activity cap is now 32 minutes under D47 (activity budget), and the
figures above are superseded by the parts audit. Teacher-led lessons are no longer the
default for non-activity periods; see the open-periods decision, when it lands.)*

---

## Thread 02: Number

### `chain.number.place-value`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.place-value.decimals` | Read, write, compare and order decimals to hundredths using place value (was thousandths; Zan 1 Oct) | `ext.arith.whole-ops` | `mis.place-value.longer-is-larger` (0.45 > 0.5) | 1 |
| `number.place-value.powers-of-ten` | Multiply and divide by 10, 100, 1000 as a shift in place value | `number.place-value.decimals` | `mis.place-value.append-zero` (3.4 × 10 = 3.40) | 1 |
| `number.round.cash` | Round to a given place, including NZ cash rounding to the nearest 10c | `number.place-value.decimals` | `mis.round.cash-per-item` (rounds each item, not the total); `mis.round.truncates` | 1 |

### `chain.number.powers`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.exponents.evaluate` | Evaluate positive whole-number powers as repeated multiplication; powers of 10 | `ext.arith.times-tables`, `number.place-value.powers-of-ten` | `mis.exponent.multiplies-base` (3⁴ = 12) | 1 |
| `number.roots.square` | Know square numbers to 12² and square roots to √144 | `number.exponents.evaluate` | `mis.root.halves` (√64 = 32); `mis.exponent.multiplies-base` (7² = 14) | 1 |

### `chain.number.order-of-operations`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.operations.order` | Apply the order of operations (GEMA), including grouping and exponents | `number.exponents.evaluate` | `mis.order.left-to-right`; `mis.order.pairs-ranked` (ranks M above D, or A above S, instead of working left to right; was `multiply-before-divide`) | 2 |

### `chain.number.factors`: 4 activities (4p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.primes.classify` | Classify whole numbers as prime or composite | `ext.arith.times-tables` | `mis.primes.one-is-prime`; `mis.primes.odd-means-prime` (9, 15, 21) | 1 |
| `number.divisibility.rules` | Use divisibility tests for 2, 3, 4, 5, 6, 8, 9 and 10 (8 added, Zan 1 Oct) | `number.primes.classify` | `mis.divisibility.last-digit-only` (uses the last digit where the test needs the digit sum or more digits: 3, 4, 8, 9; was `last-digit-for-3`) | 1 |
| `number.factors.hcf-lcm` | Find the highest common factor of two numbers under 100 and the lowest common multiple of two numbers under 10 (limits from S36; Zan 1 Oct) | `number.divisibility.rules` | `mis.factors.hcf-lcm-swapped`; `mis.factors.lcm-is-product` | 2 |

### `chain.number.integers`: 3 activities (3p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.integers.number-line` | Place, order and compare integers on a number line | `ext.arith.whole-ops` | `mis.integers.larger-digit-larger` (−8 > −3) | 1 |
| `number.integers.additive-inverse` | Use the additive inverse to add and subtract integers on a number line | `number.integers.number-line` | `mis.integers.subtract-always-smaller`; `mis.integers.sign-ignored` | 2 |

~~*Verify:*~~ **Resolved 1 Oct:** Y7 covers adding and subtracting integers on a number line (S42), so
the skill stands. The original note: *Verify:* Y8 lists "operations with negatives". Check with the Phase 3 page open that Y7
covers adding and subtracting integers on the number line and not only the inverse as an idea.

### `chain.number.fractions`: 4 activities (3p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `number.fractions.equivalent` | Generate equivalent fractions and write fractions in simplest form | `number.factors.hcf-lcm` | `mis.fractions.add-same` (2/3 = 4/5) | 1 |
| `number.fractions.to-decimal` | Convert fractions to decimals by division and from known benchmarks | `number.fractions.equivalent`, `number.place-value.decimals` | `mis.fractions.digits-as-decimal` (3/5 = 3.5; 1/4 = 14%) | 1 |
| `number.percent.hundredths` | Understand percentages as hundredths; convert between fraction, decimal and percentage | `number.fractions.to-decimal` | `mis.percent.decimal-shift` (0.5 = 5%); `mis.fractions.digits-as-decimal` (1/4 = 14%) | 1 |

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
| `algebra.equations.two-step` | Solve two-step linear equations with integer solutions and check by substituting | `algebra.equations.one-step` | `mis.equations.partial-divide` (divides only some terms: 2x + 7 = 31 → x + 7 = 15.5; was `undo-order`); `mis.equations.one-side-only`; `mis.equations.same-operation` | 2 |
| `algebra.formulae.rearrange` | Rearrange a simple formula to make another letter the subject (P = 4s → s = P/4) | `algebra.equations.two-step` | `mis.equations.same-operation` | 1 |

### `chain.pattern.linear`: 4 activities (4p). `thread.algebra-equations` (ruled 30 Sep)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `coord.four-quadrant` | Plot and read points in all four quadrants | `number.integers.number-line` | `mis.coord.axes-swapped` | 1 |
| `pattern.linear.rule` | Find the rule t = a × n + d for a linear pattern from a sequence or table | `algebra.expressions.substitute` | `mis.pattern.step-as-rule` ("add 3" written as t = n + 3); `mis.pattern.first-term-as-constant` (t = 3n + 5 when the first term is 5); `mis.pattern.assumes-proportional` (6, 10, 14 … → 20 tables seat 120) | 2 |
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
| `measure.area.composite` | Find the area of a composite shape by decomposing it | `measure.area.rect-triangle` | `mis.area.composite-overlap` (double-counts a region); `mis.area.triangle-no-half`; `mis.area.slant-as-height`; `mis.units.area-as-linear` | 1 |
| `measure.volume.cuboid` | Find the volume of cubes and cuboids in cubic units, as layers of unit cubes | `measure.area.rect-triangle` | `mis.units.volume-as-square`; `mis.volume.adds-dimensions` | 1 |

**Consolidation** (terminal skill `measure.volume.cuboid`), earned by confusability: perimeter
vs area vs volume, and their units. This is the classic Y7 mix-up.

`mis.area.same-perimeter-same-area` was added 30 Sep, from the hook bank. It names a
confusion between two skills, so it attaches to both, per the principles.

### `chain.measure.time`: 2 activities (2p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `measure.time.duration` | Calculate time durations across hour boundaries, in 12- and 24-hour time | `ext.time.read-clock` | `mis.time.decimal-hours` (1:30 treated as 1.30 h; 13:20 − 10:45 = 2.75); `mis.time.24h-convert` | 1 |
| `measure.time.timetables` | Read and use timetables to plan and compare journeys | `measure.time.duration` | `mis.time.24h-convert` (15:00 = 5 pm); `mis.time.decimal-hours` | 1 |

---

## Thread 05: Geometry

### `chain.geom.triangles-polygons`: 2 activities (2p)

**Ruled 1 Oct (Zan): `geom.angles.polygon-sums` moves to Y8.** Its practice lines are Y8-only on
the page (S85, S86). It goes into the Y8 stubs with its row as it stood:

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.angles.polygon-sums` | Find interior angle sums, 180(n − 2), and use the exterior angle sum of 360° | `geom.angles.triangle-quad-sum` | `mis.polygon.n-times-180`; `mis.polygon.exterior-grows-with-n` | 1 |

Its two misconceptions (`mis.polygon.n-times-180`, `mis.polygon.exterior-grows-with-n`) and its
hook (`hook.polygon.honeycomb`) move with it, so they leave Y7 screening.

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.triangles.classify` | Classify triangles by sides and by angles | `ext.geom.angle-measure` | `mis.triangle.orientation-matters` (a "tilted" triangle isn't isosceles) | 1 |
| `geom.angles.triangle-quad-sum` | Use the angle sums of a triangle (180°) and a quadrilateral (360°) to find missing angles | `geom.triangles.classify` | `mis.angles.sum-depends-on-size` | 1 |

### `chain.geom.parallel-lines`: 2 activities (2p)

**Ruled 1 Oct (Zan):** the first skill is relabelled to the page's four relationships (S84) and drops
"at a point", which Phase 3 doesn't name. Its id is renamed `geom.angles.line-point-vertical` →
`geom.angles.relationships` (1 Oct, before it lands in the graph), so nothing retires.

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.angles.relationships` | Use supplementary, complementary, vertical and adjacent angle relationships to find unknown angles | `ext.geom.angle-measure` | `mis.angles.vertical-as-supplementary`; `mis.angles.complement-supplement-swapped` (180° for complementary, or 90° for supplementary) | 1 |
| `geom.angles.parallel-transversal` | Find angles where a transversal crosses parallel lines | `geom.angles.relationships` | `mis.parallel.all-equal`; `mis.parallel.assumed` (applies the rules to non-parallel lines) | 1 |

~~*Verify:*~~ **Resolved 1 Oct** (`proposals/y7-nzc-phase.md`, section 3): angles on a line and vertically
opposite are Y7 (S84); "at a point" isn't on the Phase 3 page. The skill stays Y7 with both chain
skills. The original note:

> *Verify:* whether angles on a line, at a point and vertically opposite are Y7 statements or
> earlier. If earlier, `geom.angles.line-point-vertical` becomes an external (`ext.geom.angle-facts`)
> and the chain drops to one skill. Y9 names corresponding, alternate and co-interior angles
> formally, so keep the Y7 skill to finding angles, not naming the pairs.

### `chain.geom.transformations`: 4 activities (3p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.transform.reflect` | Reflect a shape in a horizontal, vertical or diagonal mirror line | `coord.four-quadrant` | `mis.reflect.translates` (slides instead of flipping); `mis.reflect.diagonal-as-vertical`; `mis.coord.axes-swapped`; `mis.reflect.half-turn-confused` | 1 |
| `geom.transform.rotate` | Rotate a shape by 90°, 180° or 270° about a given centre | `coord.four-quadrant` | `mis.rotate.centre-ignored`; `mis.coord.axes-swapped`; `mis.reflect.half-turn-confused` | 1 |
| `geom.transform.translate` | Translate a shape by a given vector or description | `coord.four-quadrant` | `mis.translate.counts-gaps` (counts the empty squares between shape and image, not how far one vertex moves); `mis.coord.axes-swapped` | 1 |

*Reordered 2026-10-10 (Zan): translation is taught first, so the chain runs translate → reflect →
rotate and the consolidation's terminal skill is `geom.transform.rotate` (graph v0.17.22).*

**Consolidation** (terminal skill `geom.transform.rotate` since the reordering; originally `geom.transform.translate`), earned by confusability:
identifying *which* single transformation maps one shape to another. Reflection vs 180°
rotation is the mix-up.

### `chain.geom.nets`: 1 activity (1p)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `geom.nets.identify` | Identify and complete nets of cubes, prisms and pyramids | `ext.geom.shape-names` | `mis.nets.any-six-squares` (every arrangement of six squares folds into a cube) | 1 |

This is the only one-activity chain, and it stays one (Zan, 1 Oct). Nets is geometry,
not measurement, and a short chain is useful to teachers as a lesson that fits a gap.

---

## Thread 06: Statistics

### `chain.stats.data-displays`: 4 activities (4p)

**Ruled 1 Oct (Zan): dot plots are for categorical data**, as the page has it (S97). Knock-ons
resolved 1 Oct: `mis.dotplot.uneven-scale` (a numerical-axis error) leaves this skill and is
carried to the first stub that teaches numerical dot plots (not Y7 or Y8 on Phase 3; check
Phase 4). `mis.bar.order-meaningful` attaches here instead (renamed `mis.display.order-meaningful` in the 1 Oct screening). The mean and median-mode skills
now take `stats.variables.classify` in place of `stats.display.dot-plot`.

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `stats.variables.classify` | Classify variables as categorical, discrete numerical or continuous numerical | — | `mis.stats.digits-are-numerical` (postcodes, jersey numbers) | 1 |
| `stats.display.categorical` | Read, draw and choose bar graphs, including stacked and clustered bars | `stats.variables.classify` | `mis.display.order-meaningful` (reads a trend across categories); `mis.timeseries.joins-categories` | 1 |
| `stats.display.dot-plot` | Read and draw dot plots for categorical data | `stats.variables.classify` | `mis.display.order-meaningful` (reads a trend across categories) | 1 |
| `stats.display.time-series` | Read and draw time-series graphs and describe the change over time | `coord.four-quadrant` | `mis.timeseries.joins-categories` (line graph for categorical data) | 1 |

### `chain.stats.summaries`: 5 activities (4p + 1c)

| skill | label | prereqs | proposed misconceptions | parts |
|---|---|---|---|---|
| `stats.summary.mean` | Calculate and interpret the mean | `ext.arith.whole-ops`, `stats.variables.classify` | `mis.mean.drops-zeros`; `mis.summary.measures-swapped` | 1 |
| `stats.summary.median-mode` | Find the median and mode, including an even number of values | `stats.variables.classify` | `mis.median.unsorted`; `mis.median.even-count`; `mis.summary.measures-swapped` | 1 |
| `stats.summary.range` | Find and interpret the range as a measure of spread | `stats.summary.median-mode` | `mis.range.as-interval` (writes "3–12"); `mis.summary.measures-swapped` | 1 |
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
| `prob.experimental.large-numbers` | Compare experimental and theoretical probability as the number of trials grows | `prob.experimental.relative-frequency`, `prob.theoretical.equally-likely` | `mis.prob.gamblers-fallacy` ("due" for a head); `mis.prob.small-sample-exact` | 1 |

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
4. ~~`chain.geom.nets`~~ **Ruled 1 Oct: kept as its own one-activity chain.**
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
finals (5 of them consolidations) would be rubric-graded, which is 19 of 61 activities.
Chain 1 at Y8 has 1 rubric DoL in 4. If that marking load is too high, the alternative is
rubric justification only at consolidations and at the finals of chains with 3 or more
activities. That gives 13 of 61: it drops powers, order of operations, time, triangles-polygons, parallel lines
and nets.

## Misconception screening (1 Oct)

**Screened and ruled 1 Oct (Zan)** from the Y7 misconception check, against §7 of
`authoring-principles.md`: each id needs a carrier on an auto-scored item, is attached wherever
students make the error, binds a FORM error only where units are a choice, and has a label that
names one error. Each label below becomes the id's registry description, which the AI grader reads
as prompt text. The ids are still proposals until they land in the graph.

Rulings, in brief (the tables above already carry them):

- **Renamed before landing** (nothing retires): `mis.equations.undo-order` → `mis.equations.partial-divide`
  (dividing first is valid if every term is divided, so the old label named a correct method);
  `mis.order.multiply-before-divide` → `mis.order.pairs-ranked`;
  `mis.divisibility.last-digit-for-3` → `mis.divisibility.last-digit-only` (8 is now in the skill);
  `mis.bar.order-meaningful` → `mis.display.order-meaningful` (it sits on dot plots too).
- **New ids:** `mis.angles.complement-supplement-swapped` (the relabelled angles skill brought in
  complementary angles); `mis.pattern.assumes-proportional` (the hui-tables guess of 120 is 6 × 20,
  not the first-term error); and, for consolidations, `mis.reflect.half-turn-confused` and
  `mis.summary.measures-swapped`.
- **Added attachments:** same-operation → two-step; multiplies-base → square roots; digits-as-decimal
  → percentages (label widened); 24h-convert → duration; area-as-linear, triangle-no-half and
  slant-as-height → composite area; joins-categories → bar graphs; small-sample-exact → large numbers.
- **Narrowed:** `mis.range.as-interval` drops the largest-value clause.
- **Consolidations:** transformations, summaries and experimental probability now each have an id
  shared across the confusion they name; fractions has one through digits-as-decimal. Area-volume
  stays on judgement (the perimeter–area pair is shared).
- **Surface area (Zan's question):** Phase 3 has no surface-area statement. Its measurement
  statements (S63–S73 in `proposals/y7-nzc-phase.md`, a complete read) cover perimeter, area,
  volume and time only. So no Y7 or Y8 skill needs a surface-area misconception. If a later stub
  teaches surface area, its area-versus-volume errors are screened there, as with
  `mis.dotplot.uneven-scale`.

| id | label (registry description) | attached to | carrier |
|---|---|---|---|
| `mis.place-value.longer-is-larger` | Judges a decimal with more digits after the point to be larger (0.45 > 0.5) | `number.place-value.decimals` | mc: order 0.5, 0.45, 0.405 |
| `mis.place-value.append-zero` | Multiplies a decimal by 10 by writing a zero on the end (3.4 × 10 = 3.40) | `number.place-value.powers-of-ten` | mc with 3.40 as an option (a numeric blank would read 3.40 as 3.4) |
| `mis.round.cash-per-item` | Rounds each price before adding, instead of rounding the cash total | `number.round.cash` | mc: the total at the dairy |
| `mis.round.truncates` | Cuts off digits instead of rounding ($4.97 paid in cash as $4.90) | `number.round.cash` | numeric blank; binding catches 4.90 |
| `mis.exponent.multiplies-base` | Multiplies the base by the exponent (3⁴ = 12, 7² = 14) | `number.exponents.evaluate`, `number.roots.square` | numeric blank |
| `mis.root.halves` | Finds a square root by halving (√64 = 32) | `number.roots.square` | numeric blank |
| `mis.order.left-to-right` | Works strictly left to right, ignoring the order of operations (6 + 4 × 2 = 20) | `number.operations.order` | numeric blank; binding catches 20 |
| `mis.order.pairs-ranked` | Ranks multiplication above division, or addition above subtraction, instead of working left to right | `number.operations.order` | numeric blank |
| `mis.primes.one-is-prime` | Counts 1 as a prime number | `number.primes.classify` | mc: which of these are prime |
| `mis.primes.odd-means-prime` | Treats every odd number as prime (9, 15, 91) | `number.primes.classify` | mc: is 91 prime |
| `mis.divisibility.last-digit-only` | Uses only the last digit where the test needs the digit sum or the last two or three digits (3, 4, 8, 9) | `number.divisibility.rules` | mc: which numbers are divisible by 3 / 8 |
| `mis.factors.hcf-lcm-swapped` | Gives the HCF when the LCM is asked for, or the reverse | `number.factors.hcf-lcm` | numeric blank |
| `mis.factors.lcm-is-product` | Gives the product as the LCM when a smaller common multiple exists (6 and 8 → 48, not 24) | `number.factors.hcf-lcm` | numeric blank; binding catches 48 |
| `mis.integers.larger-digit-larger` | Orders negative numbers by size, ignoring the sign (−8 > −3) | `number.integers.number-line` | mc: which is greater |
| `mis.integers.subtract-always-smaller` | Believes subtracting always gives a smaller number (5 − (−2) < 5) | `number.integers.additive-inverse` | mc: compare to 5 |
| `mis.integers.sign-ignored` | Adds the sizes and keeps the sign when the signs differ (−4 + 9 = −13) | `number.integers.additive-inverse` | numeric blank; binding catches −13 |
| `mis.fractions.add-same` | Adds the same number to top and bottom to make an equivalent fraction (2/3 = 4/5) | `number.fractions.equivalent` | mc: which fraction equals 2/3 |
| `mis.fractions.digits-as-decimal` | Writes a fraction's digits as a decimal or percentage (3/5 = 3.5, 1/4 = 14%) | `number.fractions.to-decimal`, `number.percent.hundredths` | mc or numeric blank |
| `mis.percent.decimal-shift` | Moves the decimal point the wrong number of places to or from a percentage (0.5 = 5%, 0.05 = 50%) | `number.percent.hundredths`, `prob.theoretical.equally-likely` | mc: three sale signs |
| `mis.notation.letter-as-object` | Reads a letter as an object or a label rather than a number (a = apples) | `algebra.notation.write` | mc: what a stands for |
| `mis.notation.juxtaposition-as-digits` | Reads 3n with n = 4 as 34 instead of 3 × 4 | `algebra.expressions.substitute` | numeric blank; binding catches 34 |
| `mis.like-terms.combine-unlike` | Combines unlike terms (2a + 3b = 5ab) | `algebra.expressions.like-terms` | mc |
| `mis.like-terms.adds-to-power` | Collects repeated addition as a power (x + x = x²) | `algebra.expressions.like-terms` | mc |
| `mis.equations.same-operation` | Applies the operation shown instead of its inverse (x + 5 = 12 → x = 17) | `algebra.equations.one-step`, `algebra.equations.two-step`, `algebra.formulae.rearrange` | numeric blank; binding catches 17 |
| `mis.equations.partial-divide` | Divides only some terms on one side (2x + 7 = 31 → x + 7 = 15.5) | `algebra.equations.two-step` | numeric blank; error analysis (the two-solvers hook) |
| `mis.equations.one-side-only` | Applies an operation to one side of the equation only | `algebra.equations.two-step` | numeric blank; error analysis |
| `mis.coord.axes-swapped` | Plots or reads (x, y) as (y, x) | `coord.four-quadrant`, `pattern.linear.graph`, `geom.transform.reflect`, `geom.transform.rotate`, `geom.transform.translate` | graph or coordinate blank |
| `mis.pattern.step-as-rule` | Writes the step as an added constant (“add 3” written as t = n + 3) | `pattern.linear.rule` | mc: the rule |
| `mis.pattern.first-term-as-constant` | Uses the first term as the constant d (t = 3n + 5 when the first term is 5) | `pattern.linear.rule`, `pattern.linear.graph` | mc: the rule; graph: read d |
| `mis.pattern.assumes-proportional` | Treats a linear pattern as proportional, multiplying the first term by n (6, 10, 14 … → 20 tables seat 120) | `pattern.linear.rule` | numeric blank; binding catches 120 (the hui-tables hook) |
| `mis.perimeter.counts-squares` | Counts the squares along the edge instead of the unit lengths, so corners are counted twice or missed | `measure.perimeter.polygons` | numeric blank on a grid figure |
| `mis.area.same-perimeter-same-area` | Assumes shapes with equal perimeters have equal areas | `measure.perimeter.polygons`, `measure.area.rect-triangle` | mc: the māra kai beds |
| `mis.area.triangle-no-half` | Leaves out the half in ½ × base × height | `measure.area.rect-triangle`, `measure.area.composite` | numeric blank |
| `mis.area.slant-as-height` | Uses the slant side as the height of a triangle | `measure.area.rect-triangle`, `measure.area.composite` | numeric blank on a figure |
| `mis.units.area-as-linear` | Gives an area in linear units (cm, not cm²) | `measure.area.rect-triangle`, `measure.area.composite` | FORM error: mc with the linear-unit option, or the unit-bearing answer type on an item that demands units; never a numeric blank (§7) |
| `mis.area.composite-overlap` | Counts a region twice when splitting a composite shape | `measure.area.composite` | numeric blank |
| `mis.units.volume-as-square` | Gives a volume in square units (cm², not cm³) | `measure.volume.cuboid` | FORM error: mc with the square-unit option, or the unit-bearing answer type on an item that demands units; never a numeric blank (§7) |
| `mis.volume.adds-dimensions` | Adds length, width and height instead of multiplying them | `measure.volume.cuboid` | numeric blank |
| `mis.time.decimal-hours` | Treats hours and minutes as a decimal (1:30 as 1.30 h; 13:20 − 10:45 = 2.75) | `measure.time.duration`, `measure.time.timetables` | numeric blank; binding catches 2.75 |
| `mis.time.24h-convert` | Converts 24-hour time by subtracting 10 (15:00 = 5 pm) | `measure.time.duration`, `measure.time.timetables` | mc |
| `mis.triangle.orientation-matters` | Believes turning a triangle changes its type (a tilted isosceles triangle is not isosceles) | `geom.triangles.classify` | mc on a rotated figure |
| `mis.angles.sum-depends-on-size` | Believes a larger triangle has a larger angle sum | `geom.angles.triangle-quad-sum` | mc: two triangles, not to scale |
| `mis.angles.vertical-as-supplementary` | Treats vertically opposite angles as adding to 180° instead of being equal | `geom.angles.relationships` | numeric blank; angle labelled x |
| `mis.angles.complement-supplement-swapped` | Uses 180° for complementary angles, or 90° for supplementary | `geom.angles.relationships` | numeric blank; angle labelled x |
| `mis.parallel.all-equal` | Believes every angle where a transversal crosses parallel lines is equal | `geom.angles.parallel-transversal` | numeric blank |
| `mis.parallel.assumed` | Applies parallel-line angle rules to lines not marked parallel | `geom.angles.parallel-transversal` | mc: “cannot be found” as the correct option |
| `mis.reflect.translates` | Slides the shape instead of flipping it in the mirror line | `geom.transform.reflect` | graph or mc |
| `mis.reflect.diagonal-as-vertical` | Reflects in a diagonal mirror line as if it were vertical or horizontal | `geom.transform.reflect` | graph or mc |
| `mis.reflect.half-turn-confused` | Confuses a reflection with a 180° rotation | `geom.transform.reflect`, `geom.transform.rotate` | mc: which transformation maps A to B |
| `mis.rotate.centre-ignored` | Rotates about a vertex or the middle of the shape instead of the given centre | `geom.transform.rotate` | graph or mc |
| `mis.translate.counts-gaps` | Counts the empty squares between the shape and its image instead of how far one vertex moves | `geom.transform.translate` | graph or mc |
| `mis.nets.any-six-squares` | Believes any arrangement of six squares folds into a cube | `geom.nets.identify` | mc: which nets fold |
| `mis.stats.digits-are-numerical` | Classifies data labelled with numbers as numerical (postcodes, jersey numbers) | `stats.variables.classify` | mc |
| `mis.display.order-meaningful` | Reads a trend across categories whose order means nothing | `stats.display.categorical`, `stats.display.dot-plot` | mc |
| `mis.timeseries.joins-categories` | Uses a line graph for categorical data | `stats.display.categorical`, `stats.display.time-series` | mc: choose the display |
| `mis.mean.drops-zeros` | Leaves zero values out when calculating the mean | `stats.summary.mean` | numeric blank |
| `mis.summary.measures-swapped` | Calculates one summary measure when another is asked for | `stats.summary.mean`, `stats.summary.median-mode`, `stats.summary.range` | numeric blank; binding catches the other measure's value |
| `mis.median.unsorted` | Takes the middle value without putting the data in order first | `stats.summary.median-mode` | numeric blank |
| `mis.median.even-count` | With an even number of values, picks one of the two middle values instead of their mean | `stats.summary.median-mode` | numeric blank |
| `mis.range.as-interval` | Writes the range as an interval (“3–12”) instead of a single value | `stats.summary.range` | mc with “3–12” as an option |
| `mis.outlier.affects-median-equally` | Believes an outlier changes the median as much as the mean | `stats.summary.outlier-effect` | mc |
| `mis.prob.order-ignored` | Counts outcomes that differ only in order as one (HT and TH) | `prob.sample-space.list` | numeric blank: how many outcomes |
| `mis.prob.equiprobability` | Treats all outcomes as equally likely when they are not (a dice total of 2 as likely as 7) | `prob.theoretical.equally-likely` | mc |
| `mis.prob.complement-as-reciprocal` | Finds P(not A) as 1 ÷ P(A) instead of 1 − P(A) | `prob.complement` | numeric blank |
| `mis.prob.small-sample-exact` | Expects the theoretical result exactly from a small number of trials (exactly 5 heads in 10) | `prob.experimental.relative-frequency`, `prob.experimental.large-numbers` | mc |
| `mis.prob.gamblers-fallacy` | Believes a result is “due” after a run of the other result | `prob.experimental.large-numbers` | mc |

## Before this goes near the graph

- [x] Zan reads it end-to-end (3 Oct 2026: read and approved).
- [x] Phase 3 page open: both *Verify* items resolved, and `nzc_phase` drafted per skill
  (`proposals/y7-nzc-phase.md`, accepted by Zan 1 Oct).
- [x] Misconception proposals screened (1 Oct, Zan): see "Misconception screening (1 Oct)" above.
- [x] Thread ids approved (30 Sep, `proposals/threads-registry.md`). The D39 migration still lands first.
- [x] Y7 DoL default ruled (29 Sep): D41 in `decision-log-additions.md`.
