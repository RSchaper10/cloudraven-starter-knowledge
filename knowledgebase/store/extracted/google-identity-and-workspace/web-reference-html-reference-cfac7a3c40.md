---
title: Sign in with Google HTML API reference | Web guides | Google for Developers
source_url: https://developers.google.com/identity/gsi/web/reference/html-reference
target_id: google-identity-and-workspace
dependency: Google Identity and Workspace Events
collected_at: 2026-04-16T03:21:01.507286+00:00
kind: extracted-doc
---

# Sign in with Google HTML API reference | Web guides | Google for Developers

Source URL:

- https://developers.google.com/identity/gsi/web/reference/html-reference

Dependency:

- Google Identity and Workspace Events

Collected at:

- 2026-04-16T03:21:01.507286+00:00

Direct links in scope:

- https://developers.google.com/identity/gsi/web/reference/html-reference
- https://developers.google.com/identity/gsi/web/guides/personalized-button
- https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid
- https://developers.google.com/identity/gsi/web/reference/js-reference
- https://developers.google.com/identity/gsi/web/guides/features
- https://developers.google.com/identity/gsi/web/guides/fedcm-migration
- https://developers.google.com/identity/gsi/web/guides/handle-credential-responses-js-functions
- https://developers.google.com/identity/gsi/web/guides/verify-google-id-token
- https://developers.google.com/identity/gsi/web/guides/supported-browsers
- https://developers.google.com/identity/gsi/web/guides/itp

Captured summary:

- Sign in with Google HTML API reference | Web guides | Google for Developers Skip to main content Identity Web guides / English Deutsch Español Español – América Latina Français Indonesia Italiano Polski Português – Brasil Tiếng Việt Türkçe Русский עברית العربيّة فارسی हिंदी বাংলা ภาษาไทย 中文 – 简体 中文 – 繁體 日本語 한국어 Sign in Home Products Google Identity Web guides Web API References Send feedback Sign in with Google HTML API reference Stay organized with collections Save and categorize content based on your preferences.
- Page Summary outlined_flag The Sign in with Google HTML data attributes API is used to display the Sign In With Google button or One Tap prompt on webpages.
- Data attributes for configuring the Sign In With Google button and One Tap prompt are placed within an element with the ID "g_id_onload".
- Key data attributes include data-client_id , data-callback or data-login_uri for handling the ID token response, and various visual attributes for customizing the Sign In With Google button.
- Server-side integration involves handling HTTP POST requests to process the returned ID token and password credentials.

Extracted text:

Sign in with Google HTML API reference | Web guides | Google for Developers

Skip to main content

Identity

Web guides

/

English

Deutsch

Español

Español – América Latina

Français

Indonesia

Italiano

Polski

Português – Brasil

Tiếng Việt

Türkçe

Русский

עברית

العربيّة

فارسی

हिंदी

বাংলা

ภาษาไทย

中文 – 简体

中文 – 繁體

日本語

한국어

Sign in

Home

Products

Google Identity

Web guides

Web API References

Send feedback

Sign in with Google HTML API reference

Stay organized with collections

Save and categorize content based on your preferences.

Page Summary

outlined_flag

The Sign in with Google HTML data attributes API is used to display the Sign In With Google button or One Tap prompt on webpages.

Data attributes for configuring the Sign In With Google button and One Tap prompt are placed within an element with the ID "g_id_onload".

Key data attributes include

data-client_id

,

data-callback

or

data-login_uri

for handling the ID token response, and various visual attributes for customizing the Sign In With Google button.

Server-side integration involves handling HTTP POST requests to process the returned ID token and password credentials.

The

sub

field of the ID token is the recommended unique identifier for a user.

This reference page describes the Sign in with Google HTML data attributes API, used to display the Sign In With Google button or One Tap prompt on web pages.

Element with ID "g_id_onload"

You can put Sign In With Google data attributes in any visible or invisible elements, such as

<div>

and

<span>

. The only requirement is that the element ID is set to

g_id_onload

. Don't put this ID on multiple elements.

Data attributes

