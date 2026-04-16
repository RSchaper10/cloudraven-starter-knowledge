---
title: Conversation state | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/conversation-state
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:40.874442+00:00
kind: extracted-doc
---

# Conversation state | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/conversation-state

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:40.874442+00:00

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

- Conversation state | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Responses Copy Page More page actions Responses Copy Page More page actions OpenAI provides a few ways to manage conversation state, which is important for preserving information across multiple messages or turns in a conversation.
- When troubleshooting cases where GPT-5.4 treats an intermediate update as the final answer, verify your integration preserves the assistant message phase field correctly.
- Manually manage conversation state While each text generation request is independent and stateless, you can still implement multi-turn conversations by providing additional messages as parameters to your text generation request.
- Consider a knock-knock joke: Manually construct a past conversation python 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 import OpenAI from "openai" ; const openai = new OpenAI(); const response = await openai.chat.completions.create({ model : "gpt-4o-mini" , messages : [ { role : "user" , content : "knock knock." , }, { role : "assistant" , content : "Who's there?" , }, { role : "user" , content : "Orange." , }, ], }); console .log(response.choices[ 0 ].message.content); 1 2 3 4 5 6 7 8 9 10 11 12 13 14 from openai import OpenAI client = OpenAI() response = client.chat.completions.create( model= "gpt-4o-mini" , messages=[ { "role" : "user" , "content" : "knock knock." }, { "role" : "assistant" , "content" : "Who's there?" }, { "role" : "user" , "content" : "Orange." }, ], ) print (response.choices[ 0 ].message.content) Manually construct a past conversation python 1 2 3 4 5 6 7 8 9 10 11 12 13 14 import OpenAI from "openai" ; const openai = new OpenAI(); const response = await openai.responses.create({ model : "gpt-4o-mini" , input : [ { role : "user" , content : "knock knock." }, { role : "assistant" , content : "Who's there?" }, { role : "user" , content : "Orange." }, ], }); console .log(response.output_text); 1 2 3 4 5 6 7 8 9 10 11 12 13 14 from openai import OpenAI client = OpenAI() response = client.responses.create( model= "gpt-4o-mini" , input =[ { "role" : "user" , "content" : "knock knock." }, { "role" : "assistant" , "content" : "Who's there?" }, { "role" : "user" , "content" : "Orange." }, ], ) print (response.output_text) By using alternating user and assistant messages, you capture the previous state of a conversation in one request to the model.
- To manually share context across generated responses, include the model’s previous response output as input, and append that input to your next request.

Extracted text:

Conversation state | OpenAI API

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

Responses

Copy Page

More page actions

Responses

Copy Page

More page actions

OpenAI provides a few ways to manage conversation state, which is important for preserving information across multiple messages or turns in a conversation.

When troubleshooting cases where GPT-5.4 treats an intermediate update as the final answer, verify your integration preserves the assistant message

phase

field correctly. See

Phase parameter

for details.

Manually manage conversation state

While each text generation request is independent and stateless, you can still implement

multi-turn conversations

by providing additional messages as parameters to your text generation request. Consider a knock-knock joke:

Manually construct a past conversation

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

const

response =

await

openai.chat.completions.create({

model

:

"gpt-4o-mini"

,

messages

: [

{

role

:

"user"

,

content

:

"knock knock."

,

},

{

role

:

"assistant"

,

content

:

"Who's there?"

,

},

{

role

:

"user"

,

content

:

"Orange."

,

},

],

});

console

.log(response.choices[

0

].message.content);

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

from

openai

import

OpenAI

client = OpenAI()

response = client.chat.completions.create(

model=

"gpt-4o-mini"

,

messages=[

{

"role"

:

"user"

,

"content"

:

"knock knock."

},

{

"role"

:

"assistant"

,

"content"

:

"Who's there?"

},

{

"role"

:

"user"

,

"content"

:

"Orange."

},

],

)

print

(response.choices[

0

].message.content)

Manually construct a past conversation

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

const

response =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

input

: [

{

role

:

"user"

,

content

:

"knock knock."

},

{

role

:

"assistant"

,

content

:

"Who's there?"

},

{

role

:

"user"

,

content

:

"Orange."

},

],

});

console

.log(response.output_text);

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

from

openai

import

OpenAI

client = OpenAI()

response = client.responses.create(

model=

"gpt-4o-mini"

,

input

=[

{

"role"

:

"user"

,

"content"

:

"knock knock."

},

{

"role"

:

"assistant"

,

"content"

:

"Who's there?"

},

{

"role"

:

"user"

,

"content"

:

"Orange."

},

],

)

print

(response.output_text)

By using alternating

user

