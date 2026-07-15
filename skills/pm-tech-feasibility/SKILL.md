---
name: pm-tech-feasibility
description: Generate a Tech Feasibility Report from raw research inputs. Use in Phase 2 (Track A) after collecting Perplexity/ChatGPT deep research and Tech Lead analysis.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.1.0"
  domain: product-management
  triggers: tech feasibility, technology assessment, stack feasibility, technical risks, no-code, disruption, Phase 2 Track A
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-domain-analysis, pm-problem-validation, pm-domain-model
---

# PM - Tech Feasibility Report


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Takes raw research input (Perplexity deep research output, ChatGPT analysis, Tech Lead notes, domain knowledge) and produces a structured Tech Feasibility Report.

This is a "bring your data" skill - Claude cleans, structures, and formalizes the input. No AI hallucination of technical facts.

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - tech constraints, non-negotiables, and budget cap are defined there

**Produces artifacts used by:**
- `pm-problem-validation` - tech feasibility is Track A input
- `pm-domain-model` - tech stack context informs domain modeling
- `common-ground` - tech feasibility report is a key input for tech stack finalization

---

## Step 0: Current state check

Check for existing artifacts:
- Tech Feasibility Report

Also check: does a Project Charter exist? Cross-reference tech constraints and budget cap stated there.

Look for: sections marked TBD, open questions not yet resolved, stack recommendation that conflicts with known constraints, AI cost modeling missing if product has AI components.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

### Re-run with new inputs (delta mode)

If a Tech Feasibility Report already exists and you are re-running it because new research arrived (new spike results, updated Tech Lead analysis, new vendor evaluation), do NOT rewrite from scratch and do NOT duplicate existing content:

1. **Read the current report first** and capture its claims in the sections most sensitive to new input: Recommended Stack, Technical Risks, Build vs Buy vs Partner, Confidence Level.
2. **Re-validate against the new sources.**
3. **Change only what the new evidence supports.** Append genuinely new findings; where new data revises a prior claim (e.g., a stack choice or risk rating), mark `[UPDATED - previous: X / new: Y - reason]`; leave what the new input does not address `[UNCHANGED]`. Where sources conflict, surface `[CONFLICT]` rather than picking one silently.
4. **Show the delta and wait for confirmation before writing** - never silently overwrite a prior feasibility verdict.
5. **Surface the cascade:** name downstream artifacts now possibly inconsistent - `/pm-domain-model` (tech stack context), `/pm-prd` (constraints), `common-ground` (tech stack finalization) - and recommend `/pm-audit strategy` to verify the strategic layer still agrees.

---

## Step 1: Gather inputs

First, ask:

Do you have technical research or analysis to work with?

  A) Yes - I have Perplexity/ChatGPT research output or tech lead analysis to paste
  B) No - I'll share what I know about the technical requirements and constraints

---

### Path A - Research available

```
I need inputs for the Tech Feasibility Report.

1. PRODUCT
   What are you building? (1-2 sentences, core functionality)
   What are the key technical requirements? (real-time, offline, high-scale, ML, integrations...)

2. RESEARCH (paste raw output below)
   Perplexity / ChatGPT deep research output:
   [paste here]

   Tech Lead / developer manual analysis (if available):
   [paste here]

3. KNOWN CONSTRAINTS
   Any tech stack preferences? (framework, language, cloud provider)
   Are integrations with existing systems required? Which ones?
   Any security / compliance requirements? (GDPR, SOC2, HIPAA...)
   (Commissioned builds: the workspace meetings/ client-discovery notes
    often already capture the client's systems, IT policy, and hosting
    constraints - point me there and I read them in full.)

4. CRITICAL QUESTIONS
   What are the biggest technical risks / unknowns?
   What don't we know yet and need to validate?
```

---

### Path B - No research (guided elicitation)

Guide the user through 2 rounds to reconstruct the technical picture from what they know. Output marked as assumption-based, with explicit flags on unknowns requiring validation.

**Group 1 of 2 - Product and requirements**

Use AskUserQuestion tool for these two questions:

