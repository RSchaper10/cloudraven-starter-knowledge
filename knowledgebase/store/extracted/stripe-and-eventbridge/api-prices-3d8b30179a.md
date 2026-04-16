---
title: Prices | Stripe API Reference
source_url: https://docs.stripe.com/api/prices
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:42.745232+00:00
kind: extracted-doc
---

# Prices | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/prices

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:42.745232+00:00

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

- Prices | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices The Price object Create a price Update a price Retrieve a price List all prices Search prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Prices Ask about this section Copy for LLM View as Markdown Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
- Products help you track inventory or provisioning, and prices help you track payment terms.
- Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices.
- This approach lets you change prices without having to change your provisioning scheme.
- For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.

Extracted text:

Prices | Stripe API Reference

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

The Price object

Create a price

Update a price

Retrieve a price

List all prices

Search prices

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

Prices

Ask about this section

Copy for LLM

View as Markdown

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.

Products

help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.

Related guides:

Set up a subscription

,

create an invoice

, and more about

products and prices

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

prices

POST

/

v1

/

prices

/

:id

GET

/

v1

/

prices

/

:id

GET

/

v1

/

prices

GET

/

v1

/

prices

/

search

The Price object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

active

boolean

Whether the price can be used for new purchases.

currency

enum

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

nickname

nullable

string

A brief description of the price, hidden from customers.

product

string

Expandable

The ID of the product this price is associated with.

recurring

nullable

object

The recurring components of a price such as

interval

and

usage

_

type

.

Show child attributes

tax

_

behavior

nullable

enum

Only required if a

default tax behavior

was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of

inclusive

,

exclusive

, or

unspecified

. Once specified as either

inclusive

or

exclusive

, it cannot be changed.

Possible enum values

exclusive

inclusive

unspecified

type

enum

One of

one

_

time

or

recurring

depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

Possible enum values

one

_

time

recurring

unit

_

amount

nullable

integer

The unit amount in

cents

to be charged, represented as a whole integer if possible. Only set if

billing

_

scheme=per

_

unit

.

More attributes

Expand all

object

string

billing

_

scheme

enum

created

timestamp

currency

_

options

nullable

object

Expandable

custom

_

unit

_

amount

nullable

object

livemode

boolean

lookup

_

key

nullable

string

tiers

nullable

array of objects

Expandable

tiers

_

mode

nullable

enum

transform

_

quantity

nullable

object

unit

_

amount

_

decimal

nullable

decimal string

The Price object

{

"

id

"

:

"

price_1MoBy5LkdIwHu7ixZhnattbh

"

,

"

object

"

:

"

price

"

,

"

active

"

:

true

,

"

billing_scheme

"

:

"

per_unit

"

,

"

created

"

:

1679431181

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

custom_unit_amount

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

lookup_key

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

nickname

"

:

null

,

"

product

"

:

"

prod_NZKdYqrwEYx6iK

"

,

"

recurring

"

:

{

"

interval

"

:

"

month

"

,

"

interval_count

"

:

1

,

"

trial_period_days

"

:

null

,

"

usage_type

"

:

"

licensed

"

},

"

tax_behavior

"

:

"

unspecified

"

,

"

tiers_mode

"

:

null

,

"

transform_quantity

"

:

null

,

"

type

"

:

"

recurring

"

,

"

unit_amount

"

:

1000

,

"

unit_amount_decimal

"

:

"

1000

"

}

Create a price

Ask about this section

Copy for LLM

View as Markdown

Creates a new

Price

for an existing

Product

. The Price can be recurring or one-time.

Parameters

currency

enum

Required

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

active

boolean

Whether the price can be used for new purchases. Defaults to

true

.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

nickname

string

A brief description of the price, hidden from customers.

product

string

Required unless product_data is provided

The ID of the

Product

that this

Price

will belong to.

recurring

object

The recurring components of a price such as

interval

and

usage

_

type

.

Show child parameters

tax

_

behavior

enum

Recommended if calculating taxes

Only required if a

default tax behavior

was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of

inclusive

,

exclusive

, or

unspecified

. Once specified as either

inclusive

or

exclusive

, it cannot be changed.

Possible enum values

exclusive

inclusive

unspecified

unit

_

amount

integer

Required conditionally

A positive integer in

cents

(or 0 for a free price) representing how much to charge. One of

unit

_

amount

,

unit

_

amount

_

decimal

, or

custom

_

unit

_

amount

is required, unless

billing

_

scheme=tiered

.

More parameters

Expand all

billing

_

scheme

enum

currency

_

options

object

custom

_

unit

_

amount

object

Required unless unit_amount is provided

lookup

_

