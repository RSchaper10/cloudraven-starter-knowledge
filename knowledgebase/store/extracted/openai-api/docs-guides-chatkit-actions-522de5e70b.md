---
title: Actions in ChatKit | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/chatkit-actions
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:32.067640+00:00
kind: extracted-doc
---

# Actions in ChatKit | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/chatkit-actions

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:32.067640+00:00

Direct links in scope:

- https://developers.openai.com/api/docs/quickstart
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/libraries
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/guides/prompt-guidance
- https://developers.openai.com/api/docs/guides/text
- https://developers.openai.com/api/docs/guides/code-generation
- https://developers.openai.com/api/docs/guides/images-vision
- https://developers.openai.com/api/docs/guides/audio
- https://developers.openai.com/api/docs/guides/structured-outputs
- https://developers.openai.com/api/docs/guides/function-calling
- https://developers.openai.com/api/docs/guides/migrate-to-responses
- https://developers.openai.com/api/docs/guides/tools
- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents/quickstart
- https://developers.openai.com/api/docs/guides/agents/define-agents
- https://developers.openai.com/api/docs/guides/agents/models
- https://developers.openai.com/api/docs/guides/agents/running-agents
- https://developers.openai.com/api/docs/guides/agents/sandboxes

Captured summary:

- Actions in ChatKit | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions Actions are a way for the ChatKit SDK frontend to trigger a streaming response without the user submitting a message.
- They can also be used to trigger side-effects outside ChatKit SDK.
- Triggering actions In response to user interaction with widgets Actions can be triggered by attaching an ActionConfig to any widget node that supports it.
- For example, you can respond to click events on Buttons.
- When a user clicks on this button, the action will be sent to your server where you can update the widget, run inference, stream new thread items, etc.

Extracted text:

Actions in ChatKit | OpenAI API

Search the API docs

Search docs

Suggested

responses create

reasoning_effort

realtime

prompt caching

Primary navigation

Search docs

Suggested

responses create

reasoning_effort

realtime

prompt caching

Get started

Overview

Quickstart

Models

Pricing

Libraries

Latest: GPT-5.4

Prompt guidance

Core concepts

Text generation

Code generation

Images and vision

Audio and speech

Structured output

Function calling

Responses API

Using tools

Agents SDK

Overview

Quickstart

Agent definitions

Models and providers

Running agents

Sandbox agents

Orchestration

Guardrails

Results and state

Integrations and observability

Evaluate agent workflows

Voice agents

Agent Builder

Overview

Node reference

Safety in building agents

ChatKit

Overview

Customize

Widgets

Actions

Advanced integrations

Tools

Web search

MCP and Connectors

Skills

Shell

Computer use

File search and retrieval

File search

Retrieval

Tool search

More tools

Apply Patch

Local shell

Image generation

Code interpreter

Run and scale

Conversation state

Background mode

Streaming

WebSocket mode

Webhooks

File inputs

Context management

Compaction

Counting tokens

Prompt caching

Prompting

Overview

Prompt engineering

Citation formatting

Reasoning

Reasoning models

Reasoning best practices

Evaluation

Getting started

Working with evals

Prompt optimizer

External models

Best practices

Realtime API

Overview

Connect

WebRTC

WebSocket

SIP

Usage

Using realtime models

Managing conversations

MCP servers

Webhooks and server-side controls

Managing costs

Realtime transcription

Voice agents

Model optimization

Optimization cycle

Fine-tuning

Supervised fine-tuning

Vision fine-tuning

Direct preference optimization

Reinforcement fine-tuning

RFT use cases

Best practices

Graders

Specialized models

Image generation

Video generation

Text to speech

Speech to text

Deep research

Embeddings

Moderation

Going live

Production best practices

Latency optimization

Overview

Predicted Outputs

Priority processing

Cost optimization

Overview

Batch

Flex processing

Accuracy optimization

Safety

Safety best practices

Safety checks

Cybersecurity checks

Under 18 API Guidance

Legacy APIs

Assistants API

Migration guide

Deep dive

Tools

Resources

Terms and policies

Changelog

Your data

Permissions

Rate limits

Deprecations

MCP for deep research

Developer mode

ChatGPT Actions

Introduction

Getting started

Actions library

Authentication

Production

Data retrieval

Sending files

Docs

Use cases

Getting Started

Overview

Quickstart

Explore use cases

Pricing

Concepts

Prompting

Customization

Sandboxing

Subagents

Workflows

Models

Cyber Safety

Using Codex

App

Overview

Features

Settings

Review

Automations

Worktrees

Local Environments

Commands

Windows

Troubleshooting

IDE Extension

Overview

Features

Settings

IDE Commands

Slash commands

CLI

Overview

Features

Command Line Options

Slash commands

Web

Overview

Environments

Internet Access

Integrations

GitHub

Slack

Linear

Codex Security

Overview

Setup

Improving the threat model

