---
title: Disputes | Stripe API Reference
source_url: https://docs.stripe.com/api/disputes
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:13.906701+00:00
kind: extracted-doc
---

# Disputes | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/disputes

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:13.906701+00:00

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

- Disputes | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes The Dispute object Update a dispute Retrieve a dispute List all disputes Close a dispute Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Disputes Ask about this section Copy for LLM View as Markdown A dispute occurs when a customer questions your charge with their card issuer.
- When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.
- Related guide: Disputes and fraud Was this section helpful?
- Yes No Endpoints POST / v1 / disputes / :id GET / v1 / disputes / :id GET / v1 / disputes POST / v1 / disputes / :id / close The Dispute object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).

Extracted text:

Disputes | Stripe API Reference

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

The Dispute object

Update a dispute

Retrieve a dispute

List all disputes

Close a dispute

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

Disputes

Ask about this section

Copy for LLM

View as Markdown

A dispute occurs when a customer questions your charge with their card issuer.

When this happens, you have the opportunity to respond to the dispute with

evidence that shows that the charge is legitimate.

Related guide:

Disputes and fraud

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

disputes

/

:id

GET

/

v1

/

disputes

/

:id

GET

/

v1

/

disputes

POST

/

v1

/

disputes

/

:id

/

close

The Dispute object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

amount

integer

Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).

charge

string

Expandable

ID of the charge that’s disputed.

currency

enum

Three-letter

ISO currency code

, in lowercase. Must be a

supported currency

.

evidence

object

Evidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.

Show child attributes

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

payment

_

intent

nullable

string

Expandable

ID of the PaymentIntent that’s disputed.

reason

string

Reason given by cardholder for dispute. Possible values are

bank

_

cannot

_

process

,

check

_

returned

,

credit

_

not

_

processed

,

customer

_

initiated

,

debit

_

not

_

authorized

,

duplicate

,

fraudulent

,

general

,

incorrect

_

account

_

details

,

insufficient

_

funds

,

noncompliant

,

product

_

not

_

received

,

product

_

unacceptable

,

subscription

_

canceled

, or

unrecognized

. Learn more about

dispute reasons

.

status

enum

The current status of a dispute. Possible values include:

warning

_

needs

_

response

,

warning

_

under

_

review

,

warning

_

closed

,

needs

_

response

,

under

_

review

,

won

,

lost

, or

prevented

.

Possible enum values

lost

A dispute resolved in the customer’s favor.

needs

_

response

A dispute that requires a response.

prevented

A dispute that was prevented from becoming a formal chargeback.

under

_

review

A dispute under review after evidence submission.

warning

_

closed

An inquiry closed without becoming a formal dispute.

warning

_

needs

_

response

An inquiry that requires a response.

warning

_

under

_

review

An inquiry under review after evidence submission.

won

A dispute resolved in the merchant’s favor.

More attributes

Expand all

object

string

balance

_

transactions

array of objects

created

timestamp

enhanced

_

eligibility

_

types

array of enums

evidence

_

details

object

is

_

charge

_

refundable

boolean

livemode

boolean

payment

_

method

_

details

nullable

object

The Dispute object

{

"

id

"

:

"

du_1MtJUT2eZvKYlo2CNaw2HvEv

"

,

"

object

"

:

"

dispute

"

,

"

amount

"

:

1000

,

"

balance_transactions

"

:

[],

"

charge

"

:

"

ch_1AZtxr2eZvKYlo2CJDX8whov

"

,

"

created

"

:

1680651737

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

evidence

"

:

{

"

access_activity_log

"

:

null

,

"

billing_address

"

:

null

,

"

cancellation_policy

"

:

null

,

"

cancellation_policy_disclosure

"

:

null

,

"

cancellation_rebuttal

"

:

null

,

"

customer_communication

"

:

null

,

"

customer_email_address

"

:

null

,

"

customer_name

"

:

null

,

"

customer_purchase_ip

"

:

null

,

"

customer_signature

"

:

null

,

"

duplicate_charge_documentation

"

:

null

,

"

duplicate_charge_explanation

"

:

null

,

"

duplicate_charge_id

"

:

null

,

"

product_description

"

:

null

,

"

receipt

"

:

null

,

"

refund_policy

"

:

null

,

"

refund_policy_disclosure

"

:

null

,

"

refund_refusal_explanation

"

:

null

,

"

service_date

"

:

null

,

"

service_documentation

"

:

null

,

"

shipping_address

"

:

null

,

"

shipping_carrier

"

:

null

,

"

shipping_date

"

:

null

,

"

shipping_documentation

"

:

null

,

"

shipping_tracking_number

"

:

null

,

"

uncategorized_file

"

:

null

,

"

uncategorized_text

"

:

null

},

"

evidence_details

"

:

{

"

due_by

"

:

1682294399

,

"

has_evidence

"

:

false

,

"

past_due

"

:

false

,

"

submission_count

"

:

0

},

"

is_charge_refundable

"

:

true

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

payment_intent

"

:

null

,

"

reason

"

:

"

general

"

,

"

status

"

:

"

warning_needs_response

"

}

