---
title: Accounts | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/accounts
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:23:59.410683+00:00
kind: extracted-doc
---

# Accounts | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/accounts

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:23:59.410683+00:00

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
- https://docs.stripe.com/api/v2/core/accounts/object
- https://docs.stripe.com/api/v2/core/accounts/create
- https://docs.stripe.com/api/v2/core/accounts/update
- https://docs.stripe.com/api/v2/core/accounts/retrieve
- https://docs.stripe.com/api/v2/core/accounts/list
- https://docs.stripe.com/api/v2/core/accounts/close
- https://docs.stripe.com/api/v2/core/accounts/event-types
- https://docs.stripe.com/api/v2/core/account-links

Captured summary:

- Accounts | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 The Account object v2 Create an account v2 Update an account v2 Retrieve an account v2 List accounts v2 Close an account v2 Account event types v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Accounts v2 Ask about this section Copy for LLM View as Markdown An Account v2 object represents a company, individual, or other entity that interacts with a platform on Stripe.
- It contains both identifying information and properties that control its behavior and functionality.
- An Account can have one or more configurations that enable sets of related features, such as allowing it to act as a merchant or customer.
- The Accounts v2 API supports both the Global Payouts preview feature and the Connect-Billing integration preview feature.
- However, a particular Account can only access one of them.

Extracted text:

Accounts | Stripe API Reference

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

The Account object

v2

Create an account

v2

Update an account

v2

Retrieve an account

v2

List accounts

v2

Close an account

v2

Account event types

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

Accounts

v2

Ask about this section

Copy for LLM

View as Markdown

An Account v2 object represents a company, individual, or other entity that interacts with a platform on Stripe. It contains both identifying information and properties that control its behavior and functionality. An Account can have one or more configurations that enable sets of related features, such as allowing it to act as a merchant or customer.

The Accounts v2 API supports both the Global Payouts preview feature and the Connect-Billing integration preview feature. However, a particular Account can only access one of them.

The Connect-Billing integration preview feature allows an Account v2 to pay subscription fees to a platform. An Account v1 required a separate Customer object to pay subscription fees.

Learn more about calling API v2 endpoints.

Was this section helpful?

Yes

No

Endpoints

POST

/

v2

/

core

/

accounts

POST

/

v2

/

core

/

accounts

/

:id

GET

/

v2

/

core

/

accounts

/

:id

GET

/

v2

/

core

/

accounts

POST

/

v2

/

core

/

accounts

/

:id

/

close

The Account object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the Account.

object

string, value is "v2.core.account"

String representing the object’s type. Objects of the same type share the same value of the object field.

applied

_

configurations

array of enums

The configurations that have been applied to this account.

Possible enum values

customer

The Account can be used as a customer.

merchant

The Account can be used as a merchant.

recipient

The Account can be used as a recipient.

closed

nullable

boolean

Indicates whether the account has been closed.

configuration

nullable

object

An Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.

Show child attributes

contact

_

email

nullable

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

nullable

string

The default contact phone for the Account.

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

dashboard

nullable

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

nullable

object

Default values for settings shared across Account configurations.

Show child attributes

display

_

name

nullable

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

future

_

requirements

nullable

object

Information about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.

Show child attributes

identity

nullable

object

Information about the company, individual, and business represented by the Account.

Show child attributes

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

requirements

nullable

object

Information about the active requirements for the Account, including what information needs to be collected, and by when.

Show child attributes

The Account object

{

"

id

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

object

"

:

"

v2.core.account

"

,

"

applied_configurations

"

:

[

"

customer

"

,

"

merchant

"

],

"

configuration

"

:

{

"

customer

"

:

{

"

automatic_indirect_tax

"

:

{

"

exempt

"

:

"

none

"

,

"

location

"

:

{

"

country

"

:

"

US

"

,

"

state

"

:

"

NY

"

},

"

location_source

"

:

"

identity_address

"

},

"

billing

"

:

{

"

invoice

"

:

{

"

next_sequence

"

:

1

,

"

prefix

"

:

"

5626C87C

"

,

"

custom_fields

"

:

[]

}

},

"

capabilities

"

:

{

"

automatic_indirect_tax

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

,

"

status_details

"

:

[]

}

}

},

"

merchant

"

:

{

"

card_payments

"

:

{

"

decline_on

"

:

{

"

avs_failure

"

:

false

,

"

cvc_failure

"

:

false

}

},

"

capabilities

"

:

{

"

card_payments

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

,

"

status_details

"

:

[]

},

"

stripe_balance

"

:

{

"

payouts

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

,

"

status_details

"

:

[]

}

}

}

}

},

"

contact_email

"

:

"

furever@example.com

"

,

"

created

"

:

"

2025-03-28T19:59:16.000Z

"

,

"

dashboard

"

:

"

full

"

,

"

identity

"

:

{

"

business_details

"

:

{

"

registered_name

"

:

"

Furever

"

,

"

address

"

:

{

"

country

"

:

"

US

"

,

"

postal_code

"

:

"

10001

"

}

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

entity_type

"

:

"

company

"

},

"

defaults

"

:

{

"

currency

"

:

"

usd

"

,

"

responsibilities

"

:

{

"

fees_collector

"

:

"

stripe

"

,

"

losses_collector

"

:

"

stripe

"

,

"

requirements_collector

"

:

"

stripe

"

}

},

"

display_name

"

:

"

Furever

"

}

Create an account

v2

Ask about this section

Copy for LLM

View as Markdown

An Account is a representation of a company, individual or other entity that a user interacts with. Accounts contain identifying information about the entity, and configurations that store the features an account has access to. An account can be configured as any or all of the following configurations: Customer, Merchant and/or Recipient.

Learn more about calling API v2 endpoints.

Parameters

account

_

token

string

The account token generated by the account token api.

configuration

object

An Account Configuration which allows the Account to take on a key persona across Stripe products.

Show child parameters

contact

_

email

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

string

The default contact phone for the Account.

dashboard

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

object

Default values to be used on Account Configurations.

Show child parameters

display

_

name

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

identity

object

Information about the company, individual, and business represented by the Account.

Show child parameters

include

array of enums

Additional fields to include in the response.

Possible enum values

configuration

.

customer

Include parameter to expose

configuration

.

customer

on an Account.

configuration

.

merchant

Include parameter to expose

configuration

.

merchant

on an Account.

configuration

.

recipient

Include parameter to expose

configuration

.

recipient

on an Account.

defaults

Include parameter to expose

defaults

on an Account.

future

_

requirements

Include parameter to expose

future

_

requirements

on an Account.

identity

Include parameter to expose

identity

on an Account.

requirements

Include parameter to expose

requirements

on an Account.

metadata

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Returns

Response attributes

id

string

Unique identifier for the Account.

object

string, value is "v2.core.account"

String representing the object’s type. Objects of the same type share the same value of the object field.

applied

_

configurations

array of enums

The configurations that have been applied to this account.

Possible enum values

customer

The Account can be used as a customer.

merchant

The Account can be used as a merchant.

recipient

The Account can be used as a recipient.

closed

nullable

boolean

Indicates whether the account has been closed.

configuration

nullable

object

An Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.

Show child attributes

contact

_

email

nullable

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

nullable

string

The default contact phone for the Account.

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

dashboard

nullable

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

nullable

object

Default values for settings shared across Account configurations.

Show child attributes

display

_

name

nullable

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

future

_

requirements

nullable

object

Information about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.

Show child attributes

identity

nullable

object

Information about the company, individual, and business represented by the Account.

Show child attributes

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

requirements

nullable

object

Information about the active requirements for the Account, including what information needs to be collected, and by when.

Show child attributes

Error Codes

400

account

_

capability

_

not

_

supported

Requested capability is not available.

400

account

_

configuration

_

not

_

supported

The requested configuration is not available for the account.

400

account

_

controller

_

express

_

dash

_

without

_

application

_

losses

_

or

_

fees

If

dashboard

is

express

,

fees

_

collector

must be

application

and

losses

_

collector

must be

application

.

400

account

_

controller

_

stripe

_

pricing

_

platform

_

liable

If

losses

_

collector

is

application

,

fees

_

collector

must also be

application

.

400

account

_

controller

_

ua

_

unsupported

_

configuration

Connect integration combination is not supported when UA beta is enabled.

400

account

_

controller

_

unsupported

_

configuration

Connect integration combination is not supported when UA beta is disabled.

400

account

_

controller

_

unsupported

_

configuration

_

private

_

preview

Responsibility combinations is not supported in private preview.

400

account

_

country

_

unsupported

_

currency

Currency is not allowed for the account’s country.

400

account

_

create

_

activation

_

required

Platform must be activated to create connected accounts.

400

account

_

creation

_

invalid

Account creation is invalid.

400

account

_

creation

_

liability

_

unacknowledged

Account creation error - liability unacknowledged.

400

account

_

creation

_

requirement

_

collection

_

and

_

liability

_

unacknowledged

Account creation error - requirement collection and liability unacknowledged.

400

account

_

creation

_

requirement

_

collection

_

unacknowledged

Account creation error - requirement collection unacknowledged.

400

account

_

terms

_

of

_

service

_

not

_

accepted

Terms of service must be accepted before adding merchant configuration.

400

account

_

token

_

required

Account token required for platforms in mandated countries (e.g., France).

400

accounts

_

v2

_

access

_

blocked

Accounts v2 is not enabled for your platform.

400

address

_

characters

_

invalid

Invalid characters are provided for address fields.

400

address

_

country

_

identity

_

country

_

mismatch

Address country doesn’t match identity country.

400

address

_

postal

_

code

_

invalid

Address postal code is invalid.

400

address

_

state

