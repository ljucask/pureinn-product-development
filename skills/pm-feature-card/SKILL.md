---
name: pm-feature-card
description: Create and manage Feature Cards for individual features (FEAT-ID). In the FDD+SDD framework, Feature Cards are the atomic delivery unit - one card per feature, living in /features/cards/. Cards are created as stubs by pm-features-list, populated in Sections 1-3 by pm-feature-design (JIT), and completed in Section 4 after build. This skill manages the card lifecycle and can create cards manually when needed.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: feature card, FEAT-ID, feature spec, feature lifecycle, cards
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-feature-design, pm-features-list, pm-stripe, pm-entity-registry
---

# PM - Feature Card

## What this skill does

Manages Feature Cards in the FDD+SDD framework. A Feature Card is the atomic delivery unit - one card per feature, progressing through a defined lifecycle from initial walkthrough to immutable post-build history.

**Card lifecycle:**

| Status | Meaning | Who sets it |
|---|---|---|
| `1_Backlog` | Stub created, feature defined | pm-features-list (auto) |
| `2_Spec_Done` | JIT design complete (Sections 1-3 populated) | pm-feature-design |
| `3_Ready_to_Build` | Human approved design | Human (Delivery Team) / Human solo confirm |
| `4_In_Build` | Build in progress | pm-stripe |
| `5_In_Review` | Code review in progress | Human / AI guardrail |
| `6_Shipped` | Complete - immutable history | pm-stripe after CI pass |

**This skill handles:**
- Creating stub Feature Cards manually (when not created by pm-features-list)
- Reviewing Feature Card completeness at any status
- Advancing status after human confirmation
- Creating the card template reference

**Section ownership:**
- Frontmatter: pm-features-list (init) + pm-mvp-scope (stripe assignment) + pm-feature-design (status updates)
- Section 1 (Biznis Mantinely): pm-feature-design
- Section 2 (Acceptance Criteria): pm-feature-design
- Section 3 (JIT Technical Design): pm-feature-design
- Section 4 (Realizacny Protokol): pm-stripe (after build)

---

## Dependencies

**Required before creating a stub:**
- Feature must exist in `features/feature_list.md`

**Required before Sections 1-3 are complete:**
- `pm-entity-registry` - entities.md must exist
- `pm-business-rules-library` - business_rules.md and decision_models.md must exist
- `pm-feature-design` - JIT design skill that populates Sections 1-3

**Produces artifacts used by:**
- `pm-feature-design` - reads stub, populates Sections 1-3
- Build skills - read completed Feature Card as implementation spec
- `pm-stripe` - Impact Analysis reads BR-IDs in Section 1

---

## Step 0: Current state check

Check for existing Feature Card at `/features/cards/[FEAT-ID].md`.

| Item | Status | Detail |
|---|---|---|
| Feature Card | [status from frontmatter] | [title] |
| Section 1 (Biznis Mantinely) | [populated / stub] | |
| Section 2 (Acceptance Criteria) | [populated / stub] | |
| Section 3 (JIT Technical Design) | [populated / stub] | |
| Section 4 (Realizacny Protokol) | [populated / pending] | |

**Verdict:** [One sentence - what stage the card is in, what is next]

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs (if creating manually)

Used when creating a card that was not auto-created by pm-features-list.

```
Creating Feature Card for: [FEAT-ID]

1. FEATURE REFERENCE
   Feature ID: [FEAT-ID]
   Feature title (FDD format): "[Action] [Result] [Object]"
   Feature Set: [FS-NN: Name]
   From feature_list.md: [confirm feature exists]

2. STRIPE ASSIGNMENT
   Assigned stripe: [stripe-name]
   Priority: [P1 / P2 / P3]
   Dependencies: [FEAT-IDs this depends on, or "none"]

3. PRD REFERENCE
   Which section of PRD covers this feature's business capability?
   [PRD.md#section or PRD_Domain.md#section]

4. FEATURE FLAG
   Flag name (format: domain.feature-name): [name]
   Default: OFF (mandatory in pureinn)
```

---

## Feature Card Template

This is the canonical template for all Feature Cards in the FDD+SDD framework.

