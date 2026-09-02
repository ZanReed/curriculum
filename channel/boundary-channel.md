# The boundary channel

Coordination with the activity-platform side runs on **two one-way Notion pages**, not on
correspondence and not on a shared page.

| page | written by | read by |
|---|---|---|
| [Curriculum → Platform boundary](https://app.notion.com/p/3ceb20a1fdd2814aa7ecfb269ffd44c8) | curriculum | platform |
| [Platform → Curriculum boundary](https://app.notion.com/p/3ceb20a1fdd28183a9afcc7e19d905c1) | platform | curriculum |

**Never edit the other side's page.** Two one-way pages rather than one shared page removes
the "who owns this row" problem structurally instead of by convention — the same move as
*one column, one meaning, one writer*, applied to the coordination surface.

**This file is not a copy of either page.** It holds the two URLs and the rules and nothing
else. A local mirror of the pages' contents would be exactly the hand-maintained duplicate
the channel exists to end, and it has been caught five times across the two systems.

## What may never go on either page

Any count, any rule text or threshold, any reasoning behind a decision, any import or format
fact. Those live in the graph, `authoring_principles`, `decision-log.md` and the platform's
generated format doc. **A cell that could disagree with an artifact does not belong on the
page.** Every row is a pointer.

## The closing rule the channel runs on

> **An item is not closed until the artifact contains the change. Close it by quoting the
> artifact, not by describing it.**

Two independent derivations, which is why it is worth stating rather than assuming: this side
reached it from `open-questions.md` recording §15 as amended for months while the amendment
had never been written; the platform reached it from a registry declaring `numbered` for four
months while nothing rendered it. Their wording is *a guard must bind to output, not to a
declaration.*

## The known asymmetry

The platform's pointer rows carry a public URL, a commit stamp, a sha256, and CI that fails on
drift. **Ours cannot.** The curriculum artifacts live in a Claude project, so our rows name a
canonical artifact without linking one, and the platform cannot verify a stamp or fetch a
current copy.

Until the curriculum artifacts sit in a repo the platform can fetch, treat our rows as claims
from this side rather than as verifiable pointers. That is stated on our page too, so nobody
reads the two as equally strong.

## What the platform's page currently supplies

A pointer to `docs/catalogue-authoring-prompt.md` — **generated** by `pnpm prompt:catalogue`
with CI failing on drift between source and doc, so it is current by construction rather than
by discipline. That is the contract for catalogue files.

⚠ It is **not** `docs/markdown-import-format.md`, which is hand-maintained and does not carry
the catalogue-only keys (`key:`, `skill:`, `supporting_skills:`, `chain_role:`, the ignored
`x_` namespace). Author against the generated doc, never against a saved copy or a
decision-log description of it.
