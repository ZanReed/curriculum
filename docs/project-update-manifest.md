# Project reference documents — what to update

**Date:** 2026-08-26 · Against the eight files currently in the project.

---

## Replace wholesale

**`thread-01-rate-of-change.json`** → **v0.12.0**
Registry **35 ids**; every skill carries at least one anticipated misconception (10 blanks → 0).
Everything this conversation changed lives here: the misconception merge (18→22 ids, 3 skills
attached), `grading_model` corrected, hook minimum on `approved`, `status_values.approved`
carrying D6's capability gate, D16's broadening and the floor clause in `review_selection`,
`grading.authoritative` deleted from all 22 capabilities, the four attachment fixes, the
`horizontal-direction` relabel, and the rewritten prose.

**`authoring-principles.md`** → the copy in this drop
Byte-identical to v0.12.0's `authoring_principles`, which is the D13 invariant and is now
tested rather than assumed. Six changes:
- §6: "Part 1 / Part 2+" → **chain position 1 / 2+**, with a note that chain position is
  unrelated to a skill part, and an explicit statement that spaced retrieval at position 2+
  is carried by the DoL
- §6, §8: the two-rows-back thresholds now **cite `review_selection.constraint`** and its
  floor clause instead of restating values
- §4, §10: hook minimum and the phase budget cite their keys
- §7: the attachment rule — *a misconception attaches to every skill that can elicit it*
- **§15: the reference-panel ambient rule, written in for the first time** — see §3 below
- **§7: the response-format rule** (D30) — a misconception about the *form* of a response
  binds only where the format admits that form and the item requires it

---

## Update in place

**`decision-log.md`** — append **D18–D30** plus amendments to D6, D8, D23, D24 (twice), D25, D27.
All drafted in `decision-log-additions.md`. Worth flattening the amendments into their
entries before appending; four decisions were amended within this conversation and the log
reads better without the archaeology.

**`open-questions.md`** — currently says *"(none — all prior questions closed)"*, which is
no longer true. Four genuinely open:
- **`chain.deriv.definition`** — the one consolidation ruling still resting on judgement.
  Revisit when its skills are instrumented.
- **NCEA alignment values** — the field shape is settled (all four alignment keys become
  arrays); the values need real achievement standards, and the graph's own instruction is to
  fill them from source documents rather than from memory. **This one needs you, not me.**
- ~~Ratification of the proposed misconception ids~~ — **closed.** 13 merged at v0.12.0;
  `mis.arith.*` split out from `mis.family.*`. Carriers remain predictions until items exist.
- **Whether `chain.transform.translate` gets its 74th activity** — I argued the plan is short
  by one at the site of the thread's highest-value misconception, and nobody has ruled it.

Also: the *standing reminder* about the hand-carried import-format sync should be checkable
now — the platform's generated format file was built to remove it. Verify before deleting it.

**`claude_chain-hooks.md`** — two corrections and it stays open as a holding pen:
- the pool minimum is now **`ceil(approved_activities / 2)`**, and the doc should cite
  `hook_contract.minimum` rather than restate it
- *"Projected activities: 4 → minimum hooks: 2"* uses the projected count, which is the rule
  we replaced
- add the authoring-order rule: **the pool is authored at chain creation, before the first
  activity.** Under the approved-based minimum nothing is owed until something is approved,
  which quietly makes hooks free — and free things get written last and badly, which is the
  retrofitted filler D9 rejected per-activity hooks to avoid.

The two drafted hooks are still unmerged; `hooks: []` on all 17 chains.

**`claude_misconception-proposals.md`** — **spent.** Its four ids were ratified and merged at
v0.11.2. Mark it closed rather than deleting it: it is the worked example of the
propose → merge → regenerate → bind order, and that order is now a standing step.

---

## Add

| file | why |
|---|---|
| `misconception-proposals-ten-skills.md` | **now also spent** — ratified and merged. Keep as the reasoning record behind 13 ids; the carriers are the testable claims |
| `curriculum-architecture.md` | the structural reference; needs a pass for v0.11.5 before it goes in |
| `catalogue-CLAUDE.md` | agent brief — invariants, declined list, routing |
| `skill-registry.txt` (47 ids, 51 parts) · `chain-registry.txt` (17) · `misconception-registry.txt` (22) · `external-prereq-registry.txt` (5) | the machine inputs |
| `partition-check.py` | gates the prose/JSON partition |

---

## Remove, or replace with a pointer

**`markdown-import-format.md`** (72KB) — under D25's three-region partition this is the
platform's region: generated from their importer's code and published as one doc. A copy here
is the thing D7 exists to prevent, and it has drifted twice before. Replace with a pointer to
the generated file.

**`thread-01-builder.html`** — not mine to change. One thing worth knowing: its *Save & load*
tab carries the hand-typed import-format copy that `open-questions.md` names as the single
hand-carried sync in the system. That is what the platform's generated file was meant to
retire.

---

## 3. The §15 gap, because it is the one that mattered

`open-questions.md` records that §15 was *"amended with the ambient rule."* **It was not** —
the text was never written, in any version, and I have been quoting the rule all week from
the open-questions summary rather than from the principles. Nothing that gets injected into a
drafting prompt has ever contained it.

Written in now:

> The reference panel is open-book for the whole activity, so it is part of "in sight."
> Nothing a review item retrieves may appear on the activity's `reference` fence — not the
> formula, not a worked instance of the procedure, not the definition being recalled. The
> author choosing what goes on the sheet is simultaneously choosing what the review may no
> longer ask, and the two decisions are usually made minutes apart by someone thinking about
> only one of them. **Write the review first, then the sheet.**

This is a pedagogical rule that had been recorded as done for long enough that both a
resolution note and an architecture document asserted it. Worth a look at whether anything
else in `open-questions.md`'s closed list was closed in summary but not in the artifact.

---

## On the focus going forward

Taken, and it matches where the value actually was. The findings worth having this week were
the ones only the curriculum side could reach — that a pair-confusion instrumented on one
side is a sensor pointed at half the phenomenon; that a label naming `f(x-h)` on a
point-slope skill would read as a mistake to the next author; that `rate.unit-rate` cannot
satisfy a two-rows-back rule because the graph is one edge deep there; that a shared
misconception is grounds to ask §14's question rather than to answer it.

The code understanding earns its place where it changes what can be taught — knowing that
numeric blanks carry no units is why `mis.rate.units-dropped` stays deferred and why error
analysis is the workaround; knowing the DoL is always captured but optionally graded is why
NCEA-first was affordable. Where it stops changing what can be taught, it stops being mine.

Concretely: no more checkers. `partition-check.py` gates something real and `fd-check.py` was
handed back. A third would be the tell.
