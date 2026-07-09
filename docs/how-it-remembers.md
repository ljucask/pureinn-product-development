# The Files That Run The System

When you run Pureinn, two things happen in parallel. Skills produce artifacts - the documents, specs, and registers that capture your thinking. But underneath that, the framework is maintaining something different: a small set of files that are not outputs of any single skill, but the persistent infrastructure that makes the whole system work.

These are not documents you read and file away. They are files the framework writes, reads, and updates continuously - across sessions, across skills, across months of a project's life. They are what gives Pureinn its memory.

Most AI tools are stateless. Every session starts cold. You re-explain the product, re-establish context, re-decide what to work on. The moment you close the chat, everything you built together disappears. The next session, you start from zero again.

Pureinn works differently. From the moment you set up a project, a small set of files begins accumulating the things the framework needs to know: where you are, what playbook you are on, what has been completed, what your product is about, and where everything lives. Every skill that runs afterward reads these files first. The context is already there.

The result is a system that behaves less like a chat assistant and more like a knowledgeable colleague who has been on the project from day one - one who remembers what was decided, knows what phase you are in, and does not need to be caught up every time you sit down to work.

Four files make this possible.

---

## state.json - The project brain

Every Pureinn project carries a single file that knows where it stands. It tracks the current phase, which playbook is running (greenfield, feature implementation, or rebuild), which phases have been completed, and which live registers have been initialized. No manual bookkeeping - the orchestrator writes it, and every skill reads it before doing anything.

**The practical effect:** you can close a project for three weeks, come back, run `/pureinn`, and the framework picks up exactly where you left off. It does not ask you to re-explain your context. It already knows your stage, your history, and what the logical next move is.

**What makes this different:** most AI tools start cold every single session. You re-explain the product, re-establish context, re-decide what to work on. state.json is what turns a collection of independent skills into a system with memory. The orchestrator does not just route you - it routes you based on a real record of where this specific project actually is.

---

## pureinn-variables.md - Fill it once

The first time you set up a project, Pureinn creates a variables file and asks you to fill in two things: your Notion workspace URLs and your project slug. From that point on, every skill that pushes to Notion, creates a task, or links an artifact knows exactly where to send it - without you specifying it again.

It is the one place that connects your local workspace to your operational stack. Change a URL in one place and every downstream sync updates automatically.

**What makes this different:** in most setups, connecting an AI tool to your stack means per-session configuration - you paste URLs, re-authenticate, re-point the tool each time. pureinn-variables.md is a one-time wire. The framework is connected to your operational tools by default from the second project session onward. The thinking you do in Claude Code and the backlog your team works from in Notion stay in sync without you managing the bridge.

---

## assessment.md - Your product, captured on day one

When you first run `/pureinn` with a new idea, the orchestrator asks a short set of intake questions - what you are building, who it is for, how far along you are, what you already know. The answers do not disappear after the session. They are written into an assessment file that travels with the project.

Skills refer back to it. When you are six weeks in and running a domain modeling session, the framework still knows the original problem statement, the target customer, and the playbook rationale. Later work stays grounded in why you started - not just what has been built since.

**What makes this different:** most frameworks treat each skill as a standalone session. There is no thread connecting the persona work you did in week one to the feature spec you are writing in week six. assessment.md is that thread. It is why a skill running months later does not produce generic output - it produces output that is specific to this product, this problem, this customer. The further into a project you go, the more the assessment file earns its keep.

---

## The workspace itself - A structure every skill knows how to navigate

Most tools give you a blank canvas. Pureinn does the opposite. The first time you run it on a project, it creates a complete, opinionated folder tree - and that structure is not arbitrary. Every skill in the framework is written against it. Domain registers live in `domain/`. Phase artifacts are sorted under `artifacts/phase-X/`. Feature Cards go into `features/cards/`. Meeting notes land in `meetings/`. Onboarding briefs go into `team/onboarding/`.

**The result:** you never create a folder by hand, you never wonder where something lives, and you never spend ten minutes finding a document you know exists somewhere.

**What makes this different:** because every skill writes to and reads from the same predictable locations, skills can build on each other's outputs without any wiring from you. The persona file that `/pm-personas` writes is exactly where `/pm-feature-design` looks for it six weeks later. The business rules that `/pm-business-rules-library` creates are exactly where `/pm-feature-design` reads them when speccing a feature. The structure is not just organization - it is the integration layer that makes 47 separate skills behave like one connected system. No other AI product framework has this. Most give you documents. Pureinn gives you a workspace where everything talks to everything else automatically.

---

## A note on CLAUDE.md

The plugin ships with one more file that does not live in your project workspace - CLAUDE.md. It is the framework's internal rulebook: the universal standards that govern how every skill is written - how it asks questions, how it handles missing inputs, how it hands off to the next step, how agent mode behaves.

You never edit it and you never see it in your project folder. But its effect is present in every skill run. Every one of the 47 skills was written against these standards, and the key rules are baked directly into each skill so they reach you at runtime. The consistency you feel across the framework - the same question patterns, the same assumption surfacing, the same handoff format - comes from here.

Think of it as the contract between the framework's author and every skill in the system. It is what makes 47 independently-written skills feel like they were built by one very consistent team.
