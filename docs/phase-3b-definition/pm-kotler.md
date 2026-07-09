# pm-kotler

> Define the product at Kotler's Five Levels - from Core Benefit to Potential Product, with KANO forward references

**Phase:** 3b - Definition (Step 1, first after Go/No-Go = GO)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** Kotler five levels, product definition, core benefit, augmented product, product levels

---

## When to use

Phase 3b, first skill after the Phase 3a Go/No-Go verdict is GO. Defines what the product actually is at five levels of abstraction before any commercial or roadmap work begins. The output frames every subsequent Phase 3b artifact (Lean Canvas, business model, PRD).

---

## What it produces

**Kotler's Five Levels of Product** (`artifacts/phase-3b-definition/kotler-product-levels.md`):

| Level | Description |
|---|---|
| 1 - Core Benefit | The fundamental job the product does; why someone hires it |
| 2 - Generic Product | The basic, functional form of the product - minimum viable version |
| 3 - Expected Product | What customers assume they get; table stakes for the category |
| 4 - Augmented Product | Features and services that exceed expectations; differentiation |
| 5 - Potential Product | Future evolution; transformations possible in the long run |

Each level is mapped to a KANO classification (Must-be / Performance / Delighter) as a forward reference for Phase 5 feature prioritization.

---

## How to invoke

```bash
/pm-kotler           # interactive
/pm-kotler --agent   # autonomous synthesis from existing Phase 3a outputs
```

---

## Dependencies

**Recommended before running:**
- `design-thinking` - problem statement and value proposition direction
- `pm-problem-validation` - validated problem and customer
- `pm-personas` - persona context anchors level 1-3 definitions

**Produces for:**
- `pm-lean-canvas` - product definition informs UVP and solution sections
- `pm-prd` - levels 1-3 are Product PRD core inputs
- `pm-product-roadmap` (v1) - augmented product features and potential product indicate roadmap phases

**Related skills:** `design-thinking`, `pm-lean-canvas`, `pm-prd`, `pm-product-roadmap`
