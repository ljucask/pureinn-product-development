---
name: pm-business-rule-core
description: Define a RULE-B - Core Business Rule. Governs standard system behavior - matching logic, pricing, trust, fulfillment, SLAs. May have exceptions. Output is a single structured rule entry ready to add to the BRD Rules Library.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: business rules, RULE-B, core rules, operational rules
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-brd, pm-business-rule-critical, pm-business-rule-governance, pm-fsd
---

# PM - Business Rule: RULE-B (Core Business Rule)

## What this skill does

Defines a single RULE-B entry - a Core Business Rule - for the BRD Rules Library.

RULE-B rules define **how the system optimizes and governs standard operations**. They encode the core product logic - the rules that make the product work the way it's supposed to in normal conditions.

A rule belongs in RULE-B when:
- It governs regular system behavior in a specific domain (matching, pricing, trust, fulfillment, SLA)
- It can have exceptions or context-dependent variations (unlike RULE-A)
- Violating it degrades quality or fairness but does not cause immediate irreversible damage
- It is referenced by FSD flows and other rules

Typical RULE-B domains: matching/search ranking, pricing and discount logic, trust and fraud signals, fulfillment windows and SLAs, booking policies, cancellation logic.

---

## Dependencies

**Required before running:**
- `pm-brd` - rules are added to the BRD Rules Library. BRD skeleton must exist.
- `pm-domain-model` - entity context needed to scope the rule correctly

**Produces artifacts used by:**
- `pm-fsd` - FSD references rule IDs when applying business logic in flows
- `pm-business-rule-critical` - RULE-B rules may reference RULE-A invariants they interact with
- Phase 7 build - developers implement the rule logic

---

## Step 0: Current state check

Check for existing artifacts:
- BRD Rules Library (RULE-B section)

List existing RULE-B entries and their IDs. Identify the next available ID.

Check if a similar rule exists - prevent duplicates. Check if this is really RULE-A (no exceptions possible) or RULE-C (governance/policy, not operational logic).

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs to define a RULE-B - Core Business Rule.

1. WHAT IS THE RULE?
   Describe the business logic in plain language.
   (e.g., "Hosts have 48 hours to respond to a booking request before it auto-expires",
    "Search results are ranked by availability, rating, and price competitiveness",
    "A booking can be cancelled penalty-free within 24 hours of confirmation")

2. WHICH DOMAIN?
   Which business domain does this rule belong to?
   (Matching / Search ranking / Pricing / Trust / Fulfillment / SLA / Booking policy /
    Cancellation / Payouts / Notifications / Other: [describe])

3. LOGIC
   Can you express it as "If [condition], then [outcome]"?
   What are the inputs to the rule? What does it produce or decide?

4. EDGE CASES AND EXCEPTIONS
   Are there known exceptions?
   (e.g., "except for premium hosts who have a 72-hour window",
    "unless the listing has instant booking enabled",
    "except during a declared force majeure period")

5. RELATED RULES
   Does this rule depend on or interact with other rules?
   (e.g., "this rule is overridden by RULE-A-001 if payment is already captured")

6. BUSINESS IMPACT
   What happens in practice if this rule is consistently violated or broken?
   (quality degradation, unfairness, customer churn, revenue impact)
```

---

## Step 2: Generate rule entry

Generate in English. Output is a formatted rule block ready to paste into the BRD Rules Library.

---

### OUTPUT: RULE-B Entry

```markdown
## RULE-B-[ID] - [Canonical Rule Name]

**Category:** B - Core Business Rule
**Domain:** [Matching / Pricing / Trust / Fulfillment / SLA / Booking / Cancellation / Other]
**Status:** [Draft / Approved]
**Added:** [date]
**Applies to Feature Sets:** [FS-IDs where this rule is enforced]

---

### Intent

[1-2 sentences: what business problem this rule solves or optimizes. Why this behavior is correct.]

---

### Applies To

- **Entities:** [ENT-XXX Name, ENT-XXX Name]
- **Processes / Lifecycles:** [Which flows and state transitions this rule governs]

---

### Rule Logic

Human-language description of the rule. Precise enough to implement, readable by non-engineers.

> "If [condition], then [outcome / system action]."

**Parameters (if rule has configurable values):**

| Parameter | Default value | Who can change | Notes |
|---|---|---|---|
| [e.g., Response window] | [48 hours] | [Ops team via config] | [May vary by market] |

---

### Decision Table (if logic is multi-condition)

| Condition 1 | Condition 2 | Condition N | Outcome |
|---|---|---|---|
| [Value A] | [Value X] | [...] | [Result] |
| [Value B] | [Value Y] | [...] | [Result] |

---

### Edge Cases and Exceptions

| Scenario | Exception / Handling |
|---|---|
| [e.g., Instant booking enabled] | [Host approval step skipped - booking auto-confirms] |
| [e.g., Listing in dispute state] | [Response window suspended until dispute resolved] |
| [e.g., First-time host] | [Window extended to 72h - lower pressure on new hosts] |

---

### Related Rules

| Rule | Relationship |
|---|---|
| [RULE-A-XXX] | [This rule is subordinate to RULE-A-XXX - invariant takes precedence] |
| [RULE-B-XXX] | [This rule interacts with RULE-B-XXX in the following way: ...] |
| [RULE-C-XXX] | [This rule is implemented via policy RULE-C-XXX] |

---

### Business Impact

**Expected outcome when rule is followed:** [What good looks like]

**Degradation when rule is violated consistently:**
[What goes wrong over time - customer experience, fairness, revenue, trust]

**Metric to monitor:** [The metric that indicates this rule is working - e.g., "Host response rate > 90%"]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**RULE-B qualification:**
- [ ] Rule governs operational/optimization behavior (not a hard invariant → RULE-A)
- [ ] Rule is specific to a domain (matching, pricing, trust, fulfillment, SLA, etc.)
- [ ] Exceptions are possible and documented

**Rule entry completeness:**
- [ ] Intent: what it optimizes and why this behavior is correct
- [ ] Logic: "If / then" formulation clear enough to implement
- [ ] Parameters: configurable values identified with defaults
- [ ] Decision table included if logic has multiple conditions
- [ ] Edge cases: at least 2 known exception scenarios documented
- [ ] Related rules: interactions and precedence noted

**For SaaS/AI products:**
- [ ] AI ranking/scoring rules (search, recommendations) belong in RULE-B with explicit logic
- [ ] Rate limiting and quota rules belong in RULE-B (with RULE-A override for financial protection)
- [ ] Retry logic for AI API calls: belongs in RULE-B (max retries, backoff, fallback)
- [ ] Freemium limits (what free users can/cannot do) are RULE-B entries
- [ ] Subscription tier capability rules are RULE-B entries

## Save to

Add this rule entry to the relevant BRD file:
```
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-brd.md
```
