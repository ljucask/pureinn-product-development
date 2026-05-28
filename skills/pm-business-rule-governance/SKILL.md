---
name: pm-business-rule-governance
description: Define a RULE-C - Governance / Policy / UX Rule. Covers admin constraints, compliance requirements, UX behavioral rules, and operational policies. Output is a single structured rule entry ready to add to the BRD Rules Library.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: governance rules, RULE-C, policy rules, UX rules, compliance rules
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-brd, pm-business-rule-critical, pm-business-rule-core, pm-fsd
---

# PM - Business Rule: RULE-C (Governance / Policy / UX)

## What this skill does

Defines a single RULE-C entry - a Governance, Policy, or UX Rule - for the BRD Rules Library.

RULE-C rules define **policies, behavioral guidelines, and compliance constraints** that govern how actors interact with the system. They cover:
- Admin and ops actions (what support agents can and cannot do)
- Compliance requirements (data handling, regulatory obligations)
- UX behavioral rules (patterns the system must follow in user interactions)
- Operational procedures (SLAs, escalation policies, operational standards)

A rule belongs in RULE-C when:
- It governs human behavior within the system (admin, ops, user)
- It defines a policy or guideline, not a hard system constraint (hard constraints → RULE-A)
- It relates to compliance, data handling, UX patterns, or operational standards
- It may have regional or partner-specific variations

---

## Dependencies

**Required before running:**
- `pm-brd` - rules are added to the BRD Rules Library. BRD skeleton must exist.

**Recommended before running:**
- `pm-privacy-requirements` - GDPR and compliance requirements often become RULE-C entries
- `pm-domain-analysis` - regulatory requirements from Phase 2 may generate RULE-C entries

**Produces artifacts used by:**
- `pm-fsd` - FSD references rule IDs when implementing governance or compliance behavior
- Phase 7 build - admin and compliance features implement RULE-C logic

---

## Step 0: Current state check

Check for existing artifacts:
- BRD Rules Library (RULE-C section)

List existing RULE-C entries and their IDs. Identify the next available ID.

Check if this belongs in a different category: if violation causes irreversible harm → RULE-A. If it governs operational optimization → RULE-B. If it's a policy or guideline → RULE-C.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs to define a RULE-C - Governance / Policy / UX Rule.

1. WHAT IS THE RULE?
   Describe the policy or guideline in plain language.
   (e.g., "Support agents cannot access booking financial details without a dispute ticket",
    "Users must be shown a clear opt-out option for marketing emails in every email sent",
    "Personal data must not be included in system logs",
    "Admin actions on user accounts must be logged with the acting admin's ID and reason")

2. CONTEXT
   Which context does this rule apply to?
   a) Admin / Ops - constrains what support or operations team can do
   b) Compliance - regulatory or legal requirement (GDPR, PSD2, ePrivacy, local law)
   c) UX / Product - behavioral pattern the product must follow in user interactions
   d) Operational - procedure, SLA, or escalation policy

3. ACTORS
   Who is subject to this rule?
   (Admin, Support agent, Operations team, End user, System, Partner)

4. EXCEPTIONS
   Are there regional variations or time-bound exceptions?
   (e.g., "except in countries where local law requires longer retention",
    "except during onboarding within the first 7 days")

5. REGULATORY BASIS (if applicable)
   Does this rule have a legal basis?
   (GDPR Article, ePrivacy Directive, PSD2, local consumer protection law, other)

6. ENFORCEMENT
   How is compliance with this rule verified or enforced?
   (system blocks the action / audit log / periodic review / manual policy / training)
```

---

## Step 2: Generate rule entry

Generate in English. Output is a formatted rule block ready to paste into the BRD Rules Library.

---

### OUTPUT: RULE-C Entry

```markdown
## RULE-C-[ID] - [Canonical Rule Name]

**Category:** C - Governance / Policy / UX Rule
**Context:** [Admin / Compliance / UX / Operational]
**Status:** [Draft / Approved]
**Added:** [date]
**Applies to Feature Sets:** [FS-IDs where this rule is implemented or referenced]

---

### Policy Statement

One clear sentence defining the rule or guideline.

> "[Actor] must / must not / should always [action]."

---

### Context

| Dimension | Applies | Notes |
|---|---|---|
| Admin / Ops | [Yes / No] | [What admin action this governs] |
| Compliance | [Yes / No] | [Regulatory basis if applicable] |
| UX / Product | [Yes / No] | [What user-facing behavior this governs] |
| Operational | [Yes / No] | [What procedure or SLA this governs] |

---

### Actors Subject to This Rule

| Actor | How the rule applies to them |
|---|---|
| [Support agent] | [Cannot access financial data without a linked dispute ticket] |
| [Admin] | [Must log reason when modifying user account data] |
| [System] | [Must include opt-out link in every marketing email] |

---

### Implementation Requirements

What the system must do to enforce or enable compliance with this rule:

1. [e.g., "Audit log entry created for every admin action on a user record, including actor ID, timestamp, and reason"]
2. [e.g., "Marketing email template enforces presence of opt-out link - build step fails without it"]
3. [e.g., "Personal data fields excluded from logging middleware by default"]

---

### Exceptions

| Exception | Condition | Notes |
|---|---|---|
| [Regional variation] | [In Germany, retention period is X due to local tax law] | [Document source] |
| [Time-bound exception] | [During onboarding (first 7 days), simplified flow applies] | |
| [None] | This rule has no exceptions | |

---

### Regulatory Basis

| Regulation | Article / Section | Requirement |
|---|---|---|
| [GDPR] | [Art. 5(1)(c) - Data minimization] | [PII must not appear in logs] |
| [ePrivacy Directive] | [Art. 13] | [Marketing emails require opt-out] |
| [None - internal policy] | - | [Business policy, not regulatory] |

---

### Verification and Enforcement

**How compliance is verified:**
[Audit review / Automated test / System block / Periodic policy review / Training]

**Who is responsible for enforcement:**
[Engineering (system enforcement) / Ops team (procedural) / Legal (regulatory) / Product (UX)]

**Non-compliance consequence:**
[What happens if this rule is violated - regulatory fine / customer complaint / internal incident]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**RULE-C qualification:**
- [ ] Rule governs human behavior or policy (not hard system invariant → RULE-A)
- [ ] Rule is specific to governance, compliance, UX, or operations
- [ ] Policy statement is clear enough to implement and audit

**Rule entry completeness:**
- [ ] Policy statement: clear "[Actor] must/must not [action]"
- [ ] Context: which dimension(s) apply
- [ ] Actors: who is subject and how the rule applies to each
- [ ] Implementation requirements: what the system must do to enforce it
- [ ] Exceptions documented (or explicitly stated "none")
- [ ] Regulatory basis cited if applicable

**For SaaS/AI products:**
- [ ] Data minimization in logs (PII must not appear in system logs) → RULE-C (GDPR)
- [ ] AI transparency (users must know when AI is making a decision that affects them) → RULE-C
- [ ] Cookie consent UX (pre-checked boxes prohibited, granular controls required) → RULE-C (ePrivacy)
- [ ] Admin access audit (every admin action on user data must be logged) → RULE-C
- [ ] Marketing opt-out in every email → RULE-C (ePrivacy + CAN-SPAM)
- [ ] Data export format (machine-readable, GDPR Art. 20) → RULE-C
- [ ] Retention policy enforcement (automated deletion after stated period) → RULE-C + RULE-A if legal obligation

## Save to

Add this rule entry to the relevant BRD file:
```
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-brd.md
```
