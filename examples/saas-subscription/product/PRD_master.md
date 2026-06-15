# Product Requirements Document - ProjectFlow

> **Phase:** 3b - Commercial Definition (Phase 3b exit artifact)
> **Date:** 2025-09-15
> **Version:** 1.0
> **Status:** Approved - frozen. New scope → Initiative PRD in initiatives/[slug]/prd.md
> **Owner:** Jana Kovac (PM)
> **Audience:** Internal team, seed investors

---

## Document Purpose

This PRD is the consolidation of Phase 2 (Discovery), Phase 3a (Validation), and Phase 3b (Commercial Definition) outputs for ProjectFlow. It captures the validated product-market fit hypothesis and serves as the stable reference for Phase 4+ execution.

It is NOT a feature spec. Feature specifications are generated per feature (JIT) in Phase 6 by `pm-feature-design` (Feature Card Sections 1-3).

New initiatives that extend the product (e.g., subscription billing, AI features) generate their own Initiative PRD and append to the domain registers. This document does not change.

---

## 1. Problem Statement

**The core problem:**
Small and mid-size tech teams (5-50 people) lose project visibility when they shift to remote or hybrid work. Existing tools either oversimplify (Trello-style boards with no dependency tracking) or overcomplicate (Jira-level configuration overhead that solo PMs cannot maintain). Teams end up context-switching across 3-4 tools and losing status information in Slack threads.

**Evidence basis:**
- 34 customer interviews conducted across 3 countries (SK, CZ, AT)
- 5 distinct JTBD identified (see JTBD Analysis artifact)
- Problem urgency: High — 28 of 34 interviewees rated "we lose track of what's blocking whom" as a Top 3 daily frustration
- 19 of 34 currently use 2+ tools in combination (Notion + Jira, Trello + Asana) indicating the market hasn't solved it

**Why this problem is not solved well today:**
Jira and Asana require a dedicated admin to configure and maintain — prohibitive for teams under 20. Notion and Linear solve documentation and lightweight tracking but lack cross-project dependency visibility. Trello has no concept of blocked tasks or project health scoring. No tool in the $15-50/seat range gives a team lead a single view of "what is blocked, why, and who owns the unblock."

---

## 2. Target Customer

### Primary Segment

**Segment:** Tech-forward SMB teams, 5-50 people
**Description:** Software product companies, agencies, and internal tech teams at SMBs. Primarily remote or hybrid. Team leads and PMs own tooling decisions. Budget authority: team lead or VP of Engineering with discretionary spend under $2,000/month does not require procurement approval.
**Size (SAM):** $480M (EU + UK market, $15-50/seat/month, 3-20M eligible seats)

**Primary Persona: Martin - Engineering Team Lead**
- Role: Engineering Team Lead, 8-15 direct reports, remote-first team
- Core goal: Ship predictably without spending 3+ hours/week chasing status in Slack
- Top pain: No single view of what is blocked — he finds out from customer escalations, not the tool
- Trigger to seek a new solution: New team member joins and onboarding reveals how broken the current setup is; or a project misses a deadline and post-mortem traces back to invisible blocking

### Early Adopter Profile

First 20 customers are Engineering Team Leads at product companies with 8-20 engineers, fully remote, frustrated with Jira complexity (have tried it and left, or never adopted it). Found through technical communities (Dev.to, Hacker News, LinkedIn Engineering groups). They will configure the tool themselves and tolerate rough edges in exchange for "it actually works without a 3-hour setup."

### Secondary Segment

**Product Managers at scale-ups (20-100 people):** Will become the primary growth segment in Phase 2 after core retention is proven with team leads. Longer evaluation cycle, require integrations (Slack, GitHub), willing to pay $25-40/seat.

---

## 3. Product Vision and Value Proposition

**Vision (3 years):**
ProjectFlow becomes the default project management layer for remote-first tech teams in Europe — the tool that replaces the Slack status-check, not just the Jira board.

**Value proposition:**
ProjectFlow gives engineering team leads a real-time view of what is blocked, who owns the unblock, and how it affects the delivery timeline — with zero configuration overhead. Set up in 20 minutes, used daily without a dedicated admin.

**For Martin (Engineering Team Lead):**
- Primary outcome: No more Friday status-check Slack threads — delivery state is visible without asking
- Pain eliminated: Blocked tasks stay invisible until they become deadline misses
- Differentiation: Dependency tracking and block detection in a tool that teams actually keep using (vs. Jira which reverts to Slack within 2 weeks of setup)

---

## 4. Market Context

**Market opportunity:**

