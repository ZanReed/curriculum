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
4. It was marked "needs a figure", and a hook is text only: the platform doesn't render hooks,
   so students draw or picture it.

---

## Remaining 14 chains

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
