---
title: Setup Intents | Stripe API Reference
source_url: https://docs.stripe.com/api/setup_intents
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:26.680540+00:00
kind: extracted-doc
---

# Setup Intents | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/setup_intents

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:26.680540+00:00

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

- Setup Intents | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents The SetupIntent object Create a SetupIntent Update a SetupIntent Retrieve a SetupIntent List all SetupIntents Cancel a SetupIntent Confirm a SetupIntent Verify microdeposits on a SetupIntent Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Setup Intents Ask about this section Copy for LLM View as Markdown A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments.
- For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment.
- Later, you can use PaymentIntents to drive the payment flow.
- Create a SetupIntent when you’re ready to collect your customer’s payment credentials.
- Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid.

Extracted text:

Setup Intents | Stripe API Reference

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

The SetupIntent object

Create a SetupIntent

Update a SetupIntent

Retrieve a SetupIntent

List all SetupIntents

Cancel a SetupIntent

Confirm a SetupIntent

Verify microdeposits on a SetupIntent

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

Setup Intents

Ask about this section

Copy for LLM

View as Markdown

A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments.

For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment.

Later, you can use

PaymentIntents

to drive the payment flow.

Create a SetupIntent when you’re ready to collect your customer’s payment credentials.

Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid.

The SetupIntent transitions through multiple

statuses

as it guides

you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for future payments.

For example, cardholders in

certain regions

might need to be run through

Strong Customer Authentication

during payment method collection

to streamline later

off-session payments

.

If you use the SetupIntent with a

Customer

,

it automatically attaches the resulting payment method to that Customer after successful setup.

We recommend using SetupIntents or

setup_future_usage

on

PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide:

Setup Intents API

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

setup_intents

POST

/

v1

/

setup_intents

/

:id

GET

/

v1

/

setup_intents

/

:id

GET

/

v1

/

setup_intents

POST

/

v1

/

setup_intents

/

:id

/

cancel

POST

/

v1

/

setup_intents

/

:id

/

confirm

POST

/

v1

/

setup_intents

/

:id

/

verify_microdeposits

The SetupIntent object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

retrievable with publishable key

Unique identifier for the object.

automatic

_

payment

_

methods

nullable

object

Settings for dynamic payment methods compatible with this Setup Intent

Show child attributes

client

_

secret

nullable

string

retrievable with publishable key

The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.

The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

customer

nullable

string

Expandable

ID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

customer

_

account

nullable

string

ID of the Account this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.

description

nullable

string

retrievable with publishable key

An arbitrary string attached to the object. Often useful for displaying to users.

last

_

setup

_

error

nullable

object

retrievable with publishable key

The error encountered in the previous SetupIntent confirmation.

Show child attributes

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

next

_

action

nullable

object

retrievable with publishable key

If present, this property tells you what actions you need to take in order for your customer to continue payment setup.

Show child attributes

payment

_

method

nullable

string

Expandable

retrievable with publishable key

ID of the payment method used with this SetupIntent. If the payment method is

card

_

present

and isn’t a digital wallet, then the

generated_card

associated with the

latest

_

attempt

is attached to the Customer instead.

status

enum

retrievable with publishable key

Status

of this SetupIntent, one of

requires

_

payment

_

method

,

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

canceled

, or

succeeded

.

Possible enum values

canceled

processing

requires

_

action

requires

_

confirmation

requires

_

payment

_

method

succeeded

usage

string

retrievable with publishable key

Indicates how the payment method is intended to be used in the future.

Use

on

_

session

if you intend to only reuse the payment method when the customer is in your checkout flow. Use

off

_

session

if your customer may or may not be in your checkout flow. If not provided, this value defaults to

off

_

session

.

More attributes

Expand all

object

string

retrievable with publishable key

application

nullable

string

Expandable

Connect only

attach

_

to

_

self

nullable

boolean

cancellation

_

reason

nullable

enum

retrievable with publishable key

created

timestamp

retrievable with publishable key

excluded

_

payment

_

method

_

types

nullable

array of enums

flow

_

directions

nullable

array of enums

latest

_

attempt

nullable

string

Expandable

livemode

boolean

retrievable with publishable key

mandate

nullable

string

Expandable

on

_

behalf

_

of

nullable

string

Expandable

Connect only

payment

_

method

_

configuration

_

details

nullable

object

payment

_

method

_

options

nullable

object

payment

_

method

_

types

array of strings

retrievable with publishable key

single

_

use

_

mandate

nullable

string

Expandable

The SetupIntent object

