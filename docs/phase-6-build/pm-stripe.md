# pm-stripe

> JIT Delivery Stripe session orchestrator - run every time you sit down to work on Phase 6-7

**Phase:** 6-7 - JIT Delivery (session start point)  
**Agent mode:** `never` - value is the live interactive session  
**Version:** 3.2.0  
**Triggers:** stripe, delivery stripe, JIT cycle, build feature, impact analysis, security review, delivery plan, build order, sequence, parallel, Phase 6, next feature

---

## When to use

**Run this every time you sit down to work on Phase 6-7.** It is not a one-time setup skill - it is your session start point. It reads current state, tells you exactly what to do next, and routes you to the right skill.

---

## What it does

Reads `features/feature_list.md` and all `features/cards/FEAT-*.md` files, then:

1. **Syncs status from Notion** (if Feature Backlog URL is configured) - Notion wins on status, markdown wins on content
2. **Detects mid-cycle features** (anything not at `1_Backlog` or `6_Shipped`) and surfaces them with a clear action prompt
3. **Computes and shows the Delivery Plan** - what is buildable now, what is blocked and why, across all stripes (see below)
4. **Routes you** to the right next action via AskUserQuestion

**Division of responsibility:**
- `feature_list.md` - source of truth for inventory, priority, stripe assignment, dependency order
- `features/cards/FEAT-*.md` - source of truth for feature status and spec content
- `pm-stripe` - session orchestrator: detects state, routes, tracks transitions, runs Impact Analysis, **computes the Delivery Plan**

---

## The Delivery Plan

Answers the two questions no earlier artifact did: **"what do we build next?"** and **"what can run in parallel right now?"** - across all stripes, in one place. It is a **derived view** computed on demand from the current state, never a hand-maintained document. Source of truth stays `feature_list.md` + Feature Cards.

Formally a **Resource-Constrained Project Scheduling Problem**: one global dependency DAG, stripes are resources of capacity 1, shared code is a mutex. One list-scheduling pass; per-stripe order falls out of it (you cannot compute it per-stripe first - a cross-stripe dependency can dictate intra-stripe order).

**What it evaluates, in order:** drop `6_Shipped`; check for dependency cycles (stop if found); mark stripes with a `4_In_Build` **or** `5_In_Review` feature as occupied (rework re-locks the lane); then for each dependency-ready feature: `override` (break-glass) → capacity → contention (`mutex_tags` overlap) → priority tie-break (P1>P2>P3, then FEAT-ID). **KANO and VxC are not used** - they decided phase upstream, not build order.

**Two renders, one computation:**
- **NOW** (default, daily): buildable-now + blocked-with-reason.
- **FULL** (plan birth, pre-dev walkthrough): every stripe's ordered queue, parallel waves, cross-stripe sync points, Mermaid swimlane.

**Plan birth:** the first `/pm-stripe` after `pm-mvp-scope` (greenfield - all backlog) or after `pm-reverse-extract`/`pm-reconcile` (rebuild - mixed statuses + `mutex_tags` from real code).

**Explainability:** every feature carries a rationale line - `Ready`, `Blocked by Dependency/Capacity/Contention`, `Yielded`, or `🔴 BREAK-GLASS`. Mechanical reasons are auto-derived; the `(Context: ...)` comes from annotated `{id, reason}` / `{tag, reason}` in the source. No separate justification document.

**Materialization + control:**
- `delivery_plan.md` is written to the repo root so AI coding agents can read it ("based on delivery_plan.md, what's next in [stripe]?").
- `plan_order` + `wave` are written back to `feature_list.md` + Notion so dumb tools sort stably. **Never hand-edit them, never reorder rows in Notion** - overwritten on recompute.
- **To change the order:** edit the source (`priority`, a soft `dependency`, or `override`), then run `/pm-stripe`. The plan recomputes; every change carries its reason into the rationale.

| Field | Authority | Direction |
|---|---|---|
| `status` | Notion / team | Notion → md |
| `priority`, `dependencies`, `mutex_tags`, `override` | source judgment | edit in one place, `/pm-stripe` reconciles |
| `plan_order`, `wave` | the computation | compute → md + Notion (never hand-edit) |

---

## How to invoke

```bash
/pm-stripe    # always the same - reads current state and routes
```

---

## Session flow

```
Session start → pm-stripe
  │
  ├─ 1_Backlog, deps met → /pm-feature-design [FEAT-ID]       → 2_Spec_Done
  ├─ 2_Spec_Done         → Design Inspection (human review)    → 3_Ready_to_Build
  ├─ 2b_In_Design        → Figma design complete?              → 3_Ready_to_Build
  ├─ 3_Ready_to_Build    → build skills                        → 4_In_Build
  ├─ 4_In_Build          → build complete                      → 5_In_Review
  ├─ 5_In_Review         → code review + Section 4             → 6_Shipped
  └─ all 6_Shipped       → Close Stripe
```

---

## Design Inspection (2_Spec_Done → 3_Ready_to_Build)

pm-stripe presents a checklist for human review of Sections 1-3:

**Section 1 - Business Constraints:**
- BR-IDs referenced and correct
- Entity guard conditions specified
- Edge cases covered

**Section 2 - Acceptance Criteria:**
- ACs are observable (Given/When/Then)
- Happy path covered
- Guard failures covered

**Section 3 - JIT Technical Design:**
- Sequence diagram present and logical
- All actors/services match real codebase
- Files to modify listed

Approval transitions the feature to `3_Ready_to_Build`.

---

## Build & review skills - always vs conditional

