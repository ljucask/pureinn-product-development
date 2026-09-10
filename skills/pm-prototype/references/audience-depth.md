# pm-prototype - Audience, depth and path reference

> Reference for `skills/pm-prototype/SKILL.md`. Read it at **Step 3b**, before choosing how the prototype gets built.

Two questions decide everything downstream: **who is looking at it**, and **which uncertainty it resolves**. The first sets what has to be real and what may be admitted-fake. The second picks the build path and the tool.

---

## 1. Audience decides depth

"Deep enough to decide" is not a criterion until you say who is looking. What may be faked differs per audience, which is why depth cannot be a single dial.

| Audience | Must prove | Deep | May be thin or faked | What kills it |
|---|---|---|---|---|
| **Internal team / feasibility** | it works with real state and data | domain model, rules, edge states, integrations | visuals, branding, content, breadth | a pretty UI over logic that does not work |
| **Investor / exec** | it has value and holds together | narrative, key screens, numbers that survive questions, business model | breadth, edge states, real data | numbers that collapse on the first question |
| **Users (usability test)** | people understand it and finish the task | flow, copy, realistic content, empty and error states | backend, architecture, scale, performance | a dead button - the test is void |
| **Idea validation (own uncertainty)** | the core mechanism works at all | the one uncertain mechanism | everything else | widening scope before the core is proven |
| **Client / pitch** | we understood their problem | their domain language, their real scenario | generality, architecture, scale | a generic example instead of their world |

Ask with **AskUserQuestion**, multi-select allowed.

**Guardrail - more than two audiences.** Warn and ask for the primary one:

> Prototyp pre [N] publiká naraz obvykle neslúži ani jednému - každé z nich chce hlbokú inú vec. Ktoré je primárne? Ostatné ostanú ako sekundárne a ich nároky ustúpia.

That is also the moment a prototype quietly starts growing into a product, so it is worth naming rather than absorbing.

**Two audience-conditional rules that come from the evidence:**

- **Variants are mandatory when the prototype exists to choose a direction.** A single committed option produces inflated ratings and near-zero rejection - in the controlled study none of 36 participants rejected the single design, while 3 of 12 rejected an alternative when shown three. When the prototype is an *answer* rather than a *choice* (a commissioned assignment, a decided direction), one variant is correct.
- **Behaviour capture earns its place the moment real users touch it.** For a reader-reviewed prototype it is overhead; for a usability test it is the difference between what people did and what they said.

**Investor fidelity is not "as polished as possible."** Three crowdfunding studies found an inverted-U between prototype fidelity and funding performance - moderate outperformed both very low and very high, the authors arguing that extreme fidelity reads as a fait accompli and reduces perceived co-creation.

---

## 2. Uncertainty decides the path and the tool

The audience largely predicts which uncertainty matters, so propose the row that follows from it and confirm rather than asking cold.

| Uncertainty | Right form | Path | Tool |
|---|---|---|---|
| Is the flow understandable? | wireframe or clickable flow | external | Figma, Figma Make |
| Is the visual direction right? | visual design on a canvas | external | Claude Design, v0 |
| Does the behaviour work with real state and data? | coded prototype, synthetic data | **in-repo** | a coding agent here; or v0 / Lovable when nothing in the real codebase matters yet |
| Is the integration technically feasible? | technical spike | **in-repo** | a coding agent against the real interfaces |
| Are business rules or state transitions correct? | executable acceptance cases | **in-repo** | visual completeness is actively misleading here |
| Is it production-ready? | not a prototype | — | normal delivery. Say so and stop |

**Where the boundary really sits.** One-shot external generation is strongest for visual direction, interaction comprehension and making an abstract idea discussable. It is weak for custom architecture, data, integrations, and business-rule correctness - a generated happy path routinely bypasses the hard constraint. In-repo iteration is stronger wherever the answer depends on real interfaces, persistent state, permissions, or existing product behaviour.

Neither answers **desirability** on its own. Both reduce the cost of making a stimulus; only target-user behaviour supplies the evidence.

---

## 3. Route

| Path | Read next | Nature |
|---|---|---|
| **External tool** | `references/external-tools.md` → Step 4, then `references/spec-artifact.md` → Step 5, then Step 6 | one-shot handoff: compile the brief, send it, iterate through the tool |
| **In-repo** | `references/in-repo-loop.md`, and `references/scaffold/` for the harness | a continuous loop: no brief to compile, no moment of handoff |

**Combined - visuals on a canvas, consumed by a coded prototype** - is a real path and nobody arrives at it unprompted, but it is not supported end to end yet. If it is what the work needs, say so plainly and pick one of the two for this run.

Both paths converge back on **Step 7** (write the prototype reference back) and **Step 8** (result mode).

**A prototype that has been paused and returned to keeps its path.** Switching mid-flight means rebuilding, so if the path looks wrong, that is a restart decision, not a toggle - see the restart signals in `in-repo-loop.md`.
