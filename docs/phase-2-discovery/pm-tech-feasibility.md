# pm-tech-feasibility

> Tech Feasibility Report from raw research inputs

**Phase:** 2 - Discovery (Track A)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** tech feasibility, technology assessment, stack feasibility, technical risks, Phase 2 Track A

---

## When to use

Phase 2, Track A. Runs in parallel with Tracks B, C, D. This is a "bring your data" skill - feed it Perplexity/ChatGPT deep research output, Tech Lead notes, or domain knowledge, and it structures the analysis. It does not hallucinate technical facts.

---

## What it produces

**Tech Feasibility Report** (`artifacts/phase-2-discovery/tech-feasibility.md`):
- Stack viability assessment - can the required tech be built with available tools?
- Key technical risks with probability and mitigation
- Build vs. buy decisions for critical components
- AI component cost modeling (if product includes AI/ML)
- Talent availability for the required stack
- Architecture approach recommendation (high-level)
- Open technical questions requiring resolution before Phase 4

---

## How to invoke

```bash
/pm-tech-feasibility           # interactive - asks for research input
/pm-tech-feasibility --agent   # autonomous draft from existing research files
```

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - tech constraints, non-negotiables, and budget cap are defined there

**Produces for:**
- `pm-problem-validation` - Track A input for Phase 2 convergence
- `pm-domain-model` - tech stack context informs domain modeling
- `common-ground` (fullstack-dev-skills) - tech feasibility report is a key input for tech stack finalization

**Related skills:** `pm-domain-analysis`, `pm-problem-validation`, `pm-domain-model`
