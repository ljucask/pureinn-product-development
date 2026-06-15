# Product Roadmap - ProjectFlow

> **Phase created:** 3b - Commercial Definition
> **Current version:** v3
> **Last updated:** 2026-04-10
> **Next scheduled update:** After Phase 3 MVP completion (subscription billing shipped)

---

## Version History

| Version | Date | Phase | Key changes |
|---|---|---|---|
| v1 | 2025-09-15 | Phase 3b | Initial - strategic phases, vision, success criteria, "not building" list |
| v2 | 2025-10-20 | Phase 4 | WebSocket deferral confirmed (polling for MVP), billing timeline pushed to Phase 2, GDPR compliance added as Phase 1 prerequisite |
| v3 | 2026-04-10 | Phase 5 | Subscription billing initiative scoped; Feature Sets and Delivery Stripes added for Phase 2 (subscription billing MVP). Phase 3 updated with AI feature hypothesis staging. |

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
**Key hypothesis tested:** Self-serve billing will raise trial-to-paid conversion from ~12% (founder-assisted) to > 22% without any sales touch.

**Unlock condition:** Phase 1 exit — 20 paying customers, Day-30 retention > 40%.

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
**Key hypothesis tested:** AI-generated project health score and risk flags are acted on by team leads within 24 hours of surfacing, measurable via blocked task resolution rate.

**Unlock condition:** Phase 2 exit — self-serve billing live, MRR > $20,000, monthly churn < 2.5%.

**Success criteria:**
- [ ] AI project health score available in all active projects
- [ ] > 50% of team leads interact with AI health flag within 24 hours of trigger
- [ ] Mobile app (iOS) in App Store with Day-14 retention > 35%
- [ ] SSO (SAML/OIDC) shipped and used by first 2 enterprise customers
- [ ] First enterprise contract (> $2,000 MRR) signed

**Note on AI staging:** AI features are staged deliberately to match training data maturity. Phase 3 entry starts with rule-based health scoring (fast to ship, no training required); ML-based predictive risk is Phase 4 when we have sufficient task lifecycle data across 800+ WAP.

---

## What We Are Not Building (Now)

These are features and capabilities we have explicitly decided not to build in the current horizon. This is a strategic choice, not a backlog.

| Item | Why deferred | Reconsider when |
|---|---|---|
| Gantt chart view | Tested in Phase 1 with 5 users - zero sessions > 2 minutes. Invalidated by usage data. | Only if ICP expands to project managers (non-engineering) |
| Time tracking | Not in primary JTBD (block detection, not billing). Adds UI complexity for unvalidated demand. | Phase 3 if agency ICP validated |
| Resource management / capacity planning | Wrong scope for 5-15 person teams. Requires maturity in how teams use tasks first. | Phase 4 |
| Multi-currency | EUR-only covers 95% of current ICP (EU + UK). Cost/complexity not justified yet. | When first non-EUR customer represents > 10% of MRR |
| Freemium (free tier) | Trial converts well enough without permanent free tier. Free tier adds infrastructure cost before unit economics proven. | Phase 3 - if PLG conversion plateaus below 18% |
| Marketplace / API platform | No partner demand signal. Premature platform investment. | Phase 4 - after enterprise motion validates |
| Advanced BI / data export | Basic reporting sufficient for early adopter segment. | Phase 3 - when > 100 workspaces request export |

---

## Dependencies and Risks

| Dependency / Risk | Type | Impact | Mitigation |
|---|---|---|---|
| Stripe webhook reliability | External | Subscription state corruption if webhooks missed | All state changes driven by webhooks, not direct API response; idempotency on all handlers |
| GDPR compliance for billing data | Regulatory | Cannot store card data locally - Stripe vaults all card details | PCI DSS scope eliminated by Stripe; store only last 4 digits + brand for display |
| Founding team capacity (2 engineers) | Internal | Subscription billing initiative competes with product roadmap features | Dedicated Stripe 1 to 3 for billing; no feature work in parallel during billing build |
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

**If any of these change:** Phase 2 completion timeline and Phase 3 unlock criteria should be reviewed. If team capacity drops, Phase 2 must be re-scoped: Stripe integration is the priority; GitHub/Slack integrations defer to Phase 3.

---

## MVP Delivery View (v3)

> Added Phase 5 - April 2026 - after Subscription Billing Initiative MVP scope defined.

### Feature Sets (Phase 2 - Subscription Billing Initiative)

| Feature Set | Description | Feature Cards Status | Priority |
|---|---|---|---|
| FS-SUB-01: Subscription Core | Plan selection, checkout, payment processing, webhook state sync | In Build / Ready to Build | P1 |
| FS-SUB-02: Invoice & Compliance | Invoice generation, VAT fields, storage, download | In Spec | P1 |
| FS-SUB-03: Plan Lifecycle | Upgrade, downgrade, cancellation, admin tools | Backlog | P2 |

### Delivery Stripes (Phase 2 - Subscription Billing)

| Stripe | Domain focus | Features included | Feature Set(s) | Goal |
|---|---|---|---|---|
| Stripe 1 | Subscription Core | FEAT-SUB-001, FEAT-SUB-002, FEAT-SUB-003, FEAT-SUB-004 | FS-SUB-01 | Self-serve plan selection and payment processing end-to-end |
| Stripe 2 | Invoice & Compliance | FEAT-SUB-005, FEAT-SUB-006, FEAT-SUB-007 | FS-SUB-02 | Every payment attempt generates a VAT-compliant invoice |
| Stripe 3 | Plan Lifecycle | FEAT-SUB-008, FEAT-SUB-009, FEAT-SUB-010 | FS-SUB-03 | Upgrade, downgrade, cancel; admin subscription management |

**MVP completion:** Stripe 3 — when FEAT-SUB-010 (admin tools) reaches 6_Shipped

**Feature status at time of v3 update:**
- FEAT-SUB-001 (Subscribe to a plan): 6_Shipped
- FEAT-SUB-002 (Payment method management): 6_Shipped
- FEAT-SUB-003 (Cancel subscription): 3_Ready_to_Build
- FEAT-SUB-004 (Renewal + grace period): 2_In_Design
- FEAT-SUB-005 through FEAT-SUB-010: Backlog

### Post-MVP Roadmap

| Horizon | Focus | Feature Sets planned |
|---|---|---|
| Month 1-3 post-billing MVP | Slack integration, GitHub integration | FS-INT-01 (Slack), FS-INT-02 (GitHub) |
| Month 4-6 post-billing MVP | AI project health scoring (rule-based v1) | FS-AI-01 |
| Month 7-12 post-billing MVP | Mobile app (iOS), SSO, Enterprise onboarding | FS-MOB-01, FS-ENT-01 |