Update a dispute

Ask about this section

Copy for LLM

View as Markdown

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your

dashboard

, but if you prefer, you can use the API to submit evidence programmatically.

Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our

guide to dispute types

.

Parameters

evidence

object

Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.

Show child parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

submit

boolean

Whether to immediately submit evidence to the bank. If

false

, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to

true

(the default).

Returns

Returns the dispute object.

POST

/

v1

/

disputes

/

:id

curl

https://api.stripe.com/v1/disputes/

du_1MtJUT2eZvKYlo2CNaw2HvEv

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

du_1MtJUT2eZvKYlo2CNaw2HvEv

"

,

"

object

"

:

"

dispute

"

,

"

amount

"

:

1000

,

"

balance_transactions

"

:

[],

"

charge

"

:

"

ch_1AZtxr2eZvKYlo2CJDX8whov

"

,

"

created

"

:

1680651737

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

evidence

"

:

{

"

access_activity_log

"

:

null

,

"

billing_address

"

:

null

,

"

cancellation_policy

"

:

null

,

"

cancellation_policy_disclosure

"

:

null

,

"

cancellation_rebuttal

"

:

null

,

"

customer_communication

"

:

null

,

"

customer_email_address

"

:

null

,

"

customer_name

"

:

null

,

"

customer_purchase_ip

"

:

null

,

"

customer_signature

"

:

null

,

"

duplicate_charge_documentation

"

:

null

,

"

duplicate_charge_explanation

"

:

null

,

"

duplicate_charge_id

"

:

null

,

"

product_description

"

:

null

,

"

receipt

"

:

null

,

"

refund_policy

"

:

null

,

"

refund_policy_disclosure

"

:

null

,

"

refund_refusal_explanation

"

:

null

,

"

service_date

"

:

null

,

"

service_documentation

"

:

null

,

"

shipping_address

"

:

null

,

"

shipping_carrier

"

:

null

,

"

shipping_date

"

:

null

,

"

shipping_documentation

"

:

null

,

"

shipping_tracking_number

"

:

null

,

"

uncategorized_file

"

:

null

,

"

uncategorized_text

"

:

null

},

"

evidence_details

"

:

{

"

due_by

"

:

1682294399

,

"

has_evidence

"

:

false

,

"

past_due

"

:

false

,

"

submission_count

"

:

0

},

"

is_charge_refundable

"

:

true

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

payment_intent

"

:

null

,

"

reason

"

:

"

general

"

,

"

status

"

:

"

warning_needs_response

"

}

Retrieve a dispute

Ask about this section

Copy for LLM

View as Markdown

Retrieves the dispute with the given ID.

Parameters

No

parameters

.

Returns

Returns a dispute if a valid dispute ID was provided.

Raises

an error

otherwise.

GET

/

v1

/

disputes

/

:id

curl

https://api.stripe.com/v1/disputes/

du_1MtJUT2eZvKYlo2CNaw2HvEv

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

du_1MtJUT2eZvKYlo2CNaw2HvEv

"

,

"

object

"

:

"

dispute

"

,

"

amount

"

:

1000

,

"

balance_transactions

"

:

[],

"

charge

"

:

"

ch_1AZtxr2eZvKYlo2CJDX8whov

