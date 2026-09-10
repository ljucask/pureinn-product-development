# pm-prototype - External tools reference

> Reference for `skills/pm-prototype/SKILL.md`. Everything specific to handing a prototype to an external tool: tool selection, the Lovable construction rules and operational tactics, and the handoff itself.

## Step 4: Select prototyping tool

From the "Prototyping" section of pureinn-variables, present the configured tools. Let the user pick which to target for this run (they may have several). If more than one is configured, use **AskUserQuestion**; recommend the tool that best fits the intent from Step 2:

- **Lovable** - functional full-stack (React + Tailwind + shadcn + Supabase). Best for clickable flows and functional/feasibility prototypes. Deepest prompt-optimization support (see the Lovable rules below).
- **v0 / Vercel** - fast UI generation, deploy to a live URL. Good for front-heavy UX/concept prototypes.
- **Figma Make** - design-native, best when the flow already lives in Figma.
- **Base44 / other** - manual paste (no MCP push here) - the compiled spec is copy-paste ready.

If no tool is configured, default to producing the spec paste-ready and note push is unavailable until an endpoint is added.

---

## Lovable build-prompt construction rules

**These are baked in - when the target is Lovable, the compiled build prompt MUST follow them.** They come from the Lovable Prompting Bible and are what separates a usable first prompt from a credit-burning mess. For other tools, apply the same underlying principles (front-load, fence scope, explicit stack, flow narrative, plan-first) adapted to the tool.

1. **The first prompt is everything.** `create_project(initial_message)` sets the tone for the entire build. It must be complete and precise upfront - not "we'll clarify later."

2. **Front-load and book-end.** The tool weights the **start and end** of the prompt most. Put app type + primary goal in the first two sentences. Restate the single hardest constraint (usually the out-of-scope fence) at the very end.

3. **Opening pattern:** start with `I need a [type] application with:` then the tech stack.

4. **State the stack explicitly, even if default.** Lovable default: Frontend React, styling Tailwind + shadcn/ui, Auth + DB Supabase (native). State it. Only override if the spec requires it.

5. **Split features: main vs secondary.** Do not present a flat list of equal features.

6. **In-scope / out-of-scope is mandatory.** This is the single most important block for a prototype - it stops the tool building the whole product. Explicitly fence what NOT to build ("Do not build auth / admin / other user types / real payments").

7. **Screen-by-screen, section-by-section.** Do not pile 5 things into one instruction. Name the pages, then direct: `Start with the [primary page] containing: [detailed requirements]`. Build order: front design first (page by page) → then backend/Supabase → then UX refinement.

8. **Flow as narrative.** "User lands on X → clicks Y → sees Z." Maps from pm-process-flows.

9. **Design guidance concrete.** Design principles, color palette, typography, layout, nav. Always mobile-first and responsive on shadcn/Tailwind breakpoints - no custom breakpoints unless required.

10. **Data model only if functional.** Entities + key states → Supabase tables. A static click-through skips this ("use mock data, no backend").

11. **Plan-first tail.** End the prompt with: `Before writing any code, create a phased plan, save it as plan.md, and confirm your understanding of the scope and what is out of scope before building.` This pairs with `plan_mode=true` on the first message and prevents hallucinated scope.

12. **Precision over vibes.** Specific element placement + consistent styling. Never "make it nice" - say what, where, and how.

13. **Fidelity calibration.** Match tool effort to the intent (Step 2). State it in the prompt: static clickable click-through vs. functional CRUD with real data.

14. **The spec IS the Knowledge Base.** Lovable's biggest lever is its project Knowledge Base (PRD, app/user flow, tech stack, frontend guidelines, backend structure). Our spec sections 1-5 map onto exactly those. Load the spec into the project Knowledge Base (`set_project_knowledge` via MCP), not only the first message - it grounds every subsequent prompt and cuts hallucination + credits.

15. **Confirm understanding before code.** The first message ends with: `Before writing any code, review the Knowledge Base and tell me your understanding of what to build and what is out of scope. Do not write code yet.` Only after the tool plays scope back correctly do you let it build. This is the anti-hallucination gate, paired with `plan_mode=true`.

