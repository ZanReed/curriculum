# Chain hooks

Hooks are a chain-level pool (D9): they are **not** welded to any activity — the teacher
fires one when *their* class day begins, because period boundaries are classroom facts the
data model cannot see. Review still keeps position one inside every activity.

Rules live in `authoring_principles` §4 and `activity_defaults.hook_contract`. In short: one
question, thinkable in under a minute, answerable by intuition or a guess, no prerequisite
knowledge needed to *engage*. It must genuinely connect to a skill in the chain, and it must
**not** front-load the lesson — if answering it needs the worked example, it has become
discovery.

**A hook must still be open on the day it is fired.** The pool spans the chain's distinct
conceptual leaps so that whatever day a teacher starts, there is a hook the class cannot
already answer. Two hooks a student can answer after the same early lesson are redundant —
one of them is doing no work on the later days.

**Authoring order.** The pool is authored at chain creation, before the chain's first
activity. The validator minimum counts *approved* activities, so with none approved nothing
is owed — which makes hooks free, and free things get written last and badly. That is the
retrofitted filler D9 rejected per-activity hooks to avoid. This rule is the counterweight and
no validator enforces it.

**Hook ids are permanent.** An id is never reused once it has been in the graph or was cut at
screening, because the platform's per-class "used" marks point at hook ids. A cut or retired id
goes in `hook-ids-retired.txt`, and `scripts/generate_hook_registry.py` fails if it reappears.
The graph's pools are generated into `hook-registry.json` for the platform's teacher-only chain
view; students never see hooks.

**Screening.** Every hook here is a draft until a human marks it approved. This doc is the
holding pen; the pool is `chains[].hooks` in the thread JSON.

---

## chain.rate.proportional — **screened and merged (v0.13.0)**

Skills: `rate.unit-rate` · `rate.constant-of-proportionality` · `rate.proportional-graph`
Two hooks, matching `ceil(4 / 2)` on the projection. This chain has two conceptual leaps
worth a hook — comparing rates, and proportional versus not. The constant of proportionality
needs no hook of its own (*k is the unit rate, renamed*), so any unit-rate hook already opens
that day.

**`hook.rate.better-value`** → `rate.unit-rate`

> Two shops sell the same lollies. One sells a bag of 5 for \$4. The other sells a bag of 12
> for \$10. Which bag is better value — and are you sure?

80c versus about 83c. The bigger bag looks like the obvious deal and is not, so the guess is
worth committing to and the reveal is a genuine surprise. Does not disclose the
divide-to-compare method. Not open after activity 01, which is correct for the chain's
opening hook.

**`hook.rate.doubles-or-not`** → `rate.proportional-graph`

> After 2 minutes of filling, a paddling pool is 10 cm deep. After 2 weeks of growing, a
> seedling is 10 cm tall. One of these you can predict at double the time. The other you
> can't. Which is which?

**Stays open after activities 01–02**, which is the property the pool exists for: a student
who can find a unit rate — 5 cm/min, 5 cm/week — will confidently double both, and that is
the error. Probes whether doubling the input doubles the output, which is what a line through
the origin *means*, so it opens the day on `mis.proportional.line-misses-origin`. Names no
graph, origin or line, so it does not front-load. Both quantities are continuous, so every
point on the eventual line means something.

---

### Cut, with reasons

**Former Hook 1 numbers — \$3 for 4 versus \$5 for 7.** Kept the hook, changed the numbers.
\$0.75 versus \$0.71 is a 5% gap, so the reveal was *"you were nearly right either way."* A
hook earns its lesson by making intuition visibly insufficient; here intuition was fine. The
replacement inverts it so the obvious answer is wrong.

**Former Hook 2 — "2 eggs for 3 people… how many for 0 people, and how could you prove it by
graphing?"** Cut for three reasons, the third decisive:
1. The intuition question cannot be wrong — nobody answers anything but zero — so it carries
   no commitment worth testing.
2. *"How could you prove your answer by graphing"* hands over the method. Establishing that a
   proportional graph passes through the origin is the lesson's job.
