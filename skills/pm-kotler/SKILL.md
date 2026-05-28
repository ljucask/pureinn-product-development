---
name: pm-kotler
description: Define the product at Kotler's Five Levels of Product for Phase 3. Maps each level to KANO classification as a forward reference for Phase 5 feature planning. Runs after Go/No-Go = GO.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: Kotler five levels, product definition, core benefit, augmented product, product levels
  role: specialist
  scope: strategy
  output-format: document
  related-skills: design-thinking, pm-lean-canvas, pm-prd, pm-product-roadmap
---

# PM - Kotler's Five Levels of Product

## What this skill does

Structures the product definition across five levels of value, from core benefit to future potential. Forces explicit separation of what the product IS from what it DOES and what it COULD become.

Output is used in two ways:
1. Product positioning - what we sell and why it matters (feeds PRD)
2. Feature planning preview - each level maps to a KANO category, giving early signal on what goes into MVP vs. post-MVP (feeds Phase 5)

No invented product facts. Claude structures the framework; user provides the product knowledge.

---

## Dependencies

**Recommended before running:**
- `pm-hypotheses` (Results mode) - Go/No-Go verdict must be GO before running this skill
- `design-thinking` - UVP and core job-to-be-done are input to Level 1 and Level 3
- `pm-personas` - customer segments inform Level 3 (expected attributes per segment)
- `pm-market-analysis` - competitor benchmarks inform Level 3 (expected) and Level 4 (augmented)

**Produces artifacts used by:**
- `pm-prd` - Five Levels summary is a PRD section (product definition)
- `pm-mvp-scope` - Level 2 and 3 map to Must-be features, Level 4 maps to Performance/Delighter

---

## Step 0: Current state check

Check for existing artifact:
- `pureinn-workspace/[slug]/artifacts/phase-3/kotler-five-levels.md`

Also check: did Go/No-Go verdict produce a GO? If the hypothesis register shows PIVOT or STOP, flag it before proceeding.

Check for Design Thinking synthesis and Personas - these are the primary inputs. If missing, output quality will be lower.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask all questions at once:

```
I need your product knowledge to build Kotler's Five Levels.

1. CORE BENEFIT (Level 1 - the fundamental job being done)
   What is the single most important outcome the customer gets from this product?
   Not the feature - the outcome. What changes in their work or life?
   Example: "save time", "avoid risk", "feel confident", "close more deals"

2. BASIC PRODUCT (Level 2 - the minimum that delivers the core benefit)
   What is the bare minimum version of this product that could deliver that outcome?
   Which 2-3 features are absolutely non-negotiable for the product to work at all?

3. EXPECTED PRODUCT (Level 3 - what customers assume is included)
   What would a customer be surprised NOT to find in this type of product?
   Think about your segment: what do they consider "standard" based on what they use today?
   List 4-6 attributes customers expect by default.

4. AUGMENTED PRODUCT (Level 4 - what differentiates you)
   What does your product offer that competitors do not, or do worse?
   What would make a customer choose you specifically over alternatives?
   List 2-4 differentiators. Be honest - are these real or aspirational?

5. POTENTIAL PRODUCT (Level 5 - future evolution)
   Where could this product go in 2-3 years?
   What new capabilities, integrations, or use cases could it unlock?
   These are not commitments - they are signals for long-term product vision.
```

---

## Step 2: Build the Five Levels artifact

Generate the structured output. For each level, include:
- Definition (what this level means)
- Product content (what specifically applies to this product)
- KANO mapping (the typical KANO category for features at this level)
- Notes (gaps, risks, open questions)

```markdown
# Kotler's Five Levels of Product

**Product:** [product name]
**Date:** [date]
**Status:** Phase 3 - Define & Validation

---

## Level 1: Core Benefit

> The fundamental job the customer hires this product to do.

**For [product name]:**
[1-2 sentences describing the core outcome]

**KANO signal:** Core benefit is not a feature - it is the reason all Must-be features exist.

---

## Level 2: Basic Product

> The minimum that physically or digitally delivers the core benefit. Without these, the product does not work.

| Component | Description | KANO |
|---|---|---|
| [feature/component] | [what it does] | Must-be |
| [feature/component] | [what it does] | Must-be |

**Gap check:** [are there known gaps between what we can build now and what Level 2 requires?]

---

## Level 3: Expected Product

> Attributes customers assume are included. Absence creates dissatisfaction even if not explicitly requested.

| Attribute | Why expected | Customer segment | KANO |
|---|---|---|---|
| [attribute] | [because competitors have it / industry standard / etc.] | [all / power users / etc.] | Must-be |
| [attribute] | [reason] | [segment] | Must-be |

**Competitive benchmark:** [where does the market set the expected bar for this category?]

---

## Level 4: Augmented Product

> What differentiates the product from alternatives. Creates satisfaction when present but not dissatisfaction when absent.

| Differentiator | Description | How it differs from competitors | KANO |
|---|---|---|---|
| [differentiator] | [description] | [comparison] | Performance / Delighter |

**Honest assessment:** [are these differentiators real and defensible today, or aspirational?]

---

## Level 5: Potential Product

> All future augmentations and transformations the product might undergo. Not commitments - vision signals.

| Future capability | Rationale | Timeline signal |
|---|---|---|
| [capability] | [why this direction makes sense] | Year 1 / Year 2+ / Exploratory |

---

## Summary: KANO Preview

| KANO Category | Levels | Implication for Phase 5 |
|---|---|---|
| Must-be | Level 2 + Level 3 | Goes into MVP |
| Performance | Level 4 (some) | Goes into MVP or first post-MVP |
| Delighter | Level 4 (some) | Post-MVP, validate before building |
| Potential | Level 5 | Roadmap vision, not near-term scope |

---

## Open items

| Item | Type | Priority |
|---|---|---|
| [gap or question] | [gap / assumption / risk] | [high / medium / low] |
```

---

## Step 3: Validate and close

After generating the artifact, surface:

1. **Internal consistency check:** Does Level 4 (differentiators) actually differentiate, or does it overlap with Level 3 (expected)? If expected by the market, it is not a differentiator.
2. **Scope signal:** How many features are implied across Levels 2+3? If the list is long, flag it - Phase 5 will need to be strict about what actually goes into MVP.
3. **Vision coherence:** Is Level 5 a natural extension of Level 4, or a pivot? A pivot at Level 5 suggests unclear product identity.

---

## Notion

Read `pureinn-variables.md` key "Kotler Five Levels" → if URL present, remind user after saving:
`Kotler Five Levels saved locally. Update Notion: [Kotler Five Levels URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3/kotler-five-levels.md
```
