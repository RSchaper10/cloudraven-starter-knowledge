---
title: Vite - shadcn/ui
source_url: https://ui.shadcn.com/docs/installation/vite
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:20.745184+00:00
kind: extracted-doc
---

# Vite - shadcn/ui

Source URL:

- https://ui.shadcn.com/docs/installation/vite

Dependency:

- shadcn/ui

Collected at:

- 2026-04-16T03:29:20.745184+00:00

Direct links in scope:

- https://ui.shadcn.com/docs/components
- https://ui.shadcn.com/docs/installation
- https://ui.shadcn.com/docs/theming
- https://ui.shadcn.com/docs/cli
- https://ui.shadcn.com/docs/rtl
- https://ui.shadcn.com/docs/skills
- https://ui.shadcn.com/docs/mcp
- https://ui.shadcn.com/docs/registry
- https://ui.shadcn.com/docs/forms
- https://ui.shadcn.com/docs/changelog
- https://ui.shadcn.com/docs/components/radix/accordion
- https://ui.shadcn.com/docs/components/radix/alert
- https://ui.shadcn.com/docs/components/radix/alert-dialog
- https://ui.shadcn.com/docs/components/radix/aspect-ratio
- https://ui.shadcn.com/docs/components/radix/avatar
- https://ui.shadcn.com/docs/components/radix/badge
- https://ui.shadcn.com/docs/components/radix/breadcrumb
- https://ui.shadcn.com/docs/components/radix/button
- https://ui.shadcn.com/docs/components/radix/button-group
- https://ui.shadcn.com/docs/components/radix/calendar

Captured summary:

- Vite - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json Vite Copy Page Previous Next Install and configure shadcn/ui for Vite.
- Choose the setup that matches your starting point.
- Use shadcn/create Build your preset and generate a Vite project command.
- Use the CLI Scaffold a new Vite project directly from the terminal.
- Existing Project Configure shadcn/ui manually in an existing Vite project.

Extracted text:

Vite - shadcn/ui

Sections

Introduction

Components

Installation

Theming

CLI

RTL

Skills

MCP Server

Registry

Forms

Changelog

Components

Accordion

Alert

Alert Dialog

Aspect Ratio

Avatar

Badge

Breadcrumb

Button

Button Group

Calendar

Card

Carousel

Chart

Checkbox

Collapsible

Combobox

Command

Context Menu

Data Table

Date Picker

Dialog

Direction

Drawer

Dropdown Menu

Empty

Field

Hover Card

Input

Input Group

Input OTP

Item

Kbd

Label

Menubar

Native Select

Navigation Menu

Pagination

Popover

Progress

Radio Group

Resizable

Scroll Area

Select

Separator

Sheet

Sidebar

Skeleton

Slider

Sonner

Spinner

Switch

Table

Tabs

Textarea

Toast

Toggle

Toggle Group

Tooltip

Typography

Get Started

Installation

components.json

Theming

Dark Mode

CLI

Monorepo

Skills

Open in v0

JavaScript

Figma

llms.txt

Legacy Docs

Forms

React Hook Form

TanStack Form

Registry

Introduction

Getting Started

Namespaces

Authentication

Examples

MCP Server

Add a Registry

Open in v0

registry.json

registry-item.json

Vite

Copy Page

Previous

Next

Install and configure shadcn/ui for Vite.

Choose the setup that matches your starting point.

Use shadcn/create

Build your preset and generate a Vite project command.

Use the CLI

Scaffold a new Vite project directly from the terminal.

Existing Project

Configure shadcn/ui manually in an existing Vite project.

Use shadcn/create

Build Your Preset

Open

shadcn/create

and build your preset visually. Choose your style, colors, fonts, icons, and more.

Open shadcn/create

Create Project

Click

Create Project

, choose your package manager, and copy the generated command.

The generated command will look similar to this:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init --preset [CODE] --template vite

Copy

The exact command will include your selected options such as

--base

,

--monorepo

, or

--rtl

.

Add Components

Add the

Card

component to your project:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card

Copy

If you created a monorepo, run the command from

apps/web

or specify the workspace from the repo root:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card -c apps/web

Copy

The command above will add the

Card

component to your project. You can then import it like this:

src/App.tsx

Copy

import

{

Card,

CardContent,

CardDescription,

CardHeader,

CardTitle,

}

from

"@/components/ui/card"

function

App

