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
- `pm-feature-card` - Feature Cards are derived from FSD acceptance criteria (one per F-ID)
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

GROUP 1 OF 3 - Scope & Context

1. FEATURE SET PURPOSE
   What is this Feature Set's core responsibility?
   What business problems does it solve?
   Which BRD rules does it directly enforce?
   [describe]

2. SCOPE BOUNDARIES
   What is explicitly IN scope for this FS?
   What is explicitly OUT of scope - and which FS handles each out-of-scope area?
   [list both]

3. DEPENDENCIES
   Which other Feature Sets does this FS depend on (upstream)?
   Which Feature Sets depend on this FS (downstream)?
   What external services does this FS call?
   [list with dependency type: synchronous / blocking / lifecycle / produces events]

Confirm Group 1, then continue to Group 2.

---

GROUP 2 OF 3 - Behavior & Events

4. EXECUTION FLOWS
   Walk me through the main flow - step by step at business level:
   - What triggers it? (user action, system event, API call, scheduled job)
   - What entities are created or updated?
   - What are the decision points and guard conditions?
   - What happens on success? On failure?
   Also describe key edge cases and exceptional scenarios.

5. VALIDATIONS & GUARDS
   What validations are required?
   - Input validations (format, presence, range)
   - Business validations (state checks, constraint enforcement)
   For each: what is the condition, and what is the business outcome on failure?

6. EVENTS
   What events does this FS produce? (canonical name, business trigger, meaning)
   What events does it consume? (from which FS, in what lifecycle state)
   Any idempotency concerns? (e.g., what if an event is processed twice)
   Any ordering requirements? (e.g., event A must precede event B)

Confirm Group 2, then continue to Group 3.

---

GROUP 3 OF 3 - Non-Functional & Observability

7. NON-FUNCTIONAL EXPECTATIONS
   Performance: any time-sensitive operations (e.g., "must complete before checkout times out")?
   Latency: anything that must respond in real-time during user interaction?
   Consistency: where must the same inputs always produce the same result?
   Accuracy: where is approximation or soft validation not acceptable?

8. OBSERVABILITY & OPERATIONS
   What are the 3 most important signals that indicate this FS is working / broken?
   What metrics define success for this FS? (conversion rate, rejection rate, etc.)
   What alert-worthy conditions should ops watch for?
   What should support know when users report issues with this FS?
```

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Functional Specification Document

```markdown
# FSD - [FS-ID]: [Feature Set Name]

---

## 0) Document Meta

| Field | Value |
|---|---|
| Feature Set | [Feature Set Name] |
| Version | Version 1 |
| Owner | [Product / Team] |
| Status | Draft / Approved / Implemented |
| Related BRD Sections | [RULE IDs and BRD Section references] |
| Related Domain Entities | [ENT-IDs] |

---

## 1) Purpose & Context

### 1.1 Purpose

Feature Set **[Name]** is [1-2 sentence business description of what this FS does and why it exists].

This Feature Set addresses the following business problems:
- **[Problem 1]:** [What it prevents or ensures]
- **[Problem 2]:** [What lifecycle it initializes or manages]
- **[Problem 3]:** [What data integrity or constraint it enforces]

It implements the logic defined in the BRD for the [relevant process], specifically enforcing [RULE-ID-1], [RULE-ID-2], and [RULE-ID-3].

### 1.2 Business Context

This Feature Set is part of the core **[Process Name]** process.

It affects and initiates the following lifecycle phases:
- **ENT-[Entity] Lifecycle:** [Initializes / Manages / Terminates] the lifecycle by [creating/transitioning] entities to state [STATE].
- **ENT-[Entity] Lifecycle:** [What this FS does to this entity]

It serves as a prerequisite for [downstream Feature Sets]: [FS-Name] (for [purpose]) and [FS-Name] (for [purpose]).

### 1.3 In Scope / Out of Scope

**In Scope:**
- **[Responsibility 1]:** [Detailed description of what this FS owns end-to-end]
- **[Responsibility 2]:** [Specific operation with entity/rule reference]
- **[Responsibility 3]:** [What lifecycle management this FS handles]
- **[Responsibility 4]:** [Housekeeping, expiry, or cleanup this FS owns]

