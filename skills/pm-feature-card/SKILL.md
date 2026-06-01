---
name: pm-feature-card
description: Generate a Feature Card for a single feature (F-ID). Bridges FDD spec layer to delivery - derives EARS functional requirements and acceptance criteria from the FSD, adds pureinn delivery context (feature flag, rollout plan, kill switch), and produces an implementation checklist for backend, frontend, and testing. One Feature Card per feature. Phase 6 skill - run after FSD is complete for the Feature Set.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: feature card, feature spec, implementation spec, EARS requirements, acceptance criteria, feature flag, F-ID
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-fsd, pm-brd, pm-feature-set-overview, pm-stripe
---

# PM - Feature Card

## What this skill does

Produces the final spec-layer document for a single feature before it enters build. Bridges the FSD (Feature Set level) to individual developer tasks.

**Document stack position:**

| Layer | Answers | Document |
|---|---|---|
| Business | What must be true and why | BRD |
| Functional | How the Feature Set behaves | FSD |
| **Delivery** | **What is built now, exactly** | **Feature Card - this document** |
| Technical | How it is coded | Tech specs / ADRs |

**Feature Card defines:**
- EARS-format functional requirements for this specific feature (derived from FSD)
- Acceptance criteria (derived from FSD ACs for this F-ID)
- Feature flag name, ON/OFF behavior, rollout plan, kill switch trigger
- Implementation checklist: backend, frontend, testing, post-launch monitoring
- Definition of Done
- Dependencies on other features

**Feature Card does NOT define:**
- Business rules → BRD (reference RULE-IDs only)
- Feature Set-level behavior → FSD (reference section numbers)
- API contracts, payloads → Tech Specs / ADRs
- UI/UX designs → Design docs (Figma)
- Infrastructure → ADRs

One Feature Card = One Feature (F-ID). If a feature is too large for one card, split it into sub-features.

---

## Dependencies

**Required before running:**
- `pm-fsd` - FSD must be complete for this Feature Set. Feature Card derives requirements and ACs from FSD.
- `pm-brd` (Phase 6 detail) - RULE-IDs referenced in EARS requirements come from BRD.

**Recommended before running:**
- `pm-feature-set-overview` - team context on what this FS owns
- `pm-stripe` - confirms this feature is assigned to an active Stripe

**Produces artifacts used by:**
- Phase 7 build - developers implement what the Feature Card specifies
- `test-master` / `playwright-expert` - ACs are the direct test basis
- QA team - Definition of Done is the verification checklist
- Notion - Feature entry updated with Feature Card content and status

---

## Step 0: Current state check

Check for existing artifacts:
- Feature Card for this F-ID

If Feature Card exists: show version, completeness, which ACs are covered.

Also check: does a completed FSD exist for the Feature Set this feature belongs to? Feature Card cannot be written without it. Does a BRD Phase 6 section exist?

Look for: requirements without RULE-ID references, ACs that don't trace back to FSD, missing feature flag section, Implementation TODO without testing tasks, Definition of Done missing post-launch monitoring.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs for the Feature Card - Feature: [F-ID: Name]

1. FEATURE REFERENCE
   Feature ID and name: [F-ID] [Feature Name]
   Feature Set: [FS-ID: Name]
   Delivery Stripe: [Stripe N]
   FSD reference: confirm FSD is in context or paste relevant sections
   [paste FSD sections or "in context"]

2. FEATURE SCOPE
   What specifically does this feature do - in one sentence?
   (This will become the Feature Card purpose statement)

   Which FSD Acceptance Criteria (AC-XX) apply to this specific feature?
   (List the AC numbers from the FSD - e.g., AC-01, AC-03, AC-05)
   [list AC numbers]

3. FEATURE FLAG
   Suggested flag name: [product_name].[feature_name] or [fs_id].[feature_name]
   Confirm or provide your preferred naming: [flag name]

   What is the OFF behavior? (what happens for users where the flag is OFF - existing behavior, hidden UI, graceful degradation)
   [describe]

4. IMPLEMENTATION CONTEXT
   Backend: which services, data models, or jobs are affected?
   Frontend: which screens, components, or interactions are affected?
   Any performance target specific to this feature? (if different from FSD Section 8)
   [describe what you know - leave blank if covered in FSD]

5. DEPENDENCIES
   Does this feature depend on other features being done first?
   (List F-IDs that must be complete before this feature can be built)
   Does this feature block other features?
   [list or "none"]

6. OPEN QUESTIONS
   Any unresolved decisions specific to this feature?
   [list or "none"]
```

---

## Step 2: Generate artifact

Before generating:
1. Extract RULE-IDs from BRD that apply to this feature (cross-reference FSD Section 2.1 with feature scope)
2. Extract relevant ACs from FSD - only those specified in Step 1 (or all if not specified)
3. Derive EARS requirements from FSD Section 4 (Main Business Flow + Validations) scoped to this feature
4. Confirm feature flag name follows the pattern: `[product_slug].[feature_slug]`

Generate in English.

---

### ARTIFACT: Feature Card

```markdown
# Feature Card - [F-ID]: [Feature Name]

