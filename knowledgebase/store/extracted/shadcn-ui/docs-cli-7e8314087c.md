---
title: shadcn - shadcn/ui
source_url: https://ui.shadcn.com/docs/cli
target_id: shadcn-ui
dependency: shadcn/ui
collected_at: 2026-04-16T03:29:16.890569+00:00
kind: extracted-doc
---

# shadcn - shadcn/ui

Source URL:

- https://ui.shadcn.com/docs/cli

Dependency:

- shadcn/ui

Collected at:

- 2026-04-16T03:29:16.890569+00:00

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

- shadcn - shadcn/ui Sections Introduction Components Installation Theming CLI RTL Skills MCP Server Registry Forms Changelog Components Accordion Alert Alert Dialog Aspect Ratio Avatar Badge Breadcrumb Button Button Group Calendar Card Carousel Chart Checkbox Collapsible Combobox Command Context Menu Data Table Date Picker Dialog Direction Drawer Dropdown Menu Empty Field Hover Card Input Input Group Input OTP Item Kbd Label Menubar Native Select Navigation Menu Pagination Popover Progress Radio Group Resizable Scroll Area Select Separator Sheet Sidebar Skeleton Slider Sonner Spinner Switch Table Tabs Textarea Toast Toggle Toggle Group Tooltip Typography Get Started Installation components.json Theming Dark Mode CLI Monorepo Skills Open in v0 JavaScript Figma llms.txt Legacy Docs Forms React Hook Form TanStack Form Registry Introduction Getting Started Namespaces Authentication Examples MCP Server Add a Registry Open in v0 registry.json registry-item.json shadcn Copy Page Previous Next Use the shadcn CLI to add components to your project.
- init Use the init command to initialize configuration and dependencies for an existing project, or create a new project with --name .
- The init command installs dependencies, adds the cn util and configures CSS variables for the project.
- pnpm npm yarn bun pnpm dlx shadcn@latest init Copy Options Copy Usage: shadcn init [options] [components...] initialize your project and install dependencies Arguments: components names, url or local path to component Options: -t, --template < templat e > the template to use.
- (next, vite, start, react-router, laravel, astro ) -b, --base < bas e > the component library to use.

Extracted text:

shadcn - shadcn/ui

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

shadcn

Copy Page

Previous

Next

Use the shadcn CLI to add components to your project.

init

Use the

init

command to initialize configuration and dependencies for an existing project, or create a new project with

--name

.

The

init

command installs dependencies, adds the

cn

util and configures CSS variables for the project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest init

Copy

Options

Copy

Usage:

shadcn

init

[options] [components...]

initialize

your

project

and

install

dependencies

Arguments:

components

names,

url

or

local

path

to

component

Options:

-t,

--template

<

templat

e

>

the

template

to

use.

(next,

vite,

start,

react-router,

laravel,

astro

)

-b,

--base

<

bas

e

>

the

component

library

to

use.

(radix,

base

)

-p,

--preset

[name] use a preset configuration

-y,

--yes

skip

confirmation

prompt.

(default:

true

)

-d,

--defaults

use

default

configuration:

--template=next

--preset=nova

(default:

false

)

-f,

--force

force

overwrite

of

existing

configuration.

(default:

false

)

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-n,

--name

<

nam

e

>

the

name

for

the

new

project.

-s,

--silent

mute

output.

(default:

false

)

--css-variables

use

css

variables

for

theming.

(default:

true

)

--no-css-variables

do

not

use

css

variables

for

theming.

--monorepo

scaffold

a

monorepo

project.

--no-monorepo

skip

the

monorepo

prompt.

--rtl

enable

RTL

support.

--no-rtl

disable

RTL

support.

--reinstall

re-install

existing

UI

components.

--no-reinstall

do

not

re-install

existing

UI

components.

-h,

--help

display

help

for

command

The

create

command is an alias for

init

:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest create

Copy

add

Use the

add

command to add components and dependencies to your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest add [component]

Copy

Options

Copy

Usage:

shadcn

add

[options] [components...]

add

a

component

to

your

project

Arguments:

components

name,

url

or

local

path

to

component

Options:

-y,

--yes

skip

confirmation

prompt.

(default:

false

)

-o,

--overwrite

overwrite

existing

files.

(default:

false

)

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-a,

--all

add

all

available

components

(default:

false

)

-p,

--path

<

pat

h

>

the

path

to

add

the

component

to.

-s,

--silent

mute

output.

(default:

false

)

--dry-run

preview

changes

without

writing

files.

(default:

false

)

--diff

[path] show diff

for

a file.

--view

[path] show file contents.

-h,

--help

display

help

for

command

apply

Use the

apply

command to apply a preset to an existing project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest apply --preset a2r6bw

Copy

Options

Copy

Usage:

shadcn

apply

[options] [preset]

apply

a

preset

to

an

existing

project

Arguments:

preset

the

preset

to

apply

Options:

--preset

<

prese

t

>

preset

configuration

to

apply

-y,

--yes

skip

confirmation

prompt.

(default:

false

)

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-s,

--silent

mute

output.

(default:

false

)

-h,

--help

display

help

for

command

view

Use the

view

command to view items from the registry before installing them.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest view [item]

Copy

You can view multiple items at once:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest view button card dialog

