---
name: pm-process-flows
description: Identifies the system's user types (actors) and maps end-to-end processes - both a lean business process map per domain (for dev + design understanding) and per-user-type user flows connected to screens (a designer brief). User-type identification is adaptive - analyse the docs, confirm with the user, ask if unsure, or propose from context. Process maps reference entity states by name and do NOT duplicate them (low-maintenance). Phase 4-5 bridge into design; feeds pm-feature-design's UX context and the designer (impeccable / Figma).
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: process map, process flow, user flow, user types, system actors, user journey, screen flow, designer brief, swimlane, e2e process
  role: specialist
  scope: design
  output-format: document
  related-skills: pm-personas, pm-entity-registry, pm-features-list, pm-feature-design, pm-diagrams
---

# PM - Process Flows (User Types + Process Maps + User Flows)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Two connected outputs that bridge the domain model into design:

1. **System user types** - the actors/roles in the system (e.g. Admin, Courier, Dispatcher, Customer, System). Identified **adaptively**.
2. **Flows** - two views built on those user types:
   - **2A. Process map per domain / process area** - the end-to-end business process, for dev + design understanding.
   - **2B. User flows per user type, connected to screens** - how each user moves through the processes E2E, with screen touchpoints and UI behaviour, so a designer can complete the screen design from the user's perspective.

This sits between the domain registers and per-feature design. `pm-feature-design`'s per-feature UX context (Section 3b) is atomic; this gives the **E2E big picture** across a module that the per-feature view then refines.

**Lean by design (low maintenance):** process maps and flows reference entity states and attributes **by name** - they do NOT restate state machines or attribute lists (those live in `entities.md`). If a state changes, you change it once in the register, not across a dozen diagrams. This skill is a **business + UX view**, not a second copy of the domain.

**Adaptive (per the Adaptive-execution standard in CLAUDE.md):** runs with whatever exists (personas? domain? features?), is re-runnable per module, and offers rather than imposes.

**Produces:**
- `process-flows/user_types.md` - the system actor catalogue
- `process-flows/[domain]_process_map.md` - the 2A business process map per domain
- `process-flows/[domain]_user_flows.md` - the 2B per-user screen-connected flows

---

## What this skill does NOT do

- Restate entity states, transitions, or attributes - it references them by name (those are in `entities.md`)
- Draw the actual screens / wireframes - that is the designer's job (impeccable / Figma). It produces the flow + screen touchpoints + UI behaviour brief that the designer draws from.
- Define business rules - those are in `business_rules.md`; flows reference BR-IDs where a rule gates a step

---

## Dependencies

**Strengthens the result if present (none are hard-required - the skill adapts):**
- `pm-personas` - market personas map onto system user types
- `pm-entity-registry` (`entities.md`) - entities/states the processes act on (referenced by name)
- `pm-features-list` - features that compose each process
- `pm-domain-model` - domain boundaries that scope each process map

**Feeds:**
- `pm-feature-design` - Section 3b UX context draws on the relevant user flow
- The designer (impeccable / Figma) - 2B is the screen-design brief

---

## Step 0: Current state check

Detect what exists: `process-flows/` artifacts? `entities.md` / personas / `feature_list.md`? Which domains/modules are defined? Show a short state table.

Ask scope: whole product, or one domain/module first (recommended - run per module, re-runnable).

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Identify system user types (adaptive)

This is a proactive-partner step, not a passive question:

```
1. ANALYSE - scan provided docs / context for clearly defined user types
             (e.g. "admin, courier, dispatcher").
        │
   ┌────┴───────────────┬──────────────────────┐
   ▼                    ▼                       ▼
 Found                Found but                None found
   │                  look wrong/partial         │
   ▼                    ▼                       ▼
 Confirm with         Ask the user             Ask: do you have
 the user they         to confirm/correct       user types defined?
 are correct + complete                          │
                                          ┌──────┴──────┐
                                          ▼             ▼
                                       User has      User has nothing
                                       → capture     → PROPOSE: extract
                                                       candidate types from
                                                       context (domain, features,
                                                       personas) + reasoning,
                                                       confirm via AskUserQuestion
```

Never stall on missing input - if the user has nothing, propose. Use AskUserQuestion to confirm the final set.

### OUTPUT: `process-flows/user_types.md`

```markdown
# System User Types - [Product Name]
> Source: [docs / confirmed with user / proposed from context]

## [User Type / Role name] (e.g. Courier)
**Description:** [who they are in the system - one line]
**Primary goals in the system:** [what they are trying to accomplish]
**Modules touched:** [Domain / module names]
**Maps to persona:** [persona name from pm-personas, or "N/A"]

[repeat per type]
```

---

## Choosing the diagram type (adaptive - applies to Steps 2 and 3)

Do not default to one diagram blindly. For each flow, **look at its character, identify the best-fit type, and offer it via AskUserQuestion with a recommendation and the reason** (per the Adaptive-execution standard). Mermaid renders all of these in UML-style notation.

| If the flow is... | Best-fit diagram | UML equivalent |
|---|---|---|
| Steps + decisions, mostly one actor | `flowchart` | Activity diagram |
| One process across several actors | `flowchart` with **swimlanes** (subgraphs per actor) | Activity + swimlanes |
| Interaction user ↔ system ↔ external over time | `sequenceDiagram` | Sequence diagram |
| A user moving screen-to-screen (2B) | `flowchart` (screens = nodes, actions = edges) | Activity / navigation map |

