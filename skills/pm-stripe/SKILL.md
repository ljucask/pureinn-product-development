---
name: pm-stripe
description: JIT Delivery Stripe session orchestrator. Run every time you sit down to work on Phase 6-7. Reads current state across all active stripes, detects where each feature is in the lifecycle, surfaces the right next action, and routes you to the correct skill. One stripe = one isolated development channel. Features process one at a time per stripe in dependency order.
license: MIT
metadata:
  agent-mode: never
  author: https://github.com/ljucask
  version: "3.2.0"
  domain: product-management
  triggers: stripe, delivery stripe, JIT cycle, feature design, build feature, impact analysis, security review, delivery plan, build order, sequence, parallel, Phase 6, Phase 7, next feature
  role: orchestrator
  scope: delivery
  output-format: document
  related-skills: pm-feature-viability, pm-feature-design, pm-feature-card, pm-mvp-scope, pm-entity-registry
---

# PM - Delivery Stripe


## Agent mode (`--agent`)

This skill's value is the live dialogue - `--agent` is not supported. If invoked with `--agent`, warn once ("this skill needs interactive back-and-forth; agent mode would hollow it out") and proceed interactively.

---

## What this skill does

**Run this every time you sit down to work on Phase 6-7.** It is not a one-time setup skill - it is your session start point.

pm-stripe reads the current state of all active stripes, detects where each active feature is in the lifecycle, and tells you exactly what to do next. It routes you to the right skill at the right moment.

**Division of responsibility:**
- `features/feature_list.md` - source of truth for feature inventory, priority, stripe assignment, dependency order
- `/features/cards/FEAT-*.md` - source of truth for feature status and spec content
- **This skill** - session orchestrator: detects state, routes to right skill, tracks transitions, runs Impact Analysis

**Full feature lifecycle:**

| Status | Meaning | Who sets it |
|---|---|---|
| `1_Backlog` | In queue, design not started | pm-features-list (auto) |
| `2_Spec_Done` | JIT spec complete (Sections 1-3 written), awaiting design inspection | pm-feature-design |
| `2b_In_Design` | **(optional - frontend features only)** UI / Figma design being produced | pm-feature-design / designer |
| `3_Ready_to_Build` | Design inspection approved, ready to enter build | pm-stripe (human confirms) |
| `4_In_Build` | Build skills actively working on this feature | pm-stripe |
| `5_In_Review` | Build complete, code review in progress | pm-stripe |
| `6_Shipped` | Complete - code reviewed, Section 4 filled, Feature Card immutable | pm-stripe |

**JIT cycle (per feature, per stripe):**
1. `1_Backlog` → run `/pm-feature-design FEAT-[ID]` → `2_Spec_Done`
2. `2_Spec_Done` → design inspection (human review of Sections 1-3) → `3_Ready_to_Build`
   - **frontend feature whose Figma design is not yet done:** `2_Spec_Done → 2b_In_Design` (produce/approve the UI design) → `3_Ready_to_Build`. Backend/system features skip `2b_In_Design` - nothing to design.
3. `3_Ready_to_Build` → run build skills → `4_In_Build`
4. `4_In_Build` → build complete → `5_In_Review`
5. `5_In_Review` → code review passed, Section 4 filled → `6_Shipped`

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - features must be assigned to stripes in feature_list.md and Feature Card frontmatter
- All Feature Cards must exist as stubs (status: `1_Backlog`) in `/features/cards/`

**Produces artifacts used by:**
- Feature Cards (status updates throughout lifecycle)
- `feature_list.md` (status column updated)
- Build skills - always: fullstack-guardian (build), code-reviewer (review). Conditional by trigger: test-master, impeccable-craft/impeccable-audit, playwright-expert, secure-code-guardian, security-reviewer (see Step 1C/1D and the Security Review Trigger Criteria)

---

## Step 0: Session start - Notion sync + read state

**Notion Status Sync (run first, before reading local files):**