_

invalid

Address state is invalid.

400

address

_

town

_

invalid

Address town is invalid.

400

bgn

_

bank

_

accounts

_

unsupported

Creating accounts with the BGN currency is no longer supported, as Bulgaria is now using the Euro as of 2026-01-01.

400

can

_

create

_

platform

_

owned

_

onboarding

_

accounts

_

required

Dormant accounts cannot create accounts where requirements collector is application (this is an account takeover prevention measure).

400

cannot

_

create

_

connected

_

account

Platform is in an invalid state and cannot create connected accounts.

400

cannot

_

create

_

new

_

account

_

rejected

Platform is in a rejected state and cannot create connected accounts.

400

capability

_

cannot

_

be

_

unrequested

_

due

_

to

_

other

_

capability

_

requirement

Feature cannot be unrequested due to being a requirement for another feature.

400

capability

_

not

_

available

_

for

_

dashboard

_

type

Feature cannot be requested for the dashboard type.

400

capability

_

not

_

available

_

for

_

entity

_

type

_

in

_

country

Requested feature is not available for the entity type in your country.

400

capability

_

not

_

available

_

for

_

loss

_

collector

A v2 Account cannot have both the specified capability and Stripe-owned loss liability.

400

capability

_

not

_

available

_

in

_

country

Requested capability is not available in your country.

400

capability

_

not

_

available

_

in

_

platform

_

country

Feature cannot be requested given the platform’s country.

400

capability

_

not

_

available

_

without

_

other

_

capability

Requested feature is not available without also requesting a different feature.

400

capability

_

not

_

available

_

without

_

other

_

capability

_

in

_

country

Requested feature is not available without also requesting a different feature in your country.

400

configuration

_

creation

_

invalid

Cannot create an account with an invalid configuration.

400

connect

_

identity

_

not

_

verified

Platform is not verified and cannot create connected accounts.

400

connect

_

profile

_

not

_

submitted

Platform has not completed platform questionnaire and cannot create connected accounts.

400

cross

_

border

_

connected

_

account

_

creation

_

not

_

allowed

Cross-border connected account creation is not allowed for this platform/account country combination.

400

custom

_

account

_

beta

Custom accounts cannot be created in certain countries.

400

date

_

of

_

birth

_

age

_

restriction

Representative date of birth does not meet the age limit.

400

date

_

of

_

birth

_

invalid

Representative date of birth is provided an invalid date or a future date.

400

default

_

currency

_

immutable

Cannot change

defaults

.

currency

post account activation.

400

default

_

payment

_

method

_

invalid

Default payment method provided for a customer does not exist or is otherwise invalid.

400

default

_

payment

_

method

_

invalid

_

type

Specified payment method exists but its type is not allowed to be the default payment method.

400

directorship

_

declaration

_

not

_

allowed

_

during

_

account

_

creation

Directorship declaration is not allowed during account creation.

400

document

_

invalid

Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.

400

document

_

purpose

_

invalid

Provided file tokens for documents are of the wrong purpose.

400

email

_

domain

_

invalid

_

for

_

recipient

Email contains unsupported domain.

400

email

_

invalid

Incorrect email is provided.

400

entity

_

type

_

not

_

supported

_

in

_

country

The

identity

.

entity

_

type

value is not supported in a given

identity

.

country

.

400

high

_

risk

_

activities

_

none

_

cant

_

be

_

combined

_

with

_

other

_

options

NONE is combined with another value in the HighRiskActivities list.

400

id

_

number

_

invalid

Provided ID number is of the wrong format for the given type.

400

identity

_

country

_

required

The

identity

.

country

value is required but not provided.

400

incorrect

_

id

_

number

_

for

_

country

Incorrect ID number is provided for a country.

400

incorrect

_

token

_

wrong

_

type

The incorrect token type is provided .

400

invalid

_

id

_

number

_

for

_

structure

ID number is provided that is not permitted for the Identity’s entity type and business structure.

400

invalid

_

id

_

number

_

registrar

The

identity

.

business

_

details

.

id

_

numbers

.

registrar

value is an invalid DE registrar.

400

invalid

_

konbini

_

payments

_

support

_

hours

Konbini Payments Support Hours is Invalid.

400

invalid

_

konbini

_

payments

_

support

_

phone

_

number

Konbini Payments Support Phone Number is Invalid.

400

invalid

_

timezone

Timezone provided in account defaults is invalid.

400

invoice

_

rendering

_

template

_

invalid

Invoice rendering template does not exist or is otherwise invalid.

400

ip

_

address

_

invalid

Invalid IP address is provided.

400

mcc

_

invalid

MCC is invalid for

configuration

.

merchant

.

mcc

.

400

non

_

jp

_

kana

_

kanji

_

address

Kana Kanji script addresses must have JP country.

400

ownership

_

declaration

_

not

_

allowed

_

during

_

account

_

creation

Ownership declaration is not allowed during account creation.

