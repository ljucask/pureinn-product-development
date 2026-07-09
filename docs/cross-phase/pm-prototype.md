# pm-prototype

> Cross-phase prototyping engine - compiles a tool-ready spec for Lovable, v0, Base44, or Figma Make

**Phase:** Cross-phase (Discovery → Build)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.1.0  
**Triggers:** prototype, prototyping, proof of concept, POC, spike, validate before build, lovable, base44, v0, figma make, clickable prototype, mockup, throwaway, quick validation

---

## When to use

Any time there is genuine uncertainty worth de-risking cheaply before production build. There is no fixed phase home:

- **During Discovery (Phase 2-3a):** concept desirability, UX hypothesis
- **Before a PRD initiative (Phase 3b):** flow validation, scope test
- **Inside Phase 6 (JIT):** UX/interaction validation before a feature enters build

---

## What it produces

**Spec mode (default):** tool-ready prototype spec (`prototypes/[scope-slug]-spec.md`) - a structured build prompt optimized for the selected prototyping tool. Pushed via MCP if a tool endpoint is configured; otherwise output as a paste-ready block.

**Result mode (re-run after prototype exists):** captures what the prototype proved or disproved, makes a decision, and cascades back to:
- Feature Card (if feature-scoped) - adds prototype reference and outcome
- Hypothesis Register - updates hypothesis status with prototype evidence

---

## How to invoke

```bash
/pm-prototype           # interactive - Step 0 detects spec mode vs. result mode
/pm-prototype --agent   # autonomous synthesis from available inputs
```

**Two modes, detected automatically at Step 0:**

| Mode | Trigger | What it does |
|---|---|---|
| **Spec mode** | No prototype exists yet | Gate-check → scope intake → ingest inputs → compile tool-ready spec → push or paste |
| **Result mode** | Prototype exists, you have results | Capture what was proved/disproved → decision → cascade to Feature Card / hypotheses |

---

## Scope - no limit

| Scope type | Example |
|---|---|
| Single feature | "Prototype FEAT-CHK-003 - the checkout flow" |
| PRD initiative | "Prototype the driver assignment module" |
| Whole product | "Build a clickable prototype of the full MVP" |
| User-type slice | "For the dispatcher, test the assignment flow only" |

---

## Tool integration

The skill reads the `Prototyping` section of `pureinn-variables.md` to find configured tool MCP endpoints. If more than one is configured (Lovable + v0, etc.), the skill asks which tool to target for this run.

If no endpoint is configured, the skill outputs a paste-ready build prompt block and reminds the user to add an endpoint to `pureinn-variables.md` for future push.

Supported tools: Lovable, v0/Vercel, Base44, Figma Make.

---

## Hard rule: no guessing

The prototype spec is only as good as its inputs. The skill never fabricates screens, flows, entities, fields, features, personas, or copy. Every element in the spec must trace to a real artifact or to something the user stated. Missing input = ask, not invent. A gap is marked `[ASSUMED - confirm before build]` only when the user has explicitly chosen from options.

---

## Dependencies

**Recommended (none strictly required - skill adapts):**
- `pm-process-flows` - user flows + screens map directly into the prototype's page/flow structure
- `pm-personas` - scopes tone, fidelity, and who the prototype is for
- `pm-hypotheses` - prototype usually tests a hypothesis; Result mode writes back here
- Feature Card (if feature-scoped) - spec pulls from it and writes a prototype reference back into it

**Produces for:**
- Feature Card `prototypes` section (if feature-scoped)
- `pm-hypotheses` - prototype results become experiment evidence in Results mode

**Related skills:** `pm-hypotheses`, `pm-problem-validation`, `pm-feature-design`, `pm-feature-card`, `pm-process-flows`