---

## 0. Feature Meta

| Field | Value |
|---|---|
| Feature ID | F-[ID] |
| Feature Name | [Feature Name] |
| Feature Set | FS-[ID]: [Feature Set Name] |
| Delivery Stripe | Stripe [N] |
| Status | Ready for Dev |
| Feature Flag | `[product_name].[feature_name]` |
| Priority | [KANO tier] - [V×C quadrant: Quick Win / Big Bet / Fill-in] |
| BRD Reference | [RULE-IDs that apply to this feature] |
| FSD Reference | [FS-ID] FSD Section [X], AC-[XX], AC-[XX] |

---

## 1. Purpose & User Value

**What this feature does:**
[1-2 sentences: what the feature does for the user and what business outcome it enables]

**Who benefits:** [Role] - [how they benefit]

**Business rules enforced:** [RULE-A/B/C-IDs] - [1-line summary of each]

---

## 2. Functional Requirements (EARS)

*Derived from FSD Section 4. EARS format: When / While / Where / The system shall.*

**FR-001: [Requirement Name]**
While [precondition - entity state or user context], when [trigger action], the system shall [response].
*(Enforces [RULE-ID])*

**FR-002: [Requirement Name]**
When [trigger], the system shall [response] within [constraint if applicable].
*(Reference: FSD Section [X.X])*

**FR-003: [Requirement Name - Failure handling]**
While [precondition], when [invalid or failing condition], the system shall [reject / block / return error].
*(Enforces [RULE-ID])*

**FR-004: [Requirement Name - Feature Flag]**
Where `[feature_flag_name]` is active, the system shall [behavior specific to this feature].
Where `[feature_flag_name]` is inactive, the system shall [fallback / existing behavior].

---

## 3. State Interactions

*State transitions this feature is responsible for triggering. Reference: FSD Section 6 + BRD Section 2.*

