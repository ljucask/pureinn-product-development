# pm-features-list

> Live Register 4 - FDD Feature List - KANO analysis, Value vs. Complexity matrix, stub Feature Cards

**Phase:** 5 - Planning (Step 1-3)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.3.0  
**Triggers:** features list, FDD format, feature list, KANO analysis, value complexity matrix, feature prioritization, Phase 5, feature hierarchy, dependencies

**Structural parity with `pm-reverse-extract`:** Dependencies (from the `Deps` column) are mirrored onto every Feature Card's `dependencies:` frontmatter field and pushed to Notion as their own property, alongside `Dev Stripe` - the same field set and Notion properties as the Rebuild migration path, so a Notion filter/view works identically regardless of which playbook a project came from.

---

## When to use

Phase 5, Step 1. Takes the product scope from PRD Business Capabilities (or `product/scope_brief.md` Business Capabilities on commissioned builds - same contract) and produces the complete prioritized feature inventory. The output of this skill is the direct input for `pm-mvp-scope` (MVP cut + stripe assignment).

Re-runnable: if new features are added (Feature Implementation), runs in append mode without destroying existing entries.

---

## What it produces

Five artifacts:

1. **FDD Feature List** (`features/feature_list.md`) - Live Register 4. All features in FDD format (`[Action] [Result] [Object]`), organized as Domain -> Feature Set -> Feature. Each feature carries: actor, KANO class, V×C quadrant, priority, dependencies, phase, stripe.
2. **Dependency Map** - which features block which, critical path, parallelizable tracks
3. **KANO Analysis** - Must-be / Performance / Delighter / Indifferent classification per feature
4. **Value vs. Complexity (V×C) Matrix** - Quick Win / Big Bet / Fill-in / Time Waster scoring per feature
5. **Stub Feature Cards** (`/features/cards/FEAT-[DOMAIN]-[NUMBER].md`) - one per feature, status `1_Backlog`

After user approval: pushes the complete feature inventory to Notion as the initial backlog.

---

## How to invoke

```bash
/pm-features-list           # interactive
/pm-features-list --agent   # autonomous draft, requires review before finalizing
```

**Two modes, detected automatically at Step 0:**

| Mode | Condition | Behavior |
|---|---|---|
| **Create** | `feature_list.md` does not exist | Full list generated from PRD_master Business Capabilities |
| **Append (FI)** | `feature_list.md` exists | New initiative features added, existing ones preserved |

---

## KANO analysis

Classifies each feature by the **type of value** it delivers:

| Category | Meaning | MVP implication |
|---|---|---|
| **Must-be** | Expected baseline - absence causes dissatisfaction, presence is not noticed | Always in MVP. Non-negotiable. |
| **Performance** | More = better. Customer notices and values improvements linearly. | Core differentiators. Include key ones in MVP. |
| **Delighter** | Unexpected positive surprise. Not expected but appreciated when present. | Post-MVP. |
| **Indifferent** | Customer does not care either way. | Cut. Do not build. |

Classification method: "How would you feel if this feature existed?" + "How would you feel if it didn't?" Combination maps to KANO category. What customers assume is already there = Must-be.

---

## Value vs. Complexity (V×C) matrix

Determines **delivery order** on two axes:

| | Low complexity | High complexity |
|---|---|---|
| **High value** | Quick Win - build first | Big Bet - plan carefully, de-risk |
| **Low value** | Fill-in - low priority | Time Waster - cut or defer |

Value = business impact + customer pain relief (from KANO + Problem Validation).  
Complexity = build effort + technical risk + dependency depth.

**KANO tells you what to include. V×C tells you in what order to deliver it.** Use both together.

---

## FDD feature naming format

All features are named in FDD format: `[Action] [Result] [Object]`

Examples:
- "Create draft order" (not "Order creation")
- "Calculate delivery fee" (not "Fee calculation")
- "Send booking confirmation" (not "Confirmation email")

Feature Sets are grouping labels only - they do not affect MVP cut or sprint planning.

---

## Dependencies

**Required before running:**
- `pm-prd` - PRD Business Capabilities section is the primary input for feature extraction (or `pm-scope-brief` on commissioned builds)
- `pm-entity-registry` - entities inform what operations are needed per domain

**Recommended:**
- `pm-personas` - user roles drive which features belong to which actor
- `pm-problem-validation` - validated pains confirm which features address real needs
- `pm-business-rules-library` - known compliance rules may constrain feature scope

**Produces for:**
- `pm-mvp-scope` - feature list + Dependency Map + KANO + V×C are all required inputs
- `pm-prioritize` - re-runnable prioritization references the feature list
- `pm-product-roadmap` (v3) - features populate the delivery view
- Phase 6 skills - `pm-feature-design` reads Feature Cards JIT before each feature enters build

**Related skills:** `pm-mvp-scope`, `pm-prioritize`, `pm-entity-registry`, `pm-business-rules-library`, `pm-prd`, `pm-product-roadmap`, `pm-open-questions`

---

## Open questions

A genuine scope/prioritization judgment call (not yet ready for `pm-mvp-scope` to rule on) is logged directly in `domain/open_questions.md` (Live Register 5, `pm-open-questions`) - Type: Question, `OQ-{DOMAIN}-NN` or `OQ-MVP-NN` for MVP-cut questions - not embedded as a note in `feature_list.md`.
