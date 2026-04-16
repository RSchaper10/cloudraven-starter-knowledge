---
title: Cash Balance Transaction | Stripe API Reference
source_url: https://docs.stripe.com/api/cash_balance_transactions
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:38.529836+00:00
kind: extracted-doc
---

# Cash Balance Transaction | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/cash_balance_transactions

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:38.529836+00:00

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

- Cash Balance Transaction | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction The Cash Balance Transaction object Create or retrieve funding instructions for a customer cash balance Retrieve a cash balance transaction List cash balance transactions Fund a test mode cash balance Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Cash Balance Transaction Ask about this section Copy for LLM View as Markdown Customers with certain payments enabled have a cash balance, representing funds that were paid by the customer to a merchant, but have not yet been allocated to a payment.
- Cash Balance Transactions represent when funds are moved into or out of this balance.
- This includes funding by the customer, allocation to payments, and refunds to the customer.
- Yes No Endpoints POST / v1 / customers / :id / funding_instructions GET / v1 / customers / :id / cash_balance_transactions / :id GET / v1 / customers / :id / cash_balance_transactions POST / v1 / test_helpers / customers / :id / fund_cash_balance The Cash Balance Transaction object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- object string String representing the object’s type.

Extracted text:

Cash Balance Transaction | Stripe API Reference

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

The Cash Balance Transaction object

Create or retrieve funding instructions for a customer cash balance

Retrieve a cash balance transaction

List cash balance transactions

Fund a test mode cash balance

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

Cash Balance Transaction

Ask about this section

Copy for LLM

View as Markdown

Customers with certain payments enabled have a cash balance, representing funds that were paid

by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions

represent when funds are moved into or out of this balance. This includes funding by the customer, allocation

to payments, and refunds to the customer.

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

funding_instructions

GET

/

v1

/

customers

/

:id

/

cash_balance_transactions

/

:id

GET

/

v1

/

customers

/

:id

/

cash_balance_transactions

POST

/

v1

/

test_helpers

/

customers

/

:id

/

fund_cash_balance

The Cash Balance Transaction object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

object

string

String representing the object’s type. Objects of the same type share the same value.

adjusted

_

for

_

overdraft

nullable

object

If this is a

type=adjusted

_

for

_

overdraft

transaction, contains information about what caused the overdraft, which triggered this transaction.

Show child attributes

applied

_

to

_

payment

nullable

object

If this is a

type=applied

_

to

_

payment

transaction, contains information about how funds were applied.

Show child attributes

created

timestamp

Time at which the object was created. Measured in seconds since the Unix epoch.

currency

string

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

customer

string

Expandable

The customer whose available cash balance changed as a result of this transaction.

customer

_

account

nullable

string

The ID of an Account representing a customer whose available cash balance changed as a result of this transaction.

ending

_

balance

integer

The total available cash balance for the specified currency after this transaction was applied. Represented in the

smallest currency unit

.

funded

nullable

object

If this is a

type=funded

transaction, contains information about the funding.

Show child attributes

livemode

boolean

If the object exists in live mode, the value is

true

. If the object exists in test mode, the value is

false

.

net

_

amount

integer

The amount by which the cash balance changed, represented in the

smallest currency unit

. A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.

refunded

_

from

_

payment

nullable

object

If this is a

type=refunded

_

from

_

payment

transaction, contains information about the source of the refund.

Show child attributes

transferred

_

to

_

balance

nullable

object

If this is a

type=transferred

_

to

_

balance

transaction, contains the balance transaction linked to the transfer.

Show child attributes

type

enum

The type of the cash balance transaction. New types may be added in future. See

Customer Balance

to learn more about these types.

Possible enum values

adjusted

_

for

_

overdraft

A cash balance transaction type:

adjusted

_

for

_

overdraft

applied

_

to

_

payment

A cash balance transaction type:

applied

_

to

_

payment

funded

A cash balance transaction type:

funded

funding

_

reversed

A cash balance transaction type:

funding

_

reversed

refunded

_

from

_

payment

A cash balance transaction type:

refunded

_

from

_

payment

return

_

canceled

A cash balance transaction type:

return

_

canceled

return

_

initiated

A cash balance transaction type:

return

_

initiated

transferred

_

to

_

balance

A cash balance transaction type:

transferred

_

to

_

balance

unapplied

_

from

_

payment

A cash balance transaction type:

unapplied

_

from

_

payment

unapplied

_

from

_

payment

nullable

object

If this is a

type=unapplied

_

from

_

payment

transaction, contains information about how funds were unapplied.

Show child attributes

The Cash Balance Transaction object

{

"

id

"

:

"

ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF

"

,

"

object

"

:

"

customer_cash_balance_transaction

"

,

"

created

"

:

1690829143

,

"

currency

"

:

"

eur

"

,

"

customer

"

:

"

cus_9s6XKzkNRiz8i3

"

,

"

ending_balance

"

:

10000

,

"

funded

"

:

{

"

bank_transfer

"

:

{

"

eu_bank_transfer

"

:

{

"

bic

"

:

"

BANKDEAAXXX

"

,

"

iban_last4

"

:

"

7089

"

,

"

sender_name

"

:

"

Sample Business GmbH

"

},

"

reference

"

:

"

Payment for Invoice 28278FC-155

"

,

"

type

"

:

"

eu_bank_transfer

"

}

},

"

livemode

"

:

false

,

"

net_amount

"

:

5000

,

"

type

"

:

"

funded

"

}

