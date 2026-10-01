# Y7 hook concept bank (D42 stage 1)

`status: draft`, for screening as a set. Written 30 Sep 2026 against the Y7 stubs
(`proposals/y7-chain-stubs.md`) and the hook rules fetched from `main`:
`authoring-principles.md` §4 and `activity_defaults.hook_contract`.

**Pool size.** The contract's minimum is `ceil(approved_activities / 2)` per chain. At stub
counts that is **34 hooks across 19 chains** (35 before polygon sums moved to Y8), and this bank gives exactly the minimum per
chain. Screening will cut some; each cut needs a replacement before that chain's activities
are drafted.

**Rules each concept was written to** (§4, restated only as a checklist):

- It's one question, thinkable in under a minute, that a student can engage with by guessing.
- It connects to a skill in its chain.
- It doesn't front-load the worked example.
- It uses a strong shape: a surprising claim, a prediction, a fictional student's wrong
  answer, or a choice between two options.

Misconception ids are the **proposed** ids from the stubs; none are registered yet. The
"sets up" column is hook screening only. It is **not** an attachment: attachments live
only on the skill's `misconceptions` list in the graph (PR #5).
"NZ" marks a specifically Aotearoa context.

---

## Thread 02: Number (10)

### `chain.number.place-value` (3 activities → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.place-value.long-jump` | `number.place-value.decimals` | School athletics: Mere jumps 3.45 m, Leilani 3.5 m. Mere says she won "because 45 is more than 5." Who gets the ribbon? | `mis.place-value.longer-is-larger` | | claim to evaluate |
| `hook.round.dairy-cash` | `number.round.cash` | At the dairy your total is $4.97 and you pay cash. Do you hand over $4.97, $4.90 or $5.00? And would buying the items one at a time cost more? | `mis.round.cash-per-item` | NZ | NZ has had no 1c/2c/5c coins since 2006; students often haven't noticed the rounding |

### `chain.number.powers` (2 → 1)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.exponent.rumour` | `number.exponents.evaluate` | You tell a secret to 2 people. Each of them tells 2 new people the next day, and so on. After 10 days, about how many new people hear it that day: 20, 200 or 1000? | `mis.exponent.multiplies-base` (2¹⁰ read as 20) | | prediction. 2¹⁰ = 1024 |

### `chain.number.order-of-operations` (2 → 1)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.order.viral-sum` | `number.operations.order` | A viral post: 6 + 4 × 2 = ? A phone calculator says 14; a cheap desk calculator says 20. Which one is broken? | `mis.order.left-to-right` | | two options. Basic calculators do evaluate left to right; the lesson earns why the convention exists |

### `chain.number.factors` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.primes.ninety-one` | `number.primes.classify` | Is 91 prime? Most adults say yes. Commit to a guess. | `mis.primes.odd-means-prime` | | 91 = 7 × 13 |
| `hook.factors.sausage-sizzle` | `number.factors.hcf-lcm` | Sausage sizzle fundraiser: sausages come in packs of 6, bread in packs of 8. What's the fewest of each you can buy so nothing is left over? | `mis.factors.lcm-is-product` (answers 48, not 24) | NZ | |

### `chain.number.integers` (3 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.integers.goat-island` | `number.integers.number-line` | Snorkelling at Goat Island: Hemi is at −8 m, Aroha at −3 m. Who is deeper? And which number is bigger? | `mis.integers.larger-digit-larger` | NZ | the two questions pull against each other, which is the point |
| `hook.integers.ohakune-morning` | `number.integers.additive-inverse` | It's −4 °C in Ohakune at 7 am. By midday it has risen 9 degrees. Ben says it's now −13 °C "because the numbers got bigger." What is it really? | `mis.integers.sign-ignored` | NZ | wrong answer to react to |

### `chain.number.fractions` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.fractions.add-two` | `number.fractions.equivalent` | Priya adds 2 to the top and bottom of 2/3 and gets 4/5: "I did the same thing to both, so it's the same fraction." Is it? | `mis.fractions.add-same` | | wrong answer to react to |
| `hook.percent.sale-signs` | `number.percent.hundredths` | Three sale signs: "0.5% off", "50% off" and "½ price". Two of them are the same deal. Which one is the odd one out? | `mis.percent.decimal-shift` | | two-of-three choice |

---

## Thread 03: Algebra (6)

### `chain.algebra.expressions` (3 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.notation.mind-reader` | `algebra.notation.write` | Think of a number. Add 5, double it, take away 10, halve it. You're back at your number, and I knew you would be without knowing what it was. How? | `mis.notation.letter-as-object` | | the lesson earns "a letter stands for any number". Don't reveal it in the hook |
| `hook.like-terms.x-plus-x` | `algebra.expressions.like-terms` | Sione says x + x = x². Try x = 3. Now try x = 2. Is he right? | `mis.like-terms.adds-to-power` | | surprise: it works for 2 (and 0), so one check isn't proof |

