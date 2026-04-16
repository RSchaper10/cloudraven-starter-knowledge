---
title: Coupons | Stripe API Reference
source_url: https://docs.stripe.com/api/coupons
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:43.844326+00:00
kind: extracted-doc
---

# Coupons | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/coupons

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:43.844326+00:00

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

- Coupons | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons The Coupon object Create a coupon Update a coupon Retrieve a coupon List all coupons Delete a coupon Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Coupons Ask about this section Copy for LLM View as Markdown A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer.
- Coupons may be applied to subscriptions , invoices , checkout sessions , quotes , and more.
- Coupons do not work with conventional one-off charges or payment intents .
- Yes No Endpoints POST / v1 / coupons POST / v1 / coupons / :id GET / v1 / coupons / :id GET / v1 / coupons DELETE / v1 / coupons / :id The Coupon object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- amount _ off nullable integer Amount (in the currency specified) that will be taken off the subtotal of any invoices for this customer.

Extracted text:

Coupons | Stripe API Reference

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

The Coupon object

Create a coupon

Update a coupon

Retrieve a coupon

List all coupons

Delete a coupon

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

Coupons

Ask about this section

Copy for LLM

View as Markdown

A coupon contains information about a percent-off or amount-off discount you

might want to apply to a customer. Coupons may be applied to

subscriptions

,

invoices

,

checkout sessions

,

quotes

, and more. Coupons do not work with conventional one-off

charges

or

payment intents

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

coupons

POST

/

v1

/

coupons

/

:id

GET

/

v1

/

coupons

/

:id

GET

/

v1

/

coupons

DELETE

/

v1

/

coupons

/

:id

The Coupon object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

_

off

nullable

integer

Amount (in the

currency

specified) that will be taken off the subtotal of any invoices for this customer.

currency

nullable

enum

If

amount

_

off

has been set, the three-letter

ISO code for the currency

of the amount to take off.

duration

enum

One of

forever

,

once

, or

repeating

. Describes how long a customer who applies this coupon will get the discount.

Possible enum values

forever

Applies to all charges from a subscription with this coupon applied.

once

Applies to the first charge from a subscription with this coupon applied.

repeating

Applies to charges in the first

duration

_

in

_

months

months from a subscription with this coupon applied.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

name

nullable

string

Name of the coupon displayed to customers on for instance invoices or receipts.

percent

_

off

nullable

float

Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a

$

100 invoice

$

50 instead.

More attributes

Expand all

object

string

applies

_

to

nullable

object

Expandable

created

timestamp

currency

_

options

nullable

object

Expandable

duration

_

in

_

months

nullable

integer

livemode

boolean

max

_

redemptions

nullable

integer

redeem

_

by

nullable

timestamp

times

_

redeemed

integer

valid

boolean

The Coupon object

{

"

id

"

:

"

jMT0WJUD

"

,

"

object

"

:

"

coupon

"

,

"

amount_off

"

:

null

,

"

created

"

:

1678037688

,

"

currency

"

:

null

,

"

duration

"

:

"

repeating

"

,

"

duration_in_months

"

:

3

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

name

"

:

null

,

"

percent_off

"

:

25.5

,

"

redeem_by

"

:

null

,

"

times_redeemed

"

:

0

,

"

valid

"

:

true

}

Create a coupon

Ask about this section

Copy for LLM

View as Markdown

You can create coupons easily via the

coupon management

page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

A coupon has either a

percent

_

off

or an

amount

_

off

and

currency

. If you set an

amount

_

off

, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of

100

USD

will have a final total of

0

USD

if a coupon with an

amount

_

off

of

20000

is applied to it and an invoice with a subtotal of

300

USD

will have a final total of

100

USD

if a coupon with an

amount

_

off

of

20000

is applied to it.

Parameters

amount

_

off

integer

A positive integer representing the amount to subtract from an invoice total (required if

percent

_

off

is not passed).

currency

enum

Three-letter

ISO code for the currency

of the

amount

_

off

parameter (required if

amount

_

off

is passed).

duration

enum

Specifies how long the discount will be in effect if used on a subscription. Defaults to

once

.

Possible enum values

forever

Applies to all charges from a subscription with this coupon applied.

once

Applies to the first charge from a subscription with this coupon applied.

repeating

Applies to charges in the first

duration

_

in

_

months

months from a subscription with this coupon applied.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the

id

is shown if

name

is not set.

The maximum length is 40 characters.

percent

_

off

float

A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if

amount

_

off

is not passed).

More parameters

Expand all

applies

_

to

object

currency

_

options

object

duration

_

in

_

months

integer

id

string

max

_

redemptions

integer

redeem

_

by

timestamp

Returns

Returns the coupon object.

POST

/

v1

/

coupons

curl

https://api.stripe.com/v1/coupons \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d duration=forever \

-d

"

percent_off=25.5

"

Response

{

"

id

"

:

"

jMT0WJUD

"

,

"

object

"

:

"

coupon

"

,

"

amount_off

"

:

null

,

"

created

"

:

1678037688

,

"

currency

"

:

null

,

"

duration

"

:

"

forever

"

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

name

"

:

null

,

"

percent_off

"

:

25.5

,

"

redeem_by

"

:

null

,

"

times_redeemed

"

:

0

,

"

valid

"

:

true

}

Update a coupon

Ask about this section

Copy for LLM

View as Markdown

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

Parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the

id

is shown if

name

is not set.

The maximum length is 40 characters.

More parameters

Expand all

currency

_

options

object

Returns

The newly updated coupon object if the call succeeded. Otherwise, this call

raises

an error

, such as if the coupon has been deleted.

POST

/

v1

/

coupons

/

:id

curl

https://api.stripe.com/v1/coupons/jMT0WJUD \

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

jMT0WJUD

"

,

"

object

"

:

"

coupon

"

,

"

amount_off

"

:

null

,

"

created

"

:

1678037688

,

"

currency

"

:

null

,

"

duration

"

:

"

repeating

"

,

"

duration_in_months

"

:

3

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

name

"

:

null

,

"

percent_off

"

:

25.5

,

"

redeem_by

"

:

null

,

"

times_redeemed

"

:

0

,

"

valid

"

:

true

}

Retrieve a coupon

Ask about this section

Copy for LLM

View as Markdown

Retrieves the coupon with the given ID.

Parameters

No

parameters

.

Returns

Returns a coupon if a valid coupon ID was provided.

Raises

an error

otherwise.

GET

/

v1

/

coupons

/

:id

curl

https://api.stripe.com/v1/coupons/jMT0WJUD \

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

jMT0WJUD

"

,

"

object

"

:

"

coupon

"

,

"

amount_off

"

:

null

,

"

created

"

:

1678037688

,

"

currency

"

:

null

,

"

duration

"

:

"

repeating

"

,

"

duration_in_months

"

:

3

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

name

"

:

null

,

"

percent_off

"

:

25.5

,

"

redeem_by

"

:

null

,

"

times_redeemed

"

:

0

,

"

valid

"

:

true

}