Create or retrieve funding instructions for a customer cash balance

Ask about this section

Copy for LLM

View as Markdown

Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new

funding instructions will be created. If funding instructions have already been created for a given customer, the same

funding instructions will be retrieved. In other words, we will return the same funding instructions each time.

Parameters

bank

_

transfer

object

Required

Additional parameters for

bank

_

transfer

funding types

Show child parameters

currency

enum

Required

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

funding

_

type

enum

Required

The

funding

_

type

to get the instructions for.

Possible enum values

bank

_

transfer

Use a bank_transfer hash to define the bank transfer type

Returns

Returns funding instructions for a customer cash balance

POST

/

v1

/

customers

/

:id

/

funding_instructions

curl

https://api.stripe.com/v1/customers/

cus_9s6XKzkNRiz8i3

/funding_instructions \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d funding_type=bank_transfer \

-d currency=eur \

-d

"

bank_transfer[type]=eu_bank_transfer

"

\

-d

"

bank_transfer[eu_bank_transfer][country]=DE

"

Response

{

"

object

"

:

"

funding_instructions

"

,

"

bank_transfer

"

:

{

"

country

"

:

"

DE

"

,

"

financial_addresses

"

:

[

{

"

iban

"

:

{

"

account_holder_address

"

:

{

"

city

"

:

"

Dublin

"

,

"

country

"

:

"

IE

"

,

"

line1

"

:

"

Some address

"

,

"

line2

"

:

null

,

"

postal_code

"

:

"

D01H104

"

,

"

state

"

:

"

Dublin 1

"

},

"

account_holder_name

"

:

"

Merchant name

"

,

"

bank_address

"

:

{

"

city

"

:

"

Dublin

"

,

"

country

"

:

"

IE

"

,

"

line1

"

:

"

1 North Wall Quay

"

,

"

line2

"

:

null

,

"

postal_code

"

:

"

D01 T8Y1

"

,

"

state

"

:

"

Dublin

"

},

"

bic

"

:

"

SOGEDEFFXXX

"

,

"

country

"

:

"

DE

"

,

"

iban

"

:

"

DE006847740991234567890

"

},

"

supported_networks

"

:

[

"

sepa

"

,

"

swift

"

],

"

type

"

:

"

iban

"

}

],

"

type

"

:

"

eu_bank_transfer

"

},

"

currency

"

:

"

eur

"

,

"

funding_type

"

:

"

bank_transfer

"

,

"

livemode

"

:

false

}

Retrieve a cash balance transaction

Ask about this section

Copy for LLM

View as Markdown

Retrieves a specific cash balance transaction, which updated the customer’s

cash balance

.

Parameters

No

parameters

.

Returns

Returns a cash balance transaction object if a valid identifier was provided.

GET

/

v1

/

customers

/

:id

/

cash_balance_transactions

/

:id

curl

https://api.stripe.com/v1/customers/

cus_9s6XKzkNRiz8i3

/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \

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

ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF

"

,

"

object

"

:

"

customer_cash_balance_transaction

"

,

"

created

"

:

1690829143

,

"

currency

"

:

"

eur

"

,

"

customer

"

:

"

cus_9s6XKzkNRiz8i3

"

,

"

ending_balance

"

:

10000

,

"

funded

"

:

{

"

bank_transfer

"

:

{

"

eu_bank_transfer

"

:

{

"

bic

"

:

"

BANKDEAAXXX

"

,

"

iban_last4

"

:

"

7089

"

,

"

sender_name

"

:

"

Sample Business GmbH

"

},

"

reference

"

:

"

Payment for Invoice 28278FC-155

"

,

"

type

"

:

"

eu_bank_transfer

"

}

},

"

livemode

"

:

false

,

"

net_amount

"

:

5000

,

"

type

"

:

"

funded

"

}

List cash balance transactions

Ask about this section

Copy for LLM

View as Markdown

Returns a list of transactions that modified the customer’s

cash balance

.

Parameters

No

parameters

.

More parameters

Expand all

ending

_

before

string

limit

integer

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

cash balance transactions, starting after item

starting

_

after

. Each entry in the array is a separate cash balance transaction object. If no more items are available, the resulting array will be empty.

GET

/

v1

/

customers

/

:id

/

cash_balance_transactions

curl

-G https://api.stripe.com/v1/customers/

cus_9s6XKzkNRiz8i3

/cash_balance_transactions \

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

/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions

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

ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF

"

,

"

object

"

:

"

customer_cash_balance_transaction

"

,

"

created

"

:

1690829143

,

"

currency

"

:

"

eur

"

,

"

customer

"

:

"

cus_9s6XKzkNRiz8i3

"

,

"

ending_balance

"

:

10000

,

"

funded

"

:

{

"

bank_transfer

"

:

{

"

eu_bank_transfer

"

:

{

"

bic

"

:

"

BANKDEAAXXX

"

,

"

iban_last4

"

:

"

7089

"

,

"

sender_name

"

:

"

Sample Business GmbH

"

},

"

reference

"

:

"

Payment for Invoice 28278FC-155

"

,

"

type

"

:

"

eu_bank_transfer

"

}

},

"

livemode

"

:

false

,

"

net_amount

"

:

5000

,

"

type

"

:

"

funded

"

}

]

}
