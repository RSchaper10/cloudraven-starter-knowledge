---
title: Tokens | Stripe API Reference
source_url: https://docs.stripe.com/api/tokens
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:31.794711+00:00
kind: extracted-doc
---

# Tokens | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/tokens

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:31.794711+00:00

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

- Tokens | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens The Token object Create a bank account token Create a card token Create a CVC update token Create a person token Create a PII token Create an account token Retrieve a token Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Tokens Ask about this section Copy for LLM View as Markdown Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner.
- A token representing this information is returned to your server to use.
- Use our recommended payments integrations to perform this process on the client-side.
- This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.
- If you can’t use client-side tokenization, you can also create tokens using the API with either your publishable or secret API key.

Extracted text:

Tokens | Stripe API Reference

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

The Token object

Create a bank account token

Create a card token

Create a CVC update token

Create a person token

Create a PII token

Create an account token

Retrieve a token

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

Tokens

Ask about this section

Copy for LLM

View as Markdown

Tokenization is the process Stripe uses to collect sensitive card or bank

account details, or personally identifiable information (PII), directly from

your customers in a secure manner. A token representing this information is

returned to your server to use. Use our

recommended payments integrations

to perform this process

on the client-side. This guarantees that no sensitive card data touches your server,

and allows your integration to operate in a PCI-compliant way.

If you can’t use client-side tokenization, you can also create tokens using

the API with either your publishable or secret API key. If

your integration uses this method, you’re responsible for any PCI compliance

that it might require, and you must keep your secret API key safe. Unlike with

client-side tokenization, your customer’s information isn’t sent directly to

Stripe, so we can’t determine how it’s handled or stored.

You can’t store or use tokens more than once. To store card or bank account

information for later use, create

Customer

objects or

External accounts

.

Radar

, our integrated solution for automatic fraud protection,

performs best with integrations that use client-side tokenization.

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

tokens

POST

/

v1

/

tokens

POST

/

v1

/

tokens

POST

/

v1

/

tokens

POST

/

v1

/

tokens

POST

/

v1

/

tokens

GET

/

v1

/

tokens

/

:id

The Token object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

card

nullable

object

Hash describing the card used to make the charge.

Show child attributes

More attributes

Expand all

object

string

bank

_

account

nullable

object

client

_

ip

nullable

string

created

timestamp

description

nullable

string

livemode

boolean

type

string

used

boolean

The Token object

{

"

id

"

:

"

tok_1N3T00LkdIwHu7ixt44h1F8k

"

,

"

object

"

:

"

token

"

,

"

card

"

:

{

"

id

"

:

"

card_1N3T00LkdIwHu7ixRdxpVI1Q

"

,

"

object

"

:

"

card

"

,

"

address_city

"

:

null

,

"

address_country

"

:

null

,

"

address_line1

"

:

null

,

"

address_line1_check

"

:

null

,

"

address_line2

"

:

null

,

"

address_state

"

:

null

,

"

address_zip

"

:

null

,

"

address_zip_check

"

:

null

,

"

brand

"

:

"

Visa

"

,

"

country

"

:

"

US

"

,

"

cvc_check

"

:

"

unchecked

"

,

"

dynamic_last4

"

:

null

,

"

exp_month

"

:

5

,

"

exp_year

"

:

2026

,

"

fingerprint

"

:

"

mToisGZ01V71BCos

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

last4

"

:

"

4242

"

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

null

,

"

tokenization_method

"

:

null

,

"

wallet

"

:

null

},

"

client_ip

"

:

"

52.35.78.6

"

,

"

created

"

:

1683071568

,

"

livemode

"

:

false

,

"

type

"

:

"

card

"

,

"

used

"

:

false

}

Create a bank account token

Ask about this section

Copy for LLM

View as Markdown

Creates a single-use token that represents a bank account’s details.

You can use this token with any v1 API method in place of a bank account

dictionary

. You can only use this token once. To do so, attach it to a

connected account

where

controller.requirement_collection

is

application

, which includes Custom accounts.

Parameters

bank

_

account

object

The bank account this token will represent.

Show child parameters

More parameters

Expand all

customer

string

Connect only

Returns

Returns the created bank account token if it’s successful. Otherwise, this call

raises

an error

.

POST

/

v1

/

tokens

curl

https://api.stripe.com/v1/tokens \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

bank_account[country]=US

"

\

-d

"

bank_account[currency]=usd