400

param

_

alongside

_

account

_

token

Parameter cannot be passed alongside account_token.

400

person

_

percent

_

ownership

_

invalid

Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.

400

phone

_

invalid

Phone number is invalid.

400

platform

_

registration

_

required

Platform has not signed up for Connect and cannot create connected accounts.

400

postal

_

code

_

required

_

for

_

jp

_

address

Postal code is required for Japanese addresses.

400

purpose

_

of

_

funds

_

description

_

must

_

be

_

empty

_

for

_

non

_

other

_

purpose

_

of

_

funds

PurposeOfFundsDescription is not empty while PurposeOfFunds is not OTHER.

400

registration

_

date

_

invalid

Registration date must be in the past.

400

script

_

characters

_

invalid

Provided script characters are invalid for the script.

400

shipping

_

address

_

required

Shipping address is required within the shipping hash.

400

shipping

_

name

_

required

Shipping name is required within the shipping hash.

400

statement

_

descriptor

_

invalid

Statement descriptor is invalid.

400

structure

_

incompatible

_

for

_

entity

_

type

_

country

The

business

_

details

.

structure

value is not valid for

identity

.

country

and

identity

.

entity

_

type

.

400

test

_

clock

_

disallowed

_

on

_

live

_

mode

Cannot set a test clock on a livemode customer.

400

test

_

clock

_

invalid

Test clock does not exist or is otherwise invalid.

400

test

_

clocks

_

advance

_

in

_

progress

Cannot modify a test clock that is currently advancing.

400

test

_

clocks

_

customer

_

limit

_

reached

Cannot add customer to a test clock that has already reached its customer limit.

400

token

_

already

_

used

The token is re-used with a different idempotency key.

400

token

_

expired

Token has expired.

400

tos

_

acceptance

_

on

_

behalf

_

not

_

allowed

TOS cannot be accepted on behalf of accounts when requirement collection is

stripe

.

400

unsupported

_

field

_

for

_

configs

Cannot set responsibilities on the current configurations.

400

unsupported

_

identity

_

field

_

for

_

configs

Cannot set identity fields when the Account is only configured as a customer.

400

unsupported

_

postal

_

code

Address is in an unsupported postal code.

400

unsupported

_

state

Address is in an unsupported state.

400

url

_

invalid

URL is invalid.

400

v1

_

token

_

invalid

_

in

_

v2

A v1 token ID is passed in v2 APIs.

403

invalid

_

account

_

token

Invalid account token.

409

idempotency

_

error

An idempotent retry occurred with different request parameters.

429

account

_

rate

_

limit

_

exceeded

Account cannot exceed a configured concurrency rate limit on updates.

POST

/

v2

/

core

/

accounts

curl

-X POST https://api.stripe.com/v2/core/accounts \

-H

"

Authorization: Bearer

[REDACTED_SECRET]

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.dahlia

"

\

--json

'

{

"contact_email": "furever@example.com",

"display_name": "Furever",

"identity": {

"country": "us",

"entity_type": "company",

"business_details": {

"registered_name": "Furever"

}

},

"configuration": {

"customer": {

"capabilities": {

"automatic_indirect_tax": {

"requested": true

}

}

},

"merchant": {

"capabilities": {

"card_payments": {

"requested": true

}

}

}

},

"defaults": {

"responsibilities": {

"fees_collector": "stripe",

"losses_collector": "stripe"

}

},

"dashboard": "full",

"include": [

"configuration.merchant",

"configuration.customer",

"identity",

"defaults"

]

}

'

Response

{

"

id

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

object

"

:

"

v2.core.account

"

,

"

applied_configurations

"

:

[

"

customer

"

,

"

merchant

"

],

"

configuration

"

:

{

"

customer

"

:

{

"

applied

"

:

"

2025-03-28T19:59:16.000Z

"

,

"

automatic_indirect_tax

"

:

{

"

exempt

"

:

"

none

"

,

"

location_source

"

:

"

identity_address

"

},

"

billing

"

:

{

"

invoice

"

:

{

"

next_sequence

"

:

1

,

"

prefix

"

:

"

5626C87C

"

,

"

custom_fields

"

:

[]

}

},

"

capabilities

"

:

{

"

automatic_indirect_tax

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

,

"

status_details

"

:

[]

}

}

},

"

merchant

"

:

{

"

applied

"

:

"

2025-03-28T19:59:16.000Z

"

,

"

card_payments

"

:

{

"

decline_on

"

:

{

"

avs_failure

"

:

false

,

"

cvc_failure

"

:

false

}

},

"

capabilities

"

:

{

"

card_payments

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

,

"

status_details

"

:

[]

},

"

stripe_balance

"

:

{

"

payouts

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

,

"

status_details

"

:

[]

}

}

}

}

},

"

contact_email

"

:

"

furever@example.com

"

,

"

created

"

:

"

2025-03-28T19:59:16.000Z

