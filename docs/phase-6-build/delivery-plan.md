# The Delivery Plan

The answer to two questions no other artifact gave you: **"what do we build next?"** and **"what can run in parallel right now?"** - across all delivery stripes, in one place. Computed and rendered by [pm-stripe](pm-stripe.md).

---

## How to read this page

This is a **runbook + use-case reference**. The first half is how the plan works and what you get; the second half is concrete situations ("I want to reorder", "why is my P1 blocked", "we're onboarding an existing product") with exactly what you do and what you see.

---

## The problem it solves

You have a feature inventory with all the fields - dependencies, stripe, priority, KANO, V×C, phase, status. A developer asks *"what's the build order, and what can we work on in parallel?"* and nobody can answer from the docs, because the data is scattered across four places (dependency map, per-stripe sequencing, priority order, live status) and no view combines them. Teams end up pasting it into an external AI tool to get a sequence nobody trusts.

The Delivery Plan combines them into one **derived** view - computed on demand from the current state, never a hand-maintained document. Your single source of truth stays `feature_list.md` + Feature Cards.

---

## How it works (the short version)

It is a **Resource-Constrained Project Scheduling Problem**: one global dependency DAG, each stripe is a resource of capacity 1, and shared code is a mutex. A single scheduling pass evaluates, in order:

1. **Drop shipped** features; their dependents are unblocked.
2. **Cycle check** - a broken dependency chain stops the plan (needs a human).
3. **Occupancy** - a stripe is busy when someone is **actively** working it. The authority is `active_feature` (the schedule axis); status (`4_In_Build`/`5_In_Review`) is only a fallback when `active_feature` is unset. This matters on a Rebuild, where those statuses come from *code state*, not active work - reading status-first would falsely lock nearly every lane.
4. For each dependency-ready feature, sort **override** (break-glass) → **phase** (earlier phase gates order - a later-phase feature never precedes a current-phase one in the same wave) → **priority** (P1>P2>P3) → FEAT-ID, then assign against **capacity** (lane free?) → **contention** (`mutex_tags` overlap with an active feature?). A per-stripe **WIP-limit warning** fires if more than one feature shows active.

