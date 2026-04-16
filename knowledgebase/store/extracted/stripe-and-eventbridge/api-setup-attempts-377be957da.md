---
title: Setup Attempts | Stripe API Reference
source_url: https://docs.stripe.com/api/setup_attempts
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:27.751844+00:00
kind: extracted-doc
---

# Setup Attempts | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/setup_attempts

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:27.751844+00:00

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

- Setup Attempts | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts The SetupAttempt object List all SetupAttempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Setup Attempts Ask about this section Copy for LLM View as Markdown A SetupAttempt describes one attempted confirmation of a SetupIntent, whether that confirmation is successful or unsuccessful.
- You can use SetupAttempts to inspect details of a specific attempt at setting up a payment method using a SetupIntent.
- Yes No Endpoints GET / v1 / setup_attempts The SetupAttempt object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- object string String representing the object’s type.
- Objects of the same type share the same value.

Extracted text:

Setup Attempts | Stripe API Reference

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

The SetupAttempt object

List all SetupAttempts

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

Setup Attempts

Ask about this section

Copy for LLM

View as Markdown

A SetupAttempt describes one attempted confirmation of a SetupIntent,

whether that confirmation is successful or unsuccessful. You can use

SetupAttempts to inspect details of a specific attempt at setting up a

payment method using a SetupIntent.

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

setup_attempts

The SetupAttempt object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

object

string

String representing the object’s type. Objects of the same type share the same value.

application

nullable

string

Expandable

The value of

application

on the SetupIntent at the time of this confirmation.

attach

_

to

_

self

nullable

boolean

If present, the SetupIntent’s payment method will be attached to the in-context Stripe Account.

It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.

created

timestamp

retrievable with publishable key

Time at which the object was created. Measured in seconds since the Unix epoch.

customer

nullable

string

Expandable

The value of

customer

on the SetupIntent at the time of this confirmation.

customer

_

account

nullable

string

The value of

customer_account

on the SetupIntent at the time of this confirmation.

flow

_

directions

nullable

array of enums

Indicates the directions of money movement for which this payment method is intended to be used.

Include

inbound

if you intend to use the payment method as the origin to pull funds from. Include

outbound

if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.

Possible enum values

inbound

outbound

livemode

boolean

retrievable with publishable key

If the object exists in live mode, the value is

true

. If the object exists in test mode, the value is

false

.

on

_

behalf

_

of

nullable

string

Expandable

The value of

on_behalf_of

on the SetupIntent at the time of this confirmation.

payment

_

method

string

Expandable

retrievable with publishable key

ID of the payment method used with this SetupAttempt.

payment

_

method

_

details

object

Details about the payment method at the time of SetupIntent confirmation.

Show child attributes

setup

_

error

nullable

object

The error encountered during this attempt to confirm the SetupIntent, if any.

Show child attributes

setup

_

intent

string

Expandable

ID of the SetupIntent that this attempt belongs to.

status

string

Status of this SetupAttempt, one of

requires

_

confirmation

,

requires

_

action

,

processing

,

succeeded

,

failed

, or

abandoned

.

usage

string

The value of

usage

on the SetupIntent at the time of this confirmation, one of

off

_

session

or

on

_

session

.

The SetupAttempt object

{

"

id

"

:

"

setatt_1ErTsH2eZvKYlo2CI7ukcoF7

"

,

"

object

"

:

"

setup_attempt

"

,

"

application

"

:

null

,

"

created

"

:

1562004309

,

"

customer

"

:

null

,

"

flow_directions

"

:

null

,

"

livemode

"

:

false

,

"

on_behalf_of

"

:

null

,

"

payment_method

"

:

"

pm_1ErTsG2eZvKYlo2CH0DNen59

"

,

"

payment_method_details

"

:

{

"

card

"

:

{

"

three_d_secure

"

:

null

},

"

type

"

:

"

card

"

},

"

setup_error

"

:

null

,

"

setup_intent

"

:

"

seti_1ErTsG2eZvKYlo2CKaT8MITz

"

,

"

status

"

:

"

succeeded

"

,

"

usage

"

:

"

off_session

"

}

List all SetupAttempts

Ask about this section

Copy for LLM

View as Markdown

Returns a list of SetupAttempts that associate with a provided SetupIntent.

Parameters

setup

_

intent

string

Required

Only return SetupAttempts created by the SetupIntent specified by

this ID.

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

property that contains

an array of up to

limit

SetupAttempts that are created by the

specified SetupIntent, which start after SetupAttempts

starting

_

after

. Each

entry in the array is a separate SetupAttempts object. If no other

SetupAttempts are available, the resulting array is be empty. This

request should never

raise

an error.

GET

/

v1

/

setup_attempts

curl

-G https://api.stripe.com/v1/setup_attempts \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d limit=3 \

-d setup_intent=

seti_1ErTsG2eZvKYlo2CKaT8MITz

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

/v1/setup_attempts

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

setatt_1ErTsH2eZvKYlo2CI7ukcoF7

"

,

"

object

"

:

"

setup_attempt

"

,

"

application

"

:

null

,

"

created

"

:

1562004309

,

"

customer

"

:

null

,

"

flow_directions

"

:

null

,

"

livemode

"

:

false

,

"

on_behalf_of

"

:

null

,

"

payment_method

"

:

"

pm_1ErTsG2eZvKYlo2CH0DNen59

"

,

"

payment_method_details

"

:

{

"

card

"

:

{

"

three_d_secure

"

:

null

},

"

type

"

:

"

card

"

},

"

setup_error

"

:

null

,

"

setup_intent

"

:

"

seti_1ErTsG2eZvKYlo2CKaT8MITz

"

,

"

status

"

:

"

succeeded

"

,

"

usage

"

:

"

off_session

"

}

]

}