The following table lists the data attributes with their descriptions:

Attribute

data-client_id

Your application's client ID

data-color_scheme

The color scheme applied to the One Tap prompt.

data-auto_prompt

Display Google One tap.

data-auto_select

Enables automatic selection on Google One Tap.

data-login_uri

The URL of your login endpoint

data-callback

The JavaScript ID token handler function name

data-native_login_uri

The URL of your password credential handler endpoint

data-native_callback

The JavaScript password credential handler function name

data-native_id_param

The parameter name for the

credential.id

value

data-native_password_param

The parameter name for the

credential.password

value

data-cancel_on_tap_outside

Controls whether to cancel the prompt if the user clicks outside of the prompt.

data-prompt_parent_id

The DOM ID of the One Tap prompt container element

data-skip_prompt_cookie

Skips One Tap if the specified cookie has a non-empty value.

data-nonce

A random string for ID tokens

data-context

The title and words in the One Tap prompt

data-moment_callback

The function name of the prompt UI status notification listener

data-state_cookie_domain

If you need to call One Tap in the parent domain and its subdomains, pass the parent domain to this attribute so that a single shared cookie is used.

data-ux_mode

The Sign In With Google button UX flow

data-allowed_parent_origin

The origins that are allowed to embed the intermediate iframe. One Tap runs in the intermediate iframe mode if this attribute is present.

data-intermediate_iframe_close_callback

Overrides the default intermediate iframe behavior when users manually close One Tap.

data-itp_support

Enables upgraded One Tap UX on ITP browsers.

data-login_hint

Skip account selection by providing a user hint.

data-hd

Limit account selection by domain.

data-use_fedcm_for_prompt

Allow the browser to control user sign-in prompts and mediate the sign-in flow between your website and Google.

data-use_fedcm_for_button

This field determines if FedCM button UX should be used on Chrome (desktop M125+ and Android M128+). Defaults to

false

.

data-button_auto_select

Whether to enable the

auto select

option for the FedCM button flow. If enabled, returning users with an active Google session will be automatically signed in, bypassing the Account Chooser prompt. Default value is

false

.

Attribute types

The following sections contain details about each attribute's type and an example.

data-client_id

This attribute is your app's client ID, which is found and created in the Google Cloud console. See the following table for further information:

Type

Required

Example

string

Yes

data-client_id="CLIENT_ID.apps.googleusercontent.com"

data-color_scheme

This field is the color scheme applied to the One Tap prompt. See the following table for further information:

Type

Required

Example

string

Optional. Defaults to the users system default color scheme.

data-color_scheme="dark"

The following table lists the available color schemes and their descriptions.

Color scheme

default

Apply the default color scheme of the user's system, depending on user preference scheme is either light or dark.

light

Apply a light color scheme.

dark

Apply a dark color scheme.

data-auto_prompt

This attribute determines whether to display One tap or not. The default value is

true

. Google One tap is not displayed when this value is

false

. See the following table for further information:

Type

Required

Example

boolean

Optional

data-auto_prompt="true"

data-auto_select

This attribute determines whether or not to return an ID token automatically, without any user interaction, if only one Google session has approved your app. The default value is

false

. See the following table for further information:

Type

Required

Example

boolean

Optional

data-auto_select="true"

data-login_uri

This attribute is the URI of your login endpoint.

The value must exactly match one of the authorized redirect URIs for the OAuth 2.0 client, which you

configured

in the Google Auth Platform and must conform to our

Redirect URI validation rules

.

This attribute may be omitted if the current page is your login page, in which case the credential is posted to this page by default.

The ID token credential response is posted to your login endpoint when no callback function is defined and a user clicks on the Sign In With Google or One Tap buttons, or automatic sign takes place.

Your

login endpoint

must handle POST requests containing a

credential

parameter with an ID token value in the body.

See the following table for further information:

Type

Optional

Example

URL

Defaults to the URI of the current page, or the value you specify.

Ignored when

data-ux_mode="popup"

and

data-callback

is set.

data-login_uri="https://www.example.com/login"

data-callback

