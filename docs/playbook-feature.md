# Playbook 3: Feature Implementation

Add new functionality to an onboarded product, one feature at a time, with JIT spec and structured delivery.

**Use when:** the product is onboarded (via Greenfield or Rebuild) and active - the goal is adding new functionality.

---

## How to read this page

This is a **route map** for a single feature's path through the framework, from idea to shipped. The JIT build/review loop itself (spec → design inspection → build → review → ship) has its own detailed runbook - this page covers everything *before* that loop starts: viability, track decision, and entering it correctly.

---

## Returning session (express path)

- **When to use:** `/pureinn` already ran on this project - `state.json` + domain registers exist. This is your default entry point for almost every session.
- **Gather first:** nothing extra - the workspace already has what it needs.
- **Command:**
```bash
/pureinn [project-slug]          # loads state.json, restores context
/pm-feature-design [FEAT-ID]     # JIT spec directly - no setup
→ JIT delivery engine
```
- **What you get:** full project context restored, straight into spec for the next feature.
- **Done when:** you're in the JIT loop (see [Phase 6+7](phase-6-build/index.md)).

**If the FEAT-ID doesn't exist yet:** add an entry to `feature_list.md`, create a stub card at `features/cards/FEAT-[ID].md`, then run `/pm-feature-design`.

---

## First-time onboarding (Phase 0)

- **When to run / skip:** run once, at project start. **Skip entirely** if all three context files already exist (`state.json`, `COMMON-GROUND.md`, glossary).
- **Gather first:** nothing - `/pureinn` scaffolds the workspace.
- **What you get:** product context, technical context, domain glossary - the baseline every later skill reads from.
- **What it does NOT give you:** onboarding of an *existing but never-onboarded* product. If the product has never been through Pureinn at all, that's the [Rebuild playbook](playbook-rebuild.md), not this step.

| Skill | Output | From |
|---|---|---|
| `/pureinn` | Product context, workspace setup | Pureinn |
| `/common-ground` | Technical context → `COMMON-GROUND.md` | fullstack-dev-skills |
| `/pm-glossary` | Domain glossary | Pureinn |

---

## Per feature: viability assessment (Step 0)

- **When to run / skip:** run before writing a single line of spec, when the feature is **not yet scoped or committed**. **Skip** if the feature is already scoped and committed (in a validated roadmap/MVP scope) - most features reaching this playbook already are.
- **Gather first:** which segment/persona the feature serves, any demand signal (analytics, tickets, feature requests).
- **Command:** `/pm-feature-viability [FEAT-ID]`
- **What you get:** KANO class, V×C class, an MDP (minimum delightful product) scope with what's deferred to V1.1, and success metrics set *before* build - so "did it work" has a pre-committed answer.
- **What it does NOT give you:** a spec or a design. It's a build/defer/drop decision, not a how-to-build.
- **Done when:** you have a build / defer / drop decision on record.

Underlying questions this answers: which segment, KANO class, V×C class, demand signal, whether a lightweight experiment (fake door, mockup, landing page) is warranted first.

---

## Track decision (Step 0.5)

- **When to run / skip:** run when you're not certain of the solution shape yet. **Skip straight to Track A** if you already know exactly what to build.

**Track A** - you know what to build → go directly to spec (below).

**Track B** - you know the area, not the solution → discovery first:

| Step | Activity / Skill | Output |
|---|---|---|
| 1 | 5-10 user interviews (target segment) | Qualitative insight |
| 2 | Competitive analysis (if direction unclear) | Differentiation signal |
| 3 | Tech feasibility with existing stack | Candidate solution |
| 4 | `/pm-hypotheses` (Plan mode) | Feature hypothesis, experiment plan, criteria |
| 5 | Run experiments | Go/No-Go signal |
| 6 | `/pm-hypotheses` (Results mode) | Verdict: build / don't build / pivot |
| → | Apply KANO + V×C → enter Track A | |

- **Done when:** you have a build verdict and enter Track A.

---

## Track A - enter the JIT loop

Once the feature is scoped (viability done, solution known), it enters the same loop as every other playbook:

```bash
/pm-feature-design [FEAT-ID]     # JIT spec
→ Design Inspection (pm-stripe)  # hard gate before build
→ Build (fullstack-guardian, etc.)
→ Code Inspection (pm-stripe)
→ 6_Shipped
```

Full step-by-step detail (what each step needs, gives you, and doesn't): **[Phase 6+7 - JIT Delivery](phase-6-build/index.md)**.

**New domain?** If the feature introduces a domain not yet in the registers, run these *before* `pm-feature-design`:
```bash
/pm-entity-registry              # new domain entities
/pm-business-rules-library       # new domain rules in Draft
→ then pm-feature-design
```

---

## Adding to the feature inventory

- **When to run / skip:** run when you have a new feature idea not yet in `feature_list.md`.

**Option 1 - just-in-time:** edit `feature_list.md`, create a stub card, run `pm-feature-design` when the Stripe reaches it. Lowest overhead - use this for one-off additions.

**Option 2 - re-run the planning skills** (delta mode, non-destructive):
```bash
/pm-features-list                # adds new features, preserves existing assignments
/pm-prioritize                   # re-runs prioritization with the new features
/pm-mvp-scope                    # updates scope decisions if needed
```
Use this when several new features arrived at once and the priority order needs re-thinking, not just appending.

---

## Delivery rules (mandatory for existing products)

Because this playbook builds onto a product with real users, these are non-negotiable - Greenfield relaxes them until launch:

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
