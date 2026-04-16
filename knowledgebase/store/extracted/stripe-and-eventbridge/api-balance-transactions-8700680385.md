---
title: Balance Transactions | Stripe API Reference
source_url: https://docs.stripe.com/api/balance_transactions
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:03.180593+00:00
kind: extracted-doc
---

# Balance Transactions | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/balance_transactions

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:03.180593+00:00

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
- https://docs.stripe.com/api/balance_transactions/object
- https://docs.stripe.com/api/balance_transactions/retrieve
- https://docs.stripe.com/api/balance_transactions/list
- https://docs.stripe.com/api/charges

Captured summary:

- Balance Transactions | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions The Balance Transaction object Retrieve a balance transaction List all balance transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Balance Transactions Ask about this section Copy for LLM View as Markdown Balance transactions represent funds moving through your Stripe account.
- Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.
- Related guide: Balance transaction types Was this section helpful?
- Yes No Endpoints GET / v1 / balance_transactions / :id GET / v1 / balance_transactions The Balance Transaction object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- amount integer Gross amount of this transaction (in cents ).

Extracted text:

Balance Transactions | Stripe API Reference

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

The Balance Transaction object

Retrieve a balance transaction

List all balance transactions

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

Balance Transactions

Ask about this section

Copy for LLM

View as Markdown

Balance transactions represent funds moving through your Stripe account.

Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

Related guide:

Balance transaction types

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

balance_transactions

/

:id

GET

/

v1

/

balance_transactions

The Balance Transaction object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

integer

Gross amount of this transaction (in

cents

). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.

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

fee

integer

Fees (in

cents

) paid for this transaction. Represented as a positive integer when assessed.

fee

_

details

array of objects

Detailed breakdown of fees (in

cents

) paid for this transaction.

Show child attributes

net

integer

Net impact to a Stripe balance (in

cents

). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by

amount

-

fee

source

nullable

string

Expandable

This transaction relates to the Stripe object.

status

string

The transaction’s net funds status in the Stripe balance, which are either

available

or

pending

.

type

enum

Transaction type:

adjustment

,

advance

,

advance

_

funding

,

anticipation

_

repayment

,

application

_

fee

,

application

_

fee

_

refund

,

charge

,

climate

_

order

_

purchase

,

climate

_

order

_

refund

,

connect

_

collection

_

transfer

,

contribution

,

issuing

_

authorization

_

hold

,

issuing

_

authorization

_

release

,

issuing

_

dispute

,

issuing

_

transaction

,

obligation

_

outbound

,

obligation

_

reversal

_

inbound

,

payment

,

payment

_

failure

_

refund

,

payment

_

network

_

reserve

_

hold

,

payment

_

network

_

reserve

_

release

,

payment

_

refund

,

payment

_

reversal

,

payment

_

unreconciled

,

payout

,

payout

_

cancel

,

payout

_

failure

,

payout

_

minimum

_

balance

_

hold

,

payout

_

minimum

_

balance

_

release

,

refund

,

refund

_

failure

,

reserve

_

transaction

,

reserved

_

funds

,

reserve

_

hold

,

reserve

_

release

,

stripe

_

fee

,

stripe

_

fx

_

fee

,

stripe

_

balance

_

payment

_

debit

,

stripe

_

balance

_

payment

_

debit

_

reversal

,

tax

_

fee

,

topup

,

topup

_

reversal

,

transfer

,

transfer

_

cancel

,

transfer

_

failure

,

transfer

_

refund

, or

fee

_

credit

_

funding

. Learn more about

balance transaction types and what they represent

. To classify transactions for accounting purposes, consider

reporting

_

category

instead.

Possible enum values

adjustment

advance

advance

_

funding

anticipation

_

repayment

application

_

fee

application

_

fee

_

refund

charge

climate

_

order

_

purchase

climate

_

order

_

refund

connect

_

collection

_

transfer

Show 37 more

More attributes

Expand all

object

string

available

_

on

timestamp

balance

_

type

enum

created

timestamp

exchange

_

rate

nullable

float

reporting

_

category

string

The Balance Transaction object

{

"

id

"

:

"

txn_1MiN3gLkdIwHu7ixxapQrznl

"

,

"

object

"

:

"

balance_transaction

"

,

"

amount

"

:

-400

,

"

available_on

"

:

1678043844

,

"

created

"

:

1678043844

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

exchange_rate

"

:

null

,

"

fee

"

:

0

,

"

fee_details

"

:

[],

"

net

"

:

-400

,

"

reporting_category

"

:

"

transfer

"

,

"

source

"

:

"

tr_1MiN3gLkdIwHu7ixNCZvFdgA

"

,

"

status

"

:

"

available

"

,

"

type

"

:

"

transfer

"

}