This attribute is the name of the JavaScript function that handles the returned ID token. See the following table for further information:

Type

Required

Example

string

Required if

data-login_uri

isn't set.

data-callback="handleToken"

One of the

data-login_uri

and

data-callback

attributes might be used. It depends on the following component and UX mode configurations:

The

data-login_uri

attribute is required for the Sign In With Google button

redirect

UX mode, which ignores the

data-callback

attribute.

One of these two attributes must be set for Google One Tap and the Google Sign-In button

popup

UX mode. If both are set, the

data-callback

attribute has a higher precedence.

JavaScript functions within a namespace are not supported by the HTML API. Instead, use a global JavaScript function without a namespace. For example, use

mylibCallback

instead of

mylib.callback

.

data-native_login_uri

This attribute is the URL of your password credential handler endpoint. If you set either the

data-native_login_uri

attribute or the

data-native_callback

attribute, the JavaScript library falls back to the built-in credential manager when there isn't a Google session. You're not allowed to set both the

data-native_callback

and

data-native_login_uri

attributes. See the following table for further information:

Type

Required

Example

string

Optional

data-login_uri="https://www.example.com/password_login"

data-native_callback

This attribute is the name of the JavaScript function that handles the password credential returned from the browser's built-in credential manager. If you set either the

data-native_login_uri

attribute or the

data-native_callback

attribute, the JavaScript library falls back to the built-in credential manager when there isn't a Google session. You're not allowed to set both

data-native_callback

and

data-native_login_uri

. See the following table for further information:

Type

Required

Example

string

Optional

data-native_callback="handlePasswordCredential"

JavaScript functions within a namespace are not supported by the HTML API. Instead, use a global JavaScript function without a namespace. For example, use

mylibCallback

instead of

mylib.callback

.

data-native_id_param

When you submit the password credential to the password credential handler endpoint, you can specify the parameter name for the

credential.id

field. The default name is

email

. See the following table for further information:

Type

Required

Example

URL

Optional

data-native_id_param="user_id"

data-native_password_param

When you submit the password credential to the password credential handler endpoint, you can specify the parameter name for the

credential.password

value. The default name is

password

. See the following table for further information:

Type

Required

Example

URL

Optional

data-native_password_param="pwd"

data-cancel_on_tap_outside

This attribute sets whether or not to cancel the One Tap request if the user clicks outside of the prompt. The default value is

true

. To disable it, set the value to

false

. See the following table for further information:

Type

Required

Example

boolean

Optional

data-cancel_on_tap_outside="false"

data-prompt_parent_id

This attribute sets the DOM ID of the container element. If it's not set, the One Tap prompt is displayed at the top-right corner of the window. See the following table for further information:

Type

Required

Example

string

Optional

data-prompt_parent_id="parent_id"

data-skip_prompt_cookie

Uses a cookie to control display of the One Tap prompt. If the cookie specified by this attribute has a non-empty value the prompt is not displayed. See the following table for further information:

Type

Required

Example

string

Optional

data-skip_prompt_cookie="SID"

data-nonce

This attribute is a random string used by the ID token to prevent replay attacks. See the following table for further information:

Type

Required

Example

string

Optional

data-nonce="biaqbm70g23"

Nonce length is limited to the maximum JWT size supported by your environment, and individual browser and server HTTP size constraints.

data-context

This field changes the text of the title and messages shown in the One Tap prompt, no effect for ITP browsers. Defaults to

signin

.

See the following table for further information:

Type

Required

Example

string

Optional

data-context="use"

The following table lists

all

the available contexts and their descriptions:

Context

signin

"Sign in to"

signup

"Sign up to"

use

"Use"

data-moment_callback

This attribute is the function name of the prompt UI status notification listener. For more information, refer to the data type

PromptMomentNotification

.

See the following table for further information:

Type

Required

Example

string

Optional

data-moment_callback="logMomentNotification"

JavaScript functions within a namespace are not supported by the HTML API. Instead, use a global JavaScript function without a namespace. For example, use

mylibCallback

instead of

mylib.callback

.

