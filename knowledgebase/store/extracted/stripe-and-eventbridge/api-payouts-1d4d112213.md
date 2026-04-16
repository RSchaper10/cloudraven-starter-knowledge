---
title: Payouts | Stripe API Reference
source_url: https://docs.stripe.com/api/payouts
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:28.755349+00:00
kind: extracted-doc
---

# Payouts | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/payouts

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:28.755349+00:00

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

- Payouts | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts The Payout object Create a payout Update a payout Retrieve a payout List all payouts Cancel a payout Reverse a payout Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Payouts Ask about this section Copy for LLM View as Markdown A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account .
- You can retrieve individual payouts, and list all payouts.
- Payouts are made on varying schedules , depending on your country and industry.
- Related guide: Receiving payouts Was this section helpful?
- Yes No Endpoints POST / v1 / payouts POST / v1 / payouts / :id GET / v1 / payouts / :id GET / v1 / payouts POST / v1 / payouts / :id / cancel POST / v1 / payouts / :id / reverse The Payout object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

Extracted text:

Payouts | Stripe API Reference

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

The Payout object

Create a payout

Update a payout

Retrieve a payout

List all payouts

Cancel a payout

Reverse a payout

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

Payouts

Ask about this section

Copy for LLM

View as Markdown

A

Payout

object is created when you receive funds from Stripe, or when you

initiate a payout to either a bank account or debit card of a

connected

Stripe account

. You can retrieve individual payouts,

and list all payouts. Payouts are made on

varying

schedules

, depending on your country and

industry.

Related guide:

Receiving payouts

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

payouts

POST

/

v1

/

payouts

/

:id

GET

/

v1

/

payouts

/

:id

GET

/

v1

/

payouts

POST

/

v1

/

payouts

/

:id

/

cancel

POST

/

v1

/

payouts

/

:id

/

reverse

The Payout object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

integer

The amount (in

cents

) that transfers to your bank account or debit card.

arrival

_

date

timestamp

Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

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

An arbitrary string attached to the object. Often useful for displaying to users.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

statement

_

descriptor

nullable

string

Extra information about a payout that displays on the user’s bank statement.

status

string

Current status of the payout:

paid

,

pending

,

in

_

transit

,

canceled

or

failed

. A payout is

pending

until it’s submitted to the bank, when it becomes

in

_

transit

. The status changes to

paid

if the transaction succeeds, or to

failed

or

canceled

(within 5 business days). Some payouts that fail might initially show as

paid

, then change to

failed

.

More attributes

Expand all

object

string

application

_

fee

nullable

string

Expandable

Connect only

application

_

fee

_

amount

nullable

integer

Connect only

automatic

boolean

balance

_

transaction

nullable

string

Expandable

created

timestamp

destination

nullable

string

Expandable

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

code

nullable

enum

failure

_

message

nullable

string

livemode

boolean

method

string

original

_

payout

nullable

string

Expandable

payout

_

method

nullable

string

reconciliation

_

status

enum

reversed

_

by

nullable

string

Expandable

source

_

type

string

trace

_

id

nullable

object

type

enum

The Payout object

{

"

id

"

:

"

po_1OaFDbEcg9tTZuTgNYmX0PKB

"

,

"

object

"

:

"

payout

"

,

"

amount

"

:

1100

,

"

arrival_date

"

:

1680652800

,

"

automatic

"

:

false

,

"

balance_transaction

"

:

"

txn_1OaFDcEcg9tTZuTgYMR25tSe

"

,

"

created

"

:

1680648691

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

description

"

:

null

,

"

destination

"

:

"

ba_1MtIhL2eZvKYlo2CAElKwKu2

"

,

"

failure_balance_transaction

"

:

null

,

"

failure_code

"

:

null

,

"

failure_message

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

metadata

"

:

{},

"

method

"

:

"

standard

"

,

"

original_payout

"

:

null

,

"

reconciliation_status

"

:

"

not_applicable

"

,

"

reversed_by

"

:

null

,

"

source_type

"

:

"

card

"

,

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

bank_account

"

}

Create a payout

Ask about this section

Copy for LLM

View as Markdown

To send funds to your own bank account, create a new payout object. Your

Stripe balance

must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.

If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.

