---
title: Refunds | Stripe API Reference
source_url: https://docs.stripe.com/api/refunds
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:29.618411+00:00
kind: extracted-doc
---

# Refunds | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/refunds

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:29.618411+00:00

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

- Refunds | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds The Refund object Create a refund Update a refund Retrieve a refund List all refunds Cancel a refund Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Refunds Ask about this section Copy for LLM View as Markdown Refund objects allow you to refund a previously created charge that isn’t refunded yet.
- Funds are refunded to the credit or debit card that’s initially charged.
- Related guide: Refunds Was this section helpful?
- Yes No Endpoints POST / v1 / refunds POST / v1 / refunds / :id GET / v1 / refunds / :id GET / v1 / refunds POST / v1 / refunds / :id / cancel The Refund object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- charge nullable string Expandable ID of the charge that’s refunded.

Extracted text:

Refunds | Stripe API Reference

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

The Refund object

Create a refund

Update a refund

Retrieve a refund

List all refunds

Cancel a refund

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

Refunds

Ask about this section

Copy for LLM

View as Markdown

Refund objects allow you to refund a previously created charge that isn’t

refunded yet. Funds are refunded to the credit or debit card that’s

initially charged.

Related guide:

Refunds

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

refunds

POST

/

v1

/

refunds

/

:id

GET

/

v1

/

refunds

/

:id

GET

/

v1

/

refunds

POST

/

v1

/

refunds

/

:id

/

cancel

The Refund object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

integer

Amount, in

cents

.

charge

nullable

string

Expandable

ID of the charge that’s refunded.

currency

enum

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

description

nullable

string

An arbitrary string attached to the object. You can use this for displaying to users (available on non-card refunds only).

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

payment

_

intent

nullable

string

Expandable

ID of the PaymentIntent that’s refunded.

reason

nullable

enum

Reason for the refund, which is either user-provided (

duplicate

,

fraudulent

, or

requested

_

by

_

customer

) or generated by Stripe internally (

expired

_

uncaptured

_

charge

).

status

nullable

string

Status of the refund. This can be

pending

,

requires

_

action

,

succeeded

,

failed

, or

canceled

. Learn more about

failed refunds

.

More attributes

Expand all

object

string

balance

_

transaction

nullable

string

Expandable

created

timestamp

destination

_

details

nullable

object

failure

_

balance

_

transaction

nullable

string

Expandable

failure

_

reason

nullable

string

instructions

_

email

nullable

string

next

_

action

nullable

object

pending

_

reason

nullable

enum

receipt

_

number

nullable

string

source

_

transfer

_

reversal

nullable

string

Expandable

Connect only

transfer

_

reversal

nullable

string

Expandable

Connect only

The Refund object

{

"

id

"

:

"

re_1Nispe2eZvKYlo2Cd31jOCgZ

"

,

"

object

"

:

"

refund

"

,

"

amount

"

:

1000

,

"

balance_transaction

"

:

"

txn_1Nispe2eZvKYlo2CYezqFhEx

"

,

"

charge

"

:

"

ch_1NirD82eZvKYlo2CIvbtLWuY

"

,

"

created

"

:

1692942318

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

destination_details

"

:

{

"

card

"

:

{

"

reference

"

:

"

123456789012

"

,

"

reference_status

"

:

"

available

"

,

"

reference_type

"

:

"

acquirer_reference_number

"

,

"

type

"

:

"

refund

"

},

"

type

"

:

"

card

"

},

"

metadata

"

:

{},

"

payment_intent

"

:

"

pi_1GszsK2eZvKYlo2CfhZyoZLp

"

,

"

reason

"

:

null

,

"

receipt_number

"

:

null

,

"

source_transfer_reversal

"

:

null

,

"

status

"

:

"

succeeded

"

,

"

transfer_reversal

"

:

null

}

Create a refund

Ask about this section

Copy for LLM

View as Markdown

When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.

Creating a new refund will refund a charge that has previously been created but not yet refunded.

Funds will be refunded to the credit or debit card that was originally charged.

You can optionally refund only part of a charge.

You can do so multiple times, until the entire charge has been refunded.

Once entirely refunded, a charge can’t be refunded again.

This method will

raise

an error when called on an already-refunded charge,

or when trying to refund more money than is left on a charge.

Parameters

amount

integer

A positive integer in the

smallest currency unit

representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge.

charge

string

The identifier of the charge to refund.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

payment

_

intent

string

The identifier of the PaymentIntent to refund.

reason

string

String indicating the reason for the refund. If set, possible values are

duplicate

,

fraudulent

, and

requested

_

by

_

customer