1. Read `pureinn-workspace/[slug]/pureinn-variables.md` - check if "Feature Backlog" URL is present
2. **If URL is blank or Notion MCP not available:** skip sync, continue with local `.md` files as source of truth. No error, no blocking.
3. **If URL is present and Notion is available:**
   - Query the Feature Backlog DB for all features in the current stripe(s)
   - For each feature: compare Notion `Status` field with `.md` frontmatter `status`
   - If drift detected: update `.md` frontmatter to match Notion status, log the change:
     ```
     Notion sync: FEAT-[ID] status updated [old] → [new] (Notion was ahead)
     ```
   - After sync, continue with updated `.md` files

**Why Notion wins:** Status changes made by PMs or teammates in Notion (e.g., moving a feature to `3_Ready_to_Build` after design review) are the authoritative team signal. Content (Sections 1-3-4) stays in `.md` - Claude owns that.

---

Read `features/feature_list.md` and scan all `/features/cards/FEAT-*.md` files.

**Re-entry detection:** Before showing the dashboard, check each stripe for features NOT at `1_Backlog` or `6_Shipped`. These are mid-cycle features that need attention:

- Feature at `2_Spec_Done`: design was written but inspection hasn't happened yet
- Feature at `3_Ready_to_Build`: inspection passed but build hasn't started yet
- Feature at `4_In_Build`: build was started but hasn't been marked complete
- Feature at `5_In_Review`: build completed but code review hasn't concluded

If any mid-cycle feature is found, surface it prominently at the top of the dashboard with a clear action prompt.

**Compute and show the Delivery Plan** (full spec: "Delivery Plan - computation, rules, materialization" section below). Compute the schedule from the current state, then render it. Two render modes, same computation:

- **NOW render (default, steady state):** what is buildable right now + what is blocked and why. This is the daily driver.
- **FULL render (first run / on request / pre-dev walkthrough):** the whole structure - every stripe's ordered queue, the parallel waves, cross-stripe sync points. Use it at plan birth (first `/pm-stripe` after Phase 5 / after rebuild extract-reconcile) and whenever someone asks "show me the whole plan".

**NOW render:**

```
DELIVERY PLAN - [Product Name]        recomputed [date] · [N] shipped / [M] remaining
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ ACTION NEEDED:
  [stripe-name] FEAT-[ID]: [title] - Status: [current] → [next action]

▶ BUILDABLE NOW (parallel across stripes):
  [stripe-name]   FEAT-[ID]  [title] (P[n])
                  ✓ Ready: deps met · lane free · no contention
  [stripe-name]   FEAT-[ID]  [title] (P[n])
                  ✓ Ready: deps met · lane free · no contention

⛔ BLOCKED (why):
  [stripe]   FEAT-[ID]  [title]
             [one rationale line - see grammar below]
  [stripe]   FEAT-[ID]  [title]
             Dependency: waiting for FEAT-[X] to ship (Context: [dep reason])
```

**FULL render** additionally prints each stripe's full ordered queue, the wave grouping (`Wave 1: A · B · C`), and the cross-stripe sync points, plus a Mermaid swimlane (stripe = lane, `→` = dependency). See the computation section for the exact shape.

After rendering, **materialize** `delivery_plan.md` to the repo root and **write `plan_order`/`wave` back** (see materialization below). Then use AskUserQuestion tool based on what's detected:

**If one clear action is obvious** (e.g., one feature at 3_Ready_to_Build): use AskUserQuestion tool with:
- Question: "What do you want to do?"
- Option A: "[Specific next action for the detected feature] (Recommended)"
- Option B: "Different stripe - choose which"
- Option C: "Impact Analysis - a business rule changed"
- Option D: "Something else - I'll describe"

**If no active features or multiple stripes need attention:** use AskUserQuestion tool with:
- Question: "What do you want to do?"
- Option A: "Advance next feature - pick a stripe (Recommended)"
- Option B: "Impact Analysis - a business rule changed"
- Option C: "Close a completed stripe"
- Option D: "Check specific feature or stripe status"

---

## Step 1A: Start JIT design (1_Backlog → 2_Spec_Done)

Feature is at `1_Backlog`, all dependencies met, no other feature in stripe is active.

**READY check before routing:**
- Status: `1_Backlog` ✓
- All dependencies: `6_Shipped` ✓
- No other feature in same stripe at `2_Spec_Done`, `3_Ready_to_Build`, `4_In_Build`, or `5_In_Review` ✓

