---
chains_superseded: 2026-10-21 by D70 (two chains: 904-chain.algebra.manipulation, 905-chain.algebra.solving); the skills, misconceptions and edges below stand, plus D72's edge
status: ratified 2026-10-20 (D58), in the graph at v0.18.0; misconceptions ratified 2026-10-21 (D59, 14 ids)
written_against: ZanReed/curriculum main @ 2990ba1 (20 Oct 2026), graph v0.17.27
depends_on: D55 and D56 (decision-log-additions.md); D43 amendment 2026-10-20 item 3
---

# Y9 Algebra: Expressions and Equations — chain stubs

Ratified by Zan item by item (D55–D63; working list `proposals/overhaul-decision-items.md`).
Changes since the draft: a 14th misconception id (D59), and `index` takes both `power` and
`exponent` as variants (D62).

**Sources.**
- Read from `main` @ `2990ba1`: `README.md`, `curriculum-graph.json` (v0.17.27),
  `authoring-principles.md` (§2, §7), `decision-log-additions.md` (D38, D42, D45, D46, D47, D48),
  `glossary.md`, `chain-registry.txt`, `docs/alignment-sources.md`,
  `external-prereq-registry.txt`, `skill-ids-retired.txt`, and the format of
  `proposals/y7-chain-stubs.md`.
- The school's 2026 Y9 Algebra scheme and student overview, the 2025 Y9 algebra scheme and
  timeline, and the 2026 Y10 Algebra scheme. These are held in the Claude project. They are not
  quoted here because this repo is public.
- NZC Phase 4 page (`https://newzealandcurriculum.tahurangi.education.govt.nz/5637291579.p`).
  The draft used a summarising fetch. Under D63, its own text was read on 2026-10-21 and Zan
  checks each statement (`proposals/d63-nzc-phase4-check-sheet.md`).

## Conventions used

- Same table shape as the Y7 stubs: skill, label, prereqs, misconceptions, parts. Ids follow
  `domain.sub.skill`. All 12 skill ids are new and checked against the graph and
  `skill-ids-retired.txt`.
