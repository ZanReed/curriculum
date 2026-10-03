# Decision log — additions and amendments from the platform alignment exchange

Source: *Platform ↔ Builder alignment* (2026-08-26), *Builder → Platform reply*
(2026-08-26), *Platform → Builder answers* (2026-08-26), *Builder confirmation*
(2026-08-26).

Four new entries, two amendments. Written in the log's existing form — the decision,
the reasoning, and what it cost — and to the log's existing standard: a future
conversation that proposes violating one of these without naming it is drifting.

Append D18–D21 to `decision-log.md`; apply the amendments in place.

---

## New entries

**D18. Activity identity is a declared `key:`, not the file path. A split mints two
new keys and retires the original.**
Every activity file carries `key: act.<domain>.<kebab-name>`, minted once, never
changed, never reused after deletion. The platform matches on it; the path becomes
browsing decoration.
*Why:* the path *was* the database identity — moving, renaming, or splitting a file
orphaned the old row and created a new one, losing published history. D1 says
activities are disposable and get split and rewritten, so under path-identity every
operation our model calls normal was destructive. The key is the field that makes
folder layout free to change.
*Split convention:* neither child is the parent, so neither inherits. The alternative
requires an unappealable decision about which half keeps the published history.
*Cost, priced late and worth restating:* **a student's link is built from the database
id, so retiring a key invalidates every existing link to the original activity** —
for students, and for anything a teacher has handed out. Free at zero submissions.
Not free later. **Split before distribution, not after.** The no-reuse commitment is
enforced by an importer warning rather than discipline, because the uniqueness
constraint deliberately excludes soft-deleted rows: a reused key does not collide, it
silently mints a fresh-looking activity.

**D19. The platform's coverage manifest is the coverage artifact of record — a
knowing exception to D3.**
Coverage is read from the platform's committed `skill-coverage-manifest.md` /
`skill-coverage.json`. Our independent count is deleted, not kept as a cross-check.
*Why:* both sides were about to compute coverage from different inputs, which is D3's
failure mode in a fourth guise (after `authored[]`, two prompts describing one
platform, and the hand-typed format prompt). The platform's is better positioned: it
reports **what actually imported**, ours reported what we believed we authored. A file
that failed to import is not covered, and the manifest saying so is the manifest
telling the truth.
*Why this does not reopen D3:* D3 forbids a **hand-maintained** duplicate of derivable
state. The manifest is machine-generated from the importer's own walk on every run. The
rule it is an exception to is the narrow one — derived state is not *stored* — and the
exception is logged rather than smuggled.
*Cost, accepted:* it is **author-refreshed, never CI-gated.** Our `.md` files live
outside the platform repository, so CI cannot regenerate it and no drift check against
it could pass. It is as fresh as the last import run and no fresher. Mitigation: both
files carry a run timestamp and file count, and we refuse to quote coverage when the
manifest timestamp predates the newest `.md` mtime.
*Do not:* rebuild a parallel count "as a sanity check." That is the drift, not the
defence against it.

**D20. Item-level skill targeting lives in reserved `x_` meta keys in the activity
file. The `.md` is the authored source, not a render target.**
`x_review_skills:` and `x_dol_skills:` carry the skill ids each component targets. Any
key beginning `x_` is skipped by the importer with no warning; the platform stores
nothing, reads nothing, validates nothing.
*Why:* the platform will not hold block- or item-grain skill ids (an id it stores and
never reads is its most expensive defect class, and we agree). But validator rules 6
and 7 — the DoL's second item and at least one review item reaching two or more rows
back — need exactly that data, and both are ours. Without a home in the file it lives
in a parallel document keyed against an artifact D1 calls disposable. The reserved
namespace keeps one source of truth per activity for the price of a prefix check.
*Keyed on skills, not position:* an earlier draft used positional indices (`1=`, `2=`).
Position is not stable across rewrites — inserting one review item silently reassigns
every mapping after it, and nothing validates the namespace to catch it. Rule 7 is
existential, so a set suffices; rule 6 is well-defined on an ordered pair because §8
fixes the DoL at exactly two items.
*Cost:* the namespace is unvalidated **by design**, so a typo (`x_reivew_skills`)
silently disables rules 6 and 7 for that file. The importer's per-run receipt line
naming ignored `x_` keys and their file counts is the only sensor on this; it is not
optional.

**D21. Misconception prefixes subdivide by error kind — ratified.**
`mis.rate.*` for unit-rate and proportionality *computation* errors, `mis.proportional.*`
for *conceptual* errors about proportional relationships and their graphs. Two prefixes
within one chain, mirroring `roc` / `deriv` in the calculus arc.
*Why:* proposed on symmetry, ratified on evidence — the platform reports the distinct
prefixes measurably help its near-duplicate detector avoid false pairs across the 13
live bindings. Moved from "proposed, awaiting ratification" to ratified.
*Cost:* an authoring judgment call per id about which side of the computation /
conception line an error falls on. Where it is genuinely ambiguous, prefer
`mis.<domain>.*` matching the skill's own domain.

---

## Amendments to existing entries

**D8 — amendment (2026-08-26). Auto-scores are server-computed, not client-computed.**
The original entry recorded the platform team's ground truth as "auto-scores are
client-computed and advisory." The first clause is **false** and was verified false
against code: the grading engine runs inside a server function and has no client
caller.
*What survives, and it is the load-bearing half:* only **teacher-entered grades are
server-authoritative**. Auto-scores are server-computed but are not the official grade.
*What this does not do:* it does not reopen D8. The decision was the two-axis split
(`scoring × captures_response` plus `score_shape` and authoritativeness), and the
distinction the split exists to preserve — advisory versus authoritative — is untouched.
Only the *where it computes* clause was wrong.
*Why the correction matters more than a typo:* `curriculum-architecture.md` is
explicitly a reference for the codebase. A session told to align code to the original
sentence would have moved grading client-side and reopened the answer-leak surface the
sanitize-and-strip design exists to close.

**D6 — amendment (2026-08-26). `approved` is the predicate; the platform's `published`
is the mechanism.**
D6 gates approval on two conditions: a human end-to-end read, and no dependency on any
`proposed` capability. Publishing is a human act performed in the platform app, so it
covers the first and **cannot** cover the second — the platform has no
capability-dependency concept and will not grow one.
*The rule:* we gate the act of publishing on our pre-publish dependency check, so
nothing reaches `published` with an open blocker. Given that, the two are equivalent in
practice and the platform's **covered (published)** count is correct by construction,
with no capability knowledge on its side and no coordination beyond us holding that
line.
*Why it needed stating:* left as a bare equivalence, an activity a human published
while it still depended on `seeded_data` or `nway_correspondence` would have counted as
covered — which is the exact failure D6 was written for, after the four-way
correspondence activity was marked approved while needing an unshipped capability.

---

## Not a decision, but it belongs somewhere: validator ownership

The §11 rule table in `curriculum-architecture.md` reads as one rule set. It is two,
across two systems, and the ownership column is now settled. Two changes from what that
document currently says:

- **Rule 9** (nothing a review item retrieves appears on the activity's reference
  panel) is **ours**, not the platform's deferred item. A rule owned by a party that has
  deferred it is a rule nobody runs, and the scope is narrower than it was priced: with
  `x_review_skills` in the file it is a lookup, not semantic overlap detection.
- **Rule 2** (exactly one primary skill) becomes machine-checked by the platform via
  `skill:`, required under `--strict`.

Both belong in the architecture document's table, not only here.

---

## Added 2026-08-26 (second exchange — multi-part skills)

**D22. The activity is the unit of scheduling; the skill is the unit of curriculum.
A skill may be delivered across two or more activities.**
`skill:` takes exactly one id per activity, and several activities may name the same
id. Parts are ordered by path order within the chain folder; nothing else declares
their sequence.
*Why:* the 20–25 minute cap (§10) exists so a teacher can slot an activity into the
period they actually have — it is a scheduling constraint, not a claim about how much
curriculum fits in one sitting. Forcing one skill per activity would either inflate
activities past the cap or fragment the graph into nodes that exist only to absorb
overflow. §6's part-2+ rule (a 60-second retrieval of the previous part, recovered
minutes to independent practice) already anticipated this shape; it had simply never
been stated as the normal case.
*The consequence that has to be written down:* **a chain whose skill count is well
below its activity count is expected.** A burndown reading activities-per-skill > 1 as
a smell will be wrong about most of the catalogue. The first session to notice 3 skills
across 4 activities in `chain.rate.proportional` proposed minting an integration node
to explain it; that conversation should not have to happen twice.
*What this does not weaken:* §2's "exactly one primary skill per activity" survives and
is reinforced — it is the rule that makes parts legible at all.
*Guardrail, so "part 2" does not become a dodge for an over-stuffed activity:* parts of
one skill **share a DoL target**. If part 2's DoL assesses something part 1's DoL could
not, it is a second skill, not a second part. Mechanically checkable, because §8 fixes
the DoL at exactly two items: the first `x_dol_skills` entry must be the same id across
both parts.
*Cost:* coverage stops being a boolean. A skill is covered only when every declared
part is published — see D23.

**D23. Planned part count is declared once, in `skill-registry.txt`. Coverage is
partial until every part is published.**
A bare id is a one-part skill; `id = n` declares a skill delivered in n parts.
Coverage reads: uncovered / partial (m of n) / covered, with the D6 publish gate
composing on top — a skill is **covered (published)** only when all n parts are
published.
*Amended before shipping (2026-08-26):* only activities marked `chain_role: part`
(the default) count against the declared count. A consolidation activity names a skill
as primary but does not teach it and is **not** one of its parts — see D24. Counting it
would make coverage read partial for a skill that is fully taught, which is the
opposite of the error this field exists to prevent.
*Why declared rather than derived:* only the author knows whether part 2 is coming.
Counting activities gives how many parts *exist*, not how many are *planned*, and the
gap between those two numbers is the entire reason the field exists. This sits inside
D3's stated exception — estimates are facts about intent, not derivable state.
*Why on the skill and not the activity:* `parts: 2` in each activity's meta fence
declares the same fact twice and the copies can disagree. D3's intent exception covers
declaring a non-derivable fact; it does not license declaring it in N places. The part
count is a property of the skill, so it lives with the skill.
*Cost:* one declaration per multi-part skill, and a new drift surface — a stale `= n`
after a part is added or cut. Mitigated by an importer warning when the activity count
naming a skill exceeds its declared part count.

**D24. Consolidation is a distinct chain role, not a part of a skill.**
Every activity in a chain is a **part** (teaches or continues teaching one skill) or a
**consolidation** (teaches no new skill; interleaves across the chain; sits after the
schema exists). A `chain_role: part | consolidation` meta key carries the distinction;
absent means `part`, so nothing already authored needs editing.
A consolidation still names exactly one primary skill — the chain's terminal skill — so
§2 is untouched. It simply is not one of that skill's parts.
*Why:* the two shapes are structurally different (a part continues teaching, faded
harder; a consolidation teaches nothing new and interleaves per §14) but look identical
to the platform, which sees only "a second activity naming skill X." Coverage is
computed on top of that distinction, so it has to be visible. Without the marker,
`rate.proportional-graph` reads **partial (1 of 2)** while being fully taught by
activity 03 — under-claiming completed work, which is worse than the over-claiming D23
was written to fix.
*Why a real key rather than the `x_` namespace (D20):* the coverage manifest depends on
it, and the platform cannot read `x_`.
*Scoping consequence — three checks are about parts only:* the
activity-count-exceeds-declared-parts warning (D23), the shared-DoL-target guardrail
(D22), and the part-adjacency warning. Each false-fires on a consolidation, which by
design sits at the chain's end and may be several activities from the part that taught
its primary skill.
*Open, and deliberately not decided here:* whether consolidation is a **chain-terminal
pattern** (every chain ends with one — in which case it belongs in the principles and
the chain projection should budget for it) or was an **opportunistic use of a spare
slot** in `chain.rate.proportional`. The builder's own account records that the
four-activity projection came first and the consolidation was fitted to it, so n = 1.
Rule this before chain 2 is authored, or a drafting model will infer the pattern from
a single instance.

