# pm-stakeholder-map

> Stakeholder Map, RACI Matrix, and Escalation Tree for a product initiative

**Phase:** 1 - Foundation  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** stakeholder map, RACI, escalation tree, stakeholder analysis, Phase 1 corporate

---

## When to use

Typically the first skill run in Phase 1, before `pm-project-charter`. Most valuable for corporate teams, multi-stakeholder initiatives, and products with external investors or board members.

**Skip if:** solo builder with no external investors, board, or multi-party stakeholders.

---

## What it produces

Three artifacts (`artifacts/phase-1-foundation/stakeholder-map.md`):

1. **Stakeholder Map** - Power/Interest matrix with engagement strategy per stakeholder
2. **RACI Matrix** - Responsible / Accountable / Consulted / Informed for key decisions
3. **Escalation Tree** - Who resolves conflicts and blockers, and how

---

## How to invoke

```bash
/pm-stakeholder-map           # standard interactive run
/pm-stakeholder-map --agent   # autonomous draft from available context
```

---

## Dependencies

**No hard prerequisites.** Can be the first skill run.

**Produces for:**
- `pm-project-charter` - stakeholder context informs charter decisions
- `pm-team-roster` - RACI and decision authority context
- `pm-comms-charter` - stakeholder communication needs

**Related skills:** `pm-project-charter`, `pm-team-roster`, `pm-comms-charter`
