---
name: pm-brd
description: Generate or update a Business Requirements Document (BRD). Living document - skeleton created in Phase 4 (system boundary, state machine overview), full detail written in Phase 6 per Feature Set. Defines how the system behaves from a business perspective - rules, state machines, processes, events. Never duplicates Domain Model content.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: BRD, business requirements, state machines, event model, business rules, feature set spec
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-fsd, pm-domain-model, pm-features-list, pm-business-rule-core, pm-business-rule-critical, pm-business-rule-governance
---

# PM - Business Requirements Document (BRD)

## What this skill does

Defines how the system behaves from a business perspective. The BRD is the authoritative source for:
- Business rules (RULE-A/B/C library)
- Entity state machines (lifecycle transitions)
- Business processes (conceptual level)
- Events and their business meaning
- Governance, compliance, and retention principles

**Document stack position:**
- Domain Model → *what the system is made of* (entities, attributes, relationships)
- **BRD → *how the system behaves*** (rules, states, processes, events)
- FSD → *how a specific Feature Set implements the BRD*

BRD never defines: entities/attributes (Domain Model), API endpoints (FSD/tech docs), UI flows (design docs), algorithms (FSD).

**Living document pattern:**
- Phase 4: BRD Skeleton - system boundary, capability map, state machine overview
- Phase 6: BRD Full Detail - written per Feature Set, one section at a time. Run this skill again for each Feature Set.

**Notion output - four connected databases (all pushed automatically after approval):**
- BRD page - full document content pushed to the BRD Notion page
- Business Rules DB - one entry per RULE-A/B/C defined in this run
- Decision Models DB - one entry per decision point / branching logic
- Event Catalogue DB - one entry per business event emitted or consumed by this Feature Set
- Data Sensitivity DB - one entry per RULE-C rule with compliance/data-retention context

---

## Dependencies

**Required before running (Phase 4 skeleton):**
- `pm-domain-model` - entities and their lifecycles are the input for state machines

**Required before running (Phase 6 detail):**
- BRD Skeleton must exist
- `pm-feature-set-overview` - Feature Set scope defines which rules and states to specify
- `pm-mvp-scope` - Feature Set list determines BRD scope per stripe

**Produces artifacts used by:**
- `pm-fsd` - BRD rules and state machines are referenced in every FSD section
- `pm-business-rule-critical/core/governance` - rules are added to the BRD Rules Library
- `pm-privacy-requirements` - data retention and governance rules go here
- Phase 7 build - developers implement behavior defined in BRD

---

## Step 0: Current state check

Check for existing artifacts:
- BRD (any version / any Feature Set)

Identify: does a BRD skeleton exist (Phase 4)? If yes, which Feature Sets have been detailed (Phase 6)? Which are still TBD?

Look for: state machines without guard conditions, business rules without RULE-ID codes, rules that duplicate Domain Model content (attributes, enums), missing edge case handling in state transitions, no events section, compliance rules not captured.

Apply the standard skill interaction pattern (CLAUDE.md). Options should reflect current state:
- A) Generate Phase 4 Skeleton (if no BRD exists)
- B) Add Phase 6 detail for Feature Set [X] (if skeleton exists)
- C) Update existing section (if BRD exists and needs revision)
- D) Something specific

---

## Step 1: Gather inputs

Questions depend on whether generating Phase 4 skeleton or Phase 6 detail.

### For Phase 4 Skeleton:

```
I need inputs for the BRD Skeleton (Phase 4).

1. DOMAIN MODEL
   Paste the Domain Model or confirm it's in context.
   I need the entity list and their lifecycle states.
   [paste or "in context"]

2. SYSTEM SCOPE
   What does the system own end-to-end?
   What is explicitly out of scope? (what does NOT belong to this system to manage)

3. USER ROLES
   What roles interact with the system?
   What can each role do (high level)?

4. KEY BUSINESS CONSTRAINTS
   Are there any non-negotiable rules you already know?
   (e.g., "payment must never release without delivery confirmation",
    "a booking cannot be double-confirmed", "user data must be deleted within 30 days of request")

5. EXTERNAL SYSTEMS
   What external systems trigger events in our system or receive events from us?
```