---

## Amendments added 2026-08-26 (third exchange)

**§6 amendment — "Part" in the review paragraph means CHAIN POSITION and is renamed.**
The paragraph said *"Chain position governs the slice"* and then used "Part 1 / Part 2+"
to name it, one paragraph away from D22–D24's "part" meaning a piece of one skill. Three
uses of one word, two meanings, all load-bearing. §6's prose is the cheapest of the three
to change (a text edit, versus a parser and four live files), and it is the ambiguous
one. It now reads **chain position 1 / chain position 2+**; the word "part" no longer
appears in §6. `chain_role: part` and the registry's `= n` keep their meaning.

**Validator rule 7 is two clauses, and the split must be recorded or the mechanism looks
dropped.**
- **7a.** At **chain position 1**, at least one *review* item reaches two or more rows
  back.
- **7b.** At **every position**, the DoL's second item reaches two or more rows back
  (§8, uniform — already validator rule 6).

*Why the scope was missing:* §11 listed the unscoped version, and a validator
implementing it literally would fail three-quarters of a correct chain — chain positions
2+ get a 60-second retrieval of the previous position only, which is one row back by
definition. Found by the platform side reading the corpus rather than filing a violation.

*Why the second clause matters:* scoping 7a to position 1 alone reads as though spaced
retrieval is switched off for the rest of the chain, which would be a real pedagogical
loss — §6 calls retrieving only the previous skill *"yesterday's lesson repeated, not
spaced retrieval."* It is not switched off. It **moves component**: the DoL carries it at
every position. All four activities in `chain.rate.proportional` satisfy 7b. Rules 6 and
7 were sitting in §11 as unrelated entries when they are one mechanism split across two
components; annotate them as such.

**D24 amendment — `.docs/`, not `_docs/`.**
Reference documents live in `.docs/`. The importer's file walk collects `.md` files and
separately skips dot-directories; **a leading underscore is not special to it.** A
`_docs/` holding `.md` reference files would have been imported — the reference documents
landing as student-reachable worksheets, which is the exact failure the platform rejected
a chain-descriptor file over. The dot directory is a guarantee rather than a convention.

---

## Added 2026-08-26 (fourth exchange — graph reconciliation)

**D25. Authoring rules live in three regions with one owner each. Nothing appears twice,
and a check enforces it.**

| Region | Holds | Owner |
|---|---|---|
| `authoring_principles` prose | reasoning — why review comes first, why faded is mandatory, what a hook is for | curriculum |
| `activity_defaults` (JSON) | every fact a validator reads — budgets, edge distances, hook minimum, status values, contract shape | curriculum |
| the platform's generated format doc | fence syntax, meta keys, what `--strict` refuses | platform |

The prose **cites keys, never values**. The resolving question for any rule is: *does a
validator read this?*

*Why:* the two hand-maintained rule sets were D7's failure mode wearing new clothes, and
they had already diverged five ways — `final_position` existed only in JSON, D16's
broadening only in prose, the hook minimum said `projected` in one and `approved` in the
other, `grading_model` carried a false claim, and `status_values.approved` omitted D6's
capability gate. The third region is named explicitly because a two-region partition
invites someone to "complete" it by copying format rules into `activity_defaults`.

*Why not the original proposal:* the first version had prose authoritative and
`activity_defaults` generated from it. Generating structured constraints out of prose is
not tractable. Partition, do not project.

*Enforcement, and it is not optional.* A partition nobody checks is two copies within
weeks — the same decay as D7, just slower. `partition-check.py` fails the build when the
prose restates a value `activity_defaults` declares. It runs on one file, since both
halves live in the thread JSON.

*Two findings from building it, both worth keeping:*
1. **A bare-digit grep false-positives at ~60%** — on section refs (`§8`), worked examples
   (`f(3)`, `(2,1)`), and chain position labels (`Part 2`). It must suppress those and
   anchor on the unit or operator (`ceil(`, `60-second`, `20–25 minute`) rather than the
   digit. A check that cries wolf gets switched off — the same lesson as the `\$6.00`
   false-positive that killed the delimiter-scanning version of the math-blank detector.
2. **Word-spelled thresholds are invisible to any such check.** "One hook per two
   activities" and "at least one item reaches two or more rows back" are genuine
   duplications no regex catches without unacceptable false positives on ordinary prose
   ("exactly one primary skill", "two ideas in one activity"). The fix is upstream, not a
   smarter matcher: **thresholds are written as digits.** That makes the check sufficient
   rather than merely necessary. Spelled-out numbers next to a unit are listed as advisory
   and never failed on.

*Current state:* 6 hard violations in the prose at v0.11.0, all genuine — `20–25 minutes`
twice, the phase budget, `ceil(activities / 2)`, and `60-second`. Note that
`ceil(activities / 2)` in prose **already disagreed** with `ceil(approved_activities / 2)`
in JSON before the patch. The drift was live, not hypothetical.

**D26. `supporting_skills:` names only skills that are NOT ancestors of the primary
skill.**
Ancestors are already stated by the graph's prereq edges; restating one per-activity is a
hand-maintained duplicate that drifts when an edge changes (D3). Anything non-ancestral is
information the graph cannot express — which is the same gap `planting_for` fills on the
review side (D16). The field goes from mostly-redundant to all-signal.
*Consequence:* the field is empty across all four activities in `chain.rate.proportional`
and has been stripped. Coverage was unchanged by the strip, because every value removed was
an ancestor already covered as the primary skill of its own activity — evidence the field
was carrying no weight.
*Cost, accepted:* the `.md` is less self-describing. A drafting model has the graph
injected (D7) and a human debugging the catalogue has it open already, so the reader who
loses out does not currently exist.
*Corollary — external prereqs.* They are graph roots, so they are usually ancestors and
therefore usually excluded. **Not always, relative to a given primary:**
`ext.geom.coordinate-plane` is a prereq of `rate.proportional-graph` and not of
`rate.unit-rate`, so a unit-rate activity that plots something should name it. The
platform's `--external-prereqs` build is deferred with that as the trigger.
*Coverage semantics this settled:* a skill named only as a supporting skill and taught by
nothing is **uncovered**, not `partial (0/1)`. Coverage is about what teaches a skill;
leaning on one is not teaching it. The manifest distinguishes "leaned on, taught by
nothing" from untouched, because the first is the more actionable gap.

**D27. `capabilities[].grading.authoritative` is derived, not stored. And D8's
`captures_response` axis is confirmed load-bearing by a single record.**
Across all 22 capabilities, `authoritative` is a **total function** of `scoring` — auto →
advisory (13), none → none (7), rubric → teacher (2), no exceptions — and always will be,
because D8's model defines it that way. The cross-cutting truth is already stated once in
`grading_model.authoritative`. The per-capability field should be deleted and derived, or
generated from `scoring` if a consumer needs it materially.
*Why it matters, with evidence:* the D8 amendment corrected the false client-computed claim
in `grading_model` and **left 13 copies of it wrong** in `capabilities[]`, where the value
is enum-shaped and a tool branches on it. That is D3's failure mode caught in the act — a
correction applied to the source leaving duplicates behind. The fused term
(`client-advisory`, welding *where it computes* to *whether it binds*) made it harder to
spot, but duplication is what let it survive in 13 places.
*The check that finds this class:* for any two fields in a machine-readable region, flag
where one is a total function of the other across every record. A `Counter` over pairs;
it found this in one call. This is **not** an extension of the partition check (D25), which
asks whether prose restates a JSON value. This asks whether JSON restates JSON — D3 applied
within a file rather than across regions.
*The contrast, and it vindicates D8:* the same test on `captures_response` finds **exactly
one exception** — `explain`, scoring `none` but capturing `true`. That is the precise case
D8 was written for, after a single `graded` boolean misclassified it. So of the four
grading fields, the genuinely redundant one is the one that carried a false value into 13
records, while the one that looks redundant holds the single record the entire two-axis
model exists to preserve. Collapsing `captures_response` into `scoring` for tidiness would
misclassify `explain` again and nothing would flag it. `score_shape` is independent across
7 shapes. **The model is three real axes plus one stored derivation, not four.**
*Ownership, agreed with the platform:* capability grading shapes are reviewed by the
platform against the code before landing, the same way ids are checked against the graph.
Three corrections in that direction have now been the same claim.

**D25 amendment — the backtick hole.**
`partition-check.py` stripped all backticked spans before probing, so a threshold in code
formatting passed clean. Latent (the prose held zero backticked spans) but guaranteed to
bite, because D25 itself tells authors to cite keys and a key is exactly what an author
puts in backticks: the first person follows the rule, the second writes a value inside the
same formatting. Fixed by stripping backticked spans **only when they look like a key
path** — dotted identifier, no digits, no operators — and probing the rest. Regression
tested in both directions.

**D27 amendment — the field is deleted, and the FD check is a report, never a gate.**
`capabilities[].grading.authoritative` is removed from all 22 entries (v0.11.2). The
platform confirmed nothing on its side reads the capability registry at all — 0 references
to it anywhere in that repo. It is a projection of what the platform told us, not an input
it consumes.
*On the FD check proposed in D27, corrected by building it:*
1. **A cardinality guard comes before the judgement question.** Run over all six fields the
   scan reports **10** dependencies, five of them `note → everything`. `note` is free text
   with 10 distinct values over 10 records — ratio 1.00 — so it determines every other field
   by construction. As a source field's cardinality approaches N the dependency becomes
   vacuous; any id, timestamp, or free-text column flags everything. With the guard the run
   reproduces the platform's five exactly. Unguarded precision is 1-in-10; guarded, 1-in-5.
2. **It cannot be a gate, and the reason is not noise.** Of five guarded hits only
   `scoring → authoritative` is **definitional** (D8 defines it). `score_shape → status`
   breaks when a proposed capability's shape is decided while still proposed;
   `score_shape → scoring` breaks on a rubric-less short answer marked pass/fail, which the
   registry already permits. No threshold separates these from the real one. The
   discriminator — *is there a rule that makes this true, or is it merely true today?* — is
   printed beside every hit because only a human can answer it.
*The general rule this settles, worth more than the check:* **a check may be a gate when
what it detects is decidable from the artifact; it must be a report when the artifact
cannot contain the answer.** `partition-check.py` gates — whether prose restates a JSON
value is fully decidable from the file. `fd-check.py` reports — whether a correlation has a
reason is not a property of the data. This is a cleaner criterion than "how noisy is it,"
and it also explains why *remove the ambiguity upstream* (D25) has no analogue here: the
ambiguity is not in the notation.

**D28. Illustrative content is marked; unverified claims about the other system are asked
about. Both halves, or neither works.**
Twice, something illustrative from the platform was read as a factual claim: an invented
skill id (`proportional.graph-through-origin`, two exchanges chasing an id with no source)
and a hypothetical reader ("a tool branches on it," which held up deleting a dead field).
*Platform half:* anything illustrative is marked illustrative — invented ids, hypothetical
consumers, example values.
*Curriculum half:* a claim about the other system's internals is asked about before it is
treated as a constraint. In the second case the cost of asking was one line in a letter
already being written, and instead a recommendation was built around not breaking a consumer
whose existence was never checked — stated explicitly, which made an unverified assumption
look like diligence.
*Why both:* marking cannot cover every phrasing, and asking does not scale if everything
needs verifying. Together they close it, because the claims that most need asking about are
exactly the ones a marking convention will miss.

---

## Added 2026-08-26 (misconception authoring pass)

