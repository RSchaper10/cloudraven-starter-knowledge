---
title: Send events to Amazon EventBridge | Stripe Documentation
source_url: https://docs.stripe.com/event-destinations/eventbridge
target_id: stripe-and-eventbridge
dependency: Stripe and EventBridge
collected_at: 2026-04-16T03:23:45.456646+00:00
kind: extracted-doc
---

# Send events to Amazon EventBridge | Stripe Documentation

Source URL:

- https://docs.stripe.com/event-destinations/eventbridge

Dependency:

- Stripe and EventBridge

Collected at:

- 2026-04-16T03:23:45.456646+00:00

Direct links in scope:

- https://docs.stripe.com/event-destinations/eventbridge
- https://docs.stripe.com/event-destinations/eventgrid
- https://docs.stripe.com/api/v2/event-destinations
- https://docs.stripe.com/api/events/types
- https://docs.stripe.com/api/events
- https://docs.stripe.com/api
- https://docs.stripe.com/payments/checkout
- https://docs.stripe.com/api/v2/core/events/event-types
- https://docs.stripe.com/api/events/

Captured summary:

- Send events to Amazon EventBridge | Stripe Documentation Skip to content Amazon EventBridge Create account or Sign in Search / Ask AI Create account Sign in Get started Payments Revenue Platforms and marketplaces Money management Developer resources APIs & SDKs Help Overview Versioning Changelog Upgrade your API version Upgrade your SDK version Essentials SDKs API Testing Stripe CLI Sample projects Tools Stripe Dashboard Workbench Developers Dashboard Stripe for Visual Studio Code Terraform Features Workflows Batch jobs Event destinations Integrate with events Amazon EventBridge Azure Event Grid Webhook endpoint Stripe health alerts File uploads AI solutions Agent toolkit Model Context Protocol Build agentic AI SaaS Billing workflows Security and privacy Security Stripebot web crawler Privacy Extend Stripe Extension points Build Stripe apps Use apps from Stripe Partners Partner ecosystem Partner certification United States English (United States) Send events to Amazon EventBridge Consume Stripe events in your AWS infrastructure.
- Ask about this page Copy for LLM View as Markdown Enable Workbench To send events to Amazon EventBridge, enable Workbench in your Developer settings in the Dashboard.
- Amazon EventBridge is a serverless, event-driven service provided by AWS that helps connect your applications together by ingesting, transforming, and delivering events.
- Integrating with EventBridge using an event destination allows you to receive event data from Stripe directly in your AWS account, instead of handling the traffic and managing integration code logic yourself.
- When events are received, EventBridge can route them to 20 supported targets to process or trigger business automations.

Extracted text:

Send events to Amazon EventBridge | Stripe Documentation

Skip to content

Amazon EventBridge

Create account

or

Sign in

Search

/

Ask AI

Create account

Sign in

Get started

Payments

Revenue

Platforms and marketplaces

Money management

Developer resources

APIs & SDKs

Help

Overview

Versioning

Changelog

Upgrade your API version

Upgrade your SDK version

Essentials

SDKs

API

Testing

Stripe CLI

Sample projects

Tools

Stripe Dashboard

Workbench

Developers Dashboard

Stripe for Visual Studio Code

Terraform

Features

Workflows

Batch jobs

Event destinations

Integrate with events

Amazon EventBridge

Azure Event Grid

Webhook endpoint

Stripe health alerts

File uploads

AI solutions

Agent toolkit

Model Context Protocol

Build agentic AI SaaS Billing workflows

Security and privacy

Security

Stripebot web crawler

Privacy

Extend Stripe

Extension points

Build Stripe apps

Use apps from Stripe

Partners

Partner ecosystem

Partner certification

United States

English (United States)

Send events to Amazon

EventBridge

Consume Stripe events in your AWS infrastructure.

Ask about this page

Copy for LLM

View as Markdown

Enable Workbench

To send events to Amazon EventBridge, enable Workbench in your

Developer settings

in the Dashboard.

Amazon EventBridge

is a serverless, event-driven service provided by AWS that helps connect your applications together by ingesting, transforming, and delivering events. Integrating with EventBridge using an event destination allows you to receive event data from Stripe directly in your AWS account, instead of handling the traffic and managing integration code logic yourself. When events are received, EventBridge can route them to

20 supported targets

to process or trigger business automations.

Send events to Amazon EventBridge

Complete the steps below to receive events in EventBridge. This involves creating a new event destination in Workbench and setting up EventBridge configuration in the

AWS Management Console

.

Warning

You won’t receive any event data in your Amazon EventBridge until you complete each step.

Add a new event

destination

Workbench

Send events in your sandbox

Use your live account or

sandboxes

to send events to Amazon EventBridge.

Create an event destination using Workbench in the Dashboard or programmatically with the

API

.

Dashboard

API

To create an event destination in the Dashboard:

Open the

Webhooks

tab in Workbench.

Click

Create new destination

.

Select where you want to receive events from. Stripe supports two types of configurations:

Your account

and

Connected accounts

. Select

Account

to listen to events from your own account. If you created a

Connect application

and want to listen to events from your connected accounts, select

Connected accounts

.

Listen to events from an Organization event destination

If you create an event destination in an

Organization account

, select

Accounts

to listen to events from accounts in your organization. If you have

Connect platforms

as members of your organizations and want to listen to events from the all the platforms’ connected accounts, select

Connected accounts

.

Select the

event types

that you want this destination to receive. Then, click

Continue

.

Select

Amazon EventBridge

as your destination type, then click

Continue

.

Enter the following information:

AWS account ID

: The AWS account that hosts your EventBridge instance for receiving events.

AWS region

: The AWS region that hosts your EventBridge instance for receiving events.

(Optional)

Destination name

: A unique name of this event destination resource in Stripe. If you don’t provide one, we generate a random name for you. You can change it later.

(Optional)

Description

: A description that distinguishes your event destination instance. You can modify this later.

Click

Create destination

.

Register a new webhook in the

Webhooks

tab

Associate the partner event

source

AWS Console

After you set up an event destination, Stripe creates a

partner event source

in the AWS account and region you provided during configuration. To start receiving events, you need to associate this event source with an

event bus

within 7 days of the event destination’s creation. If you don’t associate it within this time frame, Amazon automatically deletes the pending event source. After an event source is deleted, your Stripe event destination is automatically disabled and you must create a new destination to receive events.

Under

EventBridge

in your

AWS console

, go to the

Partner event sources page

that’s listed in the

Integration

section of the left-hand panel.

Use the

Region

dropdown list located at the top of the console to select the region you chose when configuring your

event destination in Workbench

.

Choose the newly created partner event source in the dropdown. To find the Event Source ARN field in Workbench, select your event destination. Your partner source matches the part of the ARN that reads

event-source/aws

.

partner/stripe

.

com/{UNIQUE

_

ID}

. Then, click

Associate with event bus

.

Select permissions you want to grant for this event bus as needed, then click

Associate

.

Create EventBridge

rules

AWS Console

EventBridge groups and routes events based on

rules

you define. After you create an event destination and associate its partner event source to an event bus, you must define rules to make sure that EventBridge knows how to handle the events it receives on the event bus. You can repeat these steps multiple times to define multiple rules.

Navigate to the AWS management console, then click

Rules

.

Click

Create Rule

, then provide a rule name and description.

Select your event bus from the dropdown. To find your event bus, go to Workbench, select your destination in the

Webhooks

tab, then view the

Event source ARN

field, which shares the same name as your event source ARN. Then, click

Next

.

Under

Event source

, select

AWS events or EventBridge partner events

because Stripe events are partner events.

(Optional) Include a sample Stripe event.

Under

Creation Method

, choose

Use pattern form

to use a predefined pattern. Alternatively, you can create a custom event pattern.

Under

Event Pattern

, select

EventBridge partners

as the

Event Source

.

Under

Event Pattern

, select

Stripe

as the

Partner

.

Select the appropriate event type you want to create a rule for or select

All events

to match this rule to all event types, then click

Next

.

Select the

target

you want this rule to send events to, then click

Next

.

Recommendation

We recommend you

create a CloudWatch Logs target

for each event bus to enable monitoring for your event destination. Consider using other

common architecture patterns

with EventBridge and Stripe events.

Add optional tags, then click

Next

.

Review your rule and make changes as needed, then click

Create Rule

.

Your Stripe events are now successfully delivered to EventBridge and its corresponding targets defined in your rule.

Trigger test events

To send test events, trigger an event type that your event destination is subscribed to by manually creating an object in the Stripe Dashboard. Learn how to trigger events with

Stripe for VS Code

.

Trigger a snapshot event

Trigger a thin event

You can use the following command in either

Stripe Shell

or

Stripe CLI

.

This example triggers a

payment

_

intent

.

succeeded

event:

Command Line

stripe

trigger

payment_intent.succeeded

Running fixture for: payment_intent Trigger succeeded

!

Check dashboard

for

event details.

Thin event hydration

Thin events

are notifications that include reference information about the API resource related to the event. When you send them to Amazon EventBridge, you can use that information to fetch the full event or API resource object (also known as “event hydration”). In the AWS console, you can set up this pipeline by configuring EventBridge rules and

targets

. When you send thin events to

webhook endpoints

, you must fetch the complete event or resource data yourself using the API. This process provides you with fresh data by fetching the current state of the resource associated with every event.

Event delivery behaviors

This section helps you understand different behaviors to expect regarding how Stripe sends events to Amazon EventBridge.

Automatic retries

Stripe attempts to deliver events to your destination for up to three days with an exponential back off in live mode. View when the next retry will occur, if applicable, in your event destination’s

