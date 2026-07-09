# pm-decision-model

> JIT helper - add a single decision table to the decision models register

**Phase:** 6 - JIT Delivery (during or after pm-feature-design)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** decision table, decision model, decision matrix, multi-condition logic, pricing matrix, eligibility matrix

---

## When to use

During `pm-feature-design` when the JIT design reveals multi-condition logic that should be centralized. Or standalone when a decision matrix needs to be formalized before a feature enters build.

**A decision table belongs here when:**
- Several input conditions combine to produce different outputs (not a single if/then)
- The logic is best read as a matrix - rows = condition combinations, columns = inputs + output
- Examples: discount tiers by customer level + order value + promo, eligibility by age + region + status, risk scoring by multiple signals, pricing matrix

**If the logic is a single condition → one output, it is a business rule, not a table:**
- Use `pm-business-rule-core`, `-critical`, or `-governance` instead

`pm-business-rule-core` routes here automatically when a rule it is defining turns out to have multiple condition combinations.

---

## What it produces

A single decision table entry appended to `domain/decision_models.md` (Live Register 3):

```
TBL-[DOMAIN]-[NUMBER]: [Table name]
Status: Final
Domain: [domain]
Used by rule: [BR-ID - the business rule this table elaborates, if applicable]

| Condition 1 | Condition 2 | ... | Output |
|---|---|---|---|
| value A     | value X     | ... | result 1 |
| value A     | value Y     | ... | result 2 |
| value B     | value X     | ... | result 3 |
```

The TBL-ID is then referenced in Feature Card Section 1 (Business Constraints) via `pm-feature-design`.

---

## How to invoke

```bash
/pm-decision-model                    # interactive - asks for table definition
/pm-decision-model --agent            # autonomous draft, requires review
```

---

## Dependencies

**Required:**
- `pm-business-rules-library` - `domain/decision_models.md` must exist (initialized in Phase 4)
- `pm-entity-registry` - entity context for scoping the table

**Recommended:**
- A related business rule (BR-ID) that the table elaborates - link it via "Used by rule"

**Produces for:**
- `pm-feature-design` - references TBL-ID in Feature Card Section 1
- Build phase - the table drives unit tests covering every condition combination

**Related skills:** `pm-business-rules-library`, `pm-business-rule-core`, `pm-feature-design`, `pm-entity-registry`

---

## Decision table vs. business rule

| | Business rule | Decision table |
|---|---|---|
| Structure | Single condition → outcome | Multiple conditions combined → outcome |
| Best read as | A rule statement | A matrix |
| Example | "Orders above €500 qualify for free shipping" | Discount by loyalty tier × order value × active promo code |
| Register | `business_rules.md` (R2) | `decision_models.md` (R3) |
| Skill | `pm-business-rule-*` | `pm-decision-model` |