**D29. Thirteen misconception ids ratified and merged. Every skill in the graph now carries
at least one anticipated error.**
Registry 22 → 35. Skills with `misconceptions: []`: **10 → 0.** Plus two new attachments of
existing ids (`mis.roc.uses-endpoint-value` → `roc.average.secant`,
`mis.limit.equals-substitution` → `limit.notation`).
*Why it mattered:* the ten blanks were not the skills with the thinnest error literature but
close to the opposite — `deriv.f-prime-as-function`, the vertical line test, secant-vs-tangent,
"each input exactly one output" misread as one-to-one. Coverage had been tracking **authoring
order** rather than pedagogical need, because attachment happened chain by chain and authoring
stopped at chain 1. The registry was a picture of where the writing had been, not of where the
errors are.
*Prefix split, ruled:* `mis.family.*` was carving by **skill domain** where D21 says prefixes
carve by **error kind** — it held both "misunderstands what *parent* means" and "believes
(−2)² = −4", which are unrelated error types. Split: `mis.family.any-line-is-parent` stays;
the squaring error becomes **`mis.arith.negative-squared`**, a new prefix with precedent
(`ext.arith.fractions` already exists as an external prereq, so arithmetic is an established
category even though no arithmetic skill is taught). Accepted cost: a prefix holding one id.
The alternative buried an error that recurs wherever a quadratic is evaluated at a negative
input — vertex form in chain 12 among others — under a chain-9 label.
*Correction to the proposal document's own header:* it said twelve new ids and five new
attachments. The true counts are **thirteen new ids and two new attachments.**

**D30. A misconception about the FORM of a response binds only where the response format
admits that form and the item requires it.** (§7)
*Found by:* re-checking `mis.rate.units-dropped`, which had been deferred on the grounds that
numeric blanks cannot carry units. That is true but was **the wrong reason.** Even with
units-bearing blanks shipped, binding units-dropped to a blank that does not *require* units
would still be invalid — it would fire on every correct answer, because omitting units was
never a choice the student made. The id was **mis-scoped, not blocked.** Its carrier is an mc
whose distractor is the unitless value, available today.
*Why a rule rather than a note:* `mis.slope.units-dropped` and `mis.deriv.units-dropped` are
already registered across four skills, so the same trap waits in chains 2, 4, 13 and 16.
*Family:* same as the existing constraint that distractor maps go only on auto-scored
per-item types. Both concern a binding that cannot fire meaning something other than what it
appears to mean.

**D24 amendment — the four judgement rulings, re-tested against the merged graph.**

| chain | ruling | outcome |
|---|---|---|
| `function.definition` | earns 1C | **confirmed** — `one-to-one-required` on both skills |
| `function.families` | no C | **confirmed** — no shared id |
| `function.domain-range` | no C | **flags, ruling held** — see below |
| `deriv.definition` | earns 1C | **still judgement** — no shared id after the merge |

*The proxy's limitation, now demonstrated rather than argued:* `mis.function.domain-range-swapped`
attaches to both skills of `chain.function.domain-range`, so the chain flags, and the ruling is
still no-consolidation. **The proxy detects the same error appearing in two skills; the criterion
requires the two skills to be confusable with each other.** Reading domain from a graph and
restricting domain in a context are not confusable *tasks* — a student never has to decide which
applies. Same task, two settings; the shared error is made *within* each rather than *between*
them. Contrast `chain.function.definition`, where the student genuinely must choose between the
mapping definition and its graphical test.
**A shared id is grounds to ask §14's question, not to answer it.** Third checker in this project
to land on report-not-gate.
*`deriv.definition` remains the one open consolidation ruling resting on judgement alone.*

**Standing note — carriers are predictions until items exist.** Every carrier named in the
proposals is a sketch of an item in an activity not yet written. That is the correct order (the
id must exist before an item can bind to it), but it means each is a prediction. An id whose
carrier turns out to be unwritable should be sent back, not given a strained item to justify it.
The authored-activity data is the real test, and revisions from it are expected rather than a
sign the ratification was wrong.

---

## NZ alignment pass — proposed 2026-09-02, ratified 2026-09-05 (D32 held)

Drafted on the `nz-alignment` branch against the sources quoted in
`docs/alignment-sources.md`. The §12 gate ran twice: a prediction-before-reveal walk of the
four proposals (`RATIFICATION_LOG.md`), then a critical review that superseded it and
produced the dated amendments recorded inside the entries below. D31, D33 and D34 stand as
amended; D35 was adopted from the review's counter-proposal; D32 is held until Phase 5
publishes — see its entry. The author's ten-value spot-check against the live pages, at
statement grain, is recorded under D31.

**D31 (ratified 2026-09-05, as amended). `alignment` is four arrays, `ncea` exists, and the values are pointers into
`docs/alignment-sources.md`.**
`skills[].alignment` becomes `{nzc_phase: [], ncea: [], ccss: [], teks: []}` — the shape the
D24 audit already agreed — and the NZ pair is populated for all 47 skills. `nzc_phase` values
are `P<phase>.Y<year>.<Strand>` (a phase alone is two or three years wide and the refreshed
curriculum is written year by year, so phase-only values would say almost nothing);
`ncea` values are `AS<number>`. The quoted statement behind every value lives in
`docs/alignment-sources.md` with the URL and the date it was read.
*Why pointers and not quotes in the graph:* the NZC pages are live and unnumbered. A quote in
the graph is a hand-carried copy of an external document; a short pointer plus one reference
file that names its read-date is the same pattern as the boundary stamp.
*What it does not do:* make the claim checkable. Whether a DoL assesses at the level its
standard asks remains a human read, exactly as the D24 audit said.
*Weakest values, named so nobody reads them as strong:* the three `linear.form.*` skills
(point–gradient, `Ax + By = C`, convert) have **no** NZC Y9–10 statement and point only at
AS91256, whose text was not re-read. NZ classrooms rarely name those forms. Whether the
chain keeps three skills for them is the open question below, not a value to fill.
*Cost:* `ccss` and `teks` are now empty arrays rather than nulls — a consumer that tested for
`null` would need to test for `[]`. None is known; D28 says ask, not assume.
*Amended 2026-09-05 (author-ruled, from review):* a cell-grain value (`P4.Y9.Algebra`)
pointed at a dozen statements. Every quote in `docs/alignment-sources.md` now carries a
number (`S01`–`S27`), and each `nzc_phase` value names the statement it rests on
(`P4.Y10.Algebra:S23`-style). The ten-value author spot-check (2026-09-05) was performed at
statement grain against the live pages, and all ten held.
*Corrected 2026-10-01 (author-ruled):* S12 ("Using substitution…") is relabelled `P3.Y7.Algebra`.
On the Phase 3 page it sits in a cell spanning the Y7 and Y8 practice columns, and this file
labels such cells Y7, as for S07–S11. `function.notation.evaluate` now carries
`P3.Y7.Algebra:S12`. The other 13 labels from S01–S14 were checked against the page the same
day and are correct.
*Amended 2026-09-05 (author-ruled, from review):* `ncea` is defined — the standard whose
assessment **directly exercises** the skill, else empty; appears-in and feeds-into are not
recorded (feeds-into is derivable, and derivable state is never hand-declared). The culling
pass this forced: emptied `rate.constant-of-proportionality`, both `difference-quotient`
skills, `deriv.definition.at-a-point`, `deriv.from-definition.polynomial` and
`roc.average.function-notation` (first-principles content is directly assessed by no quoted
standard — itself a finding); dropped AS91262 from `limit.secant-to-tangent` (no limits in
its notes) and from the three `roc.average.*` values (average rate is not its assessment).
Borderline keeps flagged for the ratification sitting: `rate.unit-rate` → AS91945,
`rate.proportional-graph` → AS91947, `function.definition.*` → AS91257,
`deriv.justify.constant` → AS91262, `roc.average.from-table` → AS91946. *All six
author-kept 2026-09-05, explicitly pending review by NZ teaching colleagues; dropping one
later is a value edit under this definition, not a decision reversal.*

**D32 (held 2026-09-05). The calculus re-band is deferred until Phase 5 publishes; the seed
bands stand.**
Proposed: all thirteen `limit.*` and `deriv.*` skills move Y12/Y13 → Y12, from AS91262
(Year 12: differentiates polynomials, lists no limits) and AS91578 (Year 13: owns limits and
continuity). Held on review, by the author: the evidence class the proposal used — no
statement at the claimed year, first assessed later — is the same class cited for leaving the
middle of the spine (`function.*`, `transform.*`) alone, and one rule should treat both ends.
Rather than re-band one end on a history, both ends are recorded as one open question and
decided with the Phase 5 document open. The AS91262/AS91578 readings stay quoted in
`docs/alignment-sources.md` and are not in dispute; what is held is the band change, not the
evidence. Re-proposing the re-band without the Phase 5 document is drift; proposing it with
the document open is the expected close.
*Superseded 2026-09-25 by D36:* the author re-ruled deliberately with the Phase 5
year-by-year content still unpublished, on the AS-standards evidence alone — and met this
entry's one-rule-both-ends objection by re-banding both ends in the same ruling
(`deriv.*` to Y12, `function.*` to Y12 against AS91257, `limit.*` collapsed). The
supersession is named there, so it is a recorded overrule, not drift. The platform-side
tickler for Phase 5 remains useful as a verification trigger, not a decision trigger.