| Entity | From State | To State | Trigger | Rule |
|---|---|---|---|---|
| ENT-[Name] | [State A] | [State B] | [This feature's action] | [RULE-ID] |

---

## 4. Acceptance Criteria

*Derived from FSD AC-[XX]. Scope: this specific feature only.*

### AC-01 - [Happy Path Name] *(from FSD AC-[XX])*

- **Given** [precondition: who, what state]
- **When** [action]
- **Then** [observable outcome - entity state, event emitted, user feedback]
  - **And** [additional outcome]

### AC-02 - [Failure: Guard Name] *(from FSD AC-[XX])*

- **Given** [precondition]
- **When** [invalid condition or failing action]
- **Then** [system blocks / rejects / returns error]
  - **And** [rule enforced, referenced by RULE-ID]

### AC-03 - [Feature Flag OFF behavior]*

- **Given** flag `[feature_flag_name]` is OFF
- **When** [same trigger]
- **Then** [existing behavior unchanged / feature hidden / graceful degradation]

---

## 5. Error Handling (business-level)

*Error conditions and business outcomes. HTTP codes belong in ADRs, not here.*

| Scenario | System behavior | Rule reference | User signal |
|---|---|---|---|
| [Guard condition fails] | [System blocks action, entity unchanged] | [RULE-ID] | [Error displayed / notification sent] |
| [External dependency fails] | [System falls back to / retries / queues] | [RULE-ID if applicable] | [User informed / silent retry] |
| [Concurrency conflict] | [System rejects duplicate, returns existing] | [RULE-ID] | [Idempotent response] |

---

## 6. Non-Functional Requirements

*Feature-scoped NFRs. Inherit from FSD Section 8 unless noted differently here.*

**Performance:**
- [Specific target for this feature, e.g., "validation response < 200ms during user input"]
- Inherits from FSD: [yes / see FSD Section 8.2 for details]

**Security:**
- [Authentication required: yes / no]
- [Authorization: which roles can trigger this feature]
- [PII involved: [yes - which fields] / no]

**Feature flag behavior:**
- **ON:** [Full feature behavior as specified above]
- **OFF:** [Fallback: existing behavior / feature hidden / graceful degradation]
- **Kill switch:** disable flag if [error rate > 5% / specific condition]
- **Rollout:** Internal → 5% → 25% → 50% → 100%

---

## 7. Implementation Checklist

### Backend
- [ ] [Data model change: migration for X table / add Y field to ENT-Z]
- [ ] [Service: implement X method with guard for RULE-ID]
- [ ] [Enforce state transition: ENT-X from [State A] to [State B]]
- [ ] [Emit event: [event.name] when [condition]]
- [ ] [Idempotency: check for [unique key] before creating new entity]
- [ ] Register feature flag `[feature_flag_name]` (default: OFF)

### Frontend
- [ ] [Component: create / update X component]
- [ ] [State: handle [State A] and [State B] display]
- [ ] [Validation: client-side check for [field] before submission]
- [ ] [Error state: display [error message] when [scenario]]
- [ ] [Loading state: show during [async operation]]
- [ ] [Feature flag gate: hide / show UI element based on flag]

### Testing
- [ ] Unit tests: [X service / Y method] with [happy path + failure cases]
- [ ] Integration test: [flow description covering AC-01]
- [ ] Integration test: [failure scenario from AC-02]
- [ ] Feature flag test: AC-03 - OFF state (existing behavior unchanged)
- [ ] Regression: no >10% latency increase on existing API calls
- [ ] Idempotency test: duplicate request returns existing entity

### Post-launch monitoring
- [ ] Monitor [key signal from FSD Section 9.1] for 4 weeks minimum
- [ ] Set alert for [alert condition from FSD Section 9.3]
- [ ] Kill switch ready: disable `[feature_flag_name]` if error rate > 5%

---

## 8. Dependencies

**This feature depends on:**
| F-ID | Feature Name | Why |
|---|---|---|
| F-[ID] | [Feature Name] | [Must exist before this feature can run / entity must be in State X] |

**This feature blocks:**
| F-ID | Feature Name | Why |
|---|---|---|
| F-[ID] | [Feature Name] | [This feature's output is required input for that feature] |

---

## 9. Definition of Done

- [ ] All EARS requirements implemented and passing
- [ ] All ACs from Section 4 pass (AC-01, AC-02, AC-03)
- [ ] Feature flag `[feature_flag_name]` implemented, default OFF
- [ ] OFF state verified: existing behavior unchanged
- [ ] No regression: existing API calls within +10% latency
- [ ] Code reviewed
- [ ] Feature deployed behind flag (not yet enabled)
- [ ] Post-launch monitoring active (4 weeks minimum per pureinn delivery standard)

---

## 10. Open Questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | [TBD] | [TBD] | Open |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Section 0 - Feature Meta must cover:**
- [ ] F-ID, FS-ID, Stripe, Status, Feature Flag name all filled
- [ ] BRD RULE-IDs referenced
- [ ] FSD AC numbers referenced (traceability)

**Section 2 - EARS Requirements:**
- [ ] At least 3 requirements: happy path, failure/guard, feature flag behavior
- [ ] Each requirement traces to FSD section or BRD rule
- [ ] Feature flag ON/OFF behavior explicitly stated as FR

**Section 3 - State Interactions:**
- [ ] All state transitions this feature triggers are listed
- [ ] Each transition has entity + from/to state + trigger + rule reference

**Section 4 - Acceptance Criteria:**
- [ ] ACs derived from FSD - AC numbers cited
- [ ] At minimum: happy path + at least one guard failure + feature flag OFF behavior
- [ ] Given/When/Then format strictly followed
- [ ] "Then" is observable and testable without knowledge of internals

**Section 5 - Error Handling:**
- [ ] No HTTP codes (those belong in ADRs)
- [ ] Each scenario: system behavior + rule reference + user signal

**Section 6 - Feature Flag:**
- [ ] Flag name defined (format: product.feature)
- [ ] ON behavior stated
- [ ] OFF behavior stated (what existing behavior is preserved)
- [ ] Kill switch trigger defined
- [ ] Rollout sequence: Internal → 5% → 25% → 50% → 100%

**Section 7 - Implementation Checklist:**
- [ ] Backend: data model change, service logic, state transition, event emission, idempotency, flag registration
- [ ] Frontend: component, state display, validation, error/loading states, flag gate
- [ ] Testing: unit, integration (happy + failure), flag OFF test, regression, idempotency
- [ ] Post-launch: monitoring signal, alert condition, kill switch ready

**Section 9 - Definition of Done:**
- [ ] All ACs listed by number
- [ ] Feature flag requirement explicit
- [ ] OFF state verification explicit
- [ ] Regression test explicit
- [ ] 4-week monitoring explicit

**Does NOT duplicate:**
- [ ] No business rule text repeated from BRD (reference RULE-ID only)
- [ ] No entity attribute definitions (reference Domain Model)
- [ ] No API endpoints or payloads (reference Tech Specs / ADRs)
- [ ] No UI/UX designs (reference Figma / Design docs)

---

## Notion push

**Runs after user approves the Feature Card.**

Read `pureinn-variables.md` key "Feature Backlog" → get DB URL. Find the existing Feature entry for F-[ID] (search by feature name or F-ID property).

Update the Feature entry via `notion-update-page`:

| Notion property | Value |
|---|---|
| `Status` | `Ready for Dev` |
| `Feature Flag` | `[feature_flag_name]` |
| `Stripe` | `Stripe [N]` |
| `BRD Reference` | `[RULE-IDs]` |
| `FSD Reference` | `[FS-ID] AC-[XX], AC-[XX]` |

Push Feature Card content as the Notion page body (replaces stub if pm-reverse-extract created one earlier).

If Feature Backlog URL is blank in pureinn-variables.md: save locally, remind user to update Notion manually.

---

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-6/[f-id]-feature-card.md
```
