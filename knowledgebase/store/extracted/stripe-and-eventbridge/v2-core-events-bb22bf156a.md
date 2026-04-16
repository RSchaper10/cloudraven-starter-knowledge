---
title: Events | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/events
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:16.714834+00:00
kind: extracted-doc
---

# Events | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/events

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:16.714834+00:00

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

- Events | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 The Event object v2 Retrieve an Event v2 List Events v2 Ping an Event Destination v2 Types of events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Events v2 Ask about this section Copy for LLM View as Markdown Events are generated to keep you informed of activity in your business account.
- APIs in the /v2 namespace generate thin events which have small, unversioned payloads that include a reference to the ID of the object that has changed.
- The Events v2 API returns these new thin events.
- Retrieve the event object for additional data about the event.
- Use the related object ID in the event payload to fetch the API resource of the object associated with the event.

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

Events

v2

The Event object

v2

Retrieve an Event

v2

List Events

v2

Ping an Event Destination

v2

Types of events

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

v2

Ask about this section

Copy for LLM

View as Markdown

Events are generated to keep you informed of activity in your business account. APIs in the /v2 namespace generate

thin events

which have small, unversioned payloads that include a reference to the ID of the object that has changed. The Events v2 API returns these new thin events.

Retrieve the event object

for additional data about the event. Use the related object ID in the event payload to

fetch the API resource

of the object associated with the event. Comparatively, events generated by most API v1 include a versioned snapshot of an API object in their payload.

Learn more about calling API v2 endpoints.

Was this section helpful?

Yes

No

Endpoints

GET

/

v2

/

core

/

events

/

:id

GET

/

v2

/

core

/

events

POST

/

v2

/

core

/

event_destinations

/

:id

/

ping

The Event object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the event.

object

string, value is "v2.core.event"

String representing the object’s type. Objects of the same type share the same value of the object field.

changes

nullable

object

Before and after changes for the primary related object.

context

nullable

string

Authentication context needed to fetch the event or related object.

created

timestamp

Time at which the object was created.

data

nullable

object

Additional data about the event.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

reason

nullable

object

Reason for the event.

Show child attributes

related

_

object

nullable

object

Object containing the reference to API resource relevant to the event.

Show child attributes

type

string

The type of the event.

The Event object

{

"

id

"

:

"

evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u

"

,

"

object

"

:

"

v2.core.event

"

,

"

context

"

:

null

,

"

created

"

:

"

2024-09-26T17:46:22.134Z

"

,

"

data

"

:

{

"

developer_message_summary

"

:

"

There is 1 invalid event

"

,

"

reason

"

:

{

"

error_count

"

:

1

,

"

error_types

"

:

[

{

"

code

"

:

"

meter_event_no_customer_defined

"

,

"

error_count

"

:

1

,

"

sample_errors

"

:

[

{

"

error_message

"

:

"

Customer mapping key stripe_customer_id not found in payload.

"

,

"

request

"

:

{

"

identifier

"

:

"

cb447754-6880-45c2-8f2f-ef19b6ce81e9

"

}

}

]

}

]

},

"

validation_end

"

:

"

2024-09-26T17:46:20.000Z

"

,

"

validation_start

"

:

"

2024-09-26T17:46:10.000Z

"

},

"

livemode

"

:

false

,

"

reason

"

:

null

,

"

related_object

"

:

{

"

id

"

:

"

mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

,

"

type

"

:

"

billing.meter

"

,

"

url

"

:

"

/v1/billing/meters/mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

},

"

type

"

:

"

v1.billing.meter.error_report_triggered

"

}

Retrieve an Event

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an event.

Learn more about calling API v2 endpoints.

Parameters

No

parameters

.

Returns

Response attributes

id

string

Unique identifier for the event.

object

string, value is "v2.core.event"

String representing the object’s type. Objects of the same type share the same value of the object field.

changes

nullable

object

Before and after changes for the primary related object.

context

nullable

string

Authentication context needed to fetch the event or related object.

created

timestamp

Time at which the object was created.

data

nullable

object

Additional data about the event.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

reason

nullable

object

Reason for the event.

Show child attributes

related

_

object

nullable

object

Object containing the reference to API resource relevant to the event.

Show child attributes

type

string

The type of the event.

Error Codes

404

not

_

found

The resource wasn’t found.

GET

/

v2

/

core

/

events

/

:id

curl

https://api.stripe.com/v2/core/events/evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u \

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

evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u

"

,

"

object

"

:

"

v2.core.event

"

,

"

context

"

:

null

,

"

created

"

:

"

2024-09-26T17:46:22.134Z

"

,

"

data

"

:

{

"

developer_message_summary

"

:

"

There is 1 invalid event

"

,

"

reason

"

:

{

"

error_count

"

:

1

,

"

error_types

"

:

[

{

"

code

"

:

"

meter_event_no_customer_defined

"

,

"

error_count

"

:

1

,

"

sample_errors

"

:

[

{

"

error_message

"

:

"

Customer mapping key stripe_customer_id not found in payload.

"

,

"

request

"

:

{

"

identifier

"

:

"

cb447754-6880-45c2-8f2f-ef19b6ce81e9

"

}

}

]

}

]

},

"

validation_end

"

:

"

2024-09-26T17:46:20.000Z

"

,

"

validation_start

"

:

"

2024-09-26T17:46:10.000Z

"

},

"

livemode

"

:

false

,

"

reason

"

:

null

,

"

related_object

"

:

{

"

id

"

:

"

mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

,

"

type

"

:

"

billing.meter

"

,

"

url

"

:

"

/v1/billing/meters/mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

},

"

type

"

:

"

v1.billing.meter.error_report_triggered

"

}

List Events

v2

Ask about this section

Copy for LLM

View as Markdown

List events, going back up to 30 days.

Learn more about calling API v2 endpoints.

Parameters

created

object

Set of filters to query events within a range of

created

timestamps.

Show child parameters

limit

integer

The page size.

object

_

id

string

Primary object ID used to retrieve related events.

page

string

The requested page.

types

array of strings

An array of up to 20 strings containing specific event names.

Returns

Response attributes

data

array of objects

List of events.

Show child attributes

next

_

page

_

url

nullable

string

URL to fetch the next page of the list. If there are no more pages, the value is null.

previous

_

page

_

url

nullable

string

URL to fetch the previous page of the list. If there are no previous pages, the value is null.

GET

/

v2

/

core

/

events

curl

-G https://api.stripe.com/v2/core/events \

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

-d object_id=mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

Response

{

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

evt_test_65RCjj4EqW1sabcjs2Z16RCMoNQdSQkOWvfL6L5uU2K40u

"

,

"

object

"

:

"

v2.core.event

"

,

"

context

"

:

null

,

"

created

"

:

"

2024-09-26T17:46:22.134Z

"

,

"

data

"

:

{

"

developer_message_summary

"

:

"

There is 1 invalid event

"

,

"

reason

"

:

{

"

error_count

"

:

1

,

"

error_types

"

:

[

{

"

code

"

:

"

meter_event_no_customer_defined

"

,

"

error_count

"

:

1

,

"

sample_errors

"

:

[

{

"

error_message

"

:

"

Customer mapping key stripe_customer_id not found in payload.

"

,

"

request

"

:

{

"

identifier

"

:

"

cb447754-6880-45c2-8f2f-ef19b6ce81e9

"

}

}

]

}

]

},

"

validation_end

"

:

"

2024-09-26T17:46:20.000Z

"

,

"

validation_start

"

:

"

2024-09-26T17:46:10.000Z

"

},

"

livemode

"

:

false

,

"

reason

"

:

null

,

"

related_object

"

:

{

"

id

"

:

"

mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

,

"

type

"

:

"

billing.meter

"

,

"

url

"

:

"

/v1/billing/meters/mtr_test_61RCjiqdTDC91zgip41IqPCzPnxqqSVc

"

},

"

type

"

:

"

v1.billing.meter.error_report_triggered

"

}

],

"

next_page_url

"

:

null

,

"

previous_page_url

"

:

null

}

Ping an Event Destination

v2

Ask about this section

Copy for LLM

View as Markdown

Send a

ping

event to an event destination.

Learn more about calling API v2 endpoints.

Parameters

No

parameters

.

Returns

Response attributes

id

string

Unique identifier for the event.

object

string, value is "v2.core.event"

String representing the object’s type. Objects of the same type share the same value of the object field.

changes

nullable

object

Before and after changes for the primary related object.

context

nullable

string

Authentication context needed to fetch the event or related object.

created

timestamp

Time at which the object was created.

data

nullable

object

Additional data about the event.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

reason

nullable

object

Reason for the event.

Show child attributes

related

_

object

nullable

object

Object containing the reference to API resource relevant to the event.

Show child attributes

type

string

The type of the event.

Error Codes

404

not

_

found

The resource wasn’t found.

POST

/

v2

/

core

/

event_destinations

/

:id

/

ping

curl

-X POST https://api.stripe.com/v2/core/event_destinations/evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92/ping \

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

evt_test_65RM8sQH2oXnebF5Rpc16RJyfa2xSQLHJJh1sxm7H0KI92

"

,

"

object

"

:

"

v2.core.event

"

,

"

context

"

:

null

,

"

created

"

:

"

2024-10-22T16:26:54.063Z

"

,

"

data

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

reason

"

:

null

,

"

related_object

"

:

{

"

id

"

:

"

ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6

"

,

"

type

"

:

"

event_destination

"

,

"

url

"

:

"

/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6

"

},

"

type

"

:

"

v2.core.event_destination.ping

"

}
