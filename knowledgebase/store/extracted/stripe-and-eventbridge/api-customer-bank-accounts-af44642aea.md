---
title: Bank Accounts | Stripe API Reference
source_url: https://docs.stripe.com/api/customer_bank_accounts
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:36.762432+00:00
kind: extracted-doc
---

# Bank Accounts | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/customer_bank_accounts

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:36.762432+00:00

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

- Bank Accounts | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts The Bank Account object Create a bank account Update a bank account Retrieve a bank account List all bank accounts Delete a bank account Verify a bank account Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Bank Accounts Ask about this section Copy for LLM View as Markdown These bank accounts are payment methods on Customer objects.
- On the other hand External Accounts are transfer destinations on Account objects for connected accounts.
- They can be bank accounts or debit cards as well, and are documented in the links above.
- Related guide: Bank debits and transfers Was this section helpful?
- Yes No Endpoints POST / v1 / customers / :id / sources POST / v1 / customers / :id / sources / :id GET / v1 / customers / :id / bank_accounts / :id GET / v1 / customers / :id / bank_accounts DELETE / v1 / customers / :id / sources / :id POST / v1 / customers / :id / sources / :id / verify The Bank Account object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

Extracted text:

Bank Accounts | Stripe API Reference

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

The Bank Account object

Create a bank account

Update a bank account

Retrieve a bank account

List all bank accounts

Delete a bank account

Verify a bank account

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

Bank Accounts

Ask about this section

Copy for LLM

View as Markdown

These bank accounts are payment methods on

Customer

objects.

On the other hand

External Accounts

are transfer

destinations on

Account

objects for connected accounts.

They can be bank accounts or debit cards as well, and are documented in the links above.

Related guide:

Bank debits and transfers

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

sources

POST

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

GET

/

v1

/

customers

/

:id

/

bank_accounts

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

bank_accounts

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

POST

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

/

verify

The Bank Account object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

account

_

holder

_

name

nullable

string

The name of the person or business that owns the bank account.

account

_

holder

_

type

nullable

string

The type of entity that holds the account. This can be either

individual

or

company

.

bank

_

name

nullable

string

Name of the bank associated with the routing number (e.g.,

WELLS FARGO

).

country

string

Two-letter ISO code representing the country the bank account is located in.

currency

enum

Three-letter

ISO code for the currency

paid out to the bank account.

customer

nullable

string

Expandable

The ID of the customer that the bank account is associated with.

fingerprint

nullable

string

Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

last4

string

The last four digits of the bank account number.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

routing

_

number

nullable

string

The routing transit number for the bank account.

More attributes

Expand all

object

string

account

nullable

string

Expandable

Available conditionally

account

_

type

nullable

string

available

_

payout

_

methods

nullable

array of enums

status

string

The Bank Account object

{

"

id

"

:

"

ba_1MvoIJ2eZvKYlo2CO9f0MabO

"

,

"

object

"

:

"

bank_account

"

,

"

account_holder_name

"

:

"

Jane Austen

"

,

"

account_holder_type

"

:

"

company

"

,

"

account_type

"

:

null

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

country

"

:

"

US

"

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

customer

"

:

"

cus_9s6XI9OFIdpjIg

"

,

"

fingerprint

"

:

"

1JWtPxqbdX5Gamtc

"

,

"

last4

"

:

"

6789

"

,

"

metadata

"

:

{},

"

routing_number

"

:

"

110000000

"

,

"

status

"

:

"

new

"

}

Create a bank account

Ask about this section

Copy for LLM

View as Markdown

When you create a new bank account, you must specify a

Customer

object on which to create it.

Parameters

source

object | string

Required

Either a token, like the ones returned by

Stripe.js

, or a dictionary containing a user’s bank account details (with the options shown below).

Show child parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the bank account object.

POST

/

v1

/

customers

/

:id

/

sources

curl

https://api.stripe.com/v1/customers/

cus_9s6XI9OFIdpjIg

/sources \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d source=btok_1MvoS32eZvKYlo2CDhGTErAe

Response

{

"

id

"

:

"

ba_1MvoIJ2eZvKYlo2CO9f0MabO

"

,

"

object

"

:

"

bank_account

"

,

"

account_holder_name

"

:

"

Jane Austen

"

,

"

account_holder_type

"

:

"

company

"

,

"

account_type

"

:

null

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

country

"

:

"

US

"

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

customer

"

:

"

cus_9s6XI9OFIdpjIg

"

,

"

fingerprint

"

:

"

1JWtPxqbdX5Gamtc

"

,

"

last4

"

:

"

6789

"

,

"

metadata

"

:

{},

"

routing_number

"

:

"

110000000

"

,

"

status

"

:

"

new

"

}

Update a bank account

Ask about this section

Copy for LLM

View as Markdown

Updates the

account

_

holder

_

name

,

account

_

holder

_

type

, and

metadata

of a bank account belonging to a customer. Other bank account details are not editable, by design.

Parameters

account

_

holder

_

name

string

The name of the person or business that owns the bank account.

account

_

holder

_

type

string

The type of entity that holds the account. This can be either

individual

or

company

.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the bank account object.

POST

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

curl

https://api.stripe.com/v1/customers/

cus_9s6XI9OFIdpjIg

/sources/ba_1MvoIJ2eZvKYlo2CO9f0MabO \

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

ba_1MvoIJ2eZvKYlo2CO9f0MabO

"

,

"

object

"

:

"

bank_account

"

,

"

account_holder_name

"

:

"

Jane Austen

"

,

"

account_holder_type

"

:

"

company

"

,

"

account_type

"

:

null

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

country

"

:

"

US

"

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

customer

"

:

"

cus_9s6XI9OFIdpjIg

"

,

"

fingerprint

"

:

"

1JWtPxqbdX5Gamtc

"

,

"

last4

"

:

"

6789

"

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

routing_number

"

:

"

110000000

"

,

"

status

"

:

"

new

"

}

Retrieve a bank account

Ask about this section

Copy for LLM

View as Markdown

By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

Parameters

No

parameters

.

Returns

Returns the bank account object.

GET

/

v1

/

customers

/

:id

/

bank_accounts

/

:id

cURL

curl

https://api.stripe.com/v1/customers/

cus_9s6XI9OFIdpjIg

/bank_accounts/ba_1MvoIJ2eZvKYlo2CO9f0MabO \

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

ba_1MvoIJ2eZvKYlo2CO9f0MabO

"

,

"

object

"

:

"

bank_account

"

,

"

account_holder_name

"

:

"

Jane Austen

"

,

"

account_holder_type

"

:

"

company

"

,

"

account_type

"

:

null

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

country

"

:

"

US

"

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

customer

"

:

"

cus_9s6XI9OFIdpjIg

"

,

"

fingerprint

"

:

"

1JWtPxqbdX5Gamtc

"

,

"

last4

"

:

"

6789

"

,

"

metadata

"

:

{},

"

routing_number

"

:

"

110000000

"

,

"

status

"

:

"

new

"

}
