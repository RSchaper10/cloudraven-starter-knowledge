---
title: Image generation | OpenAI API
source_url: https://developers.openai.com/api/docs/guides/tools-image-generation
target_id: openai-api
dependency: OpenAI API
collected_at: 2026-04-16T03:20:39.802806+00:00
kind: extracted-doc
---

# Image generation | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/tools-image-generation

Dependency:

- OpenAI API

Collected at:

- 2026-04-16T03:20:39.802806+00:00

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

- Image generation | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Copy Page More page actions Copy Page More page actions The image generation tool allows you to generate images using a text prompt, and optionally image inputs.
- It leverages GPT Image models ( gpt-image-1 , gpt-image-1-mini , and gpt-image-1.5 ), and automatically optimizes text inputs for improved performance.
- To learn more about image generation, refer to our dedicated image generation guide .
- Usage When you include the image_generation tool in your request, the model can decide when and how to generate images as part of the conversation, using your prompt and any provided image inputs.
- The image_generation_call tool call result will include a base64-encoded image.

Extracted text:

Image generation | OpenAI API

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

The image generation tool allows you to generate images using a text prompt, and optionally image inputs. It leverages GPT Image models (

gpt-image-1

,

gpt-image-1-mini

, and

gpt-image-1.5

), and automatically optimizes text inputs for improved performance.

To learn more about image generation, refer to our dedicated

image generation guide

.

Usage

When you include the

image_generation

tool in your request, the model can decide when and how to generate images as part of the conversation, using your prompt and any provided image inputs.

The

image_generation_call

tool call result will include a base64-encoded image.

Generate an image

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

"gpt-5"

,

input

:

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools

: [{

type

:

"image_generation"

}],

});

// Save the image to a file

const

imageData = response.output

.filter(

(

output

) =>

output.type ===

"image_generation_call"

)

.map(

(

output

) =>

output.result);

if

(imageData.length >

0

) {

const

imageBase64 = imageData[

0

];

const

fs =

await

import

(

"fs"

);

fs.writeFileSync(

"otter.png"

, Buffer.from(imageBase64,

"base64"

));

}

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

from

openai

import

OpenAI

import

base64

client = OpenAI()

response = client.responses.create(

model=

"gpt-5"

,

input

=

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools=[{

"type"

:

"image_generation"

}],

)

# Save the image to a file

image_data = [

output.result

for

output

in

response.output

if

output.

type

==

"image_generation_call"

]

if

image_data:

image_base64 = image_data[

0

]

with

open

(

"otter.png"

,

"wb"

)

as

f:

f.write(base64.b64decode(image_base64))

You can

provide input images

using file IDs or base64 data.

To force the image generation tool call, you can set the parameter

tool_choice

to

{"type": "image_generation"}

.

Tool options

You can configure the following output options as parameters for the

image generation tool

:

Size: Image dimensions (e.g., 1024x1024, 1024x1536)

Quality: Rendering quality (e.g. low, medium, high)

Format: File output format

Compression: Compression level (0-100%) for JPEG and WebP formats

Background: Transparent or opaque

Action: Whether the request should automatically choose, generate, or edit an image

size

,

quality

, and

background

support the

auto

option, where the model will automatically select the best option based on the prompt.

For more details on available options, refer to the

image generation guide

.

For

gpt-image-1.5

and

chatgpt-image-latest

when used with the Responses API, you can optionally set the

action

parameter (

auto

,

generate

, or

edit

) to control whether the request performs image generation or editing. We recommend leaving it at

auto

so the model chooses whether to generate a new image or edit one already in context, but if your use case requires always editing or always creating images, you can force the behavior by setting

action

. If not specified, the default is

auto

.

Revised prompt

When using the image generation tool, the mainline model (e.g.

gpt-4.1

) will automatically revise your prompt for improved performance.

You can access the revised prompt in the

revised_prompt

field of the image generation call:

1

2

3

4

5

6

7

