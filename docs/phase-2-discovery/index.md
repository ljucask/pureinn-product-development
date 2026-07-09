# Phase 2 - Discovery

Four parallel research tracks that converge into a Problem Validation Summary. The goal is to understand the market, technology, domain, and customer deeply enough to validate (or invalidate) the problem worth solving.

**Duration:** 1-3 weeks  
**Gate type:** Soft gate (gaps acknowledged, can proceed)  
**Playbooks:** Greenfield

---

## When to enter this phase

Enter Phase 2 after Phase 1 (or directly with `/pureinn discover`). All four tracks run in parallel and converge at the Problem Validation Summary.

**"Bring your data" rule:** Claude structures and formalizes what you bring - it does not hallucinate market data or interview insights. Research is done externally first, then fed in.

**Exception:** `/pm-market-analysis` Path C runs AI-powered web research via Perplexity/OpenAI (requires `OPENAI_API_KEY` in `pureinn-variables.md`).

---

## What you need before entering

- Phase 1 artifacts (Project Charter, basic scope)
- External research material per track (or willingness to proceed assumption-based)

Every skill in this phase offers a graceful degradation path - if you have no data, it generates assumption-based output marked `[ASSUMED - validate with real users]` rather than blocking.

---

## Four tracks (run in parallel)

### Track A - Technology

| Skill | Before running | Output |
|---|---|---|
| [pm-tech-feasibility](pm-tech-feasibility.md) | Perplexity / Tech Lead research on stack, APIs, constraints | Tech Feasibility Report |

### Track B - Domain

| Skill | Before running | Output |
|---|---|---|
| [pm-domain-analysis](pm-domain-analysis.md) | Perplexity / domain + regulatory research | Domain Analysis, Legal Requirements |

### Track C - Market

| Skill | Before running | Output |
|---|---|---|
| [pm-market-analysis](pm-market-analysis.md) | Competitor research - or use Path C (AI-powered, no prep needed) | Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT |

### Track D - Customer

| Skill | Before running | Output |
|---|---|---|
| [pm-personas](pm-personas.md) | ≥10 customer interviews (or assumption-based) | Customer Segments, Personas, Early Adopters Profile |
| [jtbd-building](jtbd-building.md) | pm-personas must exist | JTBD Analysis, Forces Diagram |

### Convergence

| Skill | Before running | Output |
|---|---|---|
| [pm-problem-validation](pm-problem-validation.md) | All Track A-D outputs complete | Problem Validation Summary (Phase 2 exit artifact) |

---

## What you exit with

- **Tech Feasibility Report** - stack viability, key constraints, risks
- **Domain Analysis** - domain structure, regulatory requirements, legal landscape
- **Market Analysis** - TAM/SAM/SOM, competitor landscape, SWOT
- **Customer Segments + Personas** - who the customer is, what they need
- **JTBD Analysis** - Jobs-to-be-Done + Forces Diagram per persona
- **Problem Validation Summary** - synthesizes all tracks; Phase 2 exit artifact

---

## Phase exit gate

Run `/pureinn` after completing Phase 2 to check the exit gate.

**Gate type: Soft.** The engine checks all four tracks and the Problem Validation Summary. You can acknowledge gaps and proceed, or loop back to strengthen weak tracks.

Phase 3a can **start in parallel with late Phase 2** once the Problem Validation Summary exists.