**Out of Scope:**
- **[Excluded area 1]:** [Falls under [FS Name]]
- **[Excluded area 2]:** [Falls under [FS Name]]
- **[Excluded area 3]:** [Falls under [FS Name] - specifically the transition from [STATE A] to [STATE B]]

---

## 2) References & Dependencies

### 2.1 Referenced Business Rules

| Rule ID | Name | Why enforced here |
|---|---|---|
| RULE-[ID] | [Rule name] | [Why this FS enforces this rule at this point - not just what the rule says] |
| RULE-[ID] | [Rule name] | [Why this FS enforces this rule at this point] |

### 2.2 Referenced State Machines

**Entity: ENT-[Name]**
- Lifecycle: [Lifecycle Name]
- Relevant states / transitions:
  - Initial State: (null) → [STATE]
  - State: [STATE]

**Entity: ENT-[Name]**
- Lifecycle: [Lifecycle Name]
- Relevant states / transitions:
  - Initial State: (null) → [STATE]
  - State: [STATE]

### 2.3 Referenced Domain Entities

| Entity | Attributes Used | Access (R/W) |
|---|---|---|
| ENT-[Name] | [attr1, attr2, attr3] | W |
| ENT-[Name] | [attr1, attr2] | R |
| EXT_ENT-[Name] | [external entity attributes used] | R |

### 2.4 Dependencies on Other Feature Sets

| Feature Set | Dependency Type | Description |
|---|---|---|
| [FS Name] | Synchronous dependency | [Must complete before this FS can proceed - e.g., geo validation is a prerequisite] |
| [FS Name] | Blocking dependency | [This FS is blocked if the dependency is unavailable or incomplete] |
| [FS Name] | Lifecycle dependency | [This FS produces data consumed by downstream FS as its input] |
| [FS Name] | Produces events | [This FS emits events that initiate downstream FS behavior] |

---

## 3) Responsibilities & Boundaries

### 3.1 Core Responsibilities

- **[Responsibility 1]:** [What entity this FS creates or initializes; what identifier is assigned]
- **[Responsibility 2]:** [What entities are validated, created, and linked to what parent]
- **[Responsibility 3]:** [What external dependency is called; what validation it performs; what attribute is checked]
- **[Responsibility 4]:** [What business rules are enforced and against which entity attributes]
- **[Responsibility 5]:** [What lifecycle management this FS owns - expiry, housekeeping, TTL]

### 3.2 Explicit Non-Responsibilities

- **This Feature Set does NOT calculate [X]:** [Calculation of [Y] falls under [FS Name]]
- **This Feature Set does NOT [Action]:** [Responsibility for [Z] belongs to [FS Name]]
- **This Feature Set does NOT [Action]:** [The transition from [STATE A] to [STATE B] is handled by [FS Name] after [prerequisite]]
- **This Feature Set does NOT [confirm / finalize / deliver]:** [The atomic promotion from [STATE] requires [condition] and is managed in [FS Name]]

### 3.3 Assumptions & Constraints

**Assumptions:**
- **[Assumption 1]:** [What actor or service is assumed to be authenticated/available before this FS runs]
- **[Assumption 2]:** [What external service is assumed functional and what it returns]
- **[Assumption 3]:** [What configuration or reference data is assumed to exist]

**Constraints:**
- **[Constraint 1]:** [A geographic, temporal, or category restriction this FS operates within]
- **[Constraint 2]:** [A time limit or TTL that governs lifecycle of entities created here]
- **[Constraint 3]:** [A data integrity rule that cannot be violated at creation time]

---

## 4) Functional Behavior (BUSINESS-LOGIC VIEW)

### 4.1 Entry Points / Triggers

