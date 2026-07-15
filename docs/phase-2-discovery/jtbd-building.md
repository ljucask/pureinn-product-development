# jtbd-building

> JTBD Analysis using Bob Moesta's Jobs-to-be-Done framework - job stories, Forces Diagram, and switching logic

**Phase:** 2 - Discovery (Track D, Step 2)  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 1.1.0  
**Triggers:** JTBD, jobs to be done, forces diagram, switching logic, job stories, customer motivation, commissioner job

---

## When to use

Phase 2, Track D, Step 2. Run after `pm-personas`. Personas give you who - JTBD gives you why. JTBD analysis goes deeper than pain points: it explains the causal mechanism behind why someone would switch from their current solution to yours. Also captures job **frequency and context** (how often, under what pressure).

**Commissioned builds - two levels of job:** the commissioner has their own job at business level (earn more / spend less / reduce risk / comply), recorded as a separate **Commissioner Job** story, distinct from and never averaged with end-user jobs.

---

## What it produces

**JTBD Analysis** (`artifacts/phase-2-discovery/jtbd-analysis.md`):

1. **Job Stories** - "When [situation], I want to [motivation], so I can [outcome]" formulations per key persona - not feature requests, but the underlying job
2. **Forces Diagram** - four forces operating on the switching decision:
   - Push: frustration with the current situation
   - Pull: attraction toward the new solution
   - Anxiety: fears about switching
   - Habit: inertia pulling back to the status quo
3. **Switching logic** - what specific trigger causes someone to start looking, and what makes them choose

---

## How to invoke

```bash
/jtbd-building           # interactive
/jtbd-building --agent   # autonomous draft, requires review
```

---

## Dependencies

**Required before running:**
- `pm-personas` - personas and their pains are the foundation for JTBD analysis

**Recommended:**
- Raw interview transcripts - JTBD is most powerful when grounded in actual interview data

**Produces for:**
- `pm-problem-validation` - JTBD analysis is a Track D input for Phase 2 convergence
- `design-thinking` - Forces Diagram informs the Define stage and HMW framing
- `pm-prd` - JTBD core is a required PRD section

**Related skills:** `pm-personas`, `pm-problem-validation`, `design-thinking`
