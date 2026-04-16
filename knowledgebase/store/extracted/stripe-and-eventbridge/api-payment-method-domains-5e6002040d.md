---
title: Payment Method Domains | Stripe API Reference
source_url: https://docs.stripe.com/api/payment_method_domains
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:35.772094+00:00
kind: extracted-doc
---

# Payment Method Domains | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/payment_method_domains

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:35.772094+00:00

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

- Payment Method Domains | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains The PaymentMethodDomain object Create a payment method domain Update a payment method domain Retrieve a payment method domain List payment method domains Validate an existing payment method domain Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Payment Method Domains Ask about this section Copy for LLM View as Markdown A payment method domain represents a web domain that you have registered with Stripe.
- Stripe Elements use registered payment method domains to control where certain payment methods are shown.
- Yes No Endpoints POST / v1 / payment_method_domains POST / v1 / payment_method_domains / :id GET / v1 / payment_method_domains / :id GET / v1 / payment_method_domains POST / v1 / payment_method_domains / :id / validate The PaymentMethodDomain object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- domain _ name string The domain name that this payment method domain object represents.
- enabled boolean Whether this payment method domain is enabled.

Extracted text:

Payment Method Domains | Stripe API Reference

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

Payment Method Domains

The PaymentMethodDomain object

Create a payment method domain

Update a payment method domain

Retrieve a payment method domain

List payment method domains

Validate an existing payment method domain

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

Payment Method Domains

Ask about this section

Copy for LLM

View as Markdown

A payment method domain represents a web domain that you have registered with Stripe.

Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guide:

Payment method domains

.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

payment_method_domains

POST

/

v1

/

payment_method_domains

/

:id

GET

/

v1

/

payment_method_domains

/

:id

GET

/

v1

/

payment_method_domains

POST

/

v1

/

payment_method_domains

/

:id

/

validate

The PaymentMethodDomain object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

domain

_

name

string

The domain name that this payment method domain object represents.

enabled

boolean

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

More attributes

Expand all

object

string

amazon

_

pay

object

apple

_

pay

object

created

timestamp

google

_

pay

object

klarna

object

link

object

livemode

boolean

paypal

object

The PaymentMethodDomain object

{

"

id

"

:

"

pmd_1Nnrer2eZvKYlo2Cips79tWl

"

,

"

object

"

:

"

payment_method_domain

"

,

"

apple_pay

"

:

{

"

status

"

:

"

active

"

},

"

created

"

:

1694129445

,

"

domain_name

"

:

"

example.com

"

,

"

enabled

"

:

true

,

"

google_pay

"

:

{

"

status

"

:

"

active

"

},

"

link

"

:

{

"

status

"

:

"

active

"

},

"

livemode

"

:

false

,

"

paypal

"

:

{

"

status

"

:

"

active

"

}

}

Create a payment method domain

Ask about this section

Copy for LLM

View as Markdown

Creates a payment method domain.

Parameters

domain

_

name

string

Required

The domain name that this payment method domain object represents.

enabled

boolean

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

Returns

Returns a payment method domain object.

POST

/

v1

/

payment_method_domains

curl

https://api.stripe.com/v1/payment_method_domains \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

domain_name=example.com

"

Response

{

"

id

"

:

"

pmd_1Nnrer2eZvKYlo2Cips79tWl

"

,

"

object

"

:

"

payment_method_domain

"

,

"

apple_pay

"

:

{

"

status

"

:

"

active

"

},

"

created

"

:

1694129445

,

"

domain_name

"

:

"

example.com

"

,

"

enabled

"

:

true

,

"

google_pay

"

:

{

"

status

"

:

"

active

"

},

"

link

"

:

{

"

status

"

:

"

active

"

},

"

livemode

"

:

false

,

"

paypal

"

:

{

"

status

"

:

"

active

"

}

}

Update a payment method domain

Ask about this section

Copy for LLM

View as Markdown

Updates an existing payment method domain.

Parameters

enabled

boolean

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.

Returns

Returns the updated payment method domain object.

POST

/

v1

/

payment_method_domains

/

:id

curl

https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d enabled=false

Response

{

"

id

"

:

"

pmd_1Nnrer2eZvKYlo2Cips79tWl

"

,

"

object

"

:

"

payment_method_domain

"

,

"

apple_pay

"

:

{

"

status

"

:

"

active

"

},

"

created

"

:

1694129445

,

"

domain_name

"

:

"

example.com

"

,

"

enabled

"

:

false

,

"

google_pay

"

:

{

"

status

"

:

"

active

"

},

"

link

"

:

{

"

status

"

:

"

active

"

},

"

livemode

"

:

false

,

"

paypal

"

:

{

"

status

"

:

"

active

"

}

}

Retrieve a payment method domain

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an existing payment method domain.

Parameters

No

parameters

.

Returns

Returns a payment method domain object.

GET

/

v1

/

payment_method_domains

/

:id

curl

https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \

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

pmd_1Nnrer2eZvKYlo2Cips79tWl

"

,

"

object

"

:

"

payment_method_domain

"

,

"

apple_pay

"

:

{

"

status

"

:

"

active

"

},

"

created

"

:

1694129445

,

"

domain_name

"

:

"

example.com

"

,

"

enabled

"

:

true

,

"

google_pay

"

:

{

"

status

"

:

"

active

"

},

"

link

"

:

{

"

status

"

:

"

active

"

},

"

livemode

"

:

false

,

"

paypal

"

:

{

"

status

"

:

"

active

"

}

}
