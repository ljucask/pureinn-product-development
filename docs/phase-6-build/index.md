# Phase 6+7 - JIT Delivery (Build)

The shared build cycle for all three playbooks. You spec **one feature at a time, just before it enters build** - not the whole Feature Set upfront. Orchestrated by `/pm-stripe`.

**Duration:** Ongoing until launch · **Gate:** Hard gate at Design Inspection · **Playbooks:** all three

---

## How to read this page

This is a **runbook** - do the steps in order, top to bottom, one feature at a time. Each step is written the same way so you always know where you stand:

| Field | Answers |
|---|---|
| **When to run / skip** | The explicit trigger - not "if applicable". If the trigger isn't met, skip and move on. |
| **Gather first** | What must exist before you run it. If something's missing, the step tells you where to get it. |
| **Command** | The exact command. |
| **What you get** | The concrete output, and what you can now *do* or *decide* with it. |
| **What it does NOT give you** | The boundary - so you don't expect the wrong thing. |
| **Done when** | The observable state that means this step is finished. |

When you need the deep detail of a skill (params, internals), open its **reference page** (linked per step). This page is the *route*; the skill pages are the *detail*.

---

## Before you start (phase entry check)

Phase 6 assumes Phase 4-5 already ran. Run `/pm-stripe` - it checks this for you and refuses to route a feature into build if the inputs aren't there. What must exist:

| Input | From | Why it's needed |
|---|---|---|
| `entities.md` (R1), `business_rules.md` (R2), `decision_models.md` (R3) | Phase 4 | JIT design finalizes rules/guards against these |
| `feature_list.md` (R4) + stub Feature Cards | Phase 5 (`pm-features-list`) | the inventory you draw features from |
| MVP scope + Stripe assignments | Phase 5 (`pm-mvp-scope`) | tells you which feature is next in which channel |

If any is missing: you're not in Phase 6 yet - go back to Phase 4-5. `/pm-stripe` will say so explicitly.

---

## The loop (one pass per feature)

