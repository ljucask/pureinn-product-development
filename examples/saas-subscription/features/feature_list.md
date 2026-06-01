# FDD Feature List - ProjectFlow SaaS
# Live Register 4 of 4 - FDD+SDD Framework

> **Product:** ProjectFlow SaaS
> **Version:** 1.2
> **Last updated:** 2026-06-01
> **Maintained by:** pm-features-list (init) + pm-features-list FI Append (new initiatives)

---

> **How to read this register:**
> - FEAT-[DOMAIN]-NNN: domain code matches entity domain in entities.md
> - Status: 1_Walkthrough through 6_Promoted_to_Build (Feature Card frontmatter)
> - Stripe: which Delivery Stripe this feature is assigned to
> - KANO: Must-be / Performance / Delighter / Indifferent
> - V×C: Quick Win / Big Bet / Fill-in / Time Waster

---

> **Note:** This example shows the Subscription Billing domain appended to an existing feature list.
> Original features (FEAT-USR-*, FEAT-WS-*, FEAT-PRJ-*) from the core product are above this section.

---

## Subscription Billing (FEAT-SUB-*)

*Initiative: subscription-billing | Domain code: SUB | Stripe: Subscription Billing*

### FEAT-SUB-001: Subscribe to a plan
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 1)
**Status:** 6_Promoted_to_Build
**Business rules:** BR-SUB-001, BR-PAY-001, BR-INV-001, BR-REG-001, BR-REG-002
**Feature flag:** `billing-subscription-create`
**Notes:** Entry point to the entire billing domain. Must be the first feature built.

---

### FEAT-SUB-002: View subscription details
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 1)
**Status:** 6_Promoted_to_Build
**Business rules:** BR-SUB-002 (grace period display), BR-SUB-003 (cancels_at display)
**Feature flag:** `billing-subscription-view`
**Notes:** Shows current plan, billing cycle, next renewal date, payment method, cancellation status.

---

### FEAT-SUB-003: Cancel subscription
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 1)
**Status:** 3_Design_Inspection_Passed
**Business rules:** BR-SUB-003, BR-SUB-004
**Feature flag:** `billing-subscription-cancel`
**Notes:** Cancellation at period_end. Includes reactivation path (BR-SUB-004).

---

### FEAT-SUB-004: Update payment method
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 1)
**Status:** 1_Walkthrough
**Business rules:** BR-PAY-002, BR-REG-002
**Feature flag:** `billing-payment-method-update`
**Notes:** Card-only in v1. Must prevent removal of last active card while subscription active.

---

### FEAT-SUB-005: Process subscription renewal (automated)
**Actor:** System (scheduler)
**KANO:** Must-be
**V×C:** Big Bet
**Delivery Stripe:** Subscription Billing (Stripe 2)
**Status:** 1_Walkthrough
**Business rules:** BR-SUB-001, BR-SUB-002, BR-PAY-001
**Feature flag:** `billing-subscription-renewal`
**Notes:** Scheduled job runs 3 days before period_end. Handles retry logic and grace period transition. Complex - design carefully.

---

### FEAT-SUB-006: Upgrade subscription plan
**Actor:** Workspace Admin
**KANO:** Performance
**V×C:** Big Bet
**Delivery Stripe:** Subscription Billing (Stripe 2)
**Status:** 1_Walkthrough
**Business rules:** BR-PAY-001, BR-INV-001
**Feature flag:** `billing-plan-upgrade`
**Notes:** Immediate effect with prorated billing. Proration calculation: (remaining_days / total_days) * price_difference.

---

### FEAT-SUB-007: View invoice history
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 2)
**Status:** 1_Walkthrough
**Business rules:** BR-INV-001, BR-REG-001
**Feature flag:** `billing-invoice-history`
**Notes:** List view with status, date, amount. Link to download. Must show Void invoices too.

---

### FEAT-SUB-008: Download invoice PDF
**Actor:** Workspace Admin
**KANO:** Must-be
**V×C:** Quick Win
**Delivery Stripe:** Subscription Billing (Stripe 2)
**Status:** 1_Walkthrough
**Business rules:** BR-INV-001, BR-REG-001
**Feature flag:** `billing-invoice-download`
**Notes:** PDF must include all required VAT fields. Generated server-side, not in browser.

---

### FEAT-SUB-009: Reactivate cancelled subscription
**Actor:** Workspace Admin
**KANO:** Performance
**V×C:** Fill-in
**Delivery Stripe:** Subscription Billing (Stripe 3)
**Status:** 1_Walkthrough
**Business rules:** BR-SUB-001, BR-PAY-001
**Feature flag:** `billing-subscription-reactivate`
**Notes:** Creates new subscription Draft from Cancelled state. New payment required.

---

### FEAT-SUB-010: Admin - manage customer subscription
**Actor:** Internal Admin
**KANO:** Must-be
**V×C:** Fill-in
**Delivery Stripe:** Subscription Billing (Stripe 3)
**Status:** 1_Walkthrough
**Business rules:** BR-SUB-001, BR-SUB-003, BR-INV-001
**Feature flag:** `billing-admin-manage`
**Notes:** Internal tool for support team. Manual plan changes, grace period extension. Audit log required (BR-REG-003 TBD).

---

## Dependency Map

| Feature | Depends on | Blocks | Type |
|---|---|---|---|
| FEAT-SUB-001 | - (no dependency on other SUB features) | All other FEAT-SUB-* | Hard - entities and rules established here |
| FEAT-SUB-002 | FEAT-SUB-001 | - | Hard - cannot view what doesn't exist |
| FEAT-SUB-003 | FEAT-SUB-001 | - | Hard - cannot cancel non-existent subscription |
| FEAT-SUB-004 | FEAT-SUB-001 | FEAT-SUB-005 | Hard - renewal needs a valid payment method |
| FEAT-SUB-005 | FEAT-SUB-001, FEAT-SUB-004 | - | Hard - renewal needs subscription + payment method |
| FEAT-SUB-006 | FEAT-SUB-001, FEAT-SUB-007 | - | Hard - upgrade generates invoice |
| FEAT-SUB-007 | FEAT-SUB-001 | FEAT-SUB-008 | Hard - download requires list |
| FEAT-SUB-008 | FEAT-SUB-007 | - | Hard - needs invoice record to generate PDF |
| FEAT-SUB-009 | FEAT-SUB-001 | - | Soft - can stub for testing |
| FEAT-SUB-010 | FEAT-SUB-001 | - | Soft - internal tool, can be deferred |

---

## Delivery Stripe Overview

| Stripe | Domain | Features | Priority |
|---|---|---|---|
| Subscription Billing - Stripe 1 | Core subscription flow | FEAT-SUB-001, 002, 003, 004 | P1 - blocks all other billing features |
| Subscription Billing - Stripe 2 | Renewal + plan management + invoices | FEAT-SUB-005, 006, 007, 008 | P2 - after Stripe 1 complete |
| Subscription Billing - Stripe 3 | Admin + edge cases | FEAT-SUB-009, 010 | P3 - post-launch |

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | 2026-05-01 | Initial feature list - FEAT-USR-*, FEAT-WS-*, FEAT-PRJ-* | Phase 5 init |
| 1.1 | 2026-05-20 | FEAT-USR-001, FEAT-WS-003 promoted | pm-stripe |
| 1.2 | 2026-06-01 | FEAT-SUB-001..010 appended | subscription-billing initiative FI Append |
