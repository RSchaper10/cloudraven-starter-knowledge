---
title: Cards | Stripe API Reference
source_url: https://docs.stripe.com/api/cards
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:39.381115+00:00
kind: extracted-doc
---

# Cards | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/cards

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:39.381115+00:00

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

- Cards | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards The Card object Create a card Update a card Retrieve a card List all cards Delete a card Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Cards Ask about this section Copy for LLM View as Markdown You can store multiple cards on a customer in order to charge the customer later.
- You can also store multiple debit cards on a recipient in order to transfer to those cards later.
- Related guide: Card payments with Sources Was this section helpful?
- Yes No Endpoints POST / v1 / customers / :id / sources POST / v1 / customers / :id / sources / :id GET / v1 / customers / :id / cards / :id GET / v1 / customers / :id / cards DELETE / v1 / customers / :id / sources / :id The Card object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- address _ city nullable string City/District/Suburb/Town/Village.

Extracted text:

Cards | Stripe API Reference

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

Bank Accounts

Cash Balance

Cash Balance Transaction

Cards

The Card object

Create a card

Update a card

Retrieve a card

List all cards

Delete a card

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

Cards

Ask about this section

Copy for LLM

View as Markdown

You can store multiple cards on a customer in order to charge the customer

later. You can also store multiple debit cards on a recipient in order to

transfer to those cards later.

Related guide:

Card payments with Sources

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

customers

/

:id

/

sources

POST

/

v1

/

customers

/

:id

/

sources

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

cards

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

cards

DELETE

/

v1

/

customers

/

:id

/

sources

/

:id

The Card object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

address

_

city

nullable

string

City/District/Suburb/Town/Village.

address

_

country

nullable

string

Billing address country, if provided when creating card.

address

_

line1

nullable

string

Address line 1 (Street address/PO Box/Company name).

address

_

line2

nullable

string

Address line 2 (Apartment/Suite/Unit/Building).

address

_

state

nullable

string

State/County/Province/Region.

address

_

zip

nullable

string

ZIP or postal code.

address

_

zip

_

check

nullable

string

If

address

_

zip

was provided, results of the check:

pass

,

fail

,

unavailable

, or

unchecked

.

brand

string

Card brand. Can be

American Express

,

Cartes Bancaires

,

Diners Club

,

Discover

,

Eftpos Australia

,

Girocard

,

JCB

,

MasterCard

,

UnionPay

,

Visa

, or

Unknown

.

country

nullable

string

Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

customer

nullable

string

Expandable

The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

cvc

_

check

nullable

string

If a CVC was provided, results of the check:

pass

,

fail

,

unavailable

, or

unchecked

. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see

Check if a card is valid without a charge

.

exp

_

month

integer

Two-digit number representing the card’s expiration month.

exp

_

year

integer

Four-digit number representing the card’s expiration year.

fingerprint

nullable

string

Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.

funding

string

Card funding type. Can be

credit

,

debit

,

prepaid

, or

unknown

.

last4

string

The last four digits of the card.

metadata

nullable

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

name

nullable

string

Cardholder name.

More attributes

Expand all

object

string

account

nullable

string

Expandable

Available conditionally

address

_

line1

_

check

nullable

string

allow

_

redisplay

nullable

enum

available

_

payout

_

methods

nullable

array of enums

currency

nullable

enum

Available conditionally

dynamic

_

last4

nullable

string

iin

nullable

string

regulated

_

status

nullable

enum

tokenization

_

method

nullable

string

wallet

nullable

object

Preview feature

The Card object

{

"

id

"

:

"

card_1MvoiELkdIwHu7ixOeFGbN9D

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

customer

"

:

"

cus_NhD8HD2bY8dP3V

"

,

"

cvc_check

"

:

null

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

4

,

"

exp_year

"

:

2024

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

}

Create a card

Ask about this section

Copy for LLM

View as Markdown

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default.

However, if the owner already has a default, then it will not change.

To change the default, you should

update the customer

to have a new

default

_

source

.

Parameters

source

object | string

Required

A token, like the ones returned by

Stripe.js

or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

Show child parameters

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

Returns

Returns the

Card

object.

POST

/

v1

/

customers

/

:id

/

sources

curl

https://api.stripe.com/v1/customers/

cus_9s6XGDTHzA66Po

/sources \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d source=tok_visa

Response

{

"

id

"

:

"

card_1NGTaT2eZvKYlo2CZWSctn5n

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

customer

"

:

"

cus_9s6XGDTHzA66Po

"

,

"

cvc_check

"

:

"

pass

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

8

,

"

exp_year

"

:

2024

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

redaction

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

}

Update a card

Ask about this section

Copy for LLM

View as Markdown

Updates a specified card for a given customer.

Parameters

address

_

city

string

City/District/Suburb/Town/Village.

address

_

country

string

Billing address country, if provided when creating card.

address

_

line1

string

Address line 1 (Street address/PO Box/Company name).

address

_

line2

string

Address line 2 (Apartment/Suite/Unit/Building).

address

_

state

string

State/County/Province/Region.

address

_

zip

string

ZIP or postal code.

exp

_

month

string

Two digit number representing the card’s expiration month.

exp

_

year

string

Four digit number representing the card’s expiration year.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

Cardholder name.

Returns

POST

/

v1

/

customers

/

:id

/

sources

/

:id

curl

https://api.stripe.com/v1/customers/

acct_1032D82eZvKYlo2C

/sources/card_1NBLeN2eZvKYlo2CIq1o7Pzs \

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

Response

{

"

id

"

:

"

card_1NBLeN2eZvKYlo2CIq1o7Pzs

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

pass

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

8

,

"

exp_year

"

:

2024

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

"

Jenny Rosen

"

,

"

redaction

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

,

"

account

"

:

"

acct_1032D82eZvKYlo2C

"

}

Retrieve a card

Ask about this section

Copy for LLM

View as Markdown

You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.

Parameters

No

parameters

.

Returns

Returns the

Card

object.

GET

/

v1

/

customers

/

:id

/

cards

/

:id

cURL

curl

https://api.stripe.com/v1/customers/

cus_NhD8HD2bY8dP3V

/cards/card_1MvoiELkdIwHu7ixOeFGbN9D \

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

card_1MvoiELkdIwHu7ixOeFGbN9D

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

customer

"

:

"

cus_NhD8HD2bY8dP3V

"

,

"

cvc_check

"

:

null

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

4

,

"

exp_year

"

:

2024

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

}