"

,

"

dashboard

"

:

"

full

"

,

"

identity

"

:

{

"

business_details

"

:

{

"

registered_name

"

:

"

Furever

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

entity_type

"

:

"

company

"

},

"

livemode

"

:

false

,

"

defaults

"

:

{

"

currency

"

:

"

usd

"

,

"

responsibilities

"

:

{

"

fees_collector

"

:

"

stripe

"

,

"

losses_collector

"

:

"

stripe

"

,

"

requirements_collector

"

:

"

stripe

"

}

},

"

display_name

"

:

"

Furever

"

}

Update an account

v2

Ask about this section

Copy for LLM

View as Markdown

Updates the details of an Account.

Learn more about calling API v2 endpoints.

Parameters

account

_

token

string

The account token generated by the account token api.

configuration

object

An Account Configuration which allows the Account to take on a key persona across Stripe products.

Show child parameters

contact

_

email

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

string

The default contact phone for the Account.

dashboard

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

object

Default values to be used on Account Configurations.

Show child parameters

display

_

name

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

identity

object

Information about the company, individual, and business represented by the Account.

Show child parameters

include

array of enums

Additional fields to include in the response.

Possible enum values

configuration

.

customer

Include parameter to expose

configuration

.

customer

on an Account.

configuration

.

merchant

Include parameter to expose

configuration

.

merchant

on an Account.

configuration

.

recipient

Include parameter to expose

configuration

.

recipient

on an Account.

defaults

Include parameter to expose

defaults

on an Account.

future

_

requirements

Include parameter to expose

future

_

requirements

on an Account.

identity

Include parameter to expose

identity

on an Account.

requirements

Include parameter to expose

requirements

on an Account.

metadata

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Returns

Response attributes

id

string

Unique identifier for the Account.

object

string, value is "v2.core.account"

String representing the object’s type. Objects of the same type share the same value of the object field.

applied

_

configurations

array of enums

The configurations that have been applied to this account.

Possible enum values

customer

The Account can be used as a customer.

merchant

The Account can be used as a merchant.

recipient

The Account can be used as a recipient.

closed

nullable

boolean

Indicates whether the account has been closed.

configuration

nullable

object

An Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.

Show child attributes

contact

_

email

nullable

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

nullable

string

The default contact phone for the Account.

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

dashboard

nullable

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

nullable

object

Default values for settings shared across Account configurations.

Show child attributes

display

_

name

nullable

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

future

_

requirements

nullable

object

Information about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.

Show child attributes

identity

nullable

object

Information about the company, individual, and business represented by the Account.

Show child attributes

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

requirements

nullable

object

Information about the active requirements for the Account, including what information needs to be collected, and by when.

Show child attributes

Error Codes

400

account

_

capability

_

not

_

supported

Requested capability is not available.

400

account

_

configuration

_

not

_

supported

The requested configuration is not available for the account.

400

account

_

controller

_

express

_

dash

_

without

_

application

_

losses

_

or

_

fees

If

dashboard

is

express

,

fees

_

collector

must be

application

and

losses

_

collector

must be

application

.

400

account

_

controller

_

stripe

_

pricing

_

platform

_

liable

If

losses

_

collector

is

application

,

fees

_

collector

must also be

application

.

400

account

_

controller

_

unsupported

_

configuration

Connect integration combination is not supported when UA beta is disabled.

400

account

_

controller

_

unsupported

_

configuration

_

private

_

preview

Responsibility combinations is not supported in private preview.

400

account

_

country

_

unsupported

_

currency

Currency is not allowed for the account’s country.

400

account

_

not

_

yet

_

compatible

_

with

_

v2

Account is not yet compatible with V2 APIs.

400

account

_

terms

_

of

_

service

_

not

_

accepted

Terms of service must be accepted before adding merchant configuration.

400

account

_

token

_

required

Account token required for platforms in mandated countries (e.g., France).

400

accounts

_

v2

_

access

_

blocked

Accounts v2 is not enabled for your platform.

400

address

_

characters

_

invalid

Invalid characters are provided for address fields.

400

address

_

country

_

identity

_

country

_

mismatch

Address country doesn’t match identity country.

400

address

_

postal

_

code

_

invalid

Address postal code is invalid.

400

address

_

state

_

invalid

Address state is invalid.

400

address

_

town

_

invalid

Address town is invalid.

400

attach

_

payment

_

method

_

to

_

customer

Default payment method is added to the customer config before attaching it to the account using

/v1/payment

_

methods

.

400

bgn

_

bank

_

accounts

_

unsupported

Creating accounts with the BGN currency is no longer supported, as Bulgaria is now using the Euro as of 2026-01-01.

400

can

_

create

_

platform

_

owned

_

onboarding

_

accounts

_

required

Dormant accounts cannot create accounts where requirements collector is application (this is an account takeover prevention measure).

400

cannot

_

use

_

validate

_

