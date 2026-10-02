# Fact-scope registry: first draft (families, scope, criteria, templates)

`status: draft` (proposal; not yet in the graph). Revision 2, 2 Oct: the platform's B-22 points ruled (named flags, fact counts in the file, "as a decimal" shown to students) and the strategy texts added (section 7). Revision 3, 2 Oct: `fact.units` added as a listed family (section 2b; D43 items 31–33). Revision 4, 2 Oct: quote check passed; section 7 approved. Revision 5, 2 Oct: strategy texts stored as structured lines (four reworded and re-approved); the platform's B-23 points (fact ids, family kind, one negative-number flag, Y7 description). R1–R4 were ruled as D43 items 27–30
(curriculum PR #15, merge `8c108e5`). The placeholder fix from the builder's 2 Oct review is in
section 2, and the fact counts were re-run against the rewritten rows on 2 Oct: all twelve are
unchanged. Written 2 Oct 2026 for the 1 December artifacts (the platform's A4 ruling). It
follows D43 items 2, 9 and 12–26 as drafted (third to seventh amendments). Field names are
working names. The courier maps them into the graph's key when it commits.

**Sources, read 2 Oct 2026** (statement text quoted from the pages):
- NZC Phase 2 (Years 4–6), Number: https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---mathematics-and-statistics-phase-2/5637239084.p
- NZC Phase 3 (Years 7–8): S-numbers from `proposals/y7-nzc-phase.md`; Y8 lines read from the same page
- NZC Phase 4 (Years 9–10), Number: https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---mathematics-and-statistics-phase-4-years-9-10/5637291579.p

**Check status: passed, 2 Oct 2026.** Every quoted Phase 2, Phase 3 (Y8) and Phase 4 line was
checked word for word against the live pages by Zan; all matched exactly. The check confirmed
wording, not page position, so these lines are cited by phase, year and strand (Number or
Measurement), not by S-number.

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
| `fact.units` | Unit relationships | Y6 (Phase 2) | enumerated list (section 2b) | — | — | listed | — | 14 | 3 s |

Fact counts were computed by script under these exact rules, from the displayed operands, with
turnaround pairs counted once. They were re-run after the placeholder rewrite: 66, 121, 11, 5,
11, 11, 11, 5, 155, 345, 126, 243, all unchanged. The generator writes each family's count into
the machine-readable file, and the platform's importer stops if its own expansion gives a
different number (ruled by Zan 2 Oct, on the platform's B-22). Nobody types the counts by hand:
they are a guard against the two sides expanding a family differently.

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

### 2b. `fact.units`: an enumerated family (revision 3, 2 Oct 2026)

Admitted under item 27 as clarified by item 32 (ninth D43 amendment). Phase 2's Measurement
Knowledge lines state these as fixed relationships (Y4–5 "There are 1000 millimetres in a
metre…", Y5 prefixes, Y6 conversions including h, min, s). The numeracy co-requisite leans on
them ("simple conversions between units of the same measure"), and a calculator can't supply
them.

**This is the first family whose facts are listed rather than generated.** Each fact carries
its own display string, spoken string and answer, so it needs no `{a}`/`{b}` placeholders. That
is a new family type and goes to the platform as an ask-back. Its count guard (item 31) is the
length of the list. Each listed fact has a stable id, `fact.units.<from>-<to>` with lower-case
unit symbols; once published, an id is never reused for a different fact (the same rule as
misconception ids).

| # | id | display | spoken | answer |
|---|---|---|---|---|
| 1 | `fact.units.cm-mm` | `1 cm = __ mm` | "one centimetre is how many millimetres" | 10 |
| 2 | `fact.units.m-cm` | `1 m = __ cm` | "one metre is how many centimetres" | 100 |
| 3 | `fact.units.m-mm` | `1 m = __ mm` | "one metre is how many millimetres" | 1000 |
| 4 | `fact.units.km-m` | `1 km = __ m` | "one kilometre is how many metres" | 1000 |
| 5 | `fact.units.kg-g` | `1 kg = __ g` | "one kilogram is how many grams" | 1000 |
| 6 | `fact.units.l-ml` | `1 L = __ mL` | "one litre is how many millilitres" | 1000 |
| 7 | `fact.units.mm-cm` | `1 mm = __ cm` | "one millimetre is how many centimetres" | 0.1 |
| 8 | `fact.units.cm-m` | `1 cm = __ m` | "one centimetre is how many metres" | 0.01 |
| 9 | `fact.units.mm-m` | `1 mm = __ m` | "one millimetre is how many metres" | 0.001 |
| 10 | `fact.units.m-km` | `1 m = __ km` | "one metre is how many kilometres" | 0.001 |
| 11 | `fact.units.g-kg` | `1 g = __ kg` | "one gram is how many kilograms" | 0.001 |
| 12 | `fact.units.ml-l` | `1 mL = __ L` | "one millilitre is how many litres" | 0.001 |
| 13 | `fact.units.min-s` | `1 min = __ s` | "one minute is how many seconds" | 60 |
| 14 | `fact.units.h-min` | `1 h = __ min` | "one hour is how many minutes" | 60 |

**Kept out:**
- The reverse time facts (1 s = 1/60 min): they can't be typed as exact answers (item 19).
- Calendar facts (24 h, 7 days, 12 months, 365 days): not in NZC's lines. They go to mixed
  practice.
- Y8 volume and capacity (1 mL = 1 cm³, 1 L = 1000 cm³, 1 m³ = 1000 L): mixed practice, with the
  Y8 volume skill. As its own family it would cost 5 items in every Y8–10 probe.

Spellings follow NZ usage (metre, litre). Unit symbols are written as on the page (mL, L).

---

## 3. Year scope

| year | adds | cumulative families | probe items (item 20) |
|---|---|---|---|
| Y7 | `fact.root.square`, plus all seven Phase 2 families (source Y5–6, including `fact.units`) | 8 | 40 |
| Y8 | `fact.root.cube`, `fact.int.add`, `fact.int.subtract` | 11 | 55 |
| Y9 | `fact.int.multiply`, `fact.int.divide` | 13 | 65 |
| Y10 | none | 13 | 65 |

With `fact.units`, the worst case at Y9–10 is 65 × 15 s, about 16 minutes. Item 30's reasoning
(once a term, own sitting allowed) still applies.

**Teacher descriptions (optional, item 18):**
- Y7: "Times tables, squares, cubes, fraction equivalents, unit relationships and square roots"
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
| `fact.fdp.to-decimal` | `{a}/{b} = __ as a decimal` | "{a} {b-fraction-name} as a decimal" |
| `fact.fdp.to-percent` | `{a}/{b} = __ %` | "{a} {b-fraction-name} as a percentage" |
| `fact.root.square` | `√{a} = __` | "the square root of {a}" |
| `fact.root.cube` | `∛{a} = __` | "the cube root of {a}" |
| `fact.int.add` | `{a} + {b} = __` | "{a} plus {b}" |
| `fact.int.subtract` | `{a} − {b} = __` | "{a} minus {b}" |
| `fact.int.multiply` | `{a} × {b} = __` | "{a} times {b}" |
| `fact.int.divide` | `{a} ÷ {b} = __` | "{a} divided by {b}" |
| `fact.units` | per fact (section 2b) | per fact (section 2b) |

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

**Strategy text** (item 18) is in section 7: form ruled, texts draft.

---

## 6. Shape sketch (one family, for the courier)

```json
{
  "id": "fact.int.subtract",
  "kind": "generated",
  "name": "Subtracting integers",
  "source_year": 8,
  "operation": "subtract",
  "generate": { "x": { "min": -10, "max": 10, "exclude": [0] },
                "y": { "min": -10, "max": 10, "exclude": [0] },
                "flags": ["exclude_plain_whole"] },
  "shown": { "a": "x", "b": "y" },
  "answer": "x - y",
  "turnaround": false,
  "criterion_s": 5,
  "weight": 1,
  "display": "{a} − {b} = __",
  "spoken": "{a} minus {b}",
  "strategy": { "intro": null, "lines": [ { "label": "", "text": "…" } ], "example": "…" }
}
```

Every family carries `kind`, either `generated` (from `generate`/`shown`/`answer`) or `listed`
(from a list of facts, each with id, display, spoken and answer). A family with both or neither
is invalid. Twelve families are `generated`; `fact.units` is `listed`.

**Range rules are named flags, not an expression language (ruled by Zan 2 Oct, on the
platform's B-22).** The platform implements and tests a fixed list. A new flag goes to the
platform as a question first. The families need exactly two:

| flag | meaning (in displayed terms) | families |
|---|---|---|
| `at_least_one_negative` | `{a}` or `{b}`, as displayed, is negative | `fact.int.add`, `fact.int.multiply`, `fact.int.divide` |
| `exclude_plain_whole` | drops facts where `{a}` > 0, `{b}` > 0 and `{a}` ≥ `{b}` | `fact.int.subtract` |

Flags are stated on the displayed operands, so for integer divide `at_least_one_negative` reads
the displayed dividend (x·y) and divisor (revision 5, on the platform's B-23: one flag instead
of two that meant the same thing). Counts re-checked: 155, 126 and 243. Zero exclusions stay as
each operand's `exclude` list, not as flags.

The `{b-fraction-name}` table (section 5) travels in the machine-readable registry as one entry
per denominator with a singular and a plural form; the platform's importer fills it at import
and fails on a missing denominator (platform record CR-22).

---

## 7. Strategy text (revision 5, 2 Oct 2026)

`status: approved.` Option (a) ruled by Zan 2 Oct: one fixed strategy per family, the same for
every fact in the family. Nine texts approved as written by Zan 2 Oct; the four reworded texts
(`fact.mult.to-12`, `fact.units`, `fact.fdp.to-decimal`, `fact.fdp.to-percent`) re-approved by
Zan 2 Oct. Needed before the sprint goes live, not for the probe.

**Stored as structured fields, no markup** (on the platform's B-23). Each family's `strategy`
has `intro` (an optional opening sentence, or `null`), `lines` (one `{ "label", "text" }` per
move; paragraph families have one line with an empty label) and `example` (one worked example in
plain text, or `null` where the lines carry the examples). The platform lays out labels and
lines itself; nothing in the text is markup. Reworded families are lists of moves a student
scans for their own fact; one-idea families stay as a single paragraph line, wording unchanged.

Rules applied:
- §11 language: NZ terms, Y7 reading level.
- "Negative" for a number's sign, "minus" for subtraction (item 26).
- True minus signs, and brackets round a negative second operand (item 21).
- No graph-key values restated (D25).
- No inline definitions (D40); terms are flagged below instead.
- No markup characters (checked by script).

```json
{
  "fact.mult.to-12": {
    "intro": "Don't count up. Start from a fact you know.",
    "lines": [
      { "label": "×2, ×4, ×8", "text": "Double. 4 × 7 is double 2 × 7, so 28. For ×8, double three times." },
      { "label": "×5", "text": "Half of ×10. 5 × 8 is half of 80, so 40." },
      { "label": "×9", "text": "×10, then take away one group. 9 × 6 is 60 − 6, so 54." },
      { "label": "×11, ×12", "text": "×10, then add one or two groups. 12 × 7 is 70 + 14, so 84." },
      { "label": "×3, ×6, ×7", "text": "Build from a fact next door. 6 × 7 is 5 × 7 + 7, so 42." },
      { "label": "Stuck?", "text": "Swap the order. 7 × 8 is the same as 8 × 7." }
    ],
    "example": null
  },
  "fact.div.to-12": {
    "intro": null,
    "lines": [ { "label": "", "text": "Think multiplication. Every division fact is a times-table fact read backwards." } ],
    "example": "For 56 ÷ 7, ask \"what number times 7 makes 56?\" You know 7 × 8 = 56, so 56 ÷ 7 = 8."
  },
  "fact.square.to-144": {
    "intro": null,
    "lines": [ { "label": "", "text": "7² means 7 × 7, so every square is a times-table fact. If you're stuck on a big one, use ×10 and add the extra groups." } ],
    "example": "12² = 12 × 10 + 12 × 2 = 120 + 24 = 144."
  },
  "fact.cube.to-125": {
    "intro": null,
    "lines": [ { "label": "", "text": "4³ means 4 × 4 × 4. Find the square first, then multiply once more. There are only five to know: 1, 8, 27, 64, 125. Say them in order until they stick." } ],
    "example": "4² = 16, and 16 × 4 = 64, so 4³ = 64."
  },
  "fact.fdp.to-decimal": {
    "intro": "Learn four landmarks, then count how many you have.",
    "lines": [
      { "label": "half", "text": "0.5" },
      { "label": "quarter", "text": "0.25 (half of a half)" },
      { "label": "tenth", "text": "0.1" },
      { "label": "fifth", "text": "0.2 (two tenths)" }
    ],
    "example": "Three quarters is 3 × 0.25, so 3/4 = 0.75."
  },
  "fact.fdp.to-percent": {
    "intro": "Percent means out of 100. Learn four landmarks, then count how many you have.",
    "lines": [
      { "label": "half", "text": "50%" },
      { "label": "quarter", "text": "25%" },
      { "label": "tenth", "text": "10%" },
      { "label": "fifth", "text": "20% (two tenths)" }
    ],
    "example": "Four fifths is 4 × 20, so 4/5 = 80%."
  },
  "fact.root.square": {
    "intro": null,
    "lines": [ { "label": "", "text": "Go backwards from the square numbers. √49 asks \"what number times itself makes 49?\" Learn the squares and the roots come with them." } ],
    "example": "7 × 7 = 49, so √49 = 7."
  },
  "fact.root.cube": {
    "intro": null,
    "lines": [ { "label": "", "text": "Go backwards from the cube numbers. ∛64 asks \"what number times itself three times makes 64?\" There are only five: 1, 8, 27, 64 and 125 go back to 1, 2, 3, 4 and 5." } ],
    "example": "4 × 4 × 4 = 64, so ∛64 = 4."
  },
  "fact.int.add": {
    "intro": null,
    "lines": [ { "label": "", "text": "Picture a number line and start at the first number. Adding a positive number moves right. Adding a negative number moves left." } ],
    "example": "For 4 + (−6), start at 4 and move 6 to the left. You land on −2."
  },
  "fact.int.subtract": {
    "intro": null,
    "lines": [ { "label": "", "text": "Subtracting a negative number is the same as adding the positive one. Subtracting a positive number moves left on the number line. If it helps, turn the subtraction into an addition first." } ],
    "example": "3 − (−5) = 3 + 5 = 8."
  },
  "fact.int.multiply": {
    "intro": null,
    "lines": [ { "label": "", "text": "Multiply the numbers as if they were both positive, then decide the sign. Same signs give a positive answer. Different signs give a negative answer." } ],
    "example": "For −6 × 7 the signs are different, so the answer is −42. For −6 × (−7) the signs are the same, so it's 42."
  },
  "fact.int.divide": {
    "intro": null,
    "lines": [ { "label": "", "text": "Think multiplication, then use the same sign rule as multiplying." } ],
    "example": "For −42 ÷ 6, ask \"what times 6 makes 42?\" That's 7. The signs are different, so −42 ÷ 6 = −7."
  },
  "fact.units": {
    "intro": "The first part of the unit name tells you the size.",
    "lines": [
      { "label": "kilo", "text": "A thousand. 1 km = 1000 m and 1 kg = 1000 g." },
      { "label": "centi", "text": "A hundredth. 1 m = 100 cm, so 1 cm = 0.01 m." },
      { "label": "milli", "text": "A thousandth. 1 m = 1000 mm and 1 L = 1000 mL, so 1 mL = 0.001 L." },
      { "label": "cm and mm", "text": "10 mm in 1 cm, so 1 mm = 0.1 cm." },
      { "label": "Small unit to big unit", "text": "The answer is a decimal." },
      { "label": "Time", "text": "60 twice. 60 seconds in a minute, 60 minutes in an hour." }
    ],
    "example": null
  }
}
```

**The worked examples were checked by script.** Every example equation is true: 4×7=28,
5×8=40, 9×6=54, 12×7=84, 6×7=42, 56÷7=8, 12²=144, 4³=64, 3/4=0.75, 4/5=80%, √49=7, ∛64=4,
4+(−6)=−2, 3−(−5)=8, −6×7=−42, −6×(−7)=42, −42÷6=−7, and the unit facts quoted in `fact.units`.

**Glossary flags (D40).** The texts use terms the glossary doesn't have yet. None is defined
inline. They should come in with the Y7 number chains' glossary words, before those chains'
activities:
- *negative number*, *number line*;
- *square number*, *square root*, *cube number*, *cube root*;
- *percent* / *percentage*, *decimal*, *tenth*, *hundredth*;
- *kilo-*, *centi-*, *milli-* (the prefixes), *thousandth* (for `fact.units`).

**Option (a)'s known cost:** one text serves every fact in a family. Revision 5 eased this for
multiplication by laying the moves out as labelled lines keyed to the multiplier. If classroom
data shows a family's text still isn't landing, that family moves to option (c).
