---
title: Sources | Stripe API Reference
source_url: https://docs.stripe.com/api/sources
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:40.338309+00:00
kind: extracted-doc
---

# Sources | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/sources

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:40.338309+00:00

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

- Sources | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources The Source object Create a source Update a source Retrieve a source Attach a source Detach a source Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Sources Deprecated Ask about this section Copy for LLM View as Markdown Source objects allow you to accept a variety of payment methods.
- They represent a customer’s payment instrument, and can be used with the Stripe API just like a Card object: once chargeable, they can be charged, or can be attached to customers.
- Stripe doesn’t recommend using the deprecated Sources API .
- We recommend that you adopt the PaymentMethods API .
- This newer API provides access to our latest features and payment method types.

Extracted text:

Sources | Stripe API Reference

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

The Source object

Create a source

Update a source

Retrieve a source

Attach a source

Detach a source

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

Sources

Deprecated

Ask about this section

Copy for LLM

View as Markdown

Source

objects allow you to accept a variety of payment methods. They

represent a customer’s payment instrument, and can be used with the Stripe API

just like a

Card

object: once chargeable, they can be charged, or can be

attached to customers.

Stripe doesn’t recommend using the deprecated

Sources API

.

We recommend that you adopt the

PaymentMethods API

.

This newer API provides access to our latest features and payment method types.

Related guides:

Sources API

and

Sources & Customers

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

sources

POST

/

v1

/

sources

/

:id

GET

/

v1

/

sources

/

:id

POST

/

v1

/

customers

/

:id

/

sources

DELETE

/

v1

/

customers

/

:id

/

sources

/

:id

The Source object

Deprecated

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

nullable

integer

A positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for

single

_

use

sources.

currency

nullable

enum

Three-letter

ISO code for the currency

associated with the source. This is the currency for which the source will be chargeable once ready. Required for

single

_

use

sources.

customer

nullable

string

The ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

owner

nullable

object

Information about the owner of the payment instrument that may be used or required by particular source types.

Show child attributes

redirect

nullable

object

Information related to the redirect flow. Present if the source is authenticated by a redirect (

flow

is

redirect

).

Show child attributes

statement

_

descriptor

nullable

string

Extra information about a source. This will appear on your customer’s statement every time you charge the source.

status

string

The status of the source, one of

canceled

,

chargeable

,

consumed

,

failed

, or

pending

. Only

chargeable

sources can be used to create a charge.

type

enum

The

type

of the source. The

type

is a payment method, one of

ach

_

credit

_

transfer

,

ach

_

debit

,

alipay

,

bancontact

,

card

,

card

_

present

,

eps

,

giropay

,

ideal

,

multibanco

,

klarna

,

p24

,

sepa

_

debit

,

sofort

,

three

_

d

_

secure

, or

wechat

. An additional hash is included on the source with a name matching this value. It contains additional information specific to the

payment method

used.

Possible enum values

ach

_

credit

_

transfer

ach

_

debit

alipay

bancontact

card

card

_

present

eps

giropay

ideal

klarna

Show 6 more

More attributes

Expand all

object

string

allow

_

redisplay

nullable

enum

client

_

secret

string

code

_

verification

nullable

object

created

timestamp

flow

string

livemode

boolean

receiver

nullable

object

source

_

order

nullable

object

usage

nullable

string

The Source object

