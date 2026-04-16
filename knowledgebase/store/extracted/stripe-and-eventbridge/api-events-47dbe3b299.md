---
title: Events | Stripe API Reference
source_url: https://docs.stripe.com/api/events
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:15.545466+00:00
kind: extracted-doc
---

# Events | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/events

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:15.545466+00:00

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

- Events | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events The Event object Retrieve an event List all events Types of events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Events Ask about this section Copy for LLM View as Markdown Snapshot events allow you to track and react to activity in your Stripe integration.
- When the state of another API resource changes, Stripe creates an Event object that contains all the relevant information associated with that action, including the affected API resource.
- For example, a successful payment triggers a charge .
- succeeded event, which contains the Charge in the event’s data property.
- For example, if you create a new subscription for a customer, it triggers both a customer .

Extracted text:

Events | Stripe API Reference

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

The Event object

Retrieve an event

List all events

Types of events

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

Events

Ask about this section

Copy for LLM

View as Markdown

Snapshot events allow you to track and react to activity in your Stripe integration. When

the state of another API resource changes, Stripe creates an

Event

object that contains

all the relevant information associated with that action, including the affected API

resource. For example, a successful payment triggers a

charge

.

succeeded

event, which

contains the

Charge

in the event’s data property. Some actions trigger multiple events.

For example, if you create a new subscription for a customer, it triggers both a

customer

.

subscription

.

created

event and a

charge

.

succeeded

event.

Configure an event destination in your account to listen for events that represent actions

your integration needs to respond to. Additionally, you can retrieve an individual event or

a list of events from the API.

Connect

platforms can also receive event notifications

that occur in their connected accounts. These events include an account attribute that

identifies the relevant connected account.

You can access events through the

Retrieve Event API

for 30 days.

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

events

/

:id

GET

/

v1

/

events

The Event object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

api

_

version

nullable

string

The Stripe API version used to render

data

when the event was created. The contents of

data

never change, so this value remains static regardless of the API version currently in use. This property is populated only for events created on or after October 31, 2014.

data

object

Object containing data associated with the event.

Show child attributes

request

nullable

object

Information on the API request that triggers the event.

Show child attributes

type

string

Description of the event (for example,

invoice

.

created

or

charge

.

refunded

).

More attributes

Expand all

object

string

account

nullable

string

Connect only

context

nullable

string

created

timestamp

livemode

boolean

pending

_

webhooks

integer

The Event object

