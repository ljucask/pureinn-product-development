---
name: pm-business-rules-library
description: Build the Business Rules Library and Decision Models Matrix - Live Registers 2 and 3 of 4 in the FDD+SDD framework. Centralizes all business rules with unique IDs (BR-XXX-001) and decision tables into /domain/business_rules.md and /domain/decision_models.md. Replaces pm-brd in the new FDD+SDD architecture. Phase 4-5 skill - initial draft at Phase 5, enriched JIT in Phase 6 per feature.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: business rules, decision models, business rules library, BR-ID, rule catalog, Phase 4, Phase 5
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-entity-registry, pm-features-list, pm-feature-design
---

# PM - Business Rules Library

## What this skill does

Builds **Live Registers 2 and 3 of 4**:
- `business_rules.md` - Business Rules Library: centralized catalog of non-negotiable rules with unique IDs
- `decision_models.md` - Decision Models Matrix: decision tables and logic matrices for complex conditions

These registers replace the BRD as standalone documents. Business rules are no longer buried in a per-Feature-Set spec document - they live in a shared, versioned catalog that all Feature Cards reference by ID.

**What belongs here:**
- Corporate policies that apply across features (e.g., payment release rules)
- Compliance and regulatory requirements (GDPR, tax, data retention)
- Security and authorization rules
- Business logic that applies to multiple features or Feature Sets
- Decision tables with multiple conditions and outcomes

**What does NOT belong here:**
- Feature-specific implementation details (those are in Feature Cards)
- API contracts or payloads (ADRs)
- UI/UX rules (design docs)
- Technical architecture decisions (ADRs)

**JIT enrichment:** Rules are added in two stages:
1. Draft (Phase 5) - known constraints, compliance rules, high-level policies captured as raw text
2. JIT finalization (Phase 6, pm-feature-design) - exact mathematical formulas, guard conditions, and decision matrices finalized just before the feature that uses them is built

---

## Dependencies

**Required before running:**
- `pm-entity-registry` - entities define the scope of rules (which entity does each rule apply to)
- `pm-prd` - Business Capabilities section reveals key business logic and compliance requirements

**Produces artifacts used by:**
- `pm-features-list` - features reference rules by ID in feature_list.md
- `pm-feature-design` (JIT) - Phase 6 finalizes rule details and adds guard conditions to entities.md
- `pm-feature-card` - Section 1 (Biznis Mantinely) references BR-IDs and TBL-IDs
- Build phase - Claude Code reads rules as source of truth for business logic implementation

---

## Step 0: Current state check + mode detection

Check for existing artifacts:
- `domain/business_rules.md`
- `domain/decision_models.md`

**Mode detection:**

| Condition | Mode | Behavior |
|---|---|---|
| Neither file exists | Create mode | Generate full registers from scratch |
| Files exist | Append mode | Add new domain rules, preserve existing |

**If append mode detected**, inform user with existing rule count and domain list, then use AskUserQuestion:
- Question 1: "Which domain/initiative is being added, and what domain code? (e.g., ONB for onboarding)" (free text)
- Question 2: "Input source for business constraints?" with options:
  - Option A: "Initiative PRD at initiatives/[slug]/prd.md - Business Capabilities section (Recommended)"
  - Option B: "Paste constraints and regulatory requirements directly"

Also check: does entities.md exist and include the new domain entities? Rules need entity context.

Look for: rules without unique IDs (cannot be referenced), rules with implementation details (those belong in Feature Cards), duplicate rules under different names, missing compliance rules for regulated domains.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs for the Business Rules Library and Decision Models Matrix.

1. KNOWN CONSTRAINTS
   What are the hard business rules you already know?
   Examples: "Payment must never be released without a confirmed delivery",
             "Users must verify email before placing first order",
             "Discounts cannot be stacked"
   [list or "extract from PRD"]

2. REGULATORY CONTEXT
   What regulatory requirements apply?
   Examples: GDPR, PSD2, SOX, HIPAA, local tax law, industry-specific rules
   [list or "extract from Domain Analysis"]

3. DECISION LOGIC
   Are there any conditions with multiple inputs that produce different outputs?
   Examples: pricing tiers, discount calculation, risk scoring, eligibility rules
   [describe or "none yet"]

4. EXISTING DOMAIN CONTEXT
   Is entities.md in context? (required for entity mapping in rules)
   [confirm or paste]

5. ENRICHMENT MODE
   A) Draft mode - capture known rules, mark complex logic as TBD (Phase 5 init)
   B) JIT mode - finalize a specific rule for an in-progress feature (Phase 6 enrichment)
      If B: which rule ID and which feature? [specify]
