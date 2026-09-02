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

**What are the NCEA achievement standards for each skill?**
Blocked, and it needs a human with the source documents. `alignment` carries `teks`, `ccss`
and `nzc_phase` and no NCEA field, while D10 makes `nz-ncea` the default locale and D8
accepted a real data cost for it. So every DoL is authored against a standard the graph
cannot record. The field shape is settled — **all four alignment fields become arrays**,
because a standard spans several skills and a skill serves several standards — but that
change is agreed and not yet applied. The values must come from the standards themselves;
the graph's own note is right that nobody should fill these from memory.

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