If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The

balance object

details available and pending amounts by source type.

Parameters

amount

integer

Required

A positive integer in cents representing how much to payout.

currency

enum

Required

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

description

string

An arbitrary string attached to the object. Often useful for displaying to users.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

statement

_

descriptor

string

A string that displays on the recipient’s bank or card statement (up to 22 characters). A

statement

_

descriptor

that’s longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.

More parameters

Expand all

destination

string

method

string

payout

_

method

string

Preview feature

source

_

type

string

Returns

Returns a payout object if no initial errors are present during the payout creation (invalid routing number, insufficient funds, and so on). We initially mark the status of the payout object as

pending

.

POST

/

v1

/

payouts

curl

https://api.stripe.com/v1/payouts \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d amount=1100 \

-d currency=usd

Response

{

"

id

"

:

"

po_1OaFDbEcg9tTZuTgNYmX0PKB

"

,

"

object

"

:

"

payout

"

,

"

amount

"

:

1100

,

"

arrival_date

"

:

1680652800

,

"

automatic

"

:

false

,

"

balance_transaction

"

:

"

txn_1OaFDcEcg9tTZuTgYMR25tSe

"

,

"

created

"

:

1680648691

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

description

"

:

null

,

"

destination

"

:

"

ba_1MtIhL2eZvKYlo2CAElKwKu2

"

,

"

failure_balance_transaction

"

:

null

,

"

failure_code

"

:

null

,

"

failure_message

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

metadata

"

:

{},

"

method

"

:

"

standard

"

,

"

original_payout

"

:

null

,

"

reconciliation_status

"

:

"

not_applicable

"

,

"

reversed_by

"

:

null

,

"

source_type

"

:

"

card

"

,

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

bank_account

"

}

Update a payout

Ask about this section

Copy for LLM

View as Markdown

Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

Parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the payout object if the update succeeds. This call

raises

an error

if update parameters are invalid.

POST

/

v1

/

payouts

/

:id

curl

https://api.stripe.com/v1/payouts/

po_1OaFDbEcg9tTZuTgNYmX0PKB

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

po_1OaFDbEcg9tTZuTgNYmX0PKB

"

,

"

object

"

:

"

payout

"

,

"

amount

"

:

1100

,

"

arrival_date

"

:

1680652800

,

"

automatic

"

:

false

,

"

balance_transaction

"

:

"

txn_1OaFDcEcg9tTZuTgYMR25tSe

"

,

"

created

"

:

1680648691

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

description

"

:

null

,

"

destination

"

:

"

ba_1MtIhL2eZvKYlo2CAElKwKu2

"

,

"

failure_balance_transaction

"

:

null

,

"

failure_code

"

:

null

,

"

failure_message

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

method

"

:

"

standard

"

,

"

original_payout

"

:

null

,

"

reconciliation_status

"

:

"

not_applicable

"

,

"

reversed_by

"

:

null

,

"

source_type

"

:

"

card

"

,

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

bank_account

"

}

Retrieve a payout

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

Parameters

No

parameters

.

Returns

Returns a payout object if a you provide a valid identifier.

raises

An error

occurs otherwise.

GET

/

v1

/

payouts

/

:id

curl

https://api.stripe.com/v1/payouts/

po_1OaFDbEcg9tTZuTgNYmX0PKB

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

po_1OaFDbEcg9tTZuTgNYmX0PKB

"

,

"

object

"

:

"

payout

"

,

"

amount

"

:

1100

,

"

arrival_date

"

:

1680652800

,

"

automatic

"

:

false

,

"

balance_transaction

"

:

"

txn_1OaFDcEcg9tTZuTgYMR25tSe

"

,

"

created

"

:

1680648691

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

description

"

:

null

,

"

destination

"

:

"

ba_1MtIhL2eZvKYlo2CAElKwKu2

"

,

"

failure_balance_transaction

"

:

null

,

"

failure_code

"

:

null

,

"

failure_message

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

metadata

"

:

{},

"

method

"

:

"

standard

"

,

"

original_payout

"

:

null

,

"

reconciliation_status

"

:

"

not_applicable

"

,

"

reversed_by

"

:

null

,

"

source_type

"

:

"

card

"

,

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

bank_account

"

}
