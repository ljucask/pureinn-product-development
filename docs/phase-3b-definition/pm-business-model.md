# pm-business-model

> Full Business Model Canvas - commercial logic of the product, for established or Rebuild-context products

**Phase:** 3b - Definition  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.1.0  
**Triggers:** business model, revenue model, pricing strategy, monetization

---

## When to use

Phase 3b, after Go/No-Go = GO. Produces the full Business Model Canvas (9-block BMC).

**When to use BMC vs. Lean Canvas:**

| Context | Use |
|---|---|
| Greenfield (new product, early stage) | `pm-lean-canvas` (hypothesis-optimized) |
| Feature Implementation | `pm-lean-canvas` |
| Rebuild (existing product with established model) | `pm-business-model` (full BMC) |
| Any product needing investor-ready full commercial logic | `pm-business-model` |

---

## What it produces

**Business Model Canvas** (`artifacts/phase-3b-definition/business-model-canvas.md`):

| Block | Content |
|---|---|
| Customer Segments | Who the product creates value for |
| Value Propositions | What value is delivered; which problems solved; which needs satisfied |
| Channels | How the company reaches and delivers value to each segment |
| Customer Relationships | What type of relationship with each segment |
| Revenue Streams | How the company earns revenue from each segment |
| Key Resources | What assets the value proposition requires |
| Key Activities | Most important things the company must do |
| Key Partners | Who helps; what is outsourced or acquired from partners |
| Cost Structure | What the business model costs; what are the most important costs |

---

## How to invoke

```bash
/pm-business-model           # interactive
/pm-business-model --agent   # autonomous draft, requires review before finalizing
```

---

## Dependencies

**Required before running:**
- `pm-hypotheses` (Results mode) - Go/No-Go = GO
- `pm-problem-validation` - validated problem and customer
- `pm-personas` - Customer Segments block

**Recommended:**
- `pm-market-analysis` - Channels and Revenue Streams informed by market data
- `pm-kotler` - Value Propositions block built from levels 1-4

**Produces for:**
- `pm-prd` - Business Model Canvas is a required PRD section
- `pm-kpis` - Revenue Streams and Customer Relationships feed KPI framework
- `pm-business-case` - all blocks feed financial projections

**Related skills:** `pm-lean-canvas`, `pm-kpis`, `pm-business-case`