{

"

id

"

:

"

evt_1NG8Du2eZvKYlo2CUI79vXWy

"

,

"

object

"

:

"

event

"

,

"

api_version

"

:

"

2019-02-19

"

,

"

created

"

:

1686089970

,

"

data

"

:

{

"

object

"

:

{

"

id

"

:

"

seti_1NG8Du2eZvKYlo2C9XMqbR0x

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

automatic_payment_methods

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

seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ

"

,

"

created

"

:

1686089970

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

"

pm_1NG8Du2eZvKYlo2CYzzldNr7

"

,

"

payment_method_options

"

:

{

"

acss_debit

"

:

{

"

currency

"

:

"

cad

"

,

"

mandate_options

"

:

{

"

interval_description

"

:

"

First day of every month

"

,

"

payment_schedule

"

:

"

interval

"

,

"

transaction_type

"

:

"

personal

"

},

"

verification_method

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

acss_debit

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

requires_confirmation

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

},

"

livemode

"

:

false

,

"

pending_webhooks

"

:

0

,

"

request

"

:

{

"

id

"

:

null

,

"

idempotency_key

"

:

null

},

"

type

"

:

"

setup_intent.created

"

}

Retrieve an event

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an event if it was created in the last 30 days. Supply the unique identifier of the event, which you might have received in a webhook.

Parameters

No

parameters

.

Returns

Returns an event object if a valid identifier was provided. All events share a common structure, detailed to the right. The only property that will differ is the

data

property.

In each case, the

data

dictionary

will have an attribute called

object

and its value will be the same as retrieving the same object directly from the API. For example, a

customer

.

created

event will have the same information as retrieving the relevant customer would.

In cases where the attributes of an object have changed,

data

will also contain a

dictionary

containing the changes.

GET

/

v1

/

events

/

:id

curl

https://api.stripe.com/v1/events/evt_1NG8Du2eZvKYlo2CUI79vXWy \

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

evt_1NG8Du2eZvKYlo2CUI79vXWy

"

,

"

object

"

:

"

event

"

,

"

api_version

"

:

"

2019-02-19

"

,

"

created

"

:

1686089970

,

"

data

"

:

{

"

object

"

:

{

"

id

"

:

"

seti_1NG8Du2eZvKYlo2C9XMqbR0x

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

automatic_payment_methods

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

seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ

"

,

"

created

"

:

1686089970

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

"

pm_1NG8Du2eZvKYlo2CYzzldNr7

"

,

"

payment_method_options

"

:

{

"

acss_debit

"

:

{

"

currency

"

:

"

cad

"

,

"

mandate_options

"

:

{

"

interval_description

"

:

"

First day of every month

"

,

"

payment_schedule

"

:

"

interval

"

,

"

transaction_type

"

:

"

personal

"

},

"

verification_method

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

acss_debit

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

requires_confirmation

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

},

"

livemode

"

:

false

,

"

pending_webhooks

"

:

0

,

"

request

"

:

{

"

id

"

:

null

,

"

idempotency_key

"

:

null

},

"

type

"

:

"

setup_intent.created

"

}

List all events

Ask about this section

Copy for LLM

View as Markdown

List events, going back up to 30 days. Each event data is rendered according to Stripe API version at its creation time, specified in

event object

api

_

version

attribute (not according to your current Stripe API version or

Stripe-Version

header).

Parameters

types

array of strings

An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either

type

or

types

, but not both.

More parameters

Expand all

created

object

delivery

_

success

boolean

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

type

string

Returns

A

dictionary

with a

data

property that contains an array of up to

limit

events, starting after event

starting

_

after

. Each entry in the array is a separate event object. If no more events are available, the resulting array will be empty.

GET

/

v1

/

events

curl

-G https://api.stripe.com/v1/events \

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

/v1/events

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

evt_1NG8Du2eZvKYlo2CUI79vXWy

"

,

"

object

"

:

"

event

"

,

"

api_version

"

:

"

2019-02-19

"

,

"

created

"

:

1686089970

,

"

data

"

:

{

"

object

"

:

{

"

id

"

:

"

seti_1NG8Du2eZvKYlo2C9XMqbR0x

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

automatic_payment_methods

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

seti_1NG8Du2eZvKYlo2C9XMqbR0x_secret_O2CdhLwGFh2Aej7bCY7qp8jlIuyR8DJ

"

,

"

created

"

:

1686089970

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

"

pm_1NG8Du2eZvKYlo2CYzzldNr7

"

,

"

payment_method_options

"

:

{

"

acss_debit

"

:

{

"

currency

"

:

"

cad

"

,

"

mandate_options

"

:

{

"

interval_description

"

:

"

First day of every month

"

,

"

payment_schedule

"

:

"

interval

"

,

"

transaction_type

"

:

"

personal

"

},

"

verification_method

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

acss_debit

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

requires_confirmation

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

},

"

livemode

"

:

false

,

"

pending_webhooks

"

:

0

,

"

request

"

:

{

"

id

"

:

null

,

"

idempotency_key

"

:

null

},

"

type

"

:

"

setup_intent.created

"

}

]

}

Types of events

Ask about this section

Copy for LLM

View as Markdown

This is a list of all public snapshot events we currently send for /v1 resources, which is continually evolving and expanding.

Stripe events use the

resource

.

event

naming convention. Events that occur on subresources like

customer

.

subscription

.

updated

don’t trigger a corresponding event for the parent resource (

customer

.

updated

).

Stripe creates event types marked as

Selection required

only when at least one

webhook

is listening for it. A webhook set to listen to all events doesn’t satisfy this requirement and won’t generate

Selection required

event types.

Event types

account

.

application

.

authorized

data

.

object

is an application

Occurs whenever a user authorizes an application. Sent to the related application only.

account

.

application

.

deauthorized

data

.

object

is an application

Occurs whenever a user deauthorizes an application. Sent to the related application only.

account

.

external

_

account

.

created

data

.

object

is an external account (e.g.,

card

or

bank account

)

Occurs whenever an external account is created.

account

.

external

_

account

.

deleted

data

.

object

is an external account (e.g.,

card

or

bank account

)

Occurs whenever an external account is deleted.

account

.

external

_

account

.

updated

data

.

object

is an external account (e.g.,

card

or

bank account

)

Occurs whenever an external account is updated.

account

.

updated

data

.

object

is

an

account

Occurs whenever an account status or property has changed.

application

_

fee

.

created

data

.

object

is

an

application fee

Occurs whenever an application fee is created on a charge.

application

_

fee

.

refund

.

updated

data

.

object

is

a

fee refund

Occurs whenever an application fee refund is updated.

application

_

fee

.

refunded

data

.

object

is

an

application fee

Occurs whenever an application fee is refunded, whether from refunding a charge or from

refunding the application fee directly

. This includes partial refunds.

balance

_

settings

.

updated

data

.

object

is

a

balance settings

Occurs whenever a balance settings status or property has changed.

balance

.

available

data

.

object

is

a

balance

Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

billing

_

portal

.

configuration

.

created

data

.

object

is

a

billing portal configuration

Occurs whenever a portal configuration is created.

billing

_

portal

.

configuration

.

updated

data

.

object

is

a

billing portal configuration

Occurs whenever a portal configuration is updated.

billing

_

portal

.

session

.

created

data

.

object

is

a

billing portal session

Occurs whenever a portal session is created.

billing

.

alert

.

triggered

data

.

object

is

a

billing alert triggered

Occurs whenever your custom alert threshold is met.

billing

.

credit

_

balance

_

transaction

.

created

data

.

object

is

a

billing credit balance transaction

Occurs when a credit balance transaction is created

billing

.

credit

_

grant

.

created

data

.

object

is

a

billing credit grant

Occurs when a credit grant is created

billing

.

credit

_

grant

.

updated

data

.

object

is

a

billing credit grant

Occurs when a credit grant is updated

billing

.

meter

.

created

data

.

object

is

a

billing meter

Occurs when a meter is created

billing

.

meter

.

deactivated

data

.

object

is

a

billing meter

Occurs when a meter is deactivated

billing

.

meter

.

reactivated

data

.

object

is

a

billing meter

Occurs when a meter is reactivated

billing

.

meter

.

updated

data

.

object

is

a

billing meter

Occurs when a meter is updated

capability

.

updated

data

.

object

is

a

capability

Occurs whenever a capability has new requirements or a new status.

cash

_

balance

.

funds

_

available

data

.

object

is

a

cash balance

Occurs whenever there is a positive remaining cash balance after Stripe automatically reconciles new funds into the cash balance. If you enabled manual reconciliation, this webhook will fire whenever there are new funds into the cash balance.

charge

.

captured

data

.

object

is

a

charge

Occurs whenever a previously uncaptured charge is captured.

charge

.

dispute

.

closed

data

.

object

is

a

dispute

Occurs when a dispute is closed and the dispute status changes to

lost

,

warning

_

closed

, or

won

.

charge

.

dispute

.

created

data

.

object

is

a

dispute

Occurs whenever a customer disputes a charge with their bank.

charge

.

dispute

.

funds

_

reinstated

data

.

object

is

a

dispute

Occurs when funds are reinstated to your account after a dispute is closed. This includes

partially refunded payments

.

charge

.

dispute

.

funds

_

withdrawn

data

.

object

is

a

dispute

Occurs when funds are removed from your account due to a dispute.

charge

.

dispute

.

updated

data

.

object

is

a

dispute

Occurs when the dispute is updated (usually with evidence).

charge

.

expired

data

.

object

is

a

charge

Occurs whenever an uncaptured charge expires.

charge

.

failed

data

.

object

is

a

charge

Occurs whenever a failed charge attempt occurs.

charge

.

pending

data

.

object

is

a

charge

Occurs whenever a pending charge is created.

charge

.

refund

.

updated

data

.

object

is

a

refund

Occurs whenever a refund is updated on selected payment methods. For updates on all refunds, listen to

refund

.

updated

instead.

charge

.

refunded

data

.

object

is

a

charge

Occurs whenever a charge is refunded, including partial refunds. Listen to

refund

.

created

for information about the refund.

charge

.

succeeded

data

.

object

is

a

charge

Occurs whenever a charge is successful.

charge

.

updated

data

.

object

is

a

charge

Occurs whenever a charge description or metadata is updated, or upon an asynchronous capture.

checkout

.

session

.

async

_

payment

_

failed

data

.

object

is

a

checkout session

Occurs when a payment intent using a delayed payment method fails.

checkout

.

session

.

async

_

payment

_

succeeded

data

.

object

is

a

checkout session

Occurs when a payment intent using a delayed payment method finally succeeds.

checkout

.

session

.

completed

data

.

object

is

a

checkout session

Occurs when a Checkout Session has been successfully completed.

checkout

.

session

.

expired

data

.

object

is

a

checkout session

Occurs when a Checkout Session is expired.

climate

.

order

.

canceled

data

.

object

is

a

climate order

Occurs when a Climate order is canceled.

climate

.

order

.

created

data

.

object

is

a

climate order

Occurs when a Climate order is created.

climate

.

order

.

delayed

data

.

object

is

a

climate order

Occurs when a Climate order is delayed.

climate

.

order

.

delivered

data

.

object

is

a

climate order

Occurs when a Climate order is delivered.

climate

.

order

.

product

_

substituted

data

.

object

is

a

climate order

Occurs when a Climate order’s product is substituted for another.

climate

.

product

.

created

data

.

object

is

a

climate product

Occurs when a Climate product is created.

climate

.

product

.

pricing

_

updated

data

.

object

is

a

climate product

Occurs when a Climate product is updated.

coupon

.

created

data

.

object

is

a

coupon

Occurs whenever a coupon is created.

coupon

.

deleted

data

.

object

is

a

coupon

Occurs whenever a coupon is deleted.

coupon

.

updated

data

.

object

is

a

coupon

Occurs whenever a coupon is updated.

credit

_

note

.

created

data

.

object

is

a

credit note

Occurs whenever a credit note is created.

credit

_

note

.

updated

data

.

object

is

a

credit note

Occurs whenever a credit note is updated.

credit

_

note

.

voided

data

.

object

is

a

credit note

Occurs whenever a credit note is voided.

customer

_

cash

_

balance

_

transaction

.

created

data

.

object

is

a

customer cash balance transaction

Occurs whenever a new customer cash balance transactions is created.

customer

.

created

data

.

object

is

a

customer

Occurs whenever a new customer is created.

customer

.

deleted

data

.

object

is

a

customer

Occurs whenever a customer is deleted.

customer

.

discount

.

created

data

.

object

is

a

discount

Occurs whenever a coupon is attached to a customer.

customer

.

discount

.

deleted

data

.

object

is

a

discount

Occurs whenever a coupon is removed from a customer.

customer

.

discount

.

updated

data

.

object

is

a

discount

Occurs whenever a customer is switched from one coupon to another.

customer

.

source

.

created

data

.

object

is a source (e.g.,

card

)

Occurs whenever a new source is created for a customer.

customer

.

source

.

deleted

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source is removed from a customer.

customer

.

source

.

expiring

data

.

object

is a source (e.g.,

card

)

Occurs whenever a card or source will expire at the end of the month. This event only works with legacy integrations using Card or Source objects. If you use the PaymentMethod API, this event won’t occur.

customer

.

source

.

updated

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source’s details are changed.

customer

.

subscription

.

created

data

.

object

is

a

subscription

Occurs whenever a customer is signed up for a new plan.

customer

.

subscription

.

deleted

data

.

object

is

a

subscription

Occurs whenever a customer’s subscription ends.

customer

.

subscription

.

paused

data

.

object

is

a

subscription

Occurs whenever a customer’s subscription is paused. Only applies when subscriptions enter

status=paused

, not when

payment collection

is paused.

customer

.

subscription

.

pending

_

update

_

applied

data

.

object

is

a

subscription

Occurs whenever a customer’s subscription’s pending update is applied, and the subscription is updated.

customer

.

subscription

.

pending

_

update

_

expired

data

.

object

is

a

subscription

Occurs whenever a customer’s subscription’s pending update expires before the related invoice is paid.

customer

.

subscription

.

resumed

data

.

object

is

a

subscription

Occurs whenever a customer’s subscription is no longer paused. Only applies when a

status=paused

subscription is

resumed

, not when

payment collection

is resumed.

customer

.

subscription

.

trial

_

will

_

end

data

.

object

is

a

subscription

Occurs three days before a subscription’s trial period is scheduled to end, or when a trial is ended immediately (using

trial

_

end=now

).

customer

.

subscription

.

updated

data

.

object

is

a

subscription

Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the status from trial to active).

customer

.

tax

_

id

.

created

data

.

object

is

a

tax id

Occurs whenever a tax ID is created for a customer.

customer

.

tax

_

id

.

deleted

data

.

object

is

a

tax id

Occurs whenever a tax ID is deleted from a customer.

customer

.

tax

_

id

.

updated

data

.

object

is

a

tax id

Occurs whenever a customer’s tax ID is updated.

customer

.

updated

data

.

object

is

a

customer

Occurs whenever any property of a customer changes.

entitlements

.

active

_

entitlement

_

summary

.

updated

data

.

object

is

an

entitlements active entitlement summary

Occurs whenever a customer’s entitlements change.

file

.

created

data

.

object

is

a

file

Occurs whenever a new Stripe-generated file is available for your account.

financial

_

connections

.

account

.

account

_

numbers

_

updated

data

.

object

is

a

financial connections account

Occurs when a Financial Connections account’s account numbers are updated.

financial

_

connections

.

account

.

created

data

.

object

is

a

financial connections account

Occurs when a new Financial Connections account is created.

financial

_

connections

.

account

.

deactivated

data

.

object

is

a

financial connections account

Occurs when a Financial Connections account’s status is updated from

active

to

inactive

.

financial

_

connections

.

account

.

disconnected

data

.

object

is

a

financial connections account

Occurs when a Financial Connections account is disconnected.

financial

_

connections

.

account

.

reactivated

data

.

object

is

a

financial connections account

Occurs when a Financial Connections account’s status is updated from

inactive

to

active

.

financial

_

connections

.

account

.

refreshed

_

balance

data

.

object

is

a

financial connections account

Occurs when an Account’s

balance

_

refresh

status transitions from

pending

to either

succeeded

or

failed

.

financial

_

connections

.

account

.

refreshed

_

ownership

data

.

object

is

a

financial connections account

Occurs when an Account’s

ownership

_

refresh

status transitions from

pending

to either

succeeded

or

failed

.

financial

_

connections

.

account

.

refreshed

_

transactions

data

.

object

is

a

financial connections account

Occurs when an Account’s

transaction

_

refresh

status transitions from

pending

to either

succeeded

or

failed

.

financial

_

connections

.

account

.

upcoming

_

account

_

number

_

expiry

data

.

object

is

a

financial connections account

Occurs when an Account’s tokenized account number is about to expire.

identity

.

verification

_

session

.

canceled

data

.

object

is

an

identity verification session

Occurs whenever a VerificationSession is canceled

identity

.

verification

_

session

.

created

data

.

object

is

an

identity verification session

Occurs whenever a VerificationSession is created

identity

.

verification

_

session

.

processing

data

.

object

is

an

identity verification session

Occurs whenever a VerificationSession transitions to processing

identity

.

verification

_

session

.

redacted

data

.

object

is

an

identity verification session

Selection required

Occurs whenever a VerificationSession is redacted.

identity

.

verification

_

session

.

requires

_

input

data

.

object

is

an

identity verification session

Occurs whenever a VerificationSession transitions to require user input

identity

.

verification

_

session

.

verified

data

.

object

is

an

identity verification session

Occurs whenever a VerificationSession transitions to verified

invoice

_

payment

.

paid

data

.

object

is

an

invoice payment

Occurs when an InvoicePayment is successfully paid.

invoice

.

created

data

.

object

is

an

invoice

Occurs whenever a new invoice is created. To learn how webhooks can be used with this event, and how they can affect it, see

Using Webhooks with Subscriptions

.

invoice

.

deleted

data

.

object

is

an

invoice

Occurs whenever a draft invoice is deleted. Note: This event is not sent for

invoice previews

.

invoice

.

finalization

_

failed

data

.

object

is

an

invoice

Occurs whenever a draft invoice cannot be finalized. See the invoice’s

last finalization error

for details.

invoice

.

finalized

data

.

object

is

an

invoice

Occurs whenever a draft invoice is finalized and updated to be an open invoice.

invoice

.

marked

_

uncollectible

data

.

object

is

an

invoice

Occurs whenever an invoice is marked uncollectible.

invoice

.

overdue

data

.

object

is

an

invoice

Occurs X number of days after an invoice becomes due—where X is determined by Automations

invoice

.

overpaid

data

.

object

is

an

invoice

Occurs when an invoice transitions to paid with a non-zero amount_overpaid.

invoice

.

paid

data

.

object

is

an

invoice

Occurs whenever an invoice payment attempt succeeds or an invoice is marked as paid out-of-band.

invoice

.

payment

_

action

_

required

data

.

object

is

an

invoice

Occurs whenever an invoice payment attempt requires further user action to complete.

invoice

.

payment

_

attempt

_

required

data

.

object

is

an

invoice

Occurs when an invoice requires a payment using a payment method that cannot be processed by Stripe.

invoice

.

payment

_

failed

data

.

object

is

an

invoice

Occurs whenever an invoice payment attempt fails, due to either a declined payment, including soft decline, or to the lack of a stored payment method.

invoice

.

payment

_

succeeded

data

.

object

is

an

invoice

Occurs whenever an invoice payment attempt succeeds.

invoice

.

sent

data

.

object

is

an

invoice

Occurs whenever an invoice email is sent out.

invoice

.

upcoming

data

.

object

is

an

invoice

Occurs X number of days before a subscription is scheduled to create an invoice that is automatically charged—where X is determined by your

subscriptions settings

. Note: The received

Invoice

object will not have an invoice ID.

invoice

.

updated

data

.

object

is

an

invoice

Occurs whenever an invoice changes (e.g., the invoice amount).

invoice

.

voided

data

.

object

is

an

invoice

Occurs whenever an invoice is voided.

invoice

.

will

_

be

_

due

data

.

object

is

an

invoice

Occurs X number of days before an invoice becomes due—where X is determined by Automations

invoiceitem

.

created

data

.

object

is

an

invoiceitem

Occurs whenever an invoice item is created.

invoiceitem

.

deleted

data

.

object

is

an

invoiceitem

Occurs whenever an invoice item is deleted.

issuing

_

authorization

.

created

data

.

object

is

an

issuing authorization

Occurs whenever an authorization is created.

issuing

_

authorization

.

request

data

.

object

is

an

issuing authorization

Selection required

Represents a synchronous request for authorization, see

Using your integration to handle authorization requests

.

issuing

_

authorization

.

updated

data

.

object

is

an

issuing authorization

Occurs whenever an authorization is updated.

issuing

_

card

.

created

data

.

object

is

an

issuing card

Occurs whenever a card is created.

issuing

_

card

.

updated

data

.

object

is

an

issuing card

Occurs whenever a card is updated.

issuing

_

cardholder

.

created

data

.

object

is

an

issuing cardholder

Occurs whenever a cardholder is created.

issuing

_

cardholder

.

updated

data

.

object

is

an

issuing cardholder

Occurs whenever a cardholder is updated.

issuing

_

dispute

.

closed

data

.

object

is

an

issuing dispute

Occurs whenever a dispute is won, lost or expired.

issuing

_

dispute

.

created

data

.

object

is

an

issuing dispute

Occurs whenever a dispute is created.

issuing

_

dispute

.

funds

_

reinstated

data

.

object

is

an

issuing dispute

Occurs whenever funds are reinstated to your account for an Issuing dispute.

issuing

_

dispute

.

funds

_

rescinded

data

.

object

is

an

issuing dispute

Occurs whenever funds are deducted from your account for an Issuing dispute.

issuing

_

dispute

.

submitted

data

.

object

is

an

issuing dispute

Occurs whenever a dispute is submitted.

issuing

_

dispute

.

updated

data

.

object

is

an

issuing dispute

Occurs whenever a dispute is updated.

issuing

_

personalization

_

design

.

activated

data

.

object

is

an

issuing personalization design

Occurs whenever a personalization design is activated following the activation of the physical bundle that belongs to it.

issuing

_

personalization

_

design

.

deactivated

data

.

object

is

an

issuing personalization design

Occurs whenever a personalization design is deactivated following the deactivation of the physical bundle that belongs to it.

issuing

_

personalization

_

design

.

rejected

data

.

object

is

an

issuing personalization design

Occurs whenever a personalization design is rejected by design review.

issuing

_

personalization

_

design

.

updated

data

.

object

is

an

issuing personalization design

Occurs whenever a personalization design is updated.

issuing

_

token

.

created

data

.

object

is

an

issuing token

Occurs whenever an issuing digital wallet token is created.

issuing

_

token

.

updated

data

.

object

is

an

issuing token

Occurs whenever an issuing digital wallet token is updated.

issuing

_

transaction

.

created

data

.

object

is

an

issuing transaction

Occurs whenever an issuing transaction is created.

issuing

_

transaction

.

purchase

_

details

_

receipt

_

updated

data

.

object

is

an

issuing transaction

Occurs whenever an issuing transaction is updated with receipt data.

issuing

_

transaction

.

updated

data

.

object

is

an

issuing transaction

Occurs whenever an issuing transaction is updated.

mandate

.

updated

data

.

object

is

a

mandate

Occurs whenever a Mandate is updated.

payment

_

intent

.

amount

_

capturable

_

updated

data

.

object

is

a

payment intent

Occurs when a PaymentIntent has funds to be captured. Check the

amount

_

capturable

property on the PaymentIntent to determine the amount that can be captured. You may capture the PaymentIntent with an

amount

_

to

_

capture

value up to the specified amount.

Learn more about capturing PaymentIntents.

payment

_

intent

.

canceled

data

.

object

is

a

payment intent

Occurs when a PaymentIntent is canceled.

payment

_

intent

.

created

data

.

object

is

a

payment intent

Occurs when a new PaymentIntent is created.

payment

_

intent

.

partially

_

funded

data

.

object

is

a

payment intent

Occurs when funds are applied to a customer_balance PaymentIntent and the ‘amount_remaining’ changes.

payment

_

intent

.

payment

_

failed

data

.

object

is

a

payment intent

Occurs when a PaymentIntent has failed the attempt to create a payment method or a payment.

payment

_

intent

.

processing

data

.

object

is

a

payment intent

Occurs when a PaymentIntent has started processing.

payment

_

intent

.

requires

_

action

data

.

object

is

a

payment intent

Occurs when a PaymentIntent transitions to requires_action state

payment

_

intent

.

succeeded

data

.

object

is

a

payment intent

Occurs when a PaymentIntent has successfully completed payment.

payment

_

link

.

created

data

.

object

is

a

payment link

Occurs when a payment link is created.

payment

_

link

.

updated

data

.

object

is

a

payment link

Occurs when a payment link is updated.

payment

_

method

.

attached

data

.

object

is

a

payment method

Occurs whenever a new payment method is attached to a customer.

payment

_

method

.

automatically

_

updated

data

.

object

is

a

payment method

Occurs whenever a payment method’s details are automatically updated by the network.

payment

_

method

.

detached

data

.

object

is

a

payment method

Occurs whenever a payment method is detached from a customer.

payment

_

method

.

updated

data

.

object

is

a

payment method

Occurs whenever a payment method is updated via the

PaymentMethod update API

.

payout

.

canceled

data

.

object

is

a

payout

Occurs whenever a payout is canceled.

payout

.

created

data

.

object

is

a

payout

Occurs whenever a payout is created.

payout

.

failed

data

.

object

is

a

payout

Occurs whenever a payout attempt fails.

payout

.

paid

data

.

object

is

a

payout

Occurs whenever a payout is

expected

to be available in the destination account. If the payout fails, a

payout

.

failed

notification is also sent, at a later time.

payout

.

reconciliation

_

completed

data

.

object

is

a

payout

Occurs whenever balance transactions paid out in an automatic payout can be queried.

payout

.

updated

data

.

object

is

a

payout

Occurs whenever a payout is updated.

person

.

created

data

.

object

is

a

person

Occurs whenever a person associated with an account is created.

person

.

deleted

data

.

object

is

a

person

Occurs whenever a person associated with an account is deleted.

person

.

updated

data

.

object

is

a

person

Occurs whenever a person associated with an account is updated.

plan

.

created

data

.

object

is

a

plan

Occurs whenever a plan is created.

plan

.

deleted

data

.

object

is

a

plan

Occurs whenever a plan is deleted.

plan

.

updated

data

.

object

is

a

plan

Occurs whenever a plan is updated.

price

.

created

data

.

object

is

a

price

Occurs whenever a price is created.

price

.

deleted

data

.

object

is

a

price

Occurs whenever a price is deleted.

price

.

updated

data

.

object

is

a

price

Occurs whenever a price is updated.

product

.

created

data

.

object

is

a

product

Occurs whenever a product is created.

product

.

deleted

data

.

object

is

a

product

Occurs whenever a product is deleted.

product

.

updated

data

.

object

is

a

product

Occurs whenever a product is updated.

promotion

_

code

.

created

data

.

object

is

a

promotion code

Occurs whenever a promotion code is created.

promotion

_

code

.

updated

data

.

object

is

a

promotion code

Occurs whenever a promotion code is updated.

quote

.

accepted

data

.

object

is

a

quote

Occurs whenever a quote is accepted.

quote

.

canceled

data

.

object

is

a

quote

Occurs whenever a quote is canceled.

quote

.

created

data

.

object

is

a

quote

Occurs whenever a quote is created.

quote

.

finalized

data

.

object

is

a

quote

Occurs whenever a quote is finalized.

quote

.

will

_

expire

data

.

object

is

a

quote

Occurs X number of days before a quote is scheduled to expire—where X is determined by Automations

radar

.

early

_

fraud

_

warning

.

created

data

.

object

is

a

radar early fraud warning

Occurs whenever an early fraud warning is created.

radar

.

early

_

fraud

_

warning

.

updated

data

.

object

is

a

radar early fraud warning

Occurs whenever an early fraud warning is updated.

refund

.

created

data

.

object

is

a

refund

Occurs whenever a refund is created.

refund

.

failed

data

.

object

is

a

refund

Occurs whenever a refund has failed.

refund

.

updated

data

.

object

is

a

refund

Occurs whenever a refund is updated.

reporting

.

report

_

run

.

failed

data

.

object

is

a

reporting report run

Occurs whenever a requested

ReportRun

failed to complete.

reporting

.

report

_

run

.

succeeded

data

.

object

is

a

reporting report run

Occurs whenever a requested

ReportRun

completed successfully.

reporting

.

report

_

type

.

updated

data

.

object

is

a

reporting report type

Selection required

Occurs whenever a

ReportType

is updated (typically to indicate that a new day’s data has come available).

reserve

.

hold

.

created

data

.

object

is

a

reserve hold

Occurs when a reserve hold is created.

reserve

.

hold

.

updated

data

.

object

is

a

reserve hold

Occurs when a reserve hold is updated.

reserve

.

plan

.

created

data

.

object

is

a

reserve plan

Occurs when a reserve plan is created.

reserve

.

plan

.

disabled

data

.

object

is

a

reserve plan

Occurs when a reserve plan is disabled.

reserve

.

plan

.

expired

data

.

object

is

a

reserve plan

Occurs when a reserve plan expires.

reserve

.

plan

.

updated

data

.

object

is

a

reserve plan

Occurs when a reserve plan is updated.

reserve

.

release

.

created

data

.

object

is

a

reserve release

Occurs when a reserve release is created.

review

.

closed

data

.

object

is

a

review

Occurs whenever a review is closed. The review’s

reason

field indicates why:

approved

,

disputed

,

refunded

,

refunded

_

as

_

fraud

, or

canceled

.

review

.

opened

data

.

object

is

a

review

Occurs whenever a review is opened.

setup

_

intent

.

canceled

data

.

object

is

a

setup intent

Occurs when a SetupIntent is canceled.

setup

_

intent

.

created

data

.

object

is

a

setup intent

Occurs when a new SetupIntent is created.

setup

_

intent

.

requires

_

action

data

.

object

is

a

setup intent

Occurs when a SetupIntent is in requires_action state.

setup

_

intent

.

setup

_

failed

data

.

object

is

a

setup intent

Occurs when a SetupIntent has failed the attempt to setup a payment method.

setup

_

intent

.

succeeded

data

.

object

is

a

setup intent

Occurs when an SetupIntent has successfully setup a payment method.

sigma

.

scheduled

_

query

_

run

.

created

data

.

object

is

a

scheduled query run

Occurs whenever a Sigma scheduled query run finishes.

source

.

canceled

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source is canceled.

source

.

chargeable

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source transitions to chargeable.

source

.

failed

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source fails.

source

.

mandate

_

notification

data

.

object

is a source (e.g.,

card

)

Occurs whenever a source mandate notification method is set to manual.

source

.

refund

_

attributes

_

required

data

.

object

is a source (e.g.,

card

)

Occurs whenever the refund attributes are required on a receiver source to process a refund or a mispayment.

source

.

transaction

.

created

data

.

object

is a

source transaction

Occurs whenever a source transaction is created.

source

.

transaction

.

updated

data

.

object

is a

source transaction

Occurs whenever a source transaction is updated.

subscription

_

schedule

.

aborted

data

.

object

is

a

subscription schedule

Occurs whenever a subscription schedule is canceled due to the underlying subscription being canceled because of delinquency.

subscription

_

schedule

.

canceled

data

.

object

is

a

subscription schedule

Occurs whenever a subscription schedule is canceled.

subscription

_

schedule

.

completed

data

.

object

is

a

subscription schedule

Occurs whenever a new subscription schedule is completed.

subscription

_

schedule

.

created

data

.

object

is

a

subscription schedule

Occurs whenever a new subscription schedule is created.

subscription

_

schedule

.

expiring

data

.

object

is

a

subscription schedule

Occurs 7 days before a subscription schedule will expire.

subscription

_

schedule

.

released

data

.

object

is

a

subscription schedule

Occurs whenever a new subscription schedule is released.

subscription

_

schedule

.

updated

data

.

object

is

a

subscription schedule

Occurs whenever a subscription schedule is updated.

tax

_

rate

.

created

data

.

object

is

a

tax rate

Occurs whenever a new tax rate is created.

tax

_

rate

.

updated

data

.

object

is

a

tax rate

Occurs whenever a tax rate is updated.

tax

.

settings

.

updated

data

.

object

is

a

tax settings

Occurs whenever tax settings is updated.

terminal

.

reader

.

action

_

failed

data

.

object

is

a

terminal reader

Occurs whenever an action sent to a Terminal reader failed.

terminal

.

reader

.

action

_

succeeded

data

.

object

is

a

terminal reader

Occurs whenever an action sent to a Terminal reader was successful.

terminal

.

reader

.

action

_

updated

data

.

object

is

a

terminal reader

Occurs whenever an action sent to a Terminal reader is updated.

test

_

helpers

.

test

_

clock

.

advancing

data

.

object

is

a

test helpers test clock

Occurs whenever a test clock starts advancing.

test

_

helpers

.

test

_

clock

.

created

data

.

object

is

a

test helpers test clock

Occurs whenever a test clock is created.

test

_

helpers

.

test

_

clock

.

deleted

data

.

object

is

a

test helpers test clock

Occurs whenever a test clock is deleted.

test

_

helpers

.

test

_

clock

.

internal

_

failure

data

.

object

is

a

test helpers test clock

Occurs whenever a test clock fails to advance its frozen time.

test

_

helpers

.

test

_

clock

.

ready

data

.

object

is

a

test helpers test clock

Occurs whenever a test clock transitions to a ready status.

topup

.

canceled

data

.

object

is

a

topup

Occurs whenever a top-up is canceled.

topup

.

created

data

.

object

is

a

topup

Occurs whenever a top-up is created.

topup

.

failed

data

.

object

is

a

topup

Occurs whenever a top-up fails.

topup

.

reversed

data

.

object

is

a

topup

Occurs whenever a top-up is reversed.

topup

.

succeeded

data

.

object

is

a

topup

Occurs whenever a top-up succeeds.

transfer

.

created

data

.

object

is

a

transfer

Occurs whenever a transfer is created.

transfer

.

reversed

data

.

object

is

a

transfer

Occurs whenever a transfer is reversed, including partial reversals.

transfer

.

updated

data

.

object

is

a

transfer

Occurs whenever a transfer’s description or metadata is updated.
