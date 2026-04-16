---
title: Products | Stripe API Reference
source_url: https://docs.stripe.com/api/products
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:41.583544+00:00
kind: extracted-doc
---

# Products | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/products

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:41.583544+00:00

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

- Products | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products The Product object Create a product Update a product Retrieve a product List all products Delete a product Search products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Products Ask about this section Copy for LLM View as Markdown Products describe the specific goods or services you offer to your customers.
- For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
- They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.
- Related guides: Set up a subscription , share a Payment Link , accept payments with Checkout , and more about Products and Prices Was this section helpful?
- Yes No Endpoints POST / v1 / products POST / v1 / products / :id GET / v1 / products / :id GET / v1 / products DELETE / v1 / products / :id GET / v1 / products / search The Product object Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the object.

Extracted text:

Products | Stripe API Reference

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

The Product object

Create a product

Update a product

Retrieve a product

List all products

Delete a product

Search products

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

Products

Ask about this section

Copy for LLM

View as Markdown

Products describe the specific goods or services you offer to your customers.

For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.

They can be used in conjunction with

Prices

to configure pricing in Payment Links, Checkout, and Subscriptions.

Related guides:

Set up a subscription

,

share a Payment Link

,

accept payments with Checkout

,

and more about

Products and Prices

Was this section helpful?

Yes

No

Endpoints

POST

/

v1

/

products

POST

/

v1

/

products

/

:id

GET

/

v1

/

products

/

:id

GET

/

v1

/

products

DELETE

/

v1

/

products

/

:id

GET

/

v1

/

products

/

search

The Product object

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the object.

active

boolean

Whether the product is currently available for purchase.

default

_

price

nullable

string

Expandable

The ID of the

Price

object that is the default price for this product.

description

nullable

string

The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

name

string

The product’s name, meant to be displayable to the customer.

tax

_

code

nullable

string

Expandable

A

tax code

ID.

More attributes

Expand all

object

string

created

timestamp

images

array of strings

livemode

boolean

marketing

_

features

array of objects

package

_

dimensions

nullable

object

shippable

nullable

boolean

statement

_

descriptor

nullable

string

unit

_

label

nullable

string

updated

timestamp

url

nullable

string

The Product object

{

"

id

"

:

"

prod_NWjs8kKbJWmuuc

"

,

"

object

"

:

"

product

"

,

"

active

"

:

true

,

"

created

"

:

1678833149

,

"

default_price

"

:

null

,

"

description

"

:

null

,

"

images

"

:

[],

"

marketing_features

"

:

[],

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

Gold Plan

"

,

"

package_dimensions

"

:

null

,

"

shippable

"

:

null

,

"

statement_descriptor

"

:

null

,

"

tax_code

"

:

null

,

"

unit_label

"

:

null

,

"

updated

"

:

1678833149

,

"

url

"

:

null

}

Create a product

Ask about this section

Copy for LLM

View as Markdown

Creates a new product object.

Parameters

name

string

Required

The product’s name, meant to be displayable to the customer.

active

boolean

Whether the product is currently available for purchase. Defaults to

true

.

description

string

The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

id

string

An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

tax

_

code

string

Recommended if calculating taxes

A

tax code

ID.

More parameters

Expand all

default

_

price

_

data

object

images

array of strings

marketing

_

features

array of objects

package

_

dimensions

object

shippable

boolean

statement

_

descriptor

string

tax

_

details

object

Recommended if calculating taxes

Preview feature

unit

_

label

string

url

string

Returns

Returns a product object if the call succeeded.

POST

/

v1

/

products

curl

https://api.stripe.com/v1/products \

-u

"

[REDACTED_SECRET]

[REDACTED_SECRET]

:

"

\

-d

"

name=Gold Plan

"

Response

{

"

id

"

:

"

prod_NWjs8kKbJWmuuc

"

,

"

object

"

:

"

product

"

,

"

active

"

:

true

,

"

created

"

:

1678833149

,

"

default_price

"

:

null

,

"

description

"

:

null

,

"

images

"

:

[],

"

marketing_features

"

:

[],

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

Gold Plan

"

,

"

package_dimensions

"

:

null

,

"

shippable

"

:

null

,

"

statement_descriptor

"

:

null

,

"

tax_code

"

:

null

,

"

unit_label

"

:

null

,

"

updated

"

:

1678833149

,

"

url

"

:

null

}

Update a product

Ask about this section

Copy for LLM

View as Markdown

Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters

active

boolean

Whether the product is available for purchase.

default

_

price

string

The ID of the

Price

object that is the default price for this product.

description

string

The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

metadata

object

Set of

key-value pairs

that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to

metadata

.

name

string

The product’s name, meant to be displayable to the customer.

tax

_

code

string

Recommended if calculating taxes

A

tax code

ID.

More parameters

Expand all

images

array of strings

marketing

_

features

array of objects

package

_

dimensions

object

shippable

boolean

statement

_

descriptor

string

tax

_

details

object

Recommended if calculating taxes

Preview feature

unit

_

label

string

url

string

Returns

Returns the product object if the update succeeded.

POST

/

v1

/

products

/

:id

curl

https://api.stripe.com/v1/products/

prod_NWjs8kKbJWmuuc

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

prod_NWjs8kKbJWmuuc

"

,

"

object

"

:

"

product

"

,

"

active

"

:

true

,

"

created

"

:

1678833149

,

"

default_price

"

:

null

,

"

description

"

:

null

,

"

images

"

:

[],

"

marketing_features

"

:

[],

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

Gold Plan

"

,

"

package_dimensions

"

:

null

,

"

shippable

"

:

null

,

"

statement_descriptor

"

:

null

,

"

tax_code

"

:

null

,

"

unit_label

"

:

null

,

"

updated

"

:

1678833149

,

"

url

"

:

null

}

Retrieve a product

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

Parameters

No

parameters

.

Returns

Returns a product object if a valid identifier was provided.

GET

/

v1

/

products

/

:id

curl

https://api.stripe.com/v1/products/

prod_NWjs8kKbJWmuuc

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

prod_NWjs8kKbJWmuuc

"

,

"

object

"

:

"

product

"

,

"

active

"

:

true

,

"

created

"

:

1678833149

,

"

default_price

"

:

null

,

"

description

"

:

null

,

"

images

"

:

[],

"

marketing_features

"

:

[],

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

Gold Plan

"

,

"

package_dimensions

"

:

null

,

"

shippable

"

:

null

,

"

statement_descriptor

"

:

null

,

"

tax_code

"

:

null

,

"

unit_label

"

:

null

,

"

updated

"

:

1678833149

,

"

url

"

:

null

}