| Trigger | Source | Meaning |
|---|---|---|
| [User initiates action] | User ([Role]) | [User begins process; system initializes entity in initial state] |
| [External system request] | Partner API / External System | [External payload arrives; enters same validation flow before entity creation] |
| [System event fires] | System Timer | [TTL expiry or scheduled job triggers housekeeping/lifecycle management] |
| [User modifies draft/pending entity] | User ([Role]) | [Change to existing unconfirmed entity requires re-validation of affected fields] |

### 4.2 Main Business Flow

1. **[Step 1 Name]:** [System creates the initial entity in [STATE]. If initiator is external, assigns [external_key] for idempotency and correlation.]

2. **[Step 2 Name]:** [System accepts [input type]. Performs [normalization/conversion]. If input is ambiguous, flow pauses and requests clarification from user.]

3. **[Step 3 Name]:** [System checks [attribute] is within [allowed scope]. If check fails, flow does not continue - [specific outcome].]

4. **[Step 4 Name]:** [System accepts [entity parameters]. Creates [child entity] in [STATE] linked to parent. Immediately validates against [limits/rules].]

5. **[Step 5 Name]:** [System checks [logical integrity] of [field set]. [Condition] must hold. Reference: [RULE-ID].]

6. **[Step 6 Name]:** [If all inputs pass, system marks entity as valid. This ends this FS's responsibility. Data is ready for [downstream FS].]

### 4.3 Validations & Guards

| Validation | Condition | Business Outcome |
|---|---|---|
| [Validation Name] | [What must be true - entity attribute / service result / rule check] | [If fails: flow blocked, what error is returned, what state entity remains in] |
| [Validation Name] | [Constraint from RULE-ID: attribute must be within limit] | [If fails: system requires correction; entity not advanced to next step] |
| [Validation Name] | [Logical integrity check between two fields] | [If fails: system prevents saving the invalid combination] |
| [Idempotency Check] | [Unique key must not already exist for a completed entity] | [If duplicate: system returns existing record; no new entity created] |

### 4.4 Edge Cases & Exceptional Scenarios

- **[Unresolvable / Ambiguous Input]:** [External service returns low confidence or multiple candidates. System returns validation error. User must manually select or correct. Entity remains in invalid state - cannot advance.]

- **[Input Out of Configured Boundary]:** [Input passes format validation but fails geographic/zone/category check. System immediately informs user. Entity creation is blocked (Hard Guard).]

- **[External Request with Invalid Data]:** [API payload contains structurally invalid values. System rejects immediately. No entity created to avoid polluting the database with invalid records.]

- **[Conflicting Temporal / Scheduling Input]:** [User provides time values that violate ordering or operational window constraints. System rejects the specific fields. If earliest valid time can be inferred, system suggests it and notifies user.]

- **[Expiry / Housekeeping]:** [User abandons the process and does not return within [TTL]. Background job identifies the entity per [RULE-ID] and performs logical deletion or archival to free resources.]

---

## 5) Events & Reactions

### 5.1 Events Produced

| Event (Canonical) | When (business trigger) | Meaning (business fact) |
|---|---|---|
| `[entity.event_created]` | [User or external system successfully provides all valid inputs; all guards pass] | [Entity ENT-X was initialized in [STATE] with valid [data context]; ready for [downstream process]] |
| `[entity.event_confirmed]` | [External request passes all validation checks atomically] | [Draft or request was promoted to confirmed entity in [STATE] and assigned internal ID] |

### 5.2 Events Consumed

| Event (Canonical) | From (Producer) | Expected Context (business preconditions / lifecycle state) |
|---|---|---|
| `[entity.event_from_upstream]` | [FS Name / External System] | [What must be true when this event is received. What entity state is expected. What check is performed before acting on it.] |

### 5.3 Idempotency & Ordering Expectations

**A) Idempotency expectations (business-level)**

| Event (Canonical) | If processed twice... | Business-safe expectation (no duplicate effect) |
|---|---|---|
| `[entity.event_created]` | [User or client sends duplicate creation request with same parameters in short time] | [System returns existing entity ID if inputs match, rather than creating duplicate record] |
| `[external.event_received]` | [External system retries on network failure] | [System identifies duplicate on unique external key and returns existing record without creating new entity] |

