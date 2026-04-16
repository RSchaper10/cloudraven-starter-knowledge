# Using tools | OpenAI API

Source URL:

- https://developers.openai.com/api/docs/guides/tools

Dependency:

- OpenAI API

Collected at:

- 2026-04-15T19:44:22.886715+00:00

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

- Using tools | OpenAI API Search the API docs Search docs Suggested responses create reasoning_effort realtime prompt caching Primary navigation Search docs Suggested responses create reasoning_effort realtime prompt caching Get started Overview Quickstart Models Pricing Libraries Latest: GPT-5.4 Prompt guidance Core concepts Text generation Code generation Images and vision Audio and speech Structured output Function calling Responses API Using tools Agents SDK Overview Quickstart Agent definitions Models and providers Running agents Sandbox agents Orchestration Guardrails Results and state Integrations and observability Evaluate agent workflows Voice agents Agent Builder Overview Node reference Safety in building agents ChatKit Overview Customize Widgets Actions Advanced integrations Tools Web search MCP and Connectors Skills Shell Computer use File search and retrieval File search Retrieval Tool search More tools Apply Patch Local shell Image generation Code interpreter Run and scale Conversation state Background mode Streaming WebSocket mode Webhooks File inputs Context management Compaction Counting tokens Prompt caching Prompting Overview Prompt engineering Citation formatting Reasoning Reasoning models Reasoning best practices Evaluation Getting started Working with evals Prompt optimizer External models Best practices Realtime API Overview Connect WebRTC WebSocket SIP Usage Using realtime models Managing conversations MCP servers Webhooks and server-side controls Managing costs Realtime transcription Voice agents Model optimization Optimization cycle Fine-tuning Supervised fine-tuning Vision fine-tuning Direct preference optimization Reinforcement fine-tuning RFT use cases Best practices Graders Specialized models Image generation Video generation Text to speech Speech to text Deep research Embeddings Moderation Going live Production best practices Latency optimization Overview Predicted Outputs Priority processing Cost optimization Overview Batch Flex processing Accuracy optimization Safety Safety best practices Safety checks Cybersecurity checks Under 18 API Guidance Legacy APIs Assistants API Migration guide Deep dive Tools Resources Terms and policies Changelog Your data Permissions Rate limits Deprecations MCP for deep research Developer mode ChatGPT Actions Introduction Getting started Actions library Authentication Production Data retrieval Sending files Docs Use cases Getting Started Overview Quickstart Explore use cases Pricing Concepts Prompting Customization Sandboxing Subagents Workflows Models Cyber Safety Using Codex App Overview Features Settings Review Automations Worktrees Local Environments Commands Windows Troubleshooting IDE Extension Overview Features Settings IDE Commands Slash commands CLI Overview Features Command Line Options Slash commands Web Overview Environments Internet Access Integrations GitHub Slack Linear Codex Security Overview Setup Improving the threat model FAQ Configuration Config File Config Basics Advanced Config Config Reference Sample Config Speed Rules Hooks AGENTS.md MCP Plugins Overview Build plugins Skills Subagents Administration Authentication Agent approvals & security Enterprise Admin Setup Governance Managed configuration Windows Automation Non-interactive Mode Codex SDK App Server MCP Server GitHub Action Learn Best practices Videos Community Blog Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma View all Cookbooks Codex Prompting Guide Modernizing your Codebase with Codex View all Building AI Teams Releases Changelog Feature Maturity Open Source Home Apps SDK Commerce Home Quickstart Core Concepts MCP Apps in ChatGPT MCP Server UX principles UI guidelines Plan Research use cases Define tools Design components Build Set up your server Build your ChatGPT UI Authenticate users Manage state Monetize your app Examples Deploy Deploy your app Connect from ChatGPT Test your integration Submit your app Guides Optimize Metadata Security & Privacy Troubleshooting Resources Changelog App submission guidelines Reference Home Guides Get started Best practices File Upload Overview Products API Overview Feeds Products Promotions Showcase Blog Cookbook Learn Community Home All posts Recent How Perplexity Brought Voice Search to Millions Using the Realtime API Designing delightful frontends with GPT-5.4 From prompts to products: One year of Responses Using skills to accelerate OSS maintenance Building frontend UIs with Codex and Figma Topics General API Apps SDK Audio Codex Home Topics Agents Evals Multimodal Text Guardrails Optimization ChatGPT Codex gpt-oss Contribute Cookbook on GitHub Home Docs MCP Categories Demo apps Videos Topics Agents Audio & Voice Computer use Codex Evals gpt-oss Fine-tuning Image generation Scaling Tools Video generation Community Programs Codex Ambassadors Codex for Students Codex for Open Source Events Meetups Hackathon Support Forum Discord API Dashboard Starter app Experiment with built-in tools in the Responses API.
- Copy Page More page actions Copy Page More page actions When generating model responses or building agents, you can extend capabilities using built‑in tools, function calling, tool search, and remote MCP servers.
- These enable the model to search the web, retrieve from your files, load deferred tool definitions at runtime, call your own functions, or access third‑party services.
- Only gpt-5.4 and later models support tool_search .
- Web search File search Tool search Function calling Remote MCP Web search Include web search results for the model response javascript 1 2 3 4 5 6 7 8 9 10 11 12 import OpenAI from "openai" ; const client = new OpenAI(); const response = await client.responses.create({ model : "gpt-5" , tools : [ { type : "web_search" }, ], input : "What was a positive news story from today?" , }); console .log(response.output_text); 1 2 3 4 5 6 7 8 9 10 from openai import OpenAI client = OpenAI() response = client.responses.create( model= "gpt-5" , tools=[{ "type" : "web_search" }], input = "What was a positive news story from today?" ) print (response.output_text) 1 2 3 4 5 6 7 8 curl "https://api.openai.com/v1/responses" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $OPENAI_API_KEY " \ -d '{ "model": "gpt-5", "tools": [{"type": "web_search"}], "input": "what was a positive news story from today?" }' 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 using OpenAI.Responses; string key = Environment.GetEnvironmentVariable( "OPENAI_API_KEY" )!; OpenAIResponseClient client = new (model: "gpt-5" , apiKey: key); ResponseCreationOptions options = new (); options.Tools.Add(ResponseTool.CreateWebSearchTool()); OpenAIResponse response = (OpenAIResponse)client.CreateResponse([ ResponseItem.CreateUserMessageItem([ ResponseContentPart.CreateInputTextPart( "What was a positive news story from today?" ), ]), ], options); Console.WriteLine(response.GetOutputText()); File search Search your files in a response javascript 1 2 3 4 5 6 7 8 9 10 11 12 from openai import OpenAI client = OpenAI() response = client.responses.create( model= "gpt-4.1" , input = "What is deep research by OpenAI?" , tools=[{ "type" : "file_search" , "vector_store_ids" : [ "<vector_store_id>" ] }] ) print (response) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 import OpenAI from "openai" ; const openai = new OpenAI(); const response = await openai.responses.create({ model : "gpt-4.1" , input : "What is deep research by OpenAI?" , tools : [ { type : "file_search" , vector_store_ids : [ "<vector_store_id>" ], }, ], }); console .log(response); 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 using OpenAI.Responses; string key = Environment.GetEnvironmentVariable( "OPENAI_API_KEY" )!; OpenAIResponseClient client = new (model: "gpt-5" , apiKey: key); ResponseCreationOptions options = new (); options.Tools.Add(ResponseTool.CreateFileSearchTool([ "<vector_store_id>" ])); OpenAIResponse response = (OpenAIResponse)client.CreateResponse([ ResponseItem.CreateUserMessageItem([ ResponseContentPart.CreateInputTextPart( "What is deep research by OpenAI?" ), ]), ], options); Console.WriteLine(response.GetOutputText()); Tool search Load deferred tools at runtime javascript 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 from openai import OpenAI client = OpenAI() crm_namespace = { "type" : "namespace" , "name" : "crm" , "description" : "CRM tools for customer lookup and order management." , "tools" : [ { "type" : "function" , "name" : "get_customer_profile" , "description" : "Fetch a customer profile by customer ID." , "parameters" : { "type" : "object" , "properties" : { "customer_id" : { "type" : "string" }, }, "required" : [ "customer_id" ], "additionalProperties" : False , }, }, { "type" : "function" , "name" : "list_open_orders" , "description" : "List open orders for a customer ID." , "defer_loading" : True , "parameters" : { "type" : "object" , "properties" : { "customer_id" : { "type" : "string" }, }, "required" : [ "customer_id" ], "additionalProperties" : False , }, }, ], } response = client.responses.create( model= "gpt-5.4" , input = "List open orders for customer CUST-12345." , tools=[ crm_namespace, { "type" : "tool_search" }, ], parallel_tool_calls= False , ) print (response.output) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 import OpenAI from "openai" ; const client = new OpenAI(); const crmNamespace = { type : "namespace" , name : "crm" , description : "CRM tools for customer lookup and order management." , tools : [ { type : "function" , name : "get_customer_profile" , description : "Fetch a customer profile by customer ID." , parameters : { type : "object" , properties : { customer_id : { type : "string" }, }, required : [ "customer_id" ], additionalProperties : false , }, }, { type : "function" , name : "list_open_orders" , description : "List open orders for a customer ID." , defer_loading : true , parameters : { type : "object" , properties : { customer_id : { type : "string" }, }, required : [ "customer_id" ], additionalProperties : false , }, }, ], }; const response = await client.responses.create({ model : "gpt-5.4" , input : "List open orders for customer CUST-12345." , tools : [crmNamespace, { type : "tool_search" }], parallel_tool_calls : false , }); console .log(response.output); Function calling Call your own function javascript 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 import OpenAI from "openai" ; const client = new OpenAI(); const tools = [ { type : "function" , name : "get_weather" , description : "Get current temperature for a given location." , parameters : { type : "object" , properties : { location : { type : "string" , description : "City and country e.g.