```
Viability      Spec            Design         Build          Review          Ship
(optional)  →  (JIT)        →  Inspection  →  (code+tests) →  (code review)→  (immutable)
pm-feature-    pm-feature-      pm-stripe      build skills   review skills   pm-stripe
 viability      design                         + coverage
    │              │                            check
    ▼              ▼
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

**You always start a session with `/pm-stripe`.** It reads where every feature is and routes you to the right step below. You never guess the step - the orchestrator tells you.

> **What to build next / what runs in parallel?** `/pm-stripe` computes the **[Delivery Plan](delivery-plan.md)** - a derived, always-current view of buildable-now vs blocked-with-reason across all stripes, materialized to `delivery_plan.md` for your AI agent to read. See the [Delivery Plan page](delivery-plan.md) for use cases (reorder, break-glass P0, rebuild onboarding, Notion sort stability).

---

## Step 0 - Viability (optional)

- **When to run / skip:** Run when the feature is **not yet scoped or committed** - you're still unsure it's worth building. **Skip** if it's already in a validated roadmap or MVP scope (most Phase 6 features are - this step is the exception).
- **Gather first:** the segment/persona it serves, any demand signal (analytics, tickets, requests).
- **Command:** `/pm-feature-viability [FEAT-ID]`
- **What you get:** KANO class, MDP scope (what's deferred to V1.1), success metrics set *before* build. You can now decide build / defer / drop with a reason on record.
- **What it does NOT give you:** a spec. It's a go/no-go on the feature, not a design.
- **Done when:** you have a build/defer/drop decision. If build → Step 1.

---

## Step 1 - JIT Spec (`1_Backlog → 2_Spec_Done`)

The core spec step. One run per feature, right before build.

- **When to run / skip:** Run when the feature is next in its Stripe, dependencies are `6_Shipped`, and no other feature in that Stripe is mid-cycle. Never skip - this produces the build spec. `/pm-stripe` confirms readiness.
- **Gather first:** the Feature Card stub, the PRD section it references, which BR-IDs apply (or let the skill identify them). Feature Implementation mode: point it at the relevant service files so the sequence diagram uses real code.
- **Command:** `/pm-feature-design [FEAT-ID]`
- **What you get:**
  - `entities.md` guard conditions + `business_rules.md` / `decision_models.md` rules moved Draft → Final (committed *before* any code - Commit 1)
  - Feature Card Sections 1-3: Business Constraints, Acceptance Criteria, sequence diagram + files to modify (Commit 2)
  - the `security_review` flag set (`none`/`build`/`review`/`both`) - decides whether a security specialist runs later
  - status → `2_Spec_Done` (or `2b_In_Design` for a frontend feature still awaiting Figma)
- **What it does NOT give you:** code, tests, or approval to build. It's the spec, not the build, and not the gate.
- **Done when:** Sections 1-3 are populated and both commits are made.

> **New domain?** If the feature introduces a domain not yet in the registers, run `/pm-entity-registry` then `/pm-business-rules-library` (rules in Draft) *before* `pm-feature-design`.

Reference: [pm-feature-design](pm-feature-design.md)

---

## Step 2 - Design Inspection (`2_Spec_Done → 3_Ready_to_Build`) · HARD GATE

- **When to run / skip:** Every feature. This is a **hard gate** - no feature enters build without it. Cannot be bypassed.
- **Gather first:** the completed Feature Card (Sections 1-3).
- **Command:** `/pm-stripe` (presents the inspection checklist)
- **What you get:** a reviewed spec. Delivery Team: someone other than the author signs off. Solo: you confirm Sections 1-3 are correct and complete. Approval flips status → `3_Ready_to_Build`.
- **What it does NOT give you:** it does not check code (there is none yet) - it checks that the *spec* is buildable: ACs testable, sequence diagram uses real methods, guards accurate.
- **Done when:** status is `3_Ready_to_Build`. Only now may build start.

Reference: [pm-stripe](pm-stripe.md)

---

## Step 3 - Build (`3_Ready_to_Build → 4_In_Build`)

`/pm-stripe` sets status to `4_In_Build` and routes you to build skills. These skills are **external and recommended-not-required** (see below) - Pureinn decides *when* each runs; you can swap the executor.

**Always run:**

| Skill | Purpose |
|---|---|
| `/fullstack-guardian` | Full-stack implementation (reads Feature Card Section 3 as the build spec) |

**Conditional - run when the trigger is met:**

| Skill | Trigger |
|---|---|
| `/test-master` | **Required** for `priority: P1` or `kano: Must-be`. P2 → happy path + guard tests. Skipping is the visible exception, not the default. |
| `/impeccable-craft` | `layer` includes `frontend` |
| `/playwright-expert` | feature has a multi-step user-facing E2E path |
| `/secure-code-guardian` | `security_review` is `build`/`both` - a **new** security mechanism (see Security Review Trigger Criteria) |

- **Gather first / context-briefing:** the generic skills don't know your repo. When you route one, hand it the relevant `entities.md` + `business_rules.md` slices **and** the existing pattern files it must follow (e.g. `src/lib/auth.ts`) - not just the FEAT-ID. Otherwise it invents a generic pattern instead of matching what's proven in the repo.
- **What you get:** working code + tests behind a feature flag (OFF by default).
- **What it does NOT give you:** review, or a shipped feature. Code exists but is unreviewed.
- **Done when:** the feature works behind its flag and you're ready to review.

---

## Step 4 - Build complete + Coverage check (`4_In_Build → 5_In_Review`)

Before moving to review, `/pm-stripe` runs the **Build Skills Coverage check** - a visibility step, **not** a blocking gate.

- **What it does:** reconciles what the triggers *required* (from `layer`, `kano`, `priority`, `security_review`) against what actually *ran*. Anything skipped-despite-trigger is surfaced plainly.
- **Why:** this is exactly how `test-master` used to get dropped unnoticed. A Solo Builder may knowingly skip - but the skip goes on record, not silent.
- **What you get:** a clear "required vs ran" list; you either run the missing skill or proceed knowingly.
- **Done when:** you've acknowledged the coverage picture; status → `5_In_Review`.

---

## Step 5 - Code review (part of `5_In_Review`)

**Always run:**

| Skill | Purpose |
|---|---|
| `/code-reviewer` | Correctness review, broad pass (includes an OWASP dimension) |

**Conditional:**

| Skill | Trigger |
|---|---|
| `/impeccable-audit` | `layer` includes `frontend` (UI quality/accessibility) |
| `/security-reviewer` | `security_review` is `review`/`both` - dedicated deeper SAST/audit with a severity-rated report |

- **Context-briefing** applies here too: pass the domain slices + repo security patterns, not just the FEAT-ID.
- **What you get:** review findings, addressed before ship.
- **Done when:** review passes and Section 4 can be filled.

---

## Step 6 - Ship (`5_In_Review → 6_Shipped`)

- **When to run / skip:** every feature, after review passes.
- **Gather first:** commit hash(es), test file paths, feature-flag-OFF verification, code inspection result + date.
- **Command:** `/pm-stripe` (fills Section 4, flips status)
- **What you get:** Feature Card Section 4 complete; status → `6_Shipped`. The card becomes **immutable history**.
- **What it does NOT give you:** it does not deploy or roll out - see Delivery rules below for the rollout discipline on existing products.
- **Done when:** status is `6_Shipped`. `/pm-stripe` surfaces the next feature in the Stripe.

---

## Reference: build & review skills are external and swappable

`fullstack-guardian`, `secure-code-guardian`, `security-reviewer`, `code-reviewer`, `test-master`, `playwright-expert` and `impeccable-*` are **not part of the Pureinn plugin**. They ship from separate marketplaces and must be installed separately:

| Plugin | Provides | Install |
|---|---|---|
| [fullstack-dev-skills](https://github.com/jeffallan/claude-skills) | fullstack-guardian, secure-code-guardian, test-master, playwright-expert, code-reviewer, security-reviewer | `/plugin install fullstack-dev-skills` |
| [impeccable](https://github.com/impeccable-dev/impeccable) | impeccable-craft, impeccable-audit, impeccable-shape | `/plugin install impeccable` |

Pureinn owns the **orchestration** - *when* to build/review, the *trigger*, the *context-briefing*, the *coverage check* - not the tool. If you run your own build/review workflow (or plain Claude Code), the triggers and coverage check still apply; map each slot to whatever executes it. If a routed skill isn't installed, `/pm-stripe` says so and offers the built-in path rather than failing.

---

## Reference: Security Review Trigger Criteria

The `security_review` value (set by `pm-feature-design`, read by `pm-stripe`) decides whether a security specialist runs. **Think in security areas, not feature types** - the trigger is whether the feature *creates, crosses, or modifies* a vulnerability area, not whether it is a specific feature. Domain-neutral (no vertical baked in) and complete (a new feature type falls into an existing area). Set above `none` when the feature touches at least one:

| # | Security area | Examples (illustrative) |
|---|---|---|
| 1 | Access control & tenant isolation | RLS, org/tenant scoping, service-role bypass, privilege escalation, impersonation, bulk/admin ops |
| 2 | Authentication & identity | login, session, token lifecycle, SSO/OAuth, new role/permission flag |
| 3 | Cryptography & secrets | key/API-key storage, token generation, hashing, encryption |
| 4 | Sensitive / regulated data | PII/regulated data crossing a boundary (regime GDPR/HIPAA/PCI is a per-vertical example) |
| 5 | Input & injection surface | untrusted input parsing, injection, deserialization, file upload |
| 6 | External / server-side integration | outbound → LLM/3rd-party API, inbound webhooks, SSRF |
| 7 | Abuse & enumeration surface | guessable identifiers (invite/coupon codes, reset tokens), brute force, rate-limiting |
| 8 | Financial integrity | money movement, accounting, transactional integrity |

Pre-auth / cross-tenant reachability **escalates** whatever area it touches. Before a production cutover, run one broad `security-reviewer` sweep across the domain, not per-feature.

`build` = **creates a new** mechanism in an area → secure-code-guardian. `review` = **crosses** a sensitive area but reuses a proven pattern → security-reviewer. `both` = new + sensitive. `none` = touches no area (plain CRUD behind proven auth). **Reuse rule:** secure-code-guardian adds value only at the *first* introduction of a mechanism in an area - a second feature reusing an existing Final security BR drops `build`. Full table: [pm-stripe](pm-stripe.md).

---

## Reference: Delivery rules for existing products

Mandatory when building onto a product that already has users. Greenfield relaxes these until launch.

| Rule | Detail |
|---|---|
| Feature flags | All new code wrapped (OFF by default), FE + BE |
| API changes | Additive only - no renames, no deletes |
| DB changes | Additive only |
| Regression | Full suite per feature before merge |
| Performance gate | ≤10% latency added to existing API calls |
| Gradual rollout | Internal → 5% → 25% → 50% → 100% |
| Kill switch | Disable flag if error rate >5% |
| Post-launch monitoring | Minimum 4 weeks |

---

## Reference: Feature Card sections

| Section | Written when | By |
|---|---|---|
| Frontmatter + stub | Phase 5 (`pm-features-list`) | Pureinn |
| Section 1 - Business Constraints | Step 1 (`pm-feature-design`) | Pureinn |
| Section 2 - Acceptance Criteria | Step 1 (`pm-feature-design`) | Pureinn |
| Section 3 - Build Spec + Sequence Diagram | Step 1 (`pm-feature-design`) | Pureinn |
| Section 4 - Post-build record | Step 6 (after review) | build team |

Section 3 is what developers read. The card is immutable after `6_Shipped`.

---

## Worked example - one feature, start to finish

`FEAT-TNT-005: Producer Invite Code Management` (Feature Implementation, Solo Builder). This is what the loop actually looks like in a session.

```bash
/pm-stripe
# → Dashboard: FEAT-TNT-005 is next in stripe-tenant, deps met, status 1_Backlog
# → routes to Step 1

