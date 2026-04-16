# Errors | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/errors

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-15T19:48:00.934465+00:00

Direct links in scope:

- https://docs.stripe.com/api
- https://docs.stripe.com/api/authentication
- https://docs.stripe.com/api/errors
- https://docs.stripe.com/api/errors/handling
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

Captured summary:

- Errors | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Handling errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Errors Ask about this section Copy for LLM View as Markdown Stripe uses conventional HTTP response codes to indicate the success or failure of an API request.
- In general: Codes in the 2xx range indicate success.
- Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.).
- Codes in the 5xx range indicate an error with Stripe’s servers (these are rare).
- Some 4xx errors that could be handled programmatically (e.g., a card is declined ) include an error code that briefly explains the error reported.

Extracted text:

Errors | Stripe API Reference

Find anything

/

Ask AI

Introduction

Authentication

Errors

Handling errors

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

Errors

Ask about this section

Copy for LLM

View as Markdown

Stripe uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the

2xx

range indicate success. Codes in the

4xx

range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the

5xx

range indicate an error with Stripe’s servers (these are rare).

Some

4xx

errors that could be handled programmatically (e.g., a card is

declined

) include an

error code

that briefly explains the error reported.

Was this section helpful?

Yes

No

Attributes

code

nullable

string

For some errors that could be handled programmatically, a short string indicating the

error code

reported.

decline

_

code

nullable

string

For card errors resulting from a card issuer decline, a short string indicating the

card issuer’s reason for the decline

if they provide one.

message

nullable

string

A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.

param

nullable

string

If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.

payment

_

intent

nullable

object

The

PaymentIntent object

for errors returned on a request involving a PaymentIntent.

type

enum

The type of error returned. One of

api

_

error

,

card

_

error

,

idempotency

_

error

, or

invalid

_

request

_

error

Possible enum values

api

_

error

card

_

error

idempotency

_

error

invalid

_

request

_

error

More

Expand all

advice

_

code

nullable

string

charge

nullable

string

doc

_

url

nullable

string

network

_

advice

_

code

nullable

string

network

_

decline

_

code

nullable

string

payment

_

method

nullable

object

payment

_

method

_

type

nullable

string

request

_

log

_

url

nullable

string

setup

_

intent

nullable

object

source

nullable

object

HTTP Status Code Summary

200

OK

Everything worked as expected.

400

Bad Request

The request was unacceptable, often due to missing a required parameter.

401

Unauthorized

No valid API key provided.

402

Request Failed

The parameters were valid but the request failed.

403

Forbidden

The API key doesn’t have permissions to perform the request.

404

Not Found

The requested resource doesn’t exist.

409

Conflict

The request conflicts with another request (perhaps due to using the same idempotent key).

424

External Dependency Failed

The request couldn’t be completed due to a failure in a dependency external to Stripe.

429

Too Many Requests

Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.

500, 502, 503, 504

Server Errors

Something went wrong on Stripe’s end. (These are rare.)

Error Types

api

_

error

API errors cover any other type of problem (e.g., a temporary problem with Stripe’s servers), and are extremely uncommon.

card

_

error

Card errors are the most common type of error you should expect to handle. They result when the user enters a card that can’t be charged for some reason.

idempotency

_

error

Idempotency errors occur when an

Idempotency-Key

is re-used on a request that does not match the first request’s API endpoint and parameters.

invalid

_

request

_

error

Invalid request errors arise when your request has invalid parameters.

Handling errors

Ask about this section

Copy for LLM

View as Markdown

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

Related

guide

:

Error Handling

# Select a client library to see examples of

# handling different kinds of errors.

Expanding Responses

Ask about this section

Copy for LLM

View as Markdown

Many objects allow you to request additional information as an expanded response by using the

expand

request parameter. This parameter is available on all API requests, and applies to the response of that request only. You can expand responses in two ways.