Extracted text:

Using tools | OpenAI API

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

Starter app

Experiment with built-in tools in the Responses API.

Copy Page

More page actions

Copy Page

More page actions

When generating model responses or building agents, you can extend capabilities using built‑in tools, function calling, tool search, and remote MCP servers. These enable the model to search the web, retrieve from your files, load deferred tool definitions at runtime, call your own functions, or access third‑party services. Only

gpt-5.4

and later models support

tool_search

.

Web search

File search

Tool search

Function calling

Remote MCP

Web search

Include web search results for the model response

javascript

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

response =

await

client.responses.create({

model

:

"gpt-5"

,

tools

: [

{

type

:

"web_search"

},

],

input

:

"What was a positive news story from today?"

,

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

from

openai

import

OpenAI

client = OpenAI()

response = client.responses.create(

model=

"gpt-5"

,

tools=[{

"type"

:

"web_search"

}],

input

=

"What was a positive news story from today?"

)

print

(response.output_text)

1

2

3

4

5

6

7

8

curl

"https://api.openai.com/v1/responses"

\

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-d

'{

"model": "gpt-5",

"tools": [{"type": "web_search"}],

"input": "what was a positive news story from today?"

}'

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

using

OpenAI.Responses;

string

key = Environment.GetEnvironmentVariable(

"OPENAI_API_KEY"

)!;

OpenAIResponseClient client =

new

(model:

"gpt-5"

, apiKey: key);

ResponseCreationOptions options =

new

();

options.Tools.Add(ResponseTool.CreateWebSearchTool());

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([

ResponseItem.CreateUserMessageItem([

ResponseContentPart.CreateInputTextPart(

"What was a positive news story from today?"

),

]),

], options);

Console.WriteLine(response.GetOutputText());

File search

Search your files in a response

javascript

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

from

openai

import

OpenAI

client = OpenAI()

response = client.responses.create(

model=

"gpt-4.1"

,

input

=

"What is deep research by OpenAI?"

,

tools=[{

"type"

:

"file_search"

,

"vector_store_ids"

: [

"<vector_store_id>"

]

}]

)

print

(response)

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

"gpt-4.1"

,

input

:

"What is deep research by OpenAI?"

,

tools

: [

{

type

:

"file_search"

,

vector_store_ids

: [

"<vector_store_id>"

],

},

],

});

