---
title: Payment Intents | Stripe API Reference
source_url: https://docs.stripe.com/api/payment_intents
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:22.893815+00:00
kind: extracted-doc
---

# Payment Intents | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/payment_intents

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:22.893815+00:00

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

- Payment Intents | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents The PaymentIntent object Create a PaymentIntent Update a PaymentIntent Retrieve a PaymentIntent List all PaymentIntent LineItems List all PaymentIntents Cancel a PaymentIntent Capture a PaymentIntent Confirm a PaymentIntent Increment an authorization Reconcile a customer_balance PaymentIntent Search PaymentIntents Verify microdeposits on a PaymentIntent Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Payment Intents Ask about this section Copy for LLM View as Markdown A PaymentIntent guides you through the process of collecting a payment from your customer.
- We recommend that you create exactly one PaymentIntent for each order or customer session in your system.
- You can reference the PaymentIntent later to see the history of payment attempts for a particular session.
- A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and ultimately creates at most one successful charge.
- Related guide: Payment Intents API Was this section helpful?

Extracted text:

Payment Intents | Stripe API Reference

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

The PaymentIntent object

Create a PaymentIntent

Update a PaymentIntent

Retrieve a PaymentIntent

List all PaymentIntent LineItems

List all PaymentIntents

Cancel a PaymentIntent

Capture a PaymentIntent

Confirm a PaymentIntent

Increment an authorization

Reconcile a customer_balance PaymentIntent

Search PaymentIntents

Verify microdeposits on a PaymentIntent

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

Payment Intents

Ask about this section

Copy for LLM

View as Markdown

A PaymentIntent guides you through the process of collecting a payment from your customer.

We recommend that you create exactly one PaymentIntent for each order or

customer session in your system. You can reference the PaymentIntent later to

see the history of payment attempts for a particular session.

A PaymentIntent transitions through

multiple statuses

throughout its lifetime as it interfaces with Stripe.js to perform

authentication flows and ultimately creates at most one successful charge.

Related guide:

Payment Intents API

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

payment_intents

POST

/

v1

/

payment_intents

/

:id

GET

/

v1

/

payment_intents

/

:id

GET

/

v1

/

payment_intents

/

:id

/

amount_details_line_items

GET

/

v1

/

payment_intents

POST

/

v1

/

payment_intents

/

:id

/

cancel

POST

/

v1

/

payment_intents

/

:id

/

capture

POST

/

v1

/

payment_intents

/

:id

/

confirm

POST

/

v1

/

payment_intents

/

:id

/

increment_authorization

POST

/

v1

/

payment_intents

/

:id

/

apply_customer_balance

GET

/

v1

/

payment_intents

/

search

POST

/

v1

/

payment_intents

/

:id

/

verify_microdeposits

The PaymentIntent object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

retrievable with publishable key

Unique identifier for the object.

amount

integer

retrievable with publishable key

Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the

smallest currency unit

