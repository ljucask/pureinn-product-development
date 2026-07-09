# pm-glossary

> Build and maintain the domain glossary - start early, update continuously

**Phase:** Any (cross-phase, start in Phase 1 or 4)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** glossary, domain glossary, terminology, definitions, ubiquitous language, terms

---

## When to use

Start early - ideally after `pm-project-charter` or `pm-domain-model`. Update continuously as new domain terminology surfaces at any phase. Can be triggered at any time to add terms, review existing entries, or export the full glossary.

The glossary is additive: each run merges new entries with existing ones. Existing definitions are updated only if explicitly requested.

---

## What it produces

`domain/glossary.md` - a living table of domain terms:

| Term | Definition | Category | Phase introduced | Used in |
|---|---|---|---|---|
| [Domain term] | [Precise definition] | [Entity / Rule / Artifact / Process / Abbreviation] | [Phase X] | [entities.md, PRD, ...] |

**Categories:** Entity, State, Business Rule, Decision Table, Product Artifact, Process, Abbreviation, Regulatory term

**Special use in Rebuild (A1 Reconcile):** captures entity name aliases - the old name from legacy docs mapped to the canonical name from code. Prevents terminology confusion during and after the reconciliation process.

---

## How to invoke

```bash
/pm-glossary                          # interactive - add terms, review, or export
/pm-glossary --agent                  # autonomous scan of existing artifacts + add terms
```

---

## How it works

1. **State check** - looks for existing `glossary.md`; shows current term count and last updated date if found
2. Asks what to do: add new terms, review existing entries, or export
3. **Add terms:** accepts list of terms + context, generates precise definitions from existing artifacts
4. **Review mode:** surfaces terms that may be stale, conflicting, or missing definitions
5. **Agent mode:** scans all existing workspace artifacts for domain terms not yet in the glossary, drafts entries for review

---

## Dependencies

**No hard dependencies.** Can run at any point.

**Best used after:**
- `pm-project-charter` - initial product and business terminology
- `pm-domain-model` - richest set of domain entities and relationships
- `pm-business-rules-library` + `pm-feature-design` - business rule terminology
- Any phase completion - new terms surface naturally

**Related skills:** `pm-domain-model`, `pm-entity-registry`, `pm-business-rules-library`, `pm-feature-design`
