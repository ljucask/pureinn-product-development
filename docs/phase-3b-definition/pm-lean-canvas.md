# pm-lean-canvas

> One-page business model optimized for validation-stage products - maps the hypothesis before scaling

**Phase:** 3b - Definition  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** lean canvas, business model, UVP, channels, cost structure, revenue streams, one-page business model

---

## When to use

Phase 3b, after Go/No-Go = GO. Lean Canvas is optimized for the validation stage: it forces explicit problem/solution pairing, early adopter definition, and unfair advantage thinking before scaling. Each block is a hypothesis, not a fact.

Use Lean Canvas for **Greenfield** and **Feature Implementation** playbooks. For **Rebuild** (existing product with an established model), use `pm-business-model` (full BMC) instead.

---

## What it produces

**Lean Canvas** (`artifacts/phase-3b-definition/lean-canvas.md`):

| Block | Content |
|---|---|
| Problem | Top 3 problems ranked by severity; existing alternatives per problem |
| Customer Segments | Primary target customer; Early Adopters profile |
| Unique Value Proposition | Single most compelling reason to use this product |
| Solution | Top 3 features matching the top 3 problems |
| Channels | Path to customers (acquisition, distribution) |
| Revenue Streams | Pricing model, revenue per customer |
| Cost Structure | Fixed + variable costs; customer acquisition cost |
| Key Metrics | AARRR funnel signals for each phase |
| Unfair Advantage | What cannot be easily copied or bought |

---

## How to invoke

```bash
/pm-lean-canvas           # interactive
/pm-lean-canvas --agent   # autonomous draft, requires review before finalizing
```

---

## Key rules

- Go/No-Go must be GO before running. If PIVOT or STOP, the canvas assumptions need to change - flag and confirm before proceeding.
- No invented market data. Lean Canvas blocks are structured from Phase 2 research and Phase 3a outcomes.
- Early Adopters is a separate column within Customer Segments - not the same as the broader segment.
- Unfair Advantage must be something genuinely hard to copy. "We work hard" is not an unfair advantage.

---

## Dependencies

**Required before running:**
- `pm-hypotheses` (Results mode) - Go/No-Go = GO
- `design-thinking` - Problem, UVP, and Solution blocks draw directly from this output
- `pm-personas` - Customer Segments and Early Adopters block

**Recommended:**
- `pm-market-analysis` - Channels and Revenue Streams informed by market research
- `pm-kotler` - product levels inform the UVP and solution framing

**Produces for:**
- `pm-prd` - Lean Canvas is a required PRD section (business model overview)
- `pm-business-case` - Revenue Streams and Cost Structure feed financial projections
- `pm-kpis` - Key Metrics block seeds the AARRR framework

**Related skills:** `pm-kotler`, `pm-kpis`, `pm-business-case`, `pm-prd`, `pm-business-model`