| Metric | Value | Confidence |
|---|---|---|
| TAM | $8.4B | Med - PM software global estimate |
| SAM | $480M | Med - EU+UK SMB tech teams, $15-50/seat |
| SOM (Year 3) | $4.8M | Low - assumption: 0.5% SAM capture via PLG |
| Market CAGR | 14% | Med - Gartner 2024 PM software report |

**Why now:**
Remote-first became permanent for tech teams post-2022. The tools built for co-located Scrum (Jira, Azure DevOps) have accumulated configuration debt that SMBs cannot manage. There is a proven willingness to pay in this segment (Linear at $8-18/seat, Notion at $16/seat) — the gap is dependency-aware project tracking without the enterprise setup cost.

**Competitive position:**
Linear wins at developer-centric issue tracking but lacks project-level dependency view and non-technical user access. Asana wins at workflow but costs 3x our target price and requires admin setup. We win on: (1) dependency-aware tracking available at $0 configuration cost, (2) pricing 30-40% below Asana/Monday for equivalent team size, (3) onboarding under 20 minutes without consulting help.

**Competitive whitespace:**
No competitor in the $15-30/seat range combines cross-project dependency tracking with automatic block detection and a clean onboarding flow that a 10-person team can self-configure. This is our entry wedge.

---

## 5. Business Model

**Revenue model:** B2B SaaS subscription, per-seat pricing, monthly and annual billing

**Pricing:**

| Tier | Price | For whom |
|---|---|---|
| Starter | $12/seat/month | Teams up to 10 seats |
| Pro | $22/seat/month | Teams 11-50 seats, adds SSO + advanced reporting |
| Enterprise | Custom / quote | 50+ seats, custom SLA, dedicated onboarding |

**Unit economics targets:**

| Metric | Target |
|---|---|
| ARPU (Month 12) | $18/seat/month blended |
| Monthly churn | < 2.5% |
| LTV/CAC | > 4:1 |
| Gross margin | > 78% |
| Payback period | < 14 months |

**Acquisition model:** Product-led growth (PLG) as primary — free trial (14 days, full features), self-serve conversion. Founder-led sales for first 30 customers to validate ICP and pricing before PLG funnel is built.

---

## 6. Success Metrics

**North Star Metric:** Weekly Active Projects (WAP) — number of projects with at least one task updated in the last 7 days across all paid workspaces

**NSM Target (Month 12):** 800 WAP

**Phase 1 exit criteria (Month 6 post-launch):**
- [ ] 20 paying customers (Starter or Pro tier)
- [ ] Day-30 retention > 40% (task activity in paying workspaces)
- [ ] At least 3 customers qualify as reference customers (NPS > 50, willing to be named)
- [ ] Manual billing process is not blocking growth (team can handle up to 30 customers without automation)

**Phase 2 targets (Month 7-12):**
- [ ] MRR $28,000
- [ ] Monthly churn < 3%
- [ ] Conversion rate: trial → paid > 20%
- [ ] Self-serve billing operational (no manual invoicing)

**AARRR summary:**

| Stage | Key Metric | Target |
|---|---|---|
| Acquisition | Signups/month | 200 (Month 6) |
| Activation | Workspace with 3+ active tasks in first 7 days | > 45% |
| Retention | Day-30 project activity (WAP contribution) | > 40% |
| Revenue | MRR Month 12 | $28,000 |
| Referral | NPS from paying customers | > 40 |

---

## 7. Product Scope

### Business Capabilities (FDD+SDD input)

What the product must enable, written as business capabilities. This section is the primary input for entity extraction (Phase 4) and feature decomposition (Phase 5).

**AUTH - User Authentication and Access Control**
- The system must enable users to register with email and password.
- The system must enable users to log in and maintain authenticated sessions.
- The system must enable workspace owners to invite members by email.
- The system must enable workspace owners to assign roles (Admin, Member, Viewer) to workspace members.
- The system must enforce that only authenticated users can access workspace data.
- The system must enforce that Viewers cannot create or modify tasks or projects.

**WS - Workspace Management**
- The system must enable users to create a workspace with a name and slug.
- The system must enable workspace owners to configure workspace settings (name, timezone, notification preferences).
- The system must enable workspace owners to remove members from the workspace.
- The system must enforce that each workspace is isolated — members of Workspace A cannot access Workspace B data.
- The system must enable a user to belong to multiple workspaces and switch between them.

**PROJ - Project Management**
- The system must enable workspace members to create projects with a name, description, status, and target date.
- The system must enable workspace members to organize projects into groups or folders.
- The system must enable workspace members to update project status (Active, On Hold, Completed, Archived).
- The system must enable workspace members to view a project health indicator derived from blocked task count and target date proximity.
- The system must enable workspace members to archive and restore projects.

