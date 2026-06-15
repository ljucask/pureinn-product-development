# Product Roadmap - ProjectFlow

> **Phase created:** 3 - Define & Validation
> **Current version:** v3
> **Last updated:** 2026-04-10
> **Next scheduled update:** After Phase 2 MVP completion (subscription billing shipped)

---

## Vision

**3-year vision:**
ProjectFlow becomes the default project management layer for remote-first tech teams in Europe - the tool that replaces the Slack status-check, not just the Jira board.

**12-month goal (from v3 update, April 2026):**
Self-serve subscription billing live by July 2026. MRR $28,000 by October 2026. Trial-to-paid conversion > 20% without sales touch.

**North Star Metric:** Weekly Active Projects (WAP) - number of projects with at least one task updated in the last 7 days across all paid workspaces
**NSM Target (Month 12 from launch):** 800 WAP

---

## Strategic Phases

### Phase 1: Foundation - Months 1-6 [COMPLETE]

**Goal:** Core workspace, task management, and block detection shipped. First paying customers acquired.
**Focus:** Prove that block detection is a daily-use feature that drives retention, not a one-time novelty.
**Key hypothesis:** Engineering team leads will adopt a new tool and keep using it daily if block visibility is instant and requires zero configuration.

**Success criteria (phase exit gate):**
- [x] 20 paying customers (Starter or Pro tier)
- [x] Day-30 retention > 40% (task activity in paying workspaces)
- [x] At least 3 reference customers (NPS > 50, willing to be named)
- [x] Manual billing process handling up to 30 customers without blocking growth

**What we did NOT build in this phase:**
- Self-serve billing (manual invoicing with 30-day net terms)
- Integrations (GitHub, Slack, Jira)
- Mobile app
- SSO

**Outcome:** Phase 1 exited Month 5. 23 paying customers. Day-30 retention 47%. 4 reference customers. Billing friction identified: 40% of churned trials cite no self-serve billing as the reason they did not convert.

---

### Phase 2: Revenue Automation + Retention - Months 7-14 [IN PROGRESS]

**Goal:** Self-serve subscription billing live. Billing friction eliminated as a conversion blocker. MRR $28,000.
**Focus:** Remove billing as a conversion barrier, stabilize retention, add Slack and GitHub integrations.
**Key hypothesis:** Self-serve billing will raise trial-to-paid conversion from ~12% (founder-assisted) to > 22% without any sales touch.

**Unlock condition:** Phase 1 exit - 20 paying customers, Day-30 retention > 40%.

**Success criteria:**
- [ ] Self-serve subscription billing live (Starter + Pro, monthly + annual)
- [ ] Trial-to-paid conversion > 20% without sales assist
- [ ] Involuntary churn (billing failure) < 2% monthly
- [ ] MRR $28,000 by Month 14
- [ ] Slack integration shipped and used by > 40% of active workspaces
- [ ] GitHub integration shipped and used by > 30% of active engineering teams

**What we are NOT doing in this phase:**
- Refunds (manual process via Stripe dashboard in v1)
- Multi-currency (EUR only in Phase 2)
- Mobile app
- AI features
- Enterprise self-serve billing (custom quote process remains)

---

### Phase 3: Intelligence + Scale - Months 15-24 [PLANNED]

**Goal:** AI-powered project health prediction. Mobile app. SSO for enterprise expansion. First enterprise contract.
**Focus:** Deepen retention with AI features, expand to mobile-first users, open the enterprise motion.
**Key hypothesis:** AI-generated project health score and risk flags are acted on by team leads within 24 hours of surfacing, measurable via blocked task resolution rate.

**Unlock condition:** Phase 2 exit - self-serve billing live, MRR > $20,000, monthly churn < 2.5%.

**Success criteria:**
- [ ] AI project health score available in all active projects
- [ ] > 50% of team leads interact with AI health flag within 24 hours of trigger
- [ ] Mobile app (iOS) in App Store with Day-14 retention > 35%
- [ ] SSO (SAML/OIDC) shipped and used by first 2 enterprise customers
- [ ] First enterprise contract (> $2,000 MRR) signed

**Note on AI staging:** Phase 3 entry starts with rule-based health scoring (fast to ship, no training data required). ML-based predictive risk is Phase 4 - after sufficient task lifecycle data accumulates across 800+ active WAP.

---

## What We Are Not Building (Now)

These are features and capabilities we have explicitly decided not to build in the current horizon. This is a strategic choice, not a backlog.

| Item | Why deferred | Reconsider when |
|---|---|---|
| Gantt chart view | Tested in Phase 1 with 5 users - zero sessions > 2 minutes. Invalidated by usage data. | Only if ICP expands to non-engineering project managers |
| Time tracking | Not in primary JTBD. Adds UI complexity for unvalidated demand. | Phase 3 if agency ICP validated |
| Resource management / capacity planning | Wrong scope for 5-15 person teams. Requires maturity in how teams use tasks first. | Phase 4 |
| Multi-currency | EUR-only covers 95% of current ICP (EU + UK). Cost/complexity not justified yet. | When first non-EUR customer represents > 10% of MRR |
| Freemium (free tier) | Trial converts well enough. Free tier adds infrastructure cost before unit economics proven. | Phase 3 - if PLG conversion plateaus below 18% |
| Marketplace / API platform | No partner demand signal. Premature platform investment. | Phase 4 - after enterprise motion validates |
| Advanced BI / data export | Basic reporting sufficient for early adopter segment. | Phase 3 - when > 100 workspaces request export |

---

## Dependencies and Risks