Show:
```
Next feature in [stripe-name]:

  FEAT-[ID]: [title]
  Priority: [P1/P2/P3]
  Dependencies: all met ✓
  PRD reference: [prd_ref from frontmatter]

→ Starting JIT design. Run:
  /pm-feature-design FEAT-[ID]
```

After pm-feature-design completes: Feature Card status becomes `2_Spec_Done`.

---

## Step 1B: Design Inspection (2_Spec_Done → 3_Ready_to_Build)

Feature Sections 1-3 are written. Human reviews before build starts.

Show what to review:
```
Design Inspection - FEAT-[ID]: [title]

Review Feature Card /features/cards/FEAT-[ID].md:

  Section 1 - Biznis Mantinely
    [ ] BR-IDs referenced and correct
    [ ] Entity guard conditions specified
    [ ] Edge cases covered

  Section 2 - Acceptance Criteria
    [ ] ACs are observable (Given/When/Then format)
    [ ] Happy path covered
    [ ] Guard failures covered (what happens when AC fails)

  Section 3 - JIT Technical Design
    [ ] Sequence diagram present and logical
    [ ] All actors/services match real codebase
    [ ] Files to modify listed

  UX/UI context (if UI feature)
    [ ] Placement in app described
    [ ] Design system reference present or Figma link provided
```

Use AskUserQuestion tool with:
- Question: "Design Inspection result for FEAT-[ID]?"
- Option A: "Approved - all sections complete and correct (Recommended if reviewed)"
- Option B: "Changes needed - I'll describe what to fix"
- Option C: "Re-run pm-feature-design - significant rework needed"

If approved: update Feature Card frontmatter `status: 3_Ready_to_Build`.

```
✅ Design inspection passed. FEAT-[ID] is ready to build.

Spec gate: PASSED
  Section 1 (Biznis Mantinely): ✓
  Section 2 (Acceptance Criteria): ✓
  Section 3 (JIT Technical Design): ✓

→ Next: start build (Step 1C)
```

---

## Step 1C: Start Build (3_Ready_to_Build → 4_In_Build)

Spec gate passed. Route to build skills.

Update Feature Card frontmatter `status: 4_In_Build`.

Build skills split into **always** and **conditional**. The conditional ones have an explicit trigger - do not treat them as optional-by-vibe. Read the Feature Card frontmatter (`layer`, `kano`, `priority`, `security_review`) to resolve each trigger before routing.

> **The build/review skills below are external and recommended-not-required.** `fullstack-guardian`, `secure-code-guardian`, `security-reviewer`, `code-reviewer`, `test-master`, `playwright-expert` and `impeccable-craft`/`impeccable-audit` are **not part of the Pureinn plugin** - they ship from separate marketplaces (`fullstack-dev-skills`, `impeccable`) and must be installed separately. Pureinn recommends them as sensible defaults. What the framework actually owns is the **orchestration**: *when* to build/review, the *trigger* that makes a specialist applicable, the *context-briefing*, and the *coverage check* - not a mandated tool. The concrete executor is swappable: if you run your own build/review workflow (or plain Claude Code without a named specialist), the triggers and the coverage check still apply - map each always/conditional slot to whatever executes it. If a routed skill isn't installed, say so and offer the built-in path rather than failing.

```
Build started for FEAT-[ID]: [title]
Status: 4_In_Build

Build instructions - read in this order:
  1. /features/cards/FEAT-[ID].md - Section 3 defines what to build
  2. /domain/entities.md - guard conditions for state transitions
  3. /domain/business_rules.md - BR-IDs referenced in Section 1
  4. /domain/decision_models.md - TBL-IDs for edge case test generation
```

**Always run (every feature):**

| Skill | Purpose |
|---|---|
| `/fullstack-guardian FEAT-[ID]` | Full-stack implementation |

**Conditional - run when the trigger is met:**

