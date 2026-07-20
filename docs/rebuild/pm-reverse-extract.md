# pm-reverse-extract

> Migration path skill - extracts feature inventory from an existing codebase into Live Register 4, with Dependencies and Priority captured the same way as pm-features-list

**Phase:** Rebuild playbook  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 2.1.0  
**Triggers:** reverse extract, existing product, feature inventory, migration path, feature implementation onboarding, sync Notion, dependencies

**Structural parity with `pm-features-list`:** this skill produces the same fields and the same Notion property set as the Greenfield flow (Priority, Dependencies, Dev Stripe, KANO, V×C on every feature) - a project migrated via this skill and one built via `pm-features-list` look identical downstream (Notion filters, `pm-stripe`, `pm-audit`). Dependencies come from two sources: what you tell it directly, and candidates it derives from code evidence (one feature's code calling another's) - code-derived candidates are proposed and confirmed, never asserted silently.

---

## When to use

Step 3 of the migration path for an existing product. Runs after domain registers are initialized:

1. `/pm-entity-registry` - entities + state machines → `entities.md`
2. `/pm-business-rules-library` - business rules → `business_rules.md` + `decision_models.md`
3. `/pm-reverse-extract` (this skill) - feature inventory → `feature_list.md` + stub Feature Cards

Use instead of `pm-features-list` + `pm-mvp-scope` for existing products. Can also be re-run at any point to re-sync Notion after significant state changes.

---

## What it produces

1. **Feature List** (`features/feature_list.md`) - Live Register 4. Full feature inventory in FDD format (`[Action] [Result] [Object]`) with `FEAT-[DOMAIN]-NNN` IDs
2. **Stub Feature Cards** (`features/cards/FEAT-*.md`) - one per feature, status `1_Backlog`
3. **Stripe assignment** - which features go into which domain-coherent delivery stripe
4. **Notion push** - Feature hierarchy pushed to Product Features database (if URL configured)

---

## How to invoke

```bash
/pm-reverse-extract           # interactive
/pm-reverse-extract --agent   # autonomous extraction from codebase + existing docs
```

---

## Source material

Claude reads directly: codebase route files, controller files, API specs, schema files, test files, existing docs (any format - old FSD, BRD, user stories). The skill structures what Claude already knows from the code - it does not hallucinate features.

---

## What this skill does NOT do

- Initialize domain registers - run `pm-entity-registry` and `pm-business-rules-library` first
- Run a full KANO/V×C scoring workshop - not applicable to features already built (Phase, KANO, V×C, Priority are still proposed with reasoning and confirmed, so downstream tooling has real values, not blanks)
- Write Feature Card Sections 1-3 (JIT design) - that is `pm-feature-design`, run just before build
- Run discovery or validation - this is a sync operation, not a new product workflow

---

## Reconciled mode (when invoked by pm-reconcile)

When `reconcile/reconciliation_report.md` exists, it is the authoritative input:
- Features derived from reconciled code reality
- Old feature names kept as aliases
- Code-only features from the report included
- Doc-only / not-yet-implemented items are NOT extracted here (those are already carded as `1_Backlog` stubs during `/pm-reconcile features`)
- Does not re-question what the report already settled

---

## Dependencies

**Required before running:**
- `domain/entities.md` - `pm-entity-registry` must have run (entities define domain codes for FEAT-IDs)
- At least one source accessible: codebase or existing docs

**Recommended:**
- `reconcile/reconciliation_report.md` - if Rebuild path was taken, provides the authoritative feature list

**Produces for:**
- `pm-feature-design` - JIT design reads `feature_list.md` for feature context
- `pm-stripe` - stripe dashboard reads `feature_list.md` and Feature Card frontmatter
- Notion Product Features database - primary operational view for the team
- `pm-audit` - runs after reverse-extract as a verification pass

**Related skills:** `pm-entity-registry`, `pm-business-rules-library`, `pm-reconcile`, `pm-feature-design`, `pm-stripe`
