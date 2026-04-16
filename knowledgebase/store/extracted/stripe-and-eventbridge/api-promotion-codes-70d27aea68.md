---
title: Promotion Code | Stripe API Reference
source_url: https://docs.stripe.com/api/promotion_codes
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:44.803603+00:00
kind: extracted-doc
---

# Promotion Code | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/promotion_codes

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:44.803603+00:00

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

- Promotion Code | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code The Promotion Code object Create a promotion code Update a promotion code Retrieve a promotion code List all promotion codes Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Promotion Code Ask about this section Copy for LLM View as Markdown A Promotion Code represents a customer-redeemable code for an underlying promotion.
- You can create multiple codes for a single promotion.
- If you enable promotion codes in your customer portal configuration , then customers can redeem a code themselves when updating a subscription in the portal.
- Customers can also view the currently active promotion codes and coupons on each of their subscriptions in the portal.
- Yes No Endpoints POST / v1 / promotion_codes POST / v1 / promotion_codes / :id GET / v1 / promotion_codes / :id GET / v1 / promotion_codes The Promotion Code object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

Extracted text:

Promotion Code | Stripe API Reference

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

Cash Balance Transaction

Cards

Sources

Products

Products

Prices

Coupons

Promotion Code

The Promotion Code object

Create a promotion code

Update a promotion code

Retrieve a promotion code

List all promotion codes

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

Promotion Code

Ask about this section

Copy for LLM

View as Markdown

A Promotion Code represents a customer-redeemable code for an underlying promotion.

You can create multiple codes for a single promotion.

If you enable promotion codes in your

customer portal configuration

, then customers can redeem a code themselves when updating a subscription in the portal.

Customers can also view the currently active promotion codes and coupons on each of their subscriptions in the portal.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

promotion_codes

POST

/

v1

/

promotion_codes

/

:id

GET

/

v1

/

promotion_codes

/

:id

GET

/

v1

/

promotion_codes

The Promotion Code object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

code

string

The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), digits (0-9), and dashes (-).

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

promotion

object

The promotion referenced by this promotion code.

Show child attributes

More attributes

Expand all

object

string

active

boolean

created

timestamp

customer

nullable

string

Expandable

customer

_

account

nullable

string

expires

_

at

nullable

timestamp

livemode

boolean

max

_

redemptions

nullable

integer

restrictions

object

times

_

redeemed

integer

The Promotion Code object

{

"

id

"

:

"

promo_1MiM6KLkdIwHu7ixrIaX4wgn

"

,

"

object

"

:

"

promotion_code

"

,

"

active

"

:

true

,

"

code

"

:

"

A1H1Q1MG

"

,

"

promotion

"

:

{

"

type

"

:

"

coupon

"

,

"

coupon

"

:

"

nVJYDOag

"

},

"

created

"

:

1678040164

,

"

customer

"

:

null

,

"

expires_at

"

:

null

,

"

livemode

"

:

false

,

"

max_redemptions

"

:

null

,

"

metadata

"

:

{},

"

restrictions

"

:

{

"

first_time_transaction

"

:

false

,

"

minimum_amount

"

:

null

,

"

minimum_amount_currency

"

:

null

},

"

times_redeemed

"

:

0

}

Create a promotion code

Ask about this section

Copy for LLM

View as Markdown

A promotion code points to an underlying promotion. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

Parameters

promotion

object

Required

The promotion referenced by this promotion code.

Show child parameters

code

string

The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), digits (0-9), and dashes (-).

If left blank, we will generate one automatically.

The maximum length is 500 characters.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

More parameters

Expand all

active

boolean

customer

string

customer

_

account

string

expires

_

at

timestamp

max

_

redemptions

integer

restrictions

object

Returns

Returns the promotion code object.

POST

/

v1

/

promotion_codes

curl

https://api.stripe.com/v1/promotion_codes \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

promotion[type]=coupon

"

\

-d

"

promotion[coupon]=nVJYDOag

"

Response

{

"

id

"

:

"

promo_1MiM6KLkdIwHu7ixrIaX4wgn

"

,

"

object

"

:

"

promotion_code

"

,

"

active

"

:

true

,

"

code

"

:

"

A1H1Q1MG

"

,

"

promotion

"

:

{

"

type

"

:

"

coupon

"

,

"

coupon

"

:

"

nVJYDOag

"

},

"

created

"

:

1678040164

,

"

customer

"

:

null

,

"

expires_at

"

:

null

,

"

livemode

"

:

false

,

"

max_redemptions

"

:

null

,

"

metadata

"

:

{},

"

restrictions

"

:

{

"

first_time_transaction

"

:

false

,

"

minimum_amount

"

:

null

,

"

minimum_amount_currency

"

:

null

},

"

times_redeemed

"

:

0

}

Update a promotion code

Ask about this section

Copy for LLM

View as Markdown

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

Parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

More parameters

Expand all

active

boolean

restrictions

object

Returns

The updated promotion code object is returned upon success. Otherwise, this call

raises

an error

.

POST

/

v1

/

promotion_codes

/

:id

curl

https://api.stripe.com/v1/promotion_codes/

promo_1MiM6KLkdIwHu7ixrIaX4wgn

\

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

metadata[order_id]=6735

"

Response

{

"

id

"

:

"

promo_1MiM6KLkdIwHu7ixrIaX4wgn

"

,

"

object

"

:

"

promotion_code

"

,

"

active

"

:

true

,

"

code

"

:

"

A1H1Q1MG

"

,

"

promotion

"

:

{

"

type

"

:

"

coupon

"

,

"

coupon

"

:

"

nVJYDOag

"

},

"

created

"

:

1678040164

,

"

customer

"

:

null

,

"

expires_at

"

:

null

,

"

livemode

"

:

false

,

"

max_redemptions

"

:

null

,

"

metadata

"

:

{

"

order_id

"

:

"

6735

"

},

"

restrictions

"

:

{

"

first_time_transaction

"

:

false

,

"

minimum_amount

"

:

null

,

"

minimum_amount_currency

"

:

null

},

"

times_redeemed

"

:

0

}

Retrieve a promotion code

Ask about this section

Copy for LLM

View as Markdown

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing

code

use

list

with the desired

code

.

Parameters

No

parameters

.

Returns

Returns a promotion code if a valid promotion code ID was provided.

Raises

an error

otherwise.

GET

/

v1

/

promotion_codes

/

:id

curl

https://api.stripe.com/v1/promotion_codes/

promo_1MiM6KLkdIwHu7ixrIaX4wgn

\

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

Response

{

"

id

"

:

"

promo_1MiM6KLkdIwHu7ixrIaX4wgn

"

,

"

object

"

:

"

promotion_code

"

,

"

active

"

:

true

,

"

code

"

:

"

A1H1Q1MG

"

,

"

promotion

"

:

{

"

type

"

:

"

coupon

"

,

"

coupon

"

:

"

nVJYDOag

"

},

"

created

"

:

1678040164

,

"

customer

"

:

null

,

"

expires_at

"

:

null

,

"

livemode

"

:

false

,

"

max_redemptions

"

:

null

,

"

metadata

"

:

{},

"

restrictions

"

:

{

"

first_time_transaction

"

:

false

,

"

minimum_amount

"

:

null

,

"

minimum_amount_currency

"

:

null

},

"

times_redeemed

"

:

0

}
