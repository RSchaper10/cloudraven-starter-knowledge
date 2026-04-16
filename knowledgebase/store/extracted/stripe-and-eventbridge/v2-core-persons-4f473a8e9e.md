---
title: Persons | Stripe API Reference
source_url: https://docs.stripe.com/api/v2/core/persons
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:24:24.334848+00:00
kind: extracted-doc
---

# Persons | Stripe API Reference

Source URL:

- https://docs.stripe.com/api/v2/core/persons

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:24:24.334848+00:00

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

- Persons | Stripe API Reference Find anything / Ask AI Introduction Authentication Errors Expanding Responses Idempotent requests Include-dependent response values (API v2) Metadata Pagination Request IDs Connected Accounts Versioning Core Resources Accounts v2 Account Links v2 Account Tokens v2 Balance Balance Transactions Charges Customers Customer Session Disputes Events Events v2 Event Destinations v2 Files File Links Mandates Payment Intents Persons v2 The Person object v2 Create a person v2 Update a person v2 Retrieve a person v2 List persons v2 Delete a person v2 Person event types v2 Person Tokens v2 Setup Intents Setup Attempts Payouts Refunds Confirmation Token Tokens Payment Methods Payment Methods Payment Method Configurations Payment Method Domains Bank Accounts Cash Balance Cash Balance Transaction Cards Sources Products Products Prices Coupons Promotion Code Discounts Tax Code Tax Rate Shipping Rates Checkout Checkout Sessions Payment Links Payment Link Billing Alerts Credit Balance Summary Credit Balance Transaction Credit Grant Credit Note Customer Balance Transaction Customer Portal Configuration Customer Portal Session Invoices Invoice Items Invoice Line Item Invoice Payment Invoice Rendering Templates Meters Meter Events Meter Event Adjustment Meter Event Adjustments v2 Meter Event Streams v2 Meter Event Summary Meter Events v2 Plans Quote Subscriptions Subscription Items Subscription Schedule Tax IDs Test Clocks Capital Financing Offer Financing Summary Connect Accounts Login Links Account Links Account Session Application Fees Application Fee Refunds Capabilities Country Specs Balance Settings External Bank Accounts External Account Cards Person Top-ups Transfers Transfer Reversals Secrets Reserves Fraud Issuing Terminal Treasury Payment Records Account Evaluation Entitlements Sigma Reporting Financial Connections Tax Identity Crypto Climate Forwarding Privacy Webhooks Persons v2 Ask about this section Copy for LLM View as Markdown A Person represents an individual associated with an Account’s identity (for example, an owner, director, executive, or representative).
- Use Persons to provide and update identity information for verification and compliance.
- Learn more about calling API v2 endpoints.
- Yes No Endpoints POST / v2 / core / accounts / :account_id / persons POST / v2 / core / accounts / :account_id / persons / :id GET / v2 / core / accounts / :account_id / persons / :id GET / v2 / core / accounts / :account_id / persons DELETE / v2 / core / accounts / :account_id / persons / :id The Person object v2 Ask about this section Copy for LLM View as Markdown Attributes id string Unique identifier for the Person.
- object string, value is "v2.core.account_person" String representing the object’s type.

Extracted text:

Persons | Stripe API Reference

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

The Person object

v2

Create a person

v2

Update a person

v2

Retrieve a person

v2

List persons

v2

Delete a person

v2

Person event types

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

Persons

v2

Ask about this section

Copy for LLM

View as Markdown

A Person represents an individual associated with an Account’s identity (for example, an owner, director, executive, or representative). Use Persons to provide and update identity information for verification and compliance.

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

/

:account_id

/

persons

POST

/

v2

/

core

/

accounts

/

:account_id

/

persons

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

:account_id

/

persons

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

:account_id

/

persons

DELETE

/

v2

/

core

/

accounts

/

:account_id

/

persons

/

:id

The Person object

v2

Ask about this section

Copy for LLM

View as Markdown

Attributes

id

string

Unique identifier for the Person.

object

string, value is "v2.core.account_person"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The account ID which the individual belongs to.

additional

_

addresses

nullable

array of objects

