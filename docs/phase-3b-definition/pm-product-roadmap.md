# pm-product-roadmap

> Living strategic roadmap that evolves across three versions - v1 (Phase 3b) through v3 (Phase 5)

**Phase:** 3b (v1), 4 (v2), 5 (v3) - updates across all three phases  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.2.0  
**Triggers:** product roadmap, roadmap, delivery phases, strategic plan, phase planning

---

## When to use

Whenever roadmap-level thinking is needed. The roadmap is a living document - it is created in Phase 3b and updated twice (after Phase 4 and Phase 5). Each version adds a new layer without replacing what came before.

Re-run whenever upstream evidence changes: re-prioritization, new market data, revised personas, updated domain model.

---

## What it produces

**Product Roadmap** (`product/roadmap.md`) - single file updated across all three versions:

| Version | Phase | What is added |
|---|---|---|
| v1 | 3b | Vision + validated problem + customer segments + business model horizon. No features - strategic direction only. |
| v2 | 4 | Domain constraints and architecture decisions. Functional Decomposition: phases mapped to Domains and Feature Sets. Still no individual Features. |
| v3 | 5 | Feature view added. Phases aligned with Feature Sets and Delivery Stripes. Delivery timeline visible. |

The roadmap is NOT a sprint backlog. It communicates strategic intent and phase sequencing, not implementation detail.

---

## How to invoke

```bash
/pm-product-roadmap           # interactive - Step 0 detects version and state
/pm-product-roadmap --agent   # autonomous synthesis from available phase artifacts
```

Step 0 always runs first: reads the current workspace, identifies the existing roadmap version (v1/v2/v3), and determines what update or new version is needed. You never need to specify the version manually.

**Re-run with new inputs (delta mode):** compares new inputs against the current roadmap, updates only what new evidence supports, shows the delta explicitly before writing. Downstream cascade is surfaced: which Feature Set phase assignments, MVP scope stripes, or PRD sections may now be inconsistent.

---

## Top-down vs. bottom-up

The roadmap and feature list are iterative and bidirectional - not strictly top-down:

- **Top-down:** phases first (partial v1/v2), features derived, roadmap completed (v3) once features exist.
- **Bottom-up:** features extracted first (via `pm-features-list` or `pm-reverse-extract`), roadmap phases filled from them.

A partial roadmap is a valid expected state - capture phases you know, derive features, and return to complete remaining sections.

---

## Dependencies

**For v1 (Phase 3b):**
- `pm-problem-validation` - validated problem as strategic foundation
- `pm-business-model` or `pm-lean-canvas` - commercial horizon
- `pm-kpis` - success metrics per phase

**For v2 (Phase 4):**
- v1 roadmap
- `pm-domain-model` - domain constraints may shift phase ordering
- `pm-privacy-requirements` - compliance requirements may shift timelines

**For v3 (Phase 5):**
- v2 roadmap
- `pm-features-list` - feature inventory for the feature view
- `pm-mvp-scope` - MVP scope, Feature Sets, and Delivery Stripes

**Dependency guard (MVP Delivery View):** the v3 delivery view (stripes + MVP/POST-MVP cut) is the output of `pm-mvp-scope`, downstream of this skill. If stripe assignments and the IN/POST-MVP cut are absent from `feature_list.md` (e.g. a Rebuild where the roadmap runs before features are carded), the skill does **not** invent them - it finalizes every other section, marks `MVP Delivery View` as `[TBD - pending /pm-mvp-scope]`, and asks you to re-run once `pm-mvp-scope` has produced the cut.

**Produces for:**
- `pm-prd` - roadmap is a required PRD section (all versions)
- `pm-business-case` - roadmap phases inform investment staging
- All Phase 6 skills - v3 roadmap defines what gets built in which stripe

**Related skills:** `pm-prd`, `pm-features-list`, `pm-mvp-scope`, `pm-business-case`, `pm-kpis`