(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or

equivalent in charge currency

. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

automatic

_

payment

_

methods

nullable

object

retrievable with publishable key

Settings to configure compatible payment methods from the

Stripe Dashboard

Show child attributes

client

_

secret

nullable

string

retrievable with publishable key

The client secret of this PaymentIntent. Used for client-side retrieval using a publishable key.

The client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

Refer to our docs to

accept a payment

and learn about how

client

_

secret

should be handled.

currency

enum

retrievable with publishable key

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

customer

nullable

string

Expandable

ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Customer instead.

customer

_

account

nullable

string

ID of the Account representing the customer that this PaymentIntent belongs to, if one exists.

Payment methods attached to other Accounts cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Account instead.

description

nullable

string

retrievable with publishable key

An arbitrary string attached to the object. Often useful for displaying to users.

last

_

payment

_

error

nullable

object

retrievable with publishable key

The payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason.

Show child attributes

latest

_

charge

nullable

string

Expandable

ID of the latest

Charge object

created by this PaymentIntent. This property is

null

until PaymentIntent confirmation is attempted.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Learn more about

storing information in metadata

.

next

_

action

nullable

object

retrievable with publishable key

If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.

Show child attributes

payment

_

method

nullable

string

Expandable

retrievable with publishable key

ID of the payment method used in this PaymentIntent.

receipt

_

email

nullable

string

retrievable with publishable key

Email address that the receipt for the resulting payment will be sent to. If

receipt

_

email

is specified for a payment in live mode, a receipt will be sent regardless of your

email settings

.

setup

_

future

_

usage

nullable

enum

retrievable with publishable key

Indicates that you intend to make future payments with this PaymentIntent’s payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to

attach the payment method

to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still

attach

the payment method to a Customer after the transaction completes.

If the payment method is

card

_

present

and isn’t a digital wallet, Stripe creates and attaches a

generated_card

payment method representing the card to the Customer instead.

When processing card payments, Stripe uses

setup

_

future

_

usage

to help you comply with regional legislation and network rules, such as

SCA

.

Possible enum values

off

_

session

Use

off

_

session

if your customer may or may not be present in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when your customer is present in your checkout flow.

shipping

nullable

object

retrievable with publishable key

Shipping information for this PaymentIntent.

Show child attributes

statement

_

descriptor

nullable

string

Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see

the Statement Descriptor docs

.

Setting this value for a card charge returns an error. For card charges, set the

statement_descriptor_suffix

instead.

statement

_

descriptor

_

suffix

nullable

string

Provides information about a card charge. Concatenated to the account’s

statement descriptor prefix

to form the complete statement descriptor that appears on the customer’s statement.

status

enum

retrievable with publishable key

Status of this PaymentIntent, one of

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

requires

_

capture

,

canceled

, or

succeeded

. Read more about each PaymentIntent

status

.

Possible enum values

canceled

The PaymentIntent has been canceled.

processing

The PaymentIntent is currently being processed.

requires

_

action

The PaymentIntent requires additional action from the customer.

requires

_

capture

The PaymentIntent has been confirmed and requires capture.

requires

_

confirmation

The PaymentIntent requires confirmation.

requires

_

payment

_

method

The PaymentIntent requires a payment method to be attached.

succeeded

The PaymentIntent has succeeded.

More attributes

Expand all

object

string

retrievable with publishable key

amount

_

capturable

integer

amount

_

details

nullable

object

amount

_

received

integer

application

nullable

string

Expandable

Connect only

application

_

fee

_

amount

nullable

integer

Connect only

canceled

_

at

nullable

timestamp

retrievable with publishable key

cancellation

_

reason

nullable

enum

retrievable with publishable key

capture

_

method

enum

retrievable with publishable key

confirmation

_

method

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

hooks

nullable

object

livemode

boolean

retrievable with publishable key

managed

_

payments

nullable

object

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

details

nullable

object

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

presentment

_

details

nullable

object

processing

nullable

object

retrievable with publishable key

review

nullable

string

Expandable

transfer

_

data

nullable

object

Connect only

transfer

_

group

nullable

string

Connect only

The PaymentIntent object

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

amount

"

:

2000

,

"

amount_capturable

"

:

0

,

"

amount_details

"

:

{

"

tip

"

:

{}

},

"

amount_received

"

:

0

,

"

application

"

:

null

,

"

application_fee_amount

"

:

null

,

"

automatic_payment_methods

"

:

{

"

enabled

"

:

true

},

"

canceled_at

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

capture_method

"

:

"

automatic

"

,

"

client_secret

"

:

"

pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH

"

,

"

confirmation_method

"

:

"

automatic

"

,

"

created

"

:

1680800504

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

last_payment_error

"

:

null

,

"

latest_charge

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

installments

"

:

null

,

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

},

"

link

"

:

{

"

persistent_token

"

:

null

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

,

"

link

"

],

"

processing

"

:

null

,

"

receipt_email

"

:

null

,

"

review

"

:

null

,

"

setup_future_usage

"

:

null

,

"

shipping

"

:

null

,

"

source

"

:

null

,

"

statement_descriptor

"

:

null

,

"

statement_descriptor_suffix

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

transfer_data

"

:

null

,

"

transfer_group

"

:

null

}

Create a PaymentIntent

Ask about this section

Copy for LLM

View as Markdown

Creates a PaymentIntent object.

After the PaymentIntent is created, attach a payment method and

confirm

to continue the payment. Learn more about

the available payment flows

with the Payment Intents API

.

When you use

confirm=true

during creation, it’s equivalent to creating

and confirming the PaymentIntent in the same call. You can use any parameters

available in the

confirm API

when you supply

confirm=true

.

Parameters

amount

integer

Required

Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the

smallest currency unit