Copy

Or view items from namespaced registries:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest view @acme/auth @v0/dashboard

Copy

Options

Copy

Usage:

shadcn

view

[options]

<

items...

>

view

items

from

the

registry

Arguments:

items

the

item

names

or

URLs

to

view

Options:

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-h,

--help

display

help

for

command

search

Use the

search

command to search for items from registries.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest search [registry]

Copy

You can search with a query:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest search @shadcn -q "button"

Copy

Or search multiple registries at once:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest search @shadcn @v0 @acme

Copy

The

list

command is an alias for

search

:

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest list @acme

Copy

Options

Copy

Usage:

shadcn

search

|

list

[options]

<

registries...

>

search

items

from

registries

Arguments:

registries

the

registry

names

or

urls

to

search

items

from.

Names

must

be

prefixed

with

@.

Options:

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-q,

--query

<

quer

y

>

query

string

-l,

--limit

<

numbe

r

>

maximum

number

of

items

to

display

per

registry

(default:

"100"

)

-o,

--offset

<

numbe

r

>

number

of

items

to

skip

(default:

"0"

)

-h,

--help

display

help

for

command

build

Use the

build

command to generate the registry JSON files.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest build

Copy

This command reads the

registry.json

file and generates the registry JSON files in the

public/r

directory.

Options

Copy

Usage:

shadcn

build

[options] [registry]

build

components

for

a

shadcn

registry

Arguments:

registry

path

to

registry.json

file

(default:

"./registry.json"

)

Options:

-o,

--output

<

pat

h

>

destination

directory

for

json

files

(default:

"./public/r"

)

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-h,

--help

display

help

for

command

To customize the output directory, use the

--output

option.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest build --output ./public/registry

Copy

docs

Use the

docs

command to fetch documentation and API references for components.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest docs [component]

Copy

Options

Copy

Usage:

shadcn

docs

[options] [component]

fetch

documentation

and

API

references

for

components

Arguments:

component

the

component

to

get

docs

for

Options:

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-b,

--base

<

bas

e

>

the

base

to

use

either

'base'

or

'radix'.

defaults

to

project

base.

--json

output

as

JSON.

(default:

false

)

-h,

--help

display

help

for

command

info

Use the

info

command to get information about your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest info

Copy

Options

Copy

Usage:

shadcn

info

[options]

get

information

about

your

project

Options:

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

--json

output

as

JSON.

(default:

false

)

-h,

--help

display

help

for

command

migrate

Use the

migrate

command to run migrations on your project.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest migrate [migration]

Copy

Available Migrations

Migration

Description

icons

Migrate your UI components to a different icon library.

radix

Migrate to radix-ui.

rtl

Migrate your components to support RTL (right-to-left).

Options

Copy

Usage:

shadcn

migrate

[options] [migration] [path]

run

a

migration.

Arguments:

migration

the

migration

to

run.

path

optional

path

or

glob

pattern

to

migrate.

Options:

-c,

--cwd

<

cw

d

>

the

working

directory.

defaults

to

the

current

directory.

-l,

--list

list

all

migrations.

(default:

false

)

-y,

--yes

skip

confirmation

prompt.

(default:

false

)

-h,

--help

display

help

for

command

migrate rtl

The

rtl

migration transforms your components to support RTL (right-to-left) languages.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest migrate rtl

Copy

This will:

Update

components.json

to set

rtl: true

Transform physical CSS properties to logical equivalents (e.g.,

ml-4

→

ms-4

,

text-left

→

text-start

)

Add

rtl:

variants where needed (e.g.,

space-x-4

→

space-x-4 rtl:space-x-reverse

)

Migrate specific files

You can migrate specific files or use glob patterns:

Copy

# Migrate a specific file

npx

shadcn@latest

migrate

rtl

src/components/ui/button.tsx

# Migrate files matching a glob pattern

npx

shadcn@latest

migrate

rtl

"src/components/ui/**"

If no path is provided, the migration will transform all files in your

ui

directory (from

components.json

).

migrate radix

The

radix

migration updates your imports from individual

@radix-ui/react-*

packages to the unified

radix-ui

package.

pnpm

npm

yarn

bun

pnpm dlx shadcn@latest migrate radix

Copy

This will:

Transform imports from

@radix-ui/react-*

to

radix-ui

Add the

radix-ui

package to your

package.json

Before

Copy

import

*

as

DialogPrimitive

from

"@radix-ui/react-dialog"

import

*

as

SelectPrimitive

from

"@radix-ui/react-select"

After

Copy

import

{ Dialog

as

DialogPrimitive, Select

as

SelectPrimitive }

from

"radix-ui"

Migrate specific files

You can migrate specific files or use glob patterns:

Copy

# Migrate a specific file.

npx

shadcn@latest

migrate

radix

src/components/ui/dialog.tsx

# Migrate files matching a glob pattern.

npx

shadcn@latest

migrate

radix

"src/components/ui/**"

If no path is provided, the migration will transform all files in your

ui

directory (from

components.json

).

Once complete, you can remove any unused

@radix-ui/react-*

packages from your

package.json

.

RTL

Monorepo

On This Page

init

add

apply

view

search

build

docs

info

migrate

migrate rtl

migrate radix

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now

Deploy to Vercel

Create Project