data-state_cookie_domain

If you need to display One Tap in a parent domain and its subdomains, pass the parent domain to this attribute so that a single shared-state cookie is used. See the following table for further information:

Type

Required

Example

string

Optional

data-state_cookie_domain="example.com"

data-ux_mode

This attribute sets the UX flow used by the Sign In With Google button. The default value is

popup

. This attribute has no impact on the One Tap UX. See the following table for further information:

Type

Required

Example

string

Optional

data-ux_mode="redirect"

The following table lists the available UX modes and their descriptions.

UX Mode

popup

Performs sign-in UX flow in a pop-up window.

redirect

Performs sign-in UX flow by a full page redirection.

data-allowed_parent_origin

The origins that are allowed to embed the intermediate iframe. One Tap runs in the intermediate iframe mode if this attribute presents. See the following table for further information:

Type

Required

Example

string or string array

Optional

data-allowed_parent_origin="https://example.com"

The following table lists the supported value types and their descriptions.

Value Types

string

A single domain URI.

"https://example.com"

string array

A list of comma-separated domain URIs.

"https://news.example.com,https://local.example.com"

If the value of

data-allowed_parent_origin

attribute is invalid, the One Tap initialization of the intermediate iframe mode would fail and stop.

Wildcard prefixes are also supported. For example,

"https://*.example.com"

matches

example.com

and its subdomains at all levels (e.g

news.example.com

,

login.news.example.com

). Things to keep in mind when using wildcards:

Pattern strings cannot be composed of only a wildcard and a top level domain. For example

https://

.com

and

https://

.co.uk

are invalid as

"https://

.example.com"

matches

example.com

and all its subdomains. Use a comma separated list to represent two different domains. For example,

"https://example1.com,https://

.example2.com"

matches the domains

example1.com

,

example2.com

and the subdomains of

example2.com

Wildcard domains must begin with a secure https:// scheme, so

"*.example.com"

is considered invalid.

data-intermediate_iframe_close_callback

Overrides the default intermediate iframe behavior when users manually close One Tap by tapping on the 'X' button in the One Tap UI. The default behavior is to remove the intermediate iframe from the DOM immediately.

The

data-intermediate_iframe_close_callback

field takes effect only in intermediate iframe mode. And it has impact only to the intermediate iframe, instead of the One Tap iframe. The One Tap UI is removed before the callback is invoked.

Type

Required

Example

function

Optional

data-intermediate_iframe_close_callback="logBeforeClose"

JavaScript functions within a namespace are not supported by the HTML API. Instead, use a global JavaScript function without a namespace. For example, use

mylibCallback

instead of

mylib.callback

.

data-itp_support

This field determines if the

upgraded One Tap UX

should be enabled on browsers that support Intelligent Tracking Prevention (ITP). The default value is

false

. See the following table for further information:

Type

Required

Example

boolean

Optional

data-itp_support="true"

data-login_hint

If your application knows in advance which user should be signed-in, it can provide a login hint to Google. When successful, account selection is skipped. Accepted values are: an email address or an ID token

sub

field.

For more information, see the OpenID Connect documentation for

login_hint

.

Type

Required

Example

String. Can be an email address or the

sub

field value from ID token.

Optional

data-login_hint="elisa.beckett@gmail.com"

data-hd

When a user has multiple accounts and should only sign-in with their Workspace account use this to provide a domain name hint to Google. When successful, user accounts displayed during account selection are limited to the provided domain. A wildcard value:

*

offers only Workspace accounts to the user and excludes consumer accounts (user@gmail.com) during account selection.

For more information, see the OpenID Connect documentation for

hd

.

Type

Required

Example

String. A fully qualified domain name or *.

Optional

data-hd="*"

data-use_fedcm_for_prompt

Allow the browser to control user sign-in prompts and mediate the sign-in flow between your website and Google. Defaults to false. See

Migrate to FedCM

page for more information.

Type

Required

Example

boolean

Deprecated

data-use_fedcm_for_prompt="true"

data-use_fedcm_for_button

