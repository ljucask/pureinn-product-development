# Playbook 1: Greenfield

Build a new product from scratch - from first idea to launch. Full discovery, validation, and JIT delivery.

**Use when:** new product, zero users, need to validate PMF before building.

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

**Trigger:** validated idea, you know what to build, no discovery needed.

```bash
/pureinn [idea]                  # workspace setup, 3 intake questions
/pm-entity-registry              # entity list + key states only (lean mode)
/pm-business-rules-library       # core rules in Draft
/pm-features-list                # feature inventory + FEAT-IDs + KANO + V×C
/pm-mvp-scope                    # MVP scope + Delivery Stripe assignment
/pm-feature-design [FEAT-ID]     # → JIT delivery engine
```

Skips: Phase 1, 2, 3a, 3b. Never skips: domain registers, feature list with FEAT-IDs (required by `pm-feature-design`).

---

## Full flow

### [Phase 1 - Foundation](phase-1-foundation/index.md) (~1 day)

| Team type | Skills |
|---|---|
| Solo | `/pm-project-charter` only |
| Small team (2-3) | `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |
| Corporate | `/pm-stakeholder-map` → `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |

### [Phase 2 - Discovery](phase-2-discovery/index.md) (1-3 weeks)

Four tracks run in parallel, converge at Problem Validation Summary:

| Track | Skill | Output |
|---|---|---|
| A - Tech | `/pm-tech-feasibility` | Tech Feasibility Report |
| B - Domain | `/pm-domain-analysis` | Domain Analysis |
| C - Market | `/pm-market-analysis` | Market Size, Competitor Analysis, SWOT |
| D - Customer | `/pm-personas` → `/jtbd-building` | Segments, Personas, JTBD |
| Convergence | `/pm-problem-validation` | Problem Validation Summary |

### [Phase 3a - Validation](phase-3a-validation/index.md) (externally paced)

| Step | Action |
|---|---|
| 1 | `/design-thinking` |
| 2 | `/pm-hypotheses` (Plan mode) |
| 3 | You: run experiments |
| 4 | `/pm-hypotheses` (Results mode) → **GO / PIVOT / STOP** |

### [Phase 3b - Commercial Definition](phase-3b-definition/index.md) (hours to a few sessions)

```
pm-kotler → pm-lean-canvas → pm-kpis → pm-business-case → pm-product-roadmap (v1) → pm-prd
```

PRD is frozen at Phase 3b exit.

### Pre-Phase 6 - Technical Foundation

```bash
/common-ground    # from fullstack-dev-skills plugin
```

Tech stack decision, repo structure, COMMON-GROUND.md.

### [Phase 4 - Domain Modeling](phase-4-domain/index.md) (3-5 days)

```
pm-domain-model → pm-entity-registry → pm-business-rules-library
→ pm-privacy-requirements → pm-process-flows → pm-product-roadmap (v2)
```

### [Phase 5 - Feature Planning](phase-5-planning/index.md) (2-3 days)

```
pm-features-list → pm-prioritize → pm-mvp-scope → pm-product-roadmap (v3)
```

### [Phase 6+7 - JIT Delivery](phase-6-build/index.md) (ongoing)

Per feature, just before build:
```
pm-feature-design [FEAT-ID] → Design Inspection → Build → Test → Deploy → Shipped
```

---

## Key rules

- **Phase 3a is a hard gate.** Only GO advances. PIVOT loops. STOP ends.
- **Phase 3b requires Phase 3a GO.** Cannot be entered without a GO verdict.
- **PRD is frozen** after Phase 3b. No scope changes without a formal change request.
- **Spec gate before build.** Feature Card Sections 1-3 complete before any feature enters code.