and

assistant

messages, you capture the previous state of a conversation in one request to the model.

To manually share context across generated responses, include the model’s previous response output as input, and append that input to your next request.

In the following example, we ask the model to tell a joke, followed by a request for another joke. Appending previous responses to new requests in this way helps ensure conversations feel natural and retain the context of previous interactions.

Manually manage conversation state with the Chat Completions API.

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

let

history = [

{

role

:

"user"

,

content

:

"tell me a joke"

,

},

];

const

completion =

await

openai.chat.completions.create({

model

:

"gpt-4o-mini"

,

messages

: history,

});

console

.log(completion.choices[

0

].message.content);

history.push(completion.choices[

0

].message);

history.push({

role

:

"user"

,

content

:

"tell me another"

,

});

const

secondCompletion =

await

openai.chat.completions.create({

model

:

"gpt-4o-mini"

,

messages

: history,

});

console

.log(secondCompletion.choices[

0

].message.content);

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

from

openai

import

OpenAI

client = OpenAI()

history = [

{

"role"

:

"user"

,

"content"

:

"tell me a joke"

}

]

response = client.chat.completions.create(

model=

"gpt-4o-mini"

,

messages=history,

)

print

(response.choices[

0

].message.content)

history.append(response.choices[

0

].message)

history.append({

"role"

:

"user"

,

"content"

:

"tell me another"

})

second_response = client.chat.completions.create(

model=

"gpt-4o-mini"

,

messages=history,

)

print

(second_response.choices[

0

].message.content)

Manually manage conversation state with the Responses API.

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

let

history = [

{

role

:

"user"

,

content

:

"tell me a joke"

,

},

];

const

response =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

input

: history,

store

:

true

,

});

console

.log(response.output_text);

// Add the response to the history

history = [

...history,

...response.output.map(

(

el

) =>

{

//

TODO:

Remove this step

delete

el.id;

return

el;

}),

];

history.push({

role

:

"user"

,

content

:

"tell me another"

,

});

const

secondResponse =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

input

: history,

store

:

true

,

});

console

.log(secondResponse.output_text);

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

from

openai

import

OpenAI

client = OpenAI()

history = [

{

"role"

:

"user"

,

"content"

:

"tell me a joke"

}

]

response = client.responses.create(

model=

"gpt-4o-mini"

,

input

=history,

store=

False

)

print

(response.output_text)

# Add the response to the conversation

history += [{

"role"

: el.role,

"content"

: el.content}

for

el

in

response.output]

history.append({

"role"

:

"user"

,

"content"

:

"tell me another"

})

second_response = client.responses.create(

model=

"gpt-4o-mini"

,

input

=history,

store=

False

)

print

(second_response.output_text)

OpenAI APIs for conversation state

Our APIs make it easier to manage conversation state automatically, so you don’t have to do pass inputs manually with each turn of a conversation.

We recommend using the

Responses API

instead. Because it’s stateful, managing context across conversations is a simple parameter.

If you’re using the Chat Completions endpoint, you’ll need to either manually manage state, as documented above.

Using the Conversations API

The

Conversations API

works with the

Responses API

to persist conversation state as a long-running object with its own durable identifier. After creating a conversation object, you can keep using it across sessions, devices, or jobs.

Conversations store items, which can be messages, tool calls, tool outputs, and other data.

Create a conversation

python

1

conversation = openai.conversations.create()

In a multi-turn interaction, you can pass the

conversation

into subsequent responses to persist state and share context across subsequent responses, rather than having to chain multiple response items together.

Manage conversation state with Conversations and Responses APIs

python

1

2

3

4

5

response = openai.responses.create(

model=

"gpt-4.1"

,

input

=[{

"role"

:

"user"

,

"content"

:

"What are the 5 Ds of dodgeball?"

}],

conversation=

"conv_689667905b048191b4740501625afd940c7533ace33a2dab"

)

Passing context from the previous response

Another way to manage conversation state is to share context across generated responses with the

previous_response_id

parameter. This parameter lets you chain responses and create a threaded conversation.

Chain responses across turns by passing the previous response ID

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

const

response =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

input

:

"tell me a joke"

,

store

:

true

,

});

console

.log(response.output_text);

const

secondResponse =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

previous_response_id

: response.id,

input

: [{

"role"

:

"user"

,

"content"

:

"explain why this is funny."

}],

store

:

true

,

});

console

.log(secondResponse.output_text);

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

from

openai

import

OpenAI

client = OpenAI()

response = client.responses.create(

model=

"gpt-4o-mini"

,

input

=

"tell me a joke"

,

)

print

(response.output_text)