{

"

id

"

:

"

src_1N3lxdLkdIwHu7ixPHXy8UcI

"

,

"

object

"

:

"

source

"

,

"

ach_credit_transfer

"

:

{

"

account_number

"

:

"

test_eb829353ed79

"

,

"

bank_name

"

:

"

TEST BANK

"

,

"

fingerprint

"

:

"

kBQsBk9KtfCgjEYK

"

,

"

refund_account_holder_name

"

:

null

,

"

refund_account_holder_type

"

:

null

,

"

refund_routing_number

"

:

null

,

"

routing_number

"

:

"

110000000

"

,

"

swift_code

"

:

"

TSTEZ122

"

},

"

amount

"

:

null

,

"

client_secret

"

:

"

src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr

"

,

"

created

"

:

1683144457

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

flow

"

:

"

receiver

"

,

"

livemode

"

:

false

,

"

metadata

"

:

{},

"

owner

"

:

{

"

address

"

:

null

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

name

"

:

null

,

"

phone

"

:

null

,

"

verified_address

"

:

null

,

"

verified_email

"

:

null

,

"

verified_name

"

:

null

,

"

verified_phone

"

:

null

},

"

receiver

"

:

{

"

address

"

:

"

110000000-test_eb829353ed79

"

,

"

amount_charged

"

:

0

,

"

amount_received

"

:

0

,

"

amount_returned

"

:

0

,

"

refund_attributes_method

"

:

"

email

"

,

"

refund_attributes_status

"

:

"

missing

"

},

"

statement_descriptor

"

:

null

,

"

status

"

:

"

pending

"

,

"

type

"

:

"

ach_credit_transfer

"

,

"

usage

"

:

"

reusable

"

}

Create a source

Ask about this section

Copy for LLM

View as Markdown

Creates a new source object.

Parameters

type

string

Required

The

type

of the source to create. Required unless

customer

and

original

_

source

are specified (see the

Cloning card Sources

guide)

amount

integer

Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for

single

_

use

sources. Not supported for

receiver

type sources, where charge amount may not be specified until funds land.

currency

enum

Three-letter

ISO code for the currency

associated with the source. This is the currency for which the source will be chargeable once ready.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

owner

object

Information about the owner of the payment instrument that may be used or required by particular source types.

Show child parameters

redirect

object

Parameters required for the redirect flow. Required if the source is authenticated by a redirect (

flow

is

redirect

).

Show child parameters

statement

_

descriptor

string

An arbitrary string to be displayed on your customer’s statement. As an example, if your website is

RunClub

and the item you’re charging for is a race ticket, you may want to specify a

statement

_

descriptor

of

RunClub 5K race ticket

.

While many payment types will display this information, some may not display it at all.

More parameters

Expand all

flow

string

mandate

object

receiver

object

source

_

order

object

token

string

usage

string

Returns

Returns a newly created source.

POST

/

v1

/

sources

curl

https://api.stripe.com/v1/sources \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d type=ach_credit_transfer \

-d currency=usd \

--data-urlencode

"

owner[email]=jenny.rosen@example.com

"

Response

{

"

id

"

:

"

src_1N3lxdLkdIwHu7ixPHXy8UcI

"

,

"

object

"

:

"

source

"

,

"

ach_credit_transfer

"

:

{

"

account_number

"

:

"

test_eb829353ed79

"

,

"

bank_name

"

:

"

TEST BANK

"

,

"

fingerprint

"

:

"

kBQsBk9KtfCgjEYK

"

,

"

refund_account_holder_name

"

:

null

,

"

refund_account_holder_type

"

:

null

,

"

refund_routing_number

"

:

null

,

"

routing_number

"

:

"

110000000

"

,

"

swift_code

"

:

"

TSTEZ122

"

},

"

amount

"

:

null

,

"

client_secret

"

:

"

src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr

"

,

"

created

"

:

1683144457

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

flow

"

:

"

receiver

"

,

"

livemode

"

:

false

,

"

metadata

"

:

{},

"

owner

"

:

{

"

address

"

:

null

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

name

"

:

null

,

"

phone

"

:

null

,

"

verified_address

"

:

null

,

"

verified_email

"

:

null

,

"

verified_name

"

:

null

,

"

verified_phone

"

:

null

},

"

receiver

"

:

{

"

address

"

:

"

110000000-test_eb829353ed79

"

,

"

amount_charged

"

:

0

,

"

amount_received

"

:

0

,

"

amount_returned

"

:

0

,

"

refund_attributes_method

"

:

"

email

"

,

"

refund_attributes_status

"

:

"

missing

"

},

"

statement_descriptor

"

:

null

,

"

status

"

:

"

pending

"

,

"

type

"

:

"

ach_credit_transfer

"

,

"

usage

"

:

"

reusable

"

}

Update a source

Ask about this section

Copy for LLM

