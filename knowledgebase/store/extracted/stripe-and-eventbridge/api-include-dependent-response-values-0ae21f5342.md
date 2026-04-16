# Include-dependent response values (API v2) | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/include_dependent_response_values

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-15T19:48:03.956679+00:00

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

- Include-dependent response values (API v2) | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Include-dependent response values (API v2) Ask about this section Copy for LLM View as Markdown Some API v2 responses contain null values for certain properties by default, regardless of their actual values.
- That reduces the size of response payloads while maintaining the basic response structure.
- To retrieve the actual values for those properties, specify them in the include array request parameter.
- To determine whether you need to use the include parameter in a given request, look at the request description.
- The include parameter’s enum values represent the response properties that depend on the include parameter.

Extracted text:

Include-dependent response values (API v2) | Stripe API Reference

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

Include-dependent response values (API v2)

Ask about this section

Copy for LLM

View as Markdown

Some API v2 responses contain null values for certain properties by default, regardless of their actual values. That reduces the size of response payloads while maintaining the basic response structure. To retrieve the actual values for those properties, specify them in the

include

array request parameter.

To determine whether you need to use the

include

parameter in a given request, look at the request description. The

include

parameter’s enum values represent the response properties that depend on the

include

parameter.

Note

Whether a response property defaults to null depends on the request endpoint, not the object that the endpoint references. If multiple endpoints return data from the same object, a particular property can depend on

include

in one endpoint and return its actual value by default for a different endpoint.

A hash property can depend on a single

include

value, or on multiple

include

values associated with its child properties. For example, when updating an Account, to return actual values for the entire

identity

hash, specify

identity

in the

include

parameter. Otherwise, the

identity

hash is null in the response. However, to return actual values for the

configuration

hash, you must specify individual configurations in the request. If you specify at least one configuration, but not all of them, specified configurations return actual values and unspecified configurations return null. If you don’t specify any configurations, the

configuration

hash is null in the response.

Related

guide

:

Include-dependent response values

POST

/

v2

/

core

/

accounts

curl

-X POST https://api.stripe.com/v2/core/accounts \

-H

"

Authorization: Bearer

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.preview

"

\

--json

'

{

"include": [

"identity",

"configuration.customer"

]

}

'

Included response properties

The response includes actual values for the properties specified in the

include

parameter, and null for all other include-dependent properties.

Response

{

"

id

"

:

"

acct_123

"

,

"

object

"

:

"

v2.core.account

"

,

"

applied_configurations

"

:

[

"

customer

"

,

"

merchant

"

],

"

configuration

"

:

{

"

customer

"

:

{

"

automatic_indirect_tax

"

:

{

...

},

"

billing

"

:

{

...

},

"

capabilities

"

:

{

...

},

...

},

"

merchant

"

:

null

,

"

recipient

"

:

null

},

"

contact_email

"

:

"

furever@example.com

"

,

"

created

"

:

"

2025-06-09T21:16:03.000Z

"

,

"

dashboard

"

:

"

full

"

,

"

defaults

"

:

null

,

"

display_name

"

:

"

Furever

"

,

"

identity

"

:

{

"

business_details

"

:

{

"

doing_business_as

"

:

"

FurEver

"

,

"

id_numbers

"

:

[

{

"

type

"

:

"

us_ein

"

}

],

"

product_description

"

:

"

Saas pet grooming platform at furever.dev using Connect embedded components

"

,

"

structure

"

:

"

sole_proprietorship

"

,

"

url

"

:

"

http://accessible.stripe.com

"

},

"

country

"

:

"

US

"

},

"

livemode

"

:

true

,

"

metadata

"

:

{},

"

requirements

"

:

null

}

Metadata

Ask about this section

Copy for LLM

View as Markdown

Updateable Stripe objects—including

Account

,

Charge

,

Customer

,

PaymentIntent

,

Refund

,

Subscription

, and

Transfer

have a

metadata

parameter. You can use this parameter to attach key-value data to these Stripe objects.

You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Keys and values are stored as strings and can contain any characters with one exception: you can’t use square brackets ([ and ]) in keys.

You can use metadata to store additional, structured information on an object. For example, you could store your user’s full name and corresponding unique identifier from your system on a Stripe

Customer

object. Stripe doesn’t use metadata—for example, we don’t use it to authorize or decline a charge and it won’t be seen by your users unless you choose to show it to them.

Some of the objects listed above also support a

description

parameter. You can use the

description

parameter to annotate a charge-for example, a human-readable description such as

2 shirts for test@example

.

com

. Unlike

metadata

,

description

is a single string, which your users might see (for example, in email receipts Stripe sends on your behalf).

Don’t store any sensitive information (bank account numbers, card details, and so on) as metadata or in the

description

parameter.

Related

guide

:

Metadata

Sample metadata use cases

Link IDs

: Attach your system’s unique IDs to a Stripe object to simplify lookups. For example, add your order number to a charge, your user ID to a customer or recipient, or a unique receipt number to a transfer.

Refund papertrails

: Store information about the reason for a refund and the individual responsible for its creation.

Customer details

: Annotate a customer by storing an internal ID for your future use.

Was this section helpful?

Yes

No

POST

/

v1

/

customers

curl

https://api.stripe.com/v1/customers \

-u

"

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

:

"

\

-d

"

metadata[order_id]=6735

"

{

"

id

"

:

"

cus_123456789

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

{

"

city

"

:

"

city

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

line1

"

:

"

line 1

"

,

"

line2

"

:

"

line 2

"

,

"

postal_code

"

:

"

90210

"

,

"

state

"

:

"

CA

"

},

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

1483565364

,

"

currency

"

:

null

,

"

default_source

"

:

null

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

null

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

C11F7E1

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

null

,

"

next_invoice_sequence

"

:

1

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

}

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