What best describes the core technical challenge?

  A) Standard CRUD + business logic - no unusual technical requirements
  B) Real-time features - live updates, collaboration, synchronization
  C) Data-intensive - large volumes, analytics, ML/AI, complex queries
  D) Integration-heavy - connects multiple external systems or APIs

What are the scale requirements at launch and within 12 months?

  A) Small - under 1,000 users, no unusual load
  B) Medium - 1,000 to 50,000 users, moderate concurrent usage
  C) Large - 50,000+ users or high-frequency transactions
  D) Unknown - not yet estimated

Then ask as plain text:

What are you building? Describe the core functionality in 2-3 sentences, focusing on what the system needs to do technically.

What are the key technical requirements? List any real-time needs, offline requirements, AI/ML components, or external system integrations. Do you have stack or infrastructure preferences?

After answers, confirm and proceed.

---

**Group 2 of 2 - Constraints, compliance, and unknowns**

Use AskUserQuestion tool for these two questions:

Are there security or compliance requirements?

  A) GDPR only - standard EU data protection
  B) GDPR + industry-specific (fintech, healthtech, legaltech)
  C) Enterprise security standards required (SOC2, ISO 27001)
  D) None identified yet

How experienced is the team with the core technical challenges?

  A) Strong - team has built this type of system before
  B) Moderate - relevant experience, some new territory
  C) Limited - significant learning curve expected
  D) Unknown - technical team not yet in place

Then ask as plain text:

What external APIs, platforms, or data sources must the product integrate with? Are any integrations with existing systems required?

What are the biggest technical risks or unknowns? What could break the product concept if the assumption turns out wrong? What needs a technical spike or prototype to validate?

After answers, show complete summary. Flag unvalidated risks explicitly.

Note at the top of every generated artifact: `> Assumption-based - built from founder knowledge, not technical research. Items marked [NEEDS VALIDATION] require verification with a technical lead or prototype before committing to architecture.`

---

## Step 2: Generate artifact

Generate in English.

**Feasibility judgment rules (apply when writing the verdict):**
- Feasibility is **relative, not absolute**. The question is never "can this be built" (almost everything can) - it is "can THIS team build it within THIS budget and timeline." Anchor the verdict to the team-experience answer and the charter's constraints, and state what would flip it (e.g. "🟢 with a senior BE hire, 🟡 without").
- Any risk rated High probability × High impact - or anything driving a 🟡/🔴 verdict - must name a **time-boxed spike** (days, not weeks) in "Next validation step." Committing to Phase 3b with an unspiked fatal technical risk is how projects die quietly in Phase 6.
- Build vs Buy default: **buy or rent everything that is not the core differentiator.** Every "Build" row must state why that component is differentiating. "We can build it cheaper" is almost always false once maintenance, security patching, and opportunity cost are counted.

---

### ARTIFACT: Tech Feasibility Report

