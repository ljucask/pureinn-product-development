---
name: pm-fsd
description: Generate a Functional Specification Document (FSD) for a single Feature Set. Defines how the Feature Set implements the BRD - execution flows, validations, state transitions, acceptance criteria (Given/When/Then), and observability. One FSD per Feature Set. Phase 6 skill.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: FSD, functional specification, user flows, acceptance criteria, validations, feature specification
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-brd, pm-feature-set-overview, pm-domain-model, pm-stripe
---

# PM - Functional Specification Document (FSD)

## What this skill does

Describes how a specific Feature Set behaves - the bridge between business rules (BRD) and implementation (Feature Cards, code).

**Document stack position:**

| Layer | Answers | Document |
|---|---|---|
| Business | What must be true and why | BRD |
| Conceptual | What entities exist and how they relate | Domain Model |
| **Functional** | **How this Feature Set behaves** | **FSD - this document** |
| Delivery | What is built in this iteration | Feature Cards |

**FSD defines:**
- Execution flows and responsibilities of the Feature Set
- Validations, guards, and failure handling
- State transitions this Feature Set triggers
- Acceptance criteria (Given / When / Then per feature)
- Business signals, metrics, and observability

**FSD does NOT define:**
- Business rules → BRD
- Entity attributes, enums → Domain Model
- UI/UX flows → Design docs
- API endpoints, payloads → Tech specs / ADRs
- Infrastructure, retries → ADRs

One FSD = One Feature Set. If a Feature Set is too large, split it.

---

## Dependencies

**Required before running:**
- `pm-brd` (Phase 6 detail for this Feature Set) - FSD applies BRD rules, never reinterprets them
- `pm-domain-model` - entities and their attributes are referenced throughout

