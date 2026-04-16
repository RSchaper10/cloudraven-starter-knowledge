---
title: Coupons | Stripe API Reference | CloudRaven Enrichment
source_url: https://docs.stripe.com/api/coupons
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:43.844326+00:00
kind: enriched-doc
tags: stripe, billing, payments, eventbridge, aws-events
---

# Coupons | Stripe API Reference | CloudRaven Enrichment

Source URL:

- https://docs.stripe.com/api/coupons

Dependency:

- Stripe and EventBridge

Collection scope:

- Collect billing and AWS event-destination entry points.

What this page is useful for:

- Coupons | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons The Coupon object Create a coupon Update a coupon Retrieve a coupon List all coupons Delete a coupon Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Coupons Ask about this section Copy for LLM View as Markdown A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer.
- Coupons may be applied to subscriptions , invoices , checkout sessions , quotes , and more.
- Coupons do not work with conventional one-off charges or payment intents .
- Yes No Endpoints POST / v1 / coupons POST / v1 / coupons / :id GET / v1 / coupons / :id GET / v1 / coupons DELETE / v1 / coupons / :id The Coupon object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

CloudRaven applicability:

- Use this material for payments, subscriptions, and event-driven back-office workflows.

Prototype-to-production review:

- Strong fit for monetization experiments and production-ready payment flows.
- Keep billing state and event processing rules aligned from the start.

CloudRaven example paths:

- Connect subscription events to AWS-native processing and entitlement updates.
- Prototype monetization flows with hosted checkout before deeper custom billing work.

Suggested retrieval tags:

- `stripe`
- `billing`
- `payments`
- `eventbridge`
- `aws-events`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/stripe-and-eventbridge/api-coupons-e75bc153e4.md`
- Raw source: `knowledgebase/store/raw_html/stripe-and-eventbridge/api-coupons-e75bc153e4.html`
