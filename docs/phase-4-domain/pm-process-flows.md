# pm-process-flows

> User Types + Process Maps + User Flows - the E2E design bridge between domain registers and per-feature specs

**Phase:** 4-5 bridge (into design)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** process map, process flow, user flow, user types, system actors, user journey, screen flow, designer brief, swimlane, e2e process

---

## When to use

Phase 4-5 bridge. After entity registry and before (or in parallel with) Phase 5 feature planning. Produces the E2E big picture across a module - the view that per-feature JIT design (`pm-feature-design`) then refines at the individual feature level.

Re-runnable per domain/module. Recommended to run per module rather than for the whole product at once.

---

## What it produces

Three artifacts under `process-flows/`:

1. **User Types** (`user_types.md`) - system actor catalogue: who interacts with the system (Admin, Courier, Dispatcher, Customer, System, etc.), their role, permissions scope, entry points
2. **Process Maps** (`[domain]_process_map.md`) - end-to-end business process per domain area: steps, decision points, triggers, outcomes. For dev + design understanding. References entity states by name - does NOT restate state machines.
3. **User Flows** (`[domain]_user_flows.md`) - per-user-type E2E journey with screen touchpoints and UI behavior: how each user type moves through the process, what screens they see, what actions they take, what the system responds with. This is the designer brief.

---

## How to invoke

```bash
/pm-process-flows           # interactive - asks scope (whole product or one module)
/pm-process-flows --agent   # autonomous synthesis from domain model and feature list
```

Scope is asked at Step 0. Recommended: run per module (one domain at a time), re-run when new features or entities are added.

---

## Key design rules

- Process maps and user flows **reference** entity states and business rule IDs by name - they do NOT restate state machines or attribute lists (those live in `entities.md` and `business_rules.md`)
- If a state changes, change it once in the register - not across diagrams
- User flows show screen touchpoints and UI behavior for the designer; they do not define the visual design
- User type identification is adaptive: Claude analyses existing docs, proposes actors, asks for confirmation before mapping flows

---

## What this skill does NOT do

- Draw wireframes or screens - that is the designer's work (Figma, Excalidraw)
- Define business rules - those are in `business_rules.md`; flows reference BR-IDs where a rule gates a step
- Replace per-feature UX context in `pm-feature-design` - that is atomic, per-feature; this gives the cross-feature big picture

---

## Dependencies

**Strongly recommended (none strictly required - skill adapts to what exists):**
- `pm-entity-registry` - entities and states the processes act on (referenced by name)
- `pm-personas` - market personas map onto system user types
- `pm-features-list` - features composing each process
- `pm-domain-model` - domain boundaries scoping each process map

**Produces for:**
- `pm-feature-design` - Section 3b UX context draws on the relevant user flow
- Designers (Figma, impeccable) - user flow output (`[domain]_user_flows.md`) is the screen design brief

**Related skills:** `pm-personas`, `pm-entity-registry`, `pm-features-list`, `pm-feature-design`, `pm-diagrams`