FAQ

Configuration

Config File

Config Basics

Advanced Config

Config Reference

Sample Config

Speed

Rules

Hooks

AGENTS.md

MCP

Plugins

Overview

Build plugins

Skills

Subagents

Administration

Authentication

Agent approvals & security

Enterprise

Admin Setup

Governance

Managed configuration

Windows

Automation

Non-interactive Mode

Codex SDK

App Server

MCP Server

GitHub Action

Learn

Best practices

Videos

Community

Blog

Using skills to accelerate OSS maintenance

Building frontend UIs with Codex and Figma

View all

Cookbooks

Codex Prompting Guide

Modernizing your Codebase with Codex

View all

Building AI Teams

Releases

Changelog

Feature Maturity

Open Source

Home

Apps SDK

Commerce

Home

Quickstart

Core Concepts

MCP Apps in ChatGPT

MCP Server

UX principles

UI guidelines

Plan

Research use cases

Define tools

Design components

Build

Set up your server

Build your ChatGPT UI

Authenticate users

Manage state

Monetize your app

Examples

Deploy

Deploy your app

Connect from ChatGPT

Test your integration

Submit your app

Guides

Optimize Metadata

Security & Privacy

Troubleshooting

Resources

Changelog

App submission guidelines

Reference

Home

Guides

Get started

Best practices

File Upload

Overview

Products

API

Overview

Feeds

Products

Promotions

Showcase

Blog

Cookbook

Learn

Community

Home

All posts

Recent

How Perplexity Brought Voice Search to Millions Using the Realtime API

Designing delightful frontends with GPT-5.4

From prompts to products: One year of Responses

Using skills to accelerate OSS maintenance

Building frontend UIs with Codex and Figma

Topics

General

API

Apps SDK

Audio

Codex

Home

Topics

Agents

Evals

Multimodal

Text

Guardrails

Optimization

ChatGPT

Codex

gpt-oss

Contribute

Cookbook on GitHub

Home

Docs MCP

Categories

Demo apps

Videos

Topics

Agents

Audio & Voice

Computer use

Codex

Evals

gpt-oss

Fine-tuning

Image generation

Scaling

Tools

Video generation

Community

Programs

Codex Ambassadors

Codex for Students

Codex for Open Source

Events

Meetups

Hackathon Support

Forum

Discord

API Dashboard

Copy Page

More page actions

Copy Page

More page actions

Actions are a way for the ChatKit SDK frontend to trigger a streaming response without the user submitting a message. They can also be used to trigger side-effects outside ChatKit SDK.

Triggering actions

In response to user interaction with widgets

Actions can be triggered by attaching an

ActionConfig

to any widget node that supports it. For example, you can respond to click events on Buttons. When a user clicks on this button, the action will be sent to your server where you can update the widget, run inference, stream new thread items, etc.

1

2

3

4

5

6

7

Button(

label=

"Example"

,

onClickAction=ActionConfig(

type

=

"example"

,

payload={

"id"

:

123

},

)

)

Actions can also be sent imperatively by your frontend with

sendAction()

. This is probably most useful when you need ChatKit to respond to interaction happening outside ChatKit, but it can also be used to chain actions when you need to respond on both the client and the server (more on that below).

1

2

3

4

await chatKit.sendAction({

type:

"example"

,

payload: { id:

123

},

});

Handling actions

On the server

By default, actions are sent to your server. You can handle actions on your server by implementing the

action

method on

ChatKitServer

.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

class

MyChatKitServer

(

ChatKitServer[RequestContext]

)

async

def

action

(

self,

thread: ThreadMetadata,

action: Action[

str

,

Any

],

sender: WidgetItem |

None

,

context: RequestContext,

) -> AsyncIterator[Event]:

if

action.

type

==

"example"

:

await

do_thing(action.payload[

'id'

])

# often you'll want to add a HiddenContextItem so the model

# can see that the user did something

await

self.store.add_thread_item(

thread.

id

,

HiddenContextItem(

id

=

"item_123"

,

created_at=datetime.now(),

content=(

"<USER_ACTION>The user did a thing</USER_ACTION>"

),

),

context,

)

# then you might want to run inference to stream a response

# back to the user.

async

for

e

in

self.generate(context, thread):

yield

e

NOTE:

As with any client/server interaction, actions and their payloads are sent by the client and should be treated as untrusted data.

Client

Sometimes you’ll want to handle actions in your client integration. To do that you need to specify that the action should be sent to your client-side action handler by adding

handler="client

to the

ActionConfig

.

1

2

3

4

5

6

7

8

Button(

label=

"Example"

,

onClickAction=ActionConfig(

type

=

"example"

,

payload={

"id"

:

123

},

handler=

"client"

)

)

Then, when the action is triggered, it will then be passed to a callback that you provide when instantiating ChatKit.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

async

function

handle

WidgetAction(

action

: {

type

:

string

, Record<

string

,

unknown

>})