**TASK - Task Management**
- The system must enable workspace members to create tasks within a project with a title, description, assignee, priority, and due date.
- The system must enable workspace members to update task status (To Do, In Progress, Blocked, In Review, Done).
- The system must enable workspace members to create blocking relationships between tasks across projects.
- The system must enable the system to automatically detect and surface a task as Blocked when its blocker task is not Done.
- The system must enable workspace members to view all tasks blocked by a specific task (reverse dependency view).
- The system must enable workspace members to view a personal task list across all projects in the workspace.

**TEAM - Team Collaboration**
- The system must enable workspace members to add comments to tasks.
- The system must enable workspace members to mention other members in comments using @mention syntax.
- The system must enable the system to notify mentioned members of new @mentions.
- The system must enable workspace members to attach files to tasks (images, PDFs; max 25MB per file).
- The system must enable workspace members to view an activity log per task (status changes, comments, assignments).

**NOTIF - Notifications**
- The system must enable the system to send in-app notifications for: task assigned, task mentioned, task blocking status changed, task due date within 24 hours.
- The system must enable users to configure notification preferences per notification type (in-app / email / off).

> These sections are referenced by Feature Cards via `prd_ref` field (e.g., `prd_ref: "PRD_master#TASK"`) — section anchors above serve as link targets.

### In Scope (MVP)

1. AUTH - Full authentication and workspace role enforcement
2. WS - Workspace creation and member management
3. PROJ - Project management with health indicator
4. TASK - Task management with blocking relationships and automatic block detection
5. TEAM - Comments, @mentions, file attachments, activity log
6. NOTIF - In-app and email notifications (configurable)

### Out of Scope (MVP)

These items are explicitly excluded from the MVP. This is a strategic decision, not omission.

| Item | Reason | Reconsider when |
|---|---|---|
| Self-serve billing (subscription automation) | Manual invoicing handles first 30 customers; build automation only when it becomes the bottleneck | Phase 2 - when churn analysis shows billing friction is a top-3 reason |
| AI task suggestions | Unvalidated demand in early adopter segment; adds AI API cost before unit economics are proven | Phase 3 - after 200 WAP and retention data |
| Mobile native apps | Browser-based sufficient for early adopters (desk-first); mobile is table stakes for Phase 2 expansion | Phase 3 - after Web retention validated |
| SSO (SAML/OIDC) | Required for Enterprise only; no Enterprise customers in Phase 1 | Phase 2 - when first 3 Enterprise leads require it |
| Time tracking | Not in primary JTBD; adds UI complexity without solving block detection problem | Post-MVP if persona expands to agencies |
| Advanced analytics / dashboards | Basic task and project views are sufficient for early adopters | Phase 2 - after retention proves product stickiness |
| Resource management / capacity planning | Wrong scope for Phase 1; requires maturity in how teams use tasks | Phase 3 |
| Gantt chart view | Requested in interviews but not a forcing function for first purchase | Phase 2 - after core board/list views are stable |

### Deferred (Post-MVP)

| Item | Target phase | Trigger |
|---|---|---|
| Subscription billing automation | Phase 2 (Month 7-12) | Manual billing overhead exceeds 4h/week or > 30 customers |
| GitHub / Jira integration | Phase 2 | Requested by > 30% of active teams in NPS feedback |
| Slack integration | Phase 2 | When notification volume makes email-only insufficient |
| AI-powered project health prediction | Phase 3 | After 800 WAP and sufficient training data |
| Mobile app (iOS + Android) | Phase 3 | After Web DAU/WAU ratio > 60% for 90 days |

---

## 8. Constraints and Risks

### Technical Constraints

| Constraint | Impact | Source |
|---|---|---|
| Real-time sync requires WebSocket infrastructure | Stateful connections add hosting cost and complexity vs. REST-only | Tech Feasibility Report |
| File storage (attachments) requires object storage | S3 or equivalent; adds storage cost per workspace | Tech Feasibility Report |
| Blocking relationship graph traversal | Circular dependency detection required; graph algorithms needed for deep chains | Tech Feasibility Report |

**Technical feasibility verdict:** Feasible with risks
Key risk: Real-time collaboration at scale requires infrastructure investment (WebSocket scaling) that is premature for MVP. Mitigation: Polling-based sync for MVP (2-second refresh); switch to WebSockets in Phase 2 when team size warrants it.

### Regulatory Constraints

| Regulation | Jurisdiction | Requirement | Timeline |
|---|---|---|---|
| GDPR | EU | Data residency, DPA with sub-processors, right to erasure | Before launch (EU customers) |
| ePrivacy Directive | EU | Cookie consent, no tracking without explicit consent | Before launch |

**Regulatory showstoppers:** None identified.

