---
title: Event Destinations | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/event-destinations
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:17.882577+00:00
kind: extracted-doc
---

# Event Destinations | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/event-destinations

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:17.882577+00:00

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

- Event Destinations | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 The Event Destination object v2 Create an Event Destination v2 Update an Event Destination v2 Retrieve an Event Destination v2 List Event Destinations v2 Delete an Event Destination v2 Disable an Event Destination v2 Enable an Event Destination v2 Event Destination event types v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Event Destinations v2 Ask about this section Copy for LLM View as Markdown Set up an event destination to receive events from Stripe across multiple destination types, including webhook endpoints and Amazon EventBridge .
- Event destinations support receiving thin events and snapshot events .
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / event_destinations POST / v2 / core / event_destinations / :id GET / v2 / core / event_destinations / :id GET / v2 / core / event_destinations DELETE / v2 / core / event_destinations / :id POST / v2 / core / event_destinations / :id / disable POST / v2 / core / event_destinations / :id / enable The Event Destination object v2 Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- object string, value is "v2.core.event_destination" String representing the object’s type.

Extracted text:

Event Destinations | Stripe API Reference

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

The Event Destination object

v2

Create an Event Destination

v2

Update an Event Destination

v2

Retrieve an Event Destination

v2

List Event Destinations

v2

Delete an Event Destination

v2

Disable an Event Destination

v2

Enable an Event Destination

v2

Event Destination event types

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

Event Destinations

v2

Ask about this section

Copy for LLM

View as Markdown

Set up an event destination to receive events from Stripe across multiple destination types, including

webhook endpoints

and

Amazon EventBridge

. Event destinations support receiving

thin events

and

snapshot events

.

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

event_destinations

POST

/

v2

/

core

/

event_destinations

/

:id

GET

/

v2

/

core

/

event_destinations

/

:id

GET

/

v2

/

core

/

event_destinations

DELETE

/

v2

/

core

/

event_destinations

/

:id

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

disable

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

enable

The Event Destination object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

object

string, value is "v2.core.event_destination"

String representing the object’s type. Objects of the same type share the same value of the object field.

amazon

_

eventbridge

nullable

object

Amazon EventBridge configuration.

Show child attributes

created

timestamp

Time at which the object was created.

description

string

An optional description of what the event destination is used for.

enabled

_

events

array of strings

The list of events to enable for this endpoint.

event

_

payload

enum

Payload type of events being subscribed to.

Possible enum values

snapshot

Events from v1 APIs.

thin

Events from v2 APIs.

events

_

from

nullable

array of strings

Specifies which accounts’ events route to this destination.

@self

: Receive events from the account that owns the event destination.

@accounts

: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.

@organization

_

members

: Receive events from accounts directly linked to the organization.

@organization

_

members/@accounts

: Receive events from all accounts connected to any platform accounts in the organization.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Metadata.

name

string

Event destination name.

snapshot

_

api

_

version

nullable

string

If using the snapshot event payload, the API version events are rendered as.

status

enum

Status. It can be set to either enabled or disabled.

Possible enum values

disabled

Event destination is disabled.

enabled

Event destination is enabled.

status

_

details

nullable

object

Additional information about event destination status.

Show child attributes

type

enum

Event destination type.

Possible enum values

amazon

_

eventbridge

Amazon EventBridge.

webhook

_

endpoint

Webhook endpoint.

updated

timestamp

Time at which the object was last updated.

webhook

_

endpoint

nullable

object

Webhook endpoint configuration.

Show child attributes

The Event Destination object

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

object

"

:

"

v2.core.event_destination

"

,

"

created

"

:

"

2024-10-22T16:20:09.931Z

"

,

"

description

"

:

"

This is my event destination, I like it a lot

"

,

"

enabled_events

"

:

[

"

v1.billing.meter.error_report_triggered

"

],

"

event_payload

"

:

"

thin

"

,

"

events_from

"

:

[

"

self

"

],

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

name

"

:

"

My Event Destination

"

,

"

snapshot_api_version

"

:

null

,

"

status

"

:

"

