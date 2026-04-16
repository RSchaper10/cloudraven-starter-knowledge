---
title: Mandates | Stripe API Reference
source_url: https://docs.stripe.com/api/mandates
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:20.825011+00:00
kind: extracted-doc
---

# Mandates | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/mandates

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:20.825011+00:00

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

- Mandates | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates The Mandate object Retrieve a Mandate Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Mandates Ask about this section Copy for LLM View as Markdown A Mandate is a record of the permission that your customer gives you to debit their payment method.
- Yes No Endpoints GET / v1 / mandates / :id The Mandate object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- customer _ acceptance object Details about the customer’s acceptance of the mandate.
- Show child attributes payment _ method string Expandable ID of the payment method associated with this mandate.
- payment _ method _ details object Additional mandate information specific to the payment method type.

Extracted text:

Mandates | Stripe API Reference

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

The Mandate object

Retrieve a Mandate

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

Mandates

Ask about this section

Copy for LLM

View as Markdown

A Mandate is a record of the permission that your customer gives you to debit their payment method.

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

mandates

/

:id

The Mandate object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

customer

_

acceptance

object

Details about the customer’s acceptance of the mandate.

Show child attributes

payment

_

method

string

Expandable

ID of the payment method associated with this mandate.

payment

_

method

_

details

object

Additional mandate information specific to the payment method type.

Show child attributes

status

enum

The mandate status indicates whether or not you can use it to initiate a payment.

Possible enum values

active

The mandate can be used to initiate a payment.

inactive

The mandate was rejected, revoked, or previously used, and may not be used to initiate future payments.

pending

The mandate is newly created and is not yet active or inactive.

type

enum

The type of the mandate.

Possible enum values

multi

_

use

Represents permission given for multiple payments.

single

_

use

Represents a one-time permission given for a single payment.

More attributes

Expand all

object

string

livemode

boolean

multi

_

use

nullable

object

on

_

behalf

_

of

nullable

string

Connect only

single

_

use

nullable

object

The Mandate object

{

"

id

"

:

"

mandate_1MvojA2eZvKYlo2CvqTABjZs

"

,

"

object

"

:

"

mandate

"

,

"

customer_acceptance

"

:

{

"

accepted_at

"

:

123456789

,

"

online

"

:

{

"

ip_address

"

:

"

127.0.0.0

"

,

"

user_agent

"

:

"

device

"

},

"

type

"

:

"

online

"

},

"

livemode

"

:

false

,

"

multi_use

"

:

{},

"

payment_method

"

:

"

pm_123456789

"

,

"

payment_method_details

"

:

{

"

sepa_debit

"

:

{

"

reference

"

:

"

123456789

"

,

"

url

"

:

""

},

"

type

"

:

"

sepa_debit

"

},

"

status

"

:

"

active

"

,

"

type

"

:

"

multi_use

"

}

Retrieve a Mandate

Ask about this section

Copy for LLM

View as Markdown

Retrieves a Mandate object.

Parameters

No

parameters

.

Returns

Returns a Mandate object.

GET

/

v1

/

mandates

/

:id

curl

https://api.stripe.com/v1/mandates/mandate_1MvojA2eZvKYlo2CvqTABjZs \

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

mandate_1MvojA2eZvKYlo2CvqTABjZs

"

,

"

object

"

:

"

mandate

"

,

"

customer_acceptance

"

:

{

"

accepted_at

"

:

123456789

,

"

online

"

:

{

"

ip_address

"

:

"

127.0.0.0

"

,

"

user_agent

"

:

"

device

"

},

"

type

"

:

"

online

"

},

"

livemode

"

:

false

,

"

multi_use

"

:

{},

"

payment_method

"

:

"

pm_123456789

"

,

"

payment_method_details

"

:

{

"

sepa_debit

"

:

{

"

reference

"

:

"

123456789

"

,

"

url

"

:

""

},

"

type

"

:

"

sepa_debit

"

},

"

status

"

:

"

active

"

,

"

type

"

:

"

multi_use

"

}