3. **Eggs are the wrong context for a graph about proportional relationships.** 2 eggs for 3
   people is ⅔ of an egg per person; a proportional graph is a continuous line through the
   origin, and every non-integer point on this one is meaningless. A defect in the context,
   not the wording, so it could not be reworded out.

**"1-litre juice \$2.50 versus 2-litre \$4.50 — is the bigger one always the better deal?"**
Cut as redundant with Hook 1: both answerable the moment a student can compute a unit rate, so
it opened no later day. It also confirmed the intuition rather than surprising — the right
diagnosis, but the remedy was to invert the numbers rather than drop the idea, which is what
the revised Hook 1 now does.

---

## chain.linear.slope — **screened and merged (v0.14.1)**

Approved by the author 2026-10-01 (B13).

Pool minimum: 3 (5 activities). Chain shape: `linear.slope.two-points` ×2 (rise over run;
then negative gradients and signed coordinates), `linear.slope.from-graph`,
`linear.slope.interpret-context`, then a consolidation (evidenced:
`mis.slope.rise-run-inverted` spans two-points and from-graph).

### `hook.slope.ten-or-point-one` → `linear.slope.two-points`

> A ramp rises 1 m over 10 m of ground. Tama says its gradient is 10. Aroha says it's 0.1. One of those numbers describes a gentle ramp and the other describes a wall. Which is which?

Chain opener. Sets up mis.slope.rise-run-inverted: students engage by picturing '10 is steep'; the lesson earns why rise goes on top. Rise and run are given but not the division, so the method isn't handed over. Answered once activity 01 is done.

### `hook.slope.cliff-or-flat` → `linear.slope.from-graph`

> Two fitness apps graph the same climb up Maungawhau. On one, the line looks like a cliff. On the other, it's nearly flat. Which app is lying?

Neither: the axes use different scales. Sets up mis.slope.steeper-is-bigger. Needs two graphs of the same data on different axis scales (existing graph block). Fire before activity 03; stays open after 01–02, because a student who can compute a gradient still trusts the picture over the scale.

### `hook.slope.candle` → `linear.slope.interpret-context`

> A candle is 20 cm tall when it's lit and 14 cm tall three hours later. Someone says, "Its number is 2." Is that enough to tell you when it will burn out?

Sets up mis.slope.units-dropped: a bare 2 doesn't say 2 what, per what, or which way. The rate is -2 cm per hour, so it burns out in 7 more hours. The 2 is given, so the gradient calculation isn't front-loaded. Fire before activity 04 (two-points takes two activities). Hook-level ancestor of the derivative-units idea three years on.

**Not covered, deliberately:** `mis.slope.subtraction-order` is a procedural slip inside
activity 02; a hook can't set it up without front-loading the subtraction.

**Written fresh 2026-10-01.** The earlier drafts were never saved; only their ids survived.
`hook.slope.hundred-or-point-one` was renamed `hook.slope.ten-or-point-one` (never merged,
so the id was free).

---

## chain.geom.triangles-polygons — **approved and merged (v0.17.1)**

Approved by Zan 2026-10-03. The first Y7 chain to be drafted (D38 amendment: geometry first).

Pool minimum: 2 under the per-skill rule (D42 amendment, 2026-10-03): two skills, two
activities, no consolidation. One hook per skill, so neither day opens empty.

### `hook.triangles.turn-the-page` → `geom.triangles.classify`

> Draw a triangle with two sides the same length. Now turn your page so the triangle is lying on its side. Is it still the same kind of triangle?

Chain opener, before activity 01. Shape: do, then predict. Sets up mis.triangle.orientation-matters: a triangle that looks tipped over doesn't match the upright picture students hold, so many say it has changed. Doesn't name isosceles or say a triangle is classified by its sides and angles alone; the lesson earns both. Answered once activity 01's worked example classifies the same triangle in two orientations. No figure: students draw their own. New concept, screened against the Y7 bank: no repeated context.

### `hook.angles.field-triangle` → `geom.angles.triangle-quad-sum`

> One triangle is painted across the whole school field. Another is drawn on your thumbnail. Which triangle's three angles add up to more?