View as Markdown

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts the

metadata

and

owner

as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our

payment method guides

for more detail.

Parameters

amount

integer

Amount associated with the source.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

owner

object

Information about the owner of the payment instrument that may be used or required by particular source types.

Show child parameters

More parameters

Expand all

mandate

object

source

_

order

object

Returns

Returns the source object if the update succeeded. This call will

raise

an error

if update parameters are invalid.

POST

/

v1

/

sources

/

:id

curl

https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \

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

src_1N3lxdLkdIwHu7ixPHXy8UcI

"

,

"

object

"

:

"

source

"

,

"

ach_credit_transfer

"

:

{

"

account_number

"

:

"

test_eb829353ed79

"

,

"

bank_name

"

:

"

TEST BANK

"

,

"

fingerprint

"

:

"

kBQsBk9KtfCgjEYK

"

,

"

refund_account_holder_name

"

:

null

,

"

refund_account_holder_type

"

:

null

,

"

refund_routing_number

"

:

null

,

"

routing_number

"

:

"

110000000

"

,

"

swift_code

"

:

"

TSTEZ122

"

},

"

amount

"

:

null

,

"

client_secret

"

:

"

src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr

"

,

"

created

"

:

1683144457

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

flow

"

:

"

receiver

"

,

"

livemode

"

:

false

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

owner

"

:

{

"

address

"

:

null

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

name

"

:

null

,

"

phone

"

:

null

,

"

verified_address

"

:

null

,

"

verified_email

"

:

null

,

"

verified_name

"

:

null

,

"

verified_phone

"

:

null

},

"

receiver

"

:

{

"

address

"

:

"

110000000-test_eb829353ed79

"

,

"

amount_charged

"

:

0

,

"

amount_received

"

:

0

,

"

amount_returned

"

:

0

,

"

refund_attributes_method

"

:

"

email

"

,

"

refund_attributes_status

"

:

"

missing

"

},

"

statement_descriptor

"

:

null

,

"

status

"

:

"

pending

"

,

"

type

"

:

"

ach_credit_transfer

"

,

"

usage

"

:

"

reusable

"

}

Retrieve a source

Ask about this section

Copy for LLM

View as Markdown

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

Parameters

No

parameters

.

More parameters

Expand all

client

_

secret

string

Returns

Returns a source if a valid identifier was provided.

GET

/

v1

/

sources

/

:id

curl

https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \

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

src_1N3lxdLkdIwHu7ixPHXy8UcI

"

,

"

object

"

:

"

source

"

,

"

ach_credit_transfer

"

:

{

"

account_number

"

:

"

test_eb829353ed79

"

,

"

bank_name

"

:

"

TEST BANK

"

,

"

fingerprint

"

:

"

kBQsBk9KtfCgjEYK

"

,

"

refund_account_holder_name

"

:

null

,

"

refund_account_holder_type

"

:

null

,

"

refund_routing_number

"

:

null

,

"

routing_number

"

:

"

110000000

"

,

"

swift_code

"

:

"

TSTEZ122

"

},

"

amount

"

:

null

,

"

client_secret

"

:

"

src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr

"

,

"

created

"

:

1683144457

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

flow

"

:

"

receiver

"

,

"

livemode

"

:

false

,

"

metadata

"

:

{},

"

owner

"

:

{

"

address

"

:

null

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

name

"

:

null

,

"

phone

"

:

null

,

"

verified_address

"

:

null

,

"

verified_email

"

:

null

,

"

verified_name

"

:

null

,

"

verified_phone

"

:

null

},

"

receiver

"

:

{

"

address

"

:

"

110000000-test_eb829353ed79

"

,

"

amount_charged

"

:

0

,

"

amount_received

"

:

0

,

"

amount_returned

"

:

0

,

"

refund_attributes_method

"

:

"

email

"

,

"

refund_attributes_status

"

:

"

missing

"

},

"

statement_descriptor

"

:

null

,

"

status

"

:

"

pending

"

,

"

type

"

:

"

ach_credit_transfer

"

,

"

usage

"

:

"

reusable

"

}
