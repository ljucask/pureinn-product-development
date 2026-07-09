# pm-business-rule-core

> JIT helper - add a single High priority operational rule to the business rules register

**Phase:** 6 - JIT Delivery (during or after pm-feature-design)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.0.0  
**Triggers:** business rules, operational rules, pricing rules, SLA rules, fulfillment rules, matching logic

---

## When to use

During `pm-feature-design` when the JIT discovery reveals business logic that should be centralized in the register. Or standalone when operational rules need to be formalized before a feature enters build.

**This skill is for rules that:**
- Govern regular system behavior in a specific domain (matching, pricing, trust, fulfillment, SLA)
- Can have exceptions or context-dependent variations
- Violating them degrades quality or fairness but does NOT cause immediate irreversible damage

**Choose a different helper when:**
- Rule has no exceptions AND violation causes financial or legal harm → `pm-business-rule-critical`
- Rule is compliance, regulatory, or policy-based → `pm-business-rule-governance`
- Logic has multiple input conditions producing different outputs → `pm-decision-model`

---

## What it produces

A single new rule entry appended to `domain/business_rules.md` (Live Register 2):

```
BR-[DOMAIN]-[NUMBER]: [Rule name]
Priority: High | Medium
Status: Final
Domain: [domain]
Description: [precise, unambiguous rule statement]
Exceptions: [list or "none"]
Enforcement point: [Service method / middleware / DB constraint]
```

---

## How to invoke

```bash
/pm-business-rule-core                     # interactive - asks for rule details
/pm-business-rule-core --agent             # autonomous draft, requires review
```

Can also be called from within `pm-feature-design` when a new rule surfaces during discovery interrogation.

---

## Dependencies

**Required:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist (initialized in Phase 4)
- `pm-entity-registry` - entity context for scoping the rule

**Produces for:**
- `pm-feature-design` - JIT design reads BR-IDs when defining Feature Card Section 1
- Build phase - developers implement the rule

**Related skills:** `pm-business-rules-library`, `pm-decision-model`, `pm-entity-registry`, `pm-feature-design`

---

## Three JIT rule helpers compared

| Helper | Priority | Exceptions | Violation consequence | Use for |
|---|---|---|---|---|
| `pm-business-rule-core` | High / Medium | Yes | Quality / fairness degradation | Pricing, SLA, matching, fulfillment logic |
| `pm-business-rule-critical` | Critical | None | Financial or legal harm | Financial invariants, safety constraints |
| `pm-business-rule-governance` | High / Medium | Sometimes | Compliance breach | Regulatory, policy, audit requirements |
