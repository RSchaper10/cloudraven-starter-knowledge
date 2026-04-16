---
title: Payment Methods | Stripe API Reference
source_url: https://docs.stripe.com/api/payment_methods
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:33.216426+00:00
kind: extracted-doc
---

# Payment Methods | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/payment_methods

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:33.216426+00:00

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

- Payment Methods | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods The PaymentMethod object Create a PaymentMethod Update a PaymentMethod Retrieve a Customer's PaymentMethod Retrieve a PaymentMethod List a Customer's PaymentMethods List PaymentMethods Attach a PaymentMethod to a Customer Detach a PaymentMethod from a Customer Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Payment Methods Ask about this section Copy for LLM View as Markdown PaymentMethod objects represent your customer’s payment instruments.
- You can use them with PaymentIntents to collect payments or save them to Customer objects to store instrument details for future payments.
- Related guides: Payment Methods and More Payment Scenarios .
- Yes No Endpoints POST / v1 / payment_methods POST / v1 / payment_methods / :id GET / v1 / customers / :id / payment_methods / :id GET / v1 / payment_methods / :id GET / v1 / customers / :id / payment_methods GET / v1 / payment_methods POST / v1 / payment_methods / :id / attach POST / v1 / payment_methods / :id / detach The PaymentMethod object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- billing _ details object Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Extracted text:

Payment Methods | Stripe API Reference

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

Payouts

Refunds

Confirmation Token

Tokens

Payment Methods

Payment Methods

The PaymentMethod object

Create a PaymentMethod

Update a PaymentMethod

Retrieve a Customer's PaymentMethod

Retrieve a PaymentMethod

List a Customer's PaymentMethods

List PaymentMethods

Attach a PaymentMethod to a Customer

Detach a PaymentMethod from a Customer

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

Payment Methods

Ask about this section

Copy for LLM

View as Markdown

PaymentMethod objects represent your customer’s payment instruments.

You can use them with

PaymentIntents

to collect payments or save them to

Customer objects to store instrument details for future payments.

Related guides:

Payment Methods

and

More Payment Scenarios

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

payment_methods

POST

/

v1

/

payment_methods

/

:id

GET

/

v1

/

customers

/

:id

/

payment_methods

/

:id

GET

/

v1

/

payment_methods

/

:id

GET

/

v1

/

customers

/

:id

/

payment_methods

GET

/

v1

/

payment_methods

POST

/

v1

/

payment_methods

/

:id

/

attach

POST

/

v1

/

payment_methods

/

:id

/

detach

The PaymentMethod object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

billing

_

details

object

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child attributes

customer

nullable

string

Expandable

The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

type

enum

The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

Possible enum values

acss

_

debit

Pre-authorized debit payments

are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

affirm

Affirm

is a buy now, pay later payment method in the US.

afterpay

_

clearpay

Afterpay / Clearpay

is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

alipay

Alipay

is a digital wallet payment method used in China.

alma

Alma

is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

amazon

_

pay

Amazon Pay

is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

au

_

becs

_

debit

BECS Direct Debit

is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

bacs

_

debit

Bacs Direct Debit

is used to debit UK bank accounts.

bancontact

Bancontact

is a bank redirect payment method used in Belgium.

billie

Billie

is a payment method.

Show 46 more

More attributes

Expand all

object

string

acss

_

debit

nullable

object

affirm

nullable

object

afterpay

_

clearpay

nullable

object

alipay

nullable

object

allow

_

redisplay

nullable

enum

alma

nullable

object

amazon

_

pay

nullable

object

au

_

becs

_

debit

nullable

object

bacs

_

debit

nullable

object

bancontact

nullable

object

billie

nullable

object

blik

nullable

object

boleto

nullable

object

card

nullable

object

card

_

present

nullable

object

cashapp

nullable

object

created

timestamp

crypto

nullable

object

custom

nullable

object

customer

_

balance

nullable

object

eps

nullable

object

fpx

nullable

object

giropay

nullable

object

grabpay

nullable

object

ideal

nullable

object

interac

_

present

nullable

object

Preview feature

kakao

_

pay

nullable

object

klarna

nullable

object

konbini

nullable

object

kr

_

card

nullable

object

link

nullable

object

livemode

boolean

mb

_

way

nullable

object

mobilepay

nullable

object

multibanco

nullable

object

naver

_

pay

nullable

object

nz

_

bank

_

account

nullable

object

oxxo

nullable

object

p24

nullable

object

pay

_

by

_

bank

nullable

object

payco

nullable

object

paynow

nullable

object

paypal

nullable

object

paypay

nullable

object

Preview feature

payto

nullable

object

pix

nullable

object

promptpay

nullable

object

radar

_

options

nullable

object

revolut

