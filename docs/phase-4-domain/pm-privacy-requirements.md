# pm-privacy-requirements

> PII Inventory, Privacy Requirements, and GDPR Action Plan - maps domain entities to data protection obligations

**Phase:** 4 - Domain Modeling  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** privacy, GDPR, PII inventory, data protection, privacy requirements, compliance

---

## When to use

Phase 4, after domain entities are defined. Maps the entity model to privacy and data protection obligations. Required before any feature that handles personal data enters Phase 6 build.

This is a PM-level analysis, not a legal opinion. Validate with legal counsel before launch.

---

## What it produces

Three artifacts under `artifacts/phase-4-domain/`:

1. **PII Inventory** (`pii-inventory.md`) - which entities contain personal data, what type, sensitivity level, legal basis for processing, retention period
2. **Privacy Requirements** (`privacy-requirements.md`) - what the system must do to comply: consent flows, data subject rights (erasure, portability, access), retention enforcement, third-party data sharing obligations
3. **GDPR Action Plan** (`gdpr-action-plan.md`) - concrete actions with owners, timing, and blocking dependencies before launch

---

## How to invoke

```bash
/pm-privacy-requirements           # interactive
/pm-privacy-requirements --agent   # autonomous synthesis from domain model and legal requirements
```

---

## Dependencies

**Required before running:**
- `pm-entity-registry` or `pm-domain-model` - entities and their attributes are the PII mapping input; without entities the inventory will be incomplete

**Recommended:**
- `pm-domain-analysis` - legal and regulatory requirements from Phase 2 provide the baseline (sector-specific regulations, EU AI Act, data protection laws)

**Produces for:**
- `pm-business-rules-library` - privacy rules become Governance class (`BR-[DOMAIN]-NNN`) entries
- `pm-feature-design` - consent flows, data export, deletion features reference privacy rules JIT in Feature Card Section 1
- Build phase - developers need privacy requirements before implementing user-facing data features

**Related skills:** `pm-domain-model`, `pm-entity-registry`, `pm-domain-analysis`, `pm-business-rules-library`
