---
name: pm-tech-feasibility
description: Generate a Tech Feasibility Report from raw research inputs. Use in Phase 2 (Track A) after collecting Perplexity/ChatGPT deep research and Tech Lead analysis.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: tech feasibility, technology assessment, stack feasibility, technical risks, Phase 2 Track A
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-domain-analysis, pm-problem-validation, pm-domain-model
---

# PM - Tech Feasibility Report

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

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user all questions at once:

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

4. CRITICAL QUESTIONS
   What are the biggest technical risks / unknowns?
   What don't we know yet and need to validate?
```

---

## Step 2: Generate artifact

Generate in English.

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
pureinn-workspace/[project-slug]/artifacts/phase-2/tech-feasibility-report.md
```