| Skill | Trigger (from frontmatter / criticality) |
|---|---|
| `/test-master FEAT-[ID]` | **Always for `priority: P1` or `kano: Must-be`.** P2 → happy path + guard tests. P3 pure CRUD may skip, but the coverage check (Step 1D) will flag it. Test-master is not "optional" - it is the default; skipping is the exception that must be visible. |
| `/impeccable-craft FEAT-[ID]` | `layer` includes `frontend` (feature has a UI to craft) |
| `/playwright-expert FEAT-[ID]` | Feature has a user-facing E2E path worth an automated flow (multi-step UI journey, not a single API call) |
| `/secure-code-guardian FEAT-[ID]` | `security_review` is `build` or `both` - the feature introduces a **new** security mechanism (see Security Review Trigger Criteria below). Skip when it reuses an already-Final security pattern. |

**Context-briefing (mandatory when routing any generic skill).** fullstack-guardian, secure-code-guardian, test-master, impeccable-craft and playwright-expert are generic marketplace skills - they do not know this repo's conventions. When you route one, the prompt MUST carry more than the FEAT-ID: include the relevant `/domain/entities.md` and `/domain/business_rules.md` slices for this feature, and point at the existing pattern files it must follow (e.g. `src/lib/auth.ts` for an auth guard, the existing service/repository the feature extends). Without this, the specialist invents a generic pattern instead of respecting what is already proven in the repo.

```
When build is complete, run /pm-stripe and mark build done.
```

---

## Step 1D: Mark Build Complete (4_In_Build → 5_In_Review)

Build skills finished. **Before transitioning, run the Build Skills Coverage check** - then move to code review.

**Build Skills Coverage check (visibility, NOT a blocking gate).**

A Solo Builder has the right to knowingly skip a skill - but the skip must be visible, not silent. Before setting `5_In_Review`, reconcile what *should* have run against what *did* run.

1. Compute what the triggers required for this feature (from `layer`, `kano`, `priority`, `security_review`).
2. Use the AskUserQuestion tool (multiSelect: true) - "Which build skills actually ran for FEAT-[ID]?" - list fullstack-guardian + every conditional skill whose trigger was met.
3. Show the reconciliation:

```
Build Skills Coverage - FEAT-[ID]
  Required by trigger      Ran?
  fullstack-guardian       [✓ / ✗]
  test-master              [✓ / ✗]   (P1 → required)
  impeccable-craft         [✓ / ✗]   (layer: frontend)
  secure-code-guardian     [✓ / — ]  (security_review: build)

⚠ Skipped despite trigger: [list, or "none"]
```

4. If anything required was skipped: surface it plainly and ask whether to run it now or proceed knowingly. **Do not block** - record the conscious skip so it is on record, not lost.

Update Feature Card frontmatter `status: 5_In_Review`.

**Always run (every feature):**

| Skill | Purpose |
|---|---|
| `/code-reviewer FEAT-[ID]` | Code correctness review (includes an OWASP Top 10 pass as one dimension) |

**Conditional - run when the trigger is met:**

| Skill | Trigger |
|---|---|
| `/impeccable-audit FEAT-[ID]` | `layer` includes `frontend` (UI quality/accessibility audit) |
| `/security-reviewer FEAT-[ID]` | `security_review` is `review` or `both` - a dedicated, deeper SAST/audit pass with a severity-rated report. Narrower and deeper than code-reviewer's broad OWASP dimension; run it when the feature touches a security area (see Security Review Trigger Criteria below). |

**Context-briefing** applies here too: code-reviewer and security-reviewer are generic - pass them the domain register slices and the repo's existing security patterns, not just the FEAT-ID, so they review against this repo's proven conventions rather than a generic checklist.

```
When code review passes, run /pm-stripe and mark review complete.
```

---

## Reference: Security Review Trigger Criteria

Determines the Feature Card `security_review` value, which in turn routes `secure-code-guardian` (build) and `security-reviewer` (review). The value is set by `pm-feature-design` during Discovery Interrogation (it has the most context there) and read here for routing. This is the authoritative definition of "applicable" - it replaces the old undefined "if applicable".

**Think in security areas, not feature types.** The trigger is not "is this feature X" - it is "does this feature **create, cross, or modify** one of the vulnerability areas below". A feature is an *instance* of an area (an invite code lives in Abuse/enumeration + Identity; it is not its own trigger). The area routes the specialist; the feature is just an example. This keeps the criterion **domain-neutral** (works for fintech, healthcare, marketplace - no vertical baked in) and **complete** (a new feature type falls into an existing area instead of opening a gap). Do NOT extend this into a list of feature types.