/pm-feature-design FEAT-TNT-005
# Discovery Interrogation runs. Feature touches Abuse/enumeration (#7, guessable
# invite code) + Authentication/identity (#2), and the PUBLIC invite endpoint is
# pre-auth reachable → escalates. It CREATES a new invite-code mechanism.
# → security_review: build   (new mechanism in an area → secure-code-guardian later)
# Commit 1: guard conditions + rule finalization (registers)
# Commit 2: Feature Card Sections 1-3
# → status 2_Spec_Done

/pm-stripe                      # Step 2 - Design Inspection (hard gate)
# Solo: confirm Sections 1-3 correct → status 3_Ready_to_Build

/pm-stripe                      # Step 3 - Build
# Always: fullstack-guardian. security_review: build → secure-code-guardian.
# kano: Must-be → test-master REQUIRED.
# Each routed WITH: entities.md + business_rules.md slices + src/lib/auth.ts pattern
/fullstack-guardian FEAT-TNT-005   # + domain slices + auth pattern in the prompt
/secure-code-guardian FEAT-TNT-005 # threat-models the invite-code primitive
/test-master FEAT-TNT-005          # required - Must-be feature
# → status 4_In_Build

/pm-stripe                      # Step 4 - Coverage check
# Required: fullstack-guardian ✓  secure-code-guardian ✓  test-master ✓
# ⚠ Skipped despite trigger: none        → status 5_In_Review

/pm-stripe                      # Step 5 - Review
/code-reviewer FEAT-TNT-005        # always
/security-reviewer FEAT-TNT-005    # security_review: build → review pass too
# findings addressed

/pm-stripe                      # Step 6 - Ship
# Fill Section 4: commits, tests, flag-OFF verified, review date → status 6_Shipped
# → surfaces next feature in stripe-tenant
```

Without the triggers, `test-master` and `secure-code-guardian` were the two easiest to drop silently - the coverage check (Step 4) is what makes a skip visible instead of an accident.
