# Playbook 2: Rebuild

Onboard an existing product into Pureinn. Reconcile legacy docs against the codebase, establish clean registers, and enter the JIT build cycle.

**Use when:** a product was built outside Pureinn (or under an older version) and you need to onboard it - especially after a team change, when legacy docs no longer match the code.

See [Rebuild reference](rebuild/index.md) for full skill documentation, flow details, and source-of-truth rules.

---

## Two sub-paths

```
Legacy docs exist AND conflict with code?
            │
      ┌─────┴─────┐
      │ Yes       │ No (clean or absent)
      ▼           ▼
  A1 RECONCILE   A2 BOOTSTRAP
```

---

## A1 - Reconcile (conflicting docs)

**Flow:**
```bash
/pureinn + /common-ground          # workspace + tech context
→ put legacy docs in legacy-docs/
→ /pm-reconcile                    # reconciliation plan
→ /pm-reconcile domain             # entities → R1
→ /pm-reconcile rules              # business rules + decision models → R2-3
→ /pm-reconcile features           # feature inventory → R4 + stub cards
→ /pm-reconcile-status             # check progress at any time
→ /pm-reconcile verify             # coverage proof; source-disposal gate
→ /pm-product-roadmap              # delivery-driven roadmap
→ /pm-audit                        # form check
→ archive source → /pm-stripe      # JIT delivery
```

**Core rule:** code wins on structure, legacy docs win on business intent. Code is never changed during reconciliation.

---

## A2 - Bootstrap (clean or no docs)

**Flow:**
```bash
/pureinn                           # workspace setup
/common-ground                     # technical context from existing code
/pm-glossary                       # domain glossary
/pm-entity-registry                # entities from codebase → R1
/pm-business-rules-library         # rules from codebase → R2-3
/pm-reverse-extract                # feature inventory from codebase → R4 + stub cards
→ /pm-stripe                       # JIT delivery
```

`pm-reverse-extract` shows what it found before writing anything - you confirm or correct.

---

## After Rebuild → Feature Implementation

Both sub-paths exit into Feature Implementation:

```bash
/pureinn [project-slug]
/pm-feature-design [FEAT-ID]
→ JIT delivery engine
```