**Multi-variant validation (UX hypothesis with competing directions):** when the intent is to compare directions, instruct: `Build N versions of [screen], each with a different [layout/visual approach], deploy all N, and return the live URLs.` (Lovable `create_project` per variant, then `deploy_project`.)

**Iterating a prototype (send_message):** scope-lock every follow-up - `Change only [X]. Do not alter [Y or Z]. Test that nothing else regresses.` Use `plan_mode=true` for delicate changes. For a visual-only tweak: `Make only visual changes. Do not touch logic, state, or APIs.`

---

## Lovable operational tactics (from the Bible)

These govern **how the run behaves** once the prompt is in Lovable - the skill applies them during handoff and iteration, and surfaces the relevant ones to the user.

**Credit economics (do not waste the user's credits):**
- **Free:** "Try to Fix" and publishing/deploy do **not** cost credits. Use "Try to Fix" first on any build error.
- **Costs credits:** each build message, and especially SQL / database scripts. When the prototype needs DB work, ask Lovable to output **all** SQL first (in one go) rather than running it piecemeal.
- One instruction at a time - piling 5 asks into one message burns credits and causes hallucination loops.

**Chat/plan mode vs build mode:**
- Use `plan_mode=true` (discuss, no code changes) for: the initial scope confirmation, weighing approaches, and any delicate change. It does not modify the project.
- Use normal build mode only once scope is confirmed.

**Debugging ladder (when a build breaks - climb in order, stop when fixed):**
1. **"Try to Fix"** up to 3 times (free).
2. Still broken → copy the error into a `plan_mode` message: `Use chain-of-thought reasoning to find the root cause. Do not edit code yet - investigate logs, flow and dependencies first, then propose a fix.`
3. UI bug → attach a **screenshot** (`files` on `send_message`) showing actual vs. intended.
4. Persistent → `Map the full flow (auth, data, integrations, state, redirects), document expected vs actual, and identify the root cause with evidence before changing anything.`
5. Debugging spiral → **revert to the last working version** rather than digging deeper.

**Reduce hallucination with visuals:** pass wireframes / Figma screenshots / reference UIs as `files` attachments on the message. A picture fences the design far better than prose.

**Reverse-meta (feed learnings back):** when a prototype iteration surfaces a fix or a scope correction, capture it in the spec's `## Result` (Step 8, in SKILL.md) as a reusable note - so the next prototype/spec starts one degree more precise.

**Note on scope:** the Lovable Bible also carries extensive refactoring / codebase-audit / production-maintenance prompts. Those are for mature production codebases and are **out of scope for a throwaway prototype** - do not apply them here. If a prototype graduates to real build, that is `pm-feature-design` + the build skills, not this skill.

---

## Step 6: Hand off to the tool

**If an MCP endpoint is configured for the selected tool:**

Confirm before any live call - MCP calls run on the user's real account and spend real credits.

**Lovable (mcp.lovable.dev):**
1. Warn once: `Lovable MCP = celý účet, live kredity, deploy je verejný na Free/Pro. Pokračovať?`
2. `create_project(initial_message = compiled build prompt, plan_mode = true)` - plan mode first so the tool confirms scope before spending build credits.
3. **Load the Knowledge Base:** push spec sections 1-5 into the project via `set_project_knowledge` so every later prompt is grounded (rule 14). Do this right after project creation.
4. **Confirm-understanding gate (rule 15):** the plan-mode reply must play the scope + out-of-scope back correctly. If it invented anything, correct it in `plan_mode` before allowing any code. Do not proceed on a wrong readback.
5. Return the **preview URL** and the tool's plan for the user to approve.
6. On approval, let the tool build; iterate via `send_message` with scope-locked follow-ups (attach screenshots as `files` for UI direction/bugs). Apply the debugging ladder if a build breaks.
7. When the user is happy: `deploy_project` → capture the **live URL** for the prototype reference.

**v0 / Vercel:** push the compiled prompt, return the deploy URL.

**Figma Make / Base44 / no endpoint:** present the compiled build prompt as a copy-paste block and tell the user to paste it into the tool. Remind them the spec is the source of truth if they iterate.

Then return to `SKILL.md` and run **Step 7 (Write the prototype reference back)**.

---

