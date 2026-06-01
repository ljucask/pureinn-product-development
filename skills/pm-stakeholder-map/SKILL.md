---
name: pm-stakeholder-map
description: Generate a Stakeholder Map, RACI Matrix, and Escalation Tree for a product initiative. Use in Phase 1 after Project Charter is complete.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: stakeholder map, RACI, escalation tree, stakeholder analysis, Phase 1 corporate
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-project-charter, pm-team-roster, pm-comms-charter
---

# PM - Stakeholder Map + RACI

## What this skill does

Generates three artifacts:
1. **Stakeholder Map** - Power/Interest matrix with engagement strategy
2. **RACI Matrix** - Responsible / Accountable / Consulted / Informed for key decisions
3. **Escalation Tree** - Who resolves conflicts and blockers

---

## Dependencies

**This skill has no hard prerequisites.** It is typically the first skill run in Phase 1.

**Produces artifacts used by:**
- `pm-project-charter` - stakeholder context informs charter decisions
- `pm-team-roster` - RACI and decision authority context
- `pm-comms-charter` - stakeholder communication needs

---

## Step 0: Current state check

Check for existing artifacts:
- Stakeholder Map
- RACI Matrix
- Escalation Tree

Look for: missing stakeholders, RACI gaps (decisions with no single Accountable), conflicts with Project Charter or Team Roster if those exist.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 2 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 2 - Stakeholders

Ask all as plain text:

List the internal team - roles involved in this project. For each, briefly describe their interest and how much influence they have over project outcomes.

Who outside the team has a stake in or influence over this project? List external stakeholders: investors, customer segments, partners, regulators, vendors. For each, what do they care about and how much power do they have? (can kill it, can block it, can slow it, or can simply be ignored)

After answers, confirm: "Is this a complete picture of who matters for this project?"

---

### Group 2 of 2 - Decisions and governance

Ask all as plain text:

What are the 5-8 most important decisions in this project? (e.g., Go/No-Go at phase gates, MVP scope, tech stack, pricing, hiring, fundraising)

Who has the final word when there is disagreement? Are there anticipated conflicts between stakeholders that need a clear escalation path?

After answers, show complete stakeholder inputs summary. Ask for final confirmation before generating the artifact.

---

## Step 2: Generate artifacts

Generate all documents in English.

---

### ARTIFACT 1: Stakeholder Map

```markdown
# Stakeholder Map - [Product Name]

> **Version:** 1.0 · **Date:** [date]

---

## Power / Interest Matrix

| | Low interest | High interest |
|---|---|---|
| **High power** | 👁 Keep satisfied | ✅ Manage closely |
| **Low power** | 🔍 Monitor | 📢 Keep informed |

### Manage Closely (High power, High interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| [Name/Role] | [Type: Internal/External] | [What they care about] | [How we engage] |

### Keep Satisfied (High power, Low interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| [Name/Role] | [Type] | [What they care about] | [How we engage] |

### Keep Informed (Low power, High interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| [Name/Role] | [Type] | [What they care about] | [How we engage] |

### Monitor (Low power, Low interest)
| Stakeholder | Role | Interest | Engagement strategy |
|---|---|---|---|
| [Name/Role] | [Type] | [What they care about] | [How we engage] |

---

## Stakeholder Register

| Name / Role | Type | Interests | Concerns / Risks | Preferred communication | Frequency |
|---|---|---|---|---|---|
| [Stakeholder 1] | Internal | [Interests] | [Concerns] | [Email/Slack/Meeting] | [Weekly/Monthly] |
```

---

### ARTIFACT 2: RACI Matrix

```markdown
# RACI Matrix - [Product Name]

> **R** = Responsible (does the work) · **A** = Accountable (owns the outcome) · **C** = Consulted (input requested) · **I** = Informed (receives update)
> Each decision has exactly one **A**.

| Decision / Activity | [Stakeholder 1] | [Stakeholder 2] | [Stakeholder 3] | [Stakeholder 4] | [Stakeholder 5] |
|---|---|---|---|---|---|
| [Decision 1] | A | R | C | I | - |
| [Decision 2] | | | | | |
| Phase 1 Go/No-Go | | | | | |
| Phase 2 Go/No-Go | | | | | |
| MVP Scope lock | | | | | |
| Tech stack decision | | | | | |
| Hiring decisions | | | | | |
| Budget / Fundraising | | | | | |

---

**Warning flags:**
- More than one **A** per decision = conflict, needs resolution
- Stakeholder with no **R** anywhere = likely not needed in core team
```

---

### ARTIFACT 3: Escalation Tree

```markdown
# Escalation Tree - [Product Name]

> Who resolves what when the team cannot agree.

---

## Escalation levels

### Level 1 - Operational decisions (within 24h)
**Decision owner:** [PM / Tech Lead]
**Types:** Scope details, technical implementation choices, daily priorities

### Level 2 - Strategic decisions (within 72h)
**Decision owner:** [PM + Leadership]
**Types:** MVP scope changes, timeline shifts, resource allocation, tech stack changes

### Level 3 - Critical / Escalated (ASAP)
**Decision owner:** [CEO / Founder / Board]
**Types:** Phase Go/No-Go, budget overruns, legal / compliance blockers, pivot decisions

---

## Conflict resolution protocol

1. Team attempts async resolution (Slack thread, 24h window)
2. If unresolved → sync meeting (max 30 min, PM facilitates)
3. If still unresolved → escalate to Level 2
4. Document the decision (what, why, who decided) → log in project workspace

---

## Anticipated conflicts and resolution rules

| Conflict | Parties | Resolution rule / Decider |
|---|---|---|
| [Anticipated conflict 1, e.g. tech vs. business priority] | [Parties] | [Who decides, based on what] |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Stakeholder Map must cover:**
- [ ] All internal stakeholders identified with role and interest (CEO, CTO, CFO, PM, Tech Lead, UX, Marketing, Sales, Support, Legal, Compliance, DPO if personal data handled)
- [ ] All external stakeholders identified (customers, investors, partners, regulators, vendors, integration partners)
- [ ] Power/Interest matrix populated across all 4 quadrants
- [ ] Payer vs. end user distinction made explicitly (critical for B2B SaaS)
- [ ] For AI products: who owns AI ethics, bias, and model decision accountability

**RACI Matrix must cover:**
- [ ] Decision authority over product scope - one owner
- [ ] Decision authority over tech stack - one owner
- [ ] Decision authority for design approval - one owner
- [ ] Final say on Go/No-Go at each phase gate - one owner
- [ ] Each key decision has exactly one Accountable
- [ ] For AI/data products: who owns data strategy and model decisions

**Escalation Tree must cover:**
- [ ] Who can block the project (and mitigation per blocker)
- [ ] Escalation path defined with time limits per level
- [ ] Conflict resolution protocol (async first, then sync, then escalate)
- [ ] Anticipated conflicts identified with resolution rules

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-1-foundation/stakeholder-map.md
pureinn-workspace/[project-slug]/artifacts/phase-1-foundation/raci-matrix.md
pureinn-workspace/[project-slug]/artifacts/phase-1-foundation/escalation-tree.md
```