key

string

product

_

data

object

Required unless product is provided

tiers

array of objects

Required if billing_scheme=tiered

tiers

_

mode

enum

Required if billing_scheme=tiered

transfer

_

lookup

_

key

boolean

transform

_

quantity

object

unit

_

amount

_

decimal

string

Returns

The newly created

Price

object is returned upon success. Otherwise, this call

raises

an error

.

POST

/

v1

/

prices

curl

https://api.stripe.com/v1/prices \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d currency=usd \

-d unit_amount=1000 \

-d

"

recurring[interval]=month

"

\

-d

"

product_data[name]=Gold Plan

"

Response

{

"

id

"

:

"

price_1MoBy5LkdIwHu7ixZhnattbh

"

,

"

object

"

:

"

price

"

,

"

active

"

:

true

,

"

billing_scheme

"

:

"

per_unit

"

,

"

created

"

:

1679431181

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

custom_unit_amount

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

lookup_key

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

nickname

"

:

null

,

"

product

"

:

"

prod_NZKdYqrwEYx6iK

"

,

"

recurring

"

:

{

"

interval

"

:

"

month

"

,

"

interval_count

"

:

1

,

"

trial_period_days

"

:

null

,

"

usage_type

"

:

"

licensed

"

},

"

tax_behavior

"

:

"

unspecified

"

,

"

tiers_mode

"

:

null

,

"

transform_quantity

"

:

null

,

"

type

"

:

"

recurring

"

,

"

unit_amount

"

:

1000

,

"

unit_amount_decimal

"

:

"

1000

"

}

Update a price

Ask about this section

Copy for LLM

View as Markdown

Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

Parameters

active

boolean

Whether the price can be used for new purchases. Defaults to

true

.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

nickname

string

A brief description of the price, hidden from customers.

tax

_

behavior

enum

Recommended if calculating taxes

Only required if a

default tax behavior

was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of

inclusive

,

exclusive

, or

unspecified

. Once specified as either

inclusive

or

exclusive

, it cannot be changed.

Possible enum values

exclusive

inclusive

unspecified

More parameters

Expand all

currency

_

options

object

lookup

_

key

string

transfer

_

lookup

_

key

boolean

Returns

The updated price object is returned upon success. Otherwise, this call

raises

an error

.

POST

/

v1

/

prices

/

:id

curl

https://api.stripe.com/v1/prices/

price_1MoBy5LkdIwHu7ixZhnattbh

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

price_1MoBy5LkdIwHu7ixZhnattbh

"

,

"

object

"

:

"

price

"

,

"

active

"

:

true

,

"

billing_scheme

"

:

"

per_unit

"

,

"

created

"

:

1679431181

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

custom_unit_amount

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

lookup_key

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

nickname

"

:

null

,

"

product

"

:

"

prod_NZKdYqrwEYx6iK

"

,

"

recurring

"

:

{

"

interval

"

:

"

month

"

,

"

interval_count

"

:

1

,

"

trial_period_days

"

:

null

,

"

usage_type

"

:

"

licensed

"

},

"

tax_behavior

"

:

"

unspecified

"

,

"

tiers_mode

"

:

null

,

"

transform_quantity

"

:

null

,

"

type

"

:

"

recurring

"

,

"

unit_amount

"

:

1000

,

"

unit_amount_decimal

"

:

"

1000

"

}

Retrieve a price

Ask about this section

Copy for LLM

View as Markdown

Retrieves the price with the given ID.

Parameters

No

parameters

.

Returns

Returns a price if a valid price or plan ID was provided.

Raises

an error

otherwise.

GET

/

v1

/

prices

/

:id

curl

https://api.stripe.com/v1/prices/

price_1MoBy5LkdIwHu7ixZhnattbh

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

price_1MoBy5LkdIwHu7ixZhnattbh

"

,

"

object

"

:

"

price

"

,

"

active

"

:

true

,

"

billing_scheme

"

:

"

per_unit

"

,

"

created

"

:

1679431181

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

custom_unit_amount

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

lookup_key

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

nickname

"

:

null

,

"

product

"

:

"

prod_NZKdYqrwEYx6iK

"

,

"

recurring

"

:

{

"

interval

"

:

"

month

"

,

"

interval_count

"

:

1

,

"

trial_period_days

"

:

null

,

"

usage_type

"

:

"

licensed

"

},

"

tax_behavior

"

:

"

unspecified

"

,

"

tiers_mode

"

:

null

,

"

transform_quantity

"

:

null

,

"

type

"

:

"

recurring

"

,

"

unit_amount

"

:

1000

,

"

unit_amount_decimal

"

:

"

1000

"

}