### `chain.algebra.equations` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.equations.two-solvers` | `algebra.equations.two-step` | Solving 2x + 7 = 31, Tama divides by 2 first and gets 8.5. Mere takes 7 away first and gets 12. Both say they "did the same to both sides." Who's right? | `mis.equations.partial-divide` (was `undo-order`; renamed in the 1 Oct screening) | | two options. Tama halved 2x and 31 but not the 7 (x = 12). Dividing first works if every term is divided; the lesson earns that, not a fixed order |
| `hook.formulae.taxi-fare` | `algebra.formulae.rearrange` | A taxi charges $4 to start plus $3 per km. You have $25. How far can you go, and can you write a rule that works for any amount of money? | `mis.equations.same-operation` | | prediction. The money context is also used in several other hooks (see screening) |

### `chain.pattern.linear` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.pattern.hui-tables` | `pattern.linear.rule` | Setting up for a hui: 1 table seats 6, 2 tables pushed end to end seat 10, 3 tables seat 14. How many people can 20 tables seat? Most people guess 120. | `mis.pattern.assumes-proportional` (new 1 Oct: 120 is 6 × 20; was `first-term-as-constant`, which would give 86) | NZ | 20 tables seat 82 (4n + 2) |
| `hook.pattern.catch-up` | `pattern.linear.graph` | Aroha has $50 and saves $5 a week. Ben has $0 and saves $10 a week. Will Ben ever catch up, and when? | `mis.pattern.first-term-as-constant` | | prediction. Sets up start = d, step = steepness; the graph shows the crossing |

---

## Thread 04: Measurement (4)

### `chain.measure.area-volume` (5 → 3)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.area.mara-kai` | `measure.area.rect-triangle` | The school māra kai gets 20 m of fencing. One plan is a 9 m × 1 m bed; the other is 5 m × 5 m. Same fence, so the same amount of garden? | `mis.area.same-perimeter-same-area` (added to the stubs 30 Sep) | NZ | 9 m² vs 25 m² |
| `hook.area.cut-rectangle` | `measure.area.rect-triangle` | Cut a rectangle along its diagonal. Leilani says each triangle has the same area as the rectangle "because it has the same base and height." Agree? | `mis.area.triangle-no-half` | | a second hook on the same skill. Screening could move one to `measure.area.composite` instead |
| `hook.volume.two-boxes` | `measure.volume.cuboid` | Two boxes: 4 × 4 × 4 and 8 × 2 × 4. Which holds more? Most pick the long one. | `mis.volume.adds-dimensions` (4+4+4 = 12 < 8+2+4 = 14) | | both hold 64. Two options |

### `chain.measure.time` (2 → 1)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.time.interislander` | `measure.time.duration` | The Interislander leaves Wellington at 13:45 and gets to Picton at 17:15. Hemi says the trip takes 3.7 hours because 17.15 − 13.45 = 3.70. How long is it really? | `mis.time.decimal-hours` | NZ | 3 h 30 min |

---

## Thread 05: Geometry (5)

### `chain.geom.triangles-polygons` (2 → 1)

**Moved to Y8 (Zan, 1 Oct), with `geom.angles.polygon-sums`.** The chain is now 2 activities, so
its pool minimum is 1 and the remaining hook meets it. Carried to the Y8 bank:

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.polygon.honeycomb` | `geom.angles.polygon-sums` | Bees build hexagons. A triangle's angles add to 180°, so Priya says a hexagon's add to 6 × 180° = 1080°. Predict: too big, too small, or right? | `mis.polygon.n-times-180` | | answer 720°. Needs a figure: stub as an image until the fence ships |

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.angles.field-triangle` | `geom.angles.triangle-quad-sum` | One triangle is painted across the whole school field; another is drawn on your thumbnail. Which one's three angles add up to more? | `mis.angles.sum-depends-on-size` | | prediction |

### `chain.geom.parallel-lines` (2 → 1)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.parallel.car-park` | `geom.angles.parallel-transversal` | Supermarket car-park lines are painted parallel, and the kerb cuts across them. Ben says every angle where they meet must be equal. Some look bigger. Which ones really are equal? | `mis.parallel.all-equal` | | needs a figure |

