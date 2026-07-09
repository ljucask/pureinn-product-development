# pm-kpis

> AARRR funnel metrics, North Star Metric, and OKRs - the measurement framework for the product

**Phase:** 3b - Definition  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** KPIs, OKRs, north star metric, AARRR, success metrics, funnel metrics

---

## When to use

Phase 3b, after Lean Canvas or Business Model Canvas. Produces the measurement framework used in the PRD, business case, and roadmap. Without this, there is no way to know if the product is working.

---

## What it produces

**KPIs & Metrics Framework** (`artifacts/phase-3b-definition/kpis-metrics.md`):

1. **North Star Metric** - the single metric that best captures the core value delivered to customers
2. **AARRR Funnel metrics** - one leading metric per stage:
   - Acquisition: how users find you
   - Activation: first value moment
   - Retention: ongoing engagement
   - Referral: word of mouth
   - Revenue: monetization signal
3. **OKRs** - Objectives and Key Results for the next 1-2 roadmap phases
4. **Instrumentation notes** - what needs to be tracked and where

---

## How to invoke

```bash
/pm-kpis           # interactive
/pm-kpis --agent   # autonomous synthesis from Lean Canvas / BMC
```

---

## Key rules

- North Star Metric must reflect value delivered to customers, not business-internal output (not "lines of code shipped" or "revenue" - revenue is a lagging indicator). Examples: "trips completed," "tasks automated per week," "reports shared."
- OKRs must have pre-defined success numbers set before work starts. Retroactive success criteria are a bias trap.
- AARRR metrics are leading indicators. Revenue is last, not first.

---

## Dependencies

**Required before running:**
- `pm-lean-canvas` or `pm-business-model` - Revenue Streams and Customer Segments are primary inputs

**Recommended:**
- `pm-market-analysis` - market size context for acquisition targets
- `pm-personas` - AARRR stage definitions are persona-specific

**Produces for:**
- `pm-business-case` - KPIs seed the financial projection assumptions
- `pm-prd` - KPIs and North Star are required PRD sections
- `pm-product-roadmap` (all versions) - success criteria per phase

**Related skills:** `pm-lean-canvas`, `pm-business-case`, `pm-prd`, `pm-product-roadmap`
