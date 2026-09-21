# pm-stripe

> JIT Delivery Stripe session orchestrator - run every time you sit down to work on Phase 6-7

**Phase:** 6-7 - JIT Delivery (session start point)  
**Agent mode:** `never` - value is the live interactive session  
**Version:** 3.9.0  
**Triggers:** stripe, delivery stripe, JIT cycle, build feature, impact analysis, security review, test types, test type matrix, dependency scan, SCA, regression gate, delivery plan, build order, sequence, parallel, Phase 6, next feature, kanban, timeline, delivery visualization, rebuild plan, WIP limit, delivery_plan.html, interactive delivery plan, click-for-detail

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

**What it evaluates, in order:** drop `6_Shipped`; check for dependency cycles (stop if found); mark a stripe occupied when someone is **actively** working it - read `active_feature` first, fall back to `4_In_Build`/`5_In_Review` status only when `active_feature` is unset (rework re-locks the lane); then for each dependency-ready feature, sort `override` (break-glass) → **phase** (earlier phase gates order) → priority (P1>P2>P3) → FEAT-ID, and assign against capacity → contention (`mutex_tags` overlap). A per-stripe **WIP-limit warning** fires if more than one feature shows active. **KANO and VxC are not used** - they decided phase upstream, not build order.

**Two independent axes (critical for Rebuild):** `status` = **code reality** (what the code is), plan order + `active_feature` = **the schedule** (what we work on next). Never reset `status` for planning, never infer active work purely from `status`. A Rebuild legitimately lands features at `4_In_Build` meaning "code half-built, nobody touching it" - occupancy comes from `active_feature`, not from that status. This is why no new lifecycle state is needed for inherited-partial builds.

**Two renders, one computation:**
- **NOW** (default, daily): buildable-now + blocked-with-reason.
- **FULL** (plan birth, pre-dev walkthrough): every stripe's ordered queue, parallel waves, cross-stripe sync points, Mermaid swimlane.

**Contention confidence (FULL only):** the `⚠ projected parallelism` marker is **data-driven, not playbook-driven** - a wave gets it iff its features actually have empty `mutex_tags`, applied identically to greenfield and Rebuild. In greenfield, far waves at `1_Backlog` have no tags yet (set at JIT design), so they're marked. A Rebuild is accurate **only if extraction populated the tags** (`pm-reverse-extract` does; a `pm-reconcile` that skipped tagging does not) - so a reconcile-based rebuild can be as contention-blind as greenfield and its waves get the marker too. It never affects the *Buildable now* decision (a feature is JIT-designed before it can enter build). Tags are never guessed to fill the gap - a wrong tag creates a false block.

**Plan birth:** the first `/pm-stripe` after `pm-mvp-scope` (greenfield - all backlog) or after `pm-reverse-extract`/`pm-reconcile` (rebuild - mixed statuses from code). On a **Rebuild first render**, before computing occupancy, pm-stripe asks a one-time **WIP question** - "of the features at `4_In_Build`/`5_In_Review`, how many is someone actually working on right now?" (none = code-state artifact, all lanes free / name specific FEAT-IDs / all real WIP). The answer is written to each stripe's `active_feature` so it's never re-asked - the bridge from code-reality statuses to the schedule axis.

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