location

_

on

_

customer

_

create

Cannot set

automatic

_

indirect

_

tax

.

validate

_

location

when initially creating a customer configuration.

400

capability

_

cannot

_

be

_

unrequested

_

due

_

to

_

other

_

capability

_

requirement

Feature cannot be unrequested due to being a requirement for another feature.

400

capability

_

not

_

available

_

for

_

dashboard

_

type

Feature cannot be requested for the dashboard type.

400

capability

_

not

_

available

_

for

_

entity

_

type

_

in

_

country

Requested feature is not available for the entity type in your country.

400

capability

_

not

_

available

_

for

_

loss

_

collector

A v2 Account cannot have both the specified capability and Stripe-owned loss liability.

400

capability

_

not

_

available

_

in

_

country

Requested capability is not available in your country.

400

capability

_

not

_

available

_

in

_

platform

_

country

Feature cannot be requested given the platform’s country.

400

capability

_

not

_

available

_

without

_

other

_

capability

Requested feature is not available without also requesting a different feature.

400

capability

_

not

_

available

_

without

_

other

_

capability

_

in

_

country

Requested feature is not available without also requesting a different feature in your country.

400

configuration

_

cannot

_

be

_

deactivated

Configuration cannot be deactivated.

400

configuration

_

cannot

_

be

_

deactivated

_

due

_

to

_

other

_

capability

_

requirement

Configuration cannot be deactivated due to a dependency with another capability.

400

configuration

_

cannot

_

be

_

deactivated

_

due

_

to

_

other

_

configuration

Cannot deactivate a configuration due to another configuration depending on it.

400

configuration

_

cannot

_

be

_

updated

_

while

_

deactivated

Configuration cannot be updated while deactivated.

400

configuration

_

creation

_

invalid

Cannot create an account with an invalid configuration.

400

cross

_

border

_

connected

_

account

_

creation

_

not

_

allowed

Cross-border connected account creation is not allowed for this platform/account country combination.

400

custom

_

account

_

beta

Custom accounts cannot be created in certain countries.

400

customer

_

invalid

_

tax

_

location

Invalid customer tax location.

400

date

_

of

_

birth

_

age

_

restriction

Representative date of birth does not meet the age limit.

400

date

_

of

_

birth

_

invalid

Representative date of birth is provided an invalid date or a future date.

400

default

_

currency

_

immutable

Cannot change

defaults

.

currency

post account activation.

400

default

_

outbound

_

destination

_

invalid

Outbound Destination ID is invalid.

400

default

_

payment

_

method

_

invalid

Default payment method provided for a customer does not exist or is otherwise invalid.

400

document

_

invalid

Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.

400

document

_

purpose

_

invalid

Provided file tokens for documents are of the wrong purpose.

400

duplicate

_

person

_

not

_

allowed

Duplicate person is added to an account.

400

email

_

domain

_

invalid

_

for

_

recipient

Email contains unsupported domain.

400

email

_

invalid

Incorrect email is provided.

400

entity

_

type

_

not

_

supported

_

in

_

country

The

identity

.

entity

_

type

value is not supported in a given

identity

.

country

.

400

high

_

risk

_

activities

_

none

_

cant

_

be

_

combined

_

with

_

other

_

options

NONE is combined with another value in the HighRiskActivities list.

400

id

_

number

_

invalid

Provided ID number is of the wrong format for the given type.

400

identity

_

country

_

required

The

identity

.

country

value is required but not provided.

400

immutable

_

identity

_

param

Identity param has been made immutable due to the state of the account.

400

incorrect

_

id

_

number

_

for

_

country

Incorrect ID number is provided for a country.

400

incorrect

_

token

_

wrong

_

type

The incorrect token type is provided .

400

invalid

_

id

_

number

_

for

_

structure

ID number is provided that is not permitted for the Identity’s entity type and business structure.

400

invalid

_

id

_

number

_

registrar

The

identity

.

business

_

details

.

id

_

numbers

.

registrar

value is an invalid DE registrar.

400

invalid

_

konbini

_

payments

_

support

_

hours

Konbini Payments Support Hours is Invalid.

400

invalid

_

konbini

_

payments

_

support

_

phone

_

number

Konbini Payments Support Phone Number is Invalid.

400

invalid

_

timezone

Timezone provided in account defaults is invalid.

400

ip

_

address

_

invalid

Invalid IP address is provided.

400

mcc

_

invalid

MCC is invalid for

configuration

.

merchant

.

mcc

.

400

non

_

jp

_

kana

_

kanji

_

address

Kana Kanji script addresses must have JP country.

400

param

_

alongside

_

account

_

token

Parameter cannot be passed alongside account_token.

400

person

_

percent

_

ownership

_

invalid

Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.

400

phone

_

invalid

Phone number is invalid.

400

platform

_

registration

_

required

Platform has not signed up for Connect and cannot create connected accounts.

400

postal

_

code