{

if

(action.

type

===

"example"

) {

const res = await

do

Something(

action

)

// You can fire off actions to your server from here as well.

// e.g. if you want to stream new thread items or update a widget.

await chatKit.send

Action({

type

:

"example_complete"

,

payload

:

res

})

}

}

chatKit.set

Options({

/

/

other

options

...

widgets

: {

onAction

:

handleWidgetAction

}

})

Strongly typed actions

By default

Action

and

ActionConfig

are not strongly typed. However, we do expose a

create

helper on

Action

making it easy to generate

ActionConfig

s from a set of strongly-typed actions.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

class

ExamplePayload

(

BaseModel

)

id

:

int

ExampleAction = Action[

Literal

[

"example"

], ExamplePayload]

OtherAction = Action[

Literal

[

"other"

],

None

]

AppAction = Annotated[

ExampleAction

| OtherAction,

Field(discriminator=

"type"

),

]

ActionAdapter: TypeAdapter[AppAction] = TypeAdapter(AppAction)

def

parse_app_action

(

action: Action[

str

,

Any

]

):

AppAction

return

ActionAdapter.model_validate(action)

# Usage in a widget

# Action provides a create helper which makes it easy to generate

# ActionConfigs from strongly typed actions.

Button(

label=

"Example"

,

onClickAction=ExampleAction.create(ExamplePayload(

id

=

123

))

)

# usage in action handler

class

MyChatKitServer

(

ChatKitServer[RequestContext]

)

async

def

action

(

self,

thread: ThreadMetadata,

action: Action[

str

,

Any

],

sender: WidgetItem |

None

,

context: RequestContext,

) -> AsyncIterator[Event]:

# add custom error handling if needed

app_action = parse_app_action(action)

if

(app_action.

type

==

"example"

):

await

do_thing(app_action.payload.

id

)

Use widgets and actions to create custom forms

When widget nodes that take user input are mounted inside a

Form

, the values from those fields will be included in the

payload

of all actions that originate from within the

Form

.

Form values are keyed in the

payload

by their

name

e.g.

Select(name="title")

→

action.payload.title

Select(name="todo.title")

→

action.payload.todo.title

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

Form(

direction=

"col"

,

validation=

"native"

onSubmitAction=ActionConfig(

type

=

"update_todo"

,

payload={

"id"

: todo.

id

}

),

children=[

Title(value=

"Edit Todo"

),

Text(value=

"Title"

, color=

"secondary"

, size=

"sm"

),

Text(

value=todo.title,

editable=EditableProps(name=

"title"

, required=

True

),

)

Text(value=

"Description"

, color=

"secondary"

, size=

"sm"

),

Text(

value=todo.description,

editable=EditableProps(name=

"description"

),

),

Button(label=

"Save"

,

type

=

"submit"

)

]

)

class

MyChatKitServer

(

ChatKitServer[RequestContext]

)

async

def

action

(

self,

thread: ThreadMetadata,

action: Action[

str

,

Any

],

sender: WidgetItem |

None

,

context: RequestContext,

) -> AsyncIterator[Event]:

if

(action.

type

==

"update_todo"

):

id

= action.payload[

'id'

]

# Any action that originates from within the Form will

# include title and description

title = action.payload[

'title'

]

description = action.payload[

'description'

]

# ...

Validation

Form

uses basic native form validation; enforcing

required

and

pattern

on fields where they are configured and blocking submission when the form has any invalid field.

We may add new validation modes with better UX, more expressive validation, custom error display, etc in the future. Until then, widgets are not a great medium for complex forms with tricky validation. If you have this need, a better pattern would be to use client side action handling to trigger a modal, show a custom form there, then pass the result back into ChatKit with

sendAction

.

Treating

Card

as a

Form

You can pass

asForm=True

to

Card

and it will behave as a

Form

, running validation and passing collected fields to the Card’s

confirm

action.

Payload key collisions

If there is a naming collision with some other existing pre-defined key on your payload, the form value will be ignored. This is probably a bug, so we’ll emit an

error

event when we see this.

Control loading state interactions in widgets

Use

ActionConfig.loadingBehavior

to control how actions trigger different loading states in a widget.

1

2

3

4

5

6

7

Button(

label=

"This make take a while..."

,

onClickAction=ActionConfig(

type

=

"long_running_action_that_should_block_other_ui_interactions"

,

loadingBehavior=

"container"

)

)

Value

Behavior

auto

The action will adapt to how it’s being used. (

default

)

self

The action triggers loading state on the widget node that the action was bound to.

container

The action triggers loading state on the entire widget container. This causes the widget to fade out slightly and become inert.

none

No loading state

Using

auto

behavior

Generally, we recommend using

auto

, which is the default.

auto

triggers loading states based on where the action is bound, for example:

Button.onClickAction

→

self

Select.onChangeAction

→

none

Card.confirm.action

→

container