Before activity 02. Shape: prediction (screened Y7 bank concept, Zan 30 Sep): the field triangle, the thumbnail triangle, or the same. Sets up mis.angles.sum-depends-on-size. Doesn't give 180° or hint that the total is fixed; the lesson establishes the sum. Answered once activity 02 shows every triangle's angles add to 180°, whatever its size. No figure needed.

---

## chain.geom.parallel-lines — **approved, landing in v0.17.18**

Approved by Zan 2026-10-07, with hook 2 reworded to a prediction. The next Y7 geometry chain after
triangles-polygons (D38 amendment order).

Pool minimum: 2 under the per-skill rule (D42 amendment, 2026-10-03): two skills, two
activities, no consolidation. One hook per skill, so neither day opens empty.

### `hook.angles.squashed-x` → `geom.angles.relationships`

> Draw two long straight lines that cross, like a squashed X. Find the narrowest of the four angles. Kiri says the angle directly across from it must be the widest one, so the two balance each other out. Is she right?

Chain opener, before activity 01. Shape: do, then a fictional student's claim to evaluate. Sets up mis.angles.vertical-as-supplementary: "balance each other out" is that error in a student's words. She treats the opposite angle as the partner that makes up a straight line. Doesn't name vertically opposite or adjacent angles, and gives no number, so neither "equal" nor 180° is front-loaded; the lesson earns both. Answered once activity 01's worked example shows vertically opposite angles are equal. No figure: students draw their own. New concept; the Y7 bank had none for this skill.

### `hook.parallel.exercise-book` → `geom.angles.parallel-transversal`

> Ben rules a slanted line across two lines in his exercise book. That makes eight angles. He measures one of the sharp ones: 50°. "The book lines are parallel," he says, "so all eight are 50°." Before you measure anything: which of his eight angles do you think are 50°?

Before activity 02. Shape: a fictional student's wrong answer, then a prediction. Zan's rewording (2026-10-07): predict, don't measure, so the hook stays under a minute and the rule isn't found with a protractor. Sets up mis.parallel.all-equal as students actually make the error: copying the one given angle into every position. **Stays open after activity 01**, but only in part. A student fresh from 01 can fix the four angles at Ben's first crossing: the angle opposite is 50°, and the two beside it are not. Ben's "all eight" is already refuted at a single crossing. What 01 can't settle is the second crossing: whether any angle at the other book line matches, and which. That is the lesson. Answer: the four sharp angles are 50° and the four wide ones are 130°. Doesn't name corresponding, alternate or co-interior angles. Gives no total: 50° is a measurement, not a rule. Answered once activity 02 is done. No figure: students rule their own line across their own book lines, which really are parallel. Replaces the bank's `hook.parallel.car-park` (cut below).

