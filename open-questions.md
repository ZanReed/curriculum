# Open questions

Unresolved means the user decides.

---

**Does `chain.deriv.definition` earn a consolidation?**
The last of the four consolidation rulings resting on judgement rather than evidence. Its
three skills — f′(a) as a limit, as a tangent slope, in context with units — read as three
views of one object, which is the argument that earned `chain.rate.proportional` its
consolidation. But the chain shares no misconception id across its skills, so the proxy
cannot confirm it. Revisit when those skills are exercised by real items. *(The other three
resolved: `function.definition` confirmed earns, `function.families` confirmed does not, and
`function.domain-range` flags on the proxy but the no-consolidation ruling is held — a shared
error inside two skills is not confusability between them.)*

**What are the NCEA achievement standards for each skill?** — *CLOSED 2026-09-05 (D31
ratified as amended).*
Closed by quoting the artifact, as the rule requires — `rate.unit-rate` now carries
`"alignment": {"nzc_phase": ["P3.Y7.Number:S02", "P4.Y9.Number:S15"], "ncea": ["AS91945"],
"ccss": [], "teks": []}` and all 47 skills carry the four-array shape at statement grain
(D31 amendments: statement-grain pointers; `ncea` means assessed-by, else empty). What
remains judgment is named in the D31 entry: six borderline `ncea` keeps, author-kept pending
NZ colleague review. The three `linear.form.*` pointers remain the weakest (AS91256 not
re-read).

**Standing reminder — the alignment sources are copies of live pages.**
`docs/alignment-sources.md` quotes the NZC pages and NZQA documents as read on 2026-09-02.
The NZC pages are live and unnumbered, so the quotes are a dated copy of a moving document —
the same standing risk as the builder's Save & load copy, kept visible the same way. Rule:
no `alignment` value is cited in an authoring or ratification argument without checking the
file's read date; if it is older than six months (author-set, 2026-09-05), re-read the live
page first and re-date the file. Clears only if the NZC publishes stable, numbered
statements.

**Which qualification is the Year 8–10 work actually for?**
Cohort arithmetic (`docs/alignment-sources.md`, last table): every learner Y9 or below in
2026 sits NZCE/NZACE and never an NCEA standard; `nz-ncea` applies to the Y11–13 chains for
Y11 through 2027, Y12 through 2028, Y13 through 2029, and then to nothing. The `nz-nzce`
locale is a stub by construction — the Ministry's Tranche 2 (grading behind the A–E letters,
internal/external balance, the Phase 5 subject content) had nothing published on
2026-09-02. **Trigger:** when Tranche 2 lands, fill the stub and re-cut the DoL contract for
it; until then `nz-ncea` stands as the proxy (D33). Not a decision anyone can make early.

**Where should the spine's bands sit for NZ?**
Both ends, one rule. The calculus end: D32 proposed moving all thirteen `limit.*` and
`deriv.*` skills to Y12 — AS91262 (Year 12) differentiates polynomials and lists no limits;
AS91578 (Year 13) owns limits and continuity — and was **held** (2026-09-05): the same
evidence class (no statement at the claimed year; first assessed later) describes the middle
of the spine, where `function.*` (Y10) and `transform.*` (Y11) have no NZC Y9–10 statement
and are first assessed by AS91257 (Year 12) — yet Year 11 courses do teach f(x). Re-banding
one end on that evidence while leaving the other was the least defensible option, so neither
moves until the Phase 5 content is published; decide both with the document open. Also under
this question: whether `chain.linear.forms` keeps three skills for point–gradient,
`Ax + By = C` and conversion, which NZ classrooms rarely name and no NZC statement asks for.

**Does the limit chain's volume fit an NZ-first thread?**
Raised by the D31–D34 review. The thread gives limits nine activities
(`chain.limit.intro` 4, `chain.limit.difference-quotient` 5) and the difference-quotient
definition five more (`chain.deriv.definition`), for content NCEA Year 12 does not assess —
while the power rule, which AS91262 actually examines, gets six (`chain.deriv.rules`). An
NZ-first thread would invert that ratio. Re-banding the year labels would make the bands
honest and leave the volume US-shaped, which is why this question outlives the banding one.
Chunking-plan territory (D22–D24), and the one that costs authoring hours wherever it lands;
decide alongside the banding question above, with Phase 5 open.

