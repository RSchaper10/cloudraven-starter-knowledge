---
title: Cash Balance | Stripe API Reference
source_url: https://docs.stripe.com/api/cash_balance
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:37.615338+00:00
kind: extracted-doc
---

# Cash Balance | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/cash_balance

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:37.615338+00:00

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
- https://docs.stripe.com/api/disputes

Captured summary:

- Cash Balance | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance The Cash balance object Update a cash balance's settings Retrieve a cash balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Cash Balance Ask about this section Copy for LLM View as Markdown A customer’s Cash balance represents real funds.
- Customers can add funds to their cash balance by sending a bank transfer.
- These funds can be used for payment and can eventually be paid out to your bank account.
- Yes No Endpoints POST / v1 / customers / :id / cash_balance GET / v1 / customers / :id / cash_balance The Cash balance object Ask about this section Copy for LLM View as Markdown Attributes object string String representing the object’s type.
- Objects of the same type share the same value.

Extracted text:

Cash Balance | Stripe API Reference

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

The Cash balance object

Update a cash balance's settings

Retrieve a cash balance

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

Cash Balance

Ask about this section

Copy for LLM

View as Markdown

A customer’s

Cash balance

represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

customers

/

:id

/

cash_balance

GET

/

v1

/

customers

/

:id

/

cash_balance

The Cash balance object

Ask about this section

Copy for LLM

View as Markdown

Attributes

object

string

String representing the object’s type. Objects of the same type share the same value.

available

nullable

object

A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the

smallest currency unit

.

customer

string

The ID of the customer whose cash balance this object represents.

customer

_

account

nullable

string

The ID of an Account representing a customer whose cash balance this object represents.

livemode

boolean

If the object exists in live mode, the value is

true

. If the object exists in test mode, the value is

false

.

settings

object

A hash of settings for this cash balance.

Show child attributes

The Cash balance object

{

"

object

"

:

"

cash_balance

"

,

"

available

"

:

{

"

eur

"

:

10000

},

"

customer

"

:

"

cus_OaCLf8Fi1nbFpJ

"

,

"

livemode

"

:

false

,

"

settings

"

:

{

"

reconciliation_mode

"

:

"

automatic

"

,

"

using_merchant_default

"

:

true

}

}

Update a cash balance's settings

Ask about this section

Copy for LLM

View as Markdown

Changes the settings on a customer’s cash balance.

Parameters

settings

object

A hash of settings for this cash balance.

Show child parameters

Returns

The customer’s cash balance, with the updated settings.

POST

/

v1

/

customers

/

:id

/

cash_balance

curl

https://api.stripe.com/v1/customers/

cus_Ob4Xiw8KXOqcvM

/cash_balance \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

settings[reconciliation_mode]=manual

"

Response

{

"

object

"

:

"

cash_balance

"

,

"

available

"

:

null

,

"

customer

"

:

"

cus_Ob4Xiw8KXOqcvM

"

,

"

livemode

"

:

false

,

"

settings

"

:

{

"

reconciliation_mode

"

:

"

manual

"

,

"

using_merchant_default

"

:

false

}

}

Retrieve a cash balance

Ask about this section

Copy for LLM

View as Markdown

Retrieves a customer’s cash balance.

Parameters

No

parameters

.

Returns

The Cash Balance object for a given customer.

GET

/

v1

/

customers

/

:id

/

cash_balance

curl

https://api.stripe.com/v1/customers/

cus_OaCLf8Fi1nbFpJ

/cash_balance \

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

cash_balance

"

,

"

available

"

:

{

"

eur

"

:

10000

},

"

customer

"

:

"

cus_OaCLf8Fi1nbFpJ

"

,

"

livemode

"

:

false

,

"

settings

"

:

{

"

reconciliation_mode

"

:

"

automatic

"

,

"

using_merchant_default

"

:

true

}

}
