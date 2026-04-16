---
title: Discounts | Stripe API Reference
source_url: https://docs.stripe.com/api/discounts
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:45.701829+00:00
kind: extracted-doc
---

# Discounts | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/discounts

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:45.701829+00:00

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

- Discounts | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts The Discount object Delete a customer discount Delete a subscription discount Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Discounts Ask about this section Copy for LLM View as Markdown A discount represents the actual application of a coupon or promotion code .
- It contains information about when the discount began, when it will end, and what it is applied to.
- Related guide: Applying discounts to subscriptions Was this section helpful?
- Yes No Endpoints DELETE / v1 / customers / :id / discount DELETE / v1 / subscriptions / :id / discount The Discount object Ask about this section Copy for LLM View as Markdown Attributes id string The ID of the discount object.
- Use expand[]=discounts in API calls to expand discount IDs in an array.

Extracted text:

Discounts | Stripe API Reference

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

Sources

Products

Products

Prices

Coupons

Promotion Code

Discounts

The Discount object

Delete a customer discount

Delete a subscription discount

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

Discounts

Ask about this section

Copy for LLM

View as Markdown

A discount represents the actual application of a

coupon

or

promotion code

.

It contains information about when the discount began, when it will end, and what it is applied to.

Related guide:

Applying discounts to subscriptions

Was this section helpful?

Yes

No

Endpoints

DELETE

/

v1

/

customers

/

:id

/

discount

DELETE

/

v1

/

subscriptions

/

:id

/

discount

The Discount object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

The ID of the discount object. Discounts cannot be fetched by ID. Use

expand[]=discounts

in API calls to expand discount IDs in an array.

customer

nullable

string

Expandable

The ID of the customer associated with this discount.

customer

_

account

nullable

string

The ID of the account representing the customer associated with this discount.

end

nullable

timestamp

If the coupon has a duration of

repeating

, the date that this discount will end. If the coupon has a duration of

once

or

forever

, this attribute will be null.

source

object

The source of the discount.

Show child attributes

start

timestamp

Date that the coupon was applied.

subscription

nullable

string

The subscription that this coupon is applied to, if it is applied to a particular subscription.

More attributes

Expand all

object

string

checkout

_

session

nullable

string

invoice

nullable

string

invoice

_

item

nullable

string

promotion

_

code

nullable

string

Expandable

subscription

_

item

nullable

string

The Discount object

{

"

id

"

:

"

di_1M6vk22eZvKYlo2CYMGIhk14

"

,

"

object

"

:

"

discount

"

,

"

checkout_session

"

:

"

cs_test_b1mywbZHtQCQW2ncaItVPFqupwmfqNU4IMMdw3lArEBGt0QD0CZDrNQswR

"

,

"

source

"

:

{

"

type

"

:

"

coupon

"

,

"

coupon

"

:

"

nVJYDOag

"

},

"

customer

"

:

"

cus_9s6XKzkNRiz8i3

"

,

"

end

"

:

null

,

"

invoice

"

:

null

,

"

invoice_item

"

:

null

,

"

promotion_code

"

:

null

,

"

start

"

:

1669120702

,

"

subscription

"

:

null

}

Delete a customer discount

Ask about this section

Copy for LLM

View as Markdown

Removes the currently applied discount on a customer.

Parameters

No

parameters

.

Returns

An object with a deleted flag set to true upon success. This call returns

an error

otherwise, such as if no discount exists on this customer.

DELETE

/

v1

/

customers

/

:id

/

discount

curl

-X DELETE https://api.stripe.com/v1/customers/

cus_9s6XKzkNRiz8i3

/discount \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

Response

{

"

object

"

:

"

discount

"

,

"

deleted

"

:

true

}

Delete a subscription discount

Ask about this section

Copy for LLM

View as Markdown

Removes the currently applied discount on a subscription.

Parameters

No

parameters

.

Returns

An object with a deleted flag set to true upon success. This call returns

an error

otherwise, such as if no discount exists on this subscription.

DELETE

/

v1

/

subscriptions

/

:id

/

discount

curl

-X DELETE https://api.stripe.com/v1/subscriptions/

sub_1NlcNX2eZvKYlo2CFqnrn9ow

/discount \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

Response

{

"

object

"

:

"

discount

"

,

"

deleted

"

:

true

}
