# Playbook 1: Greenfield

Build a new product from scratch - from first idea to launch. Full discovery, validation, and JIT delivery.

**Use when:** new product, zero users, need to validate PMF before building.

---

## How to read this page

This is a **route map** - which phase comes next, when a whole phase can be skipped, and what unlocks the next one. Each phase links to its own runbook page with the per-skill detail (when to run/skip each skill, what you get, what it doesn't).

---

## Phase overview

```
Phase 1       Phase 2       Phase 3a      Phase 3b       Phase 4        Phase 5       Phase 6+7
Foundation →  Discovery  →  Validation →  Commercial  →  Domain      →  Feature    →  JIT Delivery
                            ┃GO gate┃     Definition     + Registers    Planning      (per feature)
                            ┗━hard━━┛
```

---

## Express path (skip discovery/validation)

- **When to use:** you already have a validated idea, know exactly what to build, and don't need discovery or market/customer validation.
- **Skips:** Phase 1, 2, 3a, 3b entirely.
- **Never skips:** domain registers and a feature list with FEAT-IDs - `pm-feature-design` cannot run without them.

```bash
/pureinn [idea]                  # workspace setup, 3 intake questions
/pm-entity-registry              # entity list + key states only (lean mode)
/pm-business-rules-library       # core rules in Draft
/pm-features-list                # feature inventory + FEAT-IDs + KANO + V×C
/pm-mvp-scope                    # MVP scope + Delivery Stripe assignment
/pm-feature-design [FEAT-ID]     # → JIT delivery engine
```

**Done when:** the first feature enters `pm-feature-design`. From there you're in the same JIT cycle as the full path.

---

## Full flow

| Phase | Enter when | What happens | Detail |
|---|---|---|---|
| **1 - Foundation** | Start of every Greenfield project | Scope, team, stakeholders defined - scales down to nothing for solo builders | [Phase 1](phase-1-foundation/index.md) |
| **2 - Discovery** | Phase 1 artifacts exist (or `/pureinn discover`) | 4 parallel tracks (Tech, Domain, Market, Customer) converge into a Problem Validation Summary | [Phase 2](phase-2-discovery/index.md) |
| **3a - Validation** | Problem Validation Summary exists (can start in parallel with late Phase 2) | Real-world experiments → **hard GO/PIVOT/STOP gate** | [Phase 3a](phase-3a-validation/index.md) |
| **3b - Commercial Definition** | Phase 3a GO verdict (no workaround) | Business model, KPIs, business case, PRD - **PRD frozen at exit** | [Phase 3b](phase-3b-definition/index.md) |
| **Pre-Phase 6 - Technical Foundation** | PRD frozen | `/common-ground` (fullstack-dev-skills) - tech stack decision, repo structure, `COMMON-GROUND.md` | - |
| **4 - Domain Modeling** | Technical Foundation done | Live Registers (entities, rules, decision tables) initialized in Draft | [Phase 4](phase-4-domain/index.md) |
| **5 - Feature Planning** | Registers initialized | Feature inventory, prioritization, MVP scope, Delivery Stripes | [Phase 5](phase-5-planning/index.md) |
| **6+7 - JIT Delivery** | Features assigned to Stripes | Per feature, just before build: spec → design inspection → build → review → ship | [Phase 6+7](phase-6-build/index.md) |

---

## Key rules

- **Phase 3a is a hard gate.** Only GO advances. PIVOT loops back to targeted re-validation. STOP ends the project. No FORCE bypass.
- **Phase 3b requires Phase 3a GO.** Cannot be entered without a GO verdict - there is no workaround.
- **PRD is frozen** after Phase 3b. No scope changes without a formal change request tracked in the PRD changelog.
- **Spec gate before build** (Phase 6, hard gate). Feature Card Sections 1-3 complete + Design Inspection passed before any feature enters code.
