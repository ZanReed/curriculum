# Curriculum → Platform: spec for a fetchable curriculum repo

**Date:** 2026-09-02 · **Status:** request for build, from the curriculum side

---

## 0. What this is for

Your pointer rows carry a URL, a commit stamp, a sha256, and CI that fails on drift. Ours
name artifacts sitting in a Claude project — no link, no stamp, nothing you can fetch or
verify. The boundary page says so at the top, because the two halves of the channel should
not read as equally strong when they are not.

**The important half is not the repo.** Your guarantee is not *"it's public" —* it is
*"`catalogueAuthoringPrompt.test.ts` fails CI on any drift between source and doc, so the
copy on `main` is current by construction, not by discipline."* A repo without an equivalent
is a fetchable copy that can go stale, which is what we have now plus a URL.

So: a repo, and **four checks**. The checks are the ask; the repo is what makes them
visible to you.

---

## 1. The four checks

Every one already exists as something run by hand in a session. That is the problem — each
depends on someone remembering, and the first two break silently.

**1. `authoring_principles` is byte-identical to `authoring-principles.md`.**
The highest priority. D13 rests entirely on it: the pedagogy is stored once and injected into
every drafting prompt. It was checked by hand roughly eight times in one week of work. When
it breaks, nothing surfaces — a drafting prompt simply injects the wrong pedagogy and the
output looks fine. One assertion.

**2. Regenerating the registries produces no diff.**
`python3 generate-registries.py <graph>` rewrites `skill-registry.txt`,
`misconception-registry.txt` and `external-prereq-registry.txt`. CI regenerates and fails on
a non-empty diff. This is your byte-identical-manifest pattern, and it is what makes a
generation stamp true rather than aspirational — a hand edit to a generated file becomes a
red build instead of a stale stamp. That exact failure happened here: `skill-registry.txt`
hand-edited and stamped `v0.11.3` while carrying `v0.12.4` content, and you caught it by
reading the artifact rather than the letter claiming it.

*Note:* `chain-registry.txt` is **excluded** and carries no stamp. Its display titles are
authored prose with no source in the graph, so it is genuinely not derivable.

**3. `partition-check.py` passes.**
Fails when the prose restates a threshold that `activity_defaults` declares (D25). Already
written, already clean at v0.13.0, currently gated by nothing.

**4. Referential integrity.**
Every id in a registry exists in the graph; no dangling prereq or misconception reference; no
misconception attached to no skill; the chunking plan's skill set matches the graph's. All
currently verified ad hoc. Worth adding: the declared parts total in `skill-registry.txt`
equals the sum of `parts` over the graph's skills — it is 51 today, and it is the denominator
your burndown reads.

---

## 2. What goes in

The curriculum **scaffolding**, not the catalogue. Activity `.md` files stay where they are;
this is the thing they are authored against.

```
thread-01-rate-of-change.json     the graph — skills, edges, misconceptions,
                                  activity_defaults, chunking_plan, capabilities
authoring-principles.md           byte-identical to the graph's authoring_principles
decision-log.md                   D1–D30
open-questions.md                 what is unresolved, and who decides
chain-hooks.md                    the hook holding pen
misconception-proposals-*.md      the reasoning behind ratified ids
skill-registry.txt                generated
misconception-registry.txt        generated
external-prereq-registry.txt      generated
chain-registry.txt                hand-maintained, no stamp
generate-registries.py            produces the three, with a notation gate
partition-check.py                gates check 3
pair-attachment-report.py         your script, runs here because it reads the graph
```

---

## 3. What we need back

A stamp we can put on the boundary page, in the shape yours already uses:

> **Canonical:** `<raw URL>` · **Generation stamp:** commit `<sha>`, `<timestamp>` · sha256
> `<hash>` · **Currency guarantee:** the four checks above fail CI on drift, so the copy on
> `main` is current by construction.

That is what converts our rows from claims into pointers, and it is the whole point of the
exercise.

---

## 4. The decision that is not ours

**Public or private.** Yours is public, which is what makes your pointer clean — a raw URL,
no auth, no token to expire. If ours is private, "fetchable" becomes "fetchable if
credentials are current," which is a weaker property and a new failure mode of exactly the
kind this channel exists to remove.

The honest read on the content: the graph is a skill DAG and a misconception taxonomy. It is
genuinely valuable, but the commercial asset is the activities, and none of them are in it.
The recommendation from this side is **public, for the same reason yours is**. It is an IP
call rather than a technical one, so it is not ours to make.

**If it must be private**, the fallback is publishing only the registries and the principles.
Accepted cost, stated plainly: you can then verify neither the generation nor the byte
identity, because you cannot see the source. Checks 1 and 2 would still run in CI — you
would just be trusting the report rather than able to reproduce it.

---

## 5. Ownership and timing

**Yours to build.** It is infra and it touches CI, and the rule both sides have been applying
says the side that can regenerate a thing owns its pipeline. What we owe is this list of
guarantees; what you owe back is §3.

**Before chain 2 rather than after.** Every chain adds hooks, ids and activities — more
surface, and the byte-identity risk compounds with each session that has to remember to
check. The four activities that exist now make this the cheapest it will be, which is the
same argument that made the contract work worth doing in the first place.

---

## 6. One thing to push back on if you disagree

Check 1 is the one worth arguing about, because there is a real alternative: **stop storing
the prose twice.** Keep `authoring-principles.md` as the only copy and have the drafting
prompt read it, rather than keeping a byte-identical field inside the graph.

We are not proposing that, because the graph is what a drafting session loads and a second
fetch is a second failure point. But if you see a way to make the `.md` the single source
without adding one, that removes check 1 entirely rather than automating it — which is
strictly better, and is the same move as putting `parts` into the graph so
`skill-registry.txt` could be generated at all.