enabled

"

,

"

status_details

"

:

null

,

"

type

"

:

"

webhook_endpoint

"

,

"

updated

"

:

"

2024-10-22T16:20:09.937Z

"

,

"

webhook_endpoint

"

:

{

"

signing_secret

"

:

null

,

"

url

"

:

"

https://example.com/my/webhook/endpoint

"

}

}

Create an Event Destination

v2

Ask about this section

Copy for LLM

View as Markdown

Create a new event destination.

Learn more about calling API v2 endpoints.

Parameters

enabled

_

events

array of strings

Required

The list of events to enable for this endpoint.

event

_

payload

enum

Required

Payload type of events being subscribed to.

Possible enum values

snapshot

Events from v1 APIs.

thin

Events from v2 APIs.

name

string

Required

Event destination name.

type

enum

Required

Event destination type.

Possible enum values

amazon

_

eventbridge

Amazon EventBridge.

webhook

_

endpoint

Webhook endpoint.

amazon

_

eventbridge

object

Amazon EventBridge configuration.

Show child parameters

description

string

An optional description of what the event destination is used for.

events

_

from

array of strings

Specifies which accounts’ events route to this destination.

@self

: Receive events from the account that owns the event destination.

@accounts

: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.

@organization

_

members

: Receive events from accounts directly linked to the organization.

@organization

_

members/@accounts

: Receive events from all accounts connected to any platform accounts in the organization.

include

array of enums

Additional fields to include in the response.

Possible enum values

webhook

_

endpoint

.

signing

_

secret

Include parameter to expose

webhook

_

endpoint

.

signing

_

secret

.

webhook

_

endpoint

.

url

Include parameter to expose

webhook

_

endpoint

.

url

.

metadata

map

Metadata.

snapshot

_

api

_

version

string

If using the snapshot event payload, the API version events are rendered as.

webhook

_

endpoint

object

Webhook endpoint configuration.

Show child parameters

Returns

Response attributes

id

string

Unique identifier for the object.

object

string, value is "v2.core.event_destination"

String representing the object’s type. Objects of the same type share the same value of the object field.

amazon

_

eventbridge

nullable

object

Amazon EventBridge configuration.

Show child attributes

created

timestamp

Time at which the object was created.

description

string

An optional description of what the event destination is used for.

enabled

_

events

array of strings

The list of events to enable for this endpoint.

event

_

payload

enum

Payload type of events being subscribed to.

Possible enum values

snapshot

Events from v1 APIs.

thin

Events from v2 APIs.

events

_

from

nullable

array of strings

Specifies which accounts’ events route to this destination.

@self

: Receive events from the account that owns the event destination.

@accounts

: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.

@organization

_

members

: Receive events from accounts directly linked to the organization.

@organization

_

members/@accounts

: Receive events from all accounts connected to any platform accounts in the organization.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Metadata.

name

string

Event destination name.

snapshot

_

api

_

version

nullable

string

If using the snapshot event payload, the API version events are rendered as.

status

enum

Status. It can be set to either enabled or disabled.

Possible enum values

disabled

Event destination is disabled.

enabled

Event destination is enabled.

status

_

details

nullable

object

Additional information about event destination status.

Show child attributes

type

enum

Event destination type.

Possible enum values

amazon

_

eventbridge

Amazon EventBridge.

webhook

_

endpoint

Webhook endpoint.

updated

timestamp

Time at which the object was last updated.

webhook

_

endpoint

nullable

object

Webhook endpoint configuration.

Show child attributes

Error Codes

400

expired

_

azure

_

partner

_

authorization

Error returned when a user tries to create an event destination with an expired Azure partner authorization.

400

invalid

_

azure

_

partner

_

authorization

Error returned when a user tries to create an event destination without an Azure partner authorization.

400

invalid

_

azure

_

partner

_

configuration

Error returned when no valid partner configuration is found using the user provided Azure subscription ID and Azure resource group name.

409

idempotency

_

error

An idempotent retry occurred with different request parameters.

POST

/

v2

/

core

/

event_destinations

curl

