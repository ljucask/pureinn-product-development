# pm-business-rule-governance

> JIT helper - add a single Compliance or Policy rule to the business rules register

**Phase:** 6 - JIT Delivery (during or after pm-feature-design)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.0.0  
**Triggers:** governance rules, compliance rules, GDPR rules, policy rules, regulatory, data handling, admin constraints

---

## When to use

When `pm-privacy-requirements` or `pm-domain-analysis` surfaces a regulatory requirement that needs a formal BR-ID. Or during `pm-feature-design` when a compliance constraint is discovered that must be documented before the feature is built.

**This skill is for rules that:**
- Stem from a regulatory or legal requirement (GDPR, PSD2, ePrivacy, local tax law)
- Govern admin or ops behavior (what support agents can and cannot do)
- Define a data handling policy (retention, deletion, logging, consent)
- Enforce a UX behavioral standard required by law or company policy
- May have regional or partner-specific variations

**Choose a different helper when:**
- Rule has no exceptions AND violation causes financial/legal harm → `pm-business-rule-critical`
- Rule is standard operational logic with business exceptions → `pm-business-rule-core`

---

## What it produces

A single Compliance/Policy rule entry appended to `domain/business_rules.md` under the Regulatory/Compliance or User/Authorization section:

```
BR-[DOMAIN]-[NUMBER]: [Rule name]
Priority: High | Medium
Status: Final
Domain: [domain]
Regulatory basis: [GDPR Art. X / PSD2 / local law / company policy]
Description: [precise rule statement]
Exceptions: [regional or partner-specific variations, or "none"]
Enforcement point: [service layer / middleware / logging / consent mechanism]
Audit trail required: [yes / no]
```

---

## How to invoke

```bash
/pm-business-rule-governance               # interactive - asks for rule details
/pm-business-rule-governance --agent       # autonomous draft, requires review
```

---

## Dependencies

**Required:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist
- `pm-entity-registry` - entity context for scoping

**Related skills:** `pm-business-rules-library`, `pm-privacy-requirements`, `pm-domain-analysis`, `pm-feature-design`

---

## Three JIT rule helpers compared

| Helper | Priority | Exceptions | Violation consequence | Use for |
|---|---|---|---|---|
| `pm-business-rule-core` | High / Medium | Yes | Quality / fairness degradation | Pricing, SLA, matching, fulfillment logic |
| `pm-business-rule-critical` | Critical | None | Financial or legal harm | Financial invariants, safety constraints |
| `pm-business-rule-governance` | High / Medium | Sometimes | Compliance breach | **Regulatory, policy, audit requirements** |
