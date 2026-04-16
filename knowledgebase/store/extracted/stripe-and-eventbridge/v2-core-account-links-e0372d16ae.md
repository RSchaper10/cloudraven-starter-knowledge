---
title: Account Links | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/account-links
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:00.433978+00:00
kind: extracted-doc
---

# Account Links | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/account-links

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:00.433978+00:00

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
- https://docs.stripe.com/api/v2/core/account-links/object
- https://docs.stripe.com/api/v2/core/account-links/create
- https://docs.stripe.com/api/v2/core/account-tokens
- https://docs.stripe.com/api/balance
- https://docs.stripe.com/api/balance_transactions
- https://docs.stripe.com/api/charges
- https://docs.stripe.com/api/customers

Captured summary:

- Account Links | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 The Account Link object v2 Create an account link v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Account Links v2 Ask about this section Copy for LLM View as Markdown Account Links let a platform create a temporary, single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / account_links The Account Link object v2 Ask about this section Copy for LLM View as Markdown Attributes object string, value is "v2.core.account_link" String representing the object’s type.
- Objects of the same type share the same value of the object field.
- account string The ID of the connected account this Account Link applies to.

Extracted text:

Account Links | Stripe API Reference

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

The Account Link object

v2

Create an account link

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

Account Links

v2

Ask about this section

Copy for LLM

View as Markdown

Account Links let a platform create a temporary, single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.

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

account_links

The Account Link object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

object

string, value is "v2.core.account_link"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The ID of the connected account this Account Link applies to.

created

timestamp

The timestamp at which this Account Link was created.

expires

_

at

timestamp

The timestamp at which this Account Link will expire.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

url

string

The URL at which the account can access the Stripe-hosted flow.

use

_

case

object

Hash containing usage options.

Show child attributes

The Account Link object

{

"

object

"

:

"

v2.core.account_link

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

created

"

:

"

2025-03-27T17:15:18.000Z

"

,

"

expires_at

"

:

"

2025-03-27T17:25:18.000Z

"

,

"

url

"

:

"

https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6

"

,

"

use_case

"

:

{

"

account_onboarding

"

:

{

"

configurations

"

:

[

"

recipient

"

],

"

refresh_url

"

:

"

https://example.com/reauth

"

,

"

return_url

"

:

"

https://example.com/return

"

},

"

type

"

:

"

account_onboarding

"

}

}

Create an account link

v2

Ask about this section

Copy for LLM

View as Markdown

Creates an AccountLink object that includes a single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.

Learn more about calling API v2 endpoints.

Parameters

account

string

Required

The ID of the Account to create link for.

use

_

case

object

Required

The use case of the AccountLink.

Show child parameters

Returns

Response attributes

object

string, value is "v2.core.account_link"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The ID of the connected account this Account Link applies to.

created

timestamp

The timestamp at which this Account Link was created.

expires

_

at

timestamp

The timestamp at which this Account Link will expire.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

url

string

The URL at which the account can access the Stripe-hosted flow.

use

_

case

object

Hash containing usage options.

Show child attributes

Error Codes

400

accounts

_

v2

_

access

_

blocked

Accounts v2 is not enabled for your platform.

400

configs

_

must

_

match

_

to

_

use

_

account

_

links

Account cannot be onboard via v2/core/account_links without specifying the right configurations.

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

POST

/

v2

/

core

/

account_links

curl

-X POST https://api.stripe.com/v2/core/account_links \

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

"account": "

acct_1Nv0FGQ9RKHgCVdK

",

"use_case": {

"type": "account_onboarding",

"account_onboarding": {

"configurations": [

"recipient"

],

"return_url": "https://example.com/return",

"refresh_url": "https://example.com/reauth"

}

}

}

'

Response

{

"

object

"

:

"

v2.core.account_link

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

created

"

:

"

2025-03-27T17:15:18.000Z

"

,

"

expires_at

"

:

"

2025-03-27T17:25:18.000Z

"

,

"

livemode

"

:

true

,

"

url

"

:

"

https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6

"

,

"

use_case

"

:

{

"

account_onboarding

"

:

{

"

configurations

"

:

[

"

recipient

"

],

"

refresh_url

"

:

"

https://example.com/reauth

"

,

"

return_url

"

:

"

https://example.com/return

"

},

"

type

"

:

"

account_onboarding

"

}

}