**Compliance requirements to address before launch:**
- [ ] DPA (Data Processing Agreement) template for B2B customers
- [ ] Privacy Policy and Terms of Service reviewed by legal
- [ ] Cookie consent banner on marketing site and app
- [ ] Right to erasure workflow (workspace owner can delete all data)
- [ ] Sub-processor list published (AWS, Stripe for future billing, PostHog for analytics)

### Business Constraints

| Constraint | Impact |
|---|---|
| Founding team: 2 engineers + 1 PM, no dedicated sales/marketing | Limits parallel workstreams; Phase 1 must be founder-led, no marketing budget |
| Runway: 14 months at current burn | Phase 1 exit (20 paying customers, $4K MRR) must be achieved by Month 6 to extend runway via revenue |
| No enterprise sales motion in Phase 1 | Pricing and product must convert self-serve; no capacity for POCs or custom demos |

---

## 9. Open Questions and Assumptions

### Open Questions (not yet resolved)

| Question | Priority | Owner | Target date |
|---|---|---|---|
| Annual discount: 20% off vs. 2 months free framing? | High | Jana | Before billing build (Phase 2) |
| Free tier post-PLG: freemium model or time-limited trial only? | High | Jana | Month 3 - after first conversion data |
| Starter tier seat limit: hard cap at 10 or soft upsell prompt? | Med | Jana | Month 2 - after first 10 customers |
| Data residency: EU-only hosting required for first enterprise prospects? | Med | Legal | Month 4 |

### Critical Assumptions (that could invalidate the product)

| Assumption | Confidence | How to validate | By when |
|---|---|---|---|
| Teams of 5-15 will adopt a new tool without a 3-month change management process | Med | 5-user onboarding test with target persona | Week 2 post-launch |
| $12/seat/month is below willingness-to-pay threshold for Starter teams | Med | Pricing page A/B test + first 10 conversion conversations | Month 2 |
| Block detection (automatic Blocked status) is a daily-use feature, not a novelty | High | Day-14 and Day-30 retention of users who trigger block detection | Month 2 |
| PLG self-serve conversion achievable at > 15% without sales-assist | Low | Track trial → paid with no outreach for first 30 trials | Month 3 |
| CAC < $80 via inbound (content + community) | Low | First 500 signups, track by source | Month 4 |

---

## 10. Product Roadmap (summary)

> Full roadmap in product/product-roadmap-v3.md

**Phase 1 - Foundation (Months 1-6):** Core workspace, task management, and block detection shipped. 20 paying customers acquired through founder-led sales.

**Phase 2 - Revenue Automation + Retention (Months 7-14):** Self-serve subscription billing live (subscription-billing initiative). Integrations: GitHub, Slack. Advanced collaboration features. MRR $28K.

**Phase 3 - Intelligence + Scale (Months 15-24):** AI task health prediction. Mobile app. SSO for Enterprise expansion. First enterprise contract.

---

## 11. Artifact Input Map

This PRD synthesizes the following Phase 2, Phase 3a, and Phase 3b artifacts:

| Artifact | Phase | Status | Key contribution to PRD |
|---|---|---|---|
| Problem Validation Summary | 2 | Done | Problem statement, evidence (34 interviews), validated pains |
| Customer Segments + Personas | 2 | Done | Martin persona, early adopter profile, secondary segment |
| JTBD Analysis | 2 | Done | 5 JTBDs - forcing functions, switching triggers |
| Market Analysis (TAM/SAM/SOM, Competition, SWOT, Timing) | 2 | Done | Market size, whitespace, competitive position |
| Domain Analysis + Legal Requirements | 2 | Done | GDPR requirements, regulatory constraints |
| Tech Feasibility Report | 2 | Done | WebSocket risk, file storage, graph traversal |
| Design Thinking Synthesis | 3a | Done | Problem Statement (POV), HMW framing, solution direction |
| Hypothesis Register + Go/No-Go verdict | 3a | Done | 9 hypotheses validated, 2 invalidated (pivot: dropped Gantt from MVP) |
| Business Model Canvas | 3b | Done | Revenue model, pricing, channels, cost structure |
| KPIs (NSM, AARRR, OKRs) | 3b | Done | WAP as NSM, AARRR targets, Q1-Q2 OKRs |
| Business Case | 3b | Done | Financial projections, break-even Month 18 |
| Product Roadmap v1 | 3b | Done | 3 strategic phases, success criteria, "not building" list |

**Gaps noted:** JTBD Analysis complete but 2 JTBDs (time tracking, resource management) explicitly moved to out-of-scope after Go/No-Go verdict showed insufficient demand signal.

---

## 12. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2025-09-15 | Jana Kovac | Initial - end of Phase 3b. Frozen. |