**Set `security_review` above `none` when the feature touches at least one area:**

| # | Security area | Boundary / asset | Examples (illustrative, not definitional) |
|---|---|---|---|
| 1 | Access control & tenant isolation | authz boundary | RLS policy, org/tenant scoping, RLS bypass (service-role), privilege escalation, impersonation, bulk/admin ops |
| 2 | Authentication & identity | authn boundary | login, session, token lifecycle, SSO/OAuth, MFA, new role/permission flag |
| 3 | Cryptography & secrets | asset: keys | key/API-key storage, token generation, hashing, encryption |
| 4 | Sensitive / regulated data | asset: data | PII/regulated data crossing a boundary (→ external service, export). The specific regime (GDPR/HIPAA/PCI/CCPA) is a per-vertical example, not the trigger |
| 5 | Input & injection surface | input boundary | untrusted input parsing, injection, deserialization, file upload |
| 6 | External / server-side integration | external boundary | outbound calls (→ LLM / 3rd-party API), inbound webhooks, SSRF |
| 7 | Abuse & enumeration surface | availability / abuse | guessable identifiers (invite/referral/coupon codes, reset tokens), brute force, rate-limiting, resource exhaustion |
| 8 | Financial integrity | asset: money | money movement, accounting, transactional integrity |

**Reachability escalates.** A feature reachable **pre-auth or cross-tenant** (public endpoint, unauthenticated webhook, not-yet-scoped actor) raises the severity of whatever area it touches - treat borderline cases as triggering when the surface is pre-auth.

**Milestone sweep (not per-feature):** before a production cutover / go-live, run one broad `security-reviewer` pass across the whole Stripe/domain at once, independent of any single feature's flag.

**Value encoding:**

| `security_review` | Meaning | Routes |
|---|---|---|
| `none` | Feature touches no area (plain CRUD behind an already-proven auth pattern) | fullstack-guardian's built-in security checkpoint + code-reviewer's OWASP pass are sufficient |
| `build` | **Creates a new mechanism** in an area (new security BR Draft→Final) | `secure-code-guardian` in build (threat-model before writing the primitive) |
| `review` | **Crosses/touches** an area but reuses a proven pattern | `security-reviewer` in review only |
| `both` | New mechanism AND touches a sensitive area | Both skills |

**secure-code-guardian reuse rule (avoid needless complexity).** `secure-code-guardian`'s value is high only at the **first introduction** of a mechanism in an area. It drops to near-zero when a feature reuses an already-proven pattern (e.g. the second feature using the same `requireRole`-style guard). Discriminate by the Feature Card's rules: if Section 1 introduces a **new** security BR (going Draft→Final for the first time), that is `build`. If it only references an **existing Final** security BR, the primitive is already proven - drop `build`, keep `review` if a sensitive area is still touched.

When a feature touches none of the 8 areas (ordinary CRUD behind existing, proven auth), `security_review` stays `none`. Adding a security specialist to every feature is complexity without marginal value.

---

## Step 1E: Ship Feature (5_In_Review → 6_Shipped)

Code review passed. Fill Section 4 and ship.

```
Marking FEAT-[ID] as shipped.

Please provide (or confirm already recorded):
  1. Commit hash(es) for this feature
  2. Test file paths (unit / integration / E2E)
  3. Feature flag OFF verification (if applicable)
  4. Code Inspection result and reviewer name/date
```

Fill Feature Card Section 4 (Realizacny Protokol) with the above.

Update Feature Card frontmatter `status: 6_Shipped`.
Update `features/feature_list.md` - Status column for this feature.

```
✅ FEAT-[ID]: [title] → SHIPPED

Feature Card is now immutable history.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next in [stripe-name]:
  FEAT-[NEXT-ID]: [title]
  Dependencies: [all met ✓ / waiting for FEAT-XXX]

→ Ready to start. Run /pm-stripe to advance.
```

---

## Step 1F: Impact Analysis

