---
title: Balance | Stripe API Reference
source_url: https://docs.stripe.com/api/balance
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:02.217987+00:00
kind: extracted-doc
---

# Balance | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/balance

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:02.217987+00:00

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
- https://docs.stripe.com/api/balance/balance_object
- https://docs.stripe.com/api/balance/balance_retrieve
- https://docs.stripe.com/api/balance_transactions
- https://docs.stripe.com/api/charges
- https://docs.stripe.com/api/customers

Captured summary:

- Balance | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance The Balance object Retrieve balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Balance Ask about this section Copy for LLM View as Markdown This is an object representing your Stripe balance.
- You can retrieve it to see the balance currently on your Stripe account.
- The top-level available and pending comprise your “payments balance.” Related guide: Balances and settlement time , Understanding Connect account balances Was this section helpful?
- Yes No Endpoints GET / v1 / balance The Balance object Ask about this section Copy for LLM View as Markdown Attributes available array of objects Available funds that you can transfer or pay out automatically by Stripe or explicitly through the Transfers API or Payouts API .
- You can find the available balance for each currency and payment type in the source _ types property.

Extracted text:

Balance | Stripe API Reference

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

The Balance object

Retrieve balance

Balance Transactions

Charges

Customers

Customer Session

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

Balance

Ask about this section

Copy for LLM

View as Markdown

This is an object representing your Stripe balance. You can retrieve it to see

the balance currently on your Stripe account.

The top-level

available

and

pending

comprise your “payments balance.”

Related guide:

Balances and settlement time

,

Understanding Connect account balances

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

balance

The Balance object

Ask about this section

Copy for LLM

View as Markdown

Attributes

available

array of objects

Available funds that you can transfer or pay out automatically by Stripe or explicitly through the

Transfers API

or

Payouts API

. You can find the available balance for each currency and payment type in the

source

_

types

property.

Show child attributes

pending

array of objects

Funds that aren’t available in the balance yet. You can find the pending balance for each currency and each payment type in the

source

_

types

property.

Show child attributes

More attributes

Expand all

object

string

connect

_

reserved

nullable

array of objects

Connect only

instant

_

available

nullable

array of objects

issuing

nullable

object

livemode

boolean

refund

_

and

_

dispute

_

prefunding

nullable

object

The Balance object

{

"

object

"

:

"

balance

"

,

"

available

"

:

[

{

"

amount

"

:

666670

,

"

currency

"

:

"

usd

"

,

"

source_types

"

:

{

"

card

"

:

666670

}

}

],

"

connect_reserved

"

:

[

{

"

amount

"

:

0

,

"

currency

"

:

"

usd

"

}

],

"

livemode

"

:

false

,

"

pending

"

:

[

{

"

amount

"

:

61414

,

"

currency

"

:

"

usd

"

,

"

source_types

"

:

{

"

card

"

:

61414

}

}

]

}

Retrieve balance

Ask about this section

Copy for LLM

View as Markdown

Retrieves the current account balance, based on the authentication that was used to make the request.

For a sample request, see

Accounting for negative balances

.

Parameters

No

parameters

.

Returns

Returns a balance object for the account that was authenticated in the request.

GET

/

v1

/

balance

curl

https://api.stripe.com/v1/balance \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

Response

{

"

object

"

:

"

balance

"

,

"

available

"

:

[

{

"

amount

"

:

666670

,

"

currency

"

:

"

usd

"

,

"

source_types

"

:

{

"

card

"

:

666670

}

}

],

"

connect_reserved

"

:

[

{

"

amount

"

:

0

,

"

currency

"

:

"

usd

"

}

],

"

livemode

"

:

false

,

"

pending

"

:

[

{

"

amount

"

:

61414

,

"

currency

"

:

"

usd

"

,

"

source_types

"

:

{

"

card

"

:

61414

}

}

]

}