Retrieve a balance transaction

Ask about this section

Copy for LLM

View as Markdown

Retrieves the balance transaction with the given ID.

Note that this endpoint previously used the path

/v1/balance/history/:id

.

Parameters

No

parameters

.

Returns

Returns a balance transaction if a valid balance transaction ID was provided.

Raises

an error

otherwise.

GET

/

v1

/

balance_transactions

/

:id

curl

https://api.stripe.com/v1/balance_transactions/txn_1MiN3gLkdIwHu7ixxapQrznl \

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

txn_1MiN3gLkdIwHu7ixxapQrznl

"

,

"

object

"

:

"

balance_transaction

"

,

"

amount

"

:

-400

,

"

available_on

"

:

1678043844

,

"

created

"

:

1678043844

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

exchange_rate

"

:

null

,

"

fee

"

:

0

,

"

fee_details

"

:

[],

"

net

"

:

-400

,

"

reporting_category

"

:

"

transfer

"

,

"

source

"

:

"

tr_1MiN3gLkdIwHu7ixNCZvFdgA

"

,

"

status

"

:

"

available

"

,

"

type

"

:

"

transfer

"

}

List all balance transactions

Ask about this section

Copy for LLM

View as Markdown

Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

Note that this endpoint was previously called “Balance history” and used the path

/v1/balance/history

.

Parameters

payout

string

For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.

type

string

Only returns transactions of the given type. One of:

adjustment

,

advance

,

advance

_

funding

,

anticipation

_

repayment

,

application

_

fee

,

application

_

fee

_

refund

,

charge

,

climate

_

order

_

purchase

,

climate

_

order

_

refund

,

connect

_

collection

_

transfer

,

contribution

,

issuing

_

authorization

_

hold

,

issuing

_

authorization

_

release

,

issuing

_

dispute

,

issuing

_

transaction

,

obligation

_

outbound

,

obligation

_

reversal

_

inbound

,

payment

,

payment

_

failure

_

refund

,

payment

_

network

_

reserve

_

hold

,

payment

_

network

_

reserve

_

release

,

payment

_

refund

,

payment

_

reversal

,

payment

_

unreconciled

,

payout

,

payout

_

cancel

,

payout

_

failure

,

payout

_

minimum

_

balance

_

hold

,

payout

_

minimum

_

balance

_

release

,

refund

,

refund

_

failure

,

reserve

_

transaction

,

reserved

_

funds

,

reserve

_

hold

,

reserve

_

release

,

stripe

_

fee

,

stripe

_

fx

_

fee

,

stripe

_

balance

_

payment

_

debit

,

stripe

_

balance

_

payment

_

debit

_

reversal

,

tax

_

fee

,

topup

,

topup

_

reversal

,

transfer

,

transfer

_

cancel

,

transfer

_

failure

,

transfer

_

refund

, or

fee

_

credit

_

funding

.

More parameters

Expand all

created

object

currency

enum

ending

_

before

string

limit

integer

source

string

starting

_

after

string

Returns

A

dictionary

with a

data

property that contains an array of up to

limit

transactions, starting after transaction

starting

_

after

. Each entry in the array is a separate transaction history object. If no more transactions are available, the resulting array will be empty.

GET

/

v1

/

balance_transactions

curl

-G https://api.stripe.com/v1/balance_transactions \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d limit=3

Response

{

"

object

"

:

"

list

"

,

"

url

"

:

"

/v1/balance_transactions

"

,

"

has_more

"

:

false

,

"

data

"

:

[

{

"

id

"

:

"

txn_1MiN3gLkdIwHu7ixxapQrznl

"

,

"

object

"

:

"

balance_transaction

"

,

"

amount

"

:

-400

,

"

available_on

"

:

1678043844

,

"

created

"

:

1678043844

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

exchange_rate

"

:

null

,

"

fee

"

:

0

,

"

fee_details

"

:

[],

"

net

"

:

-400

,

"

reporting_category

"

:

"

transfer

"

,

"

source

"

:

"

tr_1MiN3gLkdIwHu7ixNCZvFdgA

"

,

"

status

"

:

"

available

"

,

"

type

"

:

"

transfer

"

}

]

}
