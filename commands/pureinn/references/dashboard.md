# Pureinn - Dashboard reference

> Reference for `commands/pureinn/COMMAND.md`. Dashboard rendering, routing, and the phase exit gates.

## STEP 7 - Dashboard and Routing

Display the project dashboard. Phase status display depends on playbook:

**Greenfield dashboard:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [Product Name]
PLAYBOOK: Greenfield
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 1 - Foundation & Collaboration          [✅ Done / ⏭ Skipped / 🔲 To do]
  Phase 2 - Discovery                           [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 3a - Validation                         [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 3b - Commercial Definition              [✅ Done / ⚠️ Partial / ⏭ Skipped / 🔲 To do]
  Phase 4 - Domain Modeling + Register Setup    [🔲 To do]
  Phase 5 - Feature Planning                    [🔲 To do]
  Phase 6 + 7 - Delivery Cycle (JIT)            [🔲 To do]

STARTING FROM: Phase [N] - [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Feature Implementation dashboard:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [Product Name]
PLAYBOOK: Feature Implementation
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 0 - Context Setup                [✅ Done / 🔲 To do]
             (pureinn + common-ground + impeccable document - runs once)
  Feature Viability Assessment           [runs per feature]
             (KANO + V×C + demand validation + MDP + success metrics)
  Track A / Track B                      [determined per feature]
  JIT Design (/pm-feature-design)        [Feature Card Sections 1-3 + register finalization per feature]
  Delivery Cycle (Phase 6 + 7)           [🔲 To do]
             (same as Greenfield JIT + backward compat + feature flags + regression)

CURRENT FEATURE: [feature name or "none - viability assessment pending"]
ACTIVE STRIPE: [stripe name or "none"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Rebuild dashboard:** entry point is `/pm-reconcile` (plan, then per-layer reconcile: domain → rules → features). Show reconcile progress via `/pm-reconcile-status`. After all areas are done, the project drops into the Phase 6 JIT delivery cycle - show the standard stripe/feature queue.

Then show the skills queue for the current phase - read that phase's skills from the **Phase → Skills Reference** in `references/playbooks.md`.

If guidance mode is ON, precede the queue with the phase purpose:

```
PHASE [N] - [PHASE NAME]
[2-3 sentences: what this phase is trying to achieve, what the output is, why it matters for what comes next]
```

Then always show:

```
SKILLS FOR THIS PHASE (run in order):

  1. /[skill-name]
     → Produces: [artifacts]
     → Input needed: [what to prepare or bring]

  2. /[skill-name]
     → Produces: [artifacts]
     → Input needed: [what to prepare or bring]

  [👤 Human activity: e.g., conduct interviews]
     → Before running /[next-skill]

  3. /[skill-name]
     → Produces: [artifacts]

Each skill checks your current state when you run it.
Run /pureinn again after this phase is complete to advance.
```

---

## Exit Gate Thresholds (default reference)

Concrete, phase-by-phase thresholds - self-contained in this repo so the exit gate never has to point at a document that does not exist. These are **defensible defaults for a general commercial SaaS/AI product**, not universal truths - they are drawn from the same benchmark logic already used inside `pm-hypotheses`, `pm-problem-validation`, `pm-kpis`, and `pm-business-case` elsewhere in this framework, gathered here so the gate has one place to read them from. **Adjust per product context** (regulated industries, hardware, enterprise-only B2B, and pre-revenue research products all warrant different numbers) - the gate always offers FORCE with an acknowledged-risk note for exactly this reason.

| Phase | Threshold | Why this number |
|---|---|---|
| **1 - Foundation** | Project Charter has a success criterion tied to retention/revenue/repeated usage (not a vanity metric) + at least one named risk with an owner + decision authority named | Completeness gate, not a numeric one - Phase 1 has no market signal yet to threshold against |
| **2 - Discovery** | ≥10 customer interviews (or synthetic-interview equivalent, clearly marked) completed for Track D + all 4 tracks (A-D) have produced output + Problem Validation verdict is ✅ Validated or ⚠️ Partially validated (not ❌) | 10 interviews is the standard qualitative-saturation floor used by `pm-problem-validation`'s own completeness checklist; a ❌ verdict means the premise itself is unconfirmed - proceeding past it is the single most expensive mistake in the framework |
| **3a - Validation** | Go/No-Go verdict = **GO** from `pm-hypotheses` (Results mode). Commissioned builds (mandate given) skip this phase entirely - recorded in `phases_skipped`, gate not evaluated | Hard gate, already enforced below with no FORCE bypass - listed here for completeness, not re-implemented. The gate protects YOUR market bet; a commissioner's mandate carries their own risk |
| **3b - Commercial Definition** | PRD exists and covers all 12 sections + Business Case has Conservative/Base/Optimistic scenarios with the Conservative scenario surviving to the first milestone (or the risk is explicitly acknowledged) + North Star Metric is defined with a Month-3/6/12 target. **Commissioned-build alternative:** Scope Brief exists, is Baselined, and its mandatory sections are filled (Business Capabilities, Scope IN/OUT with acceptance signals, Acceptance) | A scenario that dies before the milestone under Conservative assumptions is a real risk the team must see, not bury in a spreadsheet. For the Scope Brief: an unbaselined brief means the scope cut was never confirmed - Phase 4 would model an unagreed product |
| **4 - Domain Modeling** | `entities.md`, `business_rules.md`, `decision_models.md` all initialized + every Critical business rule has a stated enforcement point (no blanks) | Guard-condition and enforcement-point completeness is what makes Phase 6 JIT design possible without re-litigating the domain model mid-build |
| **5 - Feature Planning** | `feature_list.md` complete with KANO + V×C on every feature + MVP cut made (every feature has a `phase` value, not just some) + dependency map has zero cycles + `pm-mvp-scope`'s capacity reconciliation shows the MVP list fits the stated team/timeline (or the mismatch is acknowledged) | An MVP list nobody checked against capacity is the most common way delivery timelines silently fail |
| **6-7 - Build (per Stripe close)** | Every feature in the stripe is `6_Shipped` + spec gate was never bypassed (Sections 1-3 complete before any `4_In_Build`) + feature flags default OFF verified | Mirrors the framework's own non-negotiable rules (spec gate, flag-OFF default) rather than inventing a new bar |

Numeric thresholds above (10 interviews, scenario survival, etc.) are **starting points, always shown to the user as adjustable** - never enforced silently. A regulated-industry or hardware product may need a materially different Phase 2 interview count or a longer Phase 3a runway; the gate's job is to make the team consciously choose a number, not to gatekeep on a number that doesn't fit the product.

---

## Exit Gate (when user runs /pureinn after completing a phase)

Check state.json: if `current_phase_index` has increased or user states a phase is done, run exit gate.

Read the thresholds for the completed phase from the table above. If the product's context clearly warrants different numbers (regulated industry, hardware, enterprise-only, pre-revenue research), say so and propose adjusted thresholds before checking against them - do not force a SaaS-shaped bar onto a product that isn't one.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE - Phase [N]: [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Show quantitative thresholds from the table above, adjusted for context if flagged]

For each threshold, did you meet it? (yes / no / unknown)
```

If all critical thresholds met:
```
Exit gate passed. Phase [N] complete.

Type GO to advance to Phase [N+1], or tell me what to revisit first.
```

If thresholds not met, show:
```
Exit gate not passed. Conditions unmet:
  ❌ [Condition 1] - [brief note on what's missing]
  ❌ [Condition 2]
```
Then use the AskUserQuestion tool:
- Question: "How do you want to proceed?"
  - Option A: "Go back and address the gaps (Recommended)" — description: "Run: [recommended skills, from the unmet conditions]"
  - Option B: "Proceed anyway - I acknowledge the risk (FORCE)" — description: "Advances the phase with the gaps still open"

On GO or FORCE: update state.json - add phase to `phases_completed`, advance `current_phase_index`.

**Special rule - Phase 3a → 3b transition:**
This gate cannot be bypassed with FORCE. The Go/No-Go verdict from /pm-hypotheses [Results mode] is the only valid exit from Phase 3a **for a speculative product** (your own market bet). If the verdict is PIVOT or STOP, Phase 3b cannot start. One carve-out exists: a **commissioned build** (a client/exec already decided the build - the market risk is theirs) skips Phase 3a legitimately. If user attempts to proceed to Phase 3b without a GO verdict, block with:
```
Phase 3b requires a GO verdict from Phase 3a hypothesis validation.
Current status: [PIVOT / STOP / not run]

Phase 3b is commercial commitment work - business case, roadmap, and PRD.
Starting it without validated problem-market fit means those documents are built on unconfirmed assumptions.
(Exception: if this build was commissioned - a client or exec already decided it - the gate does not apply to you.)
```
Then use the AskUserQuestion tool:
- Question: "How do you want to resolve this?"
  - Option A: "Return to Phase 3a (Recommended if no experiments have run yet)" — description: "Run /pm-hypotheses [Results mode] with your experiment data"
  - Option B: "Phase 3a was done outside this framework" — description: "Provide the Go/No-Go verdict and evidence via the 'done elsewhere' handler below"
  - Option C: "This is a commissioned build - the mandate is given" — description: "Client/exec decided the build; skip Phase 3a (recorded in phases_skipped with reason 'mandate given') and run /pm-scope-brief as the Phase 3b exit"

**"Done elsewhere" handler (for any phase):**
If user states a phase was done outside this framework, collect the minimum evidence needed to confirm the phase exit criteria were met, then mark it complete. For Phase 3a specifically: collect Go/No-Go verdict + which hypothesis types were tested + key evidence signal per type. Do not require re-running skills if the work was genuinely done.

---