```markdown
---
id: FEAT-[DOMAIN]-[NUMBER]
title: "[Action] [Result] [Object]"
status: 1_Backlog
stripe: [stripe-name]
feature_set: "FS-NN: [Feature Set name]"
actor: [User / Host / Admin / System]
owner: unassigned
priority: P1
prd_ref: /product/PRD.md#[section]
feature_flag: [domain.feature-name]
flag_default: off
---

# Feature Card: {{title}}

---

## 1. Biznis Mantinely (SDD Input)

*Populated by pm-feature-design (JIT). Links to live registers as source of truth.*

**Rules enforced in this feature:**

| Rule ID | Rule | Priority | Enforcement point |
|---|---|---|---|
| [BR-XXX-001](/domain/business_rules.md#br-xxx-001) | [Rule name: one-line summary] | [Critical/High/Medium] | [Service method / middleware / DB constraint] |

**Entity guard conditions (from entities.md):**

| Entity | Transition | Guard condition |
|---|---|---|
| [Entity Name](/domain/entities.md#entity-name) | [State before] → [State after] | [exact guard expression] |

**Decision model:** [TBL-XXX-01](/domain/decision_models.md#tbl-xxx-01) - [Table name, if applicable]

**What this feature does NOT do:**
- [explicit scope exclusion]

---

## 2. Acceptance Criteria

*Derived from register state + business rules by pm-feature-design. Used for human Black-box testing.*

### AC-01: [Happy Path Name]
- **Given** [precondition: entity state, actor]
- **When** [action]
- **Then** [observable outcome: state change, event emitted, user signal]
  - **And** [secondary outcome]

### AC-02: [Guard Failure Name]
- **Given** [precondition]
- **When** [invalid condition]
- **Then** [system blocks, entity unchanged, error signal]

### AC-03: Feature Flag OFF
- **Given** flag `[feature_flag]` is OFF
- **When** [same trigger as AC-01]
- **Then** [existing behavior unchanged / feature hidden]

---

## 3. JIT Technical Design (FDD Design)

*Populated by pm-feature-design just before build. Approved during Design Inspection.*

### Data flow and object interaction

```mermaid
sequenceDiagram
    %% Generated by pm-feature-design
    %% [FEAT-ID]: [title]
```

### Files to modify
- [TBD - populated by pm-feature-design]

---

## 4. Realizacny Protokol (Build Verification)

*Populated after successful build and Code Inspection. After 6_Shipped: immutable.*

- **Production code commits:**
  - `[feat: description](commit_hash_link)`

- **Test files:**
  - `tests/unit/[ServiceName]_[FEAT-ID]_spec.[ext]`

- **Feature flag OFF verification:** [yes / no]

- **Code Inspection:** [Approved by [reviewer] on YYYY-MM-DD / AI guardrail passed on YYYY-MM-DD]
```

---

## Notion push

**Runs after Feature Card Section 4 is complete (status: 6_Shipped).**

Read `pureinn-variables.md` key "Feature Backlog" → get DB URL. Find the existing Feature entry for this FEAT-ID.

Update the Feature entry via `notion-update-page`:

| Notion property | Value |
|---|---|
| `Status` | `"6_Shipped"` |
| `Dev Stripe` | `"Stripe N"` (mapped from stripe name in frontmatter - position in delivery plan) |
| `Feature Card URL` | local path to the `.md` file for reference |

Push Feature Card content as the Notion page body.

If Feature Backlog URL is blank in pureinn-variables.md: save locally, remind user to update Notion manually.

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Stub (1_Backlog) must have:**
- [ ] All frontmatter fields populated (id, title, status, stripe, owner, priority, prd_ref, feature_flag, flag_default)
- [ ] Sections 1-4 present as stubs (not filled)

**After pm-feature-design (2_Spec_Done) must have:**
- [ ] Section 1: entity, state before/after, BR-IDs linked
- [ ] Section 2: at minimum AC-01 (happy path), AC-02 (one guard failure), AC-03 (flag OFF)
- [ ] Section 3: mermaid sequenceDiagram (not empty), files to modify listed

**After build (6_Shipped) must have:**
- [ ] Section 4: at least one commit link, at least one test file path
- [ ] Section 4: flag OFF verification stated
- [ ] Section 4: Code Inspection result with date
- [ ] Status: 6_Shipped

---

## Save to

```
pureinn-workspace/[project-slug]/features/cards/[FEAT-ID].md
```
