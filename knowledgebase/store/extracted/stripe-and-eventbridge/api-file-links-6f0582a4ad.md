---
title: File Links | Stripe API Reference
source_url: https://docs.stripe.com/api/file_links
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:19.928244+00:00
kind: extracted-doc
---

# File Links | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/file_links

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:19.928244+00:00

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

- File Links | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links The File Link object Create a file link Update a file link Retrieve a file link List all file links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks File Links Ask about this section Copy for LLM View as Markdown To share the contents of a File object with non-Stripe users, you can create a FileLink .
- FileLink s contain a URL that you can use to retrieve the contents of the file without authentication.
- Yes No Endpoints POST / v1 / file_links POST / v1 / file_links / :id GET / v1 / file_links / :id GET / v1 / file_links The File Link object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- expires _ at nullable timestamp Time that the link expires.
- file string Expandable The file object this link points to.

Extracted text:

File Links | Stripe API Reference

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

The File Link object

Create a file link

Update a file link

Retrieve a file link

List all file links

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

File Links

Ask about this section

Copy for LLM

View as Markdown

To share the contents of a

File

object with non-Stripe users, you can

create a

FileLink

.

FileLink

s contain a URL that you can use to

retrieve the contents of the file without authentication.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

file_links

POST

/

v1

/

file_links

/

:id

GET

/

v1

/

file_links

/

:id

GET

/

v1

/

file_links

The File Link object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

expires

_

at

nullable

timestamp

Time that the link expires.

file

string

Expandable

The file object this link points to.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

url

nullable

string

The publicly accessible URL to download the file.

More attributes

Expand all

object

string

created

timestamp

expired

boolean

livemode

boolean

The File Link object

{

"

id

"

:

"

link_1Mr23jLkdIwHu7ix65betcoo

"

,

"

object

"

:

"

file_link

"

,

"

created

"

:

1680108075

,

"

expired

"

:

false

,

"

expires_at

"

:

null

,

"

file

"

:

"

file_1Mr23iLkdIwHu7ixQkCV3CBR

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

url

"

:

"

https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h

"

}

Create a file link

Ask about this section

Copy for LLM

View as Markdown

Creates a new file link object.

Parameters

file

string

Required

The ID of the file. The file’s

purpose

must be one of the following:

business

_

icon

,

business

_

logo

,

customer

_

signature

,

dispute

_

evidence

,

finance

_

report

_

run

,

financial

_

account

_

statement

,

identity

_

document

_

downloadable

,

issuing

_

regulatory

_

reporting

,

pci

_

document

,

selfie

,

sigma

_

scheduled

_

query

,

tax

_

document

_

user

_

upload

,

terminal

_

android

_

apk

, or

terminal

_

reader

_

splashscreen

.

expires

_

at

timestamp

The link isn’t usable after this future timestamp.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the file link object if successful and

raises

an error

otherwise.

POST

/

v1

/

file_links

curl

https://api.stripe.com/v1/file_links \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d file=file_1Mr23iLkdIwHu7ixQkCV3CBR

Response

{

"

id

"

:

"

link_1Mr23jLkdIwHu7ix65betcoo

"

,

"

object

"

:

"

file_link

"

,

"

created

"

:

1680108075

,

"

expired

"

:

false

,

"

expires_at

"

:

null

,

"

file

"

:

"

file_1Mr23iLkdIwHu7ixQkCV3CBR

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

url

"

:

"

https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h

"

}

Update a file link

Ask about this section

Copy for LLM

View as Markdown

Updates an existing file link object. Expired links can no longer be updated.

Parameters

expires

_

at

string | timestamp

A future timestamp after which the link will no longer be usable, or

now

to expire the link immediately.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the file link object if successful, and

raises

an error

otherwise.

POST

/

v1

/

file_links

/

:id

curl

https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \

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

link_1Mr23jLkdIwHu7ix65betcoo

"

,

"

object

"

:

"

file_link

"

,

"

created

"

:

1680108075

,

"

expired

"

:

false

,

"

expires_at

"

:

null

,

"

file

"

:

"

file_1Mr23iLkdIwHu7ixQkCV3CBR

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

url

"

:

"

https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h

"

}

Retrieve a file link

Ask about this section

Copy for LLM

View as Markdown

Retrieves the file link with the given ID.

Parameters

No

parameters

.

Returns

If the identifier you provide is valid, a file link object returns. If not, Stripe

raises

an error

.

GET

/

v1

/

file_links

/

:id

curl

https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \

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

link_1Mr23jLkdIwHu7ix65betcoo

"

,

"

object

"

:

"

file_link

"

,

"

created

"

:

1680108075

,

"

expired

"

:

false

,

"

expires_at

"

:

null

,

"

file

"

:

"

file_1Mr23iLkdIwHu7ixQkCV3CBR

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

url

"

:

"

https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h

"

}
