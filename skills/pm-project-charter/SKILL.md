---
name: pm-project-charter
description: Generate a Project Charter and Assumptions & Risks Register for a new product initiative. Use when starting Phase 1 of a Greenfield project.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: project charter, assumptions register, risks register, project kickoff, Phase 1
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-team-roster, pm-comms-charter, pm-stakeholder-map
---

# PM - Project Charter

## What this skill does

Generates two artifacts:
1. **Project Charter** - 1-page document: Why now, What we're building, Success criteria, Constraints
2. **Assumptions & Risks Register** - Project assumptions and risks with severity assessment

---

## Dependencies

**Recommended before running:**
- `pm-stakeholder-map` - stakeholder context helps define charter decisions and constraints

**Produces artifacts used by:**
- All Phase 2 skills - charter defines scope, constraints, target market
- `pm-team-roster` - charter scope informs team needs
- `pm-comms-charter` - charter timeline informs meeting cadence

---

## Step 0: Current state check

Check for existing artifacts:
- Project Charter
- Assumptions & Risks Register

Also check: does a Stakeholder Map exist? If yes, cross-reference for consistency (decision authority, constraints).

Look for: empty or placeholder sections, assumptions without validation plan, risks without mitigation or owner, constraints that may have changed.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 3 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 3 - Product and motivation

Ask all as plain text:

Describe the product or initiative. Brain dump is fine - no need to be polished. What are you building and who is it for?

What triggered this project? Why now and not 6 months ago or later?

What does success look like in 6-12 months? Be as specific as possible - name metrics, milestones, or observable outcomes.

After answers, confirm: "Is this the right framing of what we're building and why?"

---

### Group 2 of 3 - Scope and constraints

Ask all as plain text:

What is fixed and non-negotiable? List hard constraints: budget cap, deadline, required tech stack, regulatory requirements, existing partnerships, or anything else that limits the solution space.

What is explicitly IN scope? What is explicitly OUT of scope? If unclear, describe what you'd cut first if time or budget runs short.

After answers, confirm: "Are these constraints and scope boundaries accurate?"

---

### Group 3 of 3 - Assumptions, risks, and resources

Ask all as plain text:

What key assumptions are you building on that haven't been validated yet? What would need to be true for this project to succeed?

What could kill or significantly slow down the project? Name the 2-3 biggest risks.

What is the current budget or runway? A rough estimate is fine.

After answers, show complete Project Charter inputs summary. Ask for final confirmation before generating the artifact.

---

## Step 2: Generate artifacts

Generate both documents in English.

---

### ARTIFACT 1: Project Charter

```markdown
# Project Charter - [Product Name]

> **Version:** 1.0 · **Status:** Draft · **Date:** [date]
> **Owner:** [PM / Founder]

---

## Why this project exists

**Trigger:**
[What initiated this project - 1-2 sentences]

**Strategic opportunity:**
[Why now - market context, timing - 1-2 sentences]

---

## What we are building

**Product / Initiative:**
[Clear description - what it is, for whom, core value]

**In Scope:**
- [Item 1]
- [Item 2]

**Out of Scope:**
- [Item 1]
- [Item 2]

---

## Definition of success

**North Star (6-12 months):**
[One sentence - what success looks like]

**Key metrics:**
| Metric | Target | Horizon |
|---|---|---|
| [Metric 1] | [Target] | [Time horizon] |
| [Metric 2] | [Target] | [Time horizon] |

---

## Constraints and non-negotiables

| Type | Detail |
|---|---|
| Budget | [amount / bootstrap / TBD] |
| Timeline | [deadline or milestone] |
| Tech stack | [if fixed] |
| Regulation | [if relevant] |
| Other | [additional hard constraints] |

---

## Decision authority

**Project Owner:** [name / role]
**Go/No-Go approver:** [name / role]
**Conflict escalation:** [name / role]

---

*This document authorizes Phase 1 initiation. All assumptions will be validated in Phase 2 (Discovery).*
```

---

### ARTIFACT 2: Assumptions & Risks Register

```markdown
# Assumptions & Risks Register - [Product Name]

> **Version:** 1.0 · **Date:** [date] · **Owner:** [PM]
> Update at each phase gate.

---

## Assumptions

| ID | Assumption | Category | Consequence if false | Validation (when/how) | Status |
|---|---|---|---|---|---|
| A-01 | [Assumption 1] | Customer / Market / Tech / Business | [What happens] | [Phase 2 - customer interviews] | Unvalidated |
| A-02 | [Assumption 2] | | | | Unvalidated |

**Categories:** Customer · Market · Tech · Business · Regulation · Team

---

## Risks

| ID | Risk | Probability | Impact | Severity | Mitigation | Owner |
|---|---|---|---|---|---|---|
| R-01 | [Risk 1] | High / Medium / Low | High / Medium / Low | 🔴 / 🟡 / 🟢 | [Concrete action] | [Name] |
| R-02 | [Risk 2] | | | | | |

**Severity = Probability × Impact:**
- 🔴 Critical - address immediately
- 🟡 Medium - monitor, mitigation in plan
- 🟢 Low - accept or monitor

---

*Register is updated at each phase exit gate.*
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Project Charter must cover:**
- [ ] Why now - specific trigger (competitive threat, regulatory change, market pull, technology shift)
- [ ] What we are building - clear description, not generic
- [ ] Explicit In Scope / Out of Scope (prevents scope creep)
- [ ] Success definition - specific and measurable, not "successful product"
- [ ] Expected success metrics with concrete numbers and time horizon
- [ ] ROI / breakeven timeline
- [ ] Budget cap (hard vs. soft) with contingency buffer noted
- [ ] Hard deadlines if any (event-driven, compliance-driven, investor-driven)
- [ ] Decision authority - who is the Project Owner and Go/No-Go approver
- [ ] For SaaS: pricing model direction (subscription, usage-based, freemium, enterprise)
- [ ] For AI products: data strategy noted (who owns data, data moat potential, AI vendor dependency)

**Assumptions & Risks Register must cover:**
- [ ] Regulatory requirements identified per target market
- [ ] Deal-breakers listed (conditions that would stop the project)
- [ ] Key assumptions documented with validation plan per assumption
- [ ] Risks across: market, tech, team, financial, legal, operational
- [ ] Each risk has Probability + Impact + Mitigation + Owner
- [ ] For SaaS/AI: third-party API dependency risk (OpenAI, payment providers, etc.)
- [ ] For SaaS/AI: data privacy risk (GDPR applicability confirmed or ruled out)

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-1/project-charter.md
pureinn-workspace/[project-slug]/artifacts/phase-1/assumptions-risks-register.md
```