"

\

-d

"

bank_account[account_holder_name]=Jenny Rosen

"

\

-d

"

bank_account[account_holder_type]=individual

"

\

-d

"

bank_account[routing_number]=110000000

"

\

-d

"

bank_account[account_number]=000123456789

"

Response

{

"

id

"

:

"

btok_1N3T00LkdIwHu7ixt44h1F8k

"

,

"

object

"

:

"

token

"

,

"

bank_account

"

:

{

"

id

"

:

"

ba_1NWScr2eZvKYlo2C8MgV5Cwn

"

,

"

object

"

:

"

bank_account

"

,

"

account_holder_name

"

:

"

Jenny Rosen

"

,

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

null

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

country

"

:

"

US

"

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

fingerprint

"

:

"

1JWtPxqbdX5Gamtz

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

routing_number

"

:

"

110000000

"

,

"

status

"

:

"

new

"

},

"

client_ip

"

:

null

,

"

created

"

:

1689981645

,

"

livemode

"

:

false

,

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

bank_account

"

,

"

used

"

:

false

}

Create a card token

Ask about this section

Copy for LLM

View as Markdown

Creates a single-use token that represents a credit card’s details.

You can use this token in place of a credit card

dictionary

with any v1 API method.

You can only use these tokens once

by

creating a new Charge object

or by attaching them to a

Customer object

.

To use this functionality, you need to

enable access

to the raw card data APIs

.

In most cases, you can use our recommended

payments integrations

instead of using the API.

Parameters

card

object | string

The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is

a dictionary

containing a user’s credit card details, with the options described below.

Show child parameters

Returns

Returns the created card token if it’s successful. Otherwise, this call raises

an error

.

POST

/

v1

/

tokens

curl

https://api.stripe.com/v1/tokens \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

card[number]=4242424242424242

"

\

-d

"

card[exp_month]=5

"

\

-d

"

card[exp_year]=2026

"

\

-d

"

card[cvc]=314

"

Response

{

"

id

"

:

"

tok_1N3T00LkdIwHu7ixt44h1F8k

"

,

"

object

"

:

"

token

"

,

"

card

"

:

{

"

id

"

:

"

card_1N3T00LkdIwHu7ixRdxpVI1Q

"

,

"

object

"

:

"

card

"

,

"

address_city

"

:

null

,

"

address_country

"

:

null

,

"

address_line1

"

:

null

,

"

address_line1_check

"

:

null

,

"

address_line2

"

:

null

,

"

address_state

"

:

null

,

"

address_zip

"

:

null

,

"

address_zip_check

"

:

null

,

"

brand

"

:

"

Visa

"

,

"

country

"

:

"

US

"

,

"

cvc_check

"

:

"

unchecked

"

,

"

dynamic_last4

"

:

null

,

"

exp_month

"

:

5

,

"

exp_year

"

:

2026

,

"

fingerprint

"

:

"

mToisGZ01V71BCos

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

last4

"

:

"

4242

"

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

null

,

"

tokenization_method

"

:

null

,

"

wallet

"

:

null

},

"

client_ip

"

:

"

52.35.78.6

"

,

"

created

"

:

1683071568

,

"

livemode

"

:

false

,

"

type

"

:

"

card

"

,

"

used

"

:

false

}

Create a CVC update token

Ask about this section

Copy for LLM

View as Markdown

Creates a single-use token that represents an updated CVC value that you can use for

CVC re-collection

.

Use this token when

you confirm a card payment

or use a saved card on a

PaymentIntent

with

confirmation

_

method: manual

.

For most cases, use our

JavaScript library

instead of using the API. For a

PaymentIntent

with

confirmation

_

method: automatic

, use our recommended

payments integration

without tokenizing the CVC value.

Parameters

cvc

_

update

object

Required

The updated CVC value this token represents.

Show child parameters

Returns

Returns the created CVC update token if it’s successful. Otherwise, this call raises

an error

.

POST

/

v1

/

tokens

curl

https://api.stripe.com/v1/tokens \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

cvc_update[cvc]=123

"

Response

{

"

id

"

:

"

cvctok_1NkWsu2eZvKYlo2CFDm6ab7X

"

,

"

object

"

:

"

token

"

,

"

client_ip

"

:

null

,

"

created

"

:

1693334608

,

"

livemode

"

:

false

,

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

cvc_update

"

,

"

used

"

:

false

}
