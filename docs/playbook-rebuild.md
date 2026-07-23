# Playbook 2: Rebuild

Onboard an existing product into Pureinn. Reconcile legacy docs against the codebase, establish clean registers, and enter the JIT build cycle.

**Use when:** a product was built outside Pureinn (or under an older version) and you need to onboard it - especially after a team change, when legacy docs no longer match the code.

---

## How to read this page

This is a **route map** - which sub-path applies to your situation, and what unlocks the next step. The full skill-by-skill runbook lives on the [Rebuild reference page](rebuild/index.md).

---

## Which sub-path? (the one decision this page makes for you)

- **Trigger for A1 Reconcile:** legacy docs (BRD, FSD, domain models) exist AND conflict with the code or with each other.
- **Trigger for A2 Bootstrap:** docs are clean/consistent with code, or don't exist at all.

```
Legacy docs exist AND conflict with code?
            │
      ┌─────┴─────┐
      │ Yes       │ No (clean or absent)
      ▼           ▼
  A1 RECONCILE   A2 BOOTSTRAP
```

If you're unsure which applies: if you'd trust the docs to write a business rule from without checking the code, you're in A2. If the docs and code visibly disagree on anything, you're in A1.

---

## A1 - Reconcile

- **When to run / skip:** run when legacy docs exist and conflict with code. Never skip if a conflict exists - shipping on stale docs propagates the wrong business intent into new features.
- **Gather first:** all legacy docs (BRD, FSD, domain models, anything describing business intent) in one `legacy-docs/` folder. Read completely, not just the summary/index files.
- **What you get:** a Reconciliation Report, clean R1-R4 registers, and a source-disposal verdict (safe to archive the legacy docs, or not yet).
- **What it does NOT give you:** code changes. Reconciliation only rewrites documents - code is source of truth for structure and is never touched.
- **Done when:** `/pm-reconcile verify` passes and the source is ruled safe to archive.

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

**Core rule:** code wins on structure, legacy docs win on business intent. On conflict, flag it (`DIV-NN`) and ask the team - don't silently pick one.

Full detail: [Rebuild reference - A1](rebuild/index.md#a1---reconcile-conflicting-docs)

---

## A2 - Bootstrap

- **When to run / skip:** run when docs are clean/consistent, or absent. Never applies if a conflict exists (that's A1).
- **Gather first:** nothing beyond the existing codebase - this path reads from code, not from docs.
- **What you get:** R1-R4 registers extracted from the codebase + feature inventory pushed to Notion. `pm-reverse-extract` shows what it found before writing anything.
- **What it does NOT give you:** a reconciliation report or a strategic layer (vision, business model) - Rebuild captures structure, not strategy.
- **Done when:** you've confirmed or corrected the extracted feature inventory.

```bash
/pureinn                           # workspace setup
/common-ground                     # technical context from existing code
/pm-glossary                       # domain glossary
/pm-entity-registry                # entities from codebase → R1
/pm-business-rules-library         # rules from codebase → R2-3
/pm-reverse-extract                # feature inventory from codebase → R4 + stub cards
→ /pm-stripe                       # JIT delivery
```

Full detail: [Rebuild reference - A2](rebuild/index.md#a2---bootstrap-clean-or-no-docs)

---

## After Rebuild → Feature Implementation

Both sub-paths exit into Feature Implementation once registers + feature inventory exist:

```bash
/pureinn [project-slug]
/pm-feature-design [FEAT-ID]
→ JIT delivery engine
```

See [Playbook 3: Feature Implementation](playbook-feature.md).
