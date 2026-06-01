---
name: pm-business-rule-critical
description: Define a RULE-A - Critical / Hard Business Invariant. Non-negotiable constraints that protect financial integrity, legal rights, or system consistency. Output is a single structured rule entry ready to add to the BRD Rules Library.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: critical invariants, RULE-A, non-negotiable rules, hard constraints
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-brd, pm-business-rule-core, pm-business-rule-governance, pm-fsd
---

# PM - Business Rule: RULE-A (Critical Invariant)

## What this skill does

Defines a single RULE-A entry - a Critical / Hard Business Invariant - for the BRD Rules Library.

RULE-A rules are **non-negotiable system constraints**. They define what the system MUST or MUST NEVER do to protect:
- Financial integrity (money cannot be lost, double-paid, or released incorrectly)
- Legal rights (user data, contractual obligations, regulatory compliance)
- System consistency (data cannot be left in a corrupt or unrecoverable state)

A rule belongs in RULE-A when:
- Violation causes financial loss, legal exposure, or irreversible damage
- It must hold in ALL circumstances - no exceptions, no admin overrides
- Breaching it is a system failure, not a policy deviation

If the rule has exceptions or context-dependent variations → it belongs in RULE-B, not RULE-A.

---

## Dependencies

**Required before running:**
- `pm-brd` - rules are added to the BRD Rules Library. BRD skeleton must exist.
- `pm-domain-model` - entity and lifecycle context needed to scope the rule correctly

**Produces artifacts used by:**
- `pm-fsd` - FSD references rule IDs when applying them in execution flows
- Phase 7 build - developers implement invariant enforcement

---

## Step 0: Current state check

Check for existing artifacts:
- BRD Rules Library (RULE-A section)

List existing RULE-A entries and their IDs. Identify the next available ID (RULE-A-XXX).

Check if a similar invariant already exists - prevent duplicates or conflicting definitions.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs to define a RULE-A - Critical Invariant.

1. WHAT IS THE RULE?
   Describe the constraint in plain language.
   (e.g., "Payment must never be released to the host without a delivery confirmation",
    "A booking cannot be confirmed if the listing is not in Active state",
    "User personal data must be fully deleted within 30 days of an erasure request")

2. WHAT DOES IT PROTECT?
   What would happen if this rule was violated?
   (financial loss / legal exposure / data corruption / safety risk)

3. SCOPE
   Which entities and lifecycles does this invariant affect?
   At what point in the flow must it be enforced?

4. ENFORCEMENT MECHANISM
   How should the system enforce it?
   (block the action / freeze the record / trigger incident alert / require manual review)

5. EDGE CASES
   Are there any known edge cases where this rule is tested?
   (e.g., concurrent requests, race conditions, admin override attempts)
   What should happen in those cases?

6. REGULATORY BASIS (if applicable)
   Is this rule required by regulation? (GDPR, PSD2, local law, financial regulation)
```

---

## Step 2: Generate rule entry

Generate in English. Output is a formatted rule block ready to paste into the BRD Rules Library.

---

### OUTPUT: RULE-A Entry

```markdown
## RULE-A-[ID] - [Canonical Rule Name]

**Category:** A - Critical / Hard Business Invariant
**Status:** [Draft / Approved]
**Added:** [date]
**Applies to Feature Sets:** [FS-IDs where this rule is enforced]

---

### Intent

[One sentence: what this rule protects and why it must exist.]

Protection of: [Financial integrity / Legal rights / Data consistency / System integrity]

---

### Scope

- **Entities:** [ENT-XXX Name, ENT-XXX Name]
- **Lifecycles:** [Which state machine this applies to]
- **Trigger point:** [At which step / transition / action this invariant is checked]

---

### Invariant Statement

The precise formulation. Must be unambiguous.

> "The system MUST NOT [X]."
> "The system MUST [Y] before [Z]."

---

### Enforcement

**Mechanism:** [Block action / Freeze record / Trigger incident / Require manual review]

**On violation attempt:**
1. [What the system does - specific actions, not vague "handle it"]
2. [Who is notified - actor, ops team, alert system]
3. [What state the affected entities are left in]

---

### Edge Cases

| Scenario | Handling |
|---|---|
| [Race condition / concurrent request] | [How system detects and handles] |
| [Admin attempts to override] | [System blocks - no exceptions for RULE-A] |
| [External system failure mid-transaction] | [Rollback / compensation approach] |

---

### Regulatory Basis (if applicable)

[GDPR Article X / PSD2 / Local law / Financial regulation / None]

---

### Violation Severity

**Impact if breached:** [What specifically would happen - financial, legal, data]
**Detection:** [How would a violation be detected - audit log, alert, customer complaint]
**Recovery:** [Is recovery possible? If yes, how? If no, what is the consequence?]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**RULE-A qualification:**
- [ ] Rule protects: financial integrity, legal rights, data consistency, or system integrity
- [ ] No exceptions exist (if exceptions exist → should be RULE-B)
- [ ] Violation causes irreversible harm or legal exposure (not just degraded quality)

**Rule entry completeness:**
- [ ] Intent: one sentence, clear protection statement
- [ ] Invariant: precise "MUST NOT" or "MUST" formulation - not vague
- [ ] Scope: entities and trigger point specific
- [ ] Enforcement: mechanism named, violation handling step-by-step
- [ ] Edge cases: at least one concurrent/race condition scenario addressed
- [ ] Violation severity: impact, detection, and recoverability assessed

**For SaaS/AI products:**
- [ ] Multi-tenant isolation: "Tenant A MUST NOT access Tenant B's data" is RULE-A
- [ ] Payment invariants: double-charge, failed refund, incorrect payout are RULE-A
- [ ] Data deletion: GDPR erasure within required timeframe is RULE-A (legal obligation)
- [ ] AI output: if AI makes a financial or legal decision without human review → RULE-A if unacceptable

## Save to

Add this rule entry to the relevant BRD file:
```
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-brd.md
```
Or to the BRD skeleton if adding before Phase 6:
```
pureinn-workspace/[project-slug]/artifacts/phase-4-domain/brd-skeleton.md
```
