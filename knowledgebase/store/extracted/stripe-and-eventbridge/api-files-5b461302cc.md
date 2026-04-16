---
title: Files | Stripe API Reference
source_url: https://docs.stripe.com/api/files
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:18.994659+00:00
kind: extracted-doc
---

# Files | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/files

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:18.994659+00:00

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

- Files | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files The File object Create a file Retrieve a file List all files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Files Ask about this section Copy for LLM View as Markdown This object represents files hosted on Stripe’s servers.
- You can upload files with the create file request (for example, when uploading dispute evidence).
- Stripe also creates files independently (for example, the results of a Sigma scheduled query ).
- Related guide: File upload guide Was this section helpful?
- Yes No Endpoints POST / v1 / files GET / v1 / files / :id GET / v1 / files The File object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

Extracted text:

Files | Stripe API Reference

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

The File object

Create a file

Retrieve a file

List all files

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

Files

Ask about this section

Copy for LLM

View as Markdown

This object represents files hosted on Stripe’s servers. You can upload

files with the

create file

request

(for example, when uploading dispute evidence). Stripe also

creates files independently (for example, the results of a

Sigma scheduled

query

).

Related guide:

File upload guide

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

files

GET

/

v1

/

files

/

:id

GET

/

v1

/

files

The File object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

purpose

enum

The

purpose

of the uploaded file.

Possible enum values

account

_

requirement

Additional documentation requirements that can be requested for an account.

additional

_

verification

Additional verification for custom accounts.

business

_

icon

A business icon.

business

_

logo

A business logo.

customer

_

signature

Customer signature image.

dispute

_

evidence

Evidence to submit with a dispute response.

finance

_

report

_

run

User-accessible copies of query results from the Reporting dataset.

financial

_

account

_

statement

Financial account statements.

identity

_

document

A document to verify the identity of an account owner during account provisioning.

identity

_

document

_

downloadable

Image of a document collected by Stripe Identity.

Show 10 more

type

nullable

string

The returned file type (for example,

csv

,

pdf

,

jpg

, or

png

).

More attributes

Expand all

object

string

created

timestamp

expires

_

at

nullable

timestamp

filename

nullable

string

links

nullable

object

size

integer

title

nullable

string

url

nullable

string

The File object

{

"

id

"

:

"

file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

,

"

object

"

:

"

file

"

,

"

created

"

:

1680116847

,

"

expires_at

"

:

1703444847

,

"

filename

"

:

"

file.png

"

,

"

links

"

:

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

data

"

:

[],

"

has_more

"

:

false

,

"

url

"

:

"

/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

},

"

purpose

"

:

"

dispute_evidence

"

,

"

size

"

:

8429

,

"

title

"

:

null

,

"

type

"

:

"

png

"

,

"

url

"

:

"

https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents

"

}

Create a file

Ask about this section

Copy for LLM

View as Markdown

To upload a file to Stripe, you need to send a request of type

multipart/form-data

. Include the file you want to upload in the request, and the parameters for creating a file.

All of Stripe’s officially supported Client libraries support sending

multipart/form-data

.

Parameters

file

object

Required

A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the

multipart/form-data

protocol.

purpose

enum

Required

The

purpose

of the uploaded file.

Possible enum values

account

_

requirement

Additional documentation requirements that can be requested for an account.

additional

_

verification

Additional verification for custom accounts.

business

_

icon

A business icon.

business

_

logo

A business logo.

customer

_

signature

Customer signature image.

dispute

_

evidence

Evidence to submit with a dispute response.

identity

_

document

A document to verify the identity of an account owner during account provisioning.

issuing

_

regulatory

_

reporting

Additional regulatory reporting requirements for Issuing.

pci

_

document

A self-assessment PCI questionnaire.

platform

_

terms

_

of

_

service

A copy of the platform’s Terms of Service.

Show 5 more

More parameters

Expand all

file

_

link

_

data

object

Returns

Returns the file object.

POST

/

v1

/

files

curl

https://files.stripe.com/v1/files \

-u

[REDACTED_SECRET]

[REDACTED_SECRET]

: \

-F purpose=dispute_evidence \

-F file=

"

@/path/to/a/file.jpg

"

Response

{

"

id

"

:

"

file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

,

"

object

"

:

"

file

"

,

"

created

"

:

1680116847

,

"

expires_at

"

:

1703444847

,

"

filename

"

:

"

file.png

"

,

"

links

"

:

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

data

"

:

[],

"

has_more

"

:

false

,

"

url

"

:

"

/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

},

"

purpose

"

:

"

dispute_evidence

"

,

"

size

"

:

8429

,

"

title

"

:

null

,

"

type

"

:

"

png

"

,

"

url

"

:

"

https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents

"

}

Retrieve a file

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to

access file contents

.

Parameters

No

parameters

.

Returns

If the identifier you provide is valid, a file object returns. If not, Stripe

raises

an error

.

GET

/

v1

/

files

/

:id

curl

https://api.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH \

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

file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

,

"

object

"

:

"

file

"

,

"

created

"

:

1680116847

,

"

expires_at

"

:

1703444847

,

"

filename

"

:

"

file.png

"

,

"

links

"

:

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

data

"

:

[],

"

has_more

"

:

false

,

"

url

"

:

"

/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

},

"

purpose

"

:

"

dispute_evidence

"

,

"

size

"

:

8429

,

"

title

"

:

null

,

"

type

"

:

"

png

"

,

"

url

"

:

"

https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents

"

}

List all files

Ask about this section

Copy for LLM

View as Markdown

Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.

Parameters

purpose

string

Filter queries by the file purpose. If you don’t provide a purpose, the queries return unfiltered files.

More parameters

Expand all

created

object

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

files, starting after the

starting

_

after

file. Each entry in the array is a separate file object. If there aren’t additional available files, the resulting array is empty.

GET

/

v1

/

files

curl

-G https://api.stripe.com/v1/files \

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

/v1/files

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

file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

,

"

object

"

:

"

file

"

,

"

created

"

:

1680116847

,

"

expires_at

"

:

1703444847

,

"

filename

"

:

"

file.png

"

,

"

links

"

:

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

data

"

:

[],

"

has_more

"

:

false

,

"

url

"

:

"

/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH

"

},

"

purpose

"

:

"

dispute_evidence

"

,

"

size

"

:

8429

,

"

title

"

:

null

,

"

type

"

:

"

png

"

,

"

url

"

:

"

https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents

"

}

]

}
