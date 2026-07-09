# Playbook 3: Feature Implementation

Add new functionality to an onboarded product, one feature at a time, with JIT spec and structured delivery.

**Use when:** the product is onboarded (via Greenfield or Rebuild) and active - the goal is adding new functionality.

---

## Returning session (express path)

**Trigger:** Pureinn already ran on this project, `state.json` + domain registers exist.

```bash
/pureinn [project-slug]          # loads state.json, restores context
/pm-feature-design [FEAT-ID]     # JIT spec directly - no setup
→ JIT delivery engine
```

If the FEAT-ID doesn't exist yet: add an entry to `feature_list.md`, create a stub card at `features/cards/FEAT-[ID].md`, then run `/pm-feature-design`.

---

## First-time onboarding (Phase 0)

Run once. Skip if all three context files already exist.

| Skill | Output | From |
|---|---|---|
| `/pureinn` | Product context, workspace setup | Pureinn |
| `/common-ground` | Technical context → `COMMON-GROUND.md` | fullstack-dev-skills |
| `/pm-glossary` | Domain glossary | Pureinn |

> Building onto a product that has never been onboarded? Use the **[Rebuild playbook](rebuild/index.md)** first, then return here for ongoing features.

---

## Per feature: viability assessment

Before writing a single line of spec, answer:

1. Which segment / persona does this feature serve?
2. KANO: Must-be / Performance / Delighter / Indifferent?
3. V×C: Quick Win / Big Bet / Fill-in / Time Waster?
4. Demand signal: analytics, support tickets, feature requests?
5. If signal is weak: run a lightweight experiment (fake door, mockup, landing page)
6. MDP: minimum delightful product version? What is deferred to V1.1?
7. Success metrics: depth of usage / behavior change / business impact (set before build)

Run `/pm-feature-viability [FEAT-ID]` to formalize this. Skip if the feature is already scoped and committed.

---

## Track decision

**Track A** - you know what to build → go directly to spec.

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

---

## Track A - Spec + Build

```bash
/pm-feature-design [FEAT-ID]     # JIT spec
→ Design Inspection (pm-stripe)  # hard gate before build
→ Build (fullstack-guardian, etc.)
→ Code Inspection (pm-stripe)
→ 6_Shipped
```

**New domain?** If the feature introduces a new domain not yet in the registers:
```bash
/pm-entity-registry              # new domain entities
/pm-business-rules-library       # new domain rules in Draft
→ then pm-feature-design
```

---

## Adding to the feature inventory

If you have a new feature idea not yet in `feature_list.md`:

```bash
# Option 1: add to the backlog and JIT-design when it's next
# → edit feature_list.md, create stub card, then pm-feature-design when the Stripe is ready

# Option 2: run pm-features-list in delta mode
/pm-features-list                # adds new features, preserves existing assignments
/pm-prioritize                   # re-runs prioritization with the new features
/pm-mvp-scope                    # updates scope decisions if needed
```

`pm-features-list` and `pm-prioritize` are both re-runnable and non-destructive.

---

## Delivery rules (mandatory for existing products)

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

See [Phase 6+7 - JIT Delivery](phase-6-build/index.md) for the full build cycle reference.