### For Phase 6 Detail (per Feature Set):

```
I need inputs for BRD detail - Feature Set: [FS-ID: Name]

1. FEATURE SET OVERVIEW
   Paste the Feature Set Overview or confirm it's in context.
   [paste or "in context"]

2. BUSINESS RULES FOR THIS FEATURE SET
   What are the key business rules that govern this Feature Set?
   (any constraints, invariants, policies that must hold)

3. STATE MACHINES
   Which entities change state within this Feature Set?
   Walk me through each transition: from state → trigger → to state (+ any guard conditions)

4. EDGE CASES AND FAILURES
   What can go wrong? What should the system do?
   (e.g., "what if payment fails?", "what if host doesn't respond within 24h?")

5. EVENTS
   What business-significant events does this Feature Set emit?
   What events does it consume from other Feature Sets?
```

---

## Step 2: Generate artifact

Generate in English.

---

### PHASE 4 SKELETON TEMPLATE

```markdown
# Business Requirements Document - [Product Name]

**Version:** 0.1 (skeleton)
**Date:** [date]
**Status:** Phase 4 - Skeleton. Full detail added per Feature Set in Phase 6.
**Based on:** Domain Model v[X]
**Author:** [Product Team]
**Review Status:** Draft

---

## 0. Document Meta & Navigation

### 0.1 Purpose & Scope

This BRD defines the business behavior of [Product Name] - the rules, processes, state machines, and events that govern how the system operates. It is the authoritative reference for what the system must do at a business level, regardless of implementation.

**Scope:** [Which product areas / Feature Sets are covered]
**Out of scope:** [What is explicitly excluded from this BRD]

### 0.2 What this BRD Defines / Does NOT Define

**BRD defines:**
- Business rules (RULE-A/B/C library)
- Entity lifecycle state machines
- Business processes at conceptual level
- Business events and their meaning
- Governance, compliance, and data retention principles
- Decision models and branching logic

**BRD does NOT define:**
- Entities, attributes, data types, enums → Domain Model
- API endpoints, payloads, integration specs → FSD / Tech Docs
- UI/UX flows, screen designs → Design Docs
- Infrastructure, retry logic, deployment → ADRs
- Algorithms, calculation logic → FSD

### 0.3 Boundaries & Relationships

| Document | Relationship | Precedence |
|---|---|---|
| Domain Model | BRD references entities defined there. Never duplicates them. | Domain Model is authoritative on structure. |
| FSD | FSD implements what BRD specifies. FSD inherits rules by reference. | BRD is authoritative on behavior. |
| PRD | PRD defines what and why. BRD defines how the system enforces it. | PRD is upstream. |
| Feature Cards | Feature Cards reference BRD rules and states for acceptance criteria. | BRD is the reference layer. |

### 0.4 Intended Audience

| Audience | Purpose |
|---|---|
| Product Owner | Owns rule decisions, approves edge case handling |
| Tech Lead / Architect | Designs system to enforce stated rules |
| Backend Engineer | Implements state machines, rule enforcement, event emission |
| QA Engineer | Derives test cases from state transitions and business rules |
| Legal / Compliance | Reviews RULE-C entries for policy alignment |

### 0.5 How to Read this Document

- **Section 1** - understand the user ecosystem and system scope before reading anything else
- **Section 2** - state machine overview; full detail added in Phase 6 per Feature Set
- **Section 3** - process orchestration and dependency rules
- **Sections 4-6** - rules, decisions, events; populated in Phase 6
- **Sections 7-10** - supporting content (notifications, policies, NFRs, open questions)

Search tip: every rule is tagged RULE-A/B/C-[ID]. Every entity is tagged ENT-[ID]. Every process is tagged PROC-[ID]. Every decision model is tagged DM-[ID].

### 0.6 References

| Document | Location | Notes |
|---|---|---|
| Domain Model | pureinn-workspace/[slug]/artifacts/phase-4/domain-model.md | Entities, attributes, relationships |
| PRD | pureinn-workspace/[slug]/artifacts/phase-3/prd.md | Product definition, scope, metrics |
| Feature Sets | pureinn-workspace/[slug]/artifacts/phase-5/feature-sets.md | Feature Set list and scope |

### 0.7 Glossary & Notation

| Term / Symbol | Meaning |
|---|---|
| RULE-A-[ID] | Critical Invariant - non-negotiable, no exceptions |
| RULE-B-[ID] | Core Business Rule - standard behavior, may have edge cases |
| RULE-C-[ID] | Governance / Policy / UX Rule |
| ENT-[ID] | Entity identifier (as defined in Domain Model) |
| PROC-[ID] | Business process identifier |
| DM-[ID] | Decision Model identifier |
| EVT-[Name] | Business event identifier |
| TBL | Decision Table |
| TRE | Decision Tree |
| SCR | Scoring Model |
| [Phase 6] | Content to be detailed in Phase 6 per Feature Set |

### 0.8 Change Management

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | [date] | [author] | Phase 4 skeleton |

---

## 1. System Boundary & Business Capabilities

### 1.1 User Ecosystem & Roles

#### Primary Roles

| Role ID | Role Name | Description | Access Level |
|---|---|---|---|
| ROLE-01 | [Host / Seller / Owner] | [Creates and manages supply-side content, receives payouts] | Full self-service |
| ROLE-02 | [Guest / Buyer / User] | [Discovers, requests, pays, and consumes the service] | Full self-service |

#### Secondary Roles

| Role ID | Role Name | Description | Access Level |
|---|---|---|---|
| ROLE-03 | [Admin] | [Platform management, dispute resolution, monitoring] | Full platform access |
| ROLE-04 | [System / Automated Actor] | [Background jobs, notifications, rule enforcement] | Internal only |

#### Motivations & Needs

| Role | Primary Goal | Key Frustration | Success Signal |
|---|---|---|---|
| [Host] | [Earn income with minimal friction] | [Uncertainty about payout timing] | [Reliable, predictable payouts] |
| [Guest] | [Find and confirm the right option quickly] | [Slow or unclear booking confirmation] | [Fast confirmation, clear status] |
| [Admin] | [Maintain platform trust and resolve issues] | [Manual work, unclear escalation paths] | [Low dispute rate, fast resolution] |

#### Multi-Role Logic

[Describe scenarios where one user holds multiple roles simultaneously, e.g., a user who is both a Host and a Guest. Define precedence rules if role conflicts arise.]

---

### 1.2 System Boundary

#### Inside - Platform Owns

| Capability | Description |
|---|---|
| [Booking lifecycle management] | [Creating, confirming, cancelling, and completing bookings] |
| [Payment orchestration] | [Collecting payments, releasing payouts, processing refunds] |
| [Listing management] | [Creating, publishing, updating, and archiving listings] |
| [Dispute resolution workflow] | [Managing escalations between parties] |
| [Notification orchestration] | [Email, push, and in-app notifications for lifecycle events] |

#### Outside - Platform Does NOT Own

| Area | Who Owns It | Integration Required? |
|---|---|---|
| [Payment processing infrastructure] | [Stripe / Payment provider] | Yes - via API |
| [Identity verification] | [External KYC provider] | Yes - via webhook |
| [Tax calculation and filing] | [Accounting integrations / User] | Partial |
| [Physical service delivery] | [Host / Service Provider] | No |

#### External Systems

| System | Direction | What it provides / receives | Trigger |
|---|---|---|---|
| [Stripe] | Outbound + Inbound | [Payment capture, payout, refund] | [Booking confirmed / Booking completed] |
| [Email provider] | Outbound | [Transactional emails] | [State change events] |
| [KYC Provider] | Inbound | [Identity verification result] | [Host onboarding] |

---

### 1.3 Business Capability Map

| Capability | Domain | Description | Primary Entities | Phase 6 Detail |
|---|---|---|---|---|
| [User Onboarding & Identity] | [Identity] | [Account creation, verification, role assignment] | [ENT-001 User] | [FS-01] |
| [Listing Management] | [Supply] | [Host creates, publishes, and manages listings] | [ENT-002 Listing] | [FS-02] |
| [Booking Orchestration] | [Transactions] | [End-to-end booking flow: request → confirm → complete] | [ENT-003 Booking] | [FS-03] |
| [Payment & Payout] | [Finance] | [Payments, payouts, refunds, escrow] | [ENT-004 Payment] | [FS-04] |
| [Reviews & Trust] | [Trust] | [Post-booking review submission and moderation] | [ENT-005 Review] | [FS-05] |

---

### 1.4 Responsibility Split

| Capability | Platform | External System | Manual / Human |
|---|---|---|---|
| [Booking state management] | Full ownership | - | Host approval |
| [Payment processing] | Orchestration only | [Stripe] | - |
| [Identity verification] | Data storage | [KYC Provider] | Admin review |
| [Dispute resolution] | Workflow + escalation | - | Admin decision |
| [Tax calculation] | Data provision | [Accounting tool] | User filing |

---

## 2. Core State Machines - Overview

*Full state machine detail added per Feature Set in Phase 6.*

| Entity | States (high level) | Key transitions | Detailed in |
|---|---|---|---|
| [ENT-001 User] | [Unverified → Active → Suspended → Deactivated] | [Email verified, Admin suspend, User deactivate] | Phase 6 - FS-01 |
| [ENT-002 Listing] | [Draft → Active → Paused → Archived] | [Host publishes, Host pauses, Admin archives] | Phase 6 - FS-02 |
| [ENT-003 Booking] | [Requested → Confirmed → Completed → Cancelled] | [Host approves, Guest cancels, Auto-expires] | Phase 6 - FS-03 |
| [ENT-004 Payment] | [Pending → Captured → Held → Released → Refunded] | [Booking confirmed, Booking completed, Dispute opened] | Phase 6 - FS-04 |

---

## 3. Business Processes & Orchestration

### 3.1 Process Overview

| Process ID | Process Name | Layer | Trigger | Goal | Affected Lifecycles |
|---|---|---|---|---|---|
| PROC-001 | [Host Onboarding] | [Onboarding] | [User registers as host] | [Verified, capable host account] | [ENT-001 User] |
| PROC-002 | [Booking Request & Approval] | [Core Transaction] | [Guest submits booking request] | [Confirmed booking with payment captured] | [ENT-003 Booking, ENT-004 Payment] |
| PROC-003 | [Booking Completion & Payout] | [Finance] | [Booking date passes or service delivered] | [Released payout to host, completed booking] | [ENT-003 Booking, ENT-004 Payment] |
| PROC-004 | [Cancellation & Refund] | [Exception] | [Guest or host cancels] | [Clean cancellation with correct refund] | [ENT-003 Booking, ENT-004 Payment] |
| PROC-005 | [Dispute Resolution] | [Operations] | [Guest or host raises dispute] | [Fair, documented resolution] | [ENT-003 Booking, ENT-006 Dispute] |

### 3.2 Orchestration Principles

#### 3.2.1 Process Ordering Rules

[Define which processes must run in a specific sequence. Example:]
- Payment capture must occur before booking confirmation is issued.
- Payout must not be released before booking completion is confirmed.
- Host verification must be complete before listing can be published.

#### 3.2.2 Blocking & Dependency Rules

[Define which state transitions or processes block other processes. Example:]
- An active dispute blocks payout release for the affected booking.
- A suspended host account blocks all new booking confirmations for their listings.
- A listing with an active booking cannot be archived.

#### 3.2.3 Override & Priority Principles

[Define who can override normal process flow and under what conditions. Example:]
- Admin can force-close a booking regardless of state.
- Admin can manually release or hold a payout (overrides automated rules).
- System auto-expiry overrides inaction by host or guest.

#### 3.2.4 Fallback & Recovery Principles

[Define what the system does when a process fails or times out. Example:]
- If payment capture fails: booking reverts to Requested state; guest is notified.
- If host does not respond within [X] hours: booking request auto-expires; guest is refunded.
- If payout fails: payment held in Held state; support ticket created; admin alerted.

---

## 4. Business Rules Library

*Populated in Phase 6 per Feature Set.*

| Name | Rule ID | Category | Affected Entity | Description | Domain | Priority |
|---|---|---|---|---|---|---|
| [TBD] | RULE-A-001 | A - Critical | [TBD] | [TBD] | [TBD] | Critical |

Full rules defined per Feature Set in Phase 6. Structure: flat table, one row per rule. Decision logic (if/then) → Section 5. Event definitions → Section 6.

---

## 5. Decision Models Catalogue

*Populated in Phase 6 per Feature Set.*

| # | ID | Name | Domain | Notes | What is being decided | Type | Produces | Used in Process | Where in lifecycle | Uses Business Rules | Uses Scoring Models | Uses Other Decisions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DM-001 | [TBD] | [TBD] | [TBD] | [TBD] | TBL / TRE / SCR | [Outcomes] | PROC-[ID] | [Lifecycle state] | - | - | - |

Types: TBL = Decision Table, TRE = Decision Tree, SCR = Scoring Model.

---

## 6. Business Events

*Populated in Phase 6 per Feature Set.*

### 6.1 Event Overview

| Event | Category | Emitted by | Key Consumers | Lifecycle trigger |
|---|---|---|---|---|
| [TBD] | [Lifecycle / System / External] | [Feature Set] | [Feature Set] | [State transition] |

### 6.2 Event Catalogue

| Name | Category | Aliases | Business Meaning | Consumers | Lifecycle + State | Primary Entity | Producer | Related Rules/Decisions | Trigger Type | Related Decisions |
|---|---|---|---|---|---|---|---|---|---|---|
| [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [Automatic / Manual] | [TBD] |

### 6.3 Event Propagation Maps

*One propagation map per major process. Added in Phase 6.*

---

## 7. Notifications & Communication Rules

*Populated in Phase 6 per Feature Set.*

| Trigger Event | Recipient | Channel | Timing | Template ref | Rule ref |
|---|---|---|---|---|---|
| [TBD] | [TBD] | [Email / Push / In-app] | [Immediate / Delayed] | [TBD] | [TBD] |

---

## 8. Platform Policies & Compliance

*Populated in Phase 6 per Feature Set. See also RULE-C entries in Section 4.*

### 8.1 Data Retention Rules

[TBD - added per Feature Set]

### 8.2 Privacy & Consent Rules

[TBD - added per Feature Set]

### 8.3 Regulatory & Legal Constraints

[TBD - added per Feature Set]

---

## 9. Non-Functional Business Requirements

*Populated in Phase 6 per Feature Set.*

| Requirement | Type | Target | Notes |
|---|---|---|---|
| [TBD] | [Availability / Latency / Throughput / Compliance] | [TBD] | [TBD] |

---

## 10. Open Questions & Decisions Log

| # | Question / Open Item | Owner | Status | Target date | Resolution |
|---|---|---|---|---|---|
| 1 | [TBD] | [TBD] | Open | [TBD] | - |

---

## Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | [date] | [author] | Phase 4 skeleton |
```