Triggered when a business rule changes in `business_rules.md` - **and equally when an entity state machine changes in `entities.md`** (new state, removed transition, changed guard). A state-machine change is just as capable of breaking shipped features as a rule change, and is easy to under-trigger because it doesn't carry a BR-ID to search for - scan Section 1 entity links, not just BR-ID references, when the change originated in `entities.md`.

**User provides:** Which rule or entity transition changed (BR-ID or Entity + transition) and what changed.

**Analysis steps:**

1. Scan all `/features/cards/FEAT-*.md` files for references to the changed BR-ID in Section 1 (Biznis Mantinely)
2. Group affected features by status:

```
Impact Analysis: BR-[DOMAIN]-[NUMBER] changed

Affected features:
  Status 6_Shipped (code must be updated):
    - FEAT-ORD-012: [title] → files: [list from Section 4]
    - FEAT-ORD-015: [title] → files: [list from Section 4]

  Status 2_Spec_Done, 3_Ready_to_Build, 4_In_Build, or 5_In_Review (re-design needed):
    - FEAT-PAY-002: [title] → re-run /pm-feature-design FEAT-PAY-002

  Status 1_Backlog (no action - JIT design will use updated rule when reached):
    - FEAT-ORD-020: [title]

Not affected: [N] features (no BR-[ID] reference in Section 1)
```

3. For Shipped features: list exact files from Section 4 that need code update
4. For in-progress features: reset to `1_Backlog`, re-run pm-feature-design
5. Update `business_rules.md`: add entry to Changelog section

---

## Step 1G: Close Stripe

All features in the stripe are at `6_Shipped`.

```
Closing [stripe-name]:

  Features shipped: [N]
  Last feature: FEAT-[ID] - [title]

Verification:
  [ ] All Feature Cards in stripe at 6_Shipped
  [ ] feature_list.md Status column up to date
  [ ] No features blocked waiting for this stripe

Stripe [stripe-name] → CLOSED ✅

Remaining active stripes: [list]
```

Update `state.json`: remove closed stripe from `current_stripes`.

---

## Delivery Plan - computation, rules, materialization

Answers the two questions no existing artifact did: **"what do we build next?"** and **"what can run in parallel right now?"** - across all stripes, at once. The plan is a **derived view** computed on demand from the current state; it is never a hand-maintained document. The source of truth stays `feature_list.md` + Feature Cards.

**This is a Resource-Constrained Project Scheduling Problem (RCPSP).** One global dependency DAG; stripes are renewable resources of capacity 1; shared code is a mutex. Do NOT compute per-stripe order as a separate prior step - a cross-stripe dependency can dictate intra-stripe order. It is one list-scheduling pass; the per-stripe order falls out of it.

### Inputs and outputs

| Read (source) | Written back (derived - never hand-edit) |
|---|---|
| `dependencies` (bare `FEAT-ID` or `{id, reason}`), `stripe`, `phase`, `priority`, `status`, `mutex_tags`, `override` | `plan_order` (global sort index), `wave` (parallelism level) → to `feature_list.md` + Notion |

`plan_order`/`wave` exist ONLY so dumb tools (Notion) can sort stably - they are a lossy flat projection of a parallel structure. The swimlane / `delivery_plan.md` is the real structure. Never hand-edit them; never reorder rows in Notion - both are overwritten on recompute.

### The algorithm (deterministic, one pass)

```
1. PRUNE: drop status = 6_Shipped. For any remaining feature depending on a shipped one, that edge is satisfied.
2. CYCLE CHECK: DFS for a cycle in the dependency DAG. If found → STOP, report the cycle (a broken chain needs a human; you cannot schedule it). Dangling dep (FEAT-ID not in list) → warn, treat as data error.
3. OCCUPANCY: mark each stripe holding a feature in 4_In_Build OR 5_In_Review as Occupied (both consume the lane - rework re-locks). Collect their mutex_tags into Active_Mutex_Set.
4. AVAILABLE POOL: all features with no unshipped dependency (in-degree 0 over the pruned graph).
5. SORT the pool by: (1) override present, (2) priority P1>P2>P3, (3) FEAT-ID (deterministic). KANO and VxC are NOT used - they decided phase upstream, not build order.
6. ASSIGN, iterating the sorted pool:
     - override present → BREAK-GLASS: mark Ready, preempt capacity/contention (never a hard dep). Loud rationale.
     - stripe Occupied → Blocked (Capacity)
     - mutex_tags ∩ Active_Mutex_Set ≠ ∅ → Blocked (Contention)
     - else → Ready. Mark stripe Occupied, add its mutex_tags to Active_Mutex_Set.
7. CLASSIFY the rest: in-degree > 0 → Blocked (Dependency).
8. WAVES: wave number = longest dependency path to the feature (topological level). Same wave = no dependency between them = candidate-parallel (still subject to capacity/contention).
9. plan_order = deterministic flatten (wave, then stripe, then intra-stripe position). Write plan_order + wave back.
```