second_response = client.responses.create(

model=

"gpt-4o-mini"

,

previous_response_id=response.

id

,

input

=[{

"role"

:

"user"

,

"content"

:

"explain why this is funny."

}],

)

print

(second_response.output_text)

In the following example, we ask the model to tell a joke. Separately, we ask the model to explain why it’s funny, and the model has all necessary context to deliver a good response.

Manually manage conversation state with the Responses API

python

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

import

OpenAI

from

"openai"

;

const

openai =

new

OpenAI();

const

response =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

input

:

"tell me a joke"

,

store

:

true

,

});

console

.log(response.output_text);

const

secondResponse =

await

openai.responses.create({

model

:

"gpt-4o-mini"

,

previous_response_id

: response.id,

input

: [{

"role"

:

"user"

,

"content"

:

"explain why this is funny."

}],

store

:

true

,

});

console

.log(secondResponse.output_text);

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

from

openai

import

OpenAI

client = OpenAI()

response = client.responses.create(

model=

"gpt-4o-mini"

,

input

=

"tell me a joke"

,

)

print

(response.output_text)

second_response = client.responses.create(

model=

"gpt-4o-mini"

,

previous_response_id=response.

id

,

input

=[{

"role"

:

"user"

,

"content"

:

"explain why this is funny."

}],

)

print

(second_response.output_text)

previous_response_id

in WebSocket mode

If you are using

the Responses API WebSocket mode

, continuation uses the same

previous_response_id

semantics as HTTP mode, but over a persistent socket with repeated

response.create

events.

The connection-local cache currently keeps the most recent previous response in memory for low-latency continuation. If an uncached ID cannot be resolved, send a new turn with

previous_response_id

set to

null

and pass full input context.

Data retention for model responses

Response objects are saved for 30 days by default. They can be viewed in the dashboard

logs

page or

retrieved

via the API. You can disable this behavior by setting

store

to

false

when creating a Response.

Conversation objects and items in them are not subject to the 30 day TTL. Any response attached to a conversation will have its items persisted with no 30 day TTL.

OpenAI does not use data sent via API to train our models without your explicit consent—

learn more

.

Even when using

previous_response_id

, all previous input tokens for responses in the chain are billed as input tokens in the API.

Managing the context window

Understanding context windows will help you successfully create threaded conversations and manage state across model interactions.

The

context window

is the maximum number of tokens that can be used in a single request. This max tokens number includes input, output, and reasoning tokens. To learn your model’s context window, see

model details

.

Managing context for text generation

As your inputs become more complex, or you include more turns in a conversation, you’ll need to consider both

output token

and

context window

limits. Model inputs and outputs are metered in

tokens

, which are parsed from inputs to analyze their content and intent and assembled to render logical outputs. Models have limits on token usage during the lifecycle of a text generation request.

Output tokens

are the tokens generated by a model in response to a prompt. Each model has different

limits for output tokens

. For example,

gpt-4o-2024-08-06

can generate a maximum of 16,384 output tokens.

A

context window

describes the total tokens that can be used for both input and output tokens (and for some models,

reasoning tokens

). Compare the

context window limits

of our models. For example,

gpt-4o-2024-08-06

has a total context window of 128k tokens.

If you create a very large prompt—often by including extra context, data, or examples for the model—you run the risk of exceeding the allocated context window for a model, which might result in truncated outputs.

Use the

tokenizer tool

, built with the

tiktoken library

, to see how many tokens are in a particular string of text.

For example, when making an API request to

Chat Completions

with the

o1 model

, the following token counts will apply toward the context window total:

Input tokens (inputs you include in the

messages

array with

Chat Completions

)

Output tokens (tokens generated in response to your prompt)

Reasoning tokens (used by the model to plan a response)

For example, when making an API request to the

Responses API

with a reasoning enabled model, like the

o1 model

, the following token counts will apply toward the context window total:

Input tokens (inputs you include in the

input

array for the

Responses API

)

Output tokens (tokens generated in response to your prompt)

Reasoning tokens (used by the model to plan a response)

Tokens generated in excess of the context window limit may be truncated in API responses.

You can estimate the number of tokens your messages will use with the

tokenizer tool

.

Compaction

Detailed compaction guidance now lives in

Compaction

.

For

/responses

with

context_management

and

compact_threshold

, see

Server-side compaction

.

For explicit compaction control, see

Standalone compact endpoint

and the

/responses/compact

API reference

.

Next steps

For more specific examples and use cases, visit the

OpenAI Cookbook

, or learn more about using the APIs to extend model capabilities:

Receive JSON responses with Structured Outputs

Extend the models with function calling

Enable streaming for real-time responses

Build a computer using agent