**Recommended before running:**
- `pm-feature-set-overview` - scope and boundaries of the Feature Set
- `pm-mvp-scope` - delivery stripe context (what's in scope for current stripe)

**Produces artifacts used by:**
- `feature-forge` - Feature Cards are derived from FSD acceptance criteria
- Phase 7 build - developers implement what FSD specifies
- QA - acceptance criteria are the test basis

---

## Step 0: Current state check

Check for existing artifacts:
- FSD for this Feature Set

If FSD exists: identify version and completeness. Which flows are specified? Which acceptance criteria are missing?

Also check: does a BRD Phase 6 section exist for this Feature Set? FSD cannot be written without it. Does a Feature Set Overview exist?

Look for: flows without failure paths, acceptance criteria without "When" triggers, validations listed without what happens on failure, state transitions in FSD that contradict BRD, missing observability section.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs for the FSD - Feature Set: [FS-ID: Name]

1. FEATURE SET SCOPE
   Paste the Feature Set Overview, or describe the Feature Set:
   - What is its purpose?
   - Which features (F-IDs) are in this Feature Set?
   - What triggers the Feature Set? (user action, system event, API call, scheduled job)
   [paste or describe]

2. BRD REFERENCE
   Which BRD rules apply to this Feature Set?
   (paste relevant RULE-A/B/C entries or confirm BRD is in context)
   [paste rules or "in context"]

3. EXECUTION FLOWS
   Walk me through the main flow(s):
   - What does the user/system do first?
   - What does the system do in response?
   - What are the decision points?
   - What happens on success? On failure?

4. VALIDATIONS
   What input validations are needed?
   What business validations (beyond data format) are required?
   (e.g., "cannot book if listing is not active", "cannot pay if booking not confirmed")

5. EDGE CASES
   What unusual but possible scenarios must be handled?
   (e.g., concurrent bookings on same listing, payment timeout, session expiry mid-flow)

6. OBSERVABILITY
   What metrics or signals matter for this Feature Set?
   (e.g., booking conversion rate, payment failure rate, response time SLA)
```

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Functional Specification Document

```markdown
# FSD - [FS-ID]: [Feature Set Name]

**Product:** [Product Name]
**Version:** 1.0
**Date:** [date]
**BRD reference:** [BRD version + relevant rule IDs]
**Domain Model reference:** [Domain Model version + relevant entity IDs]
**Delivery:** [Stripe X - Week Y-Z]

---

## 0. Feature Set Purpose

**What this Feature Set does:**
[1-2 sentences: the business capability this FS implements]

**Primary actor:** [Host / Guest / Admin / System]

**Trigger:** [What initiates this Feature Set's execution - user action, event, scheduled job, API call]

**Success outcome:** [What is the observable result when this FS executes correctly]

---

## 1. Features in Scope

| ID | Feature | FSD section |
|---|---|---|
| F-[ID] | [Feature name] | Section 2.X |
| F-[ID] | [Feature name] | Section 2.X |

---

## 2. Execution Flows

### 2.1 [Main Flow Name] (Happy Path)

**Trigger:** [What starts this flow]
**Actor:** [Who initiates]
**Preconditions:** [What must be true before this flow can start]

**Flow:**

| Step | Actor | Action | System response | Rule enforced |
|---|---|---|---|---|
| 1 | [Guest] | [Submits booking request] | [Creates BookingRequest in Pending state] | |
| 2 | [System] | [Validates listing availability] | [Checks no conflict in Availability records] | RULE-B-002 |
| 3 | [System] | [Notifies host] | [Sends booking.requested event] | |
| 4 | [Host] | [Approves request] | [Transitions Booking to Confirmed] | RULE-A-001 |
| 5 | [System] | [Initiates payment] | [Creates Payment in Pending state] | |

**Postconditions:** [What is true after the flow completes successfully]

---

### 2.2 [Alternative Flow Name]

**Trigger:** [What causes this alternative path]

[same step table structure]

---

### 2.3 [Failure Flow Name]

**Trigger:** [What causes failure]

[same step table structure - focus on how system handles failure, what state entities end up in]

---

## 3. Validations

### Input Validations (data format and presence)

| Field | Validation | Error message |
|---|---|---|
| [booking.check_in_date] | Required, must be future date | "Check-in date must be in the future" |
| [booking.guest_count] | Required, integer, min 1, max [listing.max_guests] | "Guest count exceeds listing capacity" |

### Business Validations (domain rules)

| Validation | Rule reference | Failure handling |
|---|---|---|
| Listing must be in Active state | RULE-B-001 | Return error: "This listing is not available for booking" |
| No overlapping confirmed booking | RULE-A-001 | Return error: "Selected dates are no longer available" |
| Guest cannot book their own listing | RULE-B-003 | Return error: "You cannot book your own listing" |

---

## 4. State Transitions

List of state transitions this Feature Set is responsible for:

| Entity | From | Trigger | Guard | To |
|---|---|---|---|---|
| Booking | - | Guest submits request | Listing is Active | Requested |
| Booking | Requested | Host approves | Payment captured | Confirmed |
| Booking | Requested | Host declines / 48h timeout | - | Declined |

Reference: BRD state machines for full detail.

---

## 5. Events

### Events this Feature Set emits

| Event | Trigger (step) | Payload | Consumers |
|---|---|---|---|
| `booking.requested` | Step 3 | `booking_id`, `listing_id`, `host_id`, `guest_id` | Messaging FS, Notification FS |
| `booking.confirmed` | Step 4 | `booking_id`, `confirmed_at` | Payment FS, Notification FS |

### Events this Feature Set consumes

| Event | From | Action taken |
|---|---|---|
| `payment.captured` | Payment FS | Transition Booking to Confirmed |
| `payment.failed` | Payment FS | Revert Booking to Requested, notify guest |

---

## 6. Acceptance Criteria

One Given/When/Then block per feature in this Feature Set.

### F-[ID]: [Feature Name]

**Scenario 1: [Happy path scenario name]**
```
Given [precondition - what is true before the action]
When [the user/system action]
Then [the observable outcome]
And [additional outcomes if needed]
```

**Scenario 2: [Failure/edge case scenario name]**
```
Given [precondition]
When [action]
Then [outcome - error, state, notification]
```

---

### F-[ID]: [Feature Name]

[same structure]

---

## 7. Observability

**Key metrics for this Feature Set:**

| Metric | Definition | Target | Alert threshold |
|---|---|---|---|
| [Booking request to confirmation time] | [Time from booking.requested to booking.confirmed] | [< 24h median] | [> 48h p95] |
| [Booking approval rate] | [% of requests that result in Confirmed] | [> 70%] | [< 50% over 7 days] |
| [Payment success rate] | [% of payment initiations that succeed] | [> 97%] | [< 95%] |

**Logs required:**
- [Log booking state transitions with timestamps]
- [Log validation failures with reason codes]
- [Log payment initiation and outcome]

---

## 8. Open Items

| Item | Type | Priority | Owner |
|---|---|---|---|
| [Edge case not yet specified] | Design decision | High | PM |
| [Validation rule to confirm with legal] | Requirement | Med | Legal |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Flows must cover:**
- [ ] Happy path flow defined (step by step)
- [ ] At least one failure path defined
- [ ] Each step has: actor, action, system response
- [ ] BRD rule referenced where it applies in the flow
- [ ] Preconditions and postconditions stated

**Validations must cover:**
- [ ] Input validations (format, presence, range)
- [ ] Business validations (domain rules, state checks)
- [ ] Each validation has a failure handling (what error, what state, what notification)

**Acceptance criteria must cover:**
- [ ] One AC block per feature in the Feature Set
- [ ] Each AC has at least 2 scenarios (happy path + at least one failure/edge case)
- [ ] Given/When/Then format strictly followed
- [ ] "Then" statements are observable (testable without knowledge of internals)

**Events must cover:**
- [ ] All events this FS emits are listed with payload
- [ ] All events this FS consumes are listed with action taken
- [ ] Cross-FS event dependencies are explicit

**Does NOT duplicate:**
- [ ] No business rule text repeated from BRD (reference RULE-ID instead)
- [ ] No entity attribute definitions (reference Domain Model)
- [ ] No UI/UX descriptions (reference Design docs)
- [ ] No API endpoint definitions (reference tech specs)

**For SaaS/AI products:**
- [ ] AI flows: output quality validation step included (what if AI returns low-confidence result?)
- [ ] AI flows: fallback path defined (what if AI service is unavailable?)
- [ ] Rate limiting: request throttling handling in flows where applicable
- [ ] Multi-tenant: tenant isolation enforced at query/data access level in each flow
- [ ] Async flows: polling or webhook callback pattern specified where applicable

## Notion

Read `pureinn-variables.md` key "FSD" → if URL present, remind user after saving:
`FSD saved locally. Update Notion: [FSD URL]`

Also update the corresponding Feature Set entries in the Feature Backlog DB: set `FSD URL` property on each FS entry to the local file path or a future Notion page URL once the FSD is published there.

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-fsd.md
```