_

required

_

for

_

jp

_

address

Postal code is required for Japanese addresses.

400

purpose

_

of

_

funds

_

description

_

must

_

be

_

empty

_

for

_

non

_

other

_

purpose

_

of

_

funds

PurposeOfFundsDescription is not empty while PurposeOfFunds is not OTHER.

400

registration

_

date

_

invalid

Registration date must be in the past.

400

script

_

characters

_

invalid

Provided script characters are invalid for the script.

400

shipping

_

address

_

required

Shipping address is required within the shipping hash.

400

shipping

_

name

_

required

Shipping name is required within the shipping hash.

400

statement

_

descriptor

_

invalid

Statement descriptor is invalid.

400

structure

_

incompatible

_

for

_

entity

_

type

_

country

The

business

_

details

.

structure

value is not valid for

identity

.

country

and

identity

.

entity

_

type

.

400

test

_

clock

_

disallowed

_

on

_

live

_

mode

Cannot set a test clock on a livemode customer.

400

test

_

clock

_

invalid

Test clock does not exist or is otherwise invalid.

400

token

_

already

_

used

The token is re-used with a different idempotency key.

400

token

_

expired

Token has expired.

400

tos

_

acceptance

_

on

_

behalf

_

not

_

allowed

TOS cannot be accepted on behalf of accounts when requirement collection is

stripe

.

400

total

_

person

_

ownership

_

exceeded

Total ownership percentages of all Persons on the account exceeds 100%.

400

unsupported

_

field

_

for

_

configs

Cannot set responsibilities on the current configurations.

400

unsupported

_

identity

_

field

_

for

_

configs

Cannot set identity fields when the Account is only configured as a customer.

400

unsupported

_

postal

_

code

Address is in an unsupported postal code.

400

unsupported

_

state

Address is in an unsupported state.

400

url

_

invalid

URL is invalid.

400

v1

_

account

_

instead

_

of

_

v2

_

account

V1 Account ID cannot be used in V2 Account APIs.

400

v1

_

customer

_

instead

_

of

_

v2

_

account

V1 Customer ID cannot be used in V2 Account APIs.

400

v1

_

token

_

invalid

_

in

_

v2

A v1 token ID is passed in v2 APIs.

403

invalid

_

account

_

token

Invalid account token.

404

not

_

found

The resource wasn’t found.

409

idempotency

_

error

An idempotent retry occurred with different request parameters.

429

account

_

rate

_

limit

_

exceeded

Account cannot exceed a configured concurrency rate limit on updates.

POST

/

v2

/

core

/

accounts

/

:id

curl

-X POST https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

\

-H

"

Authorization: Bearer

[REDACTED_SECRET]

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.dahlia

"

\

--json

'

{

"defaults": {

"profile": {

"business_url": "http://accessible.stripe.com",

"doing_business_as": "FurEver",

"product_description": "Saas pet grooming platform at furever.dev using Connect embedded components"

}

},

"identity": {

"business_details": {

"structure": "sole_proprietorship",

"id_numbers": [

{

"type": "us_ein",

"value": "000000000"

}

]

}

},

"include": [

"defaults",

"identity"

]

}

'

Response

{

"

id

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

object

"

:

"

v2.core.account

"

,

"

applied_configurations

"

:

[

"

customer

"

,

"

merchant

"

],

"

contact_email

"

:

"

furever@example.com

"

,

"

created

"

:

"

2024-11-26T16:33:03.000Z

"

,

"

dashboard

"

:

"

full

"

,

"

identity

"

:

{

"

business_details

"

:

{

"

id_numbers

"

:

[

{

"

type

"

:

"

us_ein

"

}

],

"

registered_name

"

:

"

Furever

"

,

"

structure

"

:

"

sole_proprietorship

"

},

"

country

"

:

"

us

"

,

"

entity_type

"

:

"

company

"

},

"

defaults

"

:

{

"

currency

"

:

"

usd

"

,

"

locales

"

:

[],

"

profile

"

:

{

"

business_url

"

:

"

http://accessible.stripe.com

"

,

"

doing_business_as

"

:

"

FurEver

"

,

"

product_description

"

:

"

Saas pet grooming platform at furever.dev using Connect embedded components

"

},

"

responsibilities

"

:

{

"

fees_collector

"

:

"

stripe

"

,

"

losses_collector

"

:

"

stripe

"

,

"

requirements_collector

"

:

"

stripe

"

}

},

"

display_name

"

:

"

Furever

"

,

"

livemode

"

:

true

,

"

metadata

"

:

{}

}

Retrieve an account

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves the details of an Account.

Learn more about calling API v2 endpoints.

Parameters

include

array of enums

Additional fields to include in the response.

Possible enum values

configuration

.

customer

Include parameter to expose

configuration

.

customer

on an Account.

configuration

.

merchant

Include parameter to expose

configuration

.

merchant

on an Account.

configuration

.

