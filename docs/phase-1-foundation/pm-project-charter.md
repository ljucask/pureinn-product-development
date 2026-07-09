# pm-project-charter

> Project Charter and Assumptions & Risks Register for a new product initiative

**Phase:** 1 - Foundation  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** project charter, assumptions register, risks register, project kickoff, Phase 1

---

## When to use

First skill in Phase 1 for every Greenfield project. For solo builders, this is often the only Phase 1 skill needed. For teams, run after `pm-stakeholder-map` so stakeholder context can inform charter decisions.

---

## What it produces

Two artifacts:

**Project Charter** (`artifacts/phase-1-foundation/project-charter.md`):
- Why now - the problem and the opportunity
- What we're building - product definition at initiative level
- Success criteria - how we know this worked
- Constraints - time, budget, technology, team
- Non-negotiables - what is not up for negotiation
- Known assumptions and risks (summary; detail in Register)

**Assumptions & Risks Register** (`artifacts/phase-1-foundation/assumptions-risks.md`):
- Assumptions with confidence rating and validation plan
- Risks with probability, impact, and mitigation
- Living document - updated throughout the project

---

## How to invoke

```bash
/pm-project-charter           # standard interactive run
/pm-project-charter --agent   # autonomous draft, requires review
```

---

## Dependencies

**Recommended before running:**
- `pm-stakeholder-map` - stakeholder context informs charter decisions and constraints

**Produces for:**
- All Phase 2 skills - charter defines scope, constraints, target market
- `pm-team-roster` - charter scope informs team needs
- `pm-comms-charter` - charter timeline informs meeting cadence

**Related skills:** `pm-team-roster`, `pm-comms-charter`, `pm-stakeholder-map`