**Not covered, deliberately:**
- `mis.angles.complement-supplement-swapped` is a mix-up of two names. A hook can't set it up without naming both terms and their totals, which is the lesson's content. It belongs to activity 01's items.
- `mis.parallel.assumed` (lines that look parallel but aren't marked) isn't set up by either hook. It's better carried by activity 02: an error-analysis item applying the angle rules to unmarked lines.

### Cut, with reasons

**`hook.parallel.car-park` (Y7 bank concept, never merged).** Replaced, not finished. The id
stays unused.
1. **The context isn't the figure.** Car-park bay lines stop at the kerb; they don't cross it,
   so each meeting point has two angles, not four. The real scene can't produce the eight-angle
   figure the lesson teaches, and §11 says contexts are real and checked.
2. It only works for slanted bays. With square-on parking every angle is 90° and Ben is right.
3. "Some look bigger" gave away half the answer.
4. It was marked "needs a figure", and a hook is text only: students never see a hook on screen
   (teachers will, in the platform's chain view), so students draw or picture it.

---

## chain.measure.area-volume — **approved, landing in v0.17.20**

Approved by Zan 2026-10-08 as drafted. The next Y7 chain in the geometry/measurement build order
(triangles-polygons → parallel-lines → area-volume).

Pool minimum: 4 under the per-skill rule (D42 amendment, 2026-10-03): four skills, five
activities (four parts and a consolidation). One hook per skill, so no part day opens empty.
The consolidation day has no hook of its own (see the end of this section).

### `hook.perimeter.patio-edge` → `measure.perimeter.polygons`

> A square patio is laid 4 paving stones long and 4 stones wide. Mele wants edging all the way round it. She counts the stones around the outside, gets 12, and says the edge is 12 stone-lengths long. Is she right?

Chain opener, before activity 01. Shape: a fictional student's claim to evaluate. Sets up mis.perimeter.counts-squares as students actually make it: counting the squares along the edge, so each corner stone counts once though it has two outside edges. Answer: 16 stone-lengths, so Mele is 4 short, one at each corner. Numbers check: a 4 × 4 square has 16 stones, 4 inside and 12 around the edge. Doesn't say "add the sides" or name perimeter; the lesson earns both. Answered once activity 01's worked example measures round the edge rather than counting tiles. No figure: students sketch a 4 × 4 square or picture a paved patio. New concept; the Y7 bank had none for this skill.

### `hook.area.mara-kai` → `measure.area.rect-triangle`

> The school māra kai gets 20 m of fencing. One plan is a bed 9 m long and 1 m wide. The other is a square, 5 m by 5 m. Same fence, so the same amount of garden?

Before activity 02. Shape: a surprising claim to evaluate. Sets up mis.area.same-perimeter-same-area: "same fence, same garden" is that error in words. Numbers check: both fences are 2 × (9 + 1) = 4 × 5 = 20 m, which a student fresh from activity 01 can confirm, and the gardens are 9 m² and 25 m², nearly three times as much. Gives no area formula and no unit; the lesson earns square units, and the reveal in m² opens mis.units.area-as-linear too. **Open on day 2 only if activity 01 leaves it open.** The misconception is attached to both skills, so activity 01's items for it stay on the perimeter side (shapes that look different but have the same perimeter) and don't compare the areas of equal-perimeter rectangles. If they do, this hook is closed before it's fired. Answered once activity 02 is done. No figure: students picture or sketch the two beds. From the Y7 bank, unchanged except the wording of the two plans.

### `hook.area.l-deck` → `measure.area.composite`

> An L-shaped deck has two arms, each 2 m wide. Measured along the outside, one arm is 6 m long and the other is 5 m long. Rangi works out 6 × 2 = 12 and 5 × 2 = 10, and orders 22 m² of decking. Too much, too little, or just right?

Before activity 03. Shape: a fictional student's wrong answer. Sets up mis.area.composite-overlap: Rangi's two rectangles both contain the 2 m × 2 m corner. Answer: 18 m² (6 × 2 + 3 × 2), so he's ordered 4 m² too much. **Stays open after activity 02**, which is the point: a student who can find a rectangle's area confidently does Rangi's two multiplications and agrees. The lesson earns splitting without overlap and finding the missing length (5 − 2 = 3), neither of which the hook gives. It does show *a* split, which is the strategy's outline; the hook's question is whether that split was right, so the method isn't handed over. No figure: students sketch the L from the spoken lengths. New concept; the Y7 bank had none for this skill.

### `hook.volume.two-boxes` → `measure.volume.cuboid`

> Two boxes. One is a cube, 40 cm long, 40 cm wide and 40 cm high. The other is 80 cm long, 20 cm wide and 40 cm high. Which one holds more?

Before activity 04. Shape: two options. Sets up mis.volume.adds-dimensions: adding gives 120 against 140, so the long box looks bigger. Answer: they hold the same, 64 000 cm³ each, which is 64 litres. **Open after activities 01–03:** a student who can find areas might spot that both bases are 1600 cm² (or both ends are 800 cm²), but turning that into "how much it holds" is the layers idea activity 04 teaches. Gives no formula and no cubic unit. No figure. From the Y7 bank, reworded (see Cut, with reasons).

**Not covered, deliberately:**
- `mis.area.triangle-no-half` is a slip in using ½ × b × h. A hook can't set it up without stating the formula, and the intuitive version (`cut-rectangle`, below) is one students get right. It belongs to activity 02's and 03's items.
- `mis.area.slant-as-height` needs a non-right triangle with its slant side and height both visible. Spoken aloud, the hook would have to describe the figure and name base and height, which is the lesson. It belongs to items with figures.
- `mis.units.area-as-linear` and `mis.units.volume-as-square` get no hook of their own. The mara-kai reveal is in m² and the two-boxes reveal in cm³ and litres, so the teacher meets both errors in the answers; the consolidation sorts them out.

**Consolidation day (activity 05): no hook.** The day's content is telling perimeter, area and volume and their units apart, and all three are taught by the end of day 4. A question about which measure or unit fits is answerable by any student who has done 01–04, so it isn't open on day 5. The one that stays open (double every length of a box: twice as much?) asks about scaling, which this chain doesn't teach, so the lesson can't earn its answer. The teacher opens day 5 on the activity's review, which already retrieves all three measures. Nothing is lost by firing no hook; §4 says quality beats coverage.

### Cut, with reasons

**`hook.area.cut-rectangle` (Y7 bank concept, never merged).** Cut, not moved. The id stays
unused. Two problems, the first decisive:
1. **There's no day it's open.** On the rect-triangle day, intuition answers it correctly:
   picture the cut, see two matching triangles, so each is half. A hook earns its lesson by
   making intuition visibly insufficient, and here intuition is fine. On the composite day,
   which the bank suggested, it's closed: activity 02 has just taught that a triangle is half
   its rectangle.
2. **Its answer is the lesson.** "Each triangle is half the rectangle" is the worked example's
   key move for ½ × b × h. A hook that a class answers correctly hands over the method.
   The misconception it aimed at is now "Not covered, deliberately" above.

**`hook.volume.two-boxes`: reworded, not cut.** Three changes:
1. **Units added.** "4 × 4 × 4 and 8 × 2 × 4" had no units, so it had no context to be real
   (§11). At 40, 80 and 20 cm both boxes hold 64 litres, which is a size students can picture
   and a check that works out.
2. **"Most pick the long one" moved out of the prompt.** Said aloud, it tells students the
   popular answer is wrong.
3. **The skill and the misconception are unchanged.**

**`hook.area.mara-kai`: kept on its bank skill.** Moving it to `measure.perimeter.polygons` was
considered and not taken: the perimeter is given in the prompt, so the perimeter lesson can't
answer it.

---

## chain.geom.transformations — **approved, landing in v0.17.22**

Approved by Zan 2026-10-10 as drafted. The next Y7 geometry chain after area-volume (D38
amendment order). **Translation is taught first** (Zan, 2026-10-10): 01 translate, 02 reflect,
03 rotate, 04 consolidation. The graph's skill order follows, so the consolidation's terminal
skill is `geom.transform.rotate`.

Pool minimum: 3 under the per-skill rule (D42 amendment, 2026-10-03): three skills, four
activities (three parts and a consolidation). One hook per skill, and one for the consolidation
day because the reflect vs half-turn mix-up is still open then. Kept above the minimum by Zan's
ruling: a teacher who wants a review-only day simply doesn't fire a hook.

### `hook.translate.domino-gap` → `geom.transform.translate`

> On squared paper, draw a domino covering two squares side by side. Draw it again further to the right, so there are three empty squares between the old domino and the new one. Sione says the domino has moved three squares. Is he right?

Chain opener, before activity 01. Shape: do, then a fictional student's claim to evaluate. Sets up mis.translate.counts-gaps exactly as the registry describes it: counting the empty squares between the shape and its image. Answer: no, it has moved five squares. Its left end moved five, its right end moved five, and so did every point of it. Numbers check: the old domino covers squares 1 and 2, the gap is squares 3 to 5, and the new domino covers 6 and 7. Doesn't say "follow one corner" or give a vector; the lesson earns that a translation is measured from a point to its own image. Answered once activity 01 is done. No figure: students draw it. New concept.

### `hook.reflect.ambulance` → `geom.transform.reflect`

> On the front of many ambulances, the word AMBULANCE is printed back to front, so a driver ahead can read it in their rear-view mirror. To write your own name that way, do you reverse the order of the letters, flip each letter over, or both?

Before activity 02. Shape: prediction from three options, then try it. Sets up mis.reflect.translates as students actually make it: reversing the order of the letters but leaving each letter facing the same way, which moves each letter without flipping it: a slide, not a reflection. Answer: both. **Open after activity 01**, and sharper for it: the class has just learned that a slide keeps every letter facing the same way. Doesn't name a mirror line or say each point lands the same distance away on the other side. Answered once activity 02's worked example reflects a shape and shows its image facing the other way. **Constraint on activity 01:** its items don't compare a slide with a flip. No figure: students write their own name. From the Y7 bank, reworded (see Cut, with reasons).

### `hook.rotate.pencil-turn` → `geom.transform.rotate`

> Lay a pencil flat on your desk. You'll give it a half turn twice: once with the eraser end pinned in place, and once with the middle of the pencil pinned in place. Before you try it: will the pencil end up in the same spot both times?

Before activity 03. Shape: prediction, then do. Sets up mis.rotate.centre-ignored: "a half turn is a half turn" is the belief that the turn alone decides where the image lands. Answer: no. Pinned at the eraser, the pencil swings round and ends up on the far side of the pinned end; pinned in the middle, it stays where it was, pointing the other way. Open after activities 01 and 02, which teach slides and flips and say nothing about turning. Doesn't name a centre of rotation, give an angle or a direction, or show how to rotate on a grid. Answered once activity 03's worked examples rotate the same shape about two different centres. No figure: students use their own pencil. New concept.

### `hook.transform.playing-card` → `geom.transform.reflect`, `geom.transform.rotate`

> The king on a playing card is printed twice, once each way up, so the card looks the same whichever way you hold it. Is the bottom king a mirror image of the top one, or the top one given a half turn?

Before activity 04 (the consolidation). Shape: two options. Sets up mis.reflect.half-turn-confused: the two kings look like a reflection in the card's middle line, and most students will say so. Answer: a half turn. The card looks the same turned upside down, which is what a half turn does; with a mirror image in the middle line, both kings would face the same way, and the card would look different upside down. The teacher checks it with a real card: whichever way the top king faces, the bottom king faces the other way. Open after activities 01 to 03. **Constraint on activity 03:** its items don't set a half turn beside a horizontal reflection of the same shape. Answered once activity 04 has compared the two. No figure: a real card in the teacher's hand. New concept.

**Not covered, deliberately:**
- `mis.reflect.diagonal-as-vertical` needs a diagonal mirror line on a grid, which spoken aloud is activity 02's figure. It belongs to activity 02's items.
- `mis.coord.axes-swapped` is a slip in writing coordinates; a hook can't set it up without giving coordinates. It belongs to the items in all three part activities.

### Held, not cut

**`hook.transform.kowhaiwhai` (Y7 bank concept, never merged).** Held by Zan's ruling,
2026-10-10: not in this pool and not retired, so its id stays free to land later. It works only
with a real panel in front of the class, chosen with colleagues alongside the Pacific-context
review. The playing-card hook covers the consolidation day until then.

### Cut, with reasons

**`hook.reflect.ambulance`: reworded, not cut.**
1. **One question, not two.** The bank asked "why is it written backwards?" and "try writing your
   name". The prompt now gives the why and asks one question with three answers.
2. **"Many ambulances", not St John's.** Back-to-front lettering on ambulance fronts is well
   documented; whether every current Hato Hone St John vehicle carries it isn't confirmed, so the
   prompt doesn't claim it (§11). This drops the bank's NZ tag.
3. **The choice makes the misconception visible:** it separates students who reverse only the
   order (the slide) from those who flip each letter.

---

## Remaining 12 chains

No pools authored. Under the authoring-order rule each is owed one at chain creation. From
2026-09-29 hooks arrive in year batches (D42): a screened concept bank per year, then each
chain's full hooks just before its activities. The Y7 bank is the first
(`proposals/y7-hook-concept-bank.md`, draft PR #4).

⚠ **A note on the hook-pool trigger (B6).** The proposed check was *every chain registered in
`chain-registry.txt` has a non-empty hook pool*, on the premise that a chain is registered when
its folder is created. All 17 were registered at once instead, to fix the ordinal numbering
while renumbering was still free — so the check as specified would fail on 16 chains that have
no folders and no activities. **It should key on folder existence, not registry entry.** The
premise was broken by a deliberate choice made for a different reason, which is worth
recording rather than letting the check be written and then switched off.
