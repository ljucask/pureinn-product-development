# pm-market-analysis

> Market Size Analysis (TAM/SAM/SOM), Competitor Analysis, SWOT, and Market Timing Rationale

**Phase:** 2 - Discovery (Track C)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.2.0  
**Triggers:** market analysis, TAM SAM SOM, competitor analysis, SWOT, market sizing, competitive landscape, client market

---

## When to use

Phase 2, Track C. Runs in parallel with Tracks A (tech feasibility), B (domain analysis), and D (customer research). Output feeds the Phase 2 convergence skill (`pm-problem-validation`).

**Commissioned builds:** the analysis targets the **client's market and the client's competitors**, not yours - stated explicitly at the top of the artifacts.

Three input paths - choose based on what you have:

| Path | When | Note |
|---|---|---|
| **Path A** - paste your research | You have Perplexity/ChatGPT market data | Most reliable - research-backed output |
| **Path B** - guided elicitation | You know the domain but haven't done formal research | Produces assumption-based output marked for validation |
| **Path C** - AI-powered research | No prior research, want AI to do it | Requires `OPENAI_API_KEY` in `pureinn-variables.md` |

Paths A and C produce research-backed artifacts. Path B produces assumption-based output marked `[ASSUMED - validate with real data]`.

---

## What it produces

Four artifacts (`artifacts/phase-2-discovery/`):

1. **Market Size Analysis** (`market-size.md`) - TAM, SAM, SOM with methodology (top-down and/or bottom-up), data sources, and confidence ratings
2. **Competitor Analysis** (`competitor-analysis.md`) - Direct and indirect competitors, positioning map, and a **per-competitor profile** (pricing model, go-to-market, customer feedback from reviews, origin/trajectory, key weaknesses mapped to our opportunity) for the 2-4 competitors that matter most
3. **SWOT Analysis** (`swot.md`) - Strengths, Weaknesses, Opportunities, Threats with strategic implications
4. **Market Timing Rationale** (`market-timing.md`) - "Why now?" argument: what changed in technology, regulation, behavior, or economics

---

## How to invoke

```bash
/pm-market-analysis           # interactive - asks which path (A/B/C)
/pm-market-analysis --agent   # autonomous draft from existing research artifacts
```

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target segment and geography are defined there

**Produces for:**
- `pm-problem-validation` - Track C input for Phase 2 convergence
- `pm-personas` - segment data informs persona development
- `pm-prd` - market context is a key PRD section
- `pm-business-case` - TAM/SAM/SOM feeds financial projections
- `pm-product-roadmap` - market sizing and timing frame roadmap prioritization

**Related skills:** `pm-domain-analysis`, `pm-personas`, `pm-problem-validation`, `pm-business-case`
