# Curriculum → Platform: skill-side state, and what reaches you

**Date:** 2026-08-26 · **Graph at v0.12.0**

---

## 0. Short version

**One file changes for you: `misconception-registry.txt`, 22 → 35 ids.** Everything else you
have installed is current.

That is the honest headline, and it is the point rather than an anticlimax. A week of
curriculum work — every skill in the graph instrumented, 26 slack activities allocated, four
consolidation rulings tested — reaches your side as one registry file. That is what the
boundary is supposed to look like.

---

## 1. Install now

**`misconception-registry.txt` — 35 ids** (was 22).

The merge you told us to do first is done. Thirteen new ids across the ten previously
uninstrumented skills, plus two new attachments of existing ids. Order was followed: ratified
→ merged into the graph → regenerated from the graph → and no id appears in any `.md` yet.

**Nothing binds to the 13 new ids today**, so this install cannot break the 13 live bindings —
it is a strict superset of the file you have. Your byte-identical-manifest check applies:
regenerating the coverage and binding manifests after installing this should produce **no
diff**, because the ids the corpus uses have not changed, only the set they are checked
against. If the manifests do move, something else did.

**Unchanged, do not reinstall:** `skill-registry.txt` (47 ids / 51 parts), `chain-registry.txt`
(17), `external-prereq-registry.txt` (5).

---

## 2. What is coming at you, and roughly when

Not asks. Shape, so nothing surprises a check you built.

**`chain_role: consolidation` will appear on about 13 files.** The D24 audit allocated the 26
slack activities: **13 consolidations, 14 additional skill parts.** One consolidation exists
today (activity 04). The other 12 arrive as their chains are authored. Your consolidations
correctly stay out of the parts numerator, so nothing changes in the logic — only the
frequency.

**`= n` values will grow in the skill registry.** Two are declared (`linear.model.contextual`,
`function.repr.correspondence`, both `= 3`). Twelve more extra parts are allocated at chain
level but not yet assigned to specific skills — that happens when each chain is written. So
the parts denominator climbs from 51 toward roughly 61 over the life of the authoring, in
per-chain steps.

Your `exceedsDeclared` warning is the thing to watch: a slot *decided* as a consolidation but
*authored* without `chain_role` fires it, which is exactly the check we wanted.

**The projection moves 73 → 74.** `chain.transform.translate` is short one activity — two
skills, two activities, and the thread's highest-value misconception is the confusion between
those two skills, so there is no room to interleave them. Chain 10, so not urgent. Recorded as
B4.

**Expect the two numbers to diverge.** 74 activities against ~61 declared parts means ~13
activities that never move the parts count, by design. Convergence would mean consolidations
had stopped being authored.

---

## 3. What is yours

**B7 — `curriculum-architecture.md` is stale and it is your file to refresh.** It was written
before the reconciliation: it describes the v0.10.0 world, predates the prose/JSON partition,
misses D18–D30, and asserts the §15 reference-panel rule that turned out never to have been
written into the principles at all. It exists to tell a codebase what the structure is, so
regenerating it from the graph is more in D7's spirit than rewriting it by hand.

**B10 — the structural pair-attachment report** (partial attachment in a 2-skill chain), if you
still want it. It feeds §7's authoring question rather than replacing it, and 2-in-6 precision
is fine for a report.

---

## 4. What is not yours, stated so the boundary stays clean

Skill authoring, chain allocation, misconception ids and their attachments, and the
consolidation rulings are curriculum-side and stay there. **The registries are the only
projection of that work you should ever need.**

One caution that follows: **the registry is not a picture of where the errors are.** Until
this week it was a picture of where the writing had been — attachment happened chain by chain,
authoring stopped at chain 1, and the ten uninstrumented skills turned out to be among the
best-documented misconception sites in the whole arc. That is fixed, but the general point
stands: do not infer curriculum state from registry shape.

---

## 5. Attached

- `misconception-registry.txt` — install
- `boundary-page.md` — the shared surface we discussed: open items with owners and landing
  artifacts, a numbered correspondence index, and a retractions table. Three rules on it worth
  reading before it fills up: nothing on the page that could disagree with an artifact; each
  side edits only rows it owns; **an item is not closed until the artifact contains the change,
  and you close it by quoting the artifact rather than describing it.**

That last rule is there because of §15. The rule was recorded as closed for months while the
amendment had never been written, and both a summary document and a run of correspondence
quoted a principle that did not exist.
