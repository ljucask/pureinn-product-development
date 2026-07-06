---
name: pm-reconcile-status
description: Progress dashboard for an in-flight reconciliation rebuild. Reads the Reconciliation Plan and state.json, shows which areas are done, in progress, and pending, surfaces open business-logic divergences that still need the team's decision, and routes to the next area command. Run it every time you sit down to a multi-session reconcile. Read-only - it changes nothing.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.1.0"
  domain: product-management
  triggers: reconcile status, reconciliation progress, rebuild status, what is left to reconcile, reconcile dashboard, disposal readiness, verify status
  role: orchestrator
  scope: status
  output-format: dashboard
  related-skills: pm-reconcile, pm-entity-registry, pm-business-rules-library, pm-reverse-extract
---

# PM - Reconcile Status


## Agent mode (`--agent`)

Podporuje `--agent`: beží autonómne v subagentovi, nadraftuje artefakt z existujúcich vstupov, vráti krátky súhrn + coverage note.

- **Bez flagu** → interaktívne (default); pri ťažkých vstupoch ponúkni agent režim.
- **`--agent`** → poslúchni. Najprv over úplnosť vstupov. Čo chýba: NEVYMÝŠĽAJ - označ `[ASSUMED - čo/prečo]` vo výstupe aj v súhrne. Nikdy nehalucinuj medzeru.

---

## What this skill does

A read-only dashboard for a reconciliation rebuild driven by `pm-reconcile`. Because reconciliation runs across multiple sessions, this skill answers "where are we" at a glance: which areas are done, what is next, and which divergences still need a human ruling. It writes nothing.

Run it whenever you return to a reconcile in progress, before deciding what to do next.

---

## Dependencies

- `pm-reconcile` plan exists: `reconcile/reconciliation_plan.md` and `state.json reconcile.areas[]`.

If no plan exists, do not guess. Tell the user:
```
No reconciliation plan found. Run /pm-reconcile first to inspect the docs and build the plan.
```

---

## Step 1: Read state

Read `state.json reconcile` (machine source of truth for status) and `reconcile/reconciliation_plan.md` (area definitions). If they disagree, trust `state.json` and note the drift. Read `reconcile/reconciliation_report.md` to count and list open divergences (`DIV-NN` rows with no ruling, and any "Open questions for the team"). If a `reconcile.verify` block exists, read it (and `coverage_report.md` if present) to report disposal readiness.

## Step 2: Render the dashboard

```
RECONCILE STATUS - [Product Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scope:  [domain-by-domain / whole product]    Policy: [source-of-truth policy]
Progress: [X]/[N] areas done

 #  AREA       TARGET                                STATUS         BATCHES  DIV OPEN
 1  domain     domain/entities.md                    ✓ done         1/1      0
 2  rules      business_rules.md + decision_models   ▸ in_progress  2/5      2
 3  features   features/feature_list.md              · pending      -        -

NEEDS A TEAM DECISION (open divergences)
  DIV-03 [rules] refund window: doc 14d vs code 30d - decide fix code / update rule
  [open question from report]

SOURCE DISPOSAL (verify gate)
  [not run yet / ⚠️ not safe - 4 gaps, 2 DIV open / ✅ safe to archive - covered 100%]

NEXT
  ▸ /pm-reconcile rules        (resumes at batch 3/5 - completed batches are not redone)
  then /pm-reconcile features
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Rules for "NEXT":
- If an area is `in_progress` → resume it first.
- Else the lowest-order `pending` area is next.
- If all areas are `done` but `verify.disposal_ready` is not `true` (or verify never ran) → next is `/pm-reconcile verify` (do not call the source safe to archive yet).
- If all areas are `done` and `verify.disposal_ready: true` → reconciliation is complete and the source is safe to retire; route onward (below).

## Step 3: Route

| Situation | Output |
|---|---|
| Area in progress | "Resume with `/pm-reconcile [area]`." |
| Next area pending | "Run `/pm-reconcile [area]` to continue." |
| Open divergences block confidence | "Decide DIV-NN with the team before marking rules Final; they are listed above." |
| All areas done, verify not yet ✅ | "Content first: run `/pm-reconcile verify` to prove the source is fully captured **and incorporate any gaps** before retiring it." |
| All areas done + verify ✅ | "Source safe to archive. Now form: `/pm-product-roadmap` (phases over the complete set) → `/pm-audit` (naming, metadata, descriptions - covers what verify added) → `/pm-stripe` for JIT delivery. Review `reconciliation_report.md` with the team." |

---

## Handoff

```
---
**Čo si teraz má:** Aktuálny obraz rekonciliácie - čo hotové, čo zostáva, ktoré divergencie čakajú na rozhodnutie tímu.

**Ďalší krok:** `/pm-reconcile [oblasť]` podľa NEXT vyššie.
Keď sú všetky oblasti hotové, poradie je obsah→plán→forma: `/pm-reconcile verify` (dôkaz pokrytia + doplnenie medzier) → `/pm-product-roadmap` (fázy) → `/pm-audit` (forma nad kompletným setom) → `/pm-stripe`.

**Môžeš preskočiť ak:** rekonciliácia ešte nezačala — vtedy spusti `/pm-reconcile` (plán) najprv.
```
