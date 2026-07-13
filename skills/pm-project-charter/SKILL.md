---
name: pm-project-charter
description: Generate a Project Charter and Assumptions & Risks Register for a new product initiative. Use when starting Phase 1 of a Greenfield project.
license: MIT
metadata:
  agent-mode: decision
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


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

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

## Step 0: PREREQ check + current state

**What this skill needs:** Your knowledge of what you're building - no documents required. If you have research notes, briefs, or specs, include them and the skill will extract relevant context automatically.

**If you have nothing written down yet:** Proceed directly to Step 1 intake questions. The skill elicits everything it needs through questions.

**If a Project Charter already exists:** Read it. Evaluate: is it still current? If scope, constraints, and success definition haven't changed, surface this:
```
A Project Charter already exists. It looks [current / potentially outdated because: X].

Skip this skill and proceed to [next Phase 1 skill / Phase 2]?
Or regenerate / update the charter?
```

**Stakeholder Map check:** If a Stakeholder Map exists, cross-reference it for decision authority and constraints - feed into charter generation.

**Re-run behavior (delta mode):** If regenerating an existing charter, do not redraft blank. Compare new answers against the existing charter section by section, show what changed, and update only what the new input supports. Never silently overwrite prior decisions.

**Gaps check before generating:** Look for: empty scope sections, assumptions without validation plan, risks without mitigation or owner, constraints that may have changed. Flag any, but do not block generation.

---

## Step 1: Gather inputs

Ask questions in 3 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 3 - Product and motivation

Ask all as plain text:

Describe the product or initiative. Brain dump is fine - no need to be polished. What are you building and who is it for?

What triggered this project? Why now and not 6 months ago or later?

What does success look like in 6-12 months? Be as specific as possible - name metrics, milestones, or observable outcomes.

**Push back on weak success criteria (once, before confirming):** if the success answer is a vanity metric (downloads, signups, page views, followers) or untestable ("be the best X", "delight users"), challenge it: "What observable behavior or revenue outcome would prove this? What number would make you say it failed?" A success criterion that cannot fail is not a criterion. Aim for at least one metric tied to retention, revenue, or repeated usage - something a failing product could not also show.

After answers, confirm: "Is this the right framing of what we're building and why?"

---

### Group 2 of 3 - Scope and constraints

Ask all as plain text:

What is fixed and non-negotiable? List hard constraints: budget cap, deadline, required tech stack, regulatory requirements, existing partnerships, or anything else that limits the solution space.

What is explicitly IN scope? What is explicitly OUT of scope? If unclear, describe what you'd cut first if time or budget runs short.

**Iron-triangle check (before confirming):** if budget, deadline, and scope are all declared fixed, flag it - one of the three must flex, or quality becomes the hidden variable that silently absorbs the pressure. Ask which one flexes first and record the answer; it goes into the charter as **Scope flex**. If the user insists all three are fixed, record that as a 🔴 risk in the register (R-xx: "No flex dimension - overrun will hit quality first").

After answers, confirm: "Are these constraints and scope boundaries accurate?"

---

### Group 3 of 3 - Assumptions, risks, and resources

Ask all as plain text:

What key assumptions are you building on that haven't been validated yet? What would need to be true for this project to succeed?

What could kill or significantly slow down the project? Name the 2-3 biggest risks.

What is the current budget or runway? A rough estimate is fine.

**Riskiest-assumption ranking (after collecting assumptions):** ask one follow-up: "Which single assumption, if false, kills the project?" Mark it `(RISKIEST)` in the register. This is the assumption Phase 2 discovery and Phase 3a experiments must attack first - validating comfortable assumptions while the fatal one waits is the most common discovery failure.

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

**Scope flex (first to cut if time or budget runs short):**
[The pre-agreed cut order - deciding this now, calmly, prevents deciding it later in a panic]

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

> Mark the single assumption that kills the project if false as `(RISKIEST)`. Customer and Market assumptions from this register become the candidate hypotheses in Phase 3a (`/pm-hypotheses`) - rank them so the riskiest is tested first, not last.

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
pureinn-workspace/[project-slug]/artifacts/phase-1-foundation/project-charter.md
pureinn-workspace/[project-slug]/artifacts/phase-1-foundation/assumptions-risks-register.md
```

---

## Handoff

---
**Čo si teraz má:** Zdokumentovaný zámer projektu - scope, success metrics, riziká a decision authority.
Toto je základ pre všetky Phase 2 skills a Phase 1 tímové skills.

**Ďalší krok:**
- Solo: `/pm-glossary` → potom `/pureinn` pre Phase 2 routing
- Malý tím: `/pm-team-roster` → `/pm-comms-charter`
- Tím/Corp: `/pm-team-roster` → `/pm-comms-charter` (stakeholder map mal byť pred charterom)
- Alebo spusti `/pureinn` pre gate check.

**Môžeš preskočiť `/pm-team-roster` ak:** Buduješ solo - žiadny tím na roster.
**Môžeš preskočiť `/pm-comms-charter` ak:** Buduješ solo - žiadny tím na komunikáciu.