_

pay

nullable

object

samsung

_

pay

nullable

object

satispay

nullable

object

sepa

_

debit

nullable

object

sofort

nullable

object

sunbit

nullable

object

Preview feature

swish

nullable

object

twint

nullable

object

upi

nullable

object

Preview feature

us

_

bank

_

account

nullable

object

wechat

_

pay

nullable

object

zip

nullable

object

The PaymentMethod object

{

"

id

"

:

"

pm_1Q0PsIJvEtkwdCNYMSaVuRz6

"

,

"

object

"

:

"

payment_method

"

,

"

allow_redisplay

"

:

"

unspecified

"

,

"

billing_details

"

:

{

"

address

"

:

{

"

city

"

:

null

,

"

country

"

:

null

,

"

line1

"

:

null

,

"

line2

"

:

null

,

"

postal_code

"

:

null

,

"

state

"

:

null

},

"

email

"

:

null

,

"

name

"

:

"

John Doe

"

,

"

phone

"

:

null

},

"

created

"

:

1726673582

,

"

customer

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

type

"

:

"

us_bank_account

"

,

"

us_bank_account

"

:

{

"

account_holder_type

"

:

"

individual

"

,

"

account_type

"

:

"

checking

"

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

financial_connections_account

"

:

null

,

"

fingerprint

"

:

"

LstWJFsCK7P349Bg

"

,

"

last4

"

:

"

6789

"

,

"

networks

"

:

{

"

preferred

"

:

"

ach

"

,

"

supported

"

:

[

"

ach

"

]

},

"

routing_number

"

:

"

110000000

"

,

"

status_details

"

:

{}

}

}

Create a PaymentMethod

Ask about this section

Copy for LLM

View as Markdown

Creates a PaymentMethod object. Read the

Stripe.js reference

to learn how to create PaymentMethods via Stripe.js.

Instead of creating a PaymentMethod directly, we recommend using the

PaymentIntents

API to accept a payment immediately or the

SetupIntent

API to collect payment method details ahead of a future payment.

Parameters

type

enum

Required

The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

Possible enum values

acss

_

debit

Pre-authorized debit payments

are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

affirm

Affirm

is a buy now, pay later payment method in the US.

afterpay

_

clearpay

Afterpay / Clearpay

is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

alipay

Alipay

is a digital wallet payment method used in China.

alma

Alma

is a Buy Now, Pay Later payment method that lets customers pay in 2, 3, or 4 installments.

amazon

_

pay

Amazon Pay

is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

au

_

becs

_

debit

BECS Direct Debit

is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

bacs

_

debit

Bacs Direct Debit

is used to debit UK bank accounts.

bancontact

Bancontact

is a bank redirect payment method used in Belgium.

billie

Billie

is a payment method.

Show 46 more

billing

_

details

object

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

More parameters

Expand all

acss

_

debit

object

affirm

object

afterpay

_

clearpay

object

alipay

object

allow

_

redisplay

enum

alma

object

amazon

_

pay

object

au

_

becs

_

debit

object

bacs

_

debit

object

bancontact

object

billie

object

blik

object

boleto

object

card

object

cashapp

object

crypto

object

custom

object

customer

_

balance

object

eps

object

fpx

object

giropay

object

grabpay

object

ideal

object

interac

_

present

object

Preview feature

kakao

_

pay

object

klarna

object

konbini

object

kr

_

card

object

link

object

mb

_

way

object

mobilepay

object

multibanco

object

naver

_

pay

object

nz

_

bank

_

account

object

oxxo

object

p24

object

pay

_

by

_

bank

object

payco

object

paynow

object

paypal

object

paypay

object

Preview feature

payto

object

pix

object

promptpay

object

radar

_

options

object

revolut

_

pay

object

samsung

_

pay

object

satispay

object

sepa

_

debit

object

sofort

object

sunbit

object

Preview feature

swish

object

twint

object

upi

object

Preview feature

us

_

bank

_

account

object

wechat

_

pay

object

zip

object

Returns

Returns a PaymentMethod object.

POST

/

v1

/

payment_methods

curl

https://api.stripe.com/v1/payment_methods \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d type=us_bank_account \

-d

"

us_bank_account[account_holder_type]=individual

"

\

-d

"

us_bank_account[account_number]=000123456789

"

\

-d

"

us_bank_account[routing_number]=110000000

"

\

-d

"

billing_details[name]=John Doe

"

Response

