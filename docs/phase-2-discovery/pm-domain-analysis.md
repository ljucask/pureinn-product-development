# pm-domain-analysis

> Domain Analysis Report and Legal & Regulatory Requirements from raw research inputs

**Phase:** 2 - Discovery (Track B)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.1.0  
**Triggers:** domain analysis, legal requirements, regulatory, compliance, industry analysis, certifications, Phase 2

---

## When to use

Phase 2, Track B. Runs in parallel with Tracks A, C, D. Bring Perplexity deep research on the domain, regulatory landscape, licensing requirements, and industry norms. This is a "bring your data" skill - Claude structures and formalizes the input.

**Important:** Legal analysis produced here should be validated by a legal professional before acting on it.

---

## What it produces

Two artifacts (`artifacts/phase-2-discovery/`):

1. **Domain Analysis Report** (`domain-analysis.md`) - Industry structure, key players, domain-specific constraints and norms, business model patterns in the space, incumbents' defensible advantages
2. **Legal & Regulatory Requirements** (`legal-requirements.md`) - Licensing, data protection obligations, sector-specific regulations (financial, healthcare, food, transport, etc.), **enterprise/B2B certifications** (SOC 2, ISO 27001 - timeline and cost, if selling to regulated buyers), EU AI Act assessment if applicable, showstoppers explicitly called out

---

## How to invoke

```bash
/pm-domain-analysis           # interactive - asks for research input
/pm-domain-analysis --agent   # autonomous draft from existing research files
```

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target markets and any known regulatory constraints

**Produces for:**
- `pm-problem-validation` - Track B input for Phase 2 convergence
- `pm-business-rules-library` - domain constraints shape what rules are needed
- `pm-privacy-requirements` - legal requirements from here feed directly into privacy planning

**Related skills:** `pm-market-analysis`, `pm-tech-feasibility`, `pm-problem-validation`, `pm-domain-model`