This field determines if FedCM button UX should be used on Chrome (desktop M125+ and Android M128+). Defaults to

false

. See the following table for further information:

Type

Required

Example

boolean

Optional

data-use_fedcm_for_button="true"

data-button_auto_select

This field determines whether to enable the

auto select

option for the FedCM button flow. If enabled, returning users with an active Google session will be automatically signed in, bypassing the Account Chooser prompt. Defaults to

false

. You need to explicitly enable button auto-sign-in during the opt-in launch. See the following table for further information:

Type

Required

Example

boolean

Optional

data-button_auto_select="true"

Element with class "g_id_signin"

If you add

g_id_signin

to an element's

class

attribute, the element renders as a Sign In With Google button.

You can render multiple Sign In With Google buttons on the same page. Each button can have its own visual settings. The settings are defined by the following data attributes.

Visual Data attributes

The following table lists visual data attributes and their descriptions:

Attribute

data-type

The button type: icon, or standard button.

data-theme

The button theme. For example, filled_blue or filled_black.

data-size

The button size. For example, small or large.

data-text

The button text. For example, "Sign in with Google" or "Sign up with Google".

data-shape

The button shape. For example, rectangular or circular.

data-logo_alignment

The Google logo alignment: left or center.

data-width

The button width, in pixels.

data-locale

The button text renders in the language set in this attribute.

data-click_listener

If set, this function is called when the Sign In With Google button is clicked.

data-state

If set, this string returns with the ID token.

Attribute types

The following sections contain details about each attribute's type and an example.

data-type

The button type. The default value is

standard

. See the following table for further information:

Type

Required

Example

string

Yes

data-type="icon"

The following table lists

all

the available button types and their descriptions:

Type

standard

A button with text or personalized information.

icon

An icon button without text.

data-theme

The button theme. The default value is

outline

. See the following table for further information:

Type

Required

Example

string

Optional

data-theme="filled_blue"

The following table lists the available themes and their descriptions:

Theme

outline

The standard button theme.

filled_blue

The blue-filled button theme.

filled_black

The black-filled button theme.

data-size

The button size. The default value is

large

. See the following table for further information:

Type

Required

Example

string

Optional

data-size="small"

The following table lists the available button sizes and their descriptions.

Size

large

A large button.

medium

A medium-sized button.

small

A small button.

data-text

The button text. The default value is

signin_with

. There are no visual differences for the text of icon buttons that have different

data-text

attributes. The only exception is when the text is read for screen accessibility.

See the following table for further information:

Type

Required

Example

string

Optional

data-text="signup_with"

The following table lists the available button texts and their descriptions:

Text

signin_with

The button text is "Sign in with Google".

signup_with

The button text is "Sign up with Google".

continue_with

The button text is "Continue with Google".

signin

The button text is "Sign in".

data-shape

The button shape. The default value is

rectangular

. See the following table for further information:

Type

Required

Example

string

Optional

data-shape="rectangular"

The following table lists the available button shapes and their descriptions:

Shape

rectangular

The rectangular-shaped button. If used for the

icon

button type, it's the same as

square

.

pill

The pill-shaped button. If used for the

icon

button type, then it's the same as

circle

.

circle

The circle-shaped button. If used for the

standard

button type, then it's the same as

pill

.

square

The square-shaped button. If used for the

standard

button type, then it's the same as

rectangular

.

data-logo_alignment

The alignment of the Google logo. The default value is

left

. This attribute only applies to the

standard

button type. See the following table for further information:

Type

Required

Example

string

Optional

data-logo_alignment="center"

The following table lists the available alignments and their descriptions:

logo_alignment

left

Left-aligns the Google logo.

center

Center-aligns the Google logo.

data-width

The minimum button width, in pixels. The maximum width available is 400 pixels.

See the following table for further information:

Type

Required

Example

string

Optional

data-width=400

data-locale

Optional. Display button text using the specified locale, otherwise default to the users Google Account or browser settings. Add the

hl

parameter and language code to the src directive when loading the library, for example:

gsi/client?hl=<iso-639-code>

.

