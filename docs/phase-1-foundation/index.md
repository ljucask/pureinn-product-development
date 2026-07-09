# Phase 1 - Foundation

Set up the project structure, define the team, identify stakeholders, and establish communication protocols before discovery begins.

**Duration:** ~1 day  
**Gate type:** Soft gate (gaps acknowledged, can proceed)  
**Playbooks:** Greenfield

---

## When to enter this phase

Enter Phase 1 at the start of every Greenfield project. This phase scales by team size - do not over-engineer for small or solo builders.

**Skip conditions:**
- `/pm-stakeholder-map` - skip if solo builder with no external investors or board
- `/pm-team-roster` - skip if solo builder
- `/pm-comms-charter` - skip if solo builder (no team to communicate with)

For solo builders, `/pm-project-charter` alone is often sufficient.

---

## What you need before entering

- A product idea or initiative to define
- Basic understanding of who is involved (team, stakeholders)

No prior artifacts required. This is the entry point.

---

## Skills in this phase

| Skill | What it does | Output |
|---|---|---|
| [pm-project-charter](pm-project-charter.md) | Defines project scope, objectives, success criteria, assumptions, and risks | Project Charter + Assumptions & Risks Register |
| [pm-stakeholder-map](pm-stakeholder-map.md) | Maps all stakeholders, their influence, interests, and engagement strategy | Stakeholder Map |
| [pm-team-roster](pm-team-roster.md) | Documents team structure, roles, responsibilities, and decision rights | Team Roster |
| [pm-comms-charter](pm-comms-charter.md) | Defines communication cadences, channels, escalation paths, and meeting structure | Communication Charter |

**Recommended order by team size:**

| Team type | Skills to run |
|---|---|
| Solo | `/pm-project-charter` only |
| Small team (2-3) | `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |
| Corporate | `/pm-stakeholder-map` → `/pm-project-charter` → `/pm-team-roster` → `/pm-comms-charter` |

---

## What you exit with

- **Project Charter** - scope, objectives, success criteria, constraints, risks
- **Assumptions & Risks Register** - live document updated throughout the project
- *(If team)* Team Roster + Communication Charter
- *(If stakeholders)* Stakeholder Map with engagement plan

---

## Phase exit gate

Run `/pureinn` after completing Phase 1 skills to check the exit gate and advance to Phase 2.

**Gate type: Soft.** The engine checks whether Phase 1 artifacts exist and flags gaps. You can proceed to Phase 2 while acknowledging missing items.
