# pm-team-roster

> Team Roster, Decision Rights Matrix, and Skill Gap Assessment

**Phase:** 1 - Foundation  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** team roster, decision rights, skill gap assessment, team structure, Phase 1

---

## When to use

After `pm-project-charter` and `pm-stakeholder-map`. Defines who is on the team, what decisions they own, and what skills are missing.

**Skip if:** solo builder with no team.

---

## What it produces

Three artifacts (`artifacts/phase-1-foundation/team-roster.md`):

1. **Team Roster** - Core team members, roles, responsibilities, availability (FTE/PT), and contact
2. **Decision Rights Matrix** - Who has final say on product, technical, design, and business decisions
3. **Skill Gap Assessment** - What the team is missing and how to address it (hire / contract / delay)

---

## How to invoke

```bash
/pm-team-roster           # standard interactive run
/pm-team-roster --agent   # autonomous draft from available context
```

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - project scope informs what team roles are needed
- `pm-stakeholder-map` - RACI context from stakeholder map

**Produces for:**
- `pm-comms-charter` - team size, timezones, and tools shape communication setup
- `pm-onboarding` - team structure is source for role-specific briefs

**Related skills:** `pm-project-charter`, `pm-comms-charter`, `pm-stakeholder-map`
