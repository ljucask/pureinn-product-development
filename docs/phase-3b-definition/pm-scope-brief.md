# pm-scope-brief

> Scope Brief - what exactly gets built on a commissioned build; Phase 3b alternative to the PRD

**Phase:** 3b - Commercial Definition (alternative exit artifact)  
**Agent mode:** `decision` - drafts, then requires your review (the scope cut is decided here)  
**Version:** 1.0.0  
**Triggers:** scope brief, scope definition, client scope, what we will build, definition document, engagement scope, build definition

---

## When to use

When the mandate is already given - a client commissioned the build, an exec directed it - and full Phase 3a validation + business-model work would re-answer an answered question. The market risk sits with the commissioner; what you owe them is a precise definition. **Speculative products (your own market bet) use `/pm-prd` via full Phase 3a+3b instead** - the skill runs a context fit check and says so.

---

## What it produces

One artifact (`product/scope_brief.md`) - fills the PRD slot for Phase 4-5:

- **Problem framing (POV-lite)** - even a directive build states the problem behind the mandate
- **Users and roles** - three populations, provenance-marked
- **Business Capabilities** - the named downstream interface: `pm-entity-registry` extracts entities from it, `pm-features-list` derives features from it, exactly as from PRD Section 7
- **Scope: IN / Deferred / Non-goals** - each IN item with evidence + acceptance signal
- **References translated** - directive references become bounded requirements with explicit "NOT copying" limits
- **Edge cases register** - Exception-sweep findings, product-enforced ones tagged `[CANDIDATE-BR]` (seed the business rules register)
- **Integrations, data, content, operations** - with client-side dependencies named
- **Acceptance** - done-criteria, sign-off model, post-launch success measure
- **Change Log** - after baseline, every scope change lands here first (in client work a scope change is a commercial event)

---

## How to invoke

```bash
/pm-scope-brief           # interactive - proposes the scope cut, you confirm
/pm-scope-brief --agent   # autonomous draft; scope decisions still require your review
```

**Guarded traps:** a reference classified *hypothesis* never enters IN as settled; missing staff/admin capabilities get flagged (the classic launch failure); every IN item needs an acceptance signal.

---

## Dependencies

**Reads:**
- `artifacts/phase-2-discovery/discovery-report.md` - primary input (falls back to `meetings/` notes + Track artifacts)
- `design-thinking-synthesis.md` if Phase 3a ran

**Produces for:**
- `pm-entity-registry`, `pm-features-list` - via Business Capabilities
- `pm-process-flows` - roles and process context
- `pm-business-rules-library` - `[CANDIDATE-BR]` edge cases

**Related skills:** `pm-discovery-report`, `pm-prd`, `pm-entity-registry`, `pm-features-list`, `pm-process-flows`, `pm-business-rules-library`