. If you believe the charge to be fraudulent, specifying

fraudulent

as the reason will add the associated card and email to your

block lists

, and will also help us improve our fraud detection algorithms.

More parameters

Expand all

instructions

_

email

string

origin

enum

refund

_

application

_

fee

boolean

Connect only

reverse

_

transfer

boolean

Connect only

Returns

Returns the

Refund

object if the refund succeeded.

Raises

an error

if the Charge/PaymentIntent has already been refunded, or if an invalid identifier was provided.

POST

/

v1

/

refunds

curl

https://api.stripe.com/v1/refunds \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d charge=

ch_1NirD82eZvKYlo2CIvbtLWuY

Response

{

"

id

"

:

"

re_1Nispe2eZvKYlo2Cd31jOCgZ

"

,

"

object

"

:

"

refund

"

,

"

amount

"

:

1000

,

"

balance_transaction

"

:

"

txn_1Nispe2eZvKYlo2CYezqFhEx

"

,

"

charge

"

:

"

ch_1NirD82eZvKYlo2CIvbtLWuY

"

,

"

created

"

:

1692942318

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

destination_details

"

:

{

"

card

"

:

{

"

reference

"

:

"

123456789012

"

,

"

reference_status

"

:

"

available

"

,

"

reference_type

"

:

"

acquirer_reference_number

"

,

"

type

"

:

"

refund

"

},

"

type

"

:

"

card

"

},

"

metadata

"

:

{},

"

payment_intent

"

:

"

pi_1GszsK2eZvKYlo2CfhZyoZLp

"

,

"

reason

"

:

null

,

"

receipt_number

"

:

null

,

"

source_transfer_reversal

"

:

null

,

"

status

"

:

"

succeeded

"

,

"

transfer_reversal

"

:

null

}

Update a refund

Ask about this section

Copy for LLM

View as Markdown

Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.

This request only accepts

metadata

as an argument.

Parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the refund object if the update succeeds. This call

raises

an error

if update parameters are invalid.

POST

/

v1

/

refunds

/

:id

curl

https://api.stripe.com/v1/refunds/

re_1Nispe2eZvKYlo2Cd31jOCgZ

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

re_1Nispe2eZvKYlo2Cd31jOCgZ

"

,

"

object

"

:

"

refund

"

,

"

amount

"

:

1000

,

"

balance_transaction

"

:

"

txn_1Nispe2eZvKYlo2CYezqFhEx

"

,

"

charge

"

:

"

ch_1NirD82eZvKYlo2CIvbtLWuY

"

,

"

created

"

:

1692942318

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

destination_details

"

:

{

"

card

"

:

{

"

reference

"

:

"

123456789012

"

,

"

reference_status

"

:

"

available

"

,

"

reference_type

"

:

"

acquirer_reference_number

"

,

"

type

"

:

"

refund

"

},

"

type

"

:

"

card

"

},

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

payment_intent

"

:

"

pi_1GszsK2eZvKYlo2CfhZyoZLp

"

,

"

reason

"

:

null

,

"

receipt_number

"

:

null

,

"

source_transfer_reversal

"

:

null

,

"

status

"

:

"

succeeded

"

,

"

transfer_reversal

"

:

null

}

Retrieve a refund

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an existing refund.

Parameters

No

parameters

.

Returns

Returns a refund if you provide a valid ID.

Raises

an error

otherwise.

GET

/

v1

/

refunds

/

:id

curl

https://api.stripe.com/v1/refunds/

re_1Nispe2eZvKYlo2Cd31jOCgZ

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

re_1Nispe2eZvKYlo2Cd31jOCgZ

"

,

"

object

"

:

"

refund

"

,

"

amount

"

:

1000

,

"

balance_transaction

"

:

"

txn_1Nispe2eZvKYlo2CYezqFhEx

"

,

"

charge

"

:

"

ch_1NirD82eZvKYlo2CIvbtLWuY

"

,

"

created

"

:

1692942318

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

destination_details

"

:

{

"

card

"

:

{

"

reference

"

:

"

123456789012

"

,

"

reference_status

"

:

"

available

"

,

"

reference_type

"

:

"

acquirer_reference_number

"

,

"

type

"

:

"

refund

"

},

"

type

"

:

"

card

"

},

"

metadata

"

:

{},

"

payment_intent

"

:

"

pi_1GszsK2eZvKYlo2CfhZyoZLp

"

,

"

reason

"

:

null

,

"

receipt_number

"

:

null

,

"

source_transfer_reversal

"

:

null

,

"

status

"

:

"

succeeded

"

,

"

transfer_reversal

"

:

null

}
