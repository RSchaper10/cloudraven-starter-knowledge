---
title: Person Tokens | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/person-tokens
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:25.404983+00:00
kind: extracted-doc
---

# Person Tokens | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/person-tokens

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:25.404983+00:00

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

- Person Tokens | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 The Person Token object v2 Create a person token v2 Retrieve a person token v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Person Tokens v2 Ask about this section Copy for LLM View as Markdown Person Tokens are single-use tokens which tokenize person information, and are used for creating or updating a Person.
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / accounts / :account_id / person_tokens GET / v2 / core / accounts / :account_id / person_tokens / :id The Person Token object v2 Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the token.
- object string, value is "v2.core.account_person_token" String representing the object’s type.
- Objects of the same type share the same value of the object field.

Extracted text:

Person Tokens | Stripe API Reference

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

The Person Token object

v2

Create a person token

v2

Retrieve a person token

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

Person Tokens

v2

Ask about this section

Copy for LLM

View as Markdown

Person Tokens are single-use tokens which tokenize person information, and are used for creating or updating a Person.

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

accounts

/

:account_id

/

person_tokens

GET

/

v2

/

core

/

accounts

/

:account_id

/

person_tokens

/

:id

The Person Token object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the token.

object

string, value is "v2.core.account_person_token"

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

The Person Token object

{

"

id

"

:

"

perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person_token

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

Create a person token

v2

Ask about this section

Copy for LLM

View as Markdown

Creates a Person Token associated with an Account.

Learn more about calling API v2 endpoints.

Parameters

additional

_

addresses

array of objects

Additional addresses associated with the person.

Show child parameters

additional

_

names

array of objects

Additional names (e.g. aliases) associated with the person.

Show child parameters

additional

_

terms

_

of

_

service

object

Attestations of accepted terms of service agreements.

Show child parameters

address

object

The person’s residential address.

Show child parameters

date

_

of

_

birth

object

The person’s date of birth.

Show child parameters

documents

object

Documents that may be submitted to satisfy various informational requests.

Show child parameters

email

string

Email.

given

_

name

string

The person’s first name.

id

_

numbers

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child parameters

legal

_

gender

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

metadata

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

nationalities

array of enums

The nationalities (countries) this person is associated with.

phone

string

The phone number for this person.

political

_

exposure

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

object

The relationship that this person has with the Account’s business or legal entity.

Show child parameters

script

_

addresses

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child parameters

script

_

names

object

The script names (e.g. non-Latin characters) associated with the person.

Show child parameters

surname

string

The person’s last name.

Returns

Response attributes

id

string

Unique identifier for the token.

object

string, value is "v2.core.account_person_token"

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

accounts

/

:account_id

/

person_tokens

curl

-X POST https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

/person_tokens \

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

"given_name": "Jenny",

"surname": "Rosen",

"email": "jenny.rosen@example.com",

"address": {

"line1": "27 Fredrick Ave",

"city": "Brothers",

"postal_code": "97712",

"state": "OR",

"country": "US"

},

"id_numbers": [

{

"type": "us_ssn_last_4",

"value": "0000"

}

],

"relationship": {

"owner": true,

"percent_ownership": "0.8",

"representative": true,

"title": "CEO"

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

perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person_token

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

Retrieve a person token

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves a Person Token associated with an Account.

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

string, value is "v2.core.account_person_token"

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

accounts

/

:account_id

/

person_tokens

/

:id

curl

https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

/person_tokens/perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \

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

perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person_token

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
