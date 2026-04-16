---
title: Payment Method Configurations | Stripe API Reference
source_url: https://docs.stripe.com/api/payment_method_configurations
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:34.810454+00:00
kind: extracted-doc
---

# Payment Method Configurations | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/payment_method_configurations

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:34.810454+00:00

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

- Payment Method Configurations | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations The Payment Method Configuration object Create a payment method configuration Update payment method configuration Retrieve payment method configuration List payment method configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Payment Method Configurations Ask about this section Copy for LLM View as Markdown PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types.
- You can have multiple configurations with different sets of payment methods for different scenarios.
- There are two types of PaymentMethodConfigurations.
- Which is used depends on the charge type : Direct configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.
- Child configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Extracted text:

Payment Method Configurations | Stripe API Reference

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

Payment Method Configurations

The Payment Method Configuration object

Create a payment method configuration

Update payment method configuration

Retrieve payment method configuration

List payment method configurations

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

Payment Method Configurations

Ask about this section

Copy for LLM

View as Markdown

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the

charge type

:

Direct

configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

Child

configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a

parent

that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are

managed in the dashboard

and are not available in this API.

Related guides:

Payment Method Configurations API

Multiple configurations on dynamic payment methods

Multiple configurations for your Connect accounts

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

payment_method_configurations

POST

/

v1

/

payment_method_configurations

/

:id

GET

/

v1

/

payment_method_configurations

/

:id

GET

/

v1

/

payment_method_configurations

The Payment Method Configuration object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

retrievable with publishable key

Unique identifier for the object.

object

string

String representing the object’s type. Objects of the same type share the same value.

active

boolean

Whether the configuration can be used for new payments.

application

nullable

string

For child configs, the Connect application associated with the configuration.

is

_

default

boolean

The default configuration is used whenever a payment method configuration is not specified.

name

string

The configuration’s name.

parent

nullable

string

For child configs, the configuration’s parent configuration.

More attributes

Expand all

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

alma

nullable

object

amazon

_

pay

nullable

object

apple

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

cartes

_

bancaires

nullable

object

cashapp

nullable

object

crypto

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

google

_

pay

nullable

object

grabpay

nullable

object

ideal

nullable

object

jcb

nullable

object

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

The Payment Method Configuration object

{

"

id

"

:

"

pmc_abcdef

"

,

"

object

"

:

"

payment_method_configuration

"

,

"

acss_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

active

"

:

true

,

"

affirm

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

afterpay_clearpay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

alipay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

apple_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

bancontact

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

card

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

cartes_bancaires

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

eps

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

giropay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

google_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

ideal

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

is_default

"

:

true

,

"

klarna

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

link

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

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

name

"

:

"

Default

"

,

"

p24

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sepa_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sofort

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

us_bank_account

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

wechat_pay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

}

}

Create a payment method configuration

Ask about this section

Copy for LLM

View as Markdown

Creates a payment method configuration

Parameters

name

string

Required unless parent is provided

Configuration name.

The maximum length is 100 characters.

parent

string

Required unless name is provided

Configuration’s parent configuration. Specify to create a child configuration.

The maximum length is 100 characters.

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

alma

object

amazon

_

pay

object

apple

_

pay

object

apple

_

pay

_

later

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

cartes

_

bancaires

object

cashapp

object

crypto

object

customer

_

balance

object

eps

object

fpx

object

fr

_

meal

_

voucher

_

conecs

object

giropay

object

google

_

pay

object

grabpay

object

ideal

object

jcb

object

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

Returns the payment method configuration object

POST

/

v1

/

payment_method_configurations

curl

https://api.stripe.com/v1/payment_method_configurations \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

name=Buy Now Pay Laters

"

Response

{

"

id

"

:

"

pmc_abcdef

"

,

"

object

"

:

"

payment_method_configuration

"

,

"

acss_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

active

"

:

true

,

"

affirm

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

afterpay_clearpay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

alipay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

apple_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

bancontact

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

card

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

cartes_bancaires

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

eps

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

giropay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

google_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

ideal

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

is_default

"

:

true

,

"

klarna

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

link

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

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

name

"

:

"

Default

"

,

"

p24

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sepa_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sofort

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

us_bank_account

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

wechat_pay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

}

}

Update payment method configuration

Ask about this section

Copy for LLM

View as Markdown

Update payment method configuration

Parameters

active

boolean

Whether the configuration can be used for new payments.

name

string

Configuration name.

The maximum length is 100 characters.

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

alma

object

amazon

_

pay

object

apple

_

pay

object

apple

_

pay

_

later

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

cartes

_

bancaires

object

cashapp

object

crypto

object

customer

_

balance

object

eps

object

fpx

object

fr

_

meal

_

voucher

_

conecs

object

giropay

object

google

_

pay

object

grabpay

object

ideal

object

jcb

object

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

An object with the updated account payment method configuration

POST

/

v1

/

payment_method_configurations

/

:id

curl

https://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

acss_debit[display_preference][preference]=on

"

Response

{

"

id

"

:

"

pmc_abcdef

"

,

"

object

"

:

"

payment_method_configuration

"

,

"

acss_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

active

"

:

true

,

"

affirm

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

afterpay_clearpay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

alipay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

apple_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

bancontact

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

card

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

cartes_bancaires

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

eps

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

giropay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

google_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

ideal

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

is_default

"

:

true

,

"

klarna

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

link

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

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

name

"

:

"

Default

"

,

"

p24

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sepa_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sofort

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

us_bank_account

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

wechat_pay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

}

}

Retrieve payment method configuration

Ask about this section

Copy for LLM

View as Markdown

Retrieve payment method configuration

Parameters

No

parameters

.

Returns

A payment method configuration object.

GET

/

v1

/

payment_method_configurations

/

:id

curl

https://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \

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

pmc_abcdef

"

,

"

object

"

:

"

payment_method_configuration

"

,

"

acss_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

active

"

:

true

,

"

affirm

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

afterpay_clearpay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

alipay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

apple_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

bancontact

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

card

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

cartes_bancaires

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

eps

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

giropay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

google_pay

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

"

}

},

"

ideal

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

is_default

"

:

true

,

"

klarna

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

link

"

:

{

"

available

"

:

true

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

on

"

,

"

value

"

:

"

on

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

name

"

:

"

Default

"

,

"

p24

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sepa_debit

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

sofort

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

us_bank_account

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

},

"

wechat_pay

"

:

{

"

available

"

:

false

,

"

display_preference

"

:

{

"

overridable

"

:

null

,

"

preference

"

:

"

off

"

,

"

value

"

:

"

off

"

}

}

}