**B) Ordering expectations (business-level)**

| Entity / Lifecycle | Relevant Events | Expected ordering (business view) | What if out-of-order (business reaction) |
|---|---|---|---|
| [ENT-X Lifecycle] | [EventA] → [EventB] → [EventC] | [Entity must be in [STATE] before [EventB] can be processed. [EventA] must precede [EventC].] | **Ignore:** If [EventA] arrives for an entity already in [STATE B/C], ignore it - lifecycle has already progressed. |

---

## 6) State Interactions

| Entity | From State | To State | Condition |
|---|---|---|---|
| ENT-[Name] | (null) | [STATE A] | [Initialization trigger AND successful [validation] per [RULE-ID]] |
| ENT-[Name] | (null) | [STATE B] | [Validation of [constraint] AND [constraint] per [RULE-ID] AND [RULE-ID]] |
| ENT-[Name] | [STATE A] | [CANCELLED / EXPIRED] | [TTL expiry per [RULE-ID]] |

---

## 7) Acceptance Criteria

### AC-01 - [Happy Path Name]

- **Given** [Actor is authenticated as [Role]; relevant preconditions are true]
- **When** [Actor provides all valid inputs: [list what is valid]]
- **Then** [System creates entity ENT-X in [STATE]]
  - **And** [System performs [validation] and confirms [condition] per [RULE-ID]]
  - **And** [Related entity ENT-Y created in [STATE] linked to parent]

### AC-02 - [Failure: Validation 1]

- **Given** [Actor initiates process]
- **When** [Actor provides [field] that fails [validation condition]]
- **Then** [System does NOT create or advance entity]
  - **And** [System returns error requiring correction per [RULE-ID]]

### AC-03 - [Failure: Validation 2]

- **Given** [[Dependent validation] has passed]
- **When** [System evaluates [field/attribute] and finds it outside allowed [scope/limit]]
- **Then** [System blocks continuation of process]
  - **And** [Entity remains in [STATE] (or is not created); cannot advance to [next step], per [RULE-ID]]

### AC-04 - [Constraint Violation]

- **Given** [Actor defines [entity parameters]]
- **When** [[Field] exceeds maximum limit defined for [constraint]]
- **Then** [System rejects creation or update of [child entity]]
  - **And** [System requires correction per [RULE-ID] before draft can be saved]

### AC-05 - [Idempotency / Deduplication]

- **Given** [External system sends request with [unique key]]
- **When** [[Unique key] already exists assigned to another entity]
- **Then** [System does NOT create new entity]
  - **And** [System returns existing entity (or its status) to ensure idempotency per [RULE-ID]]

### AC-06 - [Expiry / Housekeeping]

- **Given** [Entity exists in [STATE]]
- **When** [[TTL] elapses since last update without [completion action]]
- **Then** [System marks entity as invalid / archived]
  - **And** [Actor can no longer advance this entity; must start process again per [RULE-ID]]

---

## 8) Non-Functional Expectations

### 8.1 Performance

- **[Critical User Flow Guard]:** [The [validation/processing] step must complete within a time window that does not jeopardize the overall [KPI], otherwise [conversion risk - e.g., abandon rate increases].]
- **[High-Volume Scenario]:** [When processing [batch/B2B] requests, system must handle [volume] without blocking interactive users, ensuring fairness between [segments].]

### 8.2 Latency

- **[Interactive Operation]:** [[Validation] must provide real-time feedback during user interaction to prevent continuation with invalid data. Delay at this point directly blocks [conversion step].]
- **[Optimization Opportunity]:** [For repeated requests, system should prioritize cached/reused [data type] per [RULE-ID] instead of re-calling external services.]

### 8.3 Consistency

- **[Validation Determinism]:** [The same combination of input parameters must always produce the same validation result. System must not accept an entity in one session and reject identical inputs in another, unless global configuration has changed.]
- **[Creation Idempotency]:** [Repeated creation requests with the same parameters must not produce duplicate entities. System must return existing [entity_id] to preserve data integrity for downstream processes.]

