---
name: pm-team-roster
description: Generate a Team Roster, Decision Rights Matrix, and Skill Gap Assessment for a product initiative. Use in Phase 1 after Stakeholder Map.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: team roster, decision rights, RACI, skill gap assessment, team structure, Phase 1
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-project-charter, pm-comms-charter, pm-stakeholder-map
---

# PM - Team Roster + Decision Rights

## What this skill does

Generates three artifacts:
1. **Team Roster** - Core team members, roles, availability
2. **Decision Rights Matrix** - Who has final say on what
3. **Skill Gap Assessment** - What the team is missing and how to address it

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - scope and constraints define team requirements
- `pm-stakeholder-map` - RACI context, decision authority already partially defined there

**Produces artifacts used by:**
- `pm-comms-charter` - team size, timezones, tools inform communication setup
- Phase 6-7 skills - team capacity affects stripe planning and delivery

---

## Step 0: Current state check

Check for existing artifacts:
- Team Roster
- Decision Rights Matrix
- Skill Gap Assessment

Also check: does a Project Charter exist? Cross-reference budget constraints vs. team plan. Does a Stakeholder Map / RACI exist? Check for decision authority conflicts.

Look for: unfilled roles (TBD), gaps without mitigation plan, decision areas with no clear owner, skill gaps that block Phase 6 start.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 2 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 2 - Team

Ask all as plain text:

List the core team members. For each person: role, full-time or part-time (what %), and whether they are an employee, contractor, or co-founder.

After answers, confirm: "Is this the complete team for this project?"

---

### Group 2 of 2 - Decision rights and gaps

Ask all as plain text:

Who has the final say in each of these areas: product scope and priorities, technical decisions (architecture, stack), design and UX direction, budget and hiring, Go/No-Go at phase gates?

What is currently missing or weak in the team? What roles or skills are gaps?

How do you plan to address those gaps? (hire, contractor, outsource, skip for now, other)

After answers, show complete team inputs summary. Ask for final confirmation before generating the artifact.

---

## Step 2: Generate artifacts

Generate all documents in English.

---

### ARTIFACT 1: Team Roster

```markdown
# Team Roster - [Product Name]

> **Version:** 1.0 · **Date:** [date]

---

## Core Team

| Name | Role | Type | Availability | Responsibility |
|---|---|---|---|---|
| [Name/TBD] | PM | Internal | 100% | Product ownership, stakeholder communication, phase gates |
| [Name/TBD] | Tech Lead | Internal | 100% | Architecture decisions, tech feasibility, code quality |
| [Name/TBD] | FE Developer | [Type] | [%] | [Responsibility] |
| [Name/TBD] | BE Developer | [Type] | [%] | [Responsibility] |
| [Name/TBD] | UX Designer | [Type] | [%] | [Responsibility] |
| [Name/TBD] | QA | [Type] | [%] | [Responsibility] |

---

## Extended Team / Advisors

| Name / Role | Type | Involvement | When |
|---|---|---|---|
| Legal | External | Ad-hoc | Phase 1, Phase 4 (GDPR) |
| Data Analyst | [Type] | Part-time | Phase 8+ (Beta, Launch) |

---

## Team Capacity

**Total capacity:** [X] effective FTE
**Peak capacity (Phase 6-7 Build):** [Y] FTE
**Critical dependency:** [If one person leaves / gets sick, what breaks]
```

---

### ARTIFACT 2: Decision Rights Matrix