() {

return

(

<

Card

className

=

"max-w-sm"

>

<

CardHeader

>

<

CardTitle

>Project Overview</

CardTitle

>

<

CardDescription

>

Track progress and recent activity for your Vite app.

</

CardDescription

>

</

CardHeader

>

<

CardContent

>

Your design system is ready. Start building your next component.

</

CardContent

>

</

Card

>

)

}

export

default

App

If you created a monorepo, update

apps/web/src/App.tsx

and import from

@workspace/ui/components/card

instead.

Use the CLI

Create Project

Run the

init

command to scaffold a new Vite project. Follow the prompts to configure your project: base, preset, monorepo, and more.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init -t vite

Copy

For a monorepo project, use

--monorepo

flag:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init -t vite --monorepo

Copy

Add Components

Add the

Card

component to your project:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card

Copy

If you created a monorepo, run the command from

apps/web

or specify the workspace from the repo root:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add card -c apps/web

Copy

The command above will add the

Card

component to your project. You can then import it like this:

src/App.tsx

Copy

import

{

Card,

CardContent,

CardDescription,

CardHeader,

CardTitle,

}

from

"@/components/ui/card"

function

App

() {

return

(

<

Card

className

=

"max-w-sm"

>

<

CardHeader

>

<

CardTitle

>Project Overview</

CardTitle

>

<

CardDescription

>

Track progress and recent activity for your Vite app.

</

CardDescription

>

</

CardHeader

>

<

CardContent

>

Your design system is ready. Start building your next component.

</

CardContent

>

</

Card

>

)

}

export

default

App

If you created a monorepo, update

apps/web/src/App.tsx

and import from

@workspace/ui/components/card

instead.

Existing Project

Create Project

If you need a new Vite project, create one first and select the

React + TypeScript

template. Otherwise, skip this step.

pnpm

npm

yarn

bun

pnpm create vite@latest

Copy

Add Tailwind CSS

If your project already has Tailwind CSS configured, skip this step.

pnpm

npm

yarn

bun

pnpm add tailwindcss @tailwindcss/vite

Copy

Replace everything in

src/index.css

with the following:

src/index.css

Copy

@import

"tailwindcss"

;

Edit tsconfig.json file

If your project already has the

@/*

alias configured, skip this step.

Vite splits TypeScript configuration across multiple files. Add the

baseUrl

and

paths

properties to the

compilerOptions

section of

tsconfig.json

and

tsconfig.app.json

:

tsconfig.json

Copy

{

"files"

: [],

"references"

: [

{

"path"

:

"./tsconfig.app.json"

},

{

"path"

:

"./tsconfig.node.json"

}

],

"compilerOptions"

: {

"baseUrl"

:

"."

,

"paths"

: {

"@/*"

: [

"./src/*"

]

}

}

}

Edit tsconfig.app.json file

Add the same alias to

tsconfig.app.json

so your editor can resolve imports:

tsconfig.app.json

Copy

{

"compilerOptions"

: {

// ...

"baseUrl"

:

"."

,

"paths"

: {

"@/*"

: [

"./src/*"

]

}

// ...

}

}

Update vite.config.ts

Install

@types/node

and update

vite.config.ts

so Vite can resolve the

@

alias:

pnpm

npm

yarn

bun

pnpm add -D @types/node

Copy

vite.config.ts

Copy

import

path

from

"path"

import

tailwindcss

from

"@tailwindcss/vite"

import

react

from

"@vitejs/plugin-react"

import

{ defineConfig }

from

"vite"

// https://vite.dev/config/

export

default

defineConfig

({

plugins: [

react

(),

tailwindcss

()]

,

resolve: {

alias: {

"@"

: path.

resolve

(__dirname,

"./src"

),

},

}

,

})

Run the CLI

Run the

shadcn

init command to set up shadcn/ui in your project:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init

Copy

Add Components

You can now start adding components to your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add button

Copy

The command above will add the

Button

component to your project. You can then import it like this:

src/App.tsx

Copy

import

{ Button }

from

"@/components/ui/button"

function

App

() {

return

(

<

div

className

=

"flex min-h-svh flex-col items-center justify-center"

>

<

Button

>Click me</

Button

>

</

div

>

)

}

export

default

App

Next.js

Laravel

On This Page

Use shadcn/create

Build Your Preset

Create Project

Add Components

Use the CLI

Create Project

Add Components

Existing Project

Create Project

Add Tailwind CSS

Edit tsconfig.json file

Edit tsconfig.app.json file

Update vite.config.ts

Run the CLI

Add Components

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now

Deploy to Vercel

Create Project
