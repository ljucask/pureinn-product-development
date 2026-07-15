# pm-discovery-report

> Client-facing Discovery Report - "what we heard, what we recommend", incremental across sessions

**Phase:** 2 - Discovery (client discovery layer)  
**Agent mode:** `synthesis` - runs fully, review before sending to the client  
**Version:** 1.0.0  
**Triggers:** discovery report, client report, discovery summary, what we heard, discovery handoff, client deliverable

---

## When to use

Any time during a commissioned discovery - after the first session onward. Two jobs: a **confirmation loop** ("did we understand you correctly?" - errors caught here cost a conversation, not a sprint) and a **credibility signal** (a structured read-back of the client's own business is the strongest expertise proof during discovery).

`pm-problem-validation` stays the internal Go/No-Go artifact; this is the version the client reads - narrative, no internal scaffolding. Same facts, different audience.

---

## What it produces

One artifact (`artifacts/phase-2-discovery/discovery-report.md`), incremental and re-runnable:

- **Their context** - trigger, why now, the product's job in their business, success criteria
- **Who will use it** - three populations (customers / staff / management), provenance-marked (validated vs. `[CLIENT-ASSERTED]` vs. assumed)
- **How the work flows today** - as-is processes and friction
- **What they asked for → what we heard behind it** - including references ("like company XY") with an honest adopt/adapt/avoid take
- **Where we see the value** - incl. any tension between client benefit and user benefit, surfaced constructively
- **Recommendations, constraints, open questions, next steps**

---

## How to invoke

```bash
/pm-discovery-report           # interactive - asks purpose (interim / final / decision support)
/pm-discovery-report --agent   # autonomous draft from meetings + artifacts
```

**Re-run (delta mode):** updates only what new sessions support, flags reversals of statements the client already read, shows the delta before finalizing.

---

## Dependencies

**Reads (whatever exists - none hard-required):**
- `meetings/` - client-discovery and customer-discovery notes (primary source early)
- Track A-D artifacts, `problem-validation-summary.md` when it exists

**Produces for:**
- `pm-scope-brief` - the Discovery Report is its primary input
- `design-thinking` - client context and value alignment feed the Define stage (if Phase 3a runs)

**Related skills:** `pm-meeting`, `pm-discovery-interview`, `pm-problem-validation`, `pm-scope-brief`, `pm-personas`