console

.log(response);

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

using

OpenAI.Responses;

string

key = Environment.GetEnvironmentVariable(

"OPENAI_API_KEY"

)!;

OpenAIResponseClient client =

new

(model:

"gpt-5"

, apiKey: key);

ResponseCreationOptions options =

new

();

options.Tools.Add(ResponseTool.CreateFileSearchTool([

"<vector_store_id>"

]));

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([

ResponseItem.CreateUserMessageItem([

ResponseContentPart.CreateInputTextPart(

"What is deep research by OpenAI?"

),

]),

], options);

Console.WriteLine(response.GetOutputText());

Tool search

Load deferred tools at runtime

javascript

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

from

openai

import

OpenAI

client = OpenAI()

crm_namespace = {

"type"

:

"namespace"

,

"name"

:

"crm"

,

"description"

:

"CRM tools for customer lookup and order management."

,

"tools"

: [

{

"type"

:

"function"

,

"name"

:

"get_customer_profile"

,

"description"

:

"Fetch a customer profile by customer ID."

,

"parameters"

: {

"type"

:

"object"

,

"properties"

: {

"customer_id"

: {

"type"

:

"string"

},

},

"required"

: [

"customer_id"

],

"additionalProperties"

:

False

,

},

},

{

"type"

:

"function"

,

"name"

:

"list_open_orders"

,

"description"

:

"List open orders for a customer ID."

,

"defer_loading"

:

True

,

"parameters"

: {

"type"

:

"object"

,

"properties"

: {

"customer_id"

: {

"type"

:

"string"

},

},

"required"

: [

"customer_id"

],

"additionalProperties"

:

False

,

},

},

],

}

