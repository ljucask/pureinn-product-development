# pm-reconcile-status

> Progress dashboard for an in-flight reconciliation - areas done/pending, open divergences, next command

**Phase:** Rebuild playbook  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.1.0  
**Triggers:** reconcile status, reconciliation progress, rebuild status, what is left to reconcile, reconcile dashboard, disposal readiness, verify status

---

## When to use

Every time you sit down to continue a multi-session reconciliation. Shows exactly where you left off and what needs to happen next. Read-only - changes nothing.

---

## What it produces

**Reconciliation Dashboard** (output to conversation, not saved):

- **Area progress:** which areas are Done / In Progress / Pending
- **Open divergences:** unresolved `DIV-NN` entries from the Reconciliation Report that need a human decision
- **Next command:** exactly which `/pm-reconcile [area]` command to run next
- **Disposal readiness:** whether verify has run and whether the source is safe to archive

---

## How to invoke

```bash
/pm-reconcile-status           # interactive dashboard (read-only)
/pm-reconcile-status --agent   # autonomous dashboard from reconcile plan + state.json
```

---

## Dependencies

**Required:**
- `reconcile/reconciliation_plan.md` - the plan defines what areas exist
- `state.json` - tracks area completion status

**Related skills:** `pm-reconcile`, `pm-entity-registry`, `pm-business-rules-library`, `pm-reverse-extract`
