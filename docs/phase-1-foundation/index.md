# Phase 1 - Foundation

Set up the project structure, define the team, identify stakeholders, and establish communication protocols before discovery begins.

**Duration:** ~1 day · **Gate type:** Soft gate (gaps acknowledged, can proceed) · **Playbooks:** Greenfield

---

## How to read this page

Per-skill blocks below: **When to run/skip** (the explicit trigger) → **Gather first** (inputs) → **Command** → **What you get** → **What it does NOT give you** → **Done when**. This phase scales down hard for small teams - most of it is legitimately skippable, and the trigger tells you exactly when.

---

## When to enter this phase

Enter Phase 1 at the start of every Greenfield project. Do not over-engineer for small or solo builders - most of this phase is skip conditions, not mandatory work.

**What you need before entering:** a product idea or initiative to define, and a basic sense of who's involved. No prior artifacts required - this is the entry point.

---

## Step 1 - Project Charter

- **When to run / skip:** always run. This is the one artifact every team size needs, solo included.
- **Gather first:** nothing beyond the idea itself.
- **Command:** `/pm-project-charter`
- **What you get:** scope, objectives, success criteria, assumptions, and risks - plus the Assumptions & Risks Register, a living document updated throughout the project.
- **What it does NOT give you:** team structure or communication protocol - that's Steps 2-3, and only if you have a team.
- **Done when:** the Charter states scope, objectives, and success criteria without open placeholders.

---

## Step 2 - Stakeholder Map

- **When to run / skip:** run only if there are external investors, a board, or stakeholders beyond the building team. **Skip if solo builder with no external investors or board** - there's no one to map.
- **Gather first:** who has influence or interest in this project outside the core team.
- **Command:** `/pm-stakeholder-map`
- **What you get:** all stakeholders, their influence/interest, and an engagement strategy per stakeholder.
- **What it does NOT give you:** team roles (that's internal) - this is external-facing only.
- **Done when:** every stakeholder with real influence has an engagement plan.

---

## Step 3 - Team Roster

- **When to run / skip:** run for any team of 2+. **Skip if solo builder** - there's no roster to document.
- **Gather first:** who's on the team and in what capacity.
- **Command:** `/pm-team-roster`
- **What you get:** team structure, roles, responsibilities, decision rights.
- **What it does NOT give you:** communication cadence - that's Step 4.
- **Done when:** every team member has a defined role and decision rights are unambiguous.

---

## Step 4 - Communication Charter

- **When to run / skip:** run for any team of 2+. **Skip if solo builder** - no team to communicate with.
- **Gather first:** Team Roster (Step 3).
- **Command:** `/pm-comms-charter`
- **What you get:** communication cadences, channels, escalation paths, meeting structure.
- **What it does NOT give you:** stakeholder communication - that's the Stakeholder Map's engagement plan (Step 2), a separate concern from internal team comms.
- **Done when:** every recurring meeting/channel has an owner and cadence.

---

## Recommended path by team size

| Team type | Run |
|---|---|
| Solo | Step 1 only |
| Small team (2-3) | Step 1 → Step 3 → Step 4 |
| Corporate | Step 2 → Step 1 → Step 3 → Step 4 |

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