### 8.4 Accuracy

- **[Input Resolution Precision]:** [Accuracy of [geocoding / classification / measurement] must be sufficient for unambiguous [zone determination / categorization / pricing]. If confidence is low, system must request correction from user rather than proceeding with an approximate result that would cause [downstream failure].]
- **[Constraint Validation Strictness]:** [Validation of [dimensions / amounts / limits] must be strict against defined [vehicle / tier / policy] limits. Soft validation (warning only) represents a risk that [Matching Engine / Pricing Engine / Fulfillment] assigns the entity to an executor that cannot fulfill it.]

---

## 9) Operational & Observability Notes

### 9.1 Business Signals

| Signal | What it indicates | Why it matters |
|---|---|---|
| High [Validation Failure] Rate | [Users or partners providing [input type] that fails [validation check]] | [Indicates UX problem with input quality, or outage of external service, directly blocking new [entity] creation] |
| [Boundary Rejection] Spike | [Increased rejections due to [zone / category / limit] guard] | [Signals marketing misalignment, misconfigured [boundaries/limits], or abuse attempt] |
| High [Abandonment / Expiry] Rate | [Entities reaching TTL without [completion]] | [Key funnel health signal - high rate means validation is too strict or downstream [pricing/UX] creates friction] |
| [External Partner] Rejection Spike | [B2B API requests failing validation at elevated rate] | [Partner likely changed payload format or sends invalid data - threatens B2B volume and relationship] |

### 9.2 Key Metrics

| Metric | What it measures | Business Interpretation |
|---|---|---|
| [FS Success Conversion %] | [Ratio of initiated flows to successfully completed entities] | [Efficiency of this FS. Decline indicates friction in validation or input data quality.] |
| [[Input] Validation Success Rate] | [% of [inputs] that pass on first attempt without user correction] | [UX quality for [input type] and reliability of [external dependency].] |
| [Partner API Rejection Rate] | [% of B2B requests rejected due to validation errors] | [Health of B2B integrations. High rate indicates bad partner data or broken API contract.] |
| [Prohibited / Out-of-Bounds Attempt Count] | [Number of blocked attempts to [violate constraint]] | [Compliance risk exposure and misunderstanding of service scope.] |

### 9.3 Alert-Worthy Conditions

| Condition | Why it is alarming | Potential business impact |
|---|---|---|
| Zero Successful [Entities] ([Region/Segment]-wide) | [[Process] stopped producing valid entities in [area] despite normal traffic] | [Critical outage of [external service] or [config] error - completely stops business for [segment]] |
| Sudden Spike in [Partner/API] Rejections | [Key partner sending invalid data or changed format] | [Threatens [order/transaction] volume and partner relationship] |
| Abnormal [Dimension/Parameter] Values | [Series of requests with extreme values from single IP/account] | [Possible abuse of validation engine (DoS-style) or limit testing by bad actor] |
| Recurring [Boundary/Threshold] Mismatches | [High % of valid inputs just outside configured limit] | [Signal for Operations to review [zone/limit/configuration] - potential lost revenue] |

### 9.4 Operational Notes

- **Gatekeeper role:** Operations must understand this FS as a quality filter. Relaxing any validation (e.g., disabling [constraint]) will cause downstream failures: [specific consequence in delivery/pricing/fulfillment].
- **[External service] dependency:** When users report "[cannot complete action]", support must first verify whether [external service] can resolve the input and whether it falls within allowed [zone/category]. This is the most common failure point.
- **[Entity] TTL & Support:** Support must know that [entities] are automatically [deleted/archived] after [TTL]. Users reporting "missing [entity]" after [time window] should be informed of [RULE-ID].
- **Financial risk:** Input validation at this stage directly affects accuracy of [downstream pricing/matching]. If [FS Name] passes inaccurate [dimensions/location], the platform may absorb cost of [mis-priced/unfulfilled delivery].

---

## 10) Open Questions & Pending Decisions

| # | Question / Open Item | Owner | Status | Target date | Resolution |
|---|---|---|---|---|---|
| 1 | [TBD] | [TBD] | Open | [TBD] | - |