(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or

equivalent in charge currency

. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

currency

enum

Required

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

automatic

_

payment

_

methods

object

When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent’s other parameters.

Show child parameters

confirm

boolean

Set to

true

to attempt to

confirm this PaymentIntent

immediately. This parameter defaults to

false

. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the

Confirm API

.

customer

string

ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Customer instead.

customer

_

account

string

ID of the Account representing the customer that this PaymentIntent belongs to, if one exists.

Payment methods attached to other Accounts cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Account instead.

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

off

_

session

boolean | string

only when confirm=true

Set to

true

to indicate that the customer isn’t in your checkout flow during this payment attempt and can’t authenticate. Use this parameter in scenarios where you collect card details and

charge them later

. This parameter can only be used with

confirm=true

.

payment

_

method

string

ID of the payment method (a PaymentMethod, Card, or

compatible Source

object) to attach to this PaymentIntent.

If you omit this parameter with

confirm=true

,

customer

.

default

_

source

attaches as this PaymentIntent’s payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the

payment

_

method

moving forward.

If the payment method is attached to a Customer, you must also provide the ID of that Customer as the

customer

parameter of this PaymentIntent.

receipt

_

email

string

Email address to send the receipt to. If you specify

receipt

_

email

for a payment in live mode, you send a receipt regardless of your

email settings

.

setup

_

future

_

usage

enum

Indicates that you intend to make future payments with this PaymentIntent’s payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to

attach the payment method

to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still

attach

the payment method to a Customer after the transaction completes.

If the payment method is

card

_

present

and isn’t a digital wallet, Stripe creates and attaches a

generated_card

payment method representing the card to the Customer instead.

When processing card payments, Stripe uses

setup

_

future

_

usage

to help you comply with regional legislation and network rules, such as

SCA

.

Possible enum values

off

_

session

Use

off

_

session

if your customer may or may not be present in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when your customer is present in your checkout flow.

shipping

object

Shipping information for this PaymentIntent.

Show child parameters

statement

_

descriptor

string

Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see

the Statement Descriptor docs

.

Setting this value for a card charge returns an error. For card charges, set the

statement_descriptor_suffix

instead.

statement

_

descriptor

_

suffix

string

Provides information about a card charge. Concatenated to the account’s

statement descriptor prefix

to form the complete statement descriptor that appears on the customer’s statement.

More parameters

Expand all

amount

_

details

object

application

_

fee

_

amount

integer

Connect only

capture

_

method

enum

confirmation

_

method

enum

confirmation

_

token

string

only when confirm=true

error

_

on

_

requires

_

action

boolean

only when confirm=true

excluded

_

payment

_

method

_

types

array of enums

hooks

object

mandate

string

only when confirm=true

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

details

object

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

radar

_

options

object

return

_

url

string

only when confirm=true

transfer

_

data

object

Connect only

transfer

_

group

string

Connect only

use

_

stripe

_

sdk

boolean

Returns

Returns a PaymentIntent object.

POST

/

v1

/

payment_intents

curl

https://api.stripe.com/v1/payment_intents \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d amount=2000 \

-d currency=usd \

-d

"

automatic_payment_methods[enabled]=true

"

Response

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

amount

"

:

2000

,

"

amount_capturable

"

:

0

,

"

amount_details

"

:

{

"

tip

"

:

{}

},

"

amount_received

"

:

0

,

"

application

"

:

null

,

"

application_fee_amount

"

:

null

,

"

automatic_payment_methods

"

:

{

"

enabled

"

:

true

},

"

canceled_at

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

capture_method

"

:

"

automatic

"

,

"

client_secret

"

:

"

pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH

"

,

"

confirmation_method

"

:

"

automatic

"

,

"

created

"

:

1680800504

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

last_payment_error

"

:

null

,

"

latest_charge

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

installments

"

:

null

,

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

},

"

link

"

:

{

"

persistent_token

"

:

null

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

,

"

link

"

],

"

processing

"

:

null

,

"

receipt_email

"

:

null

,

"

review

"

:

null

,

"

setup_future_usage

"

:

null

,

"

shipping

"

:

null

,

"

source

"

:

null

,

"

statement_descriptor

"

:

null

,

"

statement_descriptor_suffix

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

transfer_data

"

:

null

,

"

transfer_group

"

:

null

}

Update a PaymentIntent

Ask about this section

Copy for LLM

View as Markdown

Updates properties on a PaymentIntent object without confirming.

Depending on which properties you update, you might need to confirm the

PaymentIntent again. For example, updating the

payment

_

method

always requires you to confirm the PaymentIntent again. If you prefer to

update and confirm at the same time, we recommend updating properties through

the

confirm API

instead.

Parameters

amount

integer

Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the

smallest currency unit