### Rationale grammar (emit one line per feature - explain STATE, not a static index)

There is no fixed "position #14" in a dynamic DAG - explain the state and the constraint that bounded it. Emit deterministically from the algorithm's evaluation order:

| State | Line |
|---|---|
| Ready | `✓ Ready: deps met · lane free · no contention` |
| Blocked (Dependency) | `⛔ Dependency: waiting for FEAT-[X] to ship (Context: [dep reason])` |
| Blocked (Capacity) | `⛔ Capacity: FEAT-[X] is In_Build/In_Review on this lane` |
| Blocked (Contention) | `⛔ Contention: waiting for FEAT-[X] to release lock on '[tag]' (Context: [mutex reason])` |
| Yielded (tie-break) | `Yielded: FEAT-[X] took this lane (P1 > P2)` |
| Break-glass | `🔴 BREAK-GLASS P0: [override reason] - preempts capacity/priority/contention` |

Mechanical reasons are auto-derived; the `(Context: ...)` parts come from the annotated `{id, reason}` / `{tag, reason}` in the source (human judgment captured where the constraint was set). **No separate justification document** - the rationale is emitted inline at every render.

**Golden rule:** when priority and a dependency clash (a P3 sequenced ahead of a P1 because the P1 needs it), the line must say so loudly: `Forced: P3 built first - P1 FEAT-[X] you want will not work without it`.

### Break-glass (P0 override)

A feature with `override: {reason}` preempts capacity, priority ordering, and contention - with the loud rationale above. It CANNOT bypass a hard dependency (physics: you can't build on code that doesn't exist). A P0 bug fix is almost always on already-shipped code, so it's dependency-free and just jumps the lane. Board integrity holds because it's a visible, logged, source-level annotation; everything else computes normally around it. Contention override = the human is explicitly accepting merge risk.

### FULL vs NOW render

- **NOW** (default): Buildable-now + Blocked-with-rationale (see Step 0). The daily driver.
- **FULL** (plan birth, pre-dev walkthrough, on request): additionally each stripe's full ordered queue, the wave grouping, cross-stripe sync points, and a Mermaid swimlane (`subgraph` per stripe, arrows for dependencies). Mostly-shipped rebuild plans collapse the Shipped block and show the forward frontier.

### Plan birth (first render)

The plan is born the first time `/pm-stripe` runs once `feature_list.md` carries statuses:
- **Greenfield / Feature Implementation:** after `pm-mvp-scope` (all `1_Backlog`) → FULL render is the whole forward plan.
- **Rebuild:** after `pm-reverse-extract` / `pm-reconcile features` (mixed statuses from code) → FULL render is mostly-Shipped history + in-flight lanes + forward frontier. `mutex_tags` are extracted from real code here, so a rebuild's first plan already has an accurate contention dimension.

### Materialization + sync direction

After every compute: write `delivery_plan.md` to the repo root (so AI coding agents can read it - "based on delivery_plan.md, what's next in [stripe]?"), and write `plan_order`/`wave` back to `feature_list.md` + Notion.

| Field | Authority | Direction |
|---|---|---|
| `status` | Notion / team | Notion → md (Notion wins, as today) |
| `priority`, `dependencies`, `mutex_tags`, `override` | source judgment | edit in ONE place per cycle; `/pm-stripe` reconciles (pulls a Notion-side change into md like status), md is the durable record |
| `plan_order`, `wave` | the computation | compute → md + Notion (never hand-edit; Notion sorts by `plan_order`, groups by `stripe`) |

