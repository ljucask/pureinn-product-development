---
name: pm-stripe
description: JIT Delivery Stripe session orchestrator. Run every time you sit down to work on Phase 6-7. Reads current state across all active stripes, detects where each feature is in the lifecycle, surfaces the right next action, and routes you to the correct skill. One stripe = one isolated development channel. Features process one at a time per stripe in dependency order.
license: MIT
metadata:
  agent-mode: never
  author: https://github.com/ljucask
  version: "3.4.1"
  domain: product-management
  triggers: stripe, delivery stripe, JIT cycle, feature design, build feature, impact analysis, security review, delivery plan, build order, sequence, parallel, Phase 6, Phase 7, next feature, kanban, timeline, delivery visualization, rebuild plan, WIP limit, delivery_plan.html, interactive delivery plan, click-for-detail
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

**Two independent axes - never conflate them (critical for Rebuild).** `status` and build order are two separate things:
- **`status` = code reality.** What the code actually is right now (nothing built / partially built / shipped). Owned by whoever observed the code: `pm-stripe` in greenfield (it moves the status forward), `pm-reverse-extract`/`pm-reconcile` in a Rebuild (they set it from the codebase).
- **Plan order (`plan_order`/`wave` + `active_feature`) = the schedule.** What we work on next and who is on which lane. Owned by the Delivery Plan computation + the human picking up work.

**Never reset `status` to serve planning, and never infer active work purely from `status`.** A Rebuild legitimately lands features at `4_In_Build` meaning "code is half-built, nobody is touching it" - that is a true statement about code reality, not a claim that work is in progress. Occupancy comes from `active_feature` (the schedule axis), not from `status` (the reality axis). This is the cheapest correct model - no new lifecycle state is needed; the inherited-partial-build case is just `status: 4_In_Build` (or `1_Backlog` for doc-only) with an empty `active_feature`.

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

After rendering, **materialize** `delivery_plan.md` to the repo root and **write `plan_order`/`wave` back** (see materialization below).

**Check `state.json` for `delivery_html` before moving on - this key is easy to miss on a project whose `state.json` predates this capability.** Three cases:
- **Key absent (never asked - true for every project created before this capability shipped, and for anyone who hit this gap before it was fixed):** ask the visualization question now (see "Delivery Plan companion page" below), even on a steady-state NOW render, even if `delivery_plan.md` already existed before this session. Do not wait for a FULL/plan-birth render to ask - a project can go many NOW renders without ever hitting one.
- **`delivery_html: true`:** regenerate `delivery_plan.html` this run too (same discipline as `delivery_plan.md` - always overwritten, never conditionally skipped).
- **`delivery_html: false`:** skip silently, don't re-ask.

Then use AskUserQuestion tool based on what's detected:

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
2. **Test-infra capability check (not just "did test-master run").** Routing test-master is not the same as the project being *able* to run the test type the feature needs. When `layer` includes `frontend`, the feature needs component tests (jsdom/happy-dom + a testing-library). Detect whether that infra exists: scan `package.json` for `@testing-library/*` and the test config for `jsdom`/`happy-dom`. If a frontend feature has no component-test infra, that is its own coverage row - `component test infra: missing` - NOT silently folded into "test-master ran" (test-master in a Node-only vitest setup writes logic tests and leaves the UI layer untested, or has to add a dependency on its own - a decision that must be explicit).
3. Use the AskUserQuestion tool (multiSelect: true) - "Which build skills actually ran for FEAT-[ID]?" - list fullstack-guardian + every conditional skill whose trigger was met.
4. Show the reconciliation:

```
Build Skills Coverage - FEAT-[ID]
  Required by trigger      Ran?
  fullstack-guardian       [✓ / ✗]
  test-master              [✓ / ✗]   (P1 → required)
  impeccable-craft         [✓ / ✗]   (layer: frontend)
  secure-code-guardian     [✓ / — ]  (security_review: build)
  component test infra     [present / MISSING]   (layer: frontend)

⚠ Skipped despite trigger: [list, or "none"]
```

