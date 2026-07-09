# About the Framework

## What Pureinn is

Pureinn is a structured product development framework that runs inside Claude Code. It covers the full product lifecycle - from the first raw idea through domain modeling, prioritization, and delivery - as a set of 47 connected skills you invoke when you need them, not as a waterfall you follow in sequence.

The goal is simple: close the gap between what a product team knows, what they decide, and what actually gets built.

---

## Why it exists

Most product processes fail the same way. Not because teams lack talent or effort - but because the knowledge is scattered.

Validated insights from customer interviews that never made it into the spec. Business rules buried in Slack threads. Feature lists without any prioritization logic. A PRD nobody reads after week two. A new developer who spends three days asking basic questions about how the system works.

The waste is not in the doing. It is in the re-doing. Re-litigating decisions that were already made. Re-explaining context that was never written down. Building features nobody validated.

Pureinn was built to prevent that. Every skill in the framework produces an artifact that the next skill can read. Decisions are recorded. Context travels forward. The team stays in sync without meetings to compensate for missing documentation.

---

## What it does

Pureinn structures the work that happens before, around, and between engineering sprints:

- **Discovery and validation** - customer research, market analysis, hypothesis testing with Go/No-Go gates before committing to build
- **Domain modeling** - entities, state machines, business rules, and decision tables as living registers the codebase references
- **Feature planning** - KANO classification, Value vs. Complexity scoring, dependency mapping, MVP scope, Delivery Stripes
- **JIT feature design** - per-feature functional specs written just before build, not months ahead when everything is still uncertain
- **Cross-phase utilities** - prototyping, audit, stress-testing, root cause diagnosis, meeting notes, onboarding briefs

All of it connects. A persona from Discovery feeds a JTBD analysis. JTBD feeds hypothesis testing. Validated hypotheses feed the PRD. The PRD's Business Capabilities feed entity extraction. Entities feed feature derivation. Features feed the JIT spec. Every step has a known input and a known output.

---

## Who it is for

### Solo builders

You are moving fast. You do not have a team to ask, and you cannot afford to build the wrong thing. Pureinn gives you the structure to think clearly without slowing down.

The framework is designed to skip what does not apply. No stakeholder map if you have no stakeholders. No team roster if it is just you. What remains is the work that matters: validate the problem before you build, model the domain before you write code, know what is in scope and what is deliberately out.

You get a framework-level process without the overhead of running one. The skills are invoked in conversation - no setup, no configuration, no tool switching.

---

### Small product teams

The biggest problem in a small team is shared context. Everyone knows different pieces. The developer knows the code. The founder knows the customer. The designer knows the flows. Nobody has the full picture, and the handoffs between them leak.

Pureinn creates a shared workspace where decisions are written down and artifacts reference each other. When a developer starts a feature, they read the spec that was written just before they picked it up - not a six-month-old document. When a new person joins, they get a role-specific onboarding brief generated from what already exists.

The framework does not require a dedicated PM. It runs in Claude Code, where engineers already work.

---

### Agencies and consulting teams

Client work has a repeatable problem: every project starts from scratch. The intake is ad hoc. The handoff to developers is informal. What the client approved in week two is forgotten by week eight.

Pureinn gives agencies a repeatable delivery structure. The same discovery → validation → domain → planning → build sequence, applied consistently across clients. Artifacts are organized, versioned with the code, and readable by the client if needed.

The Rebuild playbook specifically addresses the most common agency scenario: an existing product with scattered documentation that needs to be brought under control before new development can begin. Reconcile the codebase against the old docs, produce clean registers, and start delivering again.

---

## The experience behind it

Pureinn was built by someone who has spent over a decade working across technology, business, and product - in labs, early-stage startups, small teams, and larger corporate environments.

That range of contexts is the point. It is not a framework designed in theory. It is built from watching the same problems appear in different forms: a corporate team drowning in documentation nobody uses; a startup team building on gut feeling with no validation; an agency re-explaining a client's own domain back to them every six months because nothing was written down.

The common thread across those environments was not the tools or the methodologies. It was the absence of a consistent structure that could scale down for a solo builder and scale up for a team without changing its core logic.

Product management in practice is not about running ceremonies. It is about making decisions with the right information at the right time, recording them so they survive personnel changes, and ensuring that what gets built reflects what was validated. Pureinn is the operational answer to that.

Every design decision in the framework is made with one question in mind: does this move the product forward, or does it just create process? Speed of impact and real value delivery are the constraints - not completeness for its own sake.

- [Connect with the author](https://linkedin.com/in/YOUR_LINKEDIN) - LinkedIn
- [Pureinn on LinkedIn](https://linkedin.com/company/YOUR_PUREINN_URL)

---

## What it is not

Pureinn is not a project management tool. It does not replace Jira, Linear, or Notion. It integrates with them.

It is not a design system or a coding framework. It operates at the layer above: the thinking, decisions, and specifications that inform the design and the code.

It is not a rigid methodology. The skill sequence is a default path, not a mandate. Every skill can be re-run with new information. Discovery can feed back into validation. A feature that surfaces a missing business rule triggers the rule helper mid-sprint. The framework adapts to where the project actually is.

---

## How to get started

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@pureinn-product-development
```

Select user scope for global availability across all projects.

Then start with `/pureinn` - the orchestrator reads your context, identifies where you are, and routes you to the right entry point.