Event deliveries

tab.

We retry event deliveries created in a sandbox three times over the course of a few hours.

If your destination has been disabled or deleted when we attempt a retry, we prevent future retries of that event. However, if you disable and then re-enable the event destination before we’re able to retry, you still see future retry attempts.

Manual retries

You can’t manually resend events to Amazon EventBridge.

Event ordering

Stripe doesn’t guarantee the delivery of events in the order that they’re generated. For example, creating a subscription might generate the following events:

customer

.

subscription

.

created

invoice

.

created

invoice

.

paid

charge

.

created

(if there’s a charge)

Make sure that your event destination isn’t dependent on receiving events in a specific order. Be prepared to manage their delivery appropriately.

You can also use the API to retrieve any missing objects. For example, you can retrieve the invoice, charge, and subscription objects with the information from

invoice

.

paid

if you receive this event first.

API versioning

The API version in your account settings when the event occurs dictates the API version, and therefore the structure of an

Event

sent to your destination. For example, if your account is set to an older API version, such as 2015-02-16, and you change the API version for a specific request with

versioning

, the

Event

object generated and sent to your destination is still based on the 2015-02-16 API version.

You can’t change

Event

objects after creation. For example, if you update a charge, the original charge event remains unchanged. As a result, subsequent updates to your account’s API version don’t retroactively alter existing

Event

objects. Retrieving an older

Event

by calling

/v1/events

using a newer API version also has no impact on the structure of the received event.

You can set test event destinations to either your default API version or the latest API version. The

Event

sent to the destination is structured for the event destination’s specified version.

Event destination status

Amazon EventBridge destinations have several statuses that describe their readiness to receive events:

Active

: Stripe is sending events to Amazon EventBridge if you have associated the partner event source in AWS.

Disabled

: Stripe isn’t sending events to Amazon EventBridge. Your destination will be in this status either because you manually disabled it or Stripe automatically disabled it due to an AWS misconfiguration.

Event structure

EventBridge uses its own

event structure

that wraps the Stripe

event

JSON object within a top-level

detail

field.

This example is a

customer

.

created

event payload from EventBridge:

{

"version"

:

"0"

,

"id"

:

"17e8dff5-d6cd-3770-ace9-aeac02b6ac3f"

,

"detail-type"

:

"customer.created"

,

"source"

:

"aws.partner/stripe.com/ed_61PgtRTG5aTCIz98516PLsRGLISQK0Otk6FWKjBrcDia"

,

"account"

:

"506417113029"

,

"time"

:

"2024-03-07T18:27:56Z"

,

"region"

:

"us-west-2"

,

"resources"

:

[

See all 60 lines

Support events types where Stripe waits for a response

Stripe sends most event types asynchronously; however, for certain event types, Stripe waits for a response. The presence or absence of a response from the event destination directly influences Stripe’s actions regarding these specific event types.

Amazon EventBridge destinations offer limited support for event types that require a response:

You can’t subscribe to the

issuing

_

authorization

.

request

event type for Amazon EventBridge destinations. Instead, set up a

webhook endpoint

to subscribe to this event type. Use

issuing

_

authorization

.

request

to authorize purchase requests in real-time. This requires your destination to approve or decline requests by responding to the event. EventBridge handles the response to Stripe before sending it to your consumers. As a result, this destination type can’t use this event type to authorize any payments.

You can subscribe to

checkout

_

sessions

.

completed

when using Amazon EventBridge. However, this doesn’t

handle redirect behavior

when you embed

Checkout

directly in your website or redirect customers to a Stripe-hosted payment page. Delivering a

checkout

_

sessions

.

completed

event to Amazon EventBridge won’t affect redirect behavior. To influence Checkout redirect behavior, process this event type with a

webhook endpoint

.

Common architecture patterns with EventBridge and Stripe events

Consider the following architectural patterns when you use Amazon EventBridge with Stripe:

Trigger serverless functions with

Lambda

to define business automations

: Send Stripe events from EventBridge to Lambda to trigger serverless compute functions, such as creating a shipping label after a payment succeeds.

Enable event monitoring with

CloudWatch

: Send events from EventBridge to CloudWatch Logs to store events as log data that you can interactively search and analyze. Monitor usage patterns and errors with CloudWatch. Consider setting up alerts for errors (for example, when an EventBridge rule is broken).

Trigger low and no code workflows with

Step Functions

: Send events to a StepFunction workflow that trigger your business scenarios, such as notifying your customers that their trial is about to end.

Fan out events to internal systems with

Simple Notification Service (SNS)

or

Simple Queue Service (SQS)

: Send Stripe events to SNS or SQS to fan out Stripe event data to your internal teams to make sure that they can own and process them.

See also

List of thin event types

List of snapshot event types

Event destinations overview

Send events to webhook endpoints

On this page
