---
name: pm-domain-analysis
description: Generate a Domain Analysis Report and Legal & Regulatory Requirements document from raw research inputs. Use in Phase 2 (Track B) after collecting industry and regulatory research.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: domain analysis, legal requirements, regulatory, compliance, industry analysis, Phase 2
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-market-analysis, pm-tech-feasibility, pm-problem-validation, pm-domain-model
---

# PM - Domain Analysis & Legal Requirements

## What this skill does

Takes raw research input (Perplexity deep research on domain, regulatory landscape, licensing, industry norms) and produces a structured Domain Analysis Report + Legal & Regulatory Requirements document.

This is a "bring your data" skill - Claude structures and formalizes. Legal analysis should be validated by a legal professional before acting on it.

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target markets and regulatory context are defined there

**Produces artifacts used by:**
- `pm-problem-validation` - domain analysis is Track B input
- `pm-business-rules-library` - domain constraints shape business rules and decision models
- `pm-privacy-requirements` - legal requirements feed directly into privacy planning

---

## Step 0: Current state check

Check for existing artifacts:
- Domain Analysis Report
- Legal & Regulatory Requirements

Also check: does a Project Charter exist? Cross-reference target markets and any regulatory constraints noted there.

Look for: regulatory requirements marked TBD, missing legal professional validation note, showstoppers not explicitly stated, EU AI Act assessment missing for AI products.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

First, ask:

Do you have domain or regulatory research to work with?

  A) Yes - I have Perplexity/ChatGPT research output or legal/domain expert notes to paste
  B) No - I'll share what I know about the domain and regulatory environment

---

### Path A - Research available

```
I need inputs for the Domain Analysis + Legal Requirements.

1. PRODUCT AND DOMAIN
   What does the product do? (1-2 sentences)
   What industry / domain does it operate in? (fintech, healthtech, real estate, marketplace, SaaS B2B...)
   Which countries / markets are you planning to launch in? (SK, CZ, EU, US...)

2. DOMAIN RESEARCH (paste raw output below)
   Perplexity / ChatGPT research on domain, industry, regulations:
   [paste here]

   Manual notes (PM, legal, domain expert):
   [paste here]

3. SPECIFIC AREAS
   Does the product handle personal data? (GDPR relevant)
   Does the product handle financial transactions or payments?
   Are there licensing requirements in this industry?
   Are there certifications / standards that must be met?

4. KNOWN CRITICAL ISSUES
   What are the biggest regulatory risks you already know about?
   Have any showstoppers been identified?
```

---

### Path B - No research (guided elicitation)

Guide the user through 2 rounds to reconstruct the domain and regulatory picture from what they know. Output marked as assumption-based, with explicit flags on areas requiring legal or domain expert validation.

**Group 1 of 2 - Domain and market**

Use AskUserQuestion tool for these two questions:

What industry or domain does this product operate in?

  A) B2B SaaS - general business software
  B) Fintech - payments, lending, investing, insurance
  C) Healthtech - medical, wellness, patient data
  D) Real estate, marketplace, or regulated professional services

Which markets are you launching in first?

  A) Slovakia / Czech Republic only
  B) Central and Eastern Europe (multiple CEE countries)
  C) EU-wide from launch
  D) US or global from launch

Then ask as plain text:

What does the product do in 1-2 sentences? What industry or domain does it operate in - describe it as a practitioner in that field would?

What are the main types of data the product handles? (personal data, financial data, health data, location data, minors' data)

After answers, confirm and proceed.

---

**Group 2 of 2 - Compliance and risks**

Use AskUserQuestion tool for these two questions:

Does the product handle financial transactions or payments?

  A) Yes - directly processes or holds funds (PSD2, payment service license relevant)
  B) Yes - initiates or facilitates payments but via licensed third party (Stripe, etc.)
  C) No - no financial transactions

Are there licensing or certification requirements in this industry?

  A) Yes - known specific license or certification required
  B) Possibly - not yet researched
  C) No - no known licensing requirements
  D) Depends on market - varies by country

Then ask as plain text:

What regulatory risks are you already aware of? (e.g., GDPR data processing obligations, industry-specific rules, age verification, content moderation requirements, AI Act implications if AI-powered)

Have any potential showstoppers been identified? (requirements that could block launch or significantly increase cost/complexity)

After answers, show complete summary. Flag explicitly which regulatory areas have zero research and must be validated with a lawyer or domain expert before launch.

Note at the top of every generated artifact: `> Assumption-based - built from founder knowledge, not legal or domain expert analysis. Items marked [NEEDS LEGAL REVIEW] must be verified with a qualified professional before treating as reliable for business decisions.`

---

## Step 2: Generate artifacts

Generate in English.

---

### ARTIFACT 1: Domain Analysis Report

```markdown
# Domain Analysis Report - [Product Name]

> **Phase:** 2 - Discovery (Track B: Field & Domain Discovery)
> **Date:** [date]
> **Author:** [PM / Domain Expert]

---

## Domain Overview

**Industry / Domain:** [e.g., Short-term rental marketplace]
**Target Markets:** [e.g., Slovakia, Czech Republic, EU]

[3-5 sentences describing the domain, its maturity, key dynamics, and how the product fits within it]

---

## Industry Structure

| Segment | Description | Size / Relevance |
|---|---|---|
| [e.g., Property managers] | [who they are, what they do] | [scale/relevance to product] |
| [e.g., Guests] | | |
| [e.g., Channel managers] | | |

---

## Key Domain Dynamics

| Dynamic | Description | Implication for Product |
|---|---|---|
| [e.g., Seasonality] | [how it works] | [what this means for us] |
| [e.g., Trust asymmetry] | | |
| [e.g., Price sensitivity] | | |

---

## Domain-Specific Constraints

| Constraint | Type | Impact | Notes |
|---|---|---|---|
| [e.g., Host identity verification required] | Regulatory / Business / Technical | High / Med / Low | [detail] |
| ... | | | |

---

## Established Industry Norms

[List norms / expectations that users in this domain take for granted. Violating these creates friction.]

- [Norm 1: e.g., Hosts expect real-time availability calendar sync]
- [Norm 2]
- [Norm 3]

---

## Domain Vocabulary

| Term | Definition | Context |
|---|---|---|
| [Domain-specific term] | [clear definition] | [when/how used] |
| ... | | |

---

## Open Domain Questions

| Question | Owner | Target Date |
|---|---|---|
| [What we need to learn about the domain] | | |
```