- `band_nz: Y9` for every skill (D55 item 4: the school's year). `band_us`, `ccss` and `teks`
  are empty (D36). `ncea` is `null` (unread), not `[]`.
- `thread.algebra-equations` for every chain. `calculator: off` for every chain: integer and
  fraction work, with nothing the stance against hand calculation forbids.
- **School tier code** (D55 item 5): section and tier only, with no quoted scheme text.
  Section letters follow the school's overview (A1 Collecting … A10 Words to Expressions).
- **The spiral (Y10 folder):** every skill here reappears as the school's **Y10 Developing**
  tier. The Y9 activities double as Y10's opening review, so no Y10 copies are needed.
- **Parts (D48):** each skill below names its one idea. Every skill is 1 part. Ideas that build on
  each other are separate skills (ruling 4). A size-floor call is flagged where it is close
  (ruling 8).
- Hooks: none yet. The unit's concept bank comes next (D56).

## Summary

| chain (provisional folder) | title | skills | activities |
|---|---|---|---|
| `904-chain.algebra.terms` | Multiplying and Dividing Terms | 2 | 2p + 1c |
| `905-chain.algebra.brackets` | Expanding and Factorising | 3 | 3p |
| `906-chain.algebra.equations-multistep` | Solving Multi-Step Equations | 3 | 3p |
| `907-chain.algebra.forming` | Forming Equations and Rearranging Formulae | 2 | 2p |
| `908-chain.algebra.inequations` | Inequations | 2 | 2p |
| **unit total** | | **12** | **12p + 1c = 13** |

There are five chains, not the four first proposed. Forming equations and two-step rearranging
are the school's sections A8–A10 at Consolidating/Proficient, so they got a chain of their own,
and the equations chain doesn't carry five skills.

**Fit to the unit.** The school ran this unit in 14–17 lessons in 2025, test included. Thirteen
activity periods leave 1–4 periods for review of the Y7 Developing tier
(`707-chain.algebra.expressions`, `708-chain.algebra.equations`), revision and the test. This
fits, but tightly. D49's period kinds decide the final count, not this file.

Ordinals 904–908 sit after the linear chains (901–903), which is not the intended teaching order.
They are placeholders under D55 item 6, renumbered in one pass once the planner exists.

---

### `chain.algebra.terms`: 3 activities (2p + 1c)

| skill | label | prereqs | misconceptions | parts | school tier |
|---|---|---|---|---|---|
| `algebra.terms.multiply` | Multiply algebraic terms: multiply the coefficients and add the indices of the same letter (4a × 3b = 12ab, c² × c⁵ = c⁷, 4ab² × 3ab⁵ = 12a²b⁷) | `algebra.notation.write`, `number.exponents.evaluate` | `mis.terms.coefficients-added`; `mis.terms.product-as-sum`; `mis.exponent.indices-multiplied` | 1 | A2 D–C (P: area of a rectangle) |
| `algebra.terms.divide` | Divide algebraic terms written as a fraction: divide the coefficients, subtract the indices of the same letter, and cancel (p⁶ ÷ p² = p⁴, 16ab² ÷ 4a²b = 4b/a) | `number.exponents.evaluate`, `number.fractions.equivalent` | `mis.exponent.indices-divided`; `mis.algebra.cancelled-to-zero` | 1 | A3 D–P (P: side from area; mixed × and ÷) |

- **Idea per skill.** Multiply: "a product of terms is one term, with like letters gathered into
  a power". Divide: "a quotient of terms simplifies like a fraction, cancelling common factors".
- **No edge from multiply to divide.** p⁶ ÷ p² can be done by writing out the factors and
  cancelling, without ever having multiplied powers. Under §2 a sequencing preference is not an
  edge. The order of the two activities in the chain still puts multiply first.
- **Pair rule.** `mis.terms.product-as-sum` (a × a = 2a) mirrors the existing
  `mis.like-terms.adds-to-power` (x + x = x²). Each label is one-sided and names its direction,
  so each attaches only to the skill where that direction occurs (§7's "reword to say so"
  route).
- **NZC year mismatch (D55 item 4).** The NZC states exponent rules in Y10 Number. Y9 Algebra
  covers manipulating expressions "involving positive integer powers", which covers c² × c⁵ by
  structure. The school teaches the laws in Y9. Powers of powers ((a²)³) was in the 2025 scheme
  and is dropped from 2026, so it is left out.
- **Consolidation (D57).** "Collect or multiply?" discriminates `algebra.expressions.like-terms`
  (chain 707) and `algebra.terms.multiply`, with `algebra.terms.divide` as a third option once
  taught. The named confusion is 2a + 3a = 5a² and 2a × 3a = 6a.

### `chain.algebra.brackets`: 3 activities (3p)

| skill | label | prereqs | misconceptions | parts | school tier |
|---|---|---|---|---|---|
| `algebra.expand.single` | Expand a single bracket with a positive multiplier, including a letter multiplier (2(x + 3) = 2x + 6, x(x + 3) = x² + 3x) | `algebra.terms.multiply` | `mis.expand.first-term-only` | 1 | A4 D |
| `algebra.expand.negative` | Expand a bracket with a negative multiplier, and expand and simplify two brackets (−4(3b + 2c), 5(x + 4) − 2(3x − 5)) | `algebra.expand.single`, `algebra.expressions.like-terms`, `ext.arith.signed` | `mis.expand.first-term-only`; `mis.expand.negative-sign-dropped` | 1 | A4 C–P |
| `algebra.factorise.common-factor` | Factorise by taking out the highest common factor, including letters, and check by expanding (18x − 12 = 6(3x − 2), x²y³ − 2x = x(xy³ − 2)) | `algebra.expand.single`, `algebra.terms.divide`, `number.factors.hcf-lcm` | `mis.factorise.not-highest`; `mis.algebra.cancelled-to-zero` | 1 | A5 D–P (P: simplify, then factorise) |

- **Two expand skills, not two parts (D48 ruling 4).** The negative multiplier builds on the
  positive case and has its own prerequisite (signed multiplication). −4(3b + 2c) and
  −2(3x − 5) are where nearly all expanding errors live, and expand-and-simplify adds a
  collecting step.
- **`ext.arith.signed`** is the only route to multiplying signed numbers: no integer
  multiply/divide skill exists (D45 item 2 is still open; the D63 read puts it in NZC Y9).
- **`mis.algebra.cancelled-to-zero`** is one error with two faces: 8a ÷ 8a = 0 on divide, and
  3x + 3 = 3(x) on factorise. Under §7 it attaches to both skills, as a single id.

### `chain.algebra.equations-multistep`: 3 activities (3p)

| skill | label | prereqs | misconceptions | parts | school tier |
|---|---|---|---|---|---|
| `algebra.equations.both-sides` | Solve linear equations with the unknown on both sides (5x − 3 = 2x + 9), and check by substituting | `algebra.equations.two-step`, `algebra.expressions.like-terms` | `mis.equations.same-operation`; `mis.equations.one-side-only` | 1 | A6 C |
| `algebra.equations.brackets` | Solve linear equations that contain brackets, including a negative multiplier, by expanding first (5x + 3(x − 4) = 7x + 2) | `algebra.equations.both-sides`, `algebra.expand.negative` | `mis.expand.first-term-only`; `mis.expand.negative-sign-dropped`; `mis.equations.same-operation` | 1 | A6 P |
| `algebra.equations.fraction-coefficients` | Solve linear equations with fractional coefficients and rational solutions (x/3 + 2 = 5, −⅖x + 3 = 11, 3x = 7 → x = 7/3) | `algebra.equations.two-step`, `number.fractions.equivalent`, `ext.arith.fractions` | `mis.equations.fraction-coefficient-partial`; `mis.equations.partial-divide` | 1 | A6 P |

- **Error reused, not a new id.** Moving 2x across as +2x (5x − 3 = 2x + 9 → 7x − 3 = 9) is the
  existing `mis.equations.same-operation`: applying the operation shown instead of its inverse.
- **Size floor (D48 ruling 8). Its own skill for now (D58).** `algebra.equations.brackets` is
  "expand, then it's a both-sides equation". The only realistic fold is into
  `algebra.equations.both-sides`, which would then take the `algebra.expand.negative` edge and
  move after the brackets chain. The trigger to revisit is D48 test 2 run in reverse: if the
  drafted worked and faded sequence leaves most of the phase budget empty, it folds.
- **Rational solutions belong here, not in both-sides.** The NZC Y9 statement is "rational
  number coefficients". Y7 equations are integer-only by label.

### `chain.algebra.forming`: 2 activities (2p)

| skill | label | prereqs | misconceptions | parts | school tier |
|---|---|---|---|---|---|
| `algebra.equations.form-from-words` | Form a linear equation from a worded or geometric situation (perimeter, angles, consecutive numbers), solve it, and answer in context | `algebra.notation.write`, `algebra.equations.two-step` | `mis.forming.order-reversed` | 1 | A10 P (E: worded problems) |
| `algebra.formulae.rearrange-two-step` | Rearrange a two-step formula to make another letter the subject (P = 2l + 2w for w), and find an unknown by substituting first and then solving | `algebra.formulae.rearrange` | `mis.equations.partial-divide`; `mis.equations.same-operation` | 1 | A8 C; A9 P |

- **Pair rule touches a Y7 skill.** "Five less than n" written as 5 − n happens on
  `algebra.notation.write` as much as here, so `mis.forming.order-reversed` attaches to both
  (D59). The platform gets a pre-merge notice, because attachments reach the AI grader.
- **The Y7 skill is one step.** `algebra.formulae.rearrange` (P = 4s → s = P/4) covers the
  school's A8 Developing row. A8 Consolidating is the NZC's own Y9 example, P = 2l + 2w, which
  needs the two-step idea.
- **Geometric contexts are deliberate.** They give the measurement unit ("missing side given
  perimeter, must show algebraic working") and the geometry unit (algebraic angles) a skill to
  point their review at.

### `chain.algebra.inequations`: 2 activities (2p)

| skill | label | prereqs | misconceptions | parts | school tier |
|---|---|---|---|---|---|
| `algebra.inequations.solve` | Solve linear inequations with positive coefficients, including the unknown on both sides, and show the solution set on a number line (3x − 5 < 19, 5x − 3 ≥ 2x + 9) | `algebra.equations.both-sides`, `number.integers.number-line` | `mis.inequations.answer-as-equation`; `mis.inequations.endpoint-type`; `mis.inequations.sign-reversed-unneeded`; `mis.equations.same-operation` | 1 | A7 D–C |
| `algebra.inequations.negative-coefficient` | Solve linear inequations where multiplying or dividing by a negative number reverses the sign (−2x < 6, −3x − 5(x + 2) < 19) | `algebra.inequations.solve`, `ext.arith.signed` | `mis.inequations.sign-not-reversed`; `mis.inequations.sign-reversed-unneeded`; `mis.inequations.answer-as-equation` | 1 | A7 P |

- **Banding disagreement (D55 item 4).** The school teaches the reversal in Y9 Proficient. The
  NZC Y9 statement covers only multiplying or dividing by −1, and the general rule is Y10
  knowledge. So `band_nz` is Y9, and the `nzc_phase` pointers name both statements.
- **Number line, beyond the school.** The school's Y9 overview never draws one. The NZC's Y10
  knowledge and practice ask for it (S35, S36), and the shipped `numberline` capability is the
  carrier for `mis.inequations.endpoint-type`.
- **Vocabulary.** The school's word, *inequation*, with *inequality* as a glossary variant.

---

## Carriers: where equivalence grading reports wrong answers as right (D60, now §7)

`fill_blank` with `==` grades by math equivalence. For a skill whose point is the **form** of the
answer, equivalence accepts the question itself:
- "Factorise 18x − 12": typing `18x − 12` is equivalent, so it is marked right. So is the
  `mis.factorise.not-highest` answer `2(9x − 6)`.
- "Simplify 4a × 3b": typing `4a*3b` is equivalent, so it is marked right.

So for `algebra.terms.*`, `algebra.expand.*` and `algebra.factorise.common-factor`:
- **Use `gap_equation` with number or term gaps inside the target form**, e.g.
  `18x − 12 = \gap{6}(3x − \gap{2})`, for faded beats and independent practice.
- **Use exact-match `fill_blank` alternates (`|`), not `==`,** for a whole typed answer. List the
  acceptable orderings (12ab | 12ba).
- **Use `mc` for DoL items that carry a misconception binding.** The distractor is the
  misconception's answer, e.g. 2(9x − 6), 7ab, c¹⁰.
- **Platform wish (on the to-do list, not sent):** grade "equivalent *and* in a stated form".

Equation and inequation answers are values (x = 4, x < 8), so `fill_blank` and `numberline` work
as normal. `x < 8` versus `x = 8` needs exact alternates, not `==`.

## Misconceptions (14 new ids, D59)

| id | attaches to | carrier |
|---|---|---|
| `mis.terms.coefficients-added` | `algebra.terms.multiply` | mc |
| `mis.terms.product-as-sum` | `algebra.terms.multiply` | mc |
| `mis.exponent.indices-multiplied` | `algebra.terms.multiply` | mc; gap on the index |
| `mis.exponent.indices-divided` | `algebra.terms.divide` | mc; gap on the index |
| `mis.algebra.cancelled-to-zero` | `algebra.terms.divide`, `algebra.factorise.common-factor` | mc |
| `mis.expand.first-term-only` | `algebra.expand.single`, `algebra.expand.negative`, `algebra.equations.brackets` | mc; gap |
| `mis.expand.negative-sign-dropped` | `algebra.expand.negative`, `algebra.equations.brackets` | mc; gap |
| `mis.factorise.not-highest` | `algebra.factorise.common-factor` | mc only |
| `mis.equations.fraction-coefficient-partial` | `algebra.equations.fraction-coefficients` | fill_blank wrong-answer map; mc |
| `mis.forming.order-reversed` | `algebra.equations.form-from-words`, `algebra.notation.write` | mc |
| `mis.inequations.answer-as-equation` | `algebra.inequations.solve`, `algebra.inequations.negative-coefficient` | fill_blank exact alternates; mc |
| `mis.inequations.endpoint-type` | `algebra.inequations.solve` | numberline |
| `mis.inequations.sign-not-reversed` | `algebra.inequations.negative-coefficient` | mc; fill_blank |
| `mis.inequations.sign-reversed-unneeded` | `algebra.inequations.solve`, `algebra.inequations.negative-coefficient` | mc; fill_blank |

Labels are in the graph. Existing ids attached to new skills: `mis.equations.same-operation`,
`mis.equations.one-side-only`, `mis.equations.partial-divide`.

## Alignment (D63)

Zan ticked all ten on 2026-10-21. S28–S37 are in `docs/alignment-sources.md`, recorded by cell
location and paraphrase, and the pointers are in the graph from v0.18.1. S34 is cited for the
product and quotient rules only.

## Glossary words (D62; per chain, before that chain's activities)

term, like terms, index (variants: power, exponent), expand, factorise, common factor, highest
common factor, inequation (variant: inequality), solution set, subject (of a formula), formula,
substitute.
