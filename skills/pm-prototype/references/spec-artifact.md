# pm-prototype - Spec artifact reference

> Reference for `skills/pm-prototype/SKILL.md`. The prototype spec's shape: the universal, tool-agnostic core.

## Step 5: Compile the prototype spec

Generate `[scope]-prototype-spec.md`. It has two layers:

1. **Universal core** - tool-agnostic, human-readable, the source of truth for the prototype.
2. **Compiled build prompt** - the core rewritten in the selected tool's optimal format. This is what goes into the tool. For Lovable it follows the Lovable construction rules in `references/external-tools.md`; for other tools it follows the same universal principles adapted to that tool.

---

### ARTIFACT: [scope]-prototype-spec.md

```markdown
# Prototype Spec - [Scope name]

**Scope:** [feature FEAT-ID / initiative / product / slice]
**User type (if scoped):** [type or "all"]
**Intent:** [UX-flow / concept / feasibility / stakeholder]
**Target tool:** [Lovable / v0 / Figma Make / manual]
**Success criterion:** [The prototype succeeds if [observable signal], otherwise we [action].]
**Status:** Spec ready → awaiting build

---

## 1. Goal (what we are learning)

[2-3 sentences. What decision is blocked on this prototype. What signal we are hunting.]

## 2. In scope / Out of scope

**In scope (build this):**
- [screen / flow / interaction]

**Out of scope (do NOT build - fence hard):**
- [everything the tool must not wander into - auth if not needed, admin, other user types, real payments, etc.]

## 3. Screens + flow

**Primary screen (build first):** [name] - [detailed contents]

| Screen | Purpose | Key elements | Reached from |
|---|---|---|---|
| [screen] | [why] | [components] | [prev screen / entry] |

**User flow (narrative):**
[User lands on X → does Y → sees Z. Map from pm-process-flows.]

## 4. Data + key interactions

[Only if functional. Entities + key states the prototype needs, and what each core interaction does.]

- [Entity]: [fields the prototype shows], states: [state → state]
- Interaction: [action] → [result]

## 5. Design guidance

- **Fidelity:** [static click-through / functional]
- **For whom:** [persona - tone, polish level]
- **Look:** [design principles, color, typography, layout, nav - or "tool default taste"]
- **Responsive:** mobile-first, shadcn + Tailwind breakpoints.

## 6. Acceptance signals (maps to success criterion)

[The concrete things a user/tester must be able to do or feel for the prototype to have answered the question.]

- [ ] [signal]

---

## Compiled build prompt ([tool])

> Paste this into [tool], or push via MCP (Step 6).

[The compiled, tool-optimized prompt - see the construction rules in `references/external-tools.md`.]

---

## Result

[Empty until Result mode (Step 8, in SKILL.md). Do not fill at spec time.]
```

---