```markdown
# Decision Rights Matrix - [Product Name]

> Each decision has one **owner** (Final Say). Others may consult.

---

| Decision area | Final Say | Consulted | Notes |
|---|---|---|---|
| **Product** | | | |
| MVP scope definition | [PM] | [Tech Lead, CEO] | |
| Feature prioritization | [PM] | [Tech Lead, UX] | |
| Scope change during build | [PM + Tech Lead] | [CEO] | Changes >X days = escalate to CEO |
| Phase Go/No-Go | [PM + CEO] | [Tech Lead, CFO] | |
| **Technology** | | | |
| Tech stack selection | [Tech Lead] | [PM, CTO] | |
| Architecture decisions | [Tech Lead] | [PM] | |
| Tech debt prioritization | [Tech Lead] | [PM] | |
| **Design** | | | |
| UX direction and flow | [UX Designer] | [PM] | |
| Design system | [UX Designer] | [Tech Lead] | |
| **Business** | | | |
| Budget approval | [CEO/CFO] | [PM] | |
| Hiring decisions | [CEO] | [PM, Tech Lead] | |
| Investor communication | [CEO] | [PM] | |
| Pricing model | [CEO + PM] | [CFO] | |
```

---

### ARTIFACT 3: Skill Gap Assessment

```markdown
# Skill Gap Assessment - [Product Name]

> **Goal:** Identify what the team is missing and have a plan before Phase 4+ (Build phases).

---

## Gap Analysis

| Skill / Role | Current state | Gap | Criticality | Mitigation | Timeline |
|---|---|---|---|---|---|
| Backend development | [Who / seniority / %] | [What's missing] | 🔴 Critical | [Hire / contractor] | [By Phase X] |
| QA / Testing | [Who / seniority / %] | [What's missing] | 🟡 Medium | [Plan] | [By Phase X] |
| Data Analytics | Nobody | Completely missing | 🟢 Low | External / Phase 8+ | Phase 9 Beta |
| [Other skill] | | | | | |

**Criticality:**
- 🔴 Critical - without this we cannot start Phase 6 (Build)
- 🟡 Medium - slows us down, but we have a workaround
- 🟢 Low - needed later, we have time

---

## Mitigation Plan

### Immediate actions (by end of Phase 1)
- [ ] [Action 1 - e.g. "Post Tech Lead position by [date]"]
- [ ] [Action 2]

### Short-term (by Phase 4)
- [ ] [Action 3]

### Long-term (Phase 6+)
- [ ] [Action 4]

---

**Team risk assessment:**
[One-sentence summary: Is the team sufficient for Phase 1-5? What is the biggest risk?]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Team Roster must cover:**
- [ ] Product Manager identified (name, availability %, type)
- [ ] UX/UI Designer identified (UX and UI - same person or split?)
- [ ] Tech Lead / Architect identified
- [ ] QA coverage addressed (dedicated lead or shared responsibility)
- [ ] Marketing / GTM Lead addressed (internal or external, when needed)
- [ ] Data Analyst addressed (needed if product is data-driven / AI)
- [ ] For AI products: AI/ML engineer or data scientist identified or gap flagged
- [ ] For SaaS: DevOps / Platform engineer addressed (CI/CD, cloud infra)
- [ ] Single point of failure identified (who, what breaks if they leave)

**Decision Rights Matrix must cover:**
- [ ] Product scope and priorities - one owner
- [ ] Tech stack selection - one owner
- [ ] Design approval - one owner
- [ ] Budget and hiring - one owner
- [ ] Go/No-Go at each phase gate - one owner
- [ ] Level of product team autonomy stated (can PM decide scope alone or needs CEO approval?)
- [ ] For AI products: model and data decisions ownership defined

**Skill Gap Assessment must cover:**
- [ ] All critical gaps identified with severity (Critical / Medium / Low)
- [ ] Mitigation plan per gap (hire, contractor, outsource, skip until phase X)
- [ ] Timeline per mitigation (by when must gap be resolved before it blocks Phase 6)
- [ ] For SaaS/AI: cloud infrastructure expertise gap assessed
- [ ] For AI products: AI ethics / responsible AI competency assessed

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-1/team-roster.md
pureinn-workspace/[project-slug]/artifacts/phase-1/decision-rights-matrix.md
pureinn-workspace/[project-slug]/artifacts/phase-1/skill-gap-assessment.md
```