response = client.responses.create(

model=

"gpt-5.4"

,

input

=

"List open orders for customer CUST-12345."

,

tools=[

crm_namespace,

{

"type"

:

"tool_search"

},

],

parallel_tool_calls=

False

,

)

print

(response.output)

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

crmNamespace = {

type

:

"namespace"

,

name

:

"crm"

,

description

:

"CRM tools for customer lookup and order management."

,

tools

: [

{

type

:

"function"

,

name

:

"get_customer_profile"

,

description

:

"Fetch a customer profile by customer ID."

,

parameters

: {

type

:

"object"

,

properties

: {

customer_id

: {

type

:

"string"

},

},

required

: [

"customer_id"

],

additionalProperties

:

false

,

},

},

{

type

:

"function"

,

name

:

"list_open_orders"

,

description

:

"List open orders for a customer ID."

,

defer_loading

:

true

,

parameters

: {

type

:

"object"

,

properties

: {

customer_id

: {

type

:

"string"

},

},

required

: [

"customer_id"

],

additionalProperties

:

false

,

},

},

],

};

const

response =

await

client.responses.create({

model

:

"gpt-5.4"

,

input

:

"List open orders for customer CUST-12345."

,

tools

: [crmNamespace, {

type

:

"tool_search"

}],

parallel_tool_calls

:

false

,

});

console

.log(response.output);

Function calling

Call your own function

javascript

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

tools = [

{

type

:

"function"

,

name

:

"get_weather"

,

description

:

"Get current temperature for a given location."

,

parameters

: {

type

:

"object"

,

properties

: {

location

: {

type

:

"string"

,

description

:

"City and country e.g. Bogotá, Colombia"

,

},

},

required

: [

"location"

],

additionalProperties

:

false

,

},

strict

:

true

,

},

];

const

response =

await

client.responses.create({

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

:

"What is the weather like in Paris today?"

},

],

tools,

});

console

.log(response.output[

0

].to_json());

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

from

openai

import

OpenAI

client = OpenAI()