### `chain.geom.transformations` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.reflect.ambulance` | `geom.transform.reflect` | Why is AMBULANCE written backwards on the front of the van? Try writing your name so it reads correctly in a mirror. | `mis.reflect.translates` | NZ | St John ambulances carry it. Answering well needs the lesson; engaging with it doesn't |
| `hook.transform.kowhaiwhai` | `geom.transform.translate` (consolidation's terminal skill) | Look at a kōwhaiwhai panel: which move takes one koru to the next one? A slide, a flip or a turn? | the reflect vs 180° rotation mix-up (no single id; the consolidation names it) | NZ | needs an image of a real panel, **but not until the hook is finished** (stage 2). Candidate source: Te Papa Collections Online, where Creative Commons images are downloadable and taonga images are requested for educational use only. Pick the panel with colleagues, alongside the Pacific-context review |

### `chain.geom.nets` (1 → 1)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.nets.cross-or-line` | `geom.nets.identify` | Six squares joined in a cross, and six squares in a straight line. Both have six faces' worth. Do both fold into a cube? | `mis.nets.any-six-squares` | | needs a figure |

---

## Thread 06: Statistics (5)

### `chain.stats.data-displays` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.stats.jersey-average` | `stats.variables.classify` | The average jersey number on our rugby team is 11.4. What does that tell you about the team? | `mis.stats.digits-are-numerical` | | answer: nothing. That's the surprise |
| `hook.stats.join-the-dots` | `stats.display.time-series` | One graph shows rainfall each month; another shows the class's favourite fruit. One of them should have its dots joined by a line. Which one, and why not the other? | `mis.timeseries.joins-categories` | | two options |

### `chain.stats.summaries` (5 → 3)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.stats.nana-birthday` | `stats.summary.outlier-effect` | Ages at a whānau birthday: 8, 9, 10, 11 and Nana, 87. The mean age is 25. Is anyone at this party "about 25"? | `mis.outlier.affects-median-equally` | NZ | the lesson earns the median as the fix |
| `hook.stats.one-shoe-size` | `stats.summary.median-mode` | A shop can stock a new sneaker in only one size. Should it pick the mean size, the median size, or the most common size? | no id: sets up that "average" has three meanings | | choice. Named "no id" per the screening check |
| `hook.stats.pick-a-shooter` | `stats.summary.range` | Two netball shooters both average 6 goals a game. One scores 6, 6, 6, 6; the other 1, 11, 2, 10. Who do you pick for the final? | no id: sets up that spread matters as well as centre | | choice. No right answer, which is fine for a hook |

---

## Thread 07: Probability (4)

### `chain.prob.theoretical` (4 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.prob.dice-totals` | `prob.theoretical.equally-likely` | Roll two dice and add them. Is a total of 2 as likely as a total of 7? | `mis.prob.equiprobability` | | prediction |
| `hook.prob.two-coins` | `prob.sample-space.list` | Toss two coins. Aroha says there are three outcomes (two heads, two tails, one of each), so each has a 1-in-3 chance. Agree? | `mis.prob.order-ignored` | | wrong answer to react to |

### `chain.prob.experimental` (3 → 2)

| id | connects to | concept | sets up | NZ | notes |
|---|---|---|---|---|---|
| `hook.prob.drawing-pin` | `prob.experimental.relative-frequency` | Drop a drawing pin. It lands point-up or on its side. What's the chance of point-up? You can't work it out, so how could you find out? | `mis.prob.small-sample-exact` | | no theoretical answer exists, which is why the lesson is about experiments |
| `hook.prob.lotto-due` | `prob.experimental.large-numbers` | Lotto's website shows that number 17 hasn't been drawn for 40 draws. Is it "due"? | `mis.prob.gamblers-fallacy` | NZ | **Kept (Zan, 30 Sep) on the condition that the reveal shows how the odds are stacked against the player.** Two facts: (1) every draw is fresh, so 17 is no more likely than any other number; (2) the long run is predictable, which is the large-numbers idea: only 53c comes back in prizes for every $1 spent, and one line's chance of first division is 1 in 3,838,380, about 70,000 years of weekly play. Source: safergambling.org.nz, "How Lotto works" (6 balls from 40; 1 in 383,838 on a $7, 10-line ticket). Re-check the figures when the hook is finished |

---

## Screening as a set (D42 checks)

1. **No context repeats within Y7, or against chain 1 and the slope pool** (lollies, paddling
   pool/seedling, candle, cliff). Rugby appears once (jersey numbers) and netball once.
   Temperature and depth are split between the two integer hooks on purpose.
2. **Every concept sets up a named misconception, or says why not.** Two statistics hooks
   say "no id". One area hook uses the new id `mis.area.same-perimeter-same-area`,
   added 30 Sep.
3. **Spread.**
   - **Money is heavy:** dairy, sausage sizzle, sale signs, taxi and savings (5 of 34).
     The taxi hook is the easiest to swap.
   - **Fictional-student claims:** 9 of 34. The other shapes (prediction, two options,
     surprise) cover the rest.
   - **NZ contexts:** 11 of 34.
   - **Pacific contexts:** only through names. None of the settings are Pacific-specific,
     so this is a gap to fill from your own knowledge rather than invent. It doesn't bind
     until Y11 (AS91945), but a Y7 bank is the cheap place to start.
4. **Nothing depends on an unruled chain decision.** Two hooks lean on stub choices: the
   area pair, if the nets chain folds into area-volume; and the kōwhaiwhai hook's
   `connects_to`, if the transformations consolidation moves. Three hooks need figures (car
   park, kōwhaiwhai, nets) and stay as images until the figure fence ships.

## Screening decisions (Zan, 30 Sep)

- **`hook.prob.lotto-due`: kept**, with a reveal that shows the odds against the player
  (note updated).
- **`hook.transform.kowhaiwhai`:** the image is sourced at the finishing stage, with
  colleagues.
- **`mis.area.same-perimeter-same-area`: added** to the stubs.
- **Pacific-specific contexts: deferred.** Zan will work these out with colleagues; the
  bank stands without them for now.