5. If anything required was skipped OR component-test infra is missing on a frontend feature: surface it plainly and use the AskUserQuestion tool - **run/add it now** / **consciously skip** / **defer to Open Questions**. **Do not block.**
6. **A conscious skip or deferral is auto-logged, never left in the conversation.** When the user chooses "consciously skip" or "defer", append an entry to `/domain/open_questions.md` (Open Questions Register) with an `OQ-[DOMAIN]-NN` id, the feature, what was skipped, and why - so the decision survives past this session instead of being lost when the chat ends. "Record the conscious skip so it is on record" means write it to the register, not just print it. (Missing component-test infra is a classic deferral: card it as an OQ so the gap is tracked, not forgotten.)

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

**Fix policy - inline vs report-only (so it isn't re-decided by vibe every time).** A review skill (code-reviewer, security-reviewer, impeccable-audit) **may fix trivial, unambiguous findings inline** - a clear bug, a wrong constant, a missing touch-target, a lint-level issue - and note in its summary what it fixed. It **must report and wait** on anything larger: a behavioral change, a change touching a business rule / guard condition / security primitive, anything affecting an interface other features depend on, or anything where the "right" fix is a judgment call. When in doubt, report - don't fix. This keeps small findings from bouncing through a full review cycle while ensuring consequential changes stay a human decision, not a reviewer's silent edit.

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
3. OCCUPANCY: a stripe is Occupied when someone is **actively** working it. Read `state.json` per-stripe `active_feature` FIRST - that is the authoritative occupancy signal. Only when `active_feature` is absent (never set) fall back to status = `4_In_Build`/`5_In_Review`. **Why the order matters:** `pm-stripe` moves statuses in greenfield, so status is a fair proxy there - but in a Rebuild, `pm-reverse-extract`/`pm-reconcile` assign `4_In_Build` from *code state* ("partially built"), not from active work. Reading status-first there falsely locks nearly every lane and the scheduler surfaces only some stray low-priority feature. So: `active_feature` set → that stripe Occupied by that feature; `active_feature` empty on a Rebuild first render → treat the lane as free unless the plan-birth question (below) says otherwise. Collect the Occupied features' mutex_tags into Active_Mutex_Set. (Both `4_In_Build` and `5_In_Review` consume the lane when they ARE the active feature - rework re-locks.)
4. AVAILABLE POOL: all features with no unshipped dependency (in-degree 0 over the pruned graph).
5. SORT the pool by: (1) override present, (2) phase (earlier phase first - Phase 0/MVP before Phase 1 before Phase 2), (3) priority P1>P2>P3, (4) FEAT-ID (deterministic). Phase GATES order: a later-phase feature must never take a lane ahead of a current-phase feature in the same wave (visibly wrong on an MVP push). KANO and VxC are NOT used - they decided *phase* upstream (which is now the top content gate), not the intra-phase build order.
6. ASSIGN, iterating the sorted pool:
     - override present → BREAK-GLASS: mark Ready, preempt capacity/contention (never a hard dep). Loud rationale.
     - stripe Occupied → Blocked (Capacity)
     - mutex_tags ∩ Active_Mutex_Set ≠ ∅ → Blocked (Contention)
     - else → Ready. Mark stripe Occupied, add its mutex_tags to Active_Mutex_Set.
7. CLASSIFY the rest: in-degree > 0 → Blocked (Dependency).
8. WAVES: wave number = longest dependency path to the feature (topological level). Same wave = no dependency between them = candidate-parallel (still subject to capacity/contention).
9. plan_order = deterministic flatten (wave, then stripe, then intra-stripe position). Write plan_order + wave back.
10. WIP-LIMIT CHECK: for each stripe, count features that are Occupied/active (by `active_feature` first, else `4_In_Build`/`5_In_Review`). The rule is one per stripe. If a stripe shows >1 active - common on a Rebuild first render where many features carry `4_In_Build` from code state - emit a warning row (don't silently work around it): `⚠ [stripe]: N features active - WIP limit is 1 (resolve via the plan-birth question or set active_feature).`
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

**Rebuild FULL render - onboarding walkthrough mode.** On a Rebuild the most common real use of the FULL plan is walking a new team through a half-built product ("this is what we have, this is the scope, this is the plan"), not "what's next". For that, add a **"what already exists in code"** column per feature, pulled from the Feature Card's Evidence + Known gaps (set by `pm-reverse-extract`/`pm-reconcile`). That turns the schedule into a walkthrough agenda - the team reads row by row and decides per feature: **code review + tests** (exists, looks done) / **finish coding** (partial) / **from scratch** (stub only). Optionally record that decision in a Feature Card `entry_mode` field (`review` / `continue` / `from_scratch`) filled during the walkthrough, so the next render shows how each inherited-partial feature will be approached.

**Contention-confidence marker (FULL render only).** `mutex_tags` are populated per feature at JIT design (`pm-feature-design`), so in a greenfield plan every feature still at `1_Backlog` has none yet - the projected parallelism of far waves is **optimistic** (two features shown side by side may in fact collide on shared code once designed). This never affects the *Buildable now* decision (a feature passes the spec gate, and therefore has `mutex_tags`, before it can enter build) - only the forward projection. Do not guess tags to compensate; a wrong tag creates a false block, which is worse. Instead, mark the boundary honestly: for any wave whose features have no `mutex_tags` yet, append the marker.

```
Wave 1:  TNT-001 · BIL-001 · PAY-001
Wave 4:  FEAT-A · FEAT-B · FEAT-C
         ⚠ projected parallelism - contention unknown until JIT design
```

**The marker is data-driven, never playbook-driven.** Apply the exact same rule to every plan regardless of greenfield vs Rebuild: a wave gets the marker **iff its features actually have empty `mutex_tags`** - never "greenfield always marks / Rebuild always skips". The Rebuild advantage is real only when extraction populated the tags: `pm-reverse-extract` extracts them from real code, but `pm-reconcile` historically did **not**, so a reconcile-based Rebuild can land with empty `mutex_tags` on every card and its far-wave parallelism is exactly as unproven as greenfield's. Do not assume a Rebuild's contention dimension is trustworthy - check the tags. If they're empty, mark the wave honestly; if they're populated (real-code extraction), no marker. (Source-side fix: `pm-reverse-extract` populates `mutex_tags` in both standalone and reconciled mode - see its Step; when reconcile delegates feature carding there, tags should come with it.)

### Plan birth (first render)

The plan is born the first time `/pm-stripe` runs once `feature_list.md` carries statuses:
- **Greenfield / Feature Implementation:** after `pm-mvp-scope` (all `1_Backlog`) → FULL render is the whole forward plan.
- **Rebuild:** after `pm-reverse-extract` / `pm-reconcile features` (mixed statuses from code) → FULL render is Shipped history + inherited-partial lanes + forward frontier. A Rebuild does **not** necessarily land mostly-Shipped: if reconcile tightened the definition of done (added the client layer, back-filled tests) it can land with little Shipped and many features at `4_In_Build` meaning "code half-built, nobody working" (code reality, not active WIP - see the two-axes rule and the plan-birth question). `mutex_tags` are accurate only if extraction populated them (`pm-reverse-extract` does; a reconcile that skipped tagging does not) - the contention marker checks per wave, it doesn't assume.

**Plan-birth WIP question (Rebuild first render ONLY, before computing occupancy).** On the very first render after a Rebuild extract/reconcile, the `4_In_Build`/`5_In_Review` statuses came from code state, not from anyone actively working. Before computing occupancy, resolve real WIP vs artifact once - use the AskUserQuestion tool:

> "Of the features at `4_In_Build`/`5_In_Review`, how many is someone actually working on right now?"
> - A: **None - these came from code state, not active work** (Recommended for a fresh Rebuild) → set every `active_feature` empty; all lanes free.
> - B: **I'll name the specific FEAT-IDs** → set `active_feature` on exactly those stripes; those lanes Occupied, the rest free.
> - C: **All of them - it's real in-progress work** → keep status-as-occupancy for this render.

Write the answer to each stripe's `active_feature` in `state.json` so subsequent renders never re-ask (occupancy then reads `active_feature` directly, per algorithm step 3). This is the one-time bridge from "code reality" statuses to the "schedule" axis.

### Materialization + sync direction

After every compute: write `delivery_plan.md` to the repo root (so AI coding agents can read it - "based on delivery_plan.md, what's next in [stripe]?"), and write `plan_order`/`wave` back to `feature_list.md` + Notion.

| Field | Authority | Direction |
|---|---|---|
| `status` | Notion / team | Notion → md (Notion wins, as today) |
| `priority`, `dependencies`, `mutex_tags`, `override` | source judgment | edit in ONE place per cycle; `/pm-stripe` reconciles (pulls a Notion-side change into md like status), md is the durable record |
| `plan_order`, `wave` | the computation | compute → md + Notion (never hand-edit; Notion sorts by `plan_order`, groups by `stripe`) |

**To change the build order:** never touch `delivery_plan.md` or `plan_order`. Edit the source - `priority`, a soft `dependency {id, reason}`, or `override` - then run `/pm-stripe`. The plan recomputes and every change carries its reason into the rationale.

### Delivery Plan companion page (`delivery_plan.html`)

Beyond the text render and `delivery_plan.md`, pm-stripe can materialize a **self-contained interactive HTML companion** - one file, zero build step, zero external dependency (no CDN, no framework) - that visualizes the same computed schedule as a real, usable page: collapsible per-stripe Kanban lanes, a relative Timeline, a wave-column Dependency graph, and a Kano distribution, with click-for-detail on every card/bar/node. This originated as a hand-built prototype during a live session on a real project and earned a permanent place in the framework because it's genuinely useful - not a demo - regenerates cleanly from data pm-stripe already computes, and stays one flat file.

**Read `references/delivery-plan-companion.html` before generating - it is the fixed template.** Its `<style>` block (Pureinn design tokens) and `<script>` block (collapse/expand + click-for-detail) are copied **byte-for-byte**, never re-authored per run - they are the engine, not something to reinvent. Only the `<main>` body content and the `FEATS` data object are regenerated from current state. The reference's own leading comment block is the full generation contract (per-region source, the timeline day-math, the row-packing algorithm for overlapping bars) - follow it exactly, do not improvise a different layout.

**Offer it once per project, using the AskUserQuestion tool (optional, never forced):**

> "How do you want to see the delivery plan visually?"
> - Option A: "Interactive HTML companion - Kanban + Timeline + Dependency graph + Kano together, one file, refreshed every run (Recommended)"
> - Option B: "Static Mermaid instead - pick individual views"
> - Option C: "No visual output - text + .md only"

Persist the choice to `state.json` (`delivery_html: true/false`); don't re-ask once set.

**If Option B (static Mermaid) is chosen**, the granular per-type choice from the Mermaid views still applies - use the AskUserQuestion tool (`multiSelect: true`) - "Which view(s) do you want?":
- ☑ **Kanban by lane** (pre-checked) - `/pm-diagrams kanban`.
- ☑ **Timeline (relative Gantt)** (pre-checked) - `/pm-diagrams gantt` relative mode.
- ☐ **Dependency graph** - `/pm-diagrams dependency`.
- ☐ **Kano distribution** - `/pm-diagrams kano`.

Plus a plain-language "most suitable right now" pick computed from state: a Rebuild / mixed-state plan → **Kanban** ("you need 'what do we have' before 'what's next'"); a greenfield plan-birth → **Timeline**. This per-view granularity does not apply to Option A - the HTML companion bundles all four sections together (each collapsed by default, so nothing forces you to look at all of them at once).

**Generation summary (full detail lives in the reference file's comment block):**
- **Stats + Kanban buckets:** `4_In_Build`→part_built, `5_In_Review`→needs_review, `6_Shipped`→shipped, everything else→not_started. Lanes = stripes, collapsed by default.
- **Timeline:** excludes shipped features (nothing left to schedule for them); start day = earliest-start over unshipped dependencies (same day-0/estimate model as the relative Gantt); bars in the same lane that would overlap horizontally are packed into stacked rows, never drawn on top of each other.
- **Wave columns:** reuse the Delivery Plan algorithm's own WAVES step - never recompute independently.
- **Critical path = the one computation already used everywhere else** - dependency edges only, never lane-serialized (a capacity/mutex constraint is not a dependency). Timeline and Dependency graph highlight the identical chain.
- **Kano:** render the `kano` field stamped by `pm-features-list`. Never reclassify.
- **One semantic color mapping, fixed by the reference's CSS tokens** - coral = critical path, amber = part-built, blue = needs review, grey = not started, green = shipped. Never invent a per-section palette.
- **`FEATS` object:** title, short description, `layer`, `priority`, `stripe` per feature - powers the click-for-detail popover.
- **Never hand-edit `delivery_plan.html`.** Fully derived, like `plan_order`/`wave` - regenerated and overwritten every run where the companion is enabled. Materialize to the repo root, next to `delivery_plan.md`.
- **Not pushed to Notion** - interactive JS doesn't survive there. It lives in the repo; `delivery_plan.md` can link to it.

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
- [ ] Build Skills Coverage check run before 4_In_Build → 5_In_Review (non-blocking; skipped-despite-trigger surfaced); frontend features checked for component-test infra (`@testing-library/*` + jsdom/happy-dom), `component test infra: MISSING` surfaced as its own row
- [ ] Any conscious skip / deferral auto-logged to `/domain/open_questions.md` as an `OQ-` entry (not left in the conversation)
- [ ] Review skills' fix policy honored: trivial/unambiguous findings may be fixed inline (noted in summary); behavioral / rule-touching / interface-affecting changes reported and left to a human
- [ ] security_review value honored: build → secure-code-guardian, review → security-reviewer, both → both, none → neither
- [ ] Section 4 complete before 6_Shipped is set

**Delivery Plan:**
- [ ] Computed as one RCPSP pass (not per-stripe-first); cycle check before scheduling
- [ ] Occupancy read from `active_feature` first, status (`4_In_Build`/`5_In_Review`) only as fallback (Rebuild code-state statuses must not falsely lock lanes)
- [ ] WIP-limit check emits `⚠ N features active - WIP limit is 1` per stripe with >1 active (never silently worked around)
- [ ] Blocked features carry a rationale line (dependency / capacity / contention / yielded / break-glass) with `(Context: ...)` from annotated source
- [ ] `override` preempts capacity/priority/contention but never a hard dependency
- [ ] Sort order = override → phase → priority → FEAT-ID (phase gates order; a later-phase feature never precedes a current-phase one in the same wave); KANO/VxC NOT used in ordering
- [ ] `delivery_plan.md` materialized to repo root; `plan_order`/`wave` written back to feature_list + Notion, never hand-edited
- [ ] FULL render at plan birth (first run after mvp-scope / rebuild extract-reconcile); NOW render in steady state
- [ ] FULL render marks waves whose features have no `mutex_tags` yet as `⚠ projected parallelism` - data-driven per wave (empty tags), never "greenfield marks / rebuild skips"
- [ ] Plan-birth WIP question asked on Rebuild first render before occupancy; answer written to `active_feature` (real WIP vs code-state artifact resolved once)
- [ ] Rebuild FULL render offers the Evidence/"exists in code" walkthrough column when used for team onboarding
- [ ] `state.json` checked for `delivery_html` **every render, including steady-state NOW** (not just plan birth) - key absent → ask via AskUserQuestion now, regardless of whether `delivery_plan.md` predates this capability; persisted, never re-asked once set
- [ ] If HTML companion enabled: `references/delivery-plan-companion.html`'s `<style>`/`<script>` copied verbatim, only `<main>` + `FEATS` regenerated; critical path/waves reuse the same computation as the text render; never hand-edited
- [ ] If static Mermaid chosen instead: granular multi-select per view (Kanban/Timeline/Dependency/Kano) with the state-based "most suitable now" recommendation (Rebuild→Kanban, greenfield→Timeline)

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
- Per stripe: `active_feature` (the **occupancy authority** - who is actively on the lane; empty = lane free even if a feature sits at `4_In_Build` from code state), `queue` (ordered FEAT-ID list)
- `delivery_html`: `true`/`false` - whether the interactive HTML companion (`delivery_plan.html`) is enabled (persisted so it isn't re-asked)

Feature Card frontmatter (Rebuild walkthrough, optional): `entry_mode` (`review` / `continue` / `from_scratch`) - how an inherited-partial feature will be approached, set during the onboarding walkthrough.

---

## Handoff

**Čo si teraz má:** Aktuálny obraz delivery - kde je každá feature v lifecycle, čo je ďalšia akcia per stripe.

**Ďalší krok:** Skill, na ktorý ťa pm-stripe nasmeroval pre aktívnu feature - typicky `/pm-feature-design [FEAT-ID]` (spec) alebo build skilly podľa stavu. Spúšťaj `/pm-stripe` vždy keď si sadáš k Phase 6-7 práci.

**Môžeš preskočiť ak:** Žiadny aktívny stripe a žiadne featury v queue - najprv `/pm-mvp-scope` (alebo `/pm-reverse-extract` pre existujúci produkt).