In many cases, an object contains the ID of a related object in its response properties. For example, a

Charge

might have an associated Customer ID. You can expand these objects in line with the expand request parameter. The

expandable

label in this documentation indicates ID fields that you can expand into objects.

Some available fields aren’t included in the responses by default, such as the

number

and

cvc

fields for the Issuing Card object. You can request these fields as an expanded response by using the

expand

request parameter.

You can expand recursively by specifying nested fields after a dot (

.

). For example, requesting

payment

_

intent

.

customer

on a charge expands the

payment

_

intent

property into a full PaymentIntent object, then expands the

customer

property on that payment intent into a full Customer object.

You can use the

expand

parameter on any endpoint that returns expandable fields, including list, create, and update endpoints.

Expansions on list requests start with the

data

property. For example, you can expand

data

.

customers

on a request to list charges and associated customers. Performing deep expansions on numerous list requests might result in slower processing times.

Expansions have a maximum depth of four levels (for example, the deepest expansion allowed when listing charges is

data

.

payment

_

intent

.

customer

.

default

_

source

).

You can expand multiple objects at the same time by identifying multiple items in the

expand

array.

Related

guide

:

Expanding responses

Related

video

:

Expand

Was this section helpful?

Yes

No

curl

https://api.stripe.com/v1/charges/ch_3LmzzQ2eZvKYlo2C0XjzUzJV \

-u

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

: \

-d

"

expand[]

"

=customer \

-d

"

expand[]

"

=

"

payment_intent.customer

"

\

-G

Response

{

"

id

"

:

"

ch_3LmzzQ2eZvKYlo2C0XjzUzJV

"

,

"

object

"

:

"

charge

"

,

"

customer

"

:

{

"

id

"

:

"

cu_14HOpH2eZvKYlo2CxXIM7Pb2

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

// ...

},

"

payment_intent

"

:

{

"

id

"

:

"

pi_3MtwBwLkdIwHu7ix28a3tqPa

"

,

"

object

"

:

"

payment_intent

"

,

"

customer

"

:

{

"

id

"

:

"

cus_NffrFeUfNV2Hib

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

// ...

},

// ...

},

// ...

}

Idempotent requests

Ask about this section

Copy for LLM

View as Markdown

The API supports

idempotency

for safely retrying requests without accidentally performing the same operation twice. When creating or updating an object, use an idempotency key. Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice.

To perform an idempotent request, provide an additional

IdempotencyKey

element to the request options.

Stripe’s idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeds or fails. Subsequent requests with the same key return the same result, including

500

errors.

A client generates an idempotency key, which is a unique key that the server uses to recognize subsequent retries of the same request. How you create unique keys is up to you, but we suggest using V4 UUIDs, or another random string with enough entropy to avoid collisions. Idempotency keys are up to 255 characters long. Avoid using sensitive data (for example, email addresses or personal identifiers) as idempotency keys.

You can remove keys from the system automatically after they’re at least 24 hours old. We generate a new request if a key is reused after the original is pruned. The idempotency layer compares incoming parameters to those of the original request and errors if they’re not the same to prevent accidental misuse.

We save results only after the execution of an endpoint begins. If incoming parameters fail validation, or the request conflicts with another request that’s executing concurrently, we don’t save the idempotent result because no API endpoint initiates the execution. You can retry these requests. Learn more about when you can

retry idempotent requests

.

All

POST

requests accept idempotency keys. Don’t send idempotency keys in

GET

and

DELETE

requests because it has no effect. These requests are idempotent by definition.

Was this section helpful?

Yes

No

curl

https://api.stripe.com/v1/customers \

-u

[REDACTED_SECRET]...2HlWgH4olfQ2

[REDACTED_SECRET]

: \

-H

"

Idempotency-Key: KG5LxwFBepaKHyUD

"

\

-d description=

"

My First Test Customer (created for API docs at https://docs.stripe.com/api)

"

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
