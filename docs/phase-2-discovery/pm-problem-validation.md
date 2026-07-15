# pm-problem-validation

> Phase 2 convergence artifact - synthesizes all four discovery tracks into one Problem Validation Summary

**Phase:** 2 - Discovery (Convergence)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** problem validation, validation summary, Phase 2 exit, discovery synthesis, problem confirmed

---

## When to use

After all four Phase 2 tracks are complete (or sufficiently advanced). This is the Phase 2 exit artifact. No new research happens here - it is pure synthesis of what the four tracks found.

Can be run with partial track outputs if some tracks are still in progress. Missing tracks are surfaced as gaps with explicit impact statements.

---

## What it produces

**Problem Validation Summary** (`artifacts/phase-2-discovery/problem-validation-summary.md`):

- Problem statement (refined from all four tracks)
- Evidence per track: Track A (tech), B (domain), C (market), D (customer)
- Cross-track convergence: where tracks agree (high-confidence signal)
- Cross-track conflicts: where tracks disagree (hypothesis to resolve in Phase 3a)
- Riskiest remaining assumptions before Phase 3a
- Phase 2 verdict: problem validated / partially validated / not validated (+ what's missing)

---

## How to invoke

```bash
/pm-problem-validation           # interactive synthesis
/pm-problem-validation --agent   # autonomous synthesis from all track artifacts
```

---

## Dependencies

**Strongly recommended before running:**
- `pm-tech-feasibility` - Track A
- `pm-domain-analysis` - Track B
- `pm-market-analysis` - Track C
- `pm-personas` - Track D Step 1
- `jtbd-building` - Track D Step 2

**Produces for:**
- `pm-prd` - Problem Validation Summary is a primary PRD input
- `design-thinking` - feeds the Define stage (problem statement, POV)
- `pm-discovery-report` - on commissioned builds, its client-facing narrative companion (same facts, different audience)

**Related skills:** `pm-personas`, `jtbd-building`, `pm-market-analysis`, `pm-tech-feasibility`, `pm-domain-analysis`
