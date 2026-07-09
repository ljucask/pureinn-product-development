# pm-personas

> Customer Segments, Personas, and Early Adopter Profile from VOC data

**Phase:** 2 - Discovery (Track D, Step 1)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.0.0  
**Triggers:** personas, customer segments, early adopters, VOC, customer profile, user research, interviews

---

## When to use

Phase 2, Track D, Step 1. Run before `jtbd-building` - JTBD analysis uses personas as input. This is a "bring your data" skill - no invented personas without data. If you have no data, Path B offers AI-powered elicitation from founder knowledge (assumption-based output, clearly marked).

---

## What it produces

Three artifacts (`artifacts/phase-2-discovery/`):

1. **Customer Segments** (`customer-segments.md`) - distinct groups with shared needs, segmentation criteria, size estimates, pain intensity, revenue potential, primary segment for MVP
2. **Personas** (`personas.md`) - 1-2 personas per key segment: goals, pains + intensity + workarounds, behaviors, tools they use, direct quotes, what success looks like, why they'd adopt / why they might not
3. **Early Adopters Profile** (`early-adopters-profile.md`) - who the first 10-50 customers are, what triggers them, what they need day 1, what they'll tolerate, where to find them

---

## How to invoke

```bash
/pm-personas           # interactive - asks which path (A/B)
/pm-personas --agent   # autonomous draft, requires review
```

**Two paths:**
- **Path A** - research data available: paste interview transcripts, synthetic interview outputs (SynthFolk, ChatGPT), survey results, or behavioral observations
- **Path B** - no data: guided elicitation across 3 question groups (who they are / the problem / behavior and adoption); output marked `[ASSUMED - validate with real users]`

**Re-run with new data (delta mode):** compares new inputs against the previous version, updates only what new evidence supports, shows delta explicitly, surfaces cascade to downstream artifacts (jtbd-building, pm-problem-validation, PRD, feature KANO/V×C).

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target customer direction and geography
- `pm-market-analysis` - segment data provides foundation for persona development

**Produces for:**
- `jtbd-building` - personas are the required input for JTBD analysis
- `pm-problem-validation` - Track D input for Phase 2 convergence
- `design-thinking` - personas feed the Define stage
- `pm-prd` - customer segments and personas are core PRD sections

**Related skills:** `jtbd-building`, `pm-market-analysis`, `pm-problem-validation`, `design-thinking`, `pm-process-flows`