(e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or

equivalent in charge currency

. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

currency

enum

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

customer

string

ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Customer instead.

customer

_

account

string

ID of the Account representing the customer that this PaymentIntent belongs to, if one exists.

Payment methods attached to other Accounts cannot be used with this PaymentIntent.

If

setup_future_usage

is set and this PaymentIntent’s payment method is not

card

_

present

, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is

card

_

present

and isn’t a digital wallet, then a

generated_card

payment method representing the card is created and attached to the Account instead.

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

ID of the payment method (a PaymentMethod, Card, or

compatible Source

object) to attach to this PaymentIntent. To unset this field to null, pass in an empty string.

receipt

_

email

string

Email address that the receipt for the resulting payment will be sent to. If

receipt

_

email

is specified for a payment in live mode, a receipt will be sent regardless of your

email settings

.

setup

_

future

_

usage

enum

Indicates that you intend to make future payments with this PaymentIntent’s payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to

attach the payment method

to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don’t provide a Customer, you can still

attach

the payment method to a Customer after the transaction completes.

If the payment method is

card

_

present

and isn’t a digital wallet, Stripe creates and attaches a

generated_card

payment method representing the card to the Customer instead.

When processing card payments, Stripe uses

setup

_

future

_

usage

to help you comply with regional legislation and network rules, such as

SCA

.

If you’ve already set

setup

_

future

_

usage

and you’re performing a request using a publishable key, you can only update the value from

on

_

session

to

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

if your customer may or may not be present in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when your customer is present in your checkout flow.

shipping

object

Shipping information for this PaymentIntent.

Show child parameters

statement

_

descriptor

string

Text that appears on the customer’s statement as the statement descriptor for a non-card charge. This value overrides the account’s default statement descriptor. For information about requirements, including the 22-character limit, see

the Statement Descriptor docs

.

Setting this value for a card charge returns an error. For card charges, set the

statement_descriptor_suffix

instead.

statement

_

descriptor

_

suffix

string

Provides information about a card charge. Concatenated to the account’s

statement descriptor prefix

to form the complete statement descriptor that appears on the customer’s statement.

More parameters

Expand all

amount

_

details

object

application

_

fee

_

amount

integer

Connect only

capture

_

method

enum

secret key only

excluded

_

payment

_

method

_

types

array of enums

hooks

object

payment

_

details

object

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

transfer

_

data

object

Connect only

transfer

_

group

string

Connect only

Returns

Returns a PaymentIntent object.

POST

/

v1

/

payment_intents

/

:id

curl

https://api.stripe.com/v1/payment_intents/

pi_3MtwBwLkdIwHu7ix28a3tqPa

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

amount

"

:

2000

,

"

amount_capturable

"

:

0

,

"

amount_details

"

:

{

"

tip

"

:

{}

},

"

amount_received

"

:

0

,

"

application

"

:

null

,

"

application_fee_amount

"

:

null

,

"

automatic_payment_methods

"

:

{

"

enabled

"

:

true

},

"

canceled_at

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

capture_method

"

:

"

automatic

"

,

"

client_secret

"

:

"

pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH

"

,

"

confirmation_method

"

:

"

automatic

"

,

"

created

"

:

1680800504

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

last_payment_error

"

:

null

,

"

latest_charge

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

installments

"

:

null

,

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

},

"

link

"

:

{

"

persistent_token

"

:

null

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

,

"

link

"

],

"

processing

"

:

null

,

"

receipt_email

"

:

null

,

"

review

"

:

null

,

"

setup_future_usage

"

:

null

,

"

shipping

"

:

null

,

"

source

"

:

null

,

"

statement_descriptor

"

:

null

,

"

statement_descriptor_suffix

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

transfer_data

"

:

null

,

"

transfer_group

"

:

null

}

Retrieve a PaymentIntent

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of a PaymentIntent that has previously been created.

You can retrieve a PaymentIntent client-side using a publishable key when the

client

_

secret

is in the query string.

If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the

payment intent

object reference for more details.

Parameters

client

_

secret

string

Required if you use a publishable key.

The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.

Returns

Returns a PaymentIntent if a valid identifier was provided.

GET

/

v1

/

payment_intents

/

:id

curl

https://api.stripe.com/v1/payment_intents/

pi_3MtwBwLkdIwHu7ix28a3tqPa

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

amount

"

:

2000

,

"

amount_capturable

"

:

0

,

"

amount_details

"

:

{

"

tip

"

:

{}

},

"

amount_received

"

:

0

,

"

application

"

:

null

,

"

application_fee_amount

"

:

null

,

"

automatic_payment_methods

"

:

{

"

enabled

"

:

true

},

"

canceled_at

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

capture_method

"

:

"

automatic

"

,

"

client_secret

"

:

"

pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH

"

,

"

confirmation_method

"

:

"

automatic

"

,

"

created

"

:

1680800504

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

last_payment_error

"

:

null

,

"

latest_charge

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

installments

"

:

null

,

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

},

"

link

"

:

{

"

persistent_token

"

:

null

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

,

"

link

"

],

"

processing

"

:

null

,

"

receipt_email

"

:

null

,

"

review

"

:

null

,

"

setup_future_usage

"

:

null

,

"

shipping

"

:

null

,

"

source

"

:

null

,

"

statement_descriptor

"

:

null

,

"

statement_descriptor_suffix

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

transfer_data

"

:

null

,

"

transfer_group

"

:

null

}