```markdown
# Tech Feasibility Report - [Product Name]

> **Phase:** 2 - Discovery (Track A: Tech Feasibility)
> **Date:** [date]
> **Author:** [Tech Lead / PM]

---

## Executive Summary

[2-3 sentences: what we're building, overall feasibility verdict (Feasible / Feasible with risks / Not feasible), key rationale]

**Verdict:** 🟢 Feasible / 🟡 Feasible with risks / 🔴 Not feasible

---

## Core Technical Requirements

| Requirement | Category | Complexity | Notes |
|---|---|---|---|
| [e.g., Real-time messaging] | [Real-time / Storage / ML / Integration / Auth / ...] | High / Med / Low | [key constraint or note] |
| ... | | | |

---

## Technology Landscape

### Recommended Stack

| Layer | Technology | Rationale | Alternatives |
|---|---|---|---|
| Frontend | [e.g., Next.js] | [reason] | [alt1, alt2] |
| Backend | [e.g., Node.js + tRPC] | [reason] | [alt1, alt2] |
| Database | [e.g., PostgreSQL + Redis] | [reason] | [alt1, alt2] |
| Infrastructure | [e.g., Vercel + AWS] | [reason] | [alt1, alt2] |
| Auth | [e.g., Clerk] | [reason] | [alt1, alt2] |
| [Other] | | | |

### Justification

[2-3 sentences on why this stack fits the product requirements and team context]

---

## Integration Requirements

| Integration | Type | Complexity | Availability | Notes |
|---|---|---|---|---|
| [e.g., Stripe] | [Payment / API / Webhook / ...] | High / Med / Low | Official SDK / REST / ... | [key constraint] |
| ... | | | | |

---

## Technical Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [e.g., No SDK for X integration] | High / Med / Low | High / Med / Low | [mitigation approach] |
| ... | | | |

### Critical Blockers

[List any blockers that make the product infeasible as described. If none: "No critical blockers identified."]

---

## Compliance & Security Requirements

| Requirement | Applicability | Implementation Approach |
|---|---|---|
| GDPR | [Yes / No / Partial] | [e.g., Data residency in EU, consent management] |
| SOC 2 | [Yes / No / TBD] | [approach] |
| [Other] | | |

---

## Build vs Buy vs Partner

| Component | Decision | Rationale |
|---|---|---|
| [e.g., Authentication] | Buy (Clerk) | [reason - cost, time, security] |
| [e.g., Core matching algorithm] | Build | [reason - core differentiator] |
| [e.g., Analytics] | Buy (Mixpanel) | [reason] |

---

## Technology Disruption Check

[Honest answer to: could something existing or emerging make this build unnecessary or obsolete?]

| Threat | Assessment | Implication |
|---|---|---|
| **No-code / low-code delivers this** | [Could Webflow / Airtable / Bubble / an off-the-shelf SaaS cover the core need? If largely yes: custom build must justify itself - or recommend the cheaper path honestly, especially on commissioned builds] | |
| **AI commoditizes the core** | [Could a general AI assistant/agent do the job the product does? Timeline?] | |
| **Platform shift** | [Dependency on a platform/API that could change terms or deprecate?] | |

---

## Open Questions

| Question | Owner | Target Date |
|---|---|---|
| [What we don't know yet] | [Tech Lead / PM / ...] | [date] |
| ... | | |

---

## Confidence Level

**Overall confidence in technical assessment:** High / Medium / Low

**Why:** [brief rationale - what we know well, what remains uncertain]

**Next validation step:** [e.g., Build a proof-of-concept for X by [date]]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Tech Feasibility Report must cover:**
- [ ] Available technologies assessed for core requirements
- [ ] Compatibility with existing infrastructure confirmed or addressed
- [ ] Technology constraints documented (licensing, vendor lock-in, support lifecycle)
- [ ] Development and operational cost estimates provided
- [ ] Integration timeline and development effort estimated
- [ ] Team technology capacity assessed (internal vs. external reinforcement needed)
- [ ] Build vs. Buy vs. Partner decision made per component
- [ ] Critical blockers listed explicitly (or "none identified" stated)
- [ ] Confidence level stated with rationale

**SaaS / digital product specifics:**
- [ ] Multi-tenancy model addressed (data isolation strategy: silo, pool, bridge)
- [ ] API-first vs. monolith architecture decision addressed
- [ ] Cloud provider selection with cost model (compute, storage, egress)
- [ ] Scalability approach defined (horizontal scaling, stateless services)
- [ ] Security architecture baseline (auth, encryption at rest/in transit, secret management)

**AI product specifics (if applicable):**
- [ ] AI/ML approach assessed (third-party API vs. fine-tuned model vs. custom model)
- [ ] Third-party AI API dependencies (OpenAI, Anthropic, Google) - cost per call, rate limits, data privacy terms
- [ ] Training data availability and quality assessed
- [ ] Inference latency requirements vs. model capability tradeoff
- [ ] AI cost modeling (tokens/call × volume = monthly AI infra cost)
- [ ] EU AI Act applicability assessed (high-risk system classification)

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/tech-feasibility-report.md
```

---

## Handoff

**Čo si teraz má:** Tech Feasibility Report - vieš či je riešenie realizovateľné s daným stackom a kde sú technické riziká.

**Ďalší krok:** Dokonči ostatné Phase 2 tracky (`/pm-domain-analysis`, `/pm-market-analysis`, `/pm-personas` → `/jtbd-building`), potom konverguj cez `/pm-problem-validation`.

**Môžeš preskočiť ak:** Tech je triviálna alebo overená z predošlého produktu - Track A nepridáva hodnotu.