-X POST https://api.stripe.com/v2/core/event_destinations \

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

"name": "My Event Destination",

"description": "This is my event destination, I like it a lot",

"enabled_events": [

"v1.billing.meter.error_report_triggered"

],

"type": "webhook_endpoint",

"webhook_endpoint": {

"url": "https://example.com/my/webhook/endpoint"

},

"event_payload": "thin",

"include": [

"webhook_endpoint.url"

]

}

'

Response

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

object

"

:

"

v2.core.event_destination

"

,

"

created

"

:

"

2024-10-22T16:20:09.931Z

"

,

"

description

"

:

"

This is my event destination, I like it a lot

"

,

"

enabled_events

"

:

[

"

v1.billing.meter.error_report_triggered

"

],

"

event_payload

"

:

"

thin

"

,

"

events_from

"

:

[

"

self

"

],

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

name

"

:

"

My Event Destination

"

,

"

snapshot_api_version

"

:

null

,

"

status

"

:

"

enabled

"

,

"

status_details

"

:

null

,

"

type

"

:

"

webhook_endpoint

"

,

"

updated

"

:

"

2024-10-22T16:20:09.937Z

"

,

"

webhook_endpoint

"

:

{

"

signing_secret

"

:

null

,

"

url

"

:

"

https://example.com/my/webhook/endpoint

"

}

}

Update an Event Destination

v2

Ask about this section

Copy for LLM

View as Markdown

Update the details of an event destination.

Learn more about calling API v2 endpoints.

Parameters

description

string

An optional description of what the event destination is used for.

enabled

_

events

array of strings

The list of events to enable for this endpoint.

include

array of enums

Additional fields to include in the response. Currently supports

webhook

_

endpoint

.

url

.

Possible enum values

webhook

_

endpoint

.

url

Include parameter to expose

webhook

_

endpoint

.

url

.

metadata

map

Metadata.

name

string

Event destination name.

webhook

_

endpoint

object

Webhook endpoint configuration.

Show child parameters

Returns

Response attributes

id

string

Unique identifier for the object.

object

string, value is "v2.core.event_destination"

String representing the object’s type. Objects of the same type share the same value of the object field.

amazon

_

eventbridge

nullable

object

Amazon EventBridge configuration.

Show child attributes

created

timestamp

Time at which the object was created.

description

string

An optional description of what the event destination is used for.

enabled

_

events

array of strings

The list of events to enable for this endpoint.

event

_

payload

enum

Payload type of events being subscribed to.

Possible enum values

snapshot

Events from v1 APIs.

thin

Events from v2 APIs.

events

_

from

nullable

array of strings

Specifies which accounts’ events route to this destination.

@self

: Receive events from the account that owns the event destination.

@accounts

: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.

@organization

_

members

: Receive events from accounts directly linked to the organization.

@organization

_

members/@accounts

: Receive events from all accounts connected to any platform accounts in the organization.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Metadata.

name

string

Event destination name.

snapshot

_

api

_

version

nullable

string

If using the snapshot event payload, the API version events are rendered as.

status

enum

Status. It can be set to either enabled or disabled.

Possible enum values

disabled

Event destination is disabled.

enabled

Event destination is enabled.

status

_

details

nullable

object

Additional information about event destination status.

Show child attributes

type

enum

Event destination type.

Possible enum values

amazon

_

eventbridge

Amazon EventBridge.

webhook

_

endpoint

Webhook endpoint.

updated

timestamp

Time at which the object was last updated.

webhook

_

endpoint

nullable

object

Webhook endpoint configuration.

Show child attributes

Error Codes

404

not

_

found

The resource wasn’t found.

409

idempotency

_

error

An idempotent retry occurred with different request parameters.

POST

/

v2

/

core

/

event_destinations

/

:id

curl

-X POST https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \

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

"description": "A better description",

"enabled_events": [

"v1.billing.meter.error_report_triggered",

"v1.billing.meter.no_meter_found"

],

"include": [

"webhook_endpoint.url"

]

}

'

Response

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

object

"

:

"

v2.core.event_destination

"

,

"

