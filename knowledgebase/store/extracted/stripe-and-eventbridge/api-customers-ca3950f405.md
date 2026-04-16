---
title: Customers | Stripe API Reference
source_url: https://docs.stripe.com/api/customers
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:05.539845+00:00
kind: extracted-doc
---

# Customers | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/customers

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:05.539845+00:00

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
- https://docs.stripe.com/api/customers/object
- https://docs.stripe.com/api/customers/create

Captured summary:

- Customers | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers The Customer object Create a customer Update a customer Retrieve a customer List all customers Delete a customer Search customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Customers Ask about this section Copy for LLM View as Markdown This object represents a customer of your business.
- Use it to create recurring charges , save payment and contact information, and track payments that belong to the same customer.
- Yes No Endpoints POST / v1 / customers POST / v1 / customers / :id GET / v1 / customers / :id GET / v1 / customers DELETE / v1 / customers / :id GET / v1 / customers / search The Customer object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- address nullable object The customer’s address.
- Show child attributes customer _ account nullable string The ID of an Account representing a customer.

Extracted text:

Customers | Stripe API Reference

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

The Customer object

Create a customer

Update a customer

Retrieve a customer

List all customers

Delete a customer

Search customers

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

Customers

Ask about this section

Copy for LLM

View as Markdown

This object represents a customer of your business. Use it to

create recurring charges

,

save payment

and contact information,

and track payments that belong to the same customer.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

customers

POST

/

v1

/

customers

/

:id

GET

/

v1

/

customers

/

:id

GET

/

v1

/

customers

DELETE

/

v1

/

customers

/

:id

GET

/

v1

/

customers

/

search

The Customer object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

address

nullable

object

The customer’s address.

Show child attributes

customer

_

account

nullable

string

The ID of an Account representing a customer. You can use this ID with any v1 API that accepts a customer_account parameter.

description

nullable

string

An arbitrary string attached to the object. Often useful for displaying to users.

email

nullable

string

The customer’s email address.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

name

nullable

string

The customer’s full name or business name.

phone

nullable

string

The customer’s phone number.

shipping

nullable

object

Mailing and shipping address for the customer. Appears on invoices emailed to this customer.

Show child attributes

tax

object

Expandable

Tax details for the customer.

Show child attributes

More attributes

Expand all

object

string

balance

integer

business

_

name

nullable

string

cash

_

balance

nullable

object

Expandable

created

timestamp

currency

nullable

string

default

_

source

nullable

string

Expandable

delinquent

nullable

boolean

discount

nullable

object

individual

_

name

nullable

string

invoice

_

credit

_

balance

object

Expandable

invoice

_

prefix

nullable

string

invoice

_

settings

object

livemode

boolean

next

_

invoice

_

sequence

nullable

integer

preferred

_

locales

nullable

array of strings

sources

nullable

object

Expandable

subscriptions

nullable

object

Expandable

tax

_

exempt

nullable

enum

tax

_

ids

nullable

object

Expandable

test

_

clock

nullable

string

Expandable

The Customer object

{

"

id

"

:

"

cus_NffrFeUfNV2Hib

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1680893993

,

"

currency

"

:

null

,

"

default_source

"

:

null

,

"

delinquent

"

:

false

,

"

description

"

:

null

,

"

email

"

:

"

jennyrosen@example.com

"

,

"

invoice_prefix

"

:

"

0759376C

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

Jenny Rosen

"

,

"

next_invoice_sequence

"

:

1

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

}

Create a customer

Ask about this section

Copy for LLM

View as Markdown

Parameters

address

object

Required if calculating taxes

The customer’s address. Learn about

country-specific requirements for calculating tax

.

Show child parameters

description

string

An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

email

string

Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to

512 characters

.

The maximum length is 512 characters.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

The customer’s full name or business name.

The maximum length is 256 characters.

payment

_

method

string

The ID of the PaymentMethod to attach to the customer.

phone

string

The customer’s phone number.

The maximum length is 20 characters.

shipping

object

The customer’s shipping information. Appears on invoices emailed to this customer.

Show child parameters

tax

object

Recommended if calculating taxes

Tax details about the customer.

Show child parameters

More parameters

Expand all

balance

integer

business

_

name

string

cash

_

balance

object

individual

_

name