Additional addresses associated with the person.

Show child attributes

additional

_

names

nullable

array of objects

Additional names (e.g. aliases) associated with the person.

Show child attributes

additional

_

terms

_

of

_

service

nullable

object

Attestations of accepted terms of service agreements.

Show child attributes

address

nullable

object

The person’s residential address.

Show child attributes

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

date

_

of

_

birth

nullable

object

The person’s date of birth.

Show child attributes

documents

nullable

object

Documents that may be submitted to satisfy various informational requests.

Show child attributes

email

nullable

string

The person’s email address.

given

_

name

nullable

string

The person’s first name.

id

_

numbers

nullable

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child attributes

legal

_

gender

nullable

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

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

nationalities

nullable

array of enums

The countries where the person is a national. Two-letter country code (

ISO 3166-1 alpha-2

).

phone

nullable

string

The person’s phone number.

political

_

exposure

nullable

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

nullable

object

The relationship that this person has with the Account’s business or legal entity.

Show child attributes

script

_

addresses

nullable

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child attributes

script

_

names

nullable

object

The script names (e.g. non-Latin characters) associated with the person.

Show child attributes

surname

nullable

string

The person’s last name.

updated

timestamp

Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

The Person object

{

"

id

"

:

"

person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

additional_addresses

"

:

[],

"

additional_names

"

:

[],

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

Brothers

"

,

"

country

"

:

"

us

"

,

"

line1

"

:

"

27 Fredrick Ave

"

,

"

postal_code

"

:

"

97712

"

,

"

state

"

:

"

OR

"

},

"

created

"

:

"

2024-11-26T17:10:07.000Z

"

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

given_name

"

:

"

Jenny

"

,

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

us_ssn_last_4

"

}

],

"

metadata

"

:

{},

"

nationalities

"

:

[],

"

relationship

"

:

{

"

owner

"

:

true

,

"

percent_ownership

"

:

"

0.8

"

,

"

representative

"

:

true

,

"

title

"

:

"

CEO

"

},

"

surname

"

:

"

Rosen

"

,

"

updated

"

:

"

2024-11-26T17:10:07.000Z

"

}

Create a person

v2

Ask about this section

Copy for LLM

View as Markdown

Create a Person. Adds an individual to an Account’s identity. You can set relationship attributes and identity information at creation.

Learn more about calling API v2 endpoints.

Parameters

additional

_

addresses

array of objects

Additional addresses associated with the person.

Show child parameters

additional

_

names

array of objects

Additional names (e.g. aliases) associated with the person.

Show child parameters

additional

_

terms

_

of

_

service

object

Attestations of accepted terms of service agreements.

Show child parameters

address

object

The person’s residential address.

Show child parameters

date

_

of

_

birth

object

The person’s date of birth.

Show child parameters

documents

object

Documents that may be submitted to satisfy various informational requests.

Show child parameters

email

string

Email.

given

_

name

string

The person’s first name.

id

_

numbers

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child parameters

legal

_

gender

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

metadata

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

nationalities

array of enums

The nationalities (countries) this person is associated with.

person

_

token

string

The person token generated by the person token api.

phone

string

The phone number for this person.

political

_

exposure

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

object

The relationship that this person has with the Account’s business or legal entity.

Show child parameters

script

_

addresses

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child parameters

script

_

names

object

The script names (e.g. non-Latin characters) associated with the person.

Show child parameters

surname

string

The person’s last name.

Returns

Response attributes

id

string

Unique identifier for the Person.

object

string, value is "v2.core.account_person"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The account ID which the individual belongs to.

additional

_

addresses

nullable

array of objects

Additional addresses associated with the person.

Show child attributes

additional

_

names

nullable

array of objects

Additional names (e.g. aliases) associated with the person.

Show child attributes

additional

_

terms

_

of

_

service

nullable

object

Attestations of accepted terms of service agreements.

Show child attributes

address

nullable

object

The person’s residential address.

Show child attributes

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

date

_

of

_

birth

nullable

object

The person’s date of birth.

Show child attributes

documents

nullable

object

Documents that may be submitted to satisfy various informational requests.