**D33 (ratified 2026-09-05, as amended). A locale carries what its grade levels require. `nz-ncea` now states A/M/E;
`nz-nzce` is an explicit stub with its confirmed facts, its unconfirmed ones, and a revisit
trigger.**
`activity_defaults.locales[nz-ncea]` gains `grades`, `levels` (Achieved / relational thinking
/ extended abstract thinking, in the standards' own wording), `dol_rule`, `calculator`,
`context`, `cohorts` and `sources`. §8 of the principles points at `levels` instead of
gesturing at "Merit/Excellence".
*The rule the entry introduces:* every rubric line on an nz-ncea DoL is tagged A, M or E,
in a reserved `x_dol_rubric_levels` meta key (D20 pattern — curriculum-owned, inert to the
importer), and the **chain** reaches E somewhere — naturally at its final position or consolidation; no single DoL is required to. *(Amended 2026-09-05, author-ruled on review: the proposed per-DoL bar — every primary-skill item reaches E — quietly made every DoL rubric-graded, contradicting §8's rule that marking load is a deliberate choice and mismatching NCEA practice, where Excellence is a holistic end-of-standard judgement rather than a per-lesson event. Under the chain bar the authored drafts conform as written — activity 02's A/M/M tagging is no longer a defect.)* The tag makes the level claim a recorded one a validator can read.
*Why the stub is written out rather than left as a label:* the cohort arithmetic. Every
learner Y9 or below in 2026 will sit NZCE/NZACE and never an NCEA standard, so the Y8–Y10
chains are authored against `nz-ncea` as a proxy, and a proxy should say what it is standing
in for and until when. Tranche 2 (grading, internal/external balance) had nothing published
on 2026-09-02; the stub names that and says nothing is authored against it.
*Default locale unchanged.* `nz-ncea` remains the default: the justification-weighted DoL
shape is the right guess for the successor on everything confirmed so far (A–E, no fully
internal subjects), and a Y8 student in 2026 sits no qualification at all.

**D34 (ratified 2026-09-05, as amended). Student-facing vocabulary is NZ; ids are not renamed.**
Labels, notes and misconception labels: *slope* → *gradient*, `y = mx + b` → `y = mx + c`,
*point-slope form* → *point–gradient form*, *standard form* → *general form*
(`Ax + By = C`). *(Amended 2026-09-05: the pass originally demoted *standard form* to a
description, claiming NZ has no name for the form. Wrong — NZ texts say* general form*,
usually written `ax + by + c = 0`; caught on review, author-confirmed.)*
`chain-registry.txt` display title `Slope` → `Gradient`. §11 of the principles now says this
concretely. Ids (`linear.slope.*`, `mis.form.m-b-swapped`) are untouched: they are keys, an
activity's `x_review_skills` references them, and renaming a key is a D18-class event with
no student-visible benefit.
*Left as is, deliberately:* *parent function* (`function.family.*`). NZ usage is mixed;
changing it would be a preference, not a correction. *(The claim that the term appears in
AS91257 resources was asserted from memory and is unsourced — flagged on review; the stay is
author-confirmed 2026-09-05, on judgement rather than on that claim.)*
*Also left, by author ruling (2026-09-05):* *constant of proportionality*, in labels and in
activity 02, which is built around it. The gap analysis had flagged it as CCSS 7.RP.2
phrasing, and NZ Y8–9 teachers more often say *rate* or *the multiplier*; it stays as a
recorded judgement call — the term is teachable and the k it names is load-bearing — rather
than being dropped silently.
*Cost:* the registries regenerated (labels are in the comments), so the diff is wide for a
prose change. That is the generator working as designed.

**D35 (ratified 2026-09-05, adopted from the review's counter-proposal). Y8–10 DoLs default auto-scored; rubric justification is reserved for
chain finals.**
For learners Y9 or below in 2026, the nearest real assessment is the numeracy co-requisite
and, from 2028, the Foundational Award — procedural, closed, auto-scorable — the opposite
shape from justification-weighted rubrics. Meanwhile §8's data-cost argument bites hardest at
Y8–10, where activity volume is highest and marking lands on one teacher. The curriculum
still asks for reasoning, so justification is not dropped; it is *placed*: Y8–10 DoLs default
to auto-scored items plus an error-analysis item (§16), with rubric justification at
chain-final positions and consolidations; Y11–13 stays justification-weighted. This changes
the default D33 set for the Y8–10 chains and is recorded as its own decision rather than
folded silently into D33.

---

## Ratified 2026-09-25 (NZ-first scope rulings)

Ratified in conversation by the author, 2026-09-25; committed here by the repo session.
The source draft minted these as D35–D37, unaware the log had reached D35 on 2026-09-05;
renumbered D36–D38 on commit, internal references updated. D36 deliberately supersedes the
D32 hold — see both entries.

**D36 (ratified 2026-09-25). NZ-first authoring; non-NZ labelling retained but unpopulated.**
The curriculum is authored, banded and sequenced against New Zealand documents only: NZC
Phases 3–5 and NCEA / NZCE. Specifically:

- `band_nz` is the authoring band and gains Y7. The `band_labels.map` table and `band_us`
  field are retained as optional metadata but are no longer required on a skill and are not
  consulted by any check, review-selection weight or authoring decision.
- `alignment.ccss` and `alignment.teks` stay in the schema (arrays, default empty) so non-NZ
  alignment can be added later. No authoring task populates them; a validator must not
  require them.
- The `us-teks` locale is retained in the locale list but marked `status: dormant`. No DoL
  is authored or reviewed against it. Only `nz-ncea` (and `nz-nzce` once Tranche 2 is
  published) are active locales.
- Skill labels and `definitions` blocks use NZ vocabulary throughout (extends D34 to all
  remaining US terms: standard form, point–slope, parent function). Ids are unchanged.
- Sequencing is re-cut against the NZ documents: `limit.*` collapses to a single short
  chain inside Y12 calculus; `function.*` re-bands to Y12 against AS91257 and is trimmed to
  what that standard requires; `deriv.*` re-bands to Y12. *This supersedes the D32 hold,
  deliberately: Phase 5 year-by-year content remains unpublished, the author re-ruled on
  the AS91262/AS91578/AS91257 evidence alone, and the hold's one-rule-both-ends objection
  is met by re-banding both ends in this one ruling.*

*Reason.* Every learner this curriculum will be used with sits NZ qualifications. Carrying
a second live locale and band doubled the review surface on every DoL for no user. Keeping
the fields costs nothing and preserves the option; requiring them cost real decisions.
*Supersedes / amends.* D10 (default locale) unchanged. D34 extended. **D32's hold
superseded** (named above). The "dual" band mapping note in the graph header is replaced by
this ruling.

**D37 (ratified 2026-09-25). Senior content that depends on unpublished NZCE/NZACE detail
is deferred.**
No chain is authored for the following until the NZCE/NZACE subject assessment blueprints
(Tranche 2) are published — expected 2027:

- Y12–13 Statistics (thread 06 senior chains; AS91263–66, 91580–84 equivalents)
- Y12–13 Probability (thread 07 senior chains; AS91267–68, 91585–86 equivalents)
- Y12–13 Trigonometry (thread 05 senior chains; AS91259, 91575 equivalents)
- Y13 Calculus beyond AS91262 (thread 08's L3 chains; AS91577–79 equivalents)

Skills for these may be placed in the graph as stubs (id, label, band, strand,
prerequisites) so cross-thread edges can be drawn, but carry `status: deferred` and no
activities or hooks. The graph's burndown denominator excludes deferred skills.
Y12 calculus under AS91262 (`deriv.*` re-banded plus an anti-differentiation chain) is not
deferred: it is stable NCEA content for three more cohorts and the same material under NZCE
Mathematics.
*Reason.* Anything written against a qualification whose grading, internal/external split
and content weighting are unknown is likely rework. The deferred content is also the least
urgent for a Y9–11 classroom in 2027.
*Revisit.* When Tranche 2 lands, or if a placement makes a Y12–13 stats/calculus class the
author's own in 2027.

**D38 (ratified 2026-09-25). Scope is the whole of NZ Y7–13 mathematics, authored
bottom-up.**
The project's remit is every strand of NZC Mathematics and Statistics from Year 7 through
Year 13 (the eight threads in the Claude project's `drafts/y7-13-requirements.md` §5), not
thread-01 plus a single school's programme. Authoring proceeds year by year from Y7 upward,
all strands per year, so that at any point the curriculum is complete for every year below
the frontier:

1. Y7 — all six strands (threads 02–07)
2. Y8 — all strands; `chain.rate.proportional` (thread-01) is already written here
3. Y9 — all strands; `chain.linear.slope` / `chain.linear.forms` (in flight) fall here
4. Y10 — all strands
5. Y11 — all strands against NCEA L1 (AS91944–47) and the Y11 Phase 5 descriptor
6. Y12 — Mathematics (algebra, functions, AS91262 calculus); D37-deferred strands as stubs
7. Y13 — Mathematics (AS91262 consolidation); everything else D37-deferred

Because the placement is unknown, Y7–8 chains are authored as full lessons
(`role: lesson`), not review-only; a college locale may later down-role them without
re-authoring. OQ-E's second half is closed by this.
The in-flight `chain.linear.slope` hook pool is finished and merged before the order above
takes effect — abandoning reviewed work costs more than the sequence break.
*Reason.* The teaching placement could be any year and any strand; a curriculum complete
from the bottom is usable in whichever room the author lands in, while one complete in one
strand is not. Bottom-up also front-loads the content with the fewest external dependencies
(Y7–8 needs no datasets, no calculator policy decisions, no qualification blueprints).
*Cost.* ≈430 activities (§5 estimate, less D37 deferrals ≈ 330 live). A multi-year
programme at the current pace; the burndown denominator is re-seeded once the Y7 skill
stubs are in the graph.
*Amends.* OQ-A closed. `drafts/y7-13-requirements.md` §5 authoring order is superseded by
the year-by-year order above.

**Effect on `drafts/y7-13-requirements.md`** (Claude project document):
- §4 item 8 (two senior locales in parallel) stands; D36 makes `nz-nzce` the only future
  locale to add.
- §5 authoring order is superseded by D38 (bottom-up, all strands per year). §5's thread
  table and estimates stand.
- §6: OQ-A closed by D38. OQ-E closed (Y7 by D36; full lessons at Y7–8 by D38). OQ-G closed
  by D36 (`function.*` → Y12). Still open: OQ-B (thread layer), OQ-C (statistics DoL
  shape), OQ-D (dataset primitive), OQ-F (senior course lines). OQ-B is now the first
  blocker: the Y7 skill stubs cannot be placed until it is decided how threads live in the
  graph.

**D39 (ratified 2026-09-25). Threads live in one graph file, tagged on chains; the file is
renamed to match.**
OQ-B ruling. The graph stays a single file. It gains a top-level `threads` registry (id and
label per thread) and each `chunking_plan` chain carries a `thread` field; skills carry no
thread field — a skill's thread is derivable from its chain, and derivable state is never
hand-declared. The top-level `thread_id` is retired. The file is renamed
`curriculum-graph.json` in the same migration commit (the old name asserts thread-01-only,
which D38 makes false), with CI paths, script defaults, the builder fetch and both
boundary-page pointers updated in that one commit, and the platform side re-stamping after.
*Evidence.* Ruled after a live audit on a synthetic 8-thread / 376-skill scale-up built from
the real v0.14.0 graph: the existing `validate.js` and `generate-registries.py` run green on
the tagged single file unchanged (3ms parse, 39ms full validate, 312KB); a per-thread split
saves no bytes (309KB across 9 files), requires a composer wired into every consumer, and
creates a failure class the single file cannot have — duplicate ids across files. The
split's one real win, filename-scoped history, does not outweigh the plumbing. A future
split stays cheap by construction: the thread tag makes it sort-and-cut.
*Unblocks.* D38 step 4 — the Y7 skill stubs.


## Ratified 2026-09-28 (course glossary)

Drafted by the curriculum session in answer to the platform's glossary ask (Platform →
Curriculum page, "Ask: the course GLOSSARY as a canonical curriculum artifact", including
the row "PROPOSED v1 glossary file format"). The platform's proposal is
`docs/markdown-import-format.md` § "Course glossary" in `ZanReed/activity-platform`; its
reasoning is `docs/design/glossary.md` (D1–D9, W-2). Per that record's D8, the format is
the curriculum's to rule. **Status: ratified by the author in conversation, 2026-09-28.**

**D40 (ratified 2026-09-28). The course glossary: file, format rulings, gate, phasing.**

*The file.* `glossary.md` at the repo root is the course glossary. It is **hand-authored
and is the only place a glossary word is edited**. It is not generated, and the graph does
not carry it. Nothing in the graph references a glossary entry, and definition bodies are
prose with maths in them: storing them as escaped JSON would make them harder to review
and would add a sync step for no gain. Retired ids are listed in `glossary-retired.txt`
(hand-maintained, append-only, one `id   # date: reason` line each, the same grammar as the
registries). The ledger has to be a separate file because the glossary itself cannot show
what was taken out of it.

*The three format rulings:*

- **(a) A required, permanent `id:`, never derived from the term: ACCEPTED, with one
  curriculum-side convention.** An id is `gloss.` followed by a slug of the term *as it
  was first written*, and then it is frozen. The slug is minted once, not derived again
  later, so `term:` can be corrected under the same id. A change of spelling keeps the id.
  A change of meaning retires the id and mints a new one. Retiring means taking the entry
  out and adding its id to the ledger in the same commit. An id is never used again, even
  though the platform's store could un-retire it. The prefix follows `mis.`, `ext.`,
  `act.` and `chain.`, so any id in any file shows what kind of thing it names.
- **(b) `us:` is the only variant key, and the set is closed: ACCEPTED.** This fits D36,
  where US labelling is kept in the schema but not used. Two rules follow on this side.
  First, no definition body contains any entry's `us:` word, so the NZ-only rule is
  checked against the file rather than trusted. Second, a US word that is also an NZ word
  with a different meaning is **not** given as a variant. A variant takes that name for
  the whole file, so it would block the NZ entry. The case that exists now is *standard
  form*: the US name for the general form of a line, and the NZ name for scientific
  notation. `gloss.general-form` therefore carries no `us:` line.
- **(c) Bodies use the `definitions` grammar, NZ-only, with no `[[…]]`: ACCEPTED.** Two
  additions on this side. Terms and variants use a plain hyphen, never an en dash, because
  the platform does not fold dashes and activities type hyphens (`point-gradient form`,
  not `point–gradient form`). And a word with two school meanings gets **one entry that
  names both**, not two entries. For example, *range* gives the function meaning first,
  then the statistics meaning, and says the two differ. A student who meets both words
  gets the contrast where they look it up. This also keeps to one entry per word, which
  the format requires anyway.

*The gate.* `scripts/check_glossary.py` runs as a CI step. It checks that entries are
well-formed (fence, header order, id shape, the closed variant set, a body is present);
that ids are unique and terms and variants are unique as the platform folds them; the body
rules in (b) and (c); the size caps, set at half the platform's limits because the
platform measures the parsed JSON, which is larger than the source; and retire-not-rename,
checked against the git base. That last check means an id that disappears must be in the
ledger, the ledger only grows, and no id in the ledger comes back. A base that git cannot
resolve fails the check instead of skipping it. Whether every `[[term]]` resolves is the
platform importer's gate, because activity files are not in this repo.

*Phasing.* Glossary words come before the activities that use them, the same order as
hooks (hook pool, then activities). v1 covers thread-01: the four chain-1 activities,
`chain.linear.slope`, and every skill and misconception label in the graph. Each chain
authored after this adds its new words to the glossary before its first activity is
drafted. Y7 words arrive with the Y7 stubs (D38 step 4). An activity defines a word
locally only when it means something different by it. Wording drift in a local definition
is removed, not kept.

*Reason.* The author's 2026-09-27 ruling made the glossary a curriculum artifact that does
two jobs: it is the context for authoring and it is a gate. The platform's proposal already
had the identity rule this project uses everywhere else (keys are permanent, retire and
mint, never rename). Accepting it with side rules costs the platform nothing, and a
different shape would have cost it a loader change for no benefit to teaching.
*Cost.* One new file to keep, one ledger and one CI step. From now on every chain also
carries a glossary pass before its activities. The four chain-1 activities keep local
`definitions` fences that now shadow glossary entries, and the platform's first import
report will list them. Removing those fences is a separate edit to the activity files,
and the author decides it.
*Content questions, author-ruled 2026-09-28:* *parent function* stays for now, the D34
ruling, to be revisited only if a better NZ term turns up (the D36 list is read as not
reaching it). *Vertex* leads with *turning point*: the entry's first sentence is the
parabola meaning, and the corner-of-a-shape meaning comes second. *Secant line* stays and
does not become *chord*, also for now. The general form is shown both ways,
`ax + by + c = 0` and `Ax + By = C`.


## Ratified 2026-09-29 (Y7 DoL default; hook batching)

Ratified in conversation by the author, 2026-09-29; committed here by the repo session.
D41's short-chain count was corrected from 7 to 5 on commit, with the author's approval
(the entry's own 19 → 14 arithmetic removes five chains).

**D41 (ratified 2026-09-29). D35's DoL default extends to Y7, unchanged.**
D35 was ratified on 2026-09-05, when `band_nz` started at Y8. D36 added Y7 on 2026-09-25,
and nothing since has said which default a Y7 DoL takes. This entry closes that gap rather
than leaving Y7 to inherit D33 by silence. Y7 DoLs default to auto-scored items plus an
error-analysis item (§16), with rubric justification at chain-final positions and
consolidations, exactly as D35 sets for Y8–10.

D35's two reasons hold more strongly at Y7, not less. The nearest real assessment for a Y7
learner in 2026 is the numeracy co-requisite, then the Foundational Award, which is
procedural, closed and auto-scorable. And activity volume is highest in the intermediate
years, where marking lands on one teacher. A third reason applies only here: a written
justification at Y7 measures writing as much as mathematics, so it is a poor default and a
good occasional demand.

Cost, accepted knowingly. Y7 chains are short (5 of the 19 stubbed chains have two
activities or fewer), so chain finals are a large share of Y7 activities. At stub counts,
19 of 62 projected Y7 activities carry a rubric DoL, against 1 in 4 on
`chain.rate.proportional`. The lighter alternative was considered and not taken:
rubric only at consolidations and at the finals of chains with three or more activities,
which gives 14 of 62. Revisit this if the marking load proves real in a classroom, not
before.

Scope. Y7 only. D35's own text still names Y8–10; this entry does not edit D35. From now
on, "the D35 default" means Y7–10.

**D42 (ratified 2026-09-29). Hooks are authored in year batches: a concept bank per year, then full hooks per chain.**
When a year's chains are stubbed, one pass writes a one-line hook concept for every chain in
that year, across all strands, and the bank is screened as a set. Each concept gives the
chain, skill(s), context, the question or tension, the misconception it sets up, and whether
the context is NZ/Pacific. A chain's full hooks are finished from the screened concepts just
before that chain's activities are drafted. The rule that the hook pool is authored and
screened before any activities is unchanged at chain level; this entry adds a year-level
stage in front of it. Batches follow D38's bottom-up order: Y7 first, then upward.

Why. Authoring hooks chain by chain gives no view of a year as a whole: settings repeat
between chains, and the spread of Aotearoa/Pacific contexts is left to chance (it becomes a
standard requirement at Y11, AS91945). A year bank fixes both in one screening sitting.
Finished hooks written far ahead go stale when a chain's structure changes: the
`hook.slope.candle` closing note already depends on an unruled slack allocation. A one-line
concept is cheap to redo, so the batching happens at the cheap stage and the finishing
stays next to the activities.

Deferred to the end of the first pass, by Zan's choice:
- The in-flight `chain.linear.slope` pool is finished as it is, then checked for repeats
  against the Y9 bank.
- `chain.rate.proportional`'s hooks are checked against the Y8 bank.
- Whether `chain-hooks.md` names the year bank, and whether the bank lives there or in its
  own file.

Platform. None expected: the concept bank is curriculum-side prose and the hook contract
(`activity_defaults.hook_contract`) is untouched. The platform side confirms this on the
boundary page.

---

**D43 (ratified 2026-10-01). Practice lives outside the activity, in two generated block
types. A period is assembled from activities and practice blocks, and the period stops being
the activity's unit.** (§10 amended, §17 new)

*The gap:* a period runs 50–100 minutes, but an activity is capped at
`activity_defaults.duration_min`. Even with a hook, about half of every period had no plan.
The aim is to fill that time with evidence-based practice that the teacher **runs premade**,
not content generated and managed per class.

*Ruled: activities stay short, and practice is separate.* Making activities larger was
considered and rejected for three reasons:

- It breaks the one-skill, one-budget contract (§3, §10).
- It *masses* practice on the day's skill, the opposite of the spacing and interleaving
  findings.
- It raises the authoring cost of every activity.

*Two practice types, not three.* An earlier proposal split spaced retrieval from interleaved
practice. They merge because interleaving pays off only where the student has to *choose*
a method (Rohrer et al. 2020). Mixing unrelated skills is spacing, not interleaving.
So there is one mixed block, scheduled by spacing, that places confusable skills next to
each other. It uses the same confusability judgement as D24 and the same "practice
discriminates" logic as §14.

- **`practice.fluency`:** facts to automaticity, set per class, recommended by a
  diagnostic.
- **`practice.mixed`:** spaced review across taught skills, interleaved where skills are
  confusable.

*Double periods take two activities,* with practice between them. One activity per double
period would leave half of it as padding at one-skill-per-day pacing.

*Fluency is not assumed from year level.* Students reach Y9 without Y7 facts. A class-entry
diagnostic recommends whether the sprint runs. The teacher decides. When the sprint is off,
its minutes go to mixed practice by default, and the teacher may take them back. The
curriculum does not author SEL or other non-maths content for that time.

*Recommendation rule:* the median-based rule from classwide-intervention research (Burns
et al. 2014, Maki et al. 2021, as summarised by the Iowa Reading Research Center, 2025). If
the class median is below the fluency criterion, the diagnostic recommends switching the sprint
on. The simpler alternative in the same literature, more than half the class below
criterion, gives a similar answer. Where the class median is above criterion, students below
it still get fluency items, inside their own mixed practice.

*Late joiners* get their own diagnostic. It covers what a newcomer is missing: skills the
class has already been taught, not only upcoming prerequisites.

*Caveat:* the threshold and fluency-rate research is almost entirely US elementary
(CBM, Deno & Mirkin 1977; Spring Math, VanDerHeyden et al. 2015). Using it at Y7–10 is an
extrapolation. Treat these as defaults and revisit them against classroom data.

*Platform wishes:* to be raised by name on the Curriculum → Platform page once this entry and
§17 are on `main`. The platform builds the scheduler, engine and session types. The
curriculum specifies the banks, the fact scope and the rules in §17.

*Still open (curriculum side):* the fact scope per year, mapped against the Phase 3 and 4
statements (only S33, squares to 144, is confirmed so far); the fluency criterion for
non-multiplication fact sets (the per-fact target of about 3 seconds for benchmarks is a
working definition, not a researched cut-off); a Y7 entry bank, since Y7 prerequisites are
Phase 2 skills that come before the graph starts; and §17 banks for the chains already
drafted (the slope chain and the four proportional drafts).

*Sources:* Rohrer, Dedrick, Hartwig & Cheung (2020), interleaved practice RCT; Cepeda et al.
(2006), spacing meta-analysis; Rosenshine (2012), Principles of Instruction; Haring & Eaton
(1978), instructional hierarchy; Deno & Mirkin (1977), CBM computation criterion; Iowa
Reading Research Center (2025), "Is Tier 1.5 needed?"
(https://irrc.education.uiowa.edu/blog/2025/07/tier-15-needed-steps-consider-classwide-reading-intervention);
VanDerHeyden et al. (2015), Spring Math (NCII chart,
https://charts.intensiveintervention.org/intervention/toolGRP/bdb383d94466879b).

## Amendments added 2026-10-02 (drafting order)

**D38 amendment (2026-10-02). Within Y7, geometry is drafted first; chain 2's activities
wait for Y9.**
Ruled by Zan 2026-10-02, on the platform's sequencing questions (B-9).
- *Chain 2.* D38's exemption covered `chain.linear.slope`'s hook pool only, and that pool is
  merged (`5994d35`). The chain's activities follow the bottom-up order and come up with Y9.
  They are not finished first as in-flight work.
- *Y7 strand order.* Geometry comes first, starting with `chain.geom.triangles-polygons`, so
  the figure primitive gets a real chain to be tested against. The figure-chain order already
  given to the platform stands: triangles-polygons, parallel-lines, area-volume,
  transformations, then nets last. The order of the remaining strands is not ruled yet.
- *Note, not a new ruling.* An activity cites skill ids from the registry, so the Y7 stubs'
  graph PR (`proposals/y7-chain-stubs.md`) has to land before the first Y7 draft.

**D43 amendment (2026-10-02). The fact scope per year is this side's first D43 piece.**
Ruled by Zan 2026-10-02. Of D43's open items, the fact scope per year, mapped against the
Phase 3 and 4 statements, is done first, because the platform's first D43 build is fluency
and diagnostics, and both need it. The non-multiplication criterion, the Y7 entry bank and the
banks for drafted chains follow. No practice-item format is started until the platform's
design pass asks for one.

**D43 amendment (2026-10-02). Answers to the platform's fluency and bank-contract questions.**
Ruled by Zan 2026-10-02, on the platform's eight joint questions (B-11) for its D43 design
pass (draft, `docs/design/practice-blocks.md` in the platform repo).
1. *Fact scope.* The graph carries a machine-readable fact scope per year (fact families and
   their ranges), generated into a registry file under CI like the other registries. The
   platform generates fact items from it; nobody authors individual facts. Per D25, anything
   the platform computes from lives in the graph, not in prose.
2. *Criterion.* One criterion per fact family, held as a graph key the platform mirrors. A
   fact meets it only when it is answered correctly *and* within time.
3. *Probe shape.* A fixed item count, so every student's per-fact timings are comparable. This
   departs from the fixed-duration probes in D43's sources, so D43's caveat covers the
   cut-off.
4. *Strategies.* A strategy for a fact answered wrongly is authored on this side, one per
   fact family (for example doubles, near squares, ×9 from ×10). The platform fills it in for
   each fact.
5. *The diagnostic's skill half.* Bank items, not catalogue activities. An activity is a full
   teaching unit, and the §17 banks serve both diagnostics and mixed practice.
6. *Bank format.* Accepted as proposed: the existing catalogue markdown in a new practice file
   kind keyed by `skill:`, with a per-session seed. Two asks go with it: (a) constraints
   between seed variables, such as divisibility or excluding degenerate cases; (b) a way for
   a discrimination item to name its confusable skills, since one `skill:` key cannot hold the
   consolidation items §17 requires.
7. *Typing baseline.* Measured per student. The criterion applies to response time *net* of
   the baseline; raw times are kept as well.
8. *The Y7 entry bank* is both: Phase 2 facts in the fact scope (1), and a small set of skill
   items on the Y7 external prereqs (the `ext.*` ids).

**D43 amendment (2026-10-02, later). Turnaround facts, probe snapshots, and the class rule.**
Ruled by Zan 2026-10-02, on the platform's follow-ups (B-12, Q9–Q11), after a check of the
evidence.
9. *Turnarounds.* 7×8 and 8×7 are one fact for mastery, with one record per pair, and the
   probe and the sprint show it in both orders. Evidence: practice in one operand order
   transfers almost fully to the other, and the identical-elements model stores both orders
   as one item (Rickard, Healy & Bourne 1994). The small speed gap left on the unpractised
   order is perceptual, which is why both orders are shown (Rickard & Bourne 1996). Gains from
   cover-copy-compare in the classroom also generalise across the turnaround. Caveat: the
   memory studies are mostly with adults.
10. *Probe snapshots.* A probe's verdict is fixed when it closes and is not re-judged
   against a later criterion. The raw timings kept for the school year are what recalibrate
   the criterion.
11. *Class rule.* Per-fact `met` (answer 2) stays for the sprint and for each student's
   mastery. The class-level recommendation uses a rate instead: the class median of answers
   correct per minute on the probe, compared with an instructional-range floor. Below the
   floor, the sprint is recommended. The floor is a curriculum-owned graph key, set with the
   fact scope (answer 1). This is the researched form of the rule: classwide-intervention
   screening compares the class median rate with an instructional range (Spring Math), and no
   study sets a cut on a median share of facts met. Interim source for the floor: the grades
   4–5 instructional range in Burns, VanDerHeyden & Jiban (2006), whose unit is digits
   correct per minute and so needs converting to answers per minute. Using it at Y7–10 is the
   extrapolation D43's caveat already covers.

**D43 amendment (2026-10-02, third). The class floor's form, the student grouping rule, and
the rate's time basis.**
Ruled by Zan 2026-10-02, on the platform's two questions (B-16), with items 12 and 14 revised
the same day after review. Closes the time-basis gap flagged in the platform's
`docs/design/practice-blocks.md`. §17's recommendation sentence is repointed in the same
change.
12. *Floor form.* One floor per year level, calculated from the criteria and not authored. The
   probe is cumulative (§17: facts up to and including this year), so the mix of fact families
   grows by year. Families that are two steps in disguise take longer even for fluent
   students: division (solved through multiplication), integer operations (recall plus a sign
   rule) and roots (squaring run backwards). The problem-size effect adds a smaller slowdown
   for larger facts (Zbrodoff & Logan 2005). So a single floor would misread a fluent Y9 class
   as slow.
   The floor for the probe "facts up to Year N" is the class rate a student would produce
   answering every fact in that probe exactly at its family's criterion, multiplied by one
   floor factor k that applies to every year:
   floor(N) = k × 60 × Σ n_f ÷ Σ (n_f × t_f)
   Here n_f is the number of items from family f in the Year N probe, and t_f is that family's
   criterion in seconds (item 2). The curriculum side authors only k. Each floor then follows
   from the criterion values and the probe mix, so changing a criterion moves every year's
   floor with it. Where the calculation runs is the platform's call. If every family is given
   the same criterion, the floors come out equal, which collapses this to a single floor
   without a separate ruling. This replaces item 11's interim source for the floor (the
   grades 4–5 instructional range in Burns, VanDerHeyden & Jiban 2006).
13. *Grouping rule.* Accuracy is checked first; the rule is not a majority comparison of wrong
   against slow answers. Each student on a probe is classified in this order:
   1. inaccurate: accuracy on the probe below 90%;
   2. fluent: otherwise, if at least 80% of the probed facts meet their family's criterion
      (item 2);
   3. slow: everyone else.
   Why accuracy comes first: the instructional hierarchy (Haring & Eaton 1978) has accuracy
   before fluency. The majority rule misclassifies a student with 8 wrong and 10 slow answers
   out of 30. It calls them "slow", but at 73% accuracy, speed practice only rehearses their
   errors. The majority rule also flips back and forth when the two counts are close. Status of
   the values: 90% is in line with the acquisition-to-fluency criterion in the
   instructional-hierarchy literature; 80% mirrors the §17 success-rate target. Both are
   defaults to recalibrate against classroom data, not researched cut-offs.
14. *The rate's time basis* (closes the gap in item 11). "Answers correct per minute" means
   correct answers ÷ the summed net time of the counted attempts, in minutes. Net time is the
   same basis the criteria use (item 7), so the rate and the floor (item 12) are measured in
   the same units.
   - Net time of an attempt = raw time − (the student's typing baseline per keystroke × the
     keystrokes in the typed answer). A per-keystroke baseline removes the answer-length
     effect (typing 144 takes longer than typing 9). This refines item 7: the baseline item 7
     calls for is per keystroke, not per answer.
   - Net time is never less than zero. If the baseline deduction exceeds the raw time, the
     attempt's net time is zero.
   - Wrong and skipped attempts count in the time. They are counted attempts and are never
     correct, so their net time adds to the denominator and nothing to the numerator. A skip
     with nothing typed has no deduction, so its net time is its raw time.
   - An interrupted attempt is excluded from both the count and the time.
   - A timed-out attempt is included at the ceiling time, net of baseline, and is never
     correct. If nothing was typed, there is no deduction and its net time is the full ceiling.
   This supersedes the raw-time basis that was agreed in messages on 2 Oct.

*Still owed by 1 December 2026* (the platform's A4 ruling): the three values artifacts, which
are the fact-scope registry, the per-family criterion values, and the floor. Under item 12 the
floor artifact is the single floor factor k, not a rate; the per-year floors are calculated
from it. Items 12–14 fix the form; the numbers come with those artifacts. The proposed default
is k = 0.8. Suggested criteria: the single-recall families (multiplication, squares,
benchmarks) share one criterion, and the two-step families (division, integers, roots) get
somewhat longer ones.

**D43 amendment (2026-10-02, fourth). Where the probe's tunable values live, what "correct"
means, and the renamed group.**
Ruled by Zan 2026-10-02, on the platform's B-17, its follow-ups to the third D43 amendment
(items 12–14).
15. *Where the values live* (B-17, Q1). All of the probe's tunable values are graph keys. The
   platform reads them from the graph and invents none. They ship in the 1 December artifacts,
   alongside the fact-scope registry, the per-family criteria and k:
   - the accuracy threshold (item 13: 90%);
   - the facts-met threshold (item 13: 80%);
   - the response ceiling.
   Why: D25 puts anything the platform computes from in the graph. Keeping every recalibration
   value in one place means the first classroom data changes one place. The ceiling is the
   curriculum's value, not only a platform setting, for two reasons. It sets the time a
   timed-out attempt adds to the rate (item 14). It also marks the line between a slow strategy
   and one too slow to build on (item 16).
   Interim ceiling: 15 s, replacing the platform's proposed 30 s, until the 1 December values
   confirm it. Evidence: Siegler (1988, Table 1) timed third graders' multiplication by
   strategy. The means were retrieval 5.5 s, writing the problem 14.0 s, repeated addition
   23.3 s and counting objects 30.1 s. A 30 s ceiling cuts off only counting objects; 15 s cuts
   off most repeated addition, which is the strategy item 16 says to replace. The ceiling is set
   above a pure-recall cut-off (about 10 s) on purpose, to leave headroom for students with
   slower processing. Those data come from 8–9-year-olds answering aloud. The ceiling applies
   to net time (item 14), so typing is already removed.
16. *What "correct" means* (B-17, Q2). The platform's CR-6 is accepted as proposed. "Correct"
   means right and within the ceiling, everywhere: in the accuracy test, the facts-met test and
   the rate. A right answer given after the ceiling therefore counts against accuracy, as do
   wrong answers and skips.
   Why: a right answer past the ceiling is not slow recall. It is a counting or
   repeated-addition strategy, and speed practice on it rehearses the slow strategy instead of
   replacing it. Such a student needs the same thing as one who answered wrongly: direction to
   an efficient strategy, such as a derived fact (7×8 as 7×4 doubled), before fluency work.
   With this definition, item 13's three groups line up with three teacher actions:
   - fluent: right within the family's criterion. No action.
   - slow: right, past the criterion but within the ceiling. A workable strategy; fluency
     practice.
   - needs strategy: wrong, skipped, or past the ceiling. Strategy instruction first.
   Rename: item 13's group "inaccurate" is renamed "needs strategy", because the group now
   includes right-but-too-slow answers and the name should say what the teacher does next.
   Item 13's order, its thresholds and its reasons are otherwise unchanged.

**D43 amendment (2026-10-02, fifth). Both groups below fluent are shown the efficient
strategy.**
Written by Zan 2026-10-02, after the fourth amendment (items 15–16).
17. *Teacher actions by group* (amends item 16's action list). The efficient strategy (for
   example, a derived fact such as 7×8 as 4×7 doubled) is shown to every student grouped slow,
   as well as to every student grouped needs strategy. It is shown for each fact family the
   student did not meet, not for every family on the probe. Students are grouped as a whole,
   but the strategy follows the per-fact records. What follows differs by group:
   - fluent: no action.
   - slow (right, past the criterion, within the ceiling): the strategy is shown for each
     family not met, then fluency practice.
   - needs strategy (wrong, skipped, or past the ceiling): the strategy is taught for each
     family not met until the student is accurate on that family, then fluency practice.
     "Accurate" uses item 13's accuracy threshold (90%), applied to that family's facts in
     practice. It is the same graph key under item 15, not a new value.
   Why: the platform sees time, not strategy. The ceiling (item 15) is only a proxy for
   "efficient strategy vs counting". An older student who skip-counts quickly can land under it
   and be grouped slow. A student working a two-step fact (for example 56 ÷ 7) with a good
   strategy can go over it. Showing the strategy to both groups makes either misgrouping
   low-cost: a slow student who already uses a derived fact loses little, and a quick
   skip-counter gets exactly what they need. Showing it only for families not met keeps that
   cost low, so practice time isn't spent on facts the student already recalls. The
   accuracy-first order (item 13) is unchanged: a student who answers wrongly still reaches
   fluency practice only once they are accurate.
   *Consequence for item 15:* a single ceiling value is enough for now. Per-year or per-family
   ceilings are not needed in the 1 December artifacts. Revisit them against classroom data,
   for example if derived-fact and counting times separate differently by year level.
   Groups, names, order and thresholds (items 13, 15, 16) are otherwise unchanged.
   §17's fluency bullet is amended to match in the same change.

*Correction to item 15 (2026-10-02):* Siegler (1988, Table 1) reports the strategy times as
**means**, not medians (checked against the paper by Zan). Item 15 now reads "The means
were"; the four values are unchanged.

**D43 amendment (2026-10-02, sixth). What the fact-scope registry carries, the answer
characters, the probe's mix and length, and how facts are displayed.**
Ruled by Zan 2026-10-02, on the platform's B-19, sent ahead of the fact-scope registry.
18. *Registry contents* (B-19, items 1–7). The registry is generated under this side's CI like
   the other registries. It is written in a deterministic order, and its header carries the
   graph version and a revision id. The same revision id always means the same content. It
   carries:
   - Year scope, authored as "what Year N adds". Each family appears in exactly one year, so
     the scope can't contradict itself. The generator also outputs each year's cumulative
     family list, so the platform doesn't compute it separately.
   - Per family: a stable id; a teacher-facing name; the operation; exact operand ranges, with
     any exclusions; the criterion in seconds (item 2); whether a turnaround pair counts as one
     fact (item 9); a weight (item 20); a display template and a spoken template (item 21); the
     strategy text (item 17).
   - Per year: a one-line teacher description for the probe picker. This is optional; if it's
     missing, the platform composes one from the family names.
   - The single values (item 15 graph keys): k, the accuracy threshold, the facts-met
     threshold, the ceiling, the minimum items per family (item 20) and the practice window
     (item 20).
   Strategy text may be missing from the registry's first revision. It is required before the
   sprint goes live, because item 17 shows a family's strategy to both groups below fluent,
   and the sprint can't run without it.
19. *Answer characters* (B-19, Q1). An answer is digits, with an optional leading minus and an
   optional decimal point. Nothing else is allowed.
   - Percent stays in the prompt, so the student types only the number ("0.5 = __ %").
   - No typed fractions. Fraction-to-decimal and fraction-to-percent prompts are allowed,
     because the answer is a number. A typed fraction raises an equivalence question (2/4 vs
     1/2) that a speed task shouldn't have to settle.
   - Primes and factors leave the sprint and move to mixed practice, where multiple choice
     fits. "Is 91 prime?" has a 50% guess rate, and "the factors of 12" is a list; neither is
     a single recalled number. This removes "common primes and factors" from D43's Y9–10
     working list.
   - The typing warm-up (the platform's CR-1) includes the minus and decimal-point keys
     wherever a family in scope uses them, so the per-keystroke baseline covers every key an
     answer can contain.
20. *Probe mix and length* (B-19, Q2 and Q4).
   - Mix: families are weighted equally by default, and each has a weight field in the
     registry. Proportional sampling would fill a Y9 probe with multiplication, the family Y9
     students are most likely to have mastered.
   - Length: a minimum of 5 items per family, so the probe length is the larger of 30 and
     5 × the number of families in scope.
   - What the probe decides: student grouping (item 13) and, for each family, met or not met.
     Item 17 shows the strategy for every family not met. A wrong flag on 5 items costs
     little, which was the point of item 17.
   - What practice decides: whether a needs-strategy family has reached accuracy (item 17).
     Item 13's accuracy threshold is judged over a rolling window of the student's last 10
     practice attempts on that family, not on the probe. Five probe items can't support a 90%
     test, because one slip in five is 80%.
   - The minimum (5) and the window (10) are graph keys under item 15. Both are defaults to
     recalibrate.
21. *Display* (B-19, Q3). Each family has an authored display template and spoken template,
   which the platform fills in for each fact. Display rules: use a true minus sign (−), never a
   hyphen, and put a negative second operand in brackets, as in −3 − (−5). Benchmark families
   state their form in the template.

**D43 amendment (2026-10-02, seventh). How the probe is assembled and timed, when a family
counts as met, and the template syntax.**
Ruled by Zan 2026-10-02, on the platform's B-20 (six probe questions, P-1 to P-6).
22. *Probe assembly* (B-20, P-1). The platform's proposal is accepted. The probe length (item
   20) is shared out across families by weight. Rounding is done so the totals come out exact.
   A family with fewer facts than its share contributes all of them, and the remainder is
   shared among the other families by weight. A family's minimum is 5 or its fact count,
   whichever is smaller. Without this, a family with fewer than 5 facts (a small benchmark
   family, for example) would be marked "not judged" (item 23) on every probe.
23. *When a family counts as met on the probe* (B-20, P-5). A family is met when at least 80%
   of its counted items meet the family's criterion. This uses item 13's facts-met threshold,
   the same graph key, not a new value.
   - Not judged: if interruptions leave a family with fewer counted items than its minimum
     (item 22), the family is marked not judged, not met or not met.
   - For the strategy display (item 17), not judged is treated as not met. Showing a strategy
     is cheap, which is item 17's own argument, so a family the probe couldn't judge gets the
     strategy rather than nothing. The teacher's view still labels it "not judged".
   - Teachers see met, not met and not judged per family for each student now, before the
     sprint exists, so strategy work (item 17) can start in class without waiting for the
     platform.
24. *Probe time* (B-20, P-2). The probe has no time cap. The student is told the expected time
   up front. The probe runs once a term and has to be a fair reading, so items are not cut to
   fit a slot. The worst case is about 50 items × 15 s, roughly 12 minutes, for a very slow
   student. The probe sits outside §17's daily period shape; the 5-minute fluency block is the
   daily sprint, not the probe. The class-entry diagnostic's two halves (facts, and the
   prerequisite skills from §17) may run in separate sittings, so a long facts half at Y10
   doesn't push the whole diagnostic past one period.
25. *Revisions and the practice window* (B-20, P-3 and P-4). Confirmed:
   - Revisions: one revision id covers scope, criteria and the single values together. Any
     change to any of them makes a new id (item 18).
   - Practice window: the 10-attempt window (item 20) is read by the sprint only. The probe
     doesn't use it.
26. *Template syntax* (B-20, P-6). Operands are written `{a}` and `{b}` (the same brace style
   as the catalogue's seed fence), and the answer blank is `__`.
   - The templates don't encode item 21's display rules. The platform applies them when it
     fills each fact: a true minus sign (−), and brackets round a negative second operand. A
     template only knows `{b}`, not whether it's negative.
   - The spoken template gives the words for the operation and the sign; the platform says the
     numbers. Spoken forms keep the sign of a number separate from the operation: "negative"
     for the sign and "minus" for subtraction. So −3 − (−5) is "negative three minus negative
     five". That distinction is what the integer families teach, and saying "minus three" for
     −3 blurs it. NZ classrooms use "negative" for the sign.

**D43 amendment (2026-10-02, eighth). What a fact family is, where Phase 2 facts sit, and the
probe length at Y9–10.**
Ruled by Zan 2026-10-02 on the builder's R1–R4 (review of `drafts/fact-scope-registry.md`,
checked against `main` at `03e8ed0`).
27. *What earns a family in the registry* (R1). A family is in the fact-scope registry only if
   it is a finite set the curriculum asks to be memorised, or a finite sign-rule or inverse
   extension of one. Unbounded procedures go to mixed practice.
   - The memorised sets are Phase 2's memorising lines: multiplication and division facts,
     square and cube numbers, and the decimal and percentage equivalents of common fractions.
   - The extensions are square roots (Y7), cube roots (Y8) and integer operations (Y8–9).
   - ×/÷ by powers of 10 (S54) leaves the sprint and goes to mixed practice. It is a
     place-value procedure over unlimited numbers, so per-fact mastery records would never
     build up. This is the same reasoning as item 19's removal of primes and factors, and it
     is the second change to D43's working list.
28. *Phase 2 families* (R2). Every family carries a source year. Phase 2 families are tagged Y5
   or Y6. The curriculum side doesn't teach them, but the Y7 probe covers all of them. Probes
   exist for Y7–10 only. This matches ruling 8 (the Y7 entry bank is Phase 2 facts plus `ext.*`
   items). It is also the design's starting reason: students reach Y7 and beyond without these
   facts.
29. *Multiplication and division to 12* (R3). Phase 2's Y4 line (2s–10s) and Y5 line (2s–12s)
   become one multiplication family and one division family, each to 12, source year Y5.
   Splitting them would add two families, and ten items, to every probe for one difference in
   strategy. The ×11 and ×12 strategy goes in the family's strategy text.
30. *Probe length at Y9–10* (R4). The cumulative scope is 7 families at Y7, 10 at Y8 and 12 at
   Y9–10. Under items 20 and 22, the probes are 35, 50 and 60 items, and 60 is accepted. The
   probe runs once a term and may have its own sitting (item 24). Lowering the minimum to 4
   items per family would base each family's met / not-met call on 3 of 4 correct. Item 24's
   "about 12 minutes" was an example, not a limit. At 60 items the worst case, every item at
   the 15 s ceiling, is 15 minutes. Typical recall time is about 4–5 minutes.
   *Before citing:* the Phase 2 and Phase 4 quotes behind items 27–29 were read through a
   summarising fetch. They need the same word-for-word check `proposals/y7-nzc-phase.md`
   passed before anything cites them as S-numbers. Until then they are cited by year and phase
   only.

**D43 amendment (2026-10-02, ninth). The fact-count guard, what "asks to be memorised" covers,
and which candidate facts stay out of the registry.**
Ruled by Zan 2026-10-02, on the builder's candidate list and its three registry questions.
31. *Fact counts are a cross-side guard.* The generator writes each family's fact count into the
   machine-readable registry. The platform's importer stops if its own expansion of the family
   gives a different number. Nobody types the counts by hand. This adds the count to item 18's
   list of what the registry carries.
32. *Item 27 clarified.* "A finite set the curriculum asks to be memorised" includes NZC
   Knowledge statements that state a fixed set of relationships, not only lines worded
   "Memorising". On that reading, `fact.units` is admitted, source year Y6. It holds 14 listed
   facts: metric length, mass and capacity relationships in both directions, plus 60 s in a
   minute and 60 min in an hour. Phase 2's Measurement lines state them as fixed knowledge
   (Y4–5 "There are 1000 millimetres in a metre…", the Y5 prefixes, and Y6 conversions
   including h, min and s). The numeracy co-requisite relies on them, and a calculator can't
   supply them.
   - Cost: 5 more probe items at every year level, giving 40 at Y7, 55 at Y8 and 65 at Y9–10.
     The worst case is about 16 minutes. Item 30's reasoning (once a term, its own sitting
     allowed) still applies.
   - The clarification does not admit facts on the grounds that NCEA uses them. An NCEA clause
     was considered and not taken. It would admit far more than units, and the other
     candidates fail a stronger test anyway: NCEA L1 and the co-requisite allow a calculator
     ("Estimate or calculate, with support of a calculator"). Automating a calculation a
     calculator does changes nothing at assessment. A relationship it can't supply does.
33. *Candidates that stay out of the registry* (mixed practice). Each is assessed, but none is
   tracked for fluency fact by fact:
   - Squares 13²–20², cubes to 10³, powers of 2 and of 10: a calculator covers them at
     assessment. Powers of 10 are a place-value procedure (item 27's reasoning).
   - Eighths and thirds as decimals and percentages: thirds can't be typed as exact answers
     (0.333…, 33⅓%) under item 19. NZC doesn't ask for eighths to be memorised, and the
     calculator covers them.
   - Calendar facts (24 h, 7 days, 12 months, 365 days): not in NZC's lines.
   - Pythagorean triples: a recognition task, not a single number answer.
   - Y8 volume and capacity (1 mL = 1 cm³, 1 L = 1000 cm³, 1 m³ = 1000 L): three facts that
     would cost a whole family. They're practised with the Y8 volume skill.
   - Primes to 50: stays in mixed practice. Item 19's reasons hold.
   *Before citing:* the Phase 2 Measurement quotes behind item 32, like the other Phase 2 and 4
   lines, were read through a summarising fetch and need the word-for-word check.

*Note (2026-10-02).* The word-for-word check that items 30 and 33 required before citing has
passed. Zan checked every quoted Phase 2, Phase 3 (Y8) and Phase 4 line against the live NZC
pages, and all matched exactly. The lines stay cited by phase, year and strand. No S-numbers
are assigned, because the check confirmed wording, not page position. The 13 strategy texts in
`proposals/fact-scope-registry.md` section 7 were approved as written by Zan the same day.

*Note (2026-10-02, later).* Two registry rulings by Zan, on the platform's B-23, recorded in
`proposals/fact-scope-registry.md` revision 5: (1) the named flag list is two flags,
`at_least_one_negative` (stated on the displayed operands, for integer add, multiply and divide)
and `exclude_plain_whole`; the former `at_least_one_shown_negative` meant the same thing and is
dropped. (2) Strategy text is stored as structured fields (`intro`, `lines` of label and text,
`example`) with no markup; the platform lays it out.

*Note (2026-10-03). Revision ids and retired ids for the fact-scope registry.* Ruled by Zan on
the builder's generator design note. These are agreements between the curriculum side and the
platform, so they're recorded here, not only in code.
- *Revision id* (items 18 and 25). The registry's revision id is the sha256 of the registry's
  canonical JSON body, with the generated header excluded. The body includes the single values
  from `activity_defaults.fact_probe` as well as everything under `fact_scope`, because item 25
  says one revision covers scope, criteria and single values together. The id therefore changes
  exactly when something the platform reads changes, and never otherwise. A graph-version bump
  elsewhere in the graph leaves it unchanged, and the platform can recompute it to confirm what
  it imported. The same id always means the same content.
- *Retired ids* (B-23, item 31). Family ids and listed-fact ids (for example
  `fact.units.cm-mm`) are never reused for different content once published. Retiring an id
  means adding it to `fact-ids-retired.txt`. That file is append-only, on the same pattern as
  `glossary-retired.txt` (D40). Nothing is ever deleted from it, and CI fails if a retired id
  appears in the registry again. To change what a fact means, retire its id and issue a new
  one. Editing the fact in place under the same id is not allowed.

*Note (2026-10-03). The Y7 stubs enter the graph (D38).* Zan read `proposals/y7-chain-stubs.md`
end to end and approved it, and ruled six encoding points on the builder's recommendation.
Graph v0.17.0 adds 50 Y7 skills in 19 chains (61 activities), 66 misconception ids (labels
and attachments from the stubs' screening), six external prerequisites, and `nzc_phase`
pointers from `proposals/y7-nzc-phase.md`.
1. `band_us` is `null` for Y7 skills, and the band map has a Y7 row saying "no US mapping
   (D36)". A Grade 6 equivalence would be an unchecked claim.
2. `band` and `band_nz` are both "Y7", matching the existing skills.
3. `ncea` is empty on all 50 Y7 skills (D31: no NCEA standard assesses Y7 content).
4. Calculator use, consolidation terminal skills and the confusability reasons stay in the
   proposal as the reasoning record. Calculator use becomes a ruled graph key (probably per
   chain) only when the platform or a validator reads it; prose in a note would look enforced
   when it isn't.
5. The Y7 chains land with `hooks: []`; the concept bank stays a proposal (D42: full hooks are
   written just before each chain's activities).
6. The cross-thread follow-ups (re-pointing thread-01 prerequisites from `ext.arith.fractions`,
   `ext.arith.signed` and `ext.geom.coordinate-plane`, retiring those ids, and the candidate
   edge `pattern.linear.graph` → `rate.unit-rate`) wait for their own ruling and PR, because
   they change existing skills the platform can see. This change only adds.

**D42 amendment (2026-10-03). A hook pool has at least one hook per skill.**
Ruled by Zan 2026-10-03, on the builder's pool for `chain.geom.triangles-polygons`.
`activity_defaults.hook_contract.minimum` becomes "max(skills_with_an_approved_activity,
ceil(approved_activities / 2)) hooks per chain", in place of "ceil(approved_activities / 2)".
*Why:* §4 says the minimum exists so no teaching day opens empty. At D43's 50- and 60-minute
period shapes a class does one activity per period, so a short chain spans one day per skill.
The old minimum gave a two-skill, two-activity chain one hook, and the day that starts the
other skill either opened empty or reused a hook aimed elsewhere. One hook per skill closes
exactly that gap; extra hooks still come only when they earn their place (§4). Counting skills
that have an approved activity keeps the old timing: with nothing approved, nothing is owed.
*Consequences:*
- Most Y7 chains (two skills, two activities) need 2 hooks where the bank holds one. Each short
  chain gets a second concept, screened against the bank, before its activities are drafted.
- `chain.rate.proportional` (3 skills, 2 hooks, activities imported) now owes a third hook, for
  `rate.constant-of-proportionality`. This reverses `chain-hooks.md`'s earlier reasoning that
  that skill needed no hook of its own. It is a follow-up, written and screened on its own.
- `chain.linear.slope` (3 skills, 3 hooks) already meets the rule.
- The platform confirmed in D42 that the hook contract was unchanged; this changes the minimum
  value, so the platform is told before this merges.

**D27 amendment (2026-10-03). The capability registry's derived fields come from a pinned copy
of the platform's facts file; our CI never fetches the platform's live main.**
Ruled by Zan 2026-10-03, answering the platform's B14 rebuild proposal (B-30 → C-30, accepted
B-31); landed with the checker in this repo's PR #26. The old `generate-capabilities.mjs` imports the platform's TypeScript and cannot run in
this repo's CI.
- **Ownership.** The platform owns the derived fields: `status` and
  `grading.{scoring, captures_response, score_shape}`. It generates them into its committed
  `docs/capability-facts.json`, under its own drift test. We own the authored fields: `label`,
  `medium`, `affords`, `constraints` and `grading.note`. Nothing generated touches them.
- **The gate.** This repo commits a pinned copy of that file, with the platform's source commit
  and the file's sha256 beside it. A CI check fails when a derived field in
  `curriculum-graph.json` disagrees with the pin, or when a capability entry has a field outside
  the known shape. That shape check replaces the B14 version gate.
- **The report.** A scheduled workflow, not a PR gate, fetches the platform's main and reports
  drift against the pin. When prose contradicts a fact (e.g. "graph grades up to quadratic"),
  that is flagged, never failed.
- **The pin bump.** Bumping the pin is the act that changes derived fields. A bump that changes
  any derived field gets pre-merge notice. When a capability ships, the platform opens the
  pin-bump PR, and we merge it.
*Why a pin, not a live fetch:* a live fetch would let a push to the other repo turn one of our
commits from green to red with nothing changed here. It would also make every PR here depend on
the network and on the platform's repo. Both break "green on main is current by construction".
It also breaks the earlier D27 amendment's rule that a gate must be decidable from the
artifact. With a
pin the gate reads only our own files; the drift is reported, the same split as
`partition-check.py` and `fd-check.py`.
*The fence join, ruled at the same time:*
- `correspond` maps to `nway_correspondence`, scoring `auto`. It adds a new `score_shape` value,
  `per_cell`, because it counts cells, not pairs. `score_shape` now has 8 values.
- `table` becomes a new capability entry: shipped, scoring `none`, `captures_response` false,
  `score_shape` `none`. Blanks inside a table score as `fill_blank`. Its prose is ours.
- `seed` maps to `seeded_data`, scoring `none`. It is a data source, like `definition`. The
  blanks that use its values carry the grading.
- `meta` is exempt: activity settings, not a capability.
- `draggable_curve` and `graded_polynomial` join through the platform's schema, not a fence.
*Also:* the four `proposed` entries flip to `shipped` in the same PR as our rewrite of their
prose, so there is no window where the status and the constraints disagree. The stale
workspace copy of `generate-capabilities.mjs` is retired, with a pointer to the new home.
*Stale prose fixed in the same PR, not flagged by the checker:* `graph`'s constraints said it
graded only five families and that "Cubic+ can be shown, not graded"; `dataplot`'s said every
dataset was a literal; §9 listed "literal datasets" among the example constraints. All three
are rewritten here for the reason the flips land with their prose. `graph` now points at the
pin's `prose_facts.graded_curve_families` rather than copying the list, so the family list has
one home.

**D44 (ratified 2026-10-03). Y7 geometry is drafted against the ruled figure grammar, with no
image fallback; the drafts are held at draft until figures ship.**
Ruled by Zan 2026-10-03, on the builder's draft of `chain.geom.triangles-polygons` activity 01.
Y7 geometry activities are written against the platform's ruled figure grammar
(`docs/design/y7-figures-and-charts.md` §4 Q3 in the activity-platform repo), not against a
shipped capability. They stay at draft until two things land: the figure capability ships, and
the platform's pin bump (its task T8b) adds it to this repo's pinned capability facts as
`shipped`. Approval still needs the D6 end-to-end read on top of that.
*Why this is an exception to §9, and a deliberate one:* §9 says to author the best fallback that
can be built today. Here that would be an image per figure, and every geometry activity would
be authored twice: once with images, once with figures. The figure build is short, and the
grammar is ruled and confirmed on both sides. So the cost of waiting is lower than the cost of
the duplicate.
*What it does not change:* §9 still holds everywhere else. The exception covers only the ruled
figure grammar, and it ends when the figures ship. No draft written under it can be approved or
imported before then. The platform's eng review may still adjust syntax, so each draft expects
one mechanical syntax pass against the generated authoring prompt when the build closes.
*Discharged 2026-10-04 for the capability half:* the platform's pin bump (its T8b) landed here as
PR #28, and `curriculum-graph.json` now carries `figure` with `"status": "shipped"`, pinned to
activity-platform `4df546a`. Drafts held under D44 are now authorable under §9, and still need the
syntax pass against the generated authoring prompt and the D6 end-to-end read before approval.

**D45 (ratified 2026-10-04). Thread-01's external prerequisites re-point to the Y7 skills
behind them; one external is retired, two are kept; the candidate unit-rate edge is
rejected.**
Ruled by Zan 2026-10-04. This is the cross-thread follow-up that the D38 note of 2026-10-03 ("The Y7 stubs enter
the graph", item 6) left for its own ruling.
1. `rate.proportional-graph`: `ext.geom.coordinate-plane` → `coord.four-quadrant`. The Y7
   skill covers everything the external named (plot and read points), so
   `ext.geom.coordinate-plane` is **retired**: removed from `external_prereqs` and the
   generated registry. The id is never reused.
2. `linear.slope.two-points` gains `number.integers.additive-inverse` and **keeps**
   `ext.arith.signed`. The Y7 skill covers adding and subtracting integers. The slope from two
   points also divides signed numbers, which no taught skill covers yet. The external retires
   when a skill for multiplying and dividing integers lands (Y8).
3. `rate.unit-rate` gains `number.fractions.to-decimal` (which carries
   `number.fractions.equivalent` transitively) and **keeps** `ext.arith.fractions`. Dividing
   fractions, as in chain 1's review item ¾ ÷ 3, is Y8 content. The external retires on the
   same terms as item 2.
4. The candidate edge `pattern.linear.graph` → `rate.unit-rate` is **rejected**. Under D2 an
   edge claims you cannot hold one skill without the other, and a unit rate can be computed
   without ever graphing a linear pattern. The link between them, the step as a rate, is a
   connection a review item may plant, not a dependency.
5. `activity_defaults.review_selection.candidate_pool` reads "transitive ancestors of
   primary_skill **in any thread** plus external_prereqs", in place of "in this thread". The
   old wording predates D39's single graph. Read literally, it kept the Y7 ancestors that
   items 1–3 link out of chain 1's review pool, which defeats the point of linking them.
   Cross-thread edges exist so that review can reach across threads.
6. Retired external-prereq ids go in `external-prereq-retired.txt`, which is append-only.
   Check 4 (I) fails if a retired id comes back as an external or a prereq. This makes
   "never reused" mechanical, as the glossary and fact-id ledgers already do (the
   platform's suggestion, B-43).
*Why re-point at all:* an external is assumed prior knowledge that the course never teaches.
Once the course teaches it, keeping the external would hide a real edge from the review pool
and the coverage report.
*Consequences:* graph v0.17.4. This changes existing skills, so the platform gets a pre-merge
notice and checks the branch first (promised in C-28). Chain 1's catalogue files cite
`ext.arith.fractions` and `ext.geom.coordinate-plane` only in `x_` keys, which the importer
ignores, so no import changes. The retired id stays in those files as a stale note until they
are next edited.

**D46 (ratified 2026-10-04). Chain folder ordinals are year-banded teaching order.**
Ruled by Zan 2026-10-04, on the platform's B-42 (answered from code): the `NN-` ordinal in
a chain folder's name is teaching order. Every teacher's outline is sorted by catalogue path,
across all courses in one list, and folders must be flat, because the chain is read from the
first path segment.
- The ordinal is **year × 100 + position within the year**: Y7 is 701–719, Y8 is 801
  (`chain.rate.proportional`, renamed from `01-`), Y9 is 901–903, and so on up to Y13's
  1301–1302. `chain-registry.txt` lists all 36 chains.
- Within Y7 the default order is strand order, following the graph's `chunking_plan`: number,
  algebra, measurement, geometry, statistics, probability. It is a default, and reordering
  later costs nothing.
- The 19 Y7 display titles are new authored prose in `chain-registry.txt`. The 17 thread-01
  titles are unchanged.
*Why year-banded:* a sequential 01–36 would list Y7 after Y13 in graph order, or need
renumbering every time a year's chains are added. Bands put Y7 first and give each year its
own range. Renaming a folder is safe because identity is `key:` (D18). The platform proved
this with 0 created, 4 updated and 0 orphans.
*Consequences:* chain 1's pilot folder is renamed `01-chain.rate.proportional` →
`801-chain.rate.proportional`, and the pilot root's `chain-registry.txt` is refreshed from main
in the same step. Both are in the author's folder. The platform gets a pre-merge notice, and
its `--chain-registry <path>` flag, which retires the hand-carried copy, is triggered by this
change.