recipient

Include parameter to expose

configuration

.

recipient

on an Account.

defaults

Include parameter to expose

defaults

on an Account.

future

_

requirements

Include parameter to expose

future

_

requirements

on an Account.

identity

Include parameter to expose

identity

on an Account.

requirements

Include parameter to expose

requirements

on an Account.

Returns

Response attributes

id

string

Unique identifier for the Account.

object

string, value is "v2.core.account"

String representing the object’s type. Objects of the same type share the same value of the object field.

applied

_

configurations

array of enums

The configurations that have been applied to this account.

Possible enum values

customer

The Account can be used as a customer.

merchant

The Account can be used as a merchant.

recipient

The Account can be used as a recipient.

closed

nullable

boolean

Indicates whether the account has been closed.

configuration

nullable

object

An Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.

Show child attributes

contact

_

email

nullable

string

The default contact email address for the Account. Required when configuring the account as a merchant or recipient.

contact

_

phone

nullable

string

The default contact phone for the Account.

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

dashboard

nullable

enum

A value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.

Possible enum values

express

The Account has access to the Express hosted dashboard.

full

The Account has access to the full Stripe hosted dashboard.

none

The Account does not have access to any Stripe hosted dashboard.

defaults

nullable

object

Default values for settings shared across Account configurations.

Show child attributes

display

_

name

nullable

string

A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.

future

_

requirements

nullable

object

Information about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.

Show child attributes

identity

nullable

object

Information about the company, individual, and business represented by the Account.

Show child attributes

livemode

boolean

Has the value

true

if the object exists in live mode or the value

false

if the object exists in test mode.

metadata

nullable

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

requirements

nullable

object

Information about the active requirements for the Account, including what information needs to be collected, and by when.

Show child attributes

Error Codes

400

account

_

not

_

yet

_

compatible

_

with

_

v2

Account is not yet compatible with V2 APIs.

400

accounts

_

v2

_

access

_

blocked

Accounts v2 is not enabled for your platform.

400

v1

_

account

_

instead

_

of

_

v2

_

account

V1 Account ID cannot be used in V2 Account APIs.

400

v1

_

customer

_

instead

_

of

_

v2

_

account

V1 Customer ID cannot be used in V2 Account APIs.

404

not

_

found

The resource wasn’t found.

429

account

_

rate

_

limit

_

exceeded

Account cannot exceed a configured concurrency rate limit on updates.

GET

/

v2

/

core

/

accounts

/

:id

curl

-G https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

\

-H

"

Authorization: Bearer

[REDACTED_SECRET]

[REDACTED_SECRET]

"

\

-H

"

Stripe-Version: 2026-03-25.dahlia

"

\

-d

"

include[0]=defaults

"

\

-d

"

include[1]=identity

"

\

-d

"

include[2]=configuration.merchant

"

Response

{

"

id

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

object

"

:

"

v2.core.account

"

,

"

applied_configurations

"

:

[

"

customer

"

,

"

merchant

"

],

"

configuration

"

:

{

"

merchant

"

:

{

"

applied

"

:

"

2024-11-26T16:33:03.000Z

"

,

"

card_payments

"

:

{

"

decline_on

"

:

{

"

avs_failure

"

:

false

,

"

cvc_failure

"

:

false

}

},

"

capabilities

"

:

{

"

card_payments

"

:

{

"

status

"

:

"

restricted

"

,

"

status_details

"

:

[

{

"

code

"

:

"

requirements_past_due

"

,

"

resolution

"

:

"

provide_info

"

}

]

}

},

"

statement_descriptor

"

:

{

"

descriptor

"

:

"

accessible.stripe.com

"

}

}

},

"

contact_email

"

:

"

furever@example.com

"

,

"

created

"

:

"

2024-11-26T16:33:03.000Z

"

,

"

dashboard

"

:

"

full

"

,

"

identity

"

:

{

"

business_details

"

:

{

"

address

"

:

{

"

country

"

:

"

us

"

},

"

id_numbers

"

:

[

{

"

type

"

:

"

us_ein

"

}

],

"

structure

"

:

"

sole_proprietorship

"

},

"

country

"

:

"

us

"

,

"

entity_type

"

:

"

company

"

},

"

defaults

"

:

{

"

currency

"

:

"

usd

"

,

"

locales

"

:

[],

"

profile

"

:

{

"

business_url

"

:

"

http://accessible.stripe.com

"

,

"

doing_business_as

"

:

"

FurEver

"

,

"

product_description

"

:

"

Saas pet grooming platform at furever.dev using Connect embedded components

"

},

"

responsibilities

"

:

{

"

fees_collector

"

:

"

stripe

"

,

"

losses_collector

"

:

"

stripe

"

,

"

requirements_collector

"

:

"

stripe

"

}

},

"

display_name

"

:

"

Furever

"

,

"

livemode

"

:

true

,

"

metadata

"

:

{}

}
