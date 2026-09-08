# Authoring Principles

This document is injected into every drafting prompt. It states the *why* behind the
schema's structure, so a model composing an activity makes the same call the author
would make — not a plausible-sounding different one. Where a principle constrains you,
the constraint is deliberate. Where it is silent, use judgment and flag the gap.

Nothing here is decoration. If a draft satisfies the schema but violates a principle,
the draft is wrong.

---

## 1. What this curriculum is

An explicit-instruction mathematics curriculum, intro algebra through calculus and
statistics, delivered as short single-period activities that a platform ingests — the cap
is `activity_defaults.duration_min`. It is built
for novice learners acquiring new content. The design follows the evidence on how
novices learn: full guidance during acquisition, support faded gradually, retrieval
spaced deliberately, misconceptions anticipated and named.

It is not a discovery curriculum. During acquisition, students do not induce new
content from open-ended tasks — the working-memory cost of unguided search crowds out
the learning it is supposed to produce. Open problems and transfer tasks have a real
place *after* schema exists; they are consolidation tools, not acquisition tools.
Concede this openly when challenged: explicit instruction wins for acquiring new
content; the last stretch of a topic, once students have schema, is where richer
tasks earn their keep.

## 2. The skill graph is the asset

Skills are durable objects. Activities are disposable delivery instances aimed at them.

- Every activity targets exactly one primary skill. Review pointers, DoL items, and
  data all reference **skill ids**, never activity ids. Activities get rewritten;
  the graph endures.
- Prerequisite edges are authored at write time, never as a cleanup pass. An edge is
  a claim: *you cannot hold this skill without that one.* Sequencing preference is
  not an edge. Two skills that merely tend to be taught together get no edge.
- Anything the graph can derive is derived, never hand-declared. Progress, coverage,
  and review candidates are computed. A hand-maintained duplicate of derivable state
  will drift, and drifted state that looks authoritative is worse than no state.

## 3. Every activity keeps one contract

Three components, in this order: **review → lesson → DoL.**

The platform treats all three identically feature-wise; the division informs the
teacher and the student, it does not gate anything. But the authoring order is not
negotiable, because each position has a mechanism:

- **Review comes first** because retrieving prior skills activates the exact schema
  the new content is about to attach to. Moved after the lesson it becomes practice
  of what was just taught — a different mechanism with a smaller payoff, which
  already lives inside the lesson as the independent beat.
- **The lesson has three beats: worked → faded → independent.** Never fewer.
- **The DoL closes.** It is the only locale-bearing component (see §8).

## 4. The hook

Every teaching day opens with a hook: an interesting question, relevant to the day's
content, that students think about before anything else. It is an engagement device,
not an instruction device — it buys attention and a reason to care; it does not teach.

**Hooks are a chain-level pool; activities never carry them.** Each chain holds a pool
sized by `activity_defaults.hook_contract.minimum`. A hook is not welded to any
activity: the teacher fires one when *their* class day starts, because period
boundaries are classroom facts the data model cannot see — one class covers three
activities on a block day, another covers one and a half, and only the teacher knows
where the day began. Within every activity, review keeps position one regardless.

Rules for a hook:
- One question, thinkable in under a minute, answerable by intuition or guess —
  no prerequisite knowledge should be needed to *engage* with it, even if answering
  it well requires the day's content.
- It must genuinely connect to a skill in its chain. A fun but irrelevant opener
  trains students that the opener is skippable.
- It must not front-load the lesson's content. If answering the hook requires the
  worked example, the hook has become discovery learning through the back door. The
  hook raises the question; the lesson earns the answer.