Show child attributes

email

nullable

string

The person’s email address.

given

_

name

nullable

string

The person’s first name.

id

_

numbers

nullable

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child attributes

legal

_

gender

nullable

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

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

nationalities

nullable

array of enums

The countries where the person is a national. Two-letter country code (

ISO 3166-1 alpha-2

).

phone

nullable

string

The person’s phone number.

political

_

exposure

nullable

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

nullable

object

The relationship that this person has with the Account’s business or legal entity.

Show child attributes

script

_

addresses

nullable

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child attributes

script

_

names

nullable

object

The script names (e.g. non-Latin characters) associated with the person.

Show child attributes

surname

nullable

string

The person’s last name.

updated

timestamp

Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

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

additional

_

legal

_

guardian

_

not

_

allowed

More than one legal guardian is added to an account.

400

additional

_

representative

_

not

_

allowed

More than one representative is added to an account.

400

additional

_

tos

_

only

_

allowed

_

for

_

legal

_

guardian

Additional terms of service are signed by someone other than the legal guardian.

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

country

_

mismatch

Registered/script address country doesn’t match residential address country.

400

address

_

country

_

required

Address country is required but not provided.

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

authorizer

_

duplicate

There can only be one authorizer.

400

authorizer

_

relationship

_

invalid

_

for

_

representative

An authorizer cannot be a representative.

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

account

_

for

_

person

_

token

A person token is created with one account but used on a different account.

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

individual

_

additional

_

person

_

not

_

allowed

Additional person is added for an individual business type.

400

invalid

_

relationship

_

for

_

identity

_

type

_

structure

_

and

_

country

Some relationships are specific to type, structure, and country.

400

ip

_

address

_

invalid

Invalid IP address is provided.

400

legal

_

guardian

_

representative

_

not

_

allowed

Person is designated as both legal guardian and representative.

400

legal

_

guardian

_

requires

_

existing

_

representative

A legal guardian may not be added to the account without an existing representative.

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

person

_

token

Parameter cannot be passed alongside person_token.

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

person

_

token

_

required

Person token required for platforms in mandated countries (e.g., France).

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

script

_

characters

_

invalid

Provided script characters are invalid for the script.

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

person

_

token

Invalid person token.

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

:account_id

/

persons

curl

-X POST https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

/persons \

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

"given_name": "Jenny",

"surname": "Rosen",

"email": "jenny.rosen@example.com",

"address": {

"line1": "27 Fredrick Ave",

"city": "Brothers",

"postal_code": "97712",

"state": "OR",

"country": "us"

},

"id_numbers": [

{

"type": "us_ssn_last_4",

"value": "0000"

}

],

"relationship": {

"owner": true,

"percent_ownership": "0.8",

"representative": true,

"title": "CEO"

}

}

'

Response

{

"

id

"

:

"

person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

additional_addresses

"

:

[],

"

additional_names

"

:

[],

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

Brothers

"

,

"

country

"

:

"

us

"

,

"

line1

"

:

"

27 Fredrick Ave

"

,

"

postal_code

"

:

"

97712

"

,

"

state

"

:

"

OR

"

},

"

created

"

:

"

2024-11-26T17:10:07.000Z

"

,

"

email

"

:

"

jenny.rosen@example.com

"

,

"

given_name

"

:

"

Jenny

"

,

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

us_ssn_last_4

"

}

],

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

{},

"

nationalities

"

:

[],

"

relationship

"

:

{

"

owner

"

:

true

,

"

percent_ownership

"

:

"

0.8

"

,

"

representative

"

:

true

,

"

title

"

:

"

CEO

"

},

"

surname

"

:

"

Rosen

"

,

"

updated

"

:

"

2024-11-26T17:10:07.000Z

"

}

Update a person

v2

Ask about this section

Copy for LLM

View as Markdown

Updates a Person associated with an Account.

Learn more about calling API v2 endpoints.

Parameters

additional

_

addresses

array of objects

Additional addresses associated with the person.

Show child parameters

additional

_

names

array of objects

Additional names (e.g. aliases) associated with the person.

Show child parameters

additional

_

terms

_

of

