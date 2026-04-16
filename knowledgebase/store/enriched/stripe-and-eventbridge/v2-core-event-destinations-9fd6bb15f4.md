---
title: Event Destinations | Stripe API Reference | CloudRaven Enrichment
source_url: https://docs.stripe.com/api/v2/core/event-destinations
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:17.882577+00:00
kind: enriched-doc
tags: stripe, billing, payments, eventbridge, aws-events
---

# Event Destinations | Stripe API Reference | CloudRaven Enrichment

Source URL:

- https://docs.stripe.com/api/v2/core/event-destinations

Dependency:

- Stripe and EventBridge

Collection scope:

- Collect billing and AWS event-destination entry points.

What this page is useful for:

- Event Destinations | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 The Event Destination object v2 Create an Event Destination v2 Update an Event Destination v2 Retrieve an Event Destination v2 List Event Destinations v2 Delete an Event Destination v2 Disable an Event Destination v2 Enable an Event Destination v2 Event Destination event types v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Event Destinations v2 Ask about this section Copy for LLM View as Markdown Set up an event destination to receive events from Stripe across multiple destination types, including webhook endpoints and Amazon EventBridge .
- Event destinations support receiving thin events and snapshot events .
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / event_destinations POST / v2 / core / event_destinations / :id GET / v2 / core / event_destinations / :id GET / v2 / core / event_destinations DELETE / v2 / core / event_destinations / :id POST / v2 / core / event_destinations / :id / disable POST / v2 / core / event_destinations / :id / enable The Event Destination object v2 Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

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

- Extracted page: `knowledgebase/store/extracted/stripe-and-eventbridge/v2-core-event-destinations-9fd6bb15f4.md`
- Raw source: `knowledgebase/store/raw_html/stripe-and-eventbridge/v2-core-event-destinations-9fd6bb15f4.html`
