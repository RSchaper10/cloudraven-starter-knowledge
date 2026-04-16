---
title: Account Tokens | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/account-tokens
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:01.392688+00:00
kind: extracted-doc
---

# Account Tokens | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/account-tokens

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:01.392688+00:00

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
- https://docs.stripe.com/api/v2/core/account-tokens/object
- https://docs.stripe.com/api/v2/core/account-tokens/create
- https://docs.stripe.com/api/v2/core/account-tokens/retrieve
- https://docs.stripe.com/api/balance
- https://docs.stripe.com/api/balance_transactions
- https://docs.stripe.com/api/charges

Captured summary:

- Account Tokens | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 The Account Token object v2 Create an account token v2 Retrieve an account token v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Account Tokens v2 Ask about this section Copy for LLM View as Markdown Account tokens are single-use tokens which tokenize company/individual/business information, and are used for creating or updating an Account.
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / account_tokens GET / v2 / core / account_tokens / :id The Account Token object v2 Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the token.
- object string, value is "v2.core.account_token" String representing the object’s type.
- Objects of the same type share the same value of the object field.

Extracted text:

Account Tokens | Stripe API Reference

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

The Account Token object

v2

Create an account token

v2

Retrieve an account token

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

Account Tokens

v2

Ask about this section

Copy for LLM

View as Markdown

Account tokens are single-use tokens which tokenize company/individual/business information, and are used for creating or updating an Account.

Learn more about calling API v2 endpoints.

Was this section helpful?

Yes

No

Endpoints

POST

/

v2

/

core

/

account_tokens

GET

/

v2

/

core

/

account_tokens

/

:id

The Account Token object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the token.

object

string, value is "v2.core.account_token"

String representing the object’s type. Objects of the same type share the same value of the object field.

created

timestamp

Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

expires

_

at

timestamp

Time at which the token will expire.

livemode

boolean

Has the value

true

if the token exists in live mode or the value

false

if the object exists in test mode.

used

boolean

Determines if the token has already been used (tokens can only be used once).

The Account Token object

{

"

id

"

:

"

accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_token

"

,

"

created

"

:

"

2025-11-17T14:00:00.000Z

"

,

"

expires_at

"

:

"

2025-11-17T14:10:00.000Z

"

,

"

livemode

"

:

true

,

"

used

"

:

false

}

Create an account token

v2

Ask about this section

Copy for LLM

View as Markdown

Creates an Account Token.

Learn more about calling API v2 endpoints.

Parameters

contact

_

email

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

string

The default contact phone for the Account.

display

_

name

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

identity

object

Information about the company, individual, and business represented by the Account.

Show child parameters

Returns

Response attributes

id

string

Unique identifier for the token.

object

string, value is "v2.core.account_token"

String representing the object’s type. Objects of the same type share the same value of the object field.

created

timestamp

Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

expires

_

at

timestamp

Time at which the token will expire.

livemode

boolean

Has the value

true

if the token exists in live mode or the value

false

if the object exists in test mode.

used

boolean

Determines if the token has already been used (tokens can only be used once).

Error Codes

400

platform

_

registration

_

required

Platform has not signed up for Connect and cannot create connected accounts.

400

token

_

must

_

be

_

created

_

with

_

publishable

_

key

Token must be created with publishable key.

429

account

_

rate

_

limit

_

exceeded

Account cannot exceed a configured concurrency rate limit on updates.

POST

/

v2

/

core

/

account_tokens

curl

-X POST https://api.stripe.com/v2/core/account_tokens \

-H

"

Authorization: Bearer

[REDACTED_SECRET]

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.dahlia

"

\

--json

'

{

"contact_email": "furever@example.com",

"display_name": "Furever",

"identity": {

"attestations": {

"terms_of_service": {

"account": {

"shown_and_accepted": true

}

}

},

"entity_type": "company",

"business_details": {

"registered_name": "Furever"

}

}

}

'

Response

{

"

id

"

:

"

accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_token

"

,

"

created

"

:

"

2025-11-17T14:00:00.000Z

"

,

"

expires_at

"

:

"

2025-11-17T14:10:00.000Z

"

,

"

livemode

"

:

true

,

"

used

"

:

false

}

Retrieve an account token

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves an Account Token.

Learn more about calling API v2 endpoints.

Parameters

No

parameters

.

Returns

Response attributes

id

string

Unique identifier for the token.

object

string, value is "v2.core.account_token"

String representing the object’s type. Objects of the same type share the same value of the object field.

created

timestamp

Time at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

expires

_

at

timestamp

Time at which the token will expire.

livemode

boolean

Has the value

true

if the token exists in live mode or the value

false

if the object exists in test mode.

used

boolean

Determines if the token has already been used (tokens can only be used once).

Error Codes

404

not

_

found

The resource wasn’t found.

429

account

_

rate

_

limit

_

exceeded

Account cannot exceed a configured concurrency rate limit on updates.

GET

/

v2

/

core

/

account_tokens

/

:id

curl

https://api.stripe.com/v2/core/account_tokens/accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \

-H

"

Authorization: Bearer

[REDACTED_SECRET]

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.dahlia

"

Response

{

"

id

"

:

"

accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_token

"

,

"

created

"

:

"

2025-11-17T14:00:00.000Z

"

,

"

expires_at

"

:

"

2025-11-17T14:10:00.000Z

"

,

"

livemode

"

:

true

,

"

used

"

:

true

}