**KANO and V×C are not used here** - they decided *phase* (what's in the MVP) upstream in `pm-features-list`/`pm-mvp-scope`. Phase is now the top content gate in the sort; the rest of the order is driven by dependencies, capacity, contention, and priority.

> **Two independent axes (critical for Rebuild).** `status` = **code reality** (what the code actually is); plan order + `active_feature` = **the schedule** (what we work on next). Never reset `status` to serve planning, never infer active work purely from `status`. A Rebuild legitimately lands a feature at `4_In_Build` meaning "code half-built, nobody touching it" - occupancy comes from `active_feature`. This is why the framework needs **no new lifecycle state** for inherited-partial builds.

### Three constraints, not one

| Constraint | Meaning |
|---|---|
| **Dependency** (hard, cross-stripe) | X must ship before Y if Y needs it |
| **Capacity** (per-stripe) | a stripe builds one feature at a time; occupancy is whoever is `active_feature` (falls back to `In_Build`/`In_Review` status only when unset) |
| **Code contention** (`mutex_tags`) | two features touching the same module can't run in parallel - even across stripes - because AI agents on separate branches will collide |

---

## What you get - two renders, one computation

**NOW** (default, daily driver):

```
DELIVERY PLAN — Acme           recomputed 2026-07-23 · 12 shipped / 38 remaining
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▶ BUILDABLE NOW (parallel across stripes):
   stripe-tenant    FEAT-TNT-006  Producer role management (P1)
                    ✓ Ready: deps met · lane free · no contention
   stripe-billing   FEAT-BIL-003  Invoice PDF export (P2)
                    ✓ Ready: deps met · lane free · no contention
⛔ BLOCKED (why):
   stripe-tenant    FEAT-TNT-007  Bulk invite
                    Contention: waiting for FEAT-TNT-006 to release 'InviteService'
   stripe-payment   FEAT-PAY-002  Refund flow
                    Dependency: waiting for FEAT-BIL-003 to ship (Context: needs invoice ref)
```

**FULL** (plan birth, pre-development walkthrough) additionally shows each stripe's full ordered queue, the parallel **waves**, the cross-stripe sync points, and a Mermaid swimlane (stripe = lane, arrows = dependencies).

> **Contention confidence.** The `⚠ projected parallelism - contention unknown until JIT design` marker is **data-driven, not playbook-driven**: a wave gets it iff its features actually have empty `mutex_tags`, applied identically everywhere. On a fresh greenfield plan the far waves have none yet (tags fill at JIT design), so they're marked. A Rebuild carries no marker **only if extraction populated the tags** - `pm-reverse-extract` extracts them from real code, but a `pm-reconcile` that skipped tagging lands with empty tags, so that plan is as contention-blind as greenfield and its waves get the marker too. This never affects the **Buildable now** answer: a feature must pass the spec gate (and therefore carry `mutex_tags`) before it can enter build. Tags are never guessed ahead of design - a wrong tag creates a false block, which costs more than an optimistic projection.

Both are also written to **`delivery_plan.md`** in the repo root, so your AI coding agent can read it: *"Based on delivery_plan.md, what should I build next in stripe-tenant?"*

---

## Lifecycle

### 1. Birth - the first full plan

The plan is born the first time you run `/pm-stripe` once the feature list carries statuses:

| Playbook | Born after | Starting state |
|---|---|---|
| Greenfield / Feature Implementation | `pm-mvp-scope` | everything `1_Backlog` → FULL plan is the whole forward sequence |
| Rebuild | `pm-reverse-extract` / `pm-reconcile` | mixed statuses from code → FULL plan is Shipped history + inherited-partial lanes + forward frontier. A one-time **WIP question** runs before occupancy ("of the features at `4_In_Build`/`5_In_Review`, how many is someone actually working on now?") to separate real WIP from code-state artifacts; the answer is written to `active_feature`. A Rebuild need not land mostly-shipped - a stricter definition of done can leave it with little Shipped and many inherited-partial lanes. |

### 2. Daily loop

```
Open delivery_plan.md (or /pm-stripe)
  → your stripe shows one Ready feature → build it (point your AI agent at it)
  → other stripes' Ready features → safe parallel work
  → ship (PR merge) → /pm-stripe recomputes:
        shipped → Shipped, next feature → Ready, dependents unblock, plan_order rewritten
```

### 3. Intervention - always via the source

You never edit `delivery_plan.md` or `plan_order`. You edit the source and recompute. Every change carries a reason into the rationale.

---

## Use cases

### UC-1 · Developer: "what do I build next?"

Open `delivery_plan.md`, find your stripe's lane. The top **Ready** feature is your next build. If it's blocked, the rationale line names exactly who you're waiting on. No meeting, no Slack thread.

### UC-2 · Lead: "what can run in parallel right now?"

The **Buildable now** block is the answer - every listed feature is dependency-clear, lane-free, and code-disjoint from the others. Assign one per person/agent. The swimlane (FULL render) shows the whole parallel picture and where lanes must synchronize.

### UC-3 · "Why is my P1 still blocked?"

Read its rationale line. Examples:
- `Dependency: waiting for FEAT-BIL-003 to ship (Context: needs invoice ref)` → follow the arrow.
- `Contention: waiting for FEAT-TNT-006 to release 'InviteService'` → the code overlap is real; wait, or split the work.
- If the block is wrong (e.g. the mutex tag is stale because your agent no longer touches that module), fix the source `mutex_tags`, recompute, and it pops into Ready. **The system self-corrects through use.**

### UC-4 · "I want to change the order / priority"

Edit in **one place per cycle**, then run `/pm-stripe`:
- In the repo: change `priority` in the Feature Card / `feature_list.md`, or add a soft `dependency: {id, reason}`.
- In Notion: change the Priority property.
- `/pm-stripe` reconciles (a Notion change is pulled into the repo like status), recomputes, and writes `plan_order`/`wave` back so Notion re-sorts. Rule: don't edit the same field in both places between syncs; never drag rows in Notion (overwritten).

### UC-5 · Break-glass: a P0 bug must jump the queue

Set `override: {reason: "prod outage - refunds failing"}` on the feature, run `/pm-stripe`. It preempts capacity, priority, and contention and shows loudly: `🔴 BREAK-GLASS P0: prod outage - refunds failing`. It cannot bypass a *hard* dependency (you can't build on code that doesn't exist) - but a P0 fix is almost always on shipped code, so it just jumps the lane. Board integrity holds: everything else computes normally around it.

### UC-6 · Rebuild: onboarding an existing product

Lots of code, features at mixed statuses. After `pm-reverse-extract`, the first `/pm-stripe` runs the one-time **WIP question** (real in-progress work vs code-state statuses), then produces a FULL plan of **Shipped** history, **inherited-partial** lanes, and a **forward frontier**. `mutex_tags` are accurate from day one **only if extraction populated them** - `pm-reverse-extract` extracts them from real code (sharper than a greenfield first plan); a `pm-reconcile` that skipped tagging leaves the contention dimension blind, and those waves are honestly marked `⚠ projected parallelism`. For a team walkthrough, the FULL render can add an **"exists in code"** column (from each card's Evidence) so you go feature by feature and decide: **code-review + tests** (looks done) / **finish coding** (partial) / **from scratch** (stub) - optionally recorded as `entry_mode` on the card. This is where the plan is most valuable: the history is complex and nobody could answer "given all this, what's next" without it.

### UC-7 · Keeping order stable in Notion

Notion has no inherent row order and reshuffles on sync. The plan writes a derived `plan_order` (global sort index) and `wave` (parallelism level) to each Notion row. Set the Notion view to sort by `plan_order`, group by `stripe` - it now shows the computed order and stays stable. These fields are auto-written; editing them by hand does nothing (overwritten next recompute).

### UC-8 · Seeing the plan visually

Beyond the text render, pm-stripe can materialize `delivery_plan.html` - a self-contained interactive page, zero build step, zero external dependency. Collapsible per-stripe Kanban lanes (chip-summary until clicked open), a relative Timeline (S/M/L estimates, no faked dates, overlapping bars pack into stacked rows), a wave-column Dependency graph, and a Kano distribution - with click-for-detail on every card/bar/node. It started as a hand-built prototype on a real project and earned a permanent framework slot because it's genuinely useful, not a demo.

Offered once (Recommended); the CSS/JS engine is copied byte-for-byte from `references/delivery-plan-companion.html` every run - only the content and feature data regenerate, so it never drifts or gets hand-tweaked into inconsistency. The critical path is computed once - longest chain by dependency edges only, never lane-serialized - and shared with the text render and every section of the page, using one fixed color mapping (coral = critical path, amber = part-built, blue = needs review, grey = not started, green = shipped). Choice persists in `state.json` (`delivery_html`); not pushed to Notion (interactive JS doesn't survive there) - lives in the repo, linked from `delivery_plan.md`.

A lighter alternative remains available: static Mermaid via [pm-diagrams](pm-diagrams.md) `kanban` / `gantt` (relative mode) / `dependency` / `kano`, embedded in markdown - useful for dropping a single diagram into a Feature Card or written doc, but not collapsible or clickable.

---

## Fields (source vs derived)

| Field | Who sets it | Role |
|---|---|---|
| `dependencies` | pm-features-list / you (`{id, reason}`) | hard/soft precedence |
| `stripe`, `phase`, `priority` | pm-mvp-scope / you | lane, MVP membership, tie-break |
| `mutex_tags` | pm-feature-design (JIT) / pm-reverse-extract (code, standalone + reconciled mode) | code-contention footprint - empty tags → wave marked `⚠ projected parallelism` |
| `active_feature` | you / the schedule (per stripe in `state.json`) | occupancy authority - who is actively on the lane (empty = free, even at `4_In_Build`) |
| `override` | you (break-glass) | force a P0 past capacity/priority/contention |
| `plan_order`, `wave` | **the computation** | derived sort index + parallelism level - never hand-edit |

---

## The one rule

**The plan is derived. To change it, change the source, then recompute.** Never hand-edit `delivery_plan.md`, `plan_order`, or `wave`; never reorder rows in Notion. Everything you want the plan to say is expressed as `priority`, `dependencies`, `mutex_tags`, or `override` - and every one of those carries its reason into the rationale, so the order always explains itself.

---

*Computed by [pm-stripe](pm-stripe.md). Born at [Phase 5](../phase-5-planning/index.md) exit (or rebuild extract), driven through [Phase 6+7](index.md).*