```

---

## Step 2: Generate artifacts

Before generating:
1. Assign IDs using the pattern: `BR-[DOMAIN]-[NUMBER]` (e.g., BR-PAY-001, BR-ORD-002, BR-REG-001)
   - Domain codes: PAY (payment), ORD (order), USR (user/auth), REG (regulatory/compliance), DISC (discount/pricing), INV (inventory), etc.
2. For decision tables: assign IDs using: `TBL-[DOMAIN]-[NUMBER]` (e.g., TBL-DISC-01, TBL-RISK-01)
3. In draft mode: formulas and exact conditions can be TBD - capture the intent and apply domain clearly
4. Every rule must map to at least one entity from entities.md

Generate in English.

---

### ARTIFACT 1: Business Rules Library

Save to: `pureinn-workspace/[project-slug]/domain/business_rules.md`

```markdown
# Business Rules Library
# Live Register 2 of 4 - FDD+SDD Framework

> **Product:** [Product Name]
> **Version:** 1.0
> **Last updated:** [date]
> **Maintained by:** pm-business-rules-library (init) + pm-feature-design (JIT enrichment)

---

> **How to read this register:**
> - Rules are referenced by ID (BR-XXX-001) in Feature Cards and entities.md
> - Status: Draft = intent captured, formula TBD | Final = complete, used in build
> - Priority: Critical = blocking feature build | High = must address before launch | Medium = address before scale

---

## Payment Rules