{

"

id

"

:

"

pm_1Q0PsIJvEtkwdCNYMSaVuRz6

"

,

"

object

"

:

"

payment_method

"

,

"

allow_redisplay

"

:

"

unspecified

"

,

"

billing_details

"

:

{

"

address

"

:

{

"

city

"

:

null

,

"

country

"

:

null

,

"

line1

"

:

null

,

"

line2

"

:

null

,

"

postal_code

"

:

null

,

"

state

"

:

null

},

"

email

"

:

null

,

"

name

"

:

"

John Doe

"

,

"

phone

"

:

null

},

"

created

"

:

1726673582

,

"

customer

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

type

"

:

"

us_bank_account

"

,

"

us_bank_account

"

:

{

"

account_holder_type

"

:

"

individual

"

,

"

account_type

"

:

"

checking

"

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

financial_connections_account

"

:

null

,

"

fingerprint

"

:

"

LstWJFsCK7P349Bg

"

,

"

last4

"

:

"

6789

"

,

"

networks

"

:

{

"

preferred

"

:

"

ach

"

,

"

supported

"

:

[

"

ach

"

]

},

"

routing_number

"

:

"

110000000

"

,

"

status_details

"

:

{}

}

}

Update a PaymentMethod

Ask about this section

Copy for LLM

View as Markdown

Updates a PaymentMethod object. A PaymentMethod must be attached to a customer to be updated.

Parameters

billing

_

details

object

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

More parameters

Expand all

allow

_

redisplay

enum

card

object

payto

object

us

_

bank

_

account

object

Returns

Returns a PaymentMethod object.

POST

/

v1

/

payment_methods

/

:id

curl

https://api.stripe.com/v1/payment_methods/

pm_1Q0PsIJvEtkwdCNYMSaVuRz6

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

pm_1Q0PsIJvEtkwdCNYMSaVuRz6

"

,

"

object

"

:

"

payment_method

"

,

"

allow_redisplay

"

:

"

unspecified

"

,

"

billing_details

"

:

{

"

address

"

:

{

"

city

"

:

null

,

"

country

"

:

null

,

"

line1

"

:

null

,

"

line2

"

:

null

,

"

postal_code

"

:

null

,

"

state

"

:

null

},

"

email

"

:

null

,

"

name

"

:

"

John Doe

"

,

"

phone

"

:

null

},

"

created

"

:

1726673582

,

"

customer

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

type

"

:

"

us_bank_account

"

,

"

us_bank_account

"

:

{

"

account_holder_type

"

:

"

individual

"

,

"

account_type

"

:

"

checking

"

,

"

bank_name

"

:

"

STRIPE TEST BANK

"

,

"

financial_connections_account

"

:

null

,

"

fingerprint

"

:

"

LstWJFsCK7P349Bg

"

,

"

last4

"

:

"

6789

"

,

"

networks

"

:

{

"

preferred

"

:

"

ach

"

,

"

supported

"

:

[

"

ach

"

]

},

"

routing_number

"

:

"

110000000

"

,

"

status_details

"

:

{}

}

}

Retrieve a Customer's PaymentMethod

Ask about this section

Copy for LLM

View as Markdown

Retrieves a PaymentMethod object for a given Customer.

Parameters

No

parameters

.

Returns

Returns a PaymentMethod object.

GET

/

v1

/

customers

/

:id

/

payment_methods

/

:id

curl

https://api.stripe.com/v1/customers/

cus_9s6XKzkNRiz8i3

/payment_methods/

pm_1NVChw2eZvKYlo2CHxiM5E2E

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

pm_1NVChw2eZvKYlo2CHxiM5E2E

"

,

"

object

"

:

"

payment_method

"

,

"

billing_details

"

:

{

"

address

"

:

{

"

city

"

:

null

,

"

country

"

:

null

,

"

line1

"

:

null

,

"

line2

"

:

null

,

"

postal_code

"

:

null

,

"

state

"

:

null

},

"

email

"

:

null

,

"

name

"

:

null

,

"

phone

"

:

null

},

"

card

"

:

{

"

brand

"

:

"

visa

"

,

"

checks

"

:

{

"

address_line1_check

"

:

null

,

"

address_postal_code_check

"

:

null

,

"

cvc_check

"

:

"

pass

"

},

"

country

"

:

"

US

"

,

"

exp_month

"

:

12

,

"

exp_year

"

:

2034

,

"

fingerprint

"

:

"

Xt5EWLLDS7FJjR1c

"

,

"

funding

"

:

"

credit

"

,

"

generated_from

"

:

null

,

"

last4

"

:

"

4242

"

,

"

networks

"

:

{

"

available

"

:

[

"

visa

"

],

"

preferred

"

:

null

},

"

three_d_secure_usage

"

:

{

"

supported

"

:

true

},

"

wallet

"

:

null

},

"

created

"

:

1689682128

,

"

customer

"

:

"

cus_9s6XKzkNRiz8i3

"

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

redaction

"

:

null

,

"

type

"

:

"

card

"

}
