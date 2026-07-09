# pm-business-rule-critical

> JIT helper - add a single Critical priority hard invariant to the business rules register

**Phase:** 6 - JIT Delivery (during or after pm-feature-design)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.0.0  
**Triggers:** critical invariants, hard constraints, financial integrity rules, legal constraints, non-negotiable rules

---

## When to use

During `pm-feature-design` when the JIT discovery reveals a missing hard invariant that must be captured before build. Or standalone when a business decision introduces a new hard constraint.

**This skill is for rules that:**
- Violation causes financial loss, legal exposure, or irreversible system damage
- Must hold in ALL circumstances - no exceptions, no admin overrides
- Breaching them is a system failure, not a policy deviation

**Choose a different helper when:**
- Rule can have exceptions or context-dependent variations → `pm-business-rule-core`
- Rule stems from a regulatory or policy requirement → `pm-business-rule-governance`
- Logic is multi-condition (matrix) → `pm-decision-model`

---

## What it produces

A single Critical rule entry appended to `domain/business_rules.md` (Live Register 2):

```
BR-[DOMAIN]-[NUMBER]: [Rule name]
Priority: Critical
Status: Final
Domain: [domain]
Description: [precise, unambiguous invariant statement]
Exceptions: NONE - this is a hard invariant
Enforcement point: [service method / DB constraint / infrastructure-level guard]
Violation consequence: [financial / legal / data integrity - specific impact]
```

---

## How to invoke

```bash
/pm-business-rule-critical                 # interactive - asks for rule details
/pm-business-rule-critical --agent         # autonomous draft, requires review
```

Can also be called from within `pm-feature-design` when a critical invariant surfaces during discovery interrogation.

---

## Dependencies

**Required:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist
- `pm-entity-registry` - entity and lifecycle context for scoping the rule correctly

**Related skills:** `pm-business-rules-library`, `pm-entity-registry`, `pm-feature-design`

---

## Three JIT rule helpers compared

| Helper | Priority | Exceptions | Violation consequence | Use for |
|---|---|---|---|---|
| `pm-business-rule-core` | High / Medium | Yes | Quality / fairness degradation | Pricing, SLA, matching, fulfillment logic |
| `pm-business-rule-critical` | Critical | **None** | Financial or legal harm | Financial invariants, safety constraints |
| `pm-business-rule-governance` | High / Medium | Sometimes | Compliance breach | Regulatory, policy, audit requirements |