{

"

id

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

"

,

"

object

"

:

"

setup_intent

"

,

"

application

"

:

null

,

"

cancellation_reason

"

:

null

,

"

client_secret

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe

"

,

"

created

"

:

1678942624

,

"

customer

"

:

null

,

"

description

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

last_setup_error

"

:

null

,

"

latest_attempt

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

mandate

"

:

null

,

"

metadata

"

:

{},

"

next_action

"

:

null

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

null

,

"

payment_method_options

"

:

{

"

card

"

:

{

"

mandate_options

"

:

null

,

"

network

"

:

null

,

"

request_three_d_secure

"

:

"

automatic

"

}

},

"

payment_method_types

"

:

[

"

card

"

],

"

single_use_mandate

"

:

null

,

"

status

"

:

"

requires_payment_method

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

Create a SetupIntent

Ask about this section

Copy for LLM

View as Markdown

Creates a SetupIntent object.

After you create the SetupIntent, attach a payment method and

confirm

it to collect any required permissions to charge the payment method later.

Parameters

automatic

_

payment

_

methods

object

When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.

Show child parameters

confirm

boolean

Set to

true

to attempt to confirm this SetupIntent immediately. This parameter defaults to

false

. If a card is the attached payment method, you can provide a

return

_

url

in case further authentication is necessary.

customer

string

ID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

customer

_

account

string

ID of the Account this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.

description

string

An arbitrary string attached to the object. Often useful for displaying to users.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

payment

_

method

string

ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.

usage

enum

Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to

off

_

session

.

Possible enum values

off

_

session

Use

off

_

session

if your customer may or may not be in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when the customer is in your checkout flow.

More parameters

Expand all

attach

_

to

_

self

boolean

confirmation

_

token

string

only when confirm=true

excluded

_

payment

_

method

_

types

array of enums

flow

_

directions

array of enums

mandate

_

data

object

only when confirm=true

on

_

behalf

_

of

string

Connect only

payment

_

method

_

configuration

string

payment

_

method

_

data

object

payment

_

method

_

options

object

payment

_

method

_

types

array of strings

return

_

url

string

only when confirm=true

single

_

use

object

use

_

stripe

_

sdk

boolean

Returns

Returns a SetupIntent object.

POST

/

v1

/

setup_intents

curl

https://api.stripe.com/v1/setup_intents \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

payment_method_types[]=card

"

Response

{

"

id

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

"

,

"

object

"

:

"

setup_intent

"

,

"

application

"

:

null

,

"

cancellation_reason

"

:

null

,

"

client_secret

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe

"

,

"

created

"

:

1678942624

,

"

customer

"

:

null

,

"

description

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

last_setup_error

"

:

null

,

"

latest_attempt

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

mandate

"

:

null

,

"

metadata

"

:

{},

"

next_action

"

:

null

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

null

,

"

payment_method_options

"

:

{

"

card

"

:

{

"

mandate_options

"

:

null

,

"

network

"

:

null

,

"

request_three_d_secure

"

:

"

automatic

"

}

},

"

payment_method_types

"

:

[

"

card

"

],

"

single_use_mandate

"

:

null

,

"

status

"

:

"

requires_payment_method

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

Update a SetupIntent

Ask about this section

Copy for LLM

View as Markdown

Updates a SetupIntent object.

Parameters

customer

string

ID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.

customer

_

account

string

ID of the Account this SetupIntent belongs to, if one exists.

If present, the SetupIntent’s payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.

description

string

An arbitrary string attached to the object. Often useful for displaying to users.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

payment

_

method

string

ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string.

More parameters

Expand all

attach

_

to

_

self

boolean

excluded

_

payment

_

method

_

types

array of enums

flow

_

directions

array of enums

payment

_

method

_

configuration

string

payment

_

method

_

data

object

payment

_

method

_

options

object

payment

_

method

_

types

array of strings

Returns

Returns a SetupIntent object.

POST

/

v1

/

setup_intents

/

:id

curl

https://api.stripe.com/v1/setup_intents/

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

\

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

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

"

,

"

object

"

:

"

setup_intent

"

,

"

application

"

:

null

,

"

cancellation_reason

"

:

null

,

"

client_secret

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe

"

,

"

created

"

:

1678942624

,

"

customer

"

:

null

,

"

description

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

last_setup_error

"

:

null

,

"

latest_attempt

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

mandate

"

:

null

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

next_action

"

:

null

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

null

,

"

payment_method_options

"

:

{

"

card

"

:

{

"

mandate_options

"

:

null

,

"

network

"

:

null

,

"

request_three_d_secure

"

:

"

automatic

"

}

},

"

payment_method_types

"

:

[

"

card

"

],

"

single_use_mandate

"

:

null

,

"

status

"

:

"

requires_payment_method

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

Retrieve a SetupIntent

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of a SetupIntent that has previously been created.

Client-side retrieval using a publishable key is allowed when the

client

_

secret

is provided in the query string.

When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the

SetupIntent

object reference for more details.

Parameters

client

_

secret

string

Required if using publishable key

The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.

Returns

Returns a SetupIntent if a valid identifier was provided.

GET

/

v1

/

setup_intents

/

:id

curl

https://api.stripe.com/v1/setup_intents/

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

\

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

seti_1Mm8s8LkdIwHu7ix0OXBfTRG

"

,

"

object

"

:

"

setup_intent

"

,

"

application

"

:

null

,

"

cancellation_reason

"

:

null

,

"

client_secret

"

:

"

seti_1Mm8s8LkdIwHu7ix0OXBfTRG_secret_NXDICkPqPeiBTAFqWmkbff09lRmSVXe

"

,

"

created

"

:

1678942624

,

"

customer

"

:

null

,

"

description

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

last_setup_error

"

:

null

,

"

latest_attempt

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

mandate

"

:

null

,

"

metadata

"

:

{},

"

next_action

"

:

null

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

null

,

"

payment_method_options

"

:

{

"

card

"

:

{

"

mandate_options

"

:

null

,

"

network

"

:

null

,

"

request_three_d_secure

"

:

"

automatic

"

}

},

"

payment_method_types

"

:

[

"

card

"

],

"

single_use_mandate

"

:

null

,

"

status

"

:

"

requires_payment_method

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
