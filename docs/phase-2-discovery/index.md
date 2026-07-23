# Phase 2 - Discovery

Four parallel research tracks that converge into a Problem Validation Summary. The goal is to understand the market, technology, domain, and customer deeply enough to validate (or invalidate) the problem worth solving.

**Duration:** 1-3 weeks · **Gate type:** Soft gate (gaps acknowledged, can proceed) · **Playbooks:** Greenfield

---

## How to read this page

The four tracks run in parallel - there's no forced order between them, only within each. Per-track blocks below give the trigger, what to bring, and what you get. **"Bring your data" rule applies everywhere here:** Claude structures and formalizes what you bring - it does not hallucinate market data or interview insights. Every skill degrades gracefully if you have no data (marks output `[ASSUMED - validate with real users]` instead of blocking).

---

## When to enter this phase

Enter Phase 2 after Phase 1 (or directly with `/pureinn discover`). Phase 3a can start in parallel with late Phase 2, once the Problem Validation Summary exists.

**What you need before entering:** Phase 1 artifacts (Project Charter, basic scope), and external research material per track - or willingness to proceed assumption-based.

---

## Track A - Technology

- **When to run / skip:** run for every product - technical feasibility is never assumed. Never skip.
- **Gather first:** research on stack options, third-party APIs, technical constraints (Perplexity or your Tech Lead).
- **Command:** `/pm-tech-feasibility`
- **What you get:** Tech Feasibility Report - stack viability, key constraints, risks.
- **What it does NOT give you:** a final architecture decision - that's `/common-ground` later, closer to build.
- **Done when:** the report names a viable stack path and its risks, not just "yes it's feasible."

---

## Track B - Domain

- **When to run / skip:** run for every product with real domain/regulatory complexity. Skip only if the domain is trivial (no regulation, no specialized business logic).
- **Gather first:** domain and regulatory research (Perplexity or domain expert).
- **Command:** `/pm-domain-analysis`
- **What you get:** Domain Analysis + Legal Requirements.
- **What it does NOT give you:** the entity model itself - that's Phase 4 (`pm-entity-registry`). This is the research that informs it, not the register.
- **Done when:** regulatory obligations relevant to the product are named, not just "check with legal later."

---

## Track C - Market

- **When to run / skip:** run for every product. Never skip - even a rough TAM/SAM/SOM beats none.
- **Gather first:** competitor research - or use Path C (AI-powered web research via Perplexity/OpenAI, requires `OPENAI_API_KEY` in `pureinn-variables.md`) if you have no prep.
- **Command:** `/pm-market-analysis`
- **What you get:** Market Size (TAM/SAM/SOM), Competitor Analysis, SWOT.
- **What it does NOT give you:** a pricing decision - that comes later, in Phase 3b business model work.
- **Done when:** TAM/SAM/SOM has real numbers or explicit `[ASSUMED]` markers, not blanks.

---

## Track D - Customer

- **When to run / skip:** run for every product. Never skip - this is the track most other decisions depend on.
- **Gather first:** ≥10 customer interviews for `pm-personas` (or proceed assumption-based). `jtbd-building` requires `pm-personas` to exist first - do not run it before.
- **Commands:**
```bash
/pm-personas       # first
/jtbd-building      # after personas exist
```
- **What you get:** Customer Segments, Personas, Early Adopters Profile (from `pm-personas`); JTBD Analysis + Forces Diagram per persona (from `jtbd-building`).
- **What it does NOT give you:** a validated problem - JTBD tells you the job, not whether the market will pay to have it done. That's Phase 3a.
- **Done when:** at least one persona has a JTBD Forces Diagram with real (or clearly assumed) forces.

---

## Convergence - Problem Validation Summary

- **When to run / skip:** run only after all four tracks (A-D) are complete. Do not run early - it synthesizes them, it doesn't stand alone.
- **Gather first:** Tracks A-D outputs.
- **Command:** `/pm-problem-validation`
- **What you get:** the Phase 2 exit artifact - synthesizes all four tracks into a single validated (or flagged-as-unvalidated) problem statement.
- **What it does NOT give you:** a GO/NO-GO verdict - that requires real-world experiments, which is Phase 3a.
- **Done when:** the Summary exists and Phase 3a can start from it.

---

## Client discovery layer (commissioned builds)

When a client, sponsor, or exec commissioned the work, discovery gains a plane above the end users - the commissioner's business, trigger, benefit, budget, constraints, references. Same four tracks, added tooling:

- **When to run / skip:** run only for commissioned builds (someone other than you is the customer of this discovery). Skip for your own product.

| Step | Skill / Material | Output |
|---|---|---|
| Before each session | [pm-discovery-interview](pm-discovery-interview.md) | Session agenda targeting the biggest remaining gaps |
| After each session | `/pm-meeting` (Client Discovery type) | Structured findings - references classified directive/hypothesis, constraints, `[CANDIDATE-BR]` exceptions |
| Continuously | [pm-discovery-report](pm-discovery-report.md) | Client-facing "what we heard, what we recommend" - incremental, re-runnable |

Client claims about their own users enter Track D tagged `[CLIENT-ASSERTED]` - input, not evidence. When the mandate is already given (the client decided to build), Phase 3a can be skipped: the Discovery Report feeds `/pm-scope-brief` directly (Phase 3b alternative to the PRD).

---

## What you exit with

- **Tech Feasibility Report** - stack viability, key constraints, risks
- **Domain Analysis** - domain structure, regulatory requirements, legal landscape
- **Market Analysis** - TAM/SAM/SOM, competitor landscape, SWOT
- **Customer Segments + Personas** - who the customer is, what they need
- **JTBD Analysis** - Jobs-to-be-Done + Forces Diagram per persona
- **Problem Validation Summary** - synthesizes all tracks; Phase 2 exit artifact

---

## Phase exit gate

Run `/pureinn` after completing Phase 2 to check the exit gate.

**Gate type: Soft.** The engine checks all four tracks and the Problem Validation Summary. You can acknowledge gaps and proceed, or loop back to strengthen weak tracks.
