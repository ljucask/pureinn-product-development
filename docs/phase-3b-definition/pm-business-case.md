# pm-business-case

> Financial projections and investment rationale - synthesizes market size, business model, and KPIs

**Phase:** 3b - Definition  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** business case, financial projections, unit economics, ROI, go no go, investment rationale

---

## When to use

Phase 3b, after Lean Canvas and KPIs are complete. Synthesizes all commercial inputs into financial projections and an investment rationale. Used for internal go/no-go on funding Phase 4+ work, and as input to a pitch deck if fundraising.

---

## What it produces

**Business Case** (`artifacts/phase-3b-definition/business-case.md`):

1. **Market opportunity** - TAM/SAM/SOM from Phase 2 market analysis
2. **Revenue model** - pricing, ARPU, payment terms (from Lean Canvas / BMC)
3. **Unit economics** - CAC, LTV, LTV:CAC ratio, payback period
4. **Financial projections** - Year 1-3 scenarios (conservative / base / optimistic)
5. **Cost structure** - team, infrastructure, marketing, operations
6. **Investment ask** - what is needed, for what, for how long (runway)
7. **Break-even analysis** - when and at what customer count
8. **Key assumptions and risks** - what must be true for projections to hold

---

## How to invoke

```bash
/pm-business-case           # interactive
/pm-business-case --agent   # autonomous synthesis from Lean Canvas + KPIs + market analysis
```

---

## Key rules

- All projections must be grounded in actual market data or validated assumptions from Phase 2-3a. Mark any assumption `[ASSUMED]` if not validated.
- Three scenarios are mandatory - a business case with only optimistic projections is not a business case.
- Unit economics must be calculated at the segment level, not blended across all segments.

---

## Dependencies

**Required before running:**
- `pm-lean-canvas` or `pm-business-model` - Revenue Streams and Cost Structure are direct inputs
- `pm-kpis` - AARRR metrics seed projection growth assumptions

**Recommended:**
- `pm-market-analysis` - TAM/SAM/SOM and competitor pricing data
- `pm-personas` - segment-level revenue and CAC estimates

**Produces for:**
- `pm-prd` - business case summary is a required PRD section
- `pm-product-roadmap` (v1) - investment staging informs roadmap phases
- `pm-pitch-deck` - business case is the financial backbone of the pitch

**Related skills:** `pm-kpis`, `pm-lean-canvas`, `pm-market-analysis`, `pm-product-roadmap`, `pm-pitch-deck`