---

### PHASE 6 DETAIL TEMPLATE (added per Feature Set)

```markdown
---
<!-- Phase 6 addition - Feature Set [FS-ID]: [Name] - appended, do not overwrite existing sections -->

## Phase 6 Addition: [FS-ID] - [Feature Set Name]

**Added:** [date]
**Feature Set scope:** [Brief description of what this FS covers]

---

### Section 2 Update: State Machines - [FS-ID]

#### 2.[X] Lifecycle: ENT-[Name]

##### Lifecycle Overview

[1-2 sentences on the entity's business lifecycle within this Feature Set. What does it mean for this entity to move through its states? What business purpose does it serve?]

##### States Catalogue

| State | Description | Terminal? | Notes |
|---|---|---|---|
| [State A] | [Business meaning of being in this state] | N | [Entry/residence conditions worth noting] |
| [State B] | [Business meaning] | N | |
| [Final State] | [Business meaning - this state ends the lifecycle] | Y | [Terminal states cannot transition further] |

##### Allowed Transitions

| From State | To State | Trigger Type | Trigger Name | Conditions (high-level) | Related RULE IDs | Notes |
|---|---|---|---|---|---|---|
| [State A] | [State B] | [User action / System / Scheduled / External] | [e.g., host.approved_booking] | [e.g., Payment captured; Host within response window] | RULE-A-001 | |
| [State B] | [State C] | [System] | [e.g., booking.completed] | [e.g., Service delivery confirmed] | RULE-B-003 | |

##### Illegal / Blocked Transitions

| From State | Forbidden To State | Reason / Constraint | Related RULE IDs |
|---|---|---|---|
| [Completed] | [Confirmed] | [Cannot re-confirm a completed booking] | RULE-A-001 |
| [Cancelled] | [Any] | [Terminal state - no further transitions allowed] | RULE-A-002 |

##### Entry / Exit Semantics

**[State A]:**
- On Entry: [What happens when this state is entered - notifications, locks, side effects]
- On Exit: [What happens when this state is left - cleanup, releases, downstream triggers]

**[State B]:**
- On Entry: [...]
- On Exit: [...]

##### Exception & Override Paths

- [Non-standard transitions available to specific roles, e.g., "Admin can force-cancel any booking in any non-terminal state"]
- [System-triggered exception paths, e.g., "If payment fails during capture, system reverts booking to Requested without requiring host re-approval"]
- [Time-based expiry paths, e.g., "If host does not respond within 48h, system auto-transitions to Expired"]

##### Coverage & Gaps

**Clear in documents:**
- [What is fully specified and agreed upon]

**Open questions:**
- [What remains unresolved - edge cases, rule conflicts, missing stakeholder input]

---

### Section 4 Update: Business Rules - [FS-ID]

*Add rows to the flat Business Rules Library table in Section 4.*

| Name | Rule ID | Category | Affected Entity | Description | Domain | Priority |
|---|---|---|---|---|---|---|
| [Rule name] | RULE-A-[ID] | A - Critical | ENT-[ID] | [Full rule statement] | [Domain name] | Critical |
| [Rule name] | RULE-B-[ID] | B - Core | ENT-[ID] | [Full rule statement] | [Domain name] | High |
| [Rule name] | RULE-C-[ID] | C - Governance | ENT-[ID] | [Full rule statement] | [Domain name] | Medium |

**Rule detail cards** (for RULE-A and significant RULE-B entries):

**RULE-A-[ID]: [Name]**
- Intent: [Why this rule must exist - what it protects]
- Invariant: "The system MUST NOT [X] / MUST always [Y]"
- Scope: [Which entities and states]
- Enforcement: [Block / Freeze / Alert / Reject]
- Violation handling: [What the system does if this is about to be violated]

**RULE-B-[ID]: [Name]**
- Intent: [What behavior this governs]
- Logic: "If [condition], then [outcome]"
- Edge cases:
  - [Edge case 1]: [Handling]
  - [Edge case 2]: [Handling]
- Related: [RULE-A-XXX / RULE-C-XXX]

---

### Section 5 Update: Decision Models - [FS-ID]

*Add rows to the Decision Models Catalogue in Section 5.*

| # | ID | Name | Domain | Notes | What is being decided | Type | Produces | Used in Process | Where in lifecycle | Uses Business Rules | Uses Scoring Models | Uses Other Decisions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [n] | DM-[ID] | [Decision name] | [Domain] | [Context] | [Decision question] | TBL | [Outcome options] | PROC-[ID] | [State + transition] | RULE-[IDs] | - | - |

---

### Section 6 Update: Business Events - [FS-ID]

#### 6.2 Event Catalogue - [FS-ID] entries

| Name | Category | Aliases | Business Meaning | Consumers | Lifecycle + State | Primary Entity | Producer | Related Rules/Decisions | Trigger Type | Related Decisions |
|---|---|---|---|---|---|---|---|---|---|---|
| [event.name] | [Lifecycle] | [alt names] | [What this event means in business terms] | [FS-XX, FS-YY] | [ENT-ID: State A → State B] | ENT-[ID] | [FS-ID] | RULE-[IDs] | Automatic | DM-[IDs] |

#### 6.3 Event Propagation Map - [PROC-ID]: [Process Name]

| Canonical Event | Producer | Primary Entity | Lifecycle + State Transition | Business Reaction | Triggered Decisions | Governing Rules | Notes |
|---|---|---|---|---|---|---|---|
| [event.name] | [FS-ID] | ENT-[ID] | [State A → State B] | [What the business expects to happen as a result] | DM-[ID] | RULE-[IDs] | |

**Downstream effects:**
- Entity side-effects: [Other entities whose state changes as a result of this event]
- Blocking/overrides: [What this event blocks or overrides in other processes]

---

### Section 10 Update: Open Questions - [FS-ID]

*Add rows to the Open Questions log in Section 10.*

| # | Question / Open Item | Owner | Status | Target date | Resolution |
|---|---|---|---|---|---|
| [n] | [Open question from this FS] | [TBD] | Open | [TBD] | - |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Phase 4 Skeleton must cover:**
- [ ] Section 0: purpose, scope, audience, notation, references, change log
- [ ] Section 1.1: Primary Roles table, Secondary Roles table, Motivations & Needs table, Multi-Role Logic
- [ ] Section 1.2: Inside (platform owns), Outside (platform does not own), External Systems table
- [ ] Section 1.3: Business Capability Map grouped by domain
- [ ] Section 1.4: Responsibility Split table (Platform / External / Manual)
- [ ] Section 2: State Machine Overview table - all entities with states and key transitions listed
- [ ] Section 3.1: Process Overview table (PROC-IDs, triggers, goals, affected lifecycles)
- [ ] Section 3.2: Orchestration Principles - ordering rules, blocking rules, override principles, fallback recovery
- [ ] Sections 4-10: structural placeholders with correct headers

**Phase 6 Detail per Feature Set must cover:**
- [ ] States Catalogue: State | Description | Terminal? Y/N | Notes
- [ ] Allowed Transitions: From | To | Trigger Type | Trigger Name | Conditions | Related RULE IDs | Notes
- [ ] Illegal / Blocked Transitions: From | Forbidden To | Reason | Related RULE IDs
- [ ] Entry / Exit Semantics: On Entry and On Exit per state
- [ ] Exception & Override Paths: role overrides, system exceptions, time-based expiry
- [ ] Coverage & Gaps: clear items + open questions
- [ ] Section 4 rows: flat table with Name | Rule ID | Category | Affected Entity | Description | Domain | Priority
- [ ] RULE-A detail cards: intent, invariant statement, scope, enforcement, violation handling
- [ ] RULE-B detail cards: intent, logic (if/then), edge cases, related rules
- [ ] RULE-C entries: policy statement, context, exception handling
- [ ] Section 5 rows: Decision Models Catalogue with all columns (Type, Produces, Used in, etc.)
- [ ] Section 6.2 rows: Event Catalogue with all columns (Aliases, Consumers, Lifecycle+State, etc.)
- [ ] Section 6.3: Event Propagation Map per process (Canonical Event | Producer | Primary Entity | Lifecycle | Business Reaction | Triggered Decisions | Governing Rules)
- [ ] Section 6.3 Downstream effects: entity side-effects and blocking/overrides

**Rule quality:**
- [ ] RULE-A rules: are truly non-negotiable (financial, legal, integrity) - not just important
- [ ] RULE-B rules: have at least one edge case documented
- [ ] RULE-C rules: actor and policy clearly identified
- [ ] No rule duplicates Domain Model content (attributes, enums)
- [ ] No rule defines API or UI behavior (belongs in FSD)

**For SaaS/AI products:**
- [ ] Multi-tenant isolation rules (RULE-A: tenant A cannot access tenant B data)
- [ ] AI output governance (RULE-C: AI suggestions must be reviewable by user before execution)
- [ ] Rate limiting rules (RULE-B: API quota management, per-tenant limits)
- [ ] Data retention rules (RULE-C: user data deletion cascade, per GDPR requirements)
- [ ] Subscription state machine if applicable (Trial → Active → Cancelled → Expired)

**Notion push completeness:**
- [ ] BRD page content pushed (Phase 4: set; Phase 6: appended, not overwritten)
- [ ] All RULE-A/B/C entries pushed to Business Rules DB
- [ ] All decision points pushed to Decision Models DB
- [ ] All business events pushed to Event Catalogue DB (one entry per event in the Business Events section)
- [ ] RULE-C compliance/data-governance entries pushed to Data Sensitivity DB
- [ ] Skipped DBs (blank URL) noted in summary

## Notion push

**Runs after user approves the BRD artifact.**

Read all relevant keys from `pureinn-variables.md`. Check `state.json notion_ids` for cached data source IDs. Fetch and cache any missing IDs via `notion-fetch` before pushing.

---

### 1. BRD page content

Read `pureinn-variables.md` key "BRD" → get page URL.

- **Phase 4 skeleton:** Push the full skeleton markdown as the BRD page body via `notion-update-page` (replace/set content).
- **Phase 6 per-FS section:** Append the new FS section to the existing BRD page body. Do not overwrite existing content - add the new section at the end.

If BRD URL is blank: save locally only, note in summary.

---

### 2. Business Rules DB

Read `pureinn-variables.md` key "Business Rules" → get DB URL. Cache data source ID in `state.json notion_ids.business_rules`.

Push one entry per RULE-A, RULE-B, and RULE-C defined in this run via `notion-create-pages`:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Rule name (e.g., "RULE-A-001: Payment Release Invariant") | BRD rule ID + name |
| `Artefact Type` | `"Business Rule"` | Fixed |
| `Short Description` | Rule statement (the invariant or logic line) | BRD rule statement |
| `Status` | `"Active"` | Fixed |
| Category property | `"Critical"` / `"Core"` / `"Governance"` | RULE-A/B/C |
| Feature Set reference | FS-ID if available | BRD FS scope field |

Skip if URL blank.

---

### 3. Decision Models DB

Read `pureinn-variables.md` key "Decision Models" → get DB URL. Cache in `state.json notion_ids.decision_models`.

Push one entry per decision point or branching logic in the BRD via `notion-create-pages`:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Decision name (e.g., "Booking Approval Decision") | BRD decision point |
| `Artefact Type` | `"Decision Model"` | Fixed |
| `Short Description` | Condition + outcome summary (e.g., "If host approves within 24h → Confirmed; else → Expired") | BRD logic |
| `Status` | `"Active"` | Fixed |

Skip if URL blank.

---

### 4. Event Catalogue DB

Read `pureinn-variables.md` key "Event Catalogue" → get DB URL. Cache in `state.json notion_ids.event_catalogue`.

Push one entry per business event defined in the BRD "Business Events" section via `notion-create-pages`:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Event name (e.g., `booking.confirmed`) | BRD event name |
| `Artefact Type` | `"Event"` | Fixed |
| `Short Description` | Trigger + business meaning (1 sentence) | BRD event description |
| `Status` | `"Active"` | Fixed |
| Producer | Feature Set that emits this event | BRD events table |
| Consumers | Feature Sets that consume this event | BRD events table |

Skip if URL blank.

---

### 5. Data Sensitivity DB

Read `pureinn-variables.md` key "Data Sensitivity Map" → get DB URL. Cache in `state.json notion_ids.data_sensitivity_map`.

Push one entry per RULE-C rule that has compliance, data-retention, or data-governance context via `notion-create-pages`:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Rule name (e.g., "RULE-C-003: User Data Deletion on Account Close") | BRD RULE-C ID + name |
| `Artefact Type` | `"Data Governance Rule"` | Fixed |
| `Short Description` | Policy statement from the rule | BRD RULE-C policy |
| `Status` | `"Active"` | Fixed |
| Context | `"Compliance"` / `"Retention"` / `"GDPR"` / `"Operations"` | BRD RULE-C context field |

Only push RULE-C entries that have a compliance, retention, or data-handling context. Skip pure UX/policy rules. Skip if URL blank.

---

### 6. Confirm

After all pushes: report counts per target (BRD page updated, Business Rules created, Decision Models created, Events created, Data Governance Rules created, errors). Note any targets skipped due to missing URL in pureinn-variables.md.

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-4/brd-skeleton.md
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-brd.md
```
