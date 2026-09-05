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

## Proposed 2026-09-02 (NZ alignment pass) — NOT RATIFIED

Drafted on the `nz-alignment` branch against the sources quoted in
`docs/alignment-sources.md`. Each entry below is a proposal until a human reads the branch
end to end (§12). Ratifying one means quoting the artifact it changed, per the
`open-questions.md` rule; rejecting one means reverting its hunk, and the branch is laid out
so each hunk stands alone.

**D31 (proposed). `alignment` is four arrays, `ncea` exists, and the values are pointers into
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

**D33 (proposed). A locale carries what its grade levels require. `nz-ncea` now states A/M/E;
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

**D34 (proposed). Student-facing vocabulary is NZ; ids are not renamed.**
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

**D35 (proposed 2026-09-05, author-adopted from the review's counter-proposal; awaiting the
ratification sitting). Y8–10 DoLs default auto-scored; rubric justification is reserved for
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

