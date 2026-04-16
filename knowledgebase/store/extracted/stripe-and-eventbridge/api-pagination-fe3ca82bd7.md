# Pagination | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/pagination

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-15T19:48:06.041947+00:00

Direct links in scope:

- https://docs.stripe.com/api
- https://docs.stripe.com/api/authentication
- https://docs.stripe.com/api/errors
- https://docs.stripe.com/api/expanding_objects
- https://docs.stripe.com/api/idempotent_requests
- https://docs.stripe.com/api/include_dependent_response_values
- https://docs.stripe.com/api/metadata
- https://docs.stripe.com/api/pagination
- https://docs.stripe.com/api/pagination/search
- https://docs.stripe.com/api/pagination/auto
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

Captured summary:

- Pagination | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Search Auto-pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Pagination Ask about this section Copy for LLM View as Markdown All top-level API resources have support for bulk fetches through “list” API methods.
- For example, you can list charges , list customers , and list invoices .
- These list API methods share a common structure and accept, at a minimum, the following three parameters: limit , starting _ after , and ending _ before .
- Stripe’s list API methods use cursor-based pagination through the starting _ after and ending _ before parameters.
- Both parameters accept an existing object ID value (see below) and return objects in reverse chronological order.

Extracted text:

Pagination | Stripe API Reference

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

Search

Auto-pagination

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

Pagination

Ask about this section

Copy for LLM

View as Markdown

All top-level API resources have support for bulk fetches through “list” API methods. For example, you can

list charges

,

list customers

, and

list invoices

. These list API methods share a common structure and accept, at a minimum, the following three parameters:

limit

,

starting

_

after

, and

ending

_

before

.

Stripe’s list API methods use cursor-based

pagination

through the

starting

_

after

and

ending

_

before

parameters. Both parameters accept an existing object ID value (see below) and return objects in reverse chronological order. The

ending

_

before

parameter returns objects listed before the named object. The

starting

_

after

parameter returns objects listed after the named object. These parameters are mutually exclusive. You can use either the

starting

_

after

or

ending

_

before

parameter, but not both simultaneously.

Our client libraries offer

auto-pagination helpers

to traverse all pages of a list.

Parameters

limit

optional, default is 10

This specifies a limit on the number of objects to return, ranging between 1 and 100.

starting

_

after

optional object ID

A cursor to use in pagination.

starting

_

after

is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, ending with

obj

_

foo

, your subsequent call can include

starting

_

after=obj

_

foo

to fetch the next page of the list.

ending

_

before

optional object ID

A cursor to use in pagination.

ending

_

before

is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, starting with

obj

_

bar

, your subsequent call can include

ending

_

before=obj

_

bar

to fetch the previous page of the list.

List Response Format

object

string, value is "list"

A string that provides a description of the object type that returns.

data

array

An array containing the actual response elements, paginated by any request parameters.

has

_

more

boolean

Whether or not there are more elements available after this set. If

false

, this set comprises the end of the list.

url

url

The URL for accessing this list.

v2 API pagination

APIs within the

/v2

namespace contain a different

pagination

interface than the

v1

namespace.

Was this section helpful?

Yes

No

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

/v1/customers

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

cus_4QFJOjw2pOmAGJ

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1405641735

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

default_source

"

:

"

card_14HOpG2eZvKYlo2Cz4u5AJG5

"

,

"

delinquent

"

:

false

,

"

description

"

:

"

New customer

"

,

"

discount

"

:

null

,

"

email

"

:

null

,

"

invoice_prefix

"

:

"

7D11B54

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

name

"

:

"

cus_4QFJOjw2pOmAGJ

"

,

"

next_invoice_sequence

"

:

25

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

},

]

}

Search

Ask about this section

Copy for LLM

View as Markdown

Some top-level API resource have support for retrieval via “search” API methods. For example, you can

search charges

,

search customers

, and

search subscriptions

.

Stripe’s search API methods utilize cursor-based pagination via the

page

request parameter and

next

_

page

response parameter. For example, if you make a search request and receive

"next

_

page": "pagination

_

key"

in the response, your subsequent call can include

page=pagination

_

key

to fetch the next page of results.

Our client libraries offer

auto-pagination

helpers to easily traverse all pages of a search result.

Search request format

query

required

The search query string. See

search query language

.

limit

optional

A limit on the number of objects returned. Limit can range between 1 and 100, and the default is 10.

page

optional

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the

next

_

page

value returned in a previous response to request subsequent results.

Search response format

object

string, value is "search_result"

A string describing the object type returned.

url

string

The URL for accessing this list.

has

_

more

boolean

Whether or not there are more elements available after this set. If

false

, this set comprises the end of the list.

data

array

An array containing the actual response elements, paginated by any request parameters.

next

_

page

string

A cursor for use in pagination. If

has

_

more

is true, you can pass the value of

next

_

page

to a subsequent call to fetch the next page of results.

total

_

count

optional positive integer or zero

The total number of objects that match the query, only accurate up to 10,000. This field isn’t included by default. To include it in the response,

expand

the

total

_

count

field.

Was this section helpful?

Yes

No

Response

{

"

object

"

:

"

search_result

"

,

"

url

"

:

"

/v1/customers/search

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

cus_4QFJOjw2pOmAGJ

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1405641735

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

default_source

"

:

"

card_14HOpG2eZvKYlo2Cz4u5AJG5

"

,

"

delinquent

"

:

false

,

"

description

"

:

"

someone@example.com for Coderwall

"

,

"

discount

"

:

null

,

"

email

"

:

null

,

"

invoice_prefix

"

:

"

7D11B54

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

foo

"

:

"

bar

"

},

"

name

"

:

"

fakename

"

,

"

next_invoice_sequence

"

:

25

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

}

]

}

Auto-pagination

Ask about this section

Copy for LLM

View as Markdown

Our libraries support auto-pagination. This feature allows you to easily iterate through large lists of resources without having to manually perform the requests to fetch subsequent pages.

Was this section helpful?

Yes

No

# The auto-pagination feature is specific to Stripe's

# libraries and cannot be used directly with curl.

Request IDs

Ask about this section

Copy for LLM

View as Markdown

Each API request has an associated request identifier. You can find this value in the response headers, under

Request-Id

. You can also find request identifiers in the URLs of individual request logs in your

Dashboard

.

To expedite the resolution process, provide the request identifier when you contact us about a specific request.

Was this section helpful?

Yes

No

curl

https://api.stripe.com/v1/customers \

-u

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

: \

-D

"

-

"

\

-X POST

Connected Accounts

Ask about this section

Copy for LLM

View as Markdown

If you use Stripe

Connect

, you can issue requests on behalf of your

connected accounts

. To act as a connected account, include a

Stripe-Account

header containing the connected account ID, which typically starts with the

acct

_

prefix.

The connected account ID is set per-request. Methods on the returned object reuse the same account ID.

Related

guide

:

Making API calls for connected accounts

Was this section helpful?

Yes

No

Per-Request Account

curl

https://api.stripe.com/v1/charges/ch_3LmjFA2eZvKYlo2C09TLIsrw \

-u

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

: \

-H

"

Stripe-Account: acct_1032D82eZvKYlo2C

"

\

-G