_

service

object

Attestations of accepted terms of service agreements.

Show child parameters

address

object

The primary address associated with the person.

Show child parameters

date

_

of

_

birth

object

The person’s date of birth.

Show child parameters

documents

object

Documents that may be submitted to satisfy various informational requests.

Show child parameters

email

string

Email.

given

_

name

string

The person’s first name.

id

_

numbers

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child parameters

legal

_

gender

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

metadata

map

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

nationalities

array of enums

The nationalities (countries) this person is associated with.

person

_

token

string

The person token generated by the person token api.

phone

string

The phone number for this person.

political

_

exposure

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

object

The relationship that this person has with the Account’s business or legal entity.

Show child parameters

script

_

addresses

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child parameters

script

_

names

object

The script names (e.g. non-Latin characters) associated with the person.

Show child parameters

surname

string

The person’s last name.

Returns

Response attributes

id

string

Unique identifier for the Person.

object

string, value is "v2.core.account_person"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The account ID which the individual belongs to.

additional

_

addresses

nullable

array of objects

Additional addresses associated with the person.

Show child attributes

additional

_

names

nullable

array of objects

Additional names (e.g. aliases) associated with the person.

Show child attributes

additional

_

terms

_

of

_

service

nullable

object

Attestations of accepted terms of service agreements.

Show child attributes

address

nullable

object

The person’s residential address.

Show child attributes

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

date

_

of

_

birth

nullable

object

The person’s date of birth.

Show child attributes

documents

nullable

object

Documents that may be submitted to satisfy various informational requests.

Show child attributes

email

nullable

string

The person’s email address.

given

_

name

nullable

string

The person’s first name.

id

_

numbers

nullable

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child attributes

legal

_

gender

nullable

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

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

nationalities

nullable

array of enums

The countries where the person is a national. Two-letter country code (

ISO 3166-1 alpha-2

).

phone

nullable

string

The person’s phone number.

political

_

exposure

nullable

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

nullable

object

The relationship that this person has with the Account’s business or legal entity.

Show child attributes

script

_

addresses

nullable

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child attributes

script

_

names

nullable

object

The script names (e.g. non-Latin characters) associated with the person.

Show child attributes

surname

nullable

string

The person’s last name.

updated

timestamp

Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

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

additional

_

legal

_

guardian

_

not

_

allowed

More than one legal guardian is added to an account.

400

additional

_

representative

_

not

_

allowed

More than one representative is added to an account.

400

additional

_

tos

_

only

_

allowed

_

for

_

legal

_

guardian

Additional terms of service are signed by someone other than the legal guardian.

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

country

_

mismatch

Registered/script address country doesn’t match residential address country.

400

address

_

country

_

required

Address country is required but not provided.

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

account

_

for

_

person

_

token

A person token is created with one account but used on a different account.

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

ip

_

address

_

invalid

Invalid IP address is provided.

400

legal

_

guardian

_

representative

_

not

_

allowed

Person is designated as both legal guardian and representative.

400

legal

_

guardian

_

requires

_

existing

_

representative

A legal guardian may not be added to the account without an existing representative.

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

person

_

token

Parameter cannot be passed alongside person_token.

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

person

_

token

_

required

Person token required for platforms in mandated countries (e.g., France).

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

script

_

characters

_

invalid

Provided script characters are invalid for the script.

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

person

_

token

Invalid person token.

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

POST

/

v2

/

core

/

accounts

/

:account_id

/

persons

/

:id

curl

-X POST https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \

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

"date_of_birth": {

"day": 28,

"month": 1,

"year": 2000

}

}

'

Response

{

"

id

"

:

"

person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

additional_addresses

"

:

[],

"

additional_names

"

:

[],

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

Brothers

"

,

"

country

"

:

"

us

"

,

"

line1

"

:

"

27 Fredrick Ave

"

,

"

postal_code

"

:

"

97712

"

,

"

state

"

:

"

OR

"

},

"

created

"

:

"

2024-11-26T17:10:07.000Z

"

,

"

date_of_birth

"

:

{

"

day

"

:

28

,

"

month

"

:

1

,

"

year

"

:

2000

},

