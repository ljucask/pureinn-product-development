# pm-entity-registry

> Live Register 1 of 4 - Entity & State Registry (entities.md) - the architectural foundation of FDD+SDD

**Phase:** 4 - Domain Modeling  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 2.0.0  
**Triggers:** entity registry, domain model, state machine, entities, Phase 4, domain modeling

---

## When to use

Phase 4, after PRD is complete. The Entity Registry is the first of four Live Registers - the architectural foundation everything else references. Build this before business rules, features, or any Phase 6 work.

---

## What it produces

**Live Register 1** (`domain/entities.md`):

For each business entity:
- **Attributes** - fields with types, constraints, required/optional
- **States** - all lifecycle states the entity can be in
- **Transitions** - allowed state changes, triggers, emitted events
- **Mermaid.js state diagram** - embedded per entity for Claude Code to read as architectural guardrail

Guard conditions for transitions are **not added here**. They are finalized JIT in Phase 6 (`pm-feature-design`) when the feature using that transition is being built.

**Domain overview diagram:** Generated in Excalidraw (high-level team visual).

---

## How to invoke

```bash
/pm-entity-registry           # interactive
/pm-entity-registry --agent   # autonomous synthesis from PRD Business Capabilities
```

**Two modes, detected automatically at Step 0:**

| Mode | Condition | Behavior |
|---|---|---|
| **Create** | `domain/entities.md` does not exist | Full register generated from scratch |
| **Append** | `domain/entities.md` exists | New domain entities added, existing ones preserved |

Append mode is used in Feature Implementation when a new initiative introduces entities not covered by the existing register.

---

## How entities are derived

Source: **PRD Business Capabilities section** - or `product/scope_brief.md` Business Capabilities section on commissioned builds (same table contract; the Scope Brief's `[CANDIDATE-BR]` edge cases additionally seed the business rules register). Claude extracts nouns from the capabilities list, clusters them into business objects, and proposes the entity catalogue. The user confirms the entity catalogue before state machines are generated - preventing detailed work on top of a wrong domain structure.

Entity naming follows the Ubiquitous Language of the domain (business terms, not technical terms).

---

## The 4-register architecture

| Register | File | Skill |
|---|---|---|
| **1. Entity & State Registry** | `domain/entities.md` | `pm-entity-registry` (this skill) |
| 2. Business Rules Library | `domain/business_rules.md` | `pm-business-rules-library` |
| 3. Decision Models Matrix | `domain/decision_models.md` | `pm-business-rules-library` |
| 4. FDD Feature List | `features/feature_list.md` | `pm-features-list` |

---

## Reconciled mode (Rebuild playbook)

When `reconcile/reconciliation_report.md` exists, it is the authoritative input. Code is truth for structure and naming; the reconciliation report's resolved entities, attributes, and state machines are used directly. Claude does NOT re-derive or re-question what the report already settled.

---

## Dependencies

**Required before running:**
- `pm-prd` - PRD must include a Business Capabilities section (entities are derived from it) - or `pm-scope-brief` on commissioned builds

**Produces for:**
- `pm-business-rules-library` - entities define the scope of business rules
- `pm-features-list` - entities inform what operations and actions are needed as features
- `pm-feature-design` (JIT Phase 6) - adds guard conditions to transitions; reads entity states as guardrails
- `pm-domain-model` - entity registry is the operational foundation; domain model adds cross-domain view on top

**Related skills:** `pm-prd`, `pm-domain-model`, `pm-business-rules-library`, `pm-features-list`
