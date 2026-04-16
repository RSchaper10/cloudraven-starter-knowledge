---
title: Customer Session | Stripe API Reference
source_url: https://docs.stripe.com/api/customer_sessions
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:12.857812+00:00
kind: extracted-doc
---

# Customer Session | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/customer_sessions

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:12.857812+00:00

Direct links in scope:

- https://docs.stripe.com/api
- https://docs.stripe.com/api/authentication
- https://docs.stripe.com/api/errors
- https://docs.stripe.com/api/expanding_objects
- https://docs.stripe.com/api/idempotent_requests
- https://docs.stripe.com/api/include_dependent_response_values
- https://docs.stripe.com/api/metadata
- https://docs.stripe.com/api/pagination
- https://docs.stripe.com/api/request_ids
- https://docs.stripe.com/api/connected-accounts
- https://docs.stripe.com/api/versioning
- https://docs.stripe.com/api/v2/core/accounts
- https://docs.stripe.com/api/v2/core/account-links
- https://docs.stripe.com/api/v2/core/account-tokens
- https://docs.stripe.com/api/balance
- https://docs.stripe.com/api/balance_transactions
- https://docs.stripe.com/api/charges
- https://docs.stripe.com/api/customers
- https://docs.stripe.com/api/customer_sessions
- https://docs.stripe.com/api/customer_sessions/object

Captured summary:

- Customer Session | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session The Customer Session object Create a Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Customer Session Ask about this section Copy for LLM View as Markdown A Customer Session allows you to grant Stripe’s frontend SDKs (like Stripe.js) client-side access control over a Customer.
- Related guides: Customer Session with the Payment Element , Customer Session with the Pricing Table , Customer Session with the Buy Button .
- Yes No Endpoints POST / v1 / customer_sessions The Customer Session object Ask about this section Copy for LLM View as Markdown Attributes client _ secret string The client secret of this Customer Session.
- Used on the client to set up secure access to the given customer .
- The client secret can be used to provide access to customer from your frontend.

Extracted text:

Customer Session | Stripe API Reference

Find anything

/

Ask AI

Introduction

Authentication

Errors

Expanding Responses

Idempotent requests

Include-dependent response values (API v2)

Metadata

Pagination

Request IDs

Connected Accounts

Versioning

Core Resources

Accounts

v2

Account Links

v2

Account Tokens

v2

Balance

Balance Transactions

Charges

Customers

Customer Session

The Customer Session object

Create a Customer Session

Disputes

Events

Events

v2

Event Destinations

v2

Files

File Links

Mandates

Payment Intents

Persons

v2

Person Tokens

v2

Setup Intents

Setup Attempts

Payouts

Refunds

Confirmation Token

Tokens

Payment Methods

Payment Methods

Payment Method Configurations

Payment Method Domains

Bank Accounts

Cash Balance

Cash Balance Transaction

Cards

Sources

Products

Products

Prices

Coupons

Promotion Code

Discounts

Tax Code

Tax Rate

Shipping Rates

Checkout

Checkout Sessions

Payment Links

Payment Link

Billing

Alerts

Credit Balance Summary

Credit Balance Transaction

Credit Grant

Credit Note

Customer Balance Transaction

Customer Portal Configuration

Customer Portal Session

Invoices

Invoice Items

Invoice Line Item

Invoice Payment

Invoice Rendering Templates

Meters

Meter Events

Meter Event Adjustment

Meter Event Adjustments

v2

Meter Event Streams

v2

Meter Event Summary

Meter Events

v2

Plans

Quote

Subscriptions

Subscription Items

Subscription Schedule

Tax IDs

Test Clocks

Capital

Financing Offer

Financing Summary

Connect

Accounts

Login Links

Account Links

Account Session

Application Fees

Application Fee Refunds

Capabilities

Country Specs

Balance Settings

External Bank Accounts

External Account Cards

Person

Top-ups

Transfers

Transfer Reversals

Secrets

Reserves

Fraud

Issuing

Terminal

Treasury

Payment Records

Account Evaluation

Entitlements

Sigma

Reporting

Financial Connections

Tax

Identity

Crypto

Climate

Forwarding

Privacy

Webhooks

Customer Session

Ask about this section

Copy for LLM

View as Markdown

A Customer Session allows you to grant Stripe’s frontend SDKs (like Stripe.js) client-side access

control over a Customer.

Related guides:

Customer Session with the Payment Element

,

Customer Session with the Pricing Table

,

Customer Session with the Buy Button

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

customer_sessions

The Customer Session object

Ask about this section

Copy for LLM

View as Markdown

Attributes

client

_

secret

string

The client secret of this Customer Session. Used on the client to set up secure access to the given

customer

.

The client secret can be used to provide access to

customer

from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.

components

object

This hash defines which component is enabled and the features it supports.

Show child attributes

customer

string

Expandable

The Customer the Customer Session was created for.

expires

_

at

timestamp

The timestamp at which this Customer Session will expire.

More attributes

Expand all

object

string

created

timestamp

customer

_

account

nullable

string

livemode

boolean

The Customer Session object

{

"

object

"

:

"

customer_session

"

,

"

client_secret

"

:

"

_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje

"

,

"

components

"

:

{

"

buy_button

"

:

{

"

enabled

"

:

false

},

"

pricing_table

"

:

{

"

enabled

"

:

true

}

},

"

customer

"

:

"

cus_PO34b57IOUb83c

"

,

"

expires_at

"

:

1684790027

,

"

livemode

"

:

false

}

Create a Customer Session

Ask about this section

Copy for LLM

View as Markdown

Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.

Parameters

components

object

Required

Configuration for each component. At least 1 component must be enabled.

Show child parameters

customer

string

The ID of an existing customer for which to create the Customer Session.

More parameters

Expand all

customer

_

account

string

Returns

Returns a Customer Session object.

POST

/

v1

/

customer_sessions

curl

https://api.stripe.com/v1/customer_sessions \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d customer=

cus_PO34b57IOUb83c

\

-d

"

components[pricing_table][enabled]=true

"

Response

{

"

object

"

:

"

customer_session

"

,

"

client_secret

"

:

"

_POpxYpmkXdtttYtZQYhrsOJZ2RCQ9kCqqXRU6qrP5c4Jgje

"

,

"

components

"

:

{

"

buy_button

"

:

{

"

enabled

"

:

false

},

"

pricing_table

"

:

{

"

enabled

"

:

true

}

},

"

customer

"

:

"

cus_PO34b57IOUb83c

"

,

"

expires_at

"

:

1684790027

,

"

livemode

"

:

false

}