pm-stripe routes build skills (Step 1C, `3_Ready_to_Build → 4_In_Build`) and review skills (Step 1D, `4_In_Build → 5_In_Review`). Each set is split into **always** and **conditional-by-trigger** - "applicable" is now explicitly defined, not left to vibe.

> **These build/review skills are external and recommended-not-required.** `fullstack-guardian`, `secure-code-guardian`, `security-reviewer`, `code-reviewer`, `test-master`, `playwright-expert` and `impeccable-craft`/`impeccable-audit` are **not part of the Pureinn plugin** - they ship from separate marketplaces (`fullstack-dev-skills`, `impeccable`) and must be installed separately. Pureinn owns the *orchestration* (when to build/review, the trigger, the context-briefing, the coverage check), not the tool. The executor is swappable - use your own build/review workflow if you prefer; the triggers and coverage check still apply.

| Stage | Always | Conditional (trigger) |
|---|---|---|
| Build (1C) | `fullstack-guardian` | `test-master` (P1/Must-be → required), `impeccable-craft` (`layer: frontend`), `playwright-expert` (E2E path), `secure-code-guardian` (`security_review: build`/`both`) |
| Review (1D) | `code-reviewer` | `impeccable-audit` (`layer: frontend`), `security-reviewer` (`security_review: review`/`both`) |

**Build Skills Coverage check** (before `4_In_Build → 5_In_Review`): pm-stripe reconciles what the triggers required against what actually ran, and surfaces anything skipped-despite-trigger. It is a **visibility check, not a blocking gate** - a Solo Builder may knowingly skip, but the skip is on record rather than silent (which is how `test-master` used to get dropped unnoticed).

**Context-briefing:** the build/review specialists are generic marketplace skills. pm-stripe passes them the relevant `domain/entities.md` + `domain/business_rules.md` slices and the repo's existing pattern files (e.g. `src/lib/auth.ts`), not just the FEAT-ID - so they respect proven repo conventions instead of inventing generic ones.

---

## Security Review Trigger Criteria

The `security_review` frontmatter value (`none` / `build` / `review` / `both`) decides whether a security specialist runs. It is set by `pm-feature-design` during Discovery Interrogation and read here for routing.

**Think in security areas, not feature types.** The trigger is not "is this feature X" - it is "does this feature **create, cross, or modify** one of these vulnerability areas". A feature is an *instance* of an area (an invite code lives in Abuse/enumeration + Identity, it is not its own trigger). This keeps the criterion **domain-neutral** (fintech, healthcare, marketplace - no vertical baked in) and **complete** (a new feature type falls into an existing area instead of opening a gap). Set above `none` when the feature touches at least one:

| # | Security area | Examples (illustrative) |
|---|---|---|
| 1 | Access control & tenant isolation | RLS, org/tenant scoping, service-role bypass, privilege escalation, impersonation, bulk/admin ops |
| 2 | Authentication & identity | login, session, token lifecycle, SSO/OAuth, MFA, new role/permission flag |
| 3 | Cryptography & secrets | key/API-key storage, token generation, hashing, encryption |
| 4 | Sensitive / regulated data | PII/regulated data crossing a boundary; the regime (GDPR/HIPAA/PCI/CCPA) is a per-vertical example, not the trigger |
| 5 | Input & injection surface | untrusted input parsing, injection, deserialization, file upload |
| 6 | External / server-side integration | outbound → LLM/3rd-party API, inbound webhooks, SSRF |
| 7 | Abuse & enumeration surface | guessable identifiers (invite/referral/coupon codes, reset tokens), brute force, rate-limiting, resource exhaustion |
| 8 | Financial integrity | money movement, accounting, transactional integrity |

Pre-auth / cross-tenant reachability **escalates** whatever area it touches. Before a **production cutover**, run one broad `security-reviewer` sweep across the whole domain, independent of any single feature.

`build` = **creates a new** mechanism in an area (new security BR Draft→Final) → `secure-code-guardian`. `review` = **crosses** a sensitive area but reuses a proven pattern → `security-reviewer`. `both` = new AND sensitive. `none` = touches no area (plain CRUD behind proven auth; fullstack-guardian's checkpoint + code-reviewer's OWASP pass suffice).

**Reuse rule:** `secure-code-guardian` adds value only at the first introduction of a mechanism in an area. A second feature reusing an existing Final security BR drops `build` (keeps `review` if a sensitive area is still touched) - adding a specialist to every feature is complexity without marginal value.

---

## Impact Analysis

Triggered when a business rule in `business_rules.md` changes. Provide the changed BR-ID and what changed - pm-stripe scans all Feature Cards and groups affected features by status:

| Feature status | Action |
|---|---|
| `6_Shipped` | Code must be updated - pm-stripe lists exact files from Section 4 |
| `2_Spec_Done` / `3_Ready_to_Build` / `4_In_Build` / `5_In_Review` | Reset to `1_Backlog`, re-run `pm-feature-design` |
| `1_Backlog` | No action - JIT design will use the updated rule when reached |

---

## Atomic commit protocol

When multiple Stripes run in parallel, register updates (entities.md, business_rules.md, decision_models.md) must be committed before any code to prevent merge conflicts. pm-stripe reinforces the rule established by `pm-feature-design`.

**Stripe domain alignment:** stripes should cover coherent domain slices (e.g. stripe-checkout: Order + Payment, stripe-auth: User). Features from different domains in different stripes won't conflict on registers. Cross-domain features: coordinate manually, one stripe processes at a time.

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - features must be assigned to stripes
- All Feature Cards exist as stubs (status: `1_Backlog`)

**Related skills:** `pm-feature-viability`, `pm-feature-design`, `pm-feature-card`, `pm-mvp-scope`, `pm-entity-registry`