**Never draw an entity state machine here** - it is UML state-diagram territory that lives in `entities.md`. Reference it by name (lean / DRY).

Offer pattern: "This process spans 3 actors with hand-offs - I recommend a **swimlane** (clearest for who-does-what). Use that, a sequence diagram (if the system↔external timing matters more), or a plain flowchart?" - recommended option first, with the why.

**Rendering / editing:** Mermaid inline is the default (renders everywhere). For a richer or exportable/editable diagram, hand off to `/pm-diagrams`, or the Mermaid / Excalidraw MCP if connected.

---

## Step 2: Process map per domain (2A - business view)

For each domain / process area in scope, the **end-to-end business process** - lean, no state/attribute detail.

Every process map covers: **happy path, alternate path(s), edge cases, constraints.**

### OUTPUT: `process-flows/[domain]_process_map.md`

```markdown
# Process Map - [Domain / Process Area]
> Business + dev/design support view. References entities/rules by name - no state/attribute detail (see entities.md / business_rules.md).

## Process: [Process name] (e.g. Deliver a parcel)
**Actors involved:** [user types]
**Entities involved (by name):** [Order, Parcel - see entities.md]
**Rules that gate this process:** [BR-IDs, if any]

### Happy path
1. [Step - business action, who does it]
2. ...

### Alternate paths
- [Branch: condition → alternate sequence]

### Edge cases
- [Unusual / failure case → how the process handles it]

### Constraints
- [Time windows, prerequisites, regulatory, capacity...]

### Diagram
```mermaid
flowchart TD
    %% or swimlane for cross-actor process
```
```

Pick the diagram type per "Choosing the diagram type" above - offer it with a recommendation (swimlane for multi-actor, sequence diagram when system↔external timing dominates, plain flowchart for single-actor).

---

## Step 3: User flows per user type, connected to screens (2B - designer brief)

For each user type, **how they move through the processes E2E, mapped to screens** - so the designer can complete the screen design from the user's perspective.

Every user flow covers: **happy path, alternate path(s), edge cases, constraints** - PLUS, per step: the user's action, the system/UI response, the screen, and explicit **Loading & Empty states**.

### OUTPUT: `process-flows/[domain]_user_flows.md`

```markdown
# User Flows - [Domain / Module]

## [User Type] - [Flow name] (e.g. Courier - Accept and deliver a job)
**Goal:** [what the user is trying to do]
**Entry point:** [screen / trigger]

### Happy path (step → screen → UI behaviour)
| Step | User action | Screen / element | System & UI response |
|---|---|---|---|
| 1 | [taps "Available jobs"] | Jobs list screen | loading spinner → list renders; empty state if none |
| 2 | [taps a job] | Job detail screen | shows route map; CTA "Accept" |
| 3 | [taps "Accept"] | Job detail | optimistic update → toast "Accepted"; error state if taken |

### Alternate paths
- [Branch: condition → alternate screens/steps]

### Edge cases
- [e.g. job taken by someone else mid-flow → error state + return to list]

### Constraints
- [e.g. cannot accept a 2nd job while one is active]

### Loading & Empty states
- **Loading:** [where spinners/skeletons appear]
- **Empty:** [no jobs / no history → what the screen shows + CTA]
- **Error:** [network / conflict → message + recovery action]

### Diagram
```mermaid
flowchart TD
    %% user flow: screens as nodes, actions as edges
```

> Screen-level wireframes are out of scope here - hand this brief to the designer (impeccable / Figma). Flag any screen needing a dedicated detail diagram.
```

---

## Step 4: Coverage cross-check (before saving)

Two quick reconciliations that catch the classic gaps:

1. **Every process step has an owner.** Walk each 2A process map: every step names a user type (or System) as its actor. A step nobody owns is either automated (name System explicitly) or a hole in the process - ask, don't guess.
2. **Every user-type goal has a flow.** Walk `user_types.md`: each "primary goal in the system" is served by at least one 2B flow. A goal with no flow means either the goal is wrong or a flow is missing - surface it. (The reverse also matters: a flow serving no stated goal is a scope-creep signal.)

Report both checks in one line each before saving ("All steps owned / step X in [process] has no actor").

---

## Save to

```
pureinn-workspace/[project-slug]/process-flows/user_types.md
pureinn-workspace/[project-slug]/process-flows/[domain]_process_map.md      (2A, per domain)
pureinn-workspace/[project-slug]/process-flows/[domain]_user_flows.md       (2B, per domain)
```

References only - never copy state machines or attribute lists from `entities.md`.

---

## Handoff

**Čo si teraz má:** Katalóg systémových typov používateľov + E2E procesnú mapu (business) + user flows napojené na obrazovky (designer brief) - všetko happy/alternate/edge/constraints, a 2B navyše s UI response a loading/empty states. Lean - stavy a atribúty len po mene, nízka údržba.

**Ďalší krok:**
- Dizajnér: `process-flows/[domain]_user_flows.md` je brief na kreslenie obrazoviek (impeccable / Figma).
- `/pm-feature-design [FEAT-ID]` — UX kontext (Section 3b) čerpá z príslušného user flow.

**Môžeš preskočiť ak:** Modul je čisto backend/API bez používateľského toku a obrazoviek - vtedy 2B nepridáva hodnotu (procesnú mapu 2A môžeš spraviť aj tak).