**Interactive HTML companion (`delivery_plan.html`):** beyond the text render, pm-stripe can materialize a self-contained interactive page - zero build step, zero external dependency - visualizing the same schedule as collapsible per-stripe Kanban lanes, a relative Timeline, a wave-column Dependency graph, and a Kano distribution, with click-for-detail on every card/bar/node. All three sequencing views share one visual language on top of that: a **build-order badge** (a feature's rank within its own stripe's unshipped pool, same number in every view) and, where relevant, a **cross-stripe wait note** (which other-stripe feature it also blocks on) - annotated in place, not a separate section, with an always-visible Legend panel explaining both. It originated as a hand-built prototype on a real project and earned a permanent place in the framework: it regenerates cleanly from data pm-stripe already computes and stays one flat file. Offered once via AskUserQuestion (Recommended) - checked on **every** render (including a steady-state NOW render), not only at plan birth, so a project whose `state.json` predates this capability still gets asked the first time it's next run, even if `delivery_plan.md` already existed. A lighter static-Mermaid alternative remains available - if chosen, a further multi-select picks which view(s) (`/pm-diagrams kanban`/`gantt`/`dependency`/`kano`, embedded in markdown), with a state-based "most useful right now" pick (Rebuild → Kanban, greenfield → Timeline). The CSS design tokens and JS interaction (collapse/expand, click-for-detail) are copied byte-for-byte from `references/delivery-plan-companion.html` every run - never re-authored; only the body content and feature data regenerate. The critical path is computed once - longest chain by dependency edges only, never lane-serialized - and shared across every view and with the text render, using one fixed color mapping (coral = critical path, amber = part-built, blue = needs review, grey = not started, green = shipped). On a Rebuild the FULL render also offers an "exists in code" walkthrough column (from each card's Evidence) so a new team can go feature by feature: code-review / finish / from-scratch. The choice persists in `state.json` (`delivery_html`); the HTML companion is not pushed to Notion (interactive JS doesn't survive there) - it lives in the repo, linked from `delivery_plan.md`.

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
- ACs are observable (Given/When/Then, no checkbox lists)
- Happy path + flag OFF covered
- Edge Case Coverage table: all 6 categories resolved, no empty or TBD cell

**Section 3 - JIT Technical Design:**
- Sequence diagram present and logical
- All actors/services match real codebase
- Files to modify listed

Approval transitions the feature to `3_Ready_to_Build`. **The Edge Case Coverage table is a blocking gate:** a card with an incomplete table gets neither `3_Ready_to_Build` nor an owner, and a card with no table at all (designed before 5.62.0) is routed to `/pm-feature-design [FEAT-ID] --edge-cases`.

---

## Build & review skills - always vs conditional

pm-stripe routes build skills (Step 1C, `3_Ready_to_Build → 4_In_Build`) and review skills (Step 1D, `4_In_Build → 5_In_Review`). Each set is split into **always** and **conditional-by-trigger** - "applicable" is now explicitly defined, not left to vibe.

> **These build/review skills are external and recommended-not-required.** `fullstack-guardian`, `secure-code-guardian`, `security-reviewer`, `code-reviewer`, `test-master`, `playwright-expert` and `impeccable-craft`/`impeccable-audit` are **not part of the Pureinn plugin** - they ship from separate marketplaces (`fullstack-dev-skills`, `impeccable`) and must be installed separately. Pureinn owns the *orchestration* (when to build/review, the trigger, the context-briefing, the coverage check), not the tool. The executor is swappable - use your own build/review workflow if you prefer; the triggers and coverage check still apply.

| Stage | Always | Conditional (trigger) |
|---|---|---|
| Build (1C) | `fullstack-guardian` | `test-master` (P1/Must-be → required, specialized by `test_types`), a contract-testing tool e.g. Pact (`test_types` includes `contract`), `impeccable-craft` (`layer: frontend`), `playwright-expert` (E2E path), `secure-code-guardian` (`security_review: build`/`both`) |
| Review (1D) | `code-reviewer` | `impeccable-audit` (`layer: frontend`), `security-reviewer` (`security_review: review`/`both`) |

**Build Skills Coverage check** (before `4_In_Build → 5_In_Review`): pm-stripe reconciles what the triggers required against what actually ran, and surfaces anything skipped-despite-trigger. It is a **visibility check, not a blocking gate** - a Solo Builder may knowingly skip, but the skip is on record rather than silent (which is how `test-master` used to get dropped unnoticed). Additions: (1) a **test-infra capability check** - a frontend feature needs component-test infra (`@testing-library/*` + jsdom/happy-dom); if it's missing, that surfaces as its own row (`component test infra: MISSING`), not silently folded into "test-master ran". (2) a **test-type coverage check** - each `test_types` entry beyond `unit` (integration/contract/visual_regression/performance) needs its own artifact (integration test, Pact contract, visual baseline, load-test script) or an explicit deferral; missing ones surface as their own row, same principle as the test-infra check. (3) an **edge case test check** - every AC-ID in the card's Edge Case Coverage table needs at least one test; a missing test is a visible skip like a skipped skill, and at ship the AC-ID → test file mapping is written into Section 4. (4) Any **conscious skip or deferral is auto-logged** to the Open Questions Register (`/domain/open_questions.md`) as an `OQ-` entry - the decision survives past the session instead of being lost in the chat.

**Review fix policy:** a review skill (code-reviewer, security-reviewer, impeccable-audit) **may fix trivial, unambiguous findings inline** (a clear bug, a wrong constant, a missing touch-target) and note it in its summary; it **must report and wait** on anything larger - behavioral changes, anything touching a business rule / guard / security primitive, or anything affecting an interface other features depend on. When in doubt, report. This keeps the boundary a rule, not a per-run judgment.

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

## Test Type Matrix

The `test_types` frontmatter value specializes `test-master` routing and the Build Skills Coverage check. Set by `pm-feature-design` during Discovery Interrogation, same mechanism as `security_review`.

| Characteristic | Test type | Tool |
|---|---|---|
| Business logic / guard conditions (baseline) | `unit` | test-master (native) |
| Calls another internal service, DB, or API endpoint | `integration` | test-master (native) |
| Consumed by an external client (mobile app, partner integration, public API) | `contract` | Pact, or equivalent - not test-master's default remit |
| UI feature reusing a design-system component whose visual stability matters | `visual_regression` | Percy / Chromatic / Playwright screenshot diff |
| Feature on the money path or a high-traffic endpoint | `performance` | test-master (native - k6/Artillery) |

E2E is a separate, already-existing axis (`playwright-expert`'s own trigger) - not part of `test_types`. `unit` is the default on nearly everything; the rest are added only when their characteristic genuinely matches, not for thoroughness.

---

## Close Stripe

All features in the stripe at `6_Shipped`. Before marking CLOSED, pm-stripe confirms two things per-feature checks can't see - **non-blocking, visible, same principle as Build Skills Coverage**:

1. **Regression check** - full test suite (not just this stripe's features in isolation) green in CI since the last feature shipped.
2. **Dependency/SCA scan** - the project's scanner (Snyk, Dependabot, Aikido, or equivalent) clean of open High/Critical findings.

If either is unconfirmed, pm-stripe asks and records the answer rather than silently closing. When findings exist, they're **triaged before logging**, not dumped raw into the register: an auto-fixable dependency finding (the tool opens its own fix PR) stays in that PR flow, never logged; a non-fixable dependency finding or a code-level (SAST) finding becomes a register entry - `BLK-` for Critical/High or any concrete non-fixable gap (tagged with the security area), `OQ-` for Low/informational timing questions (e.g. a framework EOL notice). Same discipline as a build-skill skip.

**Automatic regression check (optional, GitHub Actions via `gh` CLI).** Simpler than the SCA side - no new credentials, `gh`'s existing auth is reused. Opt in once via `state.json` `ci_automation`; when enabled, pm-stripe runs `gh run list` for the relevant branch and reads the latest run's conclusion instead of asking. An in-progress/queued run is reported as unresolved, never guessed at. No workflow file is scaffolded by this framework - if the repo has none yet, it's treated as "not run yet" in the manual path.

**Automatic fetch (optional, Aikido only today).** The SCA check can run itself instead of asking, once per-project opt-in: `state.json` `sca_automation` stores `enabled`, `tool`, `region`, and the **names** of the environment variables holding Aikido OAuth2 client credentials - never the credential values themselves, which live only in the environment, never in a tracked file. When enabled, pm-stripe exchanges the credentials for a short-lived token, fetches open issues for the connected repo via Aikido's public API, and applies the same triage table automatically - no per-item confirmation. Asked once (retrofit on existing projects, same discipline as `delivery_html`); other tools can be added the same way once their API is verified with equal rigor. Full procedure (endpoints, exact request shape): `pm-stripe` → Reference: Automatic SCA Fetch (Aikido).

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
