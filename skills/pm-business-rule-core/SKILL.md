---
name: pm-business-rule-core
description: JIT helper - add a single High priority operational rule to domain/business_rules.md. For standard business logic that governs normal system behavior (matching, pricing, SLAs, fulfillment). May have exceptions or context-dependent variations. Use during pm-feature-design or standalone when operational logic needs to be formalized.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: business rules, operational rules, pricing rules, SLA rules, fulfillment rules, matching logic
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-business-rules-library, pm-decision-model, pm-entity-registry, pm-feature-design
---

# PM - Business Rule: Core Operational Rule (JIT Helper)

## What this skill does

Adds a single **High or Medium priority operational rule** to `domain/business_rules.md`.

A rule belongs here when:
- It governs regular system behavior in a specific domain (matching, pricing, trust, fulfillment, SLA)
- It CAN have exceptions or context-dependent variations (unlike Critical invariants)
- Violating it degrades quality or fairness but does not cause immediate irreversible damage
- It is referenced by feature designs when implementing the business logic

If the rule has NO exceptions and violation causes financial/legal harm → use `pm-business-rule-critical`.
If it is a compliance, regulatory, or policy rule → use `pm-business-rule-governance`.

**When to run:** During `pm-feature-design` when the JIT design reveals business logic that should be centralized. Or standalone when operational rules need to be formalized before a feature enters build.

---

## Dependencies

**Required before running:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist (initialized in Phase 4)
- `pm-entity-registry` - entity context for scoping the rule

**Produces artifacts used by:**
- `pm-feature-design` - JIT design reads BR-IDs when defining Feature Card Section 1 (Biznis Mantinely)
- Build phase - developers implement the business logic

---

## Step 0: Current state check

Read `domain/business_rules.md`.

List existing rules in the relevant domain. Identify the next available BR-[DOMAIN]-NNN.

Check if a similar rule already exists. Check if this should actually be Critical (no exceptions → pm-business-rule-critical) or a decision table (multiple conditions → `/pm-decision-model`).

Use AskUserQuestion tool to confirm scope and mode before proceeding.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Use AskUserQuestion for structured choices. Gather via text prompt:

```
I need inputs to define a Core Operational Rule for business_rules.md.

1. WHAT IS THE RULE?
   Describe the business logic in plain language.
   (e.g., "Hosts have 48 hours to respond to a booking request before it auto-expires",
    "Search results are ranked by availability, rating, and price competitiveness",
    "A booking can be cancelled penalty-free within 24 hours of confirmation")

2. WHICH DOMAIN?
   Which business domain does this rule belong to?
   (PAY / ORD / USR / BKG / LST / SRC / SLA / DISC / Other: [specify])

3. LOGIC
   Can you express it as "If [condition], then [outcome]"?
   What are the inputs? What does it produce or decide?
   (If multiple conditions produce different outputs → this needs a decision table, not a single rule)

4. EDGE CASES AND EXCEPTIONS
   Are there known exceptions?
   (e.g., "except for premium hosts who have a 72-hour window",
    "unless the listing has instant booking enabled")

5. PRIORITY
   High - affects core user experience, must be addressed before launch
   Medium - operational optimization, can be added before scale
```

---

## Step 2: Generate rule entry

Generate the BR-[DOMAIN]-NNN ID as the next available number in that domain section of business_rules.md.

Generate in English. If exceptions exist, document them explicitly.
If the logic has multiple input conditions producing different outputs → also note that a decision table (TBL-[DOMAIN]-NNN) should be added to decision_models.md.

---

### OUTPUT: business_rules.md entry

```markdown
### BR-[DOMAIN]-[NNN]: [Rule Name]
**Category:** [Matching / Pricing / SLA / Fulfillment / Booking / Cancellation / Other]
**Affected entity:** [Entity name] (entities.md#[entity])
**Priority:** High / Medium
**Status:** Draft / Final

**Rule:**
[Description of the rule in business language. No implementation details.]
Example: "Hosts have 48 hours to respond to a booking request. If no response, the request expires automatically."

**Formula/Condition:**
[Exact logical condition. Mark TBD if not yet finalized - will be finalized JIT by pm-feature-design.]
Example: `request.status = Expired IF (now - request.created_at) > 48h AND host.response_received == false`

**Exceptions:**
[List known exceptions, or "None"]
Example: "Premium hosts (host.tier == Premium) have a 72-hour window instead of 48."

**Applies to features:** [TBD - filled JIT by pm-feature-design]
**Source:** [Business decision / operational requirement / market standard]
```

---

## Save to

Append the new rule under the correct domain section in:
```
pureinn-workspace/[project-slug]/domain/business_rules.md
```

If the domain section does not yet exist, create it as:
```
## [Domain] Rules

### BR-[DOMAIN]-[NNN]: [Rule Name]
```

If the rule logic implies a decision table, note it:
```
> Note: This rule has multiple condition combinations. Add a decision table TBL-[DOMAIN]-NN
> to decision_models.md via /pm-decision-model.
```

Update the Rule Coverage Map. Update the Changelog.

---

## Handoff

**Čo si teraz má:** Jedno High-priority operačné pravidlo pridané do `business_rules.md` (nový BR-ID).

**Ďalší krok:** Späť do JIT cyklu - `/pm-feature-design [FEAT-ID]` (ak pravidlo vzniklo pri dizajne feature) alebo `/pm-stripe`.

**Môžeš preskočiť ak:** Pravidlo už v registri bolo - duplicitu nepridávaj.