{

"id"

:

"ig_123"

,

"type"

:

"image_generation_call"

,

"status"

:

"completed"

,

"revised_prompt"

:

"A gray tabby cat hugging an otter. The otter is wearing an orange scarf. Both animals are cute and friendly, depicted in a warm, heartwarming style."

,

"result"

:

"..."

}

Prompting tips

Image generation works best when you use terms like “draw” or “edit” in your prompt.

For example, if you want to combine images, instead of saying “combine” or “merge”, you can say something like “edit the first image by adding this element from the second image”.

Multi-turn editing

You can iteratively edit images by referencing previous response or image IDs. This allows you to refine images across multiple turns in a conversation.

Using previous response ID

Using image ID

Using previous response ID

Multi-turn image generation

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

const

response =

await

openai.responses.create({

model

:

"gpt-5"

,

input

:

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools

: [{

type

:

"image_generation"

}],

});

const

imageData = response.output

.filter(

(

output

) =>

output.type ===

"image_generation_call"

)

.map(

(

output

) =>

output.result);

if

(imageData.length >

0

) {

const

imageBase64 = imageData[

0

];

const

fs =

await

import

(

"fs"

);

fs.writeFileSync(

"cat_and_otter.png"

, Buffer.from(imageBase64,

"base64"

));

}

// Follow up

const

response_fwup =

await

openai.responses.create({

model

:

"gpt-5"

,

previous_response_id

: response.id,

input

:

"Now make it look realistic"

,

tools

: [{

type

:

"image_generation"

}],

});

const

imageData_fwup = response_fwup.output

.filter(

(

output

) =>

output.type ===

"image_generation_call"

)

.map(

(

output

) =>

output.result);

if

(imageData_fwup.length >

0

) {

const

imageBase64 = imageData_fwup[

0

];

const

fs =

await

import

(

"fs"

);

fs.writeFileSync(

"cat_and_otter_realistic.png"

,

Buffer.from(imageBase64,

"base64"

)

);

}

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

43

from

openai

import

OpenAI

import

base64

client = OpenAI()

response = client.responses.create(

model=

"gpt-5"

,

input

=

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools=[{

"type"

:

"image_generation"

}],

)

image_data = [

output.result

for

output

in

response.output

if

output.

type

==

"image_generation_call"

]

if

image_data:

image_base64 = image_data[

0

]

with

open

(

"cat_and_otter.png"

,

"wb"

)

as

f:

f.write(base64.b64decode(image_base64))

# Follow up

response_fwup = client.responses.create(

model=

"gpt-5"

,

previous_response_id=response.

id

,

input

=

"Now make it look realistic"

,

tools=[{

"type"

:

"image_generation"

}],

)

image_data_fwup = [

output.result

for

output

in

response_fwup.output

if

output.

type

==

"image_generation_call"

]

if

image_data_fwup:

image_base64 = image_data_fwup[

0

]

with

open

(

"cat_and_otter_realistic.png"

,

"wb"

)

as

f:

f.write(base64.b64decode(image_base64))

Using image ID

Multi-turn image generation

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

42

43

44

45

46

47

48

49

50

51

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

"gpt-5"

,

input

:

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools

: [{

type

:

"image_generation"

}],

});

const

imageGenerationCalls = response.output.filter(

(

output

) =>

output.type ===

"image_generation_call"

);

const

imageData = imageGenerationCalls.map(

(

output

) =>

output.result);

if

(imageData.length >

0

) {

const

imageBase64 = imageData[

0

];

const

fs =

await

import

(

"fs"

);

fs.writeFileSync(

"cat_and_otter.png"

, Buffer.from(imageBase64,

"base64"

));

}

// Follow up

const

response_fwup =

await

openai.responses.create({

model

:

"gpt-5"

,

input

: [

{

role

:

"user"

,

content

: [{

type

:

"input_text"

,

text

:

"Now make it look realistic"

}],

},

{

type

:

"image_generation_call"

,

id

: imageGenerationCalls[

0

].id,

},

],

tools

: [{

type

:

"image_generation"

}],

});

