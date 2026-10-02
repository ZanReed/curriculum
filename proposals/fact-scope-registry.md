# Fact-scope registry: first draft (families, scope, criteria, templates)

`status: draft` (proposal; not yet in the graph). R1–R4 were ruled as D43 items 27–30
(curriculum PR #15, merge `8c108e5`). The placeholder fix from the builder's 2 Oct review is in
section 2, and the fact counts were re-run against the rewritten rows on 2 Oct: all twelve are
unchanged. Written 2 Oct 2026 for the 1 December artifacts (the platform's A4 ruling). It
follows D43 items 2, 9 and 12–26 as drafted (third to seventh amendments). Field names are
working names. The courier maps them into the graph's key when it commits.

**Sources, read 2 Oct 2026** (statement text quoted from the pages):
- NZC Phase 2 (Years 4–6), Number: https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---mathematics-and-statistics-phase-2/5637239084.p
- NZC Phase 3 (Years 7–8): S-numbers from `proposals/y7-nzc-phase.md`; Y8 lines read from the same page
- NZC Phase 4 (Years 9–10), Number: https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---mathematics-and-statistics-phase-4-years-9-10/5637291579.p

**The Phase 2 and 4 quotes were read through a summarising fetch, not a browser.** They need the
same verbatim check `proposals/y7-nzc-phase.md` passed before anything cites them as S-numbers.

---

## 1. Rulings (ruled: D43 items 27–30, merge `8c108e5`)

Kept here as the reasoning record. The decision log's items 27–30 are the authority.

**R1. What earns a place in the registry.** Most of the fact load sits in **Phase 2**, not
Phase 3 or 4. Phase 2 is the only phase that uses the word *memorising*:

> Year 4: "Memorising multiplication and corresponding division facts for 2s to 10s"
> Year 5: "Memorising multiplication and corresponding division facts for 2s to 12s"
> Year 6: "Memorising the square numbers to 144 and cube numbers to 125"
> Year 6: "Memorising decimal and percentage equivalents of common fractions (1/2, 1/4, 3/4,
> 1/5, 2/5, 3/5, 4/5) including fractions with denominators that are 10 or 100"

Phases 3 and 4 add **finite recall extensions** of these:
- square roots of perfect squares (S33, Y7);
- cube roots (Y8: "Evaluating square and cube roots for perfect squares and cubes");
- integer operations, which are the same facts plus a sign rule (Y8: "Evaluating expressions
  involving negative numbers, addition, and subtraction (e.g. 3 + −7)"; Y9: "Adding,
  subtracting, multiplying, and dividing integers").

*Proposed rule:* a family is in the registry only if it is **a finite set the curriculum asks to
be memorised, or a finite sign-rule or inverse extension of one**. Unbounded procedures go to
mixed practice.

*Consequence:* **×/÷ by powers of 10 (S54) leaves the sprint**, just as primes and factors left it
in item 19. It's a place-value procedure over unlimited numbers, so per-fact mastery records
would never build up. This changes D43's working list a second time.

**R2. Phase 2 families in the Y7 scope.** The registry tags each family with its **source year**.
Y4–6 families come from Phase 2, so this side doesn't teach them. **Probes exist for Y7–10
only**, and the Y7 probe covers every Phase 2 family. This matches ruling 8 (the Y7 entry bank
is Phase 2 facts plus `ext.*` items) and is the problem Zan raised at the start: students
reaching Y7+ without these facts.

**R3. 12s merged with 2s–10s.** The Y4 (2s–10s) and Y5 (2s–12s) lines become **one
multiplication family and one division family to 12**, each with source year Y5. Splitting them
would add two families to every probe (10 more items) for one pedagogical difference. The ×11
and ×12 strategy can sit inside the family's strategy text.

**R4. Probe length at Y9–10.** With R1–R3 the cumulative scope is 7 families at Y7, 10 at Y8
and 12 at Y9–10. Items 20 and 22 then give probes of **35, 50 and 60 items**. At typical recall
times a 60-item probe takes about 4–5 minutes. The worst case (every item at the 15 s ceiling)
is 15 minutes, which is more than item 24's "about 12". Options:
- (a) accept 60, since it's once a term and item 24 already allows a separate sitting;
- (b) lower the per-family minimum from 5 to 4 (48 items at Y9–10).

*Recommendation: (a).* With 4 items, the probe's met / not met call per family (item 23) rests on
3 of 4, which is too thin even for a cheap strategy display.

---

## 2. Families

**Placeholder rule.** `{a}` and `{b}` in a template **always mean the operands as displayed**:
`{a}` is the first number shown and `{b}` the second. **Answer** is what fills `__`. Each family is
*generated* from variables **x** and **y**. The table gives the generating range, then how
`{a}`, `{b}` and the answer are formed from x and y. The generator and the templates never
share variable names.

Ranges are inclusive. The **criterion** is net seconds per fact (items 2 and 14). The criteria
are working values for the 1 December artifact, not researched cut-offs (see section 4).

| id | teacher name | source year | generated from | `{a}` | `{b}` | answer | turnaround (item 9) | facts | criterion |
|---|---|---|---|---|---|---|---|---|---|
| `fact.mult.to-12` | Multiplication to 12 × 12 | Y5 (Phase 2) | x, y ∈ 2–12 | x | y | x·y | yes | 66 | 3 s |
| `fact.div.to-12` | Division to 144 ÷ 12 | Y5 (Phase 2) | x, y ∈ 2–12 | x·y | x | y | no | 121 | 4 s |
| `fact.square.to-144` | Square numbers to 144 | Y6 (Phase 2) | x ∈ 2–12 | x | — | x² | — | 11 | 3 s |
| `fact.cube.to-125` | Cube numbers to 125 | Y6 (Phase 2) | x ∈ 1–5 | x | — | x³ | — | 5 | 3 s |
| `fact.fdp.to-decimal` | Common fractions as decimals | Y6 (Phase 2) | x/y ∈ {1/2, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5, 1/10, 3/10, 7/10, 9/10} | x | y | x ÷ y as a decimal | — | 11 | 3 s |
| `fact.fdp.to-percent` | Common fractions as percentages | Y6 (Phase 2) | same 11 fractions | x | y | 100x ÷ y | — | 11 | 3 s |
| `fact.root.square` | Square roots to √144 | Y7 (S33) | x ∈ 2–12 | x² | — | x | — | 11 | 4 s |
| `fact.root.cube` | Cube roots to ∛125 | Y8 | x ∈ 1–5 | x³ | — | x | — | 5 | 4 s |
| `fact.int.add` | Adding integers | Y8 | x, y ∈ −10–10, both ≠ 0, at least one negative | x | y | x + y | yes | 155 | 5 s |
| `fact.int.subtract` | Subtracting integers | Y8 | x, y ∈ −10–10, both ≠ 0; excludes x > 0, y > 0 with x ≥ y (plain whole-number subtraction) | x | y | x − y | no | 345 | 5 s |
| `fact.int.multiply` | Multiplying integers | Y9 | \|x\|, \|y\| ∈ 2–10, at least one negative | x | y | x·y | yes | 126 | 4 s |
| `fact.int.divide` | Dividing integers | Y9 | \|x\|, \|y\| ∈ 2–10; at least one of `{a}`, `{b}` negative | x·y | x | y | no | 243 | 5 s |

Fact counts were computed by script under these exact rules, from the displayed operands, with
turnaround pairs counted once. They were re-run after the placeholder rewrite: 66, 121, 11, 5,
11, 11, 11, 5, 155, 345, 126, 243, all unchanged. The generator will recompute them, so they're
here as a check, not as authored values.

**Range notes:**
- **Exclusions:** ×0 and ×1 are excluded from multiplication and division because they need no
  recall. 1³ and ∛1 stay in, so the cube families have five facts (item 22: the minimum is
  5 or the family's fact count, whichever is smaller).
- **Fractions:** the tenths that simplify (2/10, 4/10, 5/10, 6/10, 8/10) are left out because
  they repeat a fifth or a half. **Hundredths are left out entirely:** 37/100 = 0.37 is place
  value, not recall.
- **Integer magnitudes:** these stop at 10 because the integer families test the *sign rule*
  on facts the student already knows. They aren't a second times table.
- **Turnaround** (item 9) is judged on the displayed operands: 7 × 8 and 8 × 7 are one fact.
  For division, 56 ÷ 7 and 56 ÷ 8 are different facts.

---

## 3. Year scope

| year | adds | cumulative families | probe items (item 20) |
|---|---|---|---|
| Y7 | `fact.root.square`, plus all six Phase 2 families (source Y5–6) | 7 | 35 |
| Y8 | `fact.root.cube`, `fact.int.add`, `fact.int.subtract` | 10 | 50 |
| Y9 | `fact.int.multiply`, `fact.int.divide` | 12 | 60 |
| Y10 | none | 12 | 60 |

**Teacher descriptions (optional, item 18):**
- Y7: "Times tables, squares, cubes, fraction equivalents and square roots"
- Y8: adds "cube roots and adding and subtracting negatives"
- Y9–10: adds "multiplying and dividing negatives"

**Y10 adds nothing.** Phase 4's Y10 lines (index laws, surds, irrational numbers) are known
results and procedures, so they belong in mixed practice. The working list already said this
for Y11–13.

---

## 4. Single values (item 15 graph keys)

| key | value | source |
|---|---|---|
| floor factor *k* | 0.8 | item 12 |
| accuracy threshold | 0.90 | item 13 |
| facts-met threshold | 0.80 | item 13 |
| response ceiling | 15 s | item 15 |
| minimum items per family | 5 | item 20 / 22 |
| practice window | 10 attempts | item 20 |

**Where the criteria come from.**
- **3 s for single recall.** This is the common working definition of an automatic fact in
  fluency programmes.
- **4 s for inverse families** (division and roots), which are typically solved through the
  forward fact (Campbell's work on division).
- **5 s for integer addition, subtraction and division,** which take a recalled fact plus a
  sign decision. Integer multiplication gets 4 s, because its sign rule is a single
  even/odd check.

All of these are first values to recalibrate against classroom data. The floor follows
automatically from them (item 12).

---

## 5. Templates (item 26)

The platform applies the true minus sign and the brackets round a negative second operand
(item 21), and it says the numbers aloud. Spoken forms say "negative" for a number's sign and
"minus" for subtraction.

| id | display | spoken |
|---|---|---|
| `fact.mult.to-12` | `{a} × {b} = __` | "{a} times {b}" |
| `fact.div.to-12` | `{a} ÷ {b} = __` | "{a} divided by {b}" |
| `fact.square.to-144` | `{a}² = __` | "{a} squared" |
| `fact.cube.to-125` | `{a}³ = __` | "{a} cubed" |
| `fact.fdp.to-decimal` | `{a}/{b} = __` (decimal) | "{a} {b-fraction-name} as a decimal" |
| `fact.fdp.to-percent` | `{a}/{b} = __ %` | "{a} {b-fraction-name} as a percentage" |
| `fact.root.square` | `√{a} = __` | "the square root of {a}" |
| `fact.root.cube` | `∛{a} = __` | "the cube root of {a}" |
| `fact.int.add` | `{a} + {b} = __` | "{a} plus {b}" |
| `fact.int.subtract` | `{a} − {b} = __` | "{a} minus {b}" |
| `fact.int.multiply` | `{a} × {b} = __` | "{a} times {b}" |
| `fact.int.divide` | `{a} ÷ {b} = __` | "{a} divided by {b}" |

**`{b-fraction-name}`: a third placeholder, used only by the two fraction families.** It speaks
the denominator `{b}` as a fraction name, which the platform's number-speaking can't produce. The
curriculum side defines the words, so the rule is part of this registry:

| `{b}` | `{a}` = 1 | `{a}` > 1 |
|---|---|---|
| 2 | half | halves |
| 4 | quarter | quarters |
| 5 | fifth | fifths |
| 10 | tenth | tenths |

Singular when `{a}` is 1, plural otherwise. So 3/4 is "three quarters as a decimal" and 1/2 is
"one half as a percentage". `{a}` is still spoken by the platform as a number. A denominator
outside this table is an error that the generator should catch. NZ usage is "quarter", not
"fourth".

**Strategy text** (item 18) isn't in this revision. It's required before the sprint goes live,
one paragraph per family, and is the next authoring piece after the R-rulings.

---

## 6. Shape sketch (one family, for the courier)

```json
{
  "id": "fact.int.subtract",
  "name": "Subtracting integers",
  "source_year": 8,
  "operation": "subtract",
  "generate": { "x": { "min": -10, "max": 10, "exclude": [0] },
                "y": { "min": -10, "max": 10, "exclude": [0] },
                "constraint": "not (x > 0 and y > 0 and x >= y)" },
  "shown": { "a": "x", "b": "y" },
  "answer": "x - y",
  "turnaround": false,
  "criterion_s": 5,
  "weight": 1,
  "display": "{a} − {b} = __",
  "spoken": "{a} minus {b}",
  "strategy": null
}
```

The `constraint` is written as plain text here. Whether it becomes a small expression language
or a set of named flags (`at_least_one_negative`, `exclude_plain_whole`) is the courier's call
when encoding. It is an engineering choice, and this side only fixes the meaning.
