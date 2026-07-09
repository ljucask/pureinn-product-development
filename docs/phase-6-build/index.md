# Phase 6+7 - JIT Delivery (Build)

The shared build cycle for all three playbooks. Spec happens per Feature (not per Feature Set), just-in-time, immediately before build. Orchestrated by `/pm-stripe`.

**Duration:** Ongoing until launch  
**Gate type:** Hard gate at Design Inspection  
**Playbooks:** All three (Greenfield, Feature Implementation, Rebuild)

---

## The JIT cycle per feature

```
Viability      Spec            Design        Build         Review         Ship
(optional)  →  (JIT)        →  Inspection →  (code+tests)→ (code insp.) → (immutable)
pm-feature-    pm-feature-      pm-stripe                                  pm-stripe
 viability      design
    │              │
    ▼              ▼
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

| Step | Status transition | Skill | Output |
|---|---|---|---|
| 0 (optional) | - | `/pm-feature-viability [FEAT-ID]` | KANO, MDP scope, success metrics |
| 1 | → 2_Spec_Done | `/pm-feature-design [FEAT-ID]` | Register finalization + Feature Card Sections 1-3 |
| 2 | → 3_Ready_to_Build | Design Inspection (`/pm-stripe`) | Team or solo review of Sections 1-3 |
| 3 | → 4_In_Build | Build skills | Code + tests |
| 4 | → 5_In_Review | `/pm-stripe` | Commits, tests, flag verification → Section 4 |
| 5 | → 6_Shipped | Code Inspection (`/pm-stripe`) | Final review; Feature Card immutable |

**Hard spec gate:** Sections 1-3 complete + status `3_Ready_to_Build` before any feature enters build. No exceptions.

---

## Pureinn spec skills

| Skill | What it does | Output |
|---|---|---|
| [pm-feature-design](pm-feature-design.md) | JIT design for one feature: register finalization, ACs, sequence diagram, Feature Card Sections 1-3 | Feature Card Sections 1-3, register updates |
| [pm-feature-card](pm-feature-card.md) | Feature Card management and lifecycle | Feature Card CRUD operations |
| [pm-feature-viability](pm-feature-viability.md) | Pre-spec viability check: KANO, MDP scope, success metrics | Viability assessment (skip if feature already scoped) |
| [pm-business-rule-core](pm-business-rule-core.md) | Add/update a core business rule in the library | Updated `business_rules.md` |
| [pm-business-rule-critical](pm-business-rule-critical.md) | Add/update a critical business rule (high-risk, legally significant) | Updated `business_rules.md` with risk flags |
| [pm-business-rule-governance](pm-business-rule-governance.md) | Governance and change management for business rules | Rule change log, approval trail |
| [pm-decision-model](pm-decision-model.md) | Add/update a decision table in `decision_models.md` | Updated `decision_models.md` |
| [pm-diagrams](pm-diagrams.md) | Generate visual diagrams (User Flow, Architecture, JTBD Forces, ERD) | Mermaid diagrams |
| [pm-glossary](pm-glossary.md) | Domain glossary - start early, update as new terms surface | `glossary.md` |

---

## pm-feature-design: what happens in one run

The core spec skill. One run per feature, just before it enters build.

1. Reads the Feature Card (stub at entry)
2. **Discovery Interrogation** - surfaces unknowns and ambiguities; calibrated to feature criticality
3. Enriches `entities.md` - adds exact guard conditions to state transitions for this feature
4. Enriches `business_rules.md` and `decision_models.md` - finalizes rules this feature enforces (Draft → Final)
5. Populates Feature Card Section 1 (Business Constraints) - links entity IDs, BR-IDs, TBL-IDs
6. Writes Feature Card Section 2 (Acceptance Criteria) - derived from register state + business rules
7. Writes Feature Card Subtasks - nuance helpers captured in discovery
8. Generates Mermaid.js sequence diagram + files to modify - writes to Feature Card Section 3
9. Pushes to Notion; sets status to `2_Spec_Done` (or `2b_In_Design` for frontend features awaiting Figma)

**Atomic commit protocol:**
```
Commit 1: "spec([FEAT-ID]): guard conditions + rule finalization"
  → entities.md, business_rules.md, decision_models.md updated

Commit 2: "spec([FEAT-ID]): feature design complete"
  → Feature Card Sections 1-3 populated
  → status: 2_Spec_Done
```

Register updates committed *before* any code generation begins - prevents merge conflicts in parallel Stripes.

---

## Build skills (from partner plugins)

Not every skill applies to every feature. Choose what fits.

| Skill | Plugin | Purpose |
|---|---|---|
| `/fullstack-guardian` | fullstack-dev-skills | Full-stack implementation (reads Feature Card Section 3) |
| `/impeccable-craft` | impeccable | Frontend UI implementation |
| `/test-master` | fullstack-dev-skills | Unit + integration tests |
| `/playwright-expert` | fullstack-dev-skills | E2E tests |
| `/code-reviewer` | fullstack-dev-skills | Code review |
| `/impeccable-harden` | impeccable | UI edge cases, error states, accessibility |
| `/security-reviewer` | fullstack-dev-skills | Security audit |
| `/devops-engineer` | fullstack-dev-skills | CI/CD, deployment |
| `/monitoring-expert` | fullstack-dev-skills | Observability, alerting |

**Optional spec support** (run when needed, not per feature): `/architecture-designer`, `/api-designer`, `/impeccable-shape`.

---

## Delivery rules for existing products

Mandatory when building onto a product that already has users. Greenfield relaxes these until launch.

| Rule | Detail |
|---|---|
| Feature flags | All new code wrapped in feature flags (OFF by default), both FE + BE |
| API changes | Additive only - no renames, no deletes, no breaking changes |
| DB changes | Additive only - new tables, new columns |
| Regression | Full suite per feature before merge |
| Performance gate | Feature adds ≤10% latency to existing API calls |
| Gradual rollout | Internal → 5% → 25% → 50% → 100% |
| Kill switch | Disable flag if error rate >5% |
| Post-launch monitoring | Minimum 4 weeks |

---

## Feature Card sections reference

| Section | Written when | By |
|---|---|---|
| Section 0 (stub) | Phase 5 (`pm-features-list`) | Pureinn |
| Section 1 - Business Constraints | Phase 6 (`pm-feature-design`) | Pureinn |
| Section 2 - Acceptance Criteria | Phase 6 (`pm-feature-design`) | Pureinn |
| Section 3 - Build Spec + Sequence Diagram | Phase 6 (`pm-feature-design`) | Pureinn |
| Section 4 - Post-build record | After 5_In_Review | Build team |

Section 3 is what developers read. The Feature Card is immutable after `6_Shipped`.