---

## 11) Working Notes (Engineering Playground)

> This section is NOT a binding specification. It is a collaboration space for engineering.
> May contain: API sketches, endpoint drafts, payload examples, diagrams, technical notes, experiments.
> Content here does not replace Tech Specs or ADRs.
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Section 0 - Document Meta:**
- [ ] Feature Set, Version, Owner, Status, Related BRD Sections, Related Domain Entities all filled

**Section 1 - Purpose & Context:**
- [ ] 1.1 Purpose: business problem statement + BRD rules referenced
- [ ] 1.2 Business Context: process named; affected lifecycles listed; prerequisite relationship to downstream FSes stated
- [ ] 1.3 In Scope: detailed bullet list; each item names entities/rules involved
- [ ] 1.3 Out of Scope: each item explicitly names which FS handles it

**Section 2 - References & Dependencies:**
- [ ] 2.1 All referenced BRD rules listed with explanation of why enforced here (not just rule name)
- [ ] 2.2 All relevant entities listed with lifecycle name and relevant states/transitions
- [ ] 2.3 All domain entities listed with specific attributes used and R/W access
- [ ] 2.4 All upstream and downstream FSes listed with dependency type

**Section 3 - Responsibilities & Boundaries:**
- [ ] 3.1 Core Responsibilities: each item names entity + rule + operation owned
- [ ] 3.2 Explicit Non-Responsibilities: each item names which FS handles it instead
- [ ] 3.3 Assumptions & Constraints: both sub-sections present with multiple entries each

**Section 4 - Functional Behavior:**
- [ ] 4.1 All triggers listed (user, external, system/scheduled)
- [ ] 4.2 Main flow: numbered, each step named; rules referenced inline
- [ ] 4.3 Validations: all guards as table rows; each with condition + business outcome on failure
- [ ] 4.4 Edge cases: all exception paths covered; guard type noted (hard/soft); user outcome described

**Section 5 - Events & Reactions:**
- [ ] 5.1 All events produced: canonical name + business trigger + meaning as business fact
- [ ] 5.2 All events consumed: producer named + expected lifecycle state specified
- [ ] 5.3A Idempotency: each repeatable event has a business-safe expectation defined
- [ ] 5.3B Ordering: event sequences defined; out-of-order behavior specified (Ignore / Reject / Buffer)

**Section 6 - State Interactions:**
- [ ] All state transitions this FS is responsible for listed
- [ ] Each transition: entity + from state + to state + condition with rule reference

**Section 7 - Acceptance Criteria:**
- [ ] AC numbered sequentially (AC-01, AC-02, ...)
- [ ] Given/When/Then/And format strictly followed
- [ ] Minimum: happy path + each major validation failure + idempotency + expiry/housekeeping
- [ ] "Then" statements are observable and testable without knowledge of internals
- [ ] Each AC references the RULE-ID it validates

**Section 8 - Non-Functional Expectations:**
- [ ] 8.1 Performance: at least one requirement with business justification (KPI at risk)
- [ ] 8.2 Latency: interactive operations and cache/reuse opportunities
- [ ] 8.3 Consistency: determinism and idempotency requirements
- [ ] 8.4 Accuracy: where soft validation is insufficient and why (downstream impact)

**Section 9 - Operational & Observability:**
- [ ] 9.1 Business Signals: 3+ signals (Signal | What it indicates | Why it matters)
- [ ] 9.2 Key Metrics: 3+ metrics (Metric | What it measures | Business Interpretation)
- [ ] 9.3 Alert-Worthy Conditions: table with conditions that need immediate ops attention
- [ ] 9.4 Operational Notes: bullet list covering ops/support key knowledge

**Does NOT duplicate BRD or Domain Model:**
- [ ] No business rule text repeated from BRD - reference RULE-ID only
- [ ] No entity attribute definitions - reference Domain Model
- [ ] No UI/UX descriptions - reference Design docs
- [ ] No API endpoint definitions - reference Tech Specs / ADRs

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
