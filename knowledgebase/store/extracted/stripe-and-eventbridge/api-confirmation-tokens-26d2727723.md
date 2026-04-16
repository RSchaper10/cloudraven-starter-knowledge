---
title: Confirmation Token | Stripe API Reference
source_url: https://docs.stripe.com/api/confirmation_tokens
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:30.756455+00:00
kind: extracted-doc
---

# Confirmation Token | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/confirmation_tokens

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:30.756455+00:00

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

- Confirmation Token | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token The Confirmation Token object Retrieve a ConfirmationToken Create a test Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Confirmation Token Ask about this section Copy for LLM View as Markdown ConfirmationTokens help transport client side data collected by Stripe JS over to your server for confirming a PaymentIntent or SetupIntent.
- If the confirmation is successful, values present on the ConfirmationToken are written onto the Intent.
- To learn more about how to use ConfirmationToken, visit the related guides: Finalize payments on the server Build two-step confirmation .
- Yes No Endpoints GET / v1 / confirmation_tokens / :id POST / v1 / test_helpers / confirmation_tokens The Confirmation Token object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.
- object string String representing the object’s type.

Extracted text:

Confirmation Token | Stripe API Reference

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

The Confirmation Token object

Retrieve a ConfirmationToken

Create a test Confirmation Token

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

Confirmation Token

Ask about this section

Copy for LLM

View as Markdown

ConfirmationTokens help transport client side data collected by Stripe JS over

to your server for confirming a PaymentIntent or SetupIntent. If the confirmation

is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:

Finalize payments on the server

Build two-step confirmation

.

Was this section helpful?

Yes

No

Endpoints

GET

/

v1

/

confirmation_tokens

/

:id

POST

/

v1

/

test_helpers

/

confirmation_tokens

The Confirmation Token object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

object

string

String representing the object’s type. Objects of the same type share the same value.

created

timestamp

Time at which the object was created. Measured in seconds since the Unix epoch.

expires

_

at

nullable

timestamp

Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent.

livemode

boolean

If the object exists in live mode, the value is

true

. If the object exists in test mode, the value is

false

.

mandate

_

data

nullable

object

Data used for generating a Mandate.

Show child attributes

payment

_

intent

nullable

string

ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

payment

_

method

_

options

nullable

object

Payment-method-specific configuration for this ConfirmationToken.

Show child attributes

payment

_

method

_

preview

nullable

object

Payment details collected by the Payment Element, used to create a PaymentMethod when a PaymentIntent or SetupIntent is confirmed with this ConfirmationToken.

Show child attributes

return

_

url

nullable

string

Return URL used to confirm the Intent.

setup

_

future

_

usage

nullable

enum

Indicates that you intend to make future payments with this ConfirmationToken’s payment method.

The presence of this property will

attach the payment method

to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.

Possible enum values

off

_

session

Use

off

_

session

if your customer may or may not be present in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when your customer is present in your checkout flow.

setup

_

intent

nullable

string

ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.

shipping

nullable

object

Shipping information collected on this ConfirmationToken.

Show child attributes

use

_

stripe

_

sdk

boolean

Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to

true

on ConfirmationToken.

The Confirmation Token object

{

"

id

"

:

"

ctoken_1NnQUf2eZvKYlo2CIObdtbnb

"

,

"

object

"

:

"

confirmation_token

"

,

"

created

"

:

1694025025

,

"

expires_at

"

:

1694068225

,

"

livemode

"

:

true

,

"

mandate_data

"

:

null

,

"

payment_intent

"

:

null

,

"

payment_method

"

:

null

,

"

payment_method_preview

"

:

{

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

"

Hyde Park

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

line1

"

:

"

50 Sprague St

"

,

"

line2

"

:

""

,

"

postal_code

"

:

"

02136

"

,

"

state

"

:

"

MA

"

},

"

email

"

:

"

jennyrosen@stripe.com

"

,

"

name

"

:

"

Jenny Rosen

"

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

null

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

display_brand

"

:

"

visa

"

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

2026

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

type

"

:

"

card

"

},

"

return_url

"

:

"

https://example.com/return

