---
status: check sheet for Zan (D63, option b). Uncommitted.
page: NZC – Mathematics and Statistics Phase 4 (Years 9–10), https://newzealandcurriculum.tahurangi.education.govt.nz/5637291579.p
read: 2026-10-21, built-in browser. The page's own text and its table cells were read, not a model
  summary. Each statement's column was resolved from the table's row and column spans.
---

# D63: S28–S34 against the page

The page's tables have four content columns: Knowledge Y9 | Knowledge Y10 | Practices Y9 |
Practices Y10. Practices map to `Do` and Knowledge to `Know`.

The page is © 2026 Ministry of Education, and I haven't verified its reuse licence. So this sheet
does not reproduce the statements. It records where each one sits and whether the stubs' wording
matches. Zan: open the page, find each one by its location below, and tick it.

| S | stubs' location | location on page | wording vs stubs | tick |
|---|---|---|---|---|
| S28 | Y9 Algebra · Do | Algebra › Equations and relationships › Practices Y9, 1st bullet (with its 3 sub-bullets) | matches word for word | ☐ |
| S29 | Y9 Algebra · Do | same cell, 3rd bullet | matches (the page has no space after "e.g.") | ☐ |
| S30 | Y9 Algebra · Do | same cell, 4th bullet | matches | ☐ |
| S31 | Y9 Algebra · Do | same cell, 6th (last) bullet | matches | ☐ |
| S32 | Y9 Algebra · Do | same cell, 5th bullet | matches | ☐ |
| S33 | Y10 Algebra · Know | Algebra › Equations and relationships › Knowledge Y10 (the Knowledge Y9 cell of that row is empty), 1st sentence | matches | ☐ |
| S34 | Y10 Number · Know | Number › Number structures and operations › Knowledge Y10, the "Exponent rules…" sentence | **the stubs truncate it.** On the page the sentence continues ("…and include:") into five named rules: product, quotient, exponent-of-exponents, negative exponent, zero exponent | ☐ |

All seven sit in the year and column the stubs give, so the banding notes in the stubs hold.

## Fix owed before commit

- **S34:** either cite the sentence with its trailing "and include:" plus a pointer to the list,
  or cite only the product and quotient rules that `algebra.terms.*` uses. The list also covers
  the exponent-of-exponents rule, which the school dropped from its 2026 Y9 scheme. That matches
  the stubs' note that powers of powers are left out at Y9.

## Found on the read, not in the stubs (each is for Zan to take or leave)

1. **Proposed S35 (Y10 Algebra · Know):** Knowledge Y10, in the same cell as S33, last sentence.
   It says a linear inequality's solution is a set of values that a number line can show. This is
   the direct source for the number line in `algebra.inequations.solve`, which the stubs justify
   only from the Y10 practice.
2. **Proposed S36 (Y10 Algebra · Do):** Practices Y10, 2nd bullet. It covers forming and solving
   linear equations and inequalities with rational coefficients, and representing the solution on
   a number line. The stubs cite this in prose ("the NZC's Y10 statement asks for it") but never
   number it.
3. **Proposed S37 (Y9 Algebra · Do, optional):** Practices Y9, 2nd bullet. It is about generalising
   the properties of operations with variables, with distributivity as its example. It is a fit for
   `algebra.expand.single`.
4. **D45 item 2 (integer × and ÷):** Number › Number structures and operations › Practices Y9
   lists adding, subtracting, multiplying and dividing integers. Under the NZC, the missing
   integer multiply/divide skill is **Y9**, not the Y8 D45 assumed. Its `band_nz` follows the
   school's scheme under D55 item 4, but the NZC no longer argues for Y8.
5. **D62 (glossary, `index`):** two things on this page bear on the ruling.
   - Number › Knowledge Y10 says that index, power and exponent are used interchangeably.
   - The Y9 word list (Number) names *index* as a new Y9 word, and the Algebra list names
     *expanding*.

   D62 kept "power" free for 702 to mean something else ("81 is a power of 3"). That departs
   from the NZC's usage, where power is a synonym of index. See the note to Zan.
6. **Not seen on the page:** *inequation* and *inequality* are in neither year's word list. The
   page's own glossary (further down) has an entry for "Inequality". That supports stubs ruling 3
   keeping *inequality* as a variant.

`ncea` stays unset (D63).