**What does the school decide?**
Three facts about the school the author is moving to change how chains are used, and none
of them is in any document: the year levels it runs (in a Year 9–13 school the `rate.*`
chain is Year 9 diagnostic and review material, not four lessons); its period length (NZ
periods run roughly 50–100 minutes, so the number of activities a day carries is a school
fact, not a graph fact — the hook contract already assumes this); and which Y12–13 subject
the senior chains serve (*Mathematics*, not *Modelling* or *Statistics and Data Science*).
Owner: the author, on arrival. Nothing in the graph should be changed in anticipation.

**Does the plan move 73 → 74 activities?**
`chain.transform.translate` has two skills and two activities, and the thread's highest-value
misconception (`mis.transform.inside-outside`) is the confusion between those two skills — so
by the D24 criterion it earns a consolidation and has no room for one. Ruled here, not
ratified. Folding the interleaving into the second activity would push it past the duration
cap, and §5 says the faded beat is the first thing sacrificed when an activity runs long.
Not urgent: chain 10.

**Does `mis.arith.*` survive as a prefix holding one id?**
Split out of `mis.family.*` because that prefix was carving by skill domain where D21 says
prefixes carve by error kind. The reasoning holds — the squaring error recurs wherever a
quadratic meets a negative input, including vertex form in chain 12 — but a one-entry prefix
is thin. Revisit when chain 9 is authored and it is clear whether anything joins it.

**Should the hook-pool check key on folder existence rather than registry entry?**
The proposed trigger was *every chain registered in `chain-registry.txt` has a non-empty hook
pool*, on the premise that a chain is registered when its folder is created. All 17 were
registered at once instead, to fix the ordinal numbering while renumbering was still free —
so the check as specified fails on 16 chains that have no folders, no activities and nothing
owed. A check that fails on 16 correct chains on its first run is one that gets switched off.

---

*Standing note, not a question:* **every misconception carrier is a prediction until an item
exists.** The thirteen ids ratified at v0.12.0 name distractors that *could* hold them, in
activities not yet written. An id whose carrier turns out to be unwritable should be sent
back, not given a strained item to justify it. Revisions from authored-activity data are
expected.

*Standing reminder — verified live 2026-09-02, keep it:* the import-format rules in the
builder's **Save & load** tab are a hand-typed copy of the platform's prompt — the one
hand-carried sync in the system. The platform checked: `builder.html` still reads
`render_format.rules` from the thread JSON into that textarea and nothing in it fetches from
source. Verified on this side too — the canonical graph at v0.13.0 carries no `render_format`
key, so the copy that matters is whatever sits in a browser's localStorage, which neither side
can inspect.

**What changed is that it is now fixable rather than merely known.** The platform's generated
`docs/catalogue-authoring-prompt.md` is public and fetchable without auth, and CI fails on any
drift between it and its source. Delete this reminder when the builder loads from that URL —
not before, and not on the assumption that it has.

---

## Closed

**⚠ Reference sheets — closed twice, and the first time was wrong.** This entry previously
read *"principles §15 amended with the ambient rule."* **The amendment had never been
written.** Not in any version of the principles, and therefore not in anything injected into
a drafting prompt. The rule was quoted for months from this summary — including by a
curriculum architecture document that asserted it as fact — while the artifact never
contained it. Written in for real at v0.11.5: *nothing a review item retrieves may appear on
the activity's `reference` fence, because the panel is open-book for the whole activity;
write the review first, then the sheet.*

The rule this produced, which now governs this file:

> **An item is not closed until the artifact contains the change. Close it by quoting the
> artifact, not by describing it.**

Worth a pass over anything else that was ever closed here in summary. If one entry was closed
in description while the artifact stayed unchanged, others may have been.

**Ratification of the misconception ids** — closed. Thirteen merged at v0.12.0; every skill
in the graph now carries at least one anticipated error, where ten carried none. The
`mis.family.*` / `mis.arith.*` split is above as its own question.

**Consolidation as a pattern (D24)** — closed. A chain earns a consolidation when it produces
*confusability between its own skills*, not when it has a spare slot. All 17 audited; 26
slack activities allocated as 13 consolidations and 14 additional skill parts.

**Hooks for `chain.rate.proportional`** — closed. Two screened and merged at v0.13.0. Quoting
the artifact, as required: `chains[].hooks` now holds `hook.rate.better-value` and
`hook.rate.doubles-or-not`.