"

,

"

created

"

:

1680651737

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

evidence

"

:

{

"

access_activity_log

"

:

null

,

"

billing_address

"

:

null

,

"

cancellation_policy

"

:

null

,

"

cancellation_policy_disclosure

"

:

null

,

"

cancellation_rebuttal

"

:

null

,

"

customer_communication

"

:

null

,

"

customer_email_address

"

:

null

,

"

customer_name

"

:

null

,

"

customer_purchase_ip

"

:

null

,

"

customer_signature

"

:

null

,

"

duplicate_charge_documentation

"

:

null

,

"

duplicate_charge_explanation

"

:

null

,

"

duplicate_charge_id

"

:

null

,

"

product_description

"

:

null

,

"

receipt

"

:

null

,

"

refund_policy

"

:

null

,

"

refund_policy_disclosure

"

:

null

,

"

refund_refusal_explanation

"

:

null

,

"

service_date

"

:

null

,

"

service_documentation

"

:

null

,

"

shipping_address

"

:

null

,

"

shipping_carrier

"

:

null

,

"

shipping_date

"

:

null

,

"

shipping_documentation

"

:

null

,

"

shipping_tracking_number

"

:

null

,

"

uncategorized_file

"

:

null

,

"

uncategorized_text

"

:

null

},

"

evidence_details

"

:

{

"

due_by

"

:

1682294399

,

"

has_evidence

"

:

false

,

"

past_due

"

:

false

,

"

submission_count

"

:

0

},

"

is_charge_refundable

"

:

true

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

payment_intent

"

:

null

,

"

reason

"

:

"

general

"

,

"

status

"

:

"

warning_needs_response

"

}

List all disputes

Ask about this section

Copy for LLM

View as Markdown

Returns a list of your disputes.

Parameters

charge

string

Only return disputes associated to the charge specified by this charge ID.

payment

_

intent

string

Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.

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

property that contains an array of up to

limit

disputes, starting after dispute

starting

_

after

. Each entry in the array is a separate dispute object. If no more disputes are available, the resulting array will be empty.

GET

/

v1

/

disputes

curl

-G https://api.stripe.com/v1/disputes \

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

/v1/disputes

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

du_1MtJUT2eZvKYlo2CNaw2HvEv

"

,

"

object

"

:

"

dispute

"

,

"

amount

"

:

1000

,

"

balance_transactions

"

:

[],

"

charge

"

:

"

ch_1AZtxr2eZvKYlo2CJDX8whov

"

,

"

created

"

:

1680651737

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

evidence

"

:

{

"

access_activity_log

"

:

null

,

"

billing_address

"

:

null

,

"

cancellation_policy

"

:

null

,

"

cancellation_policy_disclosure

"

:

null

,

"

cancellation_rebuttal

"

:

null

,

"

customer_communication

"

:

null

,

"

customer_email_address

"

:

null

,

"

customer_name

"

:

null

,

"

customer_purchase_ip

"

:

null

,

"

customer_signature

"

:

null

,

"

duplicate_charge_documentation

"

:

null

,

"

duplicate_charge_explanation

"

:

null

,

"

duplicate_charge_id

"

:

null

,

"

product_description

"

:

null

,

"

receipt

"

:

null

,

"

refund_policy

"

:

null

,

"

refund_policy_disclosure

"

:

null

,

"

refund_refusal_explanation

"

:

null

,

"

service_date

"

:

null

,

"

service_documentation

"

:

null

,

"

shipping_address

"

:

null

,

"

shipping_carrier

"

:

null

,

"

shipping_date

"

:

null

,

"

shipping_documentation

"

:

null

,

"

shipping_tracking_number

"

:

null

,

"

uncategorized_file

"

:

null

,

"

uncategorized_text

"

:

null

},

"

evidence_details

"

:

{

"

due_by

"

:

1682294399

,

"

has_evidence

"

:

false

,

"

past_due

"

:

false

,

"

submission_count

"

:

0

},

"

is_charge_refundable

"

:

true

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

payment_intent

"

:

null

,

"

reason

"

:

"

general

"

,

"

status

"

:

"

warning_needs_response

"

}

]

}