| Dependency / Risk | Type | Impact | Mitigation |
|---|---|---|---|
| Stripe webhook reliability | External | Subscription state corruption if webhooks missed | All state changes driven by webhooks, not direct API response; idempotency on all handlers |
| GDPR compliance for billing data | Regulatory | Cannot store card data locally | PCI DSS scope eliminated by Stripe; store only last 4 digits + brand for display |
| Founding team capacity (2 engineers) | Internal | Billing initiative competes with integration roadmap | Dedicated Delivery Stripes 1-3 for billing; no integration work in parallel |
| Annual billing discount framing | Product decision | 20% discount vs. 2 months free affects perceived value and upgrade rate | A/B test at checkout before Phase 2 launch |
| AI API cost ceiling | Technical | AI health scoring gross margin risk if token cost scales with WAP | Cost model reviewed before Phase 3 commit; cap tokens per project per week |

---

## Roadmap Assumptions

The timeline in this roadmap assumes:
- Engineering team of 2 remains stable through Phase 2. No hiring before MRR $15,000.
- Stripe integration covers EUR-only, card payments only, no multi-currency in Phase 2.
- No major Stripe API pricing changes in 2025-2026.
- EU regulatory environment for SaaS billing remains stable (no new VAT rules requiring custom tax logic beyond Stripe Tax).
- Phase 3 AI feature timing is contingent on having > 800 active WAP to generate meaningful training signals.

**If any of these change:** Phase 2 completion timeline and Phase 3 unlock criteria should be reviewed. If team capacity drops, Phase 2 must be re-scoped: billing is the priority; integrations defer to Phase 3.

---

## MVP Delivery View (v3)

> Added in Phase 5 - April 2026 - after subscription billing initiative MVP scope defined.

### Feature Sets (logical groupings)

| Feature Set | Description | Feature Cards Status | Priority |
|---|---|---|---|
| FS-01: Auth & Workspace | User registration, login, workspace creation, member management, roles | Shipped | P1 |
| FS-02: Projects & Tasks | Project management, task management, blocking relationships, block detection | Shipped | P1 |
| FS-03: Collaboration & Notifications | Comments, @mentions, file attachments, activity log, in-app and email notifications | Shipped | P1 |
| FS-04: Subscription Billing | Plan selection, checkout, renewal, invoice generation, plan lifecycle management | In Build / In Spec / Backlog | P1 |
| FS-05: Integrations | Slack notifications, GitHub issue sync | Backlog | P2 |

### Delivery Stripes (domain-focused parallel channels)

**Phase 1 stripes (complete):**

| Stripe | Domain focus | Features included | Feature Set(s) | Goal |
|---|---|---|---|---|
| Stripe A | Auth & Workspace | FEAT-USR-*, FEAT-WS-* (all shipped) | FS-01 | Authenticated workspaces with role enforcement live |
| Stripe B | Projects & Tasks | FEAT-PRJ-*, FEAT-TASK-* (all shipped) | FS-02 | Block detection working end-to-end across projects |
| Stripe C | Collaboration & Notifications | FEAT-TEAM-*, FEAT-NOTIF-* (all shipped) | FS-03 | Team activity visible without leaving the tool |

**Phase 2 stripes (active):**

| Stripe | Domain focus | Features included | Feature Set(s) | Goal |
|---|---|---|---|---|
| Stripe 1 | Subscription Core | FEAT-SUB-001, FEAT-SUB-002, FEAT-SUB-003, FEAT-SUB-004 | FS-04 | Self-serve plan selection and payment processing end-to-end |
| Stripe 2 | Invoice & Compliance | FEAT-SUB-005, FEAT-SUB-006, FEAT-SUB-007 | FS-04 | Every payment attempt generates a VAT-compliant, downloadable invoice |
| Stripe 3 | Plan Lifecycle | FEAT-SUB-008, FEAT-SUB-009, FEAT-SUB-010 | FS-04 | Upgrade, downgrade, cancel; admin subscription management |
| Stripe 4 | Integrations | FEAT-INT-001, FEAT-INT-002, FEAT-INT-003, FEAT-INT-004 | FS-05 | Slack and GitHub connected; notifications routed to where teams already work |

**MVP completion:** Stripe 3 - when FEAT-SUB-010 (admin tools) reaches 6_Shipped. Stripe 4 follows as Phase 2 close-out.

**Feature status at time of v3 update (April 2026):**
- FEAT-SUB-001 (Subscribe to a plan): 6_Shipped
- FEAT-SUB-002 (Payment method management): 6_Shipped
- FEAT-SUB-003 (Cancel subscription): 3_Ready_to_Build
- FEAT-SUB-004 (Renewal + grace period): 2_In_Design
- FEAT-SUB-005 through FEAT-SUB-010: Backlog
- FEAT-INT-001 through FEAT-INT-004: Backlog

### Post-MVP Roadmap

| Horizon | Focus | Feature Sets planned |
|---|---|---|
| Month 1-3 post-billing MVP | AI project health scoring (rule-based v1) | FS-06: AI Health |
| Month 4-6 post-billing MVP | Mobile app (iOS) | FS-07: Mobile |
| Month 7-12 post-billing MVP | SSO, Enterprise onboarding, enterprise contract motion | FS-08: Enterprise |

---

## Version History

| Version | Date | Phase | Key changes |
|---|---|---|---|
| v1 | 2025-09-15 | Phase 3b | Initial - strategic phases, vision, success criteria, "not building" list |
| v2 | 2025-10-20 | Phase 4 | WebSocket deferral confirmed (polling for MVP), billing timeline pushed to Phase 2, GDPR compliance added as Phase 1 prerequisite |
| v3 | 2026-04-10 | Phase 5 | Full product Feature Sets and Delivery Stripes added. Phase 1 marked complete with outcome data. Phase 3 AI staging rationale added. |