string

invoice

_

prefix

string

invoice

_

settings

object

next

_

invoice

_

sequence

integer

preferred

_

locales

array of strings

source

string

tax

_

exempt

enum

tax

_

id

_

data

array of objects

test

_

clock

string

Returns

Returns the Customer object after successful customer creation.

Raises

an error

if create parameters are invalid (for example, specifying an invalid source).

POST

/

v1

/

customers

curl

https://api.stripe.com/v1/customers \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

name=Jenny Rosen

"

\

--data-urlencode

"

email=jennyrosen@example.com

"

Response

{

"

id

"

:

"

cus_NffrFeUfNV2Hib

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1680893993

,

"

currency

"

:

null

,

"

default_source

"

:

null

,

"

delinquent

"

:

false

,

"

description

"

:

null

,

"

email

"

:

"

jennyrosen@example.com

"

,

"

invoice_prefix

"

:

"

0759376C

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

Jenny Rosen

"

,

"

next_invoice_sequence

"

:

1

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

}

Update a customer

Ask about this section

Copy for LLM

View as Markdown

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided are left unchanged. For example, if you pass the

source

parameter, that becomes the customer’s active source (such as a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the

source

parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the

past

_

due

state, then the latest open invoice for the subscription with automatic collection enabled is retried. This retry doesn’t count as an automatic retry, and doesn’t affect the next regularly scheduled payment for the invoice. Changing the

default_source

for a customer doesn’t trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

Parameters

address

object

Required if calculating taxes

The customer’s address. Learn about

country-specific requirements for calculating tax

.

Show child parameters

description

string

An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

email

string

Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to

512 characters

.

The maximum length is 512 characters.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

The customer’s full name or business name.

The maximum length is 256 characters.

phone

string

The customer’s phone number.

The maximum length is 20 characters.

shipping

object

The customer’s shipping information. Appears on invoices emailed to this customer.

Show child parameters

tax

object

Recommended if calculating taxes

Tax details about the customer.

Show child parameters

More parameters

Expand all

balance

integer

business

_

name

string

cash

_

balance

object

default

_

source

string

individual

_

name

string

invoice

_

prefix

string

invoice

_

settings

object

next

_

invoice

_

sequence

integer

preferred

_

locales

array of strings

source

string

tax

_

exempt

enum

Returns

Returns the customer object if the update succeeded.

Raises

an error

if update parameters are invalid (for example, specifying an invalid source).

POST

/

v1

/

customers

/

:id

curl

https://api.stripe.com/v1/customers/

cus_NffrFeUfNV2Hib

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

cus_NffrFeUfNV2Hib

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1680893993

,

"

currency

"

:

null

,

"

default_source

"

:

null

,

"

delinquent

"

:

false

,

"

description

"

:

null

,

"

email

"

:

"

jennyrosen@example.com

"

,

"

invoice_prefix

"

:

"

0759376C

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

name

"

:

"

Jenny Rosen

"

,

"

next_invoice_sequence

"

:

1

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

}

Retrieve a customer

Ask about this section

Copy for LLM

View as Markdown

Retrieves a Customer object.

Parameters

No

parameters

.

Returns

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a

deleted

property that’s set to true.

GET

/

v1

/

customers

/

:id

curl

https://api.stripe.com/v1/customers/

cus_NffrFeUfNV2Hib

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

cus_NffrFeUfNV2Hib

"

,

"

object

"

:

"

customer

"

,

"

address

"

:

null

,

"

balance

"

:

0

,

"

created

"

:

1680893993

,

"

currency

"

:

null

,

"

default_source

"

:

null

,

"

delinquent

"

:

false

,

"

description

"

:

null

,

"

email

"

:

"

jennyrosen@example.com

"

,

"

invoice_prefix

"

:

"

0759376C

"

,

"

invoice_settings

"

:

{

"

custom_fields

"

:

null

,

"

default_payment_method

"

:

null

,

"

footer

"

:

null

,

"

rendering_options

"

:

null

},

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

Jenny Rosen

"

,

"

next_invoice_sequence

"

:

1

,

"

phone

"

:

null

,

"

preferred_locales

"

:

[],

"

shipping

"

:

null

,

"

tax_exempt

"

:

"

none

"

,

"

test_clock

"

:

null

}
