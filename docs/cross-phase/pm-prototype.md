# pm-prototype

> Cross-phase prototyping engine - compiles a tool-ready spec for Lovable, v0, Base44, or Figma Make

**Phase:** Cross-phase (Discovery → Build)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.2.0  
**Triggers:** prototype, prototyping, proof of concept, POC, spike, validate before build, lovable, base44, v0, figma make, clickable prototype, mockup, throwaway, quick validation, in-repo prototype, coding agent prototype, prototype harness

---

## When to use

Any time there is genuine uncertainty worth de-risking cheaply before production build. There is no fixed phase home:

- **During Discovery (Phase 2-3a):** concept desirability, UX hypothesis
- **Before a PRD initiative (Phase 3b):** flow validation, scope test
- **Inside Phase 6 (JIT):** UX/interaction validation before a feature enters build

---

## Two paths, chosen for you

The skill no longer assumes the prototype is built somewhere else. At **Step 3b** it decides how deep the prototype has to be and which of two structurally different paths builds it:

| Path | What it is | What you get |
|---|---|---|
| **External tool** | one-shot handoff - the brief is compiled, sent, and iterated through the tool | tool-ready spec (`prototypes/[scope-slug]-spec.md`), pushed via MCP or paste-ready |
| **In-repo** | a continuous loop with a coding agent - no brief to compile, no moment of handoff | a prototype folder with a harness carrying the four states, fixtures, a time scrubber, variants, device presets, an annotation layer and a local event log |

**The path is an output of the flow, not a question you answer up front.** It follows from who the prototype is for and which uncertainty it resolves - a flow-comprehension question and a business-rule-correctness question do not belong on the same path.

---

## Audience decides depth

"Deep enough to decide" means nothing until you say who is looking. Each audience makes different things non-negotiable and different things safely fake:

| Audience | Must be real | May be faked | What kills it |
|---|---|---|---|
| Internal team / feasibility | domain model, rules, edge states | visuals, branding, breadth | a pretty UI over logic that does not work |
| Investor / exec | narrative, key screens, defensible numbers | breadth, edge states, real data | numbers that collapse on the first question |
| Users (usability test) | flow, copy, realistic content, empty and error states | backend, scale, performance | a dead button - the test is void |
| Idea validation | the one uncertain mechanism | everything else | widening scope before the core is proven |
| Client / pitch | their domain language, their real scenario | generality, architecture | a generic example instead of their world |

More than two audiences triggers a warning and a request for the primary one - a prototype serving three at once usually serves none, and that is the moment it quietly starts becoming a product.

---

## What it produces

**Spec mode (default):** either a tool-ready prototype spec for an external tool, or an in-repo prototype folder with its harness - whichever the path decision reached. The in-repo folder sits at `prototypes/[name]/` and carries the uncertainty, the audience, the classification, a `targets:` link back to the production artifact it is about, a declared stop condition, and the hypotheses/findings pair.

**Prototypes stay out of the production registers.** Most prototypes die - that is what they are for - so a killed one should cost a deleted folder, not a clean-up of dead FEAT-IDs, speculative entities and rows in the delivery plan. Prototype feature IDs are `PRT-` rather than `FEAT-`, so one can never be mistaken for a committed feature.

**Promotion is layer by layer, not a rewrite:** the thin card becomes a Feature Card with a real FEAT-ID and `promoted_from:`, local rules and entities move into the global registers, and the prototype folder freezes as history.

**Result mode (re-run after prototype exists):** records the verdict as one of four states - **never "validated"**:

| State | What follows |
|---|---|
| Supported within scope | cascades to the Feature Card and hypothesis register |
| Refuted within scope | cascades, and a kill must clear five conditions before it is recorded |
| **Prototype or study failure** | **cascades nowhere** - the instrument did not expose the hypothesis, so belief in the product is unchanged and the test gets re-run |
| Inconclusive | cascades nowhere; schedules another round or a different method |

The third state is the one teams skip, and skipping it is how a broken test becomes a verdict on an idea.

---

## How to invoke

```bash
/pm-prototype           # interactive - Step 0 detects spec mode vs. result mode
/pm-prototype --agent   # autonomous synthesis from available inputs
```

**Two modes, detected automatically at Step 0:**

| Mode | Trigger | What it does |
|---|---|---|
| **Spec mode** | No prototype exists yet | Gate-check → scope intake → ingest inputs → audience, depth and path → build by the path that fits |
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

**On the in-repo path no endpoint is needed** - the prototype is built here, against a harness copied from the skill's own `references/scaffold/`. The harness must be served rather than opened as a file, because the artifact runs in an iframe so the device switcher triggers its real media queries.

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
