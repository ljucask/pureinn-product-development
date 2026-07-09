# pm-domain-model

> Domain Model - domain boundaries, entity catalogue, cross-domain ERD - the higher-level companion to pm-entity-registry

**Phase:** 4 - Domain Modeling (optional companion to pm-entity-registry)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** domain model, ERD, entity relationship, domain entities, ubiquitous language, data model, Phase 4

---

## When to use

Phase 4, after or alongside `pm-entity-registry`. While `pm-entity-registry` builds the operational register (entities + state machines per entity), `pm-domain-model` provides the higher-level view: domain boundaries, cross-domain ERD, and ubiquitous language.

**Not required for all products.** Skip if the product is small and fits within one domain. Add when the domain structure is complex enough that a cross-domain ERD adds navigational value for the team.

---

## What it produces

**Domain Model** (`artifacts/phase-4-domain/domain-model.md`) - two-stage output:

**Stage 1 (generated first, requires confirmation):**
- Business Domains - bounded areas of responsibility with ownership
- Entity Catalogue - all entities with domain ownership, brief description, key states
- Cross-domain relationships at a high level

**Stage 2 (generated after Stage 1 confirmation):**
- Full Entity Definitions per domain - attributes, relationships, cardinality
- Cross-domain ERD diagrams (Mermaid.js - embedded; Excalidraw - high-level visual)
- Ubiquitous language glossary per domain

Stage 2 never starts until Stage 1 is confirmed. This prevents building detailed specs on top of a wrong domain structure.

---

## How to invoke

```bash
/pm-domain-model           # interactive
/pm-domain-model --agent   # autonomous synthesis from PRD and entity registry
```

---

## Reconciled mode (Rebuild playbook)

When `reconcile/reconciliation_report.md` exists alongside `domain/entities.md`, the skill enters **reconciled mode**:

- Takes the entity catalogue directly from the reconciled `entities.md`
- Builds the cross-domain ERD on top of already-reconciled entities
- Does NOT re-derive entities from code or old docs
- Does NOT re-question what the Reconciliation Report already settled

Reconciled mode is announced explicitly at Step 0 before proceeding.

---

## Relationship to pm-entity-registry

| pm-entity-registry | pm-domain-model |
|---|---|
| Operational register: entities + state machines per entity | Strategic view: domain boundaries + cross-domain ERD |
| Primary Phase 4 deliverable | Optional companion |
| Referenced by Feature Cards (`prd_ref`) | Referenced for architectural navigation |
| Lives in `domain/entities.md` (Live Register 1) | Lives in `artifacts/phase-4-domain/domain-model.md` |

Run `pm-entity-registry` first. Run `pm-domain-model` when the cross-domain view adds value.

---

## Dependencies

**Required before running:**
- `pm-prd` - product scope defines what domains and entities are needed

**Recommended:**
- `pm-entity-registry` - entity registry is the operational foundation; domain model adds the cross-domain layer
- `pm-problem-validation` - validated problem informs domain boundaries

**Produces for:**
- `pm-privacy-requirements` - entity attributes are the PII inventory input
- `pm-business-rules-library` - domain boundaries scope business rule application
- `pm-feature-design` (JIT Phase 6) - domain structure referenced in functional specs

**Related skills:** `pm-entity-registry`, `pm-business-rules-library`, `pm-privacy-requirements`, `pm-domain-analysis`
