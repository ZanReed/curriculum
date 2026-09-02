# Hook screen — `chain.rate.proportional`

**Date:** 2026-08-31 · Both hooks are drafts awaiting a human screen (§12). This is the
screen's findings and a recommendation, not an approval.

**Verdict: Hook 1 accept with a change to the numbers. Hook 2 reject and replace.**

---

## Hook 1 — `rate.unit-rate`

> *Two shops sell the same lollies. One is \$3 for 4, the other \$5 for 7. Which line would
> you stand in — and could you be sure in ten seconds?*

**Passes the §4 tests.** Thinkable in under a minute, answerable by a guess, needs no
prerequisite to engage, connects to a real skill, and does not reveal the divide-to-compare
method.

**But the numbers work against the hook's purpose.** \$0.75 versus about \$0.71 is a 5%
difference. The draft's note treats "too close to eyeball" as the virtue — it is, for
*forcing the method*, but it wrecks the payoff. The reveal is *"you were nearly right either
way; it's 3.6 cents."* A hook earns the lesson by making intuition visibly insufficient, and
here intuition was fine.

**The chain's own cut file already found the better shape and discarded it for the wrong
reason.** The cut hook was rejected because it *"confirms the intuition (the bigger juice
*is* cheaper per litre) rather than surprising"* — correct diagnosis, wrong remedy. The fix
was to invert the numbers, not to drop the idea.

**Recommended replacement numbers:** make the intuitive answer *wrong*. The bigger pack
should lose.

> *Two shops sell the same lollies. One sells a bag of 5 for \$4. The other sells a bag of 12
> for \$10. Which bag is better value — and are you sure?*

80c versus about 83c. The bigger bag looks like the obvious deal and is not. Now the guess is
worth committing to, the reveal is a genuine surprise, and the method is what resolves it.

**One smaller change:** *"which line would you stand in"* introduces queueing, which is a
second variable — a student can rationally pick the shorter line. Ask which is better value.

---

## Hook 2 — `rate.proportional-graph` · **reject**

> *A recipe uses 2 eggs for 3 people. For 6 people you'd need 4 eggs. How many eggs would 0
> people need — and how could you prove your answer by graphing these numbers?*

Three problems, and the third is the one that decides it.

**1. The intuition question cannot be wrong.** Nobody answers anything but zero. §4 wants a
prediction worth committing to; this one has no failure mode, so it does no work.

**2. It front-loads, and the draft says so.** *"How could you prove your answer by graphing"*
hands the student the method — plot the points, extend the line back. Establishing that a
proportional graph passes through the origin is the *lesson's* job. Under §4 that makes it
discovery, not a hook.

**3. Eggs are the wrong context for a graph about proportional relationships.** 2 eggs for 3
people is ⅔ of an egg per person. A proportional graph is a continuous line through the
origin, and every non-integer point on this one is meaningless — you cannot use 1⅓ eggs. The
hook for the graph skill should not be built on a quantity where most of the line is
nonsense. This is a defect in the context, not the wording, so it cannot be reworded out.

---

## Replacement Hook 2 — `rate.proportional-graph`

> *After 2 minutes of filling, a paddling pool is 10 cm deep. After 2 weeks of growing, a
> seedling is 10 cm tall. One of these you can predict at double the time. The other you
> can't. Which is which?*

**Why this one is open on the day it is fired**, which is the property the pool exists for. A
student who has finished activities 01 and 02 can compute both unit rates — 5 cm/min and 5
cm/week — and will confidently double both. Being able to find a unit rate is exactly what
makes this hook *look* answerable and get it wrong. So it stays open after the first two
activities, which is what Hook 1 cannot do and what the cut juice hook also could not do.

**It does not front-load.** No graph, no origin, no line. It asks for a prediction and the
lesson supplies the structure that explains why one prediction holds.

**It plants the chain's own sensor.** The property being probed is whether doubling the input
doubles the output — which is what a straight line through the origin *means*, and the
failure to hold it is `mis.proportional.line-misses-origin`, already attached to
`rate.proportional-graph`. The hook opens the day on the exact confusion the chain
instruments.

**It does not collide with activity 04.** That DoL turns on a fixed fee breaking
proportionality, so any hook built on a joining fee or flat charge would front-load the
consolidation's own assessment. Growth versus filling avoids that surface entirely.

**Continuity is honest here.** Water depth and plant height are genuinely continuous, so
every point on the line means something — the flaw that disqualifies eggs.

---

## Pool coverage after these changes

| | opens | still open after activities 01–02? |
|---|---|---|
| Hook 1 (revised numbers) | comparing rates | no — and it should not be |
| Hook 2 (replacement) | proportional vs not | **yes** |

Two hooks, two distinct conceptual leaps, and whichever day a teacher starts there is one the
class cannot already answer. The draft's own reasoning holds: the constant of proportionality
needs no hook, because k is the unit rate renamed, so any unit-rate hook already opens that
day.

**Not merged.** These stay in the holding pen until you approve them; nothing goes into
`chains[].hooks` before that.
