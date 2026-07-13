---
name: pm-feature-viability
description: Feature Viability Assessment for Feature Implementation playbook. Run before JIT design to confirm a feature is worth building, how to scope it minimally, and what success looks like before build starts. Explicitly skippable when the decision is already made. Produces KANO classification, MDP definition, and pre-defined success metrics.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: feature viability, feature assessment, worth building, should we build this, feature scoping, MDP, minimum desirable product, feature prioritization, FI viability
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-stripe, pm-feature-design, pm-features-list, pm-mvp-scope
---

# PM - Feature Viability Assessment


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

A lightweight decision check before committing to build a new feature.

Answers three questions before any spec work begins:
1. **Is this worth building now?** (KANO classification - is this Must-be, Performance, Delighter, or Indifferent relative to current product state?)
2. **What is the smallest version that delivers real value?** (MDP - Minimum Desirable Product)
3. **How will we know it worked?** (Success metrics, defined before build)

This skill is **not a gate**. If the decision is already made - feature is in the validated roadmap, committed to a customer, or comes from a hard constraint - skip it explicitly and go directly to pm-feature-design.

---

## When to run

**Run when:**
- New feature initiated internally (idea from team or product, not from validated roadmap)
- Unclear whether to build now vs. defer vs. not build
- Unclear what the smallest valuable scope looks like
- No pre-defined success metric for this feature

**Skip when:**
- Feature comes from a validated PRD / feature list with KANO already assigned
- Customer explicitly committed to this feature (contractual or sales commitment)
- Hard compliance or infrastructure requirement (no choice)
- Team already has clear scope and knows what done looks like

---

## Step 0: Skip check

Use AskUserQuestion tool:

Is this feature already scoped and committed, or do you need help deciding?

  A) Already decided - feature is in the roadmap / customer commitment / hard requirement. Skip assessment, go to pm-feature-design. (Recommended if context is clear)
  B) Need to validate - I want to confirm this is worth building and how to scope it.
  C) Partially clear - I know what to build but not sure about scope or success criteria.

If A: confirm skip and route to pm-feature-design.

If C: run abbreviated assessment (Steps 1 + 2 only, skip KANO).

---

## Step 1: Feature context

Ask as plain text:

What does this feature do? Describe it from the user's perspective in one sentence: "This allows [who] to [do what]."

Who requested this? (customer feedback, internal initiative, competitor pressure, compliance, other)

What problem does it solve that isn't solved today? Be specific.

After answers, show summary and ask: "Is this the right feature to assess? Anything to sharpen before continuing?"

---

## Step 2: KANO classification

Use AskUserQuestion tool for this question:

How would your primary user feel if this feature did NOT exist?

  A) Dissatisfied - they expect it, it's a baseline requirement (Must-be)
  B) Less satisfied - they'd notice and prefer it, but would still use the product (Performance)
  C) Neutral - they wouldn't miss it (Indifferent / candidate for cut)
  D) Not sure - I need help thinking this through

If D: ask "Who is the user for this feature and what are they trying to accomplish?" then analyze and suggest the most likely KANO category with reasoning.

**Loss-aversion check (apply even when the answer is A):** internal requesters systematically over-report Must-be because the request itself feels urgent to them - this is the most common source of MVP bloat. Before accepting "Must-be," ask one pressure-test question: "Has a real user asked for this, or is this the team's judgment of what they'd need?" A Must-be with no user evidence behind it is a hypothesis, not a classification - proceed, but note it as `[UNVALIDATED Must-be]` in the summary so it gets revisited if build capacity tightens.

Use AskUserQuestion tool for this follow-up:

Given this classification, what should we do?

  A) Build it - it's justified (Must-be or Performance with clear demand) (Recommended if Must-be or Performance)
  B) Defer it - it's a Delighter, ship after core is solid
  C) Cut it - it's Indifferent, not worth the effort
  D) Discuss - I'm not sure

If C: confirm decision and log as explicitly cut. No further steps needed.

---

## Step 3: MDP - Minimum Desirable Product

Ask as plain text:

What is the minimum version of this feature that still delivers real value to the user? Describe it in terms of what the user can do with it, not implementation details.

What would you cut from the "full" version to ship faster while keeping it genuinely useful?

After answers, confirm: "Is this MDP scope specific enough to spec and build without ambiguity?"

If vague: ask "Can you describe one complete user action this MDP enables, from trigger to outcome?"

---

## Step 4: Success metrics

Ask as plain text:

How will you know this feature worked after it ships? Name one specific, observable metric. (Not "users will be happy" - something you can measure: adoption rate, task completion rate, support ticket reduction, revenue impact, etc.)

What is your target for that metric? (e.g., "60% of active users use this within 30 days of launch")

What is the earliest you can measure this? (e.g., "2 weeks post-launch")

---

## Step 5: Viability summary

Generate:

```markdown
# Feature Viability Assessment - [FEAT-ID or Feature Name]

**Date:** [date]
**Requested by:** [source]
**Assessed by:** [PM name]

---

## Decision

**KANO:** [Must-be / Performance / Delighter / Indifferent]
**Recommendation:** ✅ Build now / ⏳ Defer / ❌ Cut

**Rationale:** [1-2 sentences: why this classification and recommendation]

---

## MDP Scope

**What the MDP enables:** [One complete user action: trigger → outcome]

**Included in MDP:**
- [capability 1]
- [capability 2]

**Explicitly cut from MDP (deferred):**
- [what's being cut and why]

---

## Success Metrics

| Metric | Target | Measure by |
|---|---|---|
| [metric name] | [target] | [date / timeframe post-launch] |

**Failure condition:** [What would indicate this feature did not work and should be reassessed]

---

## Next step

[If Build now]: → Run `/pm-feature-design [FEAT-ID]` with MDP scope as input
[If Defer]: → Feature stays in backlog with KANO = Delighter, revisit after [condition]
[If Cut]: → Feature removed from consideration, logged as explicitly cut
```

Save to: `pureinn-workspace/[project-slug]/initiatives/[feature-slug or FEAT-ID]-viability.md` (or inline in feature discussion - not a required artifact).

---

## Internal checklist

<!-- Claude reference only -->
- [ ] Skip check offered before any assessment work
- [ ] KANO classification has explicit reasoning, not just a label
- [ ] MDP describes a complete user action, not a list of tasks
- [ ] Success metric is observable and measurable, not qualitative
- [ ] Failure condition defined (what would tell us it didn't work)
- [ ] Clear next step: build / defer / cut

---

## Handoff

**Čo si teraz má:** Viability verdikt pre feature - KANO klasifikáciu, MDP scope a merateľné success metriky stanovené pred buildom.

**Ďalší krok:** Ak verdikt = build → `/pm-feature-design [FEAT-ID]` pre JIT dizajn. Ak defer/cut → späť na `/pm-stripe`.

**Môžeš preskočiť ak:** Feature je už scopnutá, commitnutá alebo vo validovanej roadmape - viability nepridáva hodnotu, choď rovno na `/pm-feature-design`.