---

### ARTIFACT 2: Legal & Regulatory Requirements

```markdown
# Legal & Regulatory Requirements - [Product Name]

> **Phase:** 2 - Discovery (Track B: Field & Domain Discovery)
> **Date:** [date]
> **Status:** DRAFT - requires legal professional validation before acting

---

## Regulatory Landscape Overview

**Applicable jurisdictions:** [e.g., Slovakia, Czech Republic, EU]
**Core regulatory frameworks:** [e.g., GDPR, PSD2, local rental law, consumer protection]

[2-3 sentences summarizing the overall regulatory environment and its complexity]

---

## Regulatory Requirements

| Regulation / Law | Jurisdiction | Applicability | Requirement | Deadline / Trigger |
|---|---|---|---|---|
| GDPR | EU | High | Data processing consent, right to erasure, DPA if applicable | Before launch |
| [Local regulation] | [SK/CZ/...] | High / Med / Low | [what is required] | [when it applies] |
| ... | | | | |

---

## Licensing Requirements

| License / Permit | Jurisdiction | Required for | How to Obtain | Timeline |
|---|---|---|---|---|
| [e.g., Payment institution license] | EU | [if we process payments ourselves] | [via NBS / BaFin / ...] | [6-18 months] |
| [e.g., None - using payment provider] | - | [explanation] | - | - |

---

## Data & Privacy Requirements

| Requirement | Framework | Implementation Approach |
|---|---|---|
| User consent for data processing | GDPR Art. 6 | Consent management at onboarding |
| Right to data portability | GDPR Art. 20 | Export endpoint + user dashboard |
| Data retention limits | GDPR + local law | Automated deletion policy |
| [Other] | | |

**Data residency requirement:** [Yes - EU / No / TBD]

---

## Consumer Protection Requirements

| Requirement | Applicability | Notes |
|---|---|---|
| [e.g., Clear pricing before checkout] | High | [detail] |
| [e.g., Right to refund within 14 days] | High | [EU consumer protection law] |
| ... | | |

---

## Compliance Checklist (Pre-Launch)

- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] Legal review of Terms of Service and Privacy Policy
- [ ] DPA (Data Processing Agreement) with all data processors
- [ ] Cookie consent implementation
- [ ] [Other]

---

## Regulatory Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [e.g., Regulatory change mid-build] | Low / Med / High | High / Med / Low | [mitigation] |
| [e.g., Local licensing blocker] | | | |

### Showstoppers

[List any regulatory requirements that could prevent launch. If none: "No showstoppers identified."]

---

## Recommended Legal Actions

1. [e.g., Engage local legal counsel in Slovakia + Czech Republic by [date]]
2. [e.g., File for payment facilitator exemption under PSD2 - research timeline]
3. [e.g., Draft Privacy Policy based on this analysis for legal review]

---

## Disclaimer

This document is based on PM and desk research. It does not constitute legal advice. Validate all regulatory requirements with a qualified legal professional before launch.
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Domain Analysis Report must cover:**
- [ ] Industry / domain clearly defined with maturity stage
- [ ] Key domain dynamics identified (seasonality, trust asymmetry, network effects, etc.)
- [ ] Industry structure mapped (key players, segments, power dynamics)
- [ ] Domain-specific constraints documented (norms, expectations, standards)
- [ ] Domain vocabulary defined (terms users and industry take for granted)
- [ ] Open domain questions listed with owner

**Legal & Regulatory Requirements must cover:**
- [ ] Regulations affecting the domain per target jurisdiction
- [ ] Licenses or permits required to operate the platform - explicitly stated or ruled out
- [ ] Licenses or permits customers/users need to use the platform
- [ ] Enterprise certifications required for B2B sales (SOC 2, ISO 27001, etc.)
- [ ] Showstoppers listed explicitly (or "none identified")
- [ ] Recommended legal actions with timeline

**Digital / SaaS / AI specific:**
- [ ] GDPR applicability confirmed (personal data processing, consent, DPA requirements)
- [ ] Data residency requirements (EU data sovereignty, local storage laws)
- [ ] EU AI Act applicability assessed (high-risk AI system = stricter obligations)
- [ ] Industry-specific regulation: PSD2/open banking (fintech), HIPAA (healthtech), DSA (marketplace), eIDAS (identity)
- [ ] Consumer protection requirements (right to refund, price transparency, cancellation rights)
- [ ] Cookie consent and tracking regulation (ePrivacy Directive)

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/domain-analysis-report.md
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/legal-regulatory-requirements.md
```

---

## Handoff

**Čo si teraz má:** Domain Analysis + legal/regulatory requirements - poznáš pravidlá ihriska a compliance mantinely ešte pred dizajnom.

**Ďalší krok:** Dokonči Phase 2 tracky, potom `/pm-problem-validation` (konvergencia). Compliance zistenia neskôr použije `/pm-privacy-requirements` v Phase 4.

**Môžeš preskočiť ak:** Doména je dobre známa a bez regulačnej zložitosti.