tools = [

{

"type"

:

"function"

,

"name"

:

"get_weather"

,

"description"

:

"Get current temperature for a given location."

,

"parameters"

: {

"type"

:

"object"

,

"properties"

: {

"location"

: {

"type"

:

"string"

,

"description"

:

"City and country e.g. Bogotá, Colombia"

,

}

},

"required"

: [

"location"

],

"additionalProperties"

:

False

,

},

"strict"

:

True

,

},

]

response = client.responses.create(

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

:

"What is the weather like in Paris today?"

},

],

tools=tools,

)

print

(response.output[

0

].to_json())

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

using

System.Text.Json;

using

OpenAI.Responses;

string

key = Environment.GetEnvironmentVariable(

"OPENAI_API_KEY"

)!;

OpenAIResponseClient client =

new

(model:

"gpt-5"

, apiKey: key);

ResponseCreationOptions options =

new

();

options.Tools.Add(ResponseTool.CreateFunctionTool(

functionName:

"get_weather"

,

functionDescription:

"Get current temperature for a given location."

,

functionParameters: BinaryData.FromObjectAsJson(

new

{

type =

"object"

,

properties =

new

{

location =

new

{

type =

"string"

,

description =

"City and country e.g. Bogotá, Colombia"

}

},

required =

new

[] {

"location"

},

additionalProperties =

false

}),

strictModeEnabled:

true

)

);

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([

ResponseItem.CreateUserMessageItem([

ResponseContentPart.CreateInputTextPart(

"What is the weather like in Paris today?"

)

])

], options);

Console.WriteLine(JsonSerializer.Serialize(response.OutputItems[

0

]));

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

curl -X POST https://api.openai.com/v1/responses \

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-H

"Content-Type: application/json"

\

-d

'{

"model": "gpt-5",

"input": [

{"role": "user", "content": "What is the weather like in Paris today?"}

],

"tools": [

{

"type": "function",

"name": "get_weather",

"description": "Get current temperature for a given location.",

"parameters": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "City and country e.g. Bogotá, Colombia"

}

},

"required": ["location"],

"additionalProperties": false

},

"strict": true

}

]

}'

Remote MCP

Call a remote MCP server

javascript

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

curl https://api.openai.com/v1/responses \

-H

"Content-Type: application/json"

\

-H

"Authorization: Bearer

$OPENAI_API_KEY

"

\

-d

'{

"model": "gpt-5",

"tools": [

{

"type": "mcp",

"server_label": "dmcp",

"server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",

"server_url": "https://dmcp-server.deno.dev/sse",

"require_approval": "never"

}

],

"input": "Roll 2d4+1"

}'

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

import

OpenAI

from

"openai"

;

const

client =

new

OpenAI();

const

resp =

await

client.responses.create({

model

:

"gpt-5"

,

tools

: [

{

type

:

"mcp"

,

server_label

:

"dmcp"

,

server_description

:

"A Dungeons and Dragons MCP server to assist with dice rolling."

,

server_url

:

"https://dmcp-server.deno.dev/sse"

,

require_approval

:

"never"

,

},

],

input

:

"Roll 2d4+1"

,

});

console

.log(resp.output_text);

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

client = OpenAI()

resp = client.responses.create(

model=

"gpt-5"

,

tools=[

{

"type"

:

"mcp"

,

"server_label"

:

"dmcp"

,

"server_description"

:

"A Dungeons and Dragons MCP server to assist with dice rolling."

,

"server_url"

:

"https://dmcp-server.deno.dev/sse"

,

"require_approval"

:

"never"

,

},

],

input

=

"Roll 2d4+1"

,

)

print

(resp.output_text)

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

using

OpenAI.Responses;

string

key = Environment.GetEnvironmentVariable(

"OPENAI_API_KEY"

)!;

OpenAIResponseClient client =

new

(model:

"gpt-5"

, apiKey: key);

ResponseCreationOptions options =

new

();

