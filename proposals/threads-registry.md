# `threads` registry: proposed ids and labels (D39 migration input)

`status: approved by Zan 30 Sep 2026` (ids and labels). Released by Zan 1 Oct for the D39 migration, which follows the `chain.linear.slope` hook pool. Written 29 Sep 2026 against D39 as pasted from `decision-log-additions.md:714`
at `f1faa07`. D39 sets the registry's shape (id and label per thread) and names no ids.
This draft proposes them, for approval before the migration commit touches the JSON.

## Proposed registry

```json
"threads": [
  { "id": "thread.rate-of-change",       "label": "Rate of change" },
  { "id": "thread.number-proportion",    "label": "Number and proportion" },
  { "id": "thread.algebra-equations",    "label": "Algebraic manipulation and equations" },
  { "id": "thread.measurement",          "label": "Measurement" },
  { "id": "thread.geometry-trig",        "label": "Geometry and trigonometry" },
  { "id": "thread.statistical-enquiry",  "label": "Statistical enquiry" },
  { "id": "thread.probability",          "label": "Probability" },
  { "id": "thread.senior-calculus",      "label": "Senior calculus beyond the derivative" }
]
```

| § 5 # | id | years (§5) | strands |
|---|---|---|---|
| 01 | `thread.rate-of-change` | Y8–13 | Algebra, Calculus |
| 02 | `thread.number-proportion` | Y7–11 | Number |
| 03 | `thread.algebra-equations` | Y7–12 | Algebra |
| 04 | `thread.measurement` | Y7–11 | Measurement |
| 05 | `thread.geometry-trig` | Y7–13 | Geometry |
| 06 | `thread.statistical-enquiry` | Y7–13 | Statistics |
| 07 | `thread.probability` | Y7–13 | Probability |
| 08 | `thread.senior-calculus` | Y12–13 | Calculus |

## Choices made

- **`thread.rate-of-change` is kept as it is.** It is the current top-level `thread_id`,
  which D39 retires. Reusing the value as the first registry id means the migration is a move,
  not a rename, and nothing that already quotes it goes stale.
- **No numbers in ids.** "Thread 05" is §5's ordering, and the ordering is a proposal. Ids
  that carry a number would assert an order the registry doesn't hold. The numbers stay
  in prose and in this table only.
- **Ids name content, not year span.** Year ranges move (D36 moved `deriv.*`; D37 deferred
  most of the senior end), so none of the ids say "senior" except thread 08. Thread 08 is
  senior by definition.
- **Labels follow §5 verbatim.** Thread 01 is "Rate of change". The graph's current
  `label`, `Linear → Function → Transformation → Rate of Change → Derivative`, describes
  the chain sequence rather than naming the thread, so it doesn't move into the registry.
  "Rate of change" is the thread's spine: gradient is a constant rate, and the derivative
  is an instantaneous one. Functions and transformations are what carry it between those
  two points. It also matches the id, and it's the same length as the other labels.

## Things this doesn't settle

- **Thread 08 under D37.** Its L3 content is deferred, but the Y12 anti-differentiation
  chain (AS91262) isn't. The thread is registered now, and its deferred chains carry
  `status: deferred` as D37 describes.
- ~~Where `chain.pattern.linear` goes~~ **Ruled 30 Sep:** `thread.algebra-equations`,
  following the NZ curriculum. `thread.rate-of-change` starts at Y8.
- **§5's chain/skill/activity estimates for thread 01 predate D36** (limit collapse,
  function trim). Only the thread list is used here, not the counts.