- Strong hook shapes: a surprising claim to evaluate ("a 20% discount then 20% tax
  returns the price to normal — true?"), a prediction to commit to, a wrong answer
  from a fictional student to react to, two plausible-looking options to choose
  between. Weak hooks: trivia, "have you ever wondered," anything answerable with
  a shrug.
- Quality beats coverage: the pool minimum exists so no teaching day opens empty,
  not to manufacture filler. A chain may exceed the minimum only with hooks that
  earn their place.

## 5. The lesson beats

**Worked (I do).** Fully worked. Every step visible, including the step an expert
performs silently. The narration says the reasoning out loud — not what was done but
*why it was the move*. No "what do you notice" as the mechanism for new content; if
noticing is doing the teaching, it is discovery wearing a lab coat.

**Faded (we do).** The same procedure with support removed **from the end** — the
start intact, the later steps blanked. This beat is mandatory, no exceptions. The
jump from demonstration straight to independent practice is the single most common
failure in explicit-instruction materials; the faded beat is where the worked-example
effect actually pays out. Fade level responds to position in the chain: earlier
parts fade less, later parts fade more.

**Independent (you do).** Practice on the skill itself, at enough volume to be worth
grading (typically 4–8 items). Where the platform supports a decision, prefer items
that force the *choice* of method, not just its execution.

One worked example per new idea. Two ideas in one activity means the activity should
have been two activities.

## 6. Review is spaced retrieval, not warm-up filler

The review component draws from the primary skill's **ancestor pool** — the set of
skills upstream of it in the graph. Not siblings, not vibes: ancestors.

- **At least one item reaches far enough back**, per
  `activity_defaults.review_selection.constraint`. Retrieving only yesterday's skill is
  yesterday's lesson repeated, not spaced retrieval. Where the graph is shallower than the
  constraint asks — as it is at the very top of the curriculum — the constraint's own floor
  clause applies; do not invent an intermediate skill to satisfy it.
- Prefer prerequisites the students have not touched recently — staleness is the
  point. Prefer prerequisites the lesson is about to lean on — activation is the
  other point. The best review item is both: stale *and* load-bearing for today.
- Chain position governs the slice, per `activity_defaults.chain_rules`. Chain position 1
  gets full prerequisite-targeted review. Chain position 2+ gets a brief retrieval of the
  previous position only, with the recovered minutes going to independent practice; never
  repeat chain position 1's review later in the chain. Spaced retrieval is not lost at
  chain position 2+ — the DoL carries it at every position (§8). The final position in a
  chain has its own exit-check rule (`chain_rules.final_position`).
  Note: "chain position" is position within the chain. It is unrelated to a *skill part*,
  which is one of the activities delivering a single skill.
- Long-arc edges are the flagship. When a skill's ancestor sits years back
  (units-on-gradient feeding units-on-derivatives), reviewing it just before it is
  needed is the whole argument for the graph. Plant those items deliberately.

## 7. Misconceptions are first-class

A wrong answer is rarely random. Anticipated wrong answers map to **named
misconception ids** via distractor maps, and the map is what turns feedback from
"incorrect, try again" into diagnosis.

- **A misconception attaches to every skill that can elicit it** — not merely the one it
  was first noticed on. The test is whether an author writing distractors for that skill
  should be anticipating this error; "conceivably possible" is too broad and "names this
  skill" is too narrow. The clearest case: **a label naming a confusion *between* two things
  attaches to both skills.** A pair-confusion instrumented on one side is a sensor pointed at half the
  phenomenon: items on the unattached skill carry no binding, so the data under-reports the
  error and attributes all of what it does see to whichever skill holds the attachment. If
  only one attachment is defensible, the label is describing a one-sided error and should be
  reworded to say so.
  Not mechanically checkable: whether a second skill can exhibit an error is a question
  about the mathematics, not about the label. Ask it once per chain at authoring time, for
  every misconception attached to any skill in that chain.
- **A misconception about the FORM of a response binds only where the response format
  admits that form and the item requires it.** A units-dropped binding on a numeric blank
  cannot fire on the misconception, because the blank cannot carry units at all — it fires on
  the format, and reports every correct answer as an error. The carrier is an item where
  omitting the form is a choice the student makes: an mc whose distractor is the unitless
  value, or a response type that accepts units and an item that demands them. Same family as
  the auto-scored rule above — a binding that cannot fire does not mean what it appears to
  mean.
- Use only ids that exist in the registry. Never invent one inline — describe the
  anticipated error in a note instead, so a human can promote it to an id.
- **Distractor maps go only on auto-scored, per-item captured types** (multiple
  choice, graph, fill-in-the-blank). On a teacher-graded item the map produces no
  aggregate signal until a human marks it; it is dead weight there.
- Feedback attached to a wrong answer names the error's logic, not just the fact of
  the error. "That is the third-largest city, not the capital" beats "incorrect."
- The misconception data is the platform's most valuable output. Every mapped
  distractor is a sensor. Author accordingly.

## 8. Assessment is local; instruction is not

Mathematics is universal; assessment of mathematical skill is not. The same skill
terminates in a procedural computation under one qualification and a justified
argument under another.

- The **DoL is the only component that varies by locale.** Review and lesson are
  written locale-neutral. When the qualification changes, the DoL swaps and the
  rest stands.
- Write the DoL the way the named locale asks — its response format, its idea of
  evidence. A rubric-graded justification for a Merit/Excellence locale; auto-scored
  items for a procedural one. What each grade level requires is stated on the locale
  itself (`activity_defaults.locales`, the `levels` entry) — read it there, and tag
  every rubric line with the level it evidences so the claim is recorded, not implied.
- Know the data cost: auto-scored DoLs feed misconception aggregates immediately;
  rubric-graded DoLs capture text now and yield structured per-criterion scores only
  after a human grades. Neither is wrong. A chain whose every DoL is rubric-graded
  is a deliberate marking-load decision, not a default.
- A DoL has exactly 2 items: one on the primary skill, one on a review-pool skill far
  enough back, per `activity_defaults.review_selection.constraint` and its floor clause.
  Contextual items require units in the answer.

## 9. Compose only from shipped capabilities

The capability registry is the platform's truth. Draft only with capabilities marked
shipped, inside their stated constraints (graded curve families, two-column matching,
literal datasets, and the rest).

- If the pedagogically ideal move needs an unshipped capability, author the
  **fallback** — the best version buildable today — and record the wish against the
  proposed capability. A wish without a working fallback is a blocker, and a blocker
  caps the activity at draft.
- Never assume a capability exists because it plausibly should. The registry, not
  intuition, is the boundary.

## 10. Time is a budget, not a suggestion

One period per activity, hard cap: `activity_defaults.duration_min`. The default internal
split across the beats is `activity_defaults.phase_budget_min`; read the values there
rather than from memory. Content that does not fit becomes another activity
in the chain — that trade was accepted at the start. Do not compress the faded beat
to make room; it is the beat that looks most optional and is least.

## 11. Language and tone

- Voice is a teacher talking to students, not a textbook. Narrations are speakable.
- Precision beats friendliness where they conflict; say "expression" when it is an
  expression and "equation" when it is an equation.
- Lexical simplicity in the prose, full precision in the mathematics. Sentence
  structure stays simple — the difficulty lives in the maths, not the reading, and a
  multilingual student who can do the maths must not be assessed on English. But
  mathematical vocabulary is never simplified away: students need "coefficient,"
  "vertex," and "rate of change" flowing naturally, because those are the words the
  discipline and the exams use.
- Every technical term is marked with the definition capability
  ([[term :: meaning]]) in every activity — not just on first use. It is a tap-away
  reference, not an interruption; forcing a student to scroll back to wherever a
  word was first defined helps no one. The pop-up serves the student who needs it
  and is invisible to the one who does not.
- Name conventions honestly: "this is the gradient formula you already know, renamed" —
  unification is taught, not discovered.
- Contexts are real and checked. A context with fake numbers that fall apart under
  scrutiny teaches students that context is decoration.
- In NZ settings, use NZ vocabulary and conventions naturally (Year levels, NZ
  contexts where they help), without performing them. Concretely: *gradient*, never
  *slope*; `y = mx + c`, never `y = mx + b`; *Year 9*, never *Grade 8*. Skill and
  misconception **ids** keep whatever spelling they were minted with (`linear.slope.*`,
  `mis.form.m-b-swapped`) because ids are keys, not prose; every label, definition and
  narration a student can see uses the NZ term.

## 12. The human gate

Everything a model drafts is a **draft**. It does not count toward progress, it does
not ship, until a human has read it end to end and approved it. The model is a
drafter whose reasoning gets checked, not a colleague whose judgment is trusted.
Plausible prose at volume is the failure mode; the gate is the defense. An activity
that satisfies every rule in this document can still be wrong in ways only a teacher
reading it will catch — that reading is not optional overhead, it is the quality
mechanism.

---

## 13. Examples are minimal pairs

Across a sequence of worked and faded examples, vary **one feature at a time**:
signs, then the position of the variable, then a fraction coefficient. The student's
attention lands on the thing that changed because everything else held still.
"Varied practice" that shuffles every surface feature at once feels richer and
teaches less — the structure is buried under noise. This rule exists because
unprompted drafting defaults to variety; the sequence design is the instruction.

## 14. Practice discriminates

Once two confusable skills both exist (evaluate f(3) vs solve f(x)=3), independent
practice interleaves items that force the *choice* between them. Blocked practice —
six of one, then six of the other — inflates lesson-end scores and hides the
confusion, because the block tells the student which procedure applies and the item
never has to. The named misconceptions are the map of what to interleave: students
who know skills but not when to apply them is the failure this prevents.

## 15. Retrieval is closed-book

Review items are answerable from memory, with nothing on screen or in notes that
contains the answer. An item whose answer is visible tests navigation, not
retention, and the retrieval effect — the mechanism the review component exists
for — only occurs when memory does the work. Phrase accordingly: "find the gradient
through (2,1) and (5,7)" retrieves; "state the gradient formula" fails if the formula
is anywhere in sight.

**The reference panel is open-book for the whole activity, so it is part of "in
sight."** Nothing a review item retrieves may appear on the activity's `reference`
fence — not the formula, not a worked instance of the procedure, not the
definition being recalled. The author choosing what goes on the sheet is
simultaneously choosing what the review may no longer ask, and the two decisions
are usually made minutes apart by someone thinking about only one of them. Write
the review first, then the sheet.

## 16. Error analysis is a first-class item type

"A student wrote X — find and explain the error." These test the skill and the
misconception simultaneously, and the planted error always comes from a named
misconception id. Under an NCEA-first curriculum they carry extra weight: they are
the one format that keeps misconception targeting in auto-scorable form inside a
justification locale, so they are the main automatic data source when most DoLs are
rubric-graded. Use them routinely in DoLs and independent practice.