If it's not set, the browser's default locale or the Google session user's preference is used. Therefore, different users might see different versions of localized buttons, and possibly with different sizes.

See the following table for further information:

Type

Required

Example

string

Optional

data-locale="zh_CN"

data-click_listener

You can define a JavaScript function to be called when the Sign in with Google button is clicked using the

data-click_listener

attribute.

<script>

function onClickHandler(){ console.log("Sign in with Google button clicked...") }

</script> ..... <div class="g_id_signin" data-size="large" data-theme="outline"

data-click_listener="onClickHandler"

> </div>

In this example, the message

Sign in with Google button clicked...

is logged to the console when the Sign in with Google button is clicked.

data-state

Optional, as multiple Sign in with Google buttons can be rendered on the same page, you can assign each button with a unique string. The same string would return along with the ID token, so you can identify which button user clicked to sign in.

See the following table for further information:

Type

Required

Example

string

Optional

data-state="button 1"

Server-side integration

Your server-side endpoints must handle the following HTTP

POST

requests.

The ID token handler endpoint

The ID token handler endpoint processes the ID token. Based on the status of the corresponding account, you can sign the user in and either direct them to a sign-up page or direct them to an account-linking page for additional information. Clients MUST ignore unrecognized response parameters.

An example request to your login endpoint:

POST /login HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Cookie: g_csrf_token=<RANDOM_STRING>

Host: www.example.com

credential=<JWT_ENCODED_ID_TOKEN>&g_csrf_token=<RANDOM_STRING>

The HTTP

POST

request contains the following information:

Format

Name

Description

Cookie

g_csrf_token

A random string that changes with each request to the login endpoint specified by

data-login_uri

, must match the value in the

g_csrf_token

request parameter.

Request parameter

g_csrf_token

A random string that changes with each request to the login endpoint specified by

data-login_uri

, must match the value of the

g_csrf_token

cookie.

Request parameter

credential

The encoded JWT ID token that Google issues.

Request parameter

select_by

How the user signed in.

Request parameter

state

This parameter is only defined when user clicks a Sign in with Google button to sign in, and the button's

state

attribute is specified.

credential

When

decoded

, the ID token looks like the following example:

header

{

"alg"

:

"RS256"

,

"kid"

:

"f05415b13acb9590f70df862765c655f5a7a019e"

,

//

JWT

signature

"typ"

:

"JWT"

}

payload

{

"iss"

:

"https://accounts.google.com"

,

//

The

JWT

's issuer

"nbf"

:

161803398874

,

"aud"

:

"314159265-pi.apps.googleusercontent.com"

,

//

Your

server

's client ID

"sub"

:

"3141592653589793238"

,

//

The

unique

ID

of

the

user

's Google Account

"hd"

:

"gmail.com"

,

//

If

present

,

the

host

domain

of

the

user

's GSuite email address

"email"

:

"elisa.g.beckett@gmail.com"

,

//

The

user

's email address

"email_verified"

:

true

,

//

true

,

if

Google

has

verified

the

email

address

"azp"

:

"314159265-pi.apps.googleusercontent.com"

,

"name"

:

"Elisa Beckett"

,

//

If

present

,

a

URL

to

user

's profile picture

"picture"

:

"https://lh3.googleusercontent.com/a-/e2718281828459045235360uler"

,

"given_name"

:

"Eliza"

,

"family_name"

:

"Beckett"

,

"iat"

:

1596474000

,

//

Unix

timestamp

of

the

assertion

's creation time

"exp"

:

1596477600

,

//

Unix

timestamp

of

the

assertion

's expiration time

"jti"

:

"abc161803398874def"

}

Clients MUST ignore unrecognized JWT claims.

The

sub

field is a globally unique identifier for the Google Account.

Only

use

sub

field as identifier for the user as it is unique among all Google Accounts and never reused.

Using the

email

,

email_verified

and

hd

fields you can determine if Google hosts and is authoritative for an email address. In cases where Google is authoritative the user is confirmed to be the legitimate account owner.

Cases where Google is authoritative:

email

has a

@gmail.com