const

imageData_fwup = response_fwup.output

.filter(

(

output

) =>

output.type ===

"image_generation_call"

)

.map(

(

output

) =>

output.result);

if

(imageData_fwup.length >

0

) {

const

imageBase64 = imageData_fwup[

0

];

const

fs =

await

import

(

"fs"

);

fs.writeFileSync(

"cat_and_otter_realistic.png"

,

Buffer.from(imageBase64,

"base64"

)

);

}

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

43

44

45

46

47

48

49

50

51

import

openai

import

base64

response = openai.responses.create(

model=

"gpt-5"

,

input

=

"Generate an image of gray tabby cat hugging an otter with an orange scarf"

,

tools=[{

"type"

:

"image_generation"

}],

)

image_generation_calls = [

output

for

output

in

response.output

if

output.

type

==

"image_generation_call"

]

image_data = [output.result

for

output

in

image_generation_calls]

if

image_data:

image_base64 = image_data[

0

]

with

open

(

"cat_and_otter.png"

,

"wb"

)

as

f:

f.write(base64.b64decode(image_base64))

# Follow up

response_fwup = openai.responses.create(

model=

"gpt-5"

,

input

=[

{

"role"

:

"user"

,

"content"

: [{

"type"

:

"input_text"

,

"text"

:

"Now make it look realistic"

}],

},

{

"type"

:

"image_generation_call"

,

"id"

: image_generation_calls[

0

].

id

,

},

],

tools=[{

"type"

:

"image_generation"

}],

)

image_data_fwup = [

output.result

for

output

in

response_fwup.output

if

output.

type

==

"image_generation_call"

]

if

image_data_fwup:

image_base64 = image_data_fwup[

0

]

with

open

(

"cat_and_otter_realistic.png"

,

"wb"

)

as

f:

f.write(base64.b64decode(image_base64))

Streaming

The image generation tool supports streaming partial images as the final result is being generated. This provides faster visual feedback for users and improves perceived latency.

You can set the number of partial images (1-3) with the

partial_images

parameter.

Stream an image

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

import

fs

from

"fs"

;

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

prompt =

"Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape"

;

const

stream =

await

openai.images.generate({

prompt

: prompt,

model

:

"gpt-image-1.5"

,

stream

:

true

,

partial_images

:

2

,

});

for

await

(

const

event

of

stream) {

if

(event.type ===

"image_generation.partial_image"

) {

const

idx = event.partial_image_index;

const

imageBase64 = event.b64_json;

const

imageBuffer = Buffer.from(imageBase64,

"base64"

);

fs.writeFileSync(

`river

${idx}

.png`

, imageBuffer);

}

}

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

from

openai

import

OpenAI

import

base64

client = OpenAI()

stream = client.images.generate(

prompt=

"Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape"

,

model=

"gpt-image-1.5"

,

stream=

True

,

partial_images=

2

,

)

for

event

in

stream:

if

event.

type

==

"image_generation.partial_image"

:

idx = event.partial_image_index

image_base64 = event.b64_json

image_bytes = base64.b64decode(image_base64)

with

open

(

f"river

{idx}

.png"

,

"wb"

)

as

f:

f.write(image_bytes)

Supported models

The image generation tool is supported for the following models:

gpt-4o

gpt-4o-mini

gpt-4.1

gpt-4.1-mini

gpt-4.1-nano

o3

gpt-5

gpt-5.4-mini

gpt-5.4-nano

gpt-5-nano

gpt-5.4

gpt-5.2

The model used for the image generation process is always a GPT Image model (

gpt-image-1.5

,

gpt-image-1

, or

gpt-image-1-mini

), but these models are not valid values for the

model

field in the Responses API. Use a text-capable mainline model (for example,

gpt-4.1

or

gpt-5

) with the hosted

image_generation

tool.