**To change the build order:** never touch `delivery_plan.md` or `plan_order`. Edit the source - `priority`, a soft `dependency {id, reason}`, or `override` - then run `/pm-stripe`. The plan recomputes and every change carries its reason into the rationale.

---

## Atomic commit protocol (parallel stripe safety)

When multiple stripes run in parallel, register updates can cause merge conflicts.

**Rule enforced by pm-feature-design (reinforced here):**
- Register updates (entities.md, business_rules.md, decision_models.md) are committed BEFORE any code
- Each feature gets exactly 2 atomic commits during design phase:
  1. `spec([FEAT-ID]): guard conditions + rule finalization` - registers only
  2. `spec([FEAT-ID]): feature design complete` - Feature Card Sections 1-3 only

**Stripe domain alignment guidance:**
- Stripes should cover coherent domain slices (stripe-checkout: Order + Payment, stripe-auth: User)
- Features from different domains in different stripes will not conflict on registers
- Cross-domain features (rare): coordinate manually - one stripe processes at a time

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Per-feature routing:**
- [ ] READY check: status 1_Backlog + all dependencies 6_Shipped + no active feature in same stripe
- [ ] One feature per stripe in active design/build at any time (no parallel features in same stripe)
- [ ] Spec gate verified before 3_Ready_to_Build → 4_In_Build transition (Sections 1-3 present)
- [ ] Build skills receive Feature Card FEAT-ID + domain register slices + repo pattern files (context-briefing), not just FEAT-ID
- [ ] Conditional build/review skills resolved against triggers (layer, kano, priority, security_review) - not skipped by default
- [ ] Build Skills Coverage check run before 4_In_Build → 5_In_Review (non-blocking; skipped-despite-trigger surfaced)
- [ ] security_review value honored: build → secure-code-guardian, review → security-reviewer, both → both, none → neither
- [ ] Section 4 complete before 6_Shipped is set

**Delivery Plan:**
- [ ] Computed as one RCPSP pass (not per-stripe-first); cycle check before scheduling
- [ ] 4_In_Build AND 5_In_Review both occupy the lane (rework re-locks)
- [ ] Blocked features carry a rationale line (dependency / capacity / contention / yielded / break-glass) with `(Context: ...)` from annotated source
- [ ] `override` preempts capacity/priority/contention but never a hard dependency
- [ ] KANO/VxC NOT used in ordering (they decided phase upstream); tie-break = priority then FEAT-ID
- [ ] `delivery_plan.md` materialized to repo root; `plan_order`/`wave` written back to feature_list + Notion, never hand-edited
- [ ] FULL render at plan birth (first run after mvp-scope / rebuild extract-reconcile); NOW render in steady state

**Status transitions:**
- [ ] Feature Card frontmatter `status:` updated at every transition
- [ ] `feature_list.md` Status column kept in sync at every transition
- [ ] Re-entry: mid-cycle features (2-5) detected and surfaced on dashboard

**Impact Analysis:**
- [ ] All Feature Cards scanned, not just active ones
- [ ] Shipped features: exact files identified from Section 4
- [ ] In-progress features: reset to 1_Backlog, re-routed to pm-feature-design
- [ ] business_rules.md Changelog updated

**Stripe closure:**
- [ ] All features at 6_Shipped before closing
- [ ] state.json current_stripes updated

---

## State updates

Feature status in Feature Card frontmatter:
```
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

State update → `pureinn-workspace/[project-slug]/state.json`:
- `current_stripes`: list of active stripe names (remove on closure)
- Per stripe: `active_feature`, `queue` (ordered FEAT-ID list)

---

## Handoff

**Čo si teraz má:** Aktuálny obraz delivery - kde je každá feature v lifecycle, čo je ďalšia akcia per stripe.

**Ďalší krok:** Skill, na ktorý ťa pm-stripe nasmeroval pre aktívnu feature - typicky `/pm-feature-design [FEAT-ID]` (spec) alebo build skilly podľa stavu. Spúšťaj `/pm-stripe` vždy keď si sadáš k Phase 6-7 práci.

**Môžeš preskočiť ak:** Žiadny aktívny stripe a žiadne featury v queue - najprv `/pm-mvp-scope` (alebo `/pm-reverse-extract` pre existujúci produkt).