options.Tools.Add(ResponseTool.CreateMcpTool(

serverLabel:

"dmcp"

,

serverUri:

new

Uri(

"https://dmcp-server.deno.dev/sse"

),

toolCallApprovalPolicy:

new

McpToolCallApprovalPolicy(GlobalMcpToolCallApprovalPolicy.NeverRequireApproval)

));

OpenAIResponse response = (OpenAIResponse)client.CreateResponse([

ResponseItem.CreateUserMessageItem([

ResponseContentPart.CreateInputTextPart(

"Roll 2d4+1"

)

])

], options);

Console.WriteLine(response.GetOutputText());

Available tools

Here’s an overview of the tools available in the OpenAI platform—select one of them for further guidance on usage.

Function calling

Call custom code to give the model access to additional data and capabilities.

Web search

Include data from the Internet in model response generation.

Remote MCP servers

Give the model access to new capabilities via Model Context Protocol (MCP) servers.

Skills

Upload and reuse versioned skill bundles in hosted shell environments.

Shell

Run shell commands in hosted containers or in your own local runtime.

Computer use

Create agentic workflows that enable a model to control a computer interface.

Image generation

Generate or edit images using GPT Image.

File search

Search the contents of uploaded files for context when generating a response.

Tool search

Dynamically load relevant tools into the model’s context to optimize token usage.

Usage in the API

When making a request to generate a

model response

, you usually enable tool access by specifying configurations in the

tools

parameter. Each tool has its own unique configuration requirements—see the

Available tools

section for detailed instructions.

Based on the provided

prompt

, the model automatically decides whether to use a configured tool. For instance, if your prompt requests information beyond the model’s training cutoff date and web search is enabled, the model will typically invoke the web search tool to retrieve relevant, up-to-date information.

Some advanced workflows can also load more tool definitions during the interaction. For example,

tool search

can defer function definitions until the model decides they’re needed.

You can explicitly control or guide this behavior by setting the

tool_choice

parameter

in the API request

.

Usage in the Agents SDK

In the Agents SDK, the tool semantics stay the same, but the wiring moves into the agent definition and workflow design rather than a single Responses API request.

Attach hosted tools, function tools, or hosted MCP tools directly on the agent when one specialist should call them itself.

Expose a specialist as a tool when a manager should stay in control of the user-facing reply.

Keep shell, apply patch, and computer-use harnesses in your runtime even when the SDK models the tool decision.

Wrap local logic as a function tool

typescript

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

import

{ tool }

from

"@openai/agents"

;

import

{ z }

from

"zod"

;

const

getWeatherTool = tool({

name

:

"get_weather"

,

description

:

"Get the weather for a given city."

,

parameters

: z.object({

city

: z.string() }),

async

execute

(

{ city }

)

{

return

`The weather in

${city}

is sunny.`

;

},

});

1

2

3

4

5

6

7

from

agents

import

function_tool

@function_tool

def

get_weather

(

city:

str

) ->

str

:

"""Get the weather for a given city."""

return

f"The weather in

{city}

is sunny."

Expose a specialist as a tool

typescript

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

import

{ Agent }

from

"@openai/agents"

;

const

summarizer =

new

Agent({

name

:

"Summarizer"

,

instructions

:

"Generate a concise summary of the supplied text."

,

});

const

mainAgent =

new

Agent({

name

:

"Research assistant"

,

tools

: [

summarizer.asTool({

toolName

:

"summarize_text"

,

toolDescription

:

"Generate a concise summary of the supplied text."

,

}),

],

});

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

from

agents

import

Agent

summarizer = Agent(

name=

"Summarizer"

,

instructions=

"Generate a concise summary of the supplied text."

,

)

main_agent = Agent(

name=

"Research assistant"

,

tools=[

summarizer.as_tool(

tool_name=

"summarize_text"

,

tool_description=

"Generate a concise summary of the supplied text."

,

)

],

)

Use

Agent definitions

when you are shaping a single specialist,

Orchestration and handoffs

when tools affect ownership,

Guardrails and human review

when tools affect approvals, and

Integrations and observability

when the capability comes from MCP.