created

"

:

"

2024-10-22T16:20:09.931Z

"

,

"

description

"

:

"

A better description

"

,

"

enabled_events

"

:

[

"

v1.billing.meter.error_report_triggered

"

,

"

v1.billing.meter.no_meter_found

"

],

"

event_payload

"

:

"

thin

"

,

"

events_from

"

:

[

"

self

"

],

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

name

"

:

"

My Event Destination

"

,

"

snapshot_api_version

"

:

null

,

"

status

"

:

"

disabled

"

,

"

status_details

"

:

{

"

disabled

"

:

{

"

reason

"

:

"

user

"

}

},

"

type

"

:

"

webhook_endpoint

"

,

"

updated

"

:

"

2024-10-22T16:25:48.976Z

"

,

"

webhook_endpoint

"

:

{

"

signing_secret

"

:

null

,

"

url

"

:

"

https://example.com/my/webhook/endpoint

"

}

}

Retrieve an Event Destination

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an event destination.

Learn more about calling API v2 endpoints.

Parameters

include

array of enums

Additional fields to include in the response.

Possible enum values

webhook

_

endpoint

.

url

Include parameter to expose

webhook

_

endpoint

.

url

.

Returns

Response attributes

id

string

Unique identifier for the object.

object

string, value is "v2.core.event_destination"

String representing the object’s type. Objects of the same type share the same value of the object field.

amazon

_

eventbridge

nullable

object

Amazon EventBridge configuration.

Show child attributes

created

timestamp

Time at which the object was created.

description

string

An optional description of what the event destination is used for.

enabled

_

events

array of strings

The list of events to enable for this endpoint.

event

_

payload

enum

Payload type of events being subscribed to.

Possible enum values

snapshot

Events from v1 APIs.

thin

Events from v2 APIs.

events

_

from

nullable

array of strings

Specifies which accounts’ events route to this destination.

@self

: Receive events from the account that owns the event destination.

@accounts

: Receive events emitted from other accounts you manage which includes your v1 and v2 accounts.

@organization

_

members

: Receive events from accounts directly linked to the organization.

@organization

_

members/@accounts

: Receive events from all accounts connected to any platform accounts in the organization.

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Metadata.

name

string

Event destination name.

snapshot

_

api

_

version

nullable

string

If using the snapshot event payload, the API version events are rendered as.

status

enum

Status. It can be set to either enabled or disabled.

Possible enum values

disabled

Event destination is disabled.

enabled

Event destination is enabled.

status

_

details

nullable

object

Additional information about event destination status.

Show child attributes

type

enum

Event destination type.

Possible enum values

amazon

_

eventbridge

Amazon EventBridge.

webhook

_

endpoint

Webhook endpoint.

updated

timestamp

Time at which the object was last updated.

webhook

_

endpoint

nullable

object

Webhook endpoint configuration.

Show child attributes

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

event_destinations

/

:id

curl

-G https://api.stripe.com/v2/core/event_destinations/ed_test_61RM8ltWcTW4mbsxf16RJyfa2xSQLHJJh1sxm7H0KVT6 \

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

-d

"

include[0]=webhook_endpoint.url

"

Response

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

object

"

:

"

v2.core.event_destination

"

,

"

created

"

:

"

2024-10-22T16:20:09.931Z

"

,

"

description

"

:

"

This is my event destination, I like it a lot

"

,

"

enabled_events

"

:

[

"

v1.billing.meter.error_report_triggered

"

],

"

event_payload

"

:

"

thin

"

,

"

events_from

"

:

[

"

self

"

],

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

name

"

:

"

My Event Destination

"

,

"

snapshot_api_version

"

:

null

,

"

status

"

:

"

disabled

"

,

"

status_details

"

:

{

"

disabled

"

:

{

"

reason

"

:

"

user

"

}

},

"

type

"

:

"

webhook_endpoint

"

,

"

updated

"

:

"

2024-10-22T16:22:02.524Z

"

,

"

webhook_endpoint

"

:

{

"

signing_secret

"

:

null

,

"

url

"

:

null

}

}