suffix, this is a Gmail account.

email_verified

is true and

hd

is set, this is a Google Workspace account.

Users may register for Google Accounts without using Gmail or Google Workspace. When

email

does not contain a

@gmail.com

suffix and

hd

is absent Google is not authoritative and password or other challenge methods are recommended to verify the user.

email_verified

can also be true as Google initially verified the user when the Google Account was created, however ownership of the third party email account may have since changed.

The

exp

field shows the expiration time for you to

verify the token on your server side

. It is one hour for the ID token obtained from Sign In With Google. You need to

verify the token

before the expiration time.

Don't use

exp

for session management.

An expired ID token does

not

mean the user is signed out. Your app is responsible for session management of your users.

g_csrf_token

An anti-forgery state token. This is a Cross-site request forgery (CSRF) token created by the

gsi/client

library. A random value is included both as a Cookie and as a Request Parameter in the POST payload body. If these two values don't match when processing the request on your server, the request should be considered invalid.

select_by

The following table lists the possible values for the

select_by

field. The type of button used along with the session and consent state are used to set the value,

The user pressed either the One Tap or Sign In With Google button or used the touchless Automatic sign-in process.

An existing session was found, or the user selected and signed-in to a Google Account to establish a new session.

Prior to sharing ID token credentials with your app the user either

pressed the Confirm button to grant their consent to share credentials, or

had previously granted consent and used Select an Account to choose a Google Account.

The value of this field is set to one of these types,

Value

Description

auto

Automatic sign-in of a user with an existing session who had previously granted consent to share credentials. Applies only to non-FedCM supported browsers.

user

A user with an existing session who had previously granted consent pressed the One Tap 'Continue as' button to share credentials. Applies only to non-FedCM supported browsers.

fedcm

A user pressed the One Tap 'Continue as' button to share credentials using FedCM. Applies only to FedCM

supported

browsers.

fedcm_auto

Automatic sign-in of a user with an existing session who had previously granted consent to share credentials using FedCM One Tap. Applies only to FedCM

supported

browsers.

user_1tap

A user with an existing session pressed the One Tap 'Continue as' button to grant consent and share credentials. Applies only to Chrome v75 and higher.

user_2tap

A user without an existing session pressed the One Tap 'Continue as' button to select an account and then pressed the Confirm button in a pop-up window to grant consent and share credentials. Applies to non-Chromium based browsers.

itp

A user who had previously granted consent pressed the One Tap on

ITP

browsers.

itp_confirm

A user who did not grant consent pressed the One Tap on

ITP

browsers and pressed the 'Continue' button to grant consent and share credentials.

btn

A user who had previously granted consent pressed the Sign In With Google button and selected a Google Account from 'Choose an Account' to share credentials.

btn_confirm

A user who did not grant consent pressed the Sign In With Google button and pressed the 'Continue' button to grant consent and share credentials.

state

This parameter is only defined when user clicks a Sign in with Google button to sign in, and the clicked button's

data-state

attribute is specified. The value of this field is the same value you specified in the button's

data-state

attribute.

As multiple Sign in with Google buttons can be rendered on the same page, you can assign each button with a unique string. Hence, you can this

state

parameter to identify which button user clicked to sign in.

Password credential handler endpoint

The password credential handler endpoint processes password credentials that the built-in credential manager retrieves.

The HTTP

POST

request contains the following information:

Format

Name

Description

Cookie

g_csrf_token

A random string that changes with each request to the login endpoint specified by

data-native_login_uri

, must match the value in the

g_csrf_token

request parameter.

Request parameter

g_csrf_token

A random string that changes with each request to the login endpoint specified by

data-native_login_uri

, must match the value of the

g_csrf_token

cookie.

Request parameter

email

This ID token that Google issues.

Request parameter

password

How the credential is selected.

Send feedback

Except as otherwise noted, the content of this page is licensed under the

Creative Commons Attribution 4.0 License

, and code samples are licensed under the

Apache 2.0 License

. For details, see the

Google Developers Site Policies

. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-10 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-10 UTC."],[],[]]