"

,

"

setup_future_usage

"

:

"

off_session

"

,

"

setup_intent

"

:

null

,

"

shipping

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

"

Hyde Park

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

line1

"

:

"

50 Sprague St

"

,

"

line2

"

:

""

,

"

postal_code

"

:

"

02136

"

,

"

state

"

:

"

MA

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

phone

"

:

null

}

}

Retrieve a ConfirmationToken

Ask about this section

Copy for LLM

View as Markdown

Retrieves an existing ConfirmationToken object

Parameters

No

parameters

.

Returns

Returns the specified ConfirmationToken

GET

/

v1

/

confirmation_tokens

/

:id

curl

https://api.stripe.com/v1/confirmation_tokens/ctoken_1NnQUf2eZvKYlo2CIObdtbnb \

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

ctoken_1NnQUf2eZvKYlo2CIObdtbnb

"

,

"

object

"

:

"

confirmation_token

"

,

"

created

"

:

1694025025

,

"

expires_at

"

:

1694068225

,

"

livemode

"

:

true

,

"

mandate_data

"

:

null

,

"

payment_intent

"

:

null

,

"

payment_method

"

:

null

,

"

payment_method_preview

"

:

{

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

"

Hyde Park

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

line1

"

:

"

50 Sprague St

"

,

"

line2

"

:

""

,

"

postal_code

"

:

"

02136

"

,

"

state

"

:

"

MA

"

},

"

email

"

:

"

jennyrosen@stripe.com

"

,

"

name

"

:

"

Jenny Rosen

"

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

null

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

display_brand

"

:

"

visa

"

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

2026

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

type

"

:

"

card

"

},

"

return_url

"

:

"

https://example.com/return

"

,

"

setup_future_usage

"

:

"

off_session

"

,

"

setup_intent

"

:

null

,

"

shipping

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

"

Hyde Park

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

line1

"

:

"

50 Sprague St

"

,

"

line2

"

:

""

,

"

postal_code

"

:

"

02136

"

,

"

state

"

:

"

MA

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

phone

"

:

null

}

}

Create a test Confirmation Token

Test helper

Ask about this section

Copy for LLM

View as Markdown

Creates a test mode Confirmation Token server side for your integration tests.

Parameters

payment

_

method

string

ID of an existing PaymentMethod.

payment

_

method

_

data

object

If provided, this hash will be used to create a PaymentMethod.

Show child parameters

payment

_

method

_

options

object

Payment-method-specific configuration for this ConfirmationToken.

Show child parameters

return

_

url

string

Return URL used to confirm the Intent.

setup

_

future

_

usage

enum

Indicates that you intend to make future payments with this ConfirmationToken’s payment method.

The presence of this property will

attach the payment method

to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.

Possible enum values

off

_

session

Use

off

_

session

if your customer may or may not be present in your checkout flow.

on

_

session

Use

on

_

session

if you intend to only reuse the payment method when your customer is present in your checkout flow.

shipping

object

Shipping information for this ConfirmationToken.

Show child parameters

Returns

Returns a testmode Confirmation Token

POST

/

v1

/

test_helpers

/

confirmation_tokens

curl

https://api.stripe.com/v1/test_helpers/confirmation_tokens \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d payment_method=pm_card_visa

Response

{

"

id

"

:

"

ctoken_1Ow71CL4FhS6zgoxWjxc7sfr

"

,

"

object

"

:

"

confirmation_token

"

,

"

created

"

:

1710871450

,

"

expires_at

"

:

1710914650

,

"

livemode

"

:

false

,

"

payment_intent

"

:

null

,

"

payment_method_preview

"

:

{

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

unchecked

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

display_brand

"

:

"

visa

"

,

"

exp_month

"

:

3

,

"

exp_year

"

:

2025

,

"

fingerprint

"

:

"

jbGyCKrSRsFpOBWP

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

type

"

:

"

card

"

},

"

return_url

"

:

null

,

"

setup_future_usage

"

:

null

,

"

setup_intent

"

:

null

,

"

shipping

"

:

null

,

"

use_stripe_sdk

"

:

true

}