### BR-PAY-001: [Rule Name]
**Category:** Payment  
**Affected entity:** Payment (entities.md#payment)  
**Priority:** Critical  
**Status:** Draft / Final  

**Rule:**  
[Description of the rule in business language. No implementation details.]  
Example: "Payment must not be released to the provider until the Order transitions to Confirmed state."

**Formula/Condition:**  
[Exact mathematical formula or logical condition. Mark as TBD in draft mode.]  
Example: `release_payment = true ONLY IF order.status == Confirmed AND delivery.confirmed == true`

**Applies to features:** [FEAT-XXX-001, FEAT-XXX-002 - filled as features are designed]  
**Exceptions:** [List known exceptions, or "None"]  
**Source:** [PRD section / regulatory requirement / business decision]

---

### BR-PAY-002: [Rule Name]

[same structure]

---

## Order Rules

### BR-ORD-001: [Rule Name]

[same structure]

---

## Regulatory / Compliance Rules

### BR-REG-001: [Rule Name]
**Category:** Compliance  
**Regulation:** [GDPR / PSD2 / local tax law]  
**Affected entity:** [Entity name]  
**Priority:** Critical  
**Status:** Draft  

**Rule:**  
[Compliance requirement in business language]

**Data retention / action required:**  
[What must be stored, deleted, or reported and when]

**Applies to features:** [TBD - filled JIT]  
**Source:** [Regulation name + article if known]

---

## User / Authorization Rules

### BR-USR-001: [Rule Name]

[same structure]

---

## [Domain] Rules

[additional domain sections as needed]

---

## Rule Coverage Map

| Rule ID | Rule Name | Status | Used in Features |
|---|---|---|---|
| BR-PAY-001 | [Name] | Draft / Final | [FEAT-IDs - filled JIT] |
| BR-ORD-001 | [Name] | Draft | TBD |

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | [date] | Initial draft from PRD + Domain Analysis | Phase 5 init |
| 1.1 | [date] | BR-PAY-001 finalized | pm-feature-design FEAT-ORD-012 |
```

---

### ARTIFACT 2: Decision Models Matrix

Save to: `pureinn-workspace/[project-slug]/domain/decision_models.md`

```markdown
# Decision Models Matrix
# Live Register 3 of 4 - FDD+SDD Framework

> **Product:** [Product Name]
> **Version:** 1.0
> **Last updated:** [date]
> **Maintained by:** pm-business-rules-library (init) + pm-feature-design (JIT enrichment)

---

> **How to read this register:**
> - Decision tables define outputs for all combinations of input conditions
> - Used by Claude Code to generate unit tests covering all edge cases
> - Referenced in Feature Cards Section 1 (Biznis Mantinely) by TBL-ID
> - Status: Draft = structure defined, values TBD | Final = complete, used in build

---

## TBL-DISC-01: [Decision Table Name]
**Domain:** Discount / Pricing  
**Used by rule:** BR-DISC-001  
**Affected entity:** Order (entities.md#order)  
**Status:** Draft  
**Used in features:** [FEAT-IDs - filled JIT]

| Customer Tier | Order Value | Promo Code | Discount % | Notes |
|---|---|---|---|---|
| Gold | > €100 | None | 15% | |
| Gold | > €100 | EXTRA10 | 20% | Cannot exceed 20% max |
| Gold | <= €100 | Any | 10% | |
| Silver | > €100 | None | 10% | |
| Silver | <= €100 | Any | 5% | |
| Basic | Any | None | 0% | |
| Basic | Any | PROMO5 | 5% | |

**Edge cases:**
- Multiple promo codes: [only first valid code applies / not allowed]
- Expired promo code: [ignored / error returned]
- Negative result: [impossible by rule - discount cannot exceed order value]

---

## TBL-RISK-01: [Decision Table Name]

[same structure]

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | [date] | Initial structure | Phase 5 init |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Business Rules Library:**
- [ ] Every rule has a unique ID (BR-[DOMAIN]-[NUMBER])
- [ ] Every rule maps to at least one entity from entities.md
- [ ] Rules are in business language - no implementation details
- [ ] Compliance rules are separated by regulation
- [ ] Priority and status set per rule
- [ ] No duplicate rules under different names
- [ ] Coverage map includes all rules

**Decision Models Matrix:**
- [ ] Every table has a unique ID (TBL-[DOMAIN]-[NUMBER])
- [ ] All input condition combinations covered (no missing rows)
- [ ] Edge cases explicitly listed
- [ ] Tables link back to the BR-ID they support
- [ ] Status set per table

**JIT mode completeness:**
- [ ] Formula/condition is fully specified (not TBD)
- [ ] All edge cases in the table have defined outputs
- [ ] Status updated from Draft to Final

---

## Save to

**Create mode (first run):**
```
pureinn-workspace/[project-slug]/domain/business_rules.md
pureinn-workspace/[project-slug]/domain/decision_models.md
```
State update → `state.json`: set `registers.business_rules_initialized` and `registers.decision_models_initialized` to `true`.

**Append mode (new domain/initiative):**
- Open existing `domain/business_rules.md`
- Add new domain section with `## [Domain] Rules (BR-[DOMAIN]-*)` header
- Append new BR-[DOMAIN]-* rules under that section
- Update the Changelog at bottom of file
- Same pattern for `domain/decision_models.md` if new decision tables are added
- Do NOT modify existing rule IDs, rule text, or status of existing rules

**Append checklist:**
- [ ] Existing rules preserved exactly (ID, text, status unchanged)
- [ ] New domain section added with clear domain header
- [ ] No ID collisions (new domain code is distinct: BR-ONB-* vs. existing BR-PAY-*, BR-ORD-*)
- [ ] Changelog in both files updated

---

## Notion push

After saving local files, push to Notion DBs.

### Business Rules DB

1. Read `pureinn-variables.md` key `"Business Rules"` → get DB URL
2. If blank: skip, continue
3. Call `mcp__claude_ai_Notion__notion-fetch` → extract `data_source_id`, cache in `state.json notion_ids.business_rules`
4. From notion-fetch `<templates>` section: find template named `"A — Critical / Hard Business Invariant (Business Rule)"`, `"B — Core Business Rule (Business Rule)"`, or `"C — Governance / Policy / UX Rule (Business Rule)"` - match by rule Category
5. For each rule in `business_rules.md`, call `mcp__claude_ai_Notion__notion-create-pages` with both `properties` AND `content`. Do NOT use `template_id` - provide content directly.

```
properties:
  Name: [Rule name]
  Rule ID: BR-[DOMAIN]-[NUMBER]
  Category: [A / B / C category]
  Domain (BLD): [Domain name]
  Description: [Rule description]
  Priority: [Critical / High / Medium / Low]
  Affecteed Entity: [Entity name(s)]

content:
  ## [Rule Name]

  **ID:** BR-[DOMAIN]-[NUMBER]
  **Category:** [A / B / C]
  **Status:** [Draft / Final]

  ## Rule Definition

  [Full rule text from business_rules.md]

  ## Affected Entities

  [Entity names and how they are affected]

  ## Enforcement

  [When and how this rule is enforced]
```
**Append mode:** Only create entries for newly added rules. Do NOT update existing entries.

### Decision Models DB

1. Read `pureinn-variables.md` key `"Decision Models"` → get DB URL
2. If blank: skip, continue
3. Call `mcp__claude_ai_Notion__notion-fetch` → extract `data_source_id`, cache in `state.json notion_ids.decision_models`
4. From notion-fetch `<templates>` section: find template matching the model type (TBL/TRE/SCR)
5. For each decision table in `decision_models.md`, call `mcp__claude_ai_Notion__notion-create-pages` with both `properties` AND `content`. Do NOT use `template_id` - provide content directly.

```
properties:
  Name: [Decision model name]
  userDefined:ID: TBL-[DOMAIN]-[NUMBER]
  Type: [TBL / TRE / SCR]
  Domain: [[Domain name]]
  What is being decided: [Decision description]
  Uses Business Rules: [BR-IDs]

content:
  ## [Decision Model Name]

  **ID:** TBL-[DOMAIN]-[NUMBER]
  **Type:** [Table / Tree / Scoring]

  ## What is being decided

  [Decision description from decision_models.md]

  ## Decision Table / Logic

  [Full table or logic from decision_models.md]

  ## References

  **Business Rules:** [BR-IDs]
  **Used in process:** [Process names]
```

After push: report counts (rules pushed, decision models pushed, errors).
- [ ] New rules cross-reference existing entities from entities.md (append mode entities must exist)