"

email

"

:

"

jenny.rosen@example.com

"

,

"

given_name

"

:

"

Jenny

"

,

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

us_ssn_last_4

"

}

],

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

{},

"

nationalities

"

:

[],

"

relationship

"

:

{

"

owner

"

:

true

,

"

percent_ownership

"

:

"

0.8

"

,

"

representative

"

:

true

,

"

title

"

:

"

CEO

"

},

"

surname

"

:

"

Rosen

"

,

"

updated

"

:

"

2024-11-26T17:12:55.000Z

"

}

Retrieve a person

v2

Ask about this section

Copy for LLM

View as Markdown

Retrieves a Person associated with an Account.

Learn more about calling API v2 endpoints.

Parameters

No

parameters

.

Returns

Response attributes

id

string

Unique identifier for the Person.

object

string, value is "v2.core.account_person"

String representing the object’s type. Objects of the same type share the same value of the object field.

account

string

The account ID which the individual belongs to.

additional

_

addresses

nullable

array of objects

Additional addresses associated with the person.

Show child attributes

additional

_

names

nullable

array of objects

Additional names (e.g. aliases) associated with the person.

Show child attributes

additional

_

terms

_

of

_

service

nullable

object

Attestations of accepted terms of service agreements.

Show child attributes

address

nullable

object

The person’s residential address.

Show child attributes

created

timestamp

Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

date

_

of

_

birth

nullable

object

The person’s date of birth.

Show child attributes

documents

nullable

object

Documents that may be submitted to satisfy various informational requests.

Show child attributes

email

nullable

string

The person’s email address.

given

_

name

nullable

string

The person’s first name.

id

_

numbers

nullable

array of objects

The identification numbers (e.g., SSN) associated with the person.

Show child attributes

legal

_

gender

nullable

enum

The person’s gender (International regulations require either “male” or “female”).

Possible enum values

female

Female gender person.

male

Male gender person.

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

nationalities

nullable

array of enums

The countries where the person is a national. Two-letter country code (

ISO 3166-1 alpha-2

).

phone

nullable

string

The person’s phone number.

political

_

exposure

nullable

enum

The person’s political exposure.

Possible enum values

existing

The person has disclosed that they do have political exposure.

none

The person has disclosed that they have no political exposure.

relationship

nullable

object

The relationship that this person has with the Account’s business or legal entity.

Show child attributes

script

_

addresses

nullable

object

The script addresses (e.g., non-Latin characters) associated with the person.

Show child attributes

script

_

names

nullable

object

The script names (e.g. non-Latin characters) associated with the person.

Show child attributes

surname

nullable

string

The person’s last name.

updated

timestamp

Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

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

:account_id

/

persons

/

:id

curl

https://api.stripe.com/v2/core/accounts/

acct_1Nv0FGQ9RKHgCVdK

/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \

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

Response

{

"

id

"

:

"

person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY

"

,

"

object

"

:

"

v2.core.account_person

"

,

"

account

"

:

"

acct_1Nv0FGQ9RKHgCVdK

"

,

"

additional_addresses

"

:

[],

"

additional_names

"

:

[],

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

Brothers

"

,

"

country

"

:

"

us

"

,

"

line1

"

:

"

27 Fredrick Ave

"

,

"

postal_code

"

:

"

97712

"

,

"

state

"

:

"

OR

"

},

"

created

"

:

"

2024-11-26T17:10:07.000Z

"

,

"

date_of_birth

"

:

{

"

day

"

:

28

,

"

month

"

:

1

,

"

year

"

:

2000

},

"

email

"

:

"

jenny.rosen@example.com

"

,

"

given_name

"

:

"

Jenny

"

,

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

us_ssn_last_4

"

}

],

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

{},

"

nationalities

"

:

[],

"

relationship

"

:

{

"

owner

"

:

true

,

"

percent_ownership

"

:

"

0.8

"

,

"

representative

"

:

true

,

"

title

"

:

"

CEO

"

},

"

surname

"

:

"

Rosen

"

,

"

updated

"

:

"

2024-11-26T17:12:55.000Z

"

}
