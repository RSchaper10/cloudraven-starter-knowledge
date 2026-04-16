---
title: <page url="/docs/react/components/button-group"> | CloudRaven Enrichment
source_url: https://heroui.com/react/llms-components.txt
target_id: heroui-react
dependency: HeroUI React
collected_at: 2026-04-16T03:20:47.405381+00:00
kind: enriched-doc
tags: ui-system, react, design-system
---

# <page url="/docs/react/components/button-group"> | CloudRaven Enrichment

Source URL:

- https://heroui.com/react/llms-components.txt

Dependency:

- HeroUI React

Collection scope:

- Collect the official HeroUI React LLM exports for guides, components, and patterns.

What this page is useful for:

- <page url="/docs/react/components/button-group"> # ButtonGroup **Category**: react **URL**: https://www.heroui.com/docs/react/components/button-group **Source**: https://raw.githubusercontent.com/heroui-inc/heroui/refs/heads/v3/apps/docs/content/docs/react/components/(buttons)/button-group.mdx > Group related buttons together with consistent styling and spacing ## Import ```tsx import { ButtonGroup, Button } from '@heroui/react'; ``` ### Usage ```tsx import { ChevronDown, ChevronLeft, ChevronRight, CodeFork, Ellipsis, Picture, Pin, QrCode, Star, TextAlignCenter, TextAlignJustify, TextAlignLeft, TextAlignRight, ThumbsDown, ThumbsUp, Video, } from "@gravity-ui/icons"; import {Button, ButtonGroup, Chip, Description, Dropdown, Label} from "@heroui/react"; export function Basic() { return ( <div className="flex flex-col items-start gap-6"> {/* Single button with dropdown */} <div className="flex flex-col gap-2"> <ButtonGroup> <Button>Merge pull request</Button> <Dropdown> <Button isIconOnly aria-label="More options"> <ButtonGroup.Separator /> <ChevronDown /> </Button> <Dropdown.Popover className="max-w-[290px]" placement="bottom end"> <Dropdown.Menu> <Dropdown.Item className="flex flex-col items-start gap-1" id="merge" textValue="Create a merge commit" > <Label>Create a merge commit</Label> <Description> All commits from this branch will be added to the base branch </Description> </Dropdown.Item> <Dropdown.Item className="flex flex-col items-start gap-1" id="squash-and-merge" textValue="Squash and merge" > <Label>Squash and merge</Label> <Description> The 14 commits from this branch will be combined into one commit in the base branch </Description> </Dropdown.Item> <Dropdown.Item className="flex flex-col items-start gap-1" id="rebase-and-merge" textValue="Rebase and merge" > <Label>Rebase and merge</Label> <Description> The 14 commits from this branch will be rebased and added to the base branch </Description> </Dropdown.Item> </Dropdown.Menu> </Dropdown.Popover> </Dropdown> </ButtonGroup> </div> {/* Individual buttons */} <div className="flex flex-col gap-2"> <div className="flex flex-wrap gap-x-2 gap-y-4"> <ButtonGroup variant="tertiary"> <Button> <CodeFork className="size-3.5" /> Fork <Chip color="accent" size="sm" variant="soft"> 24 </Chip> </Button> <Button isIconOnly> <ButtonGroup.Separator /> <ChevronDown /> </Button> </ButtonGroup> <ButtonGroup variant="tertiary"> <Button isIconOnly> <QrCode /> </Button> <Button> <ButtonGroup.Separator /> Scan to pay </Button> </ButtonGroup> <ButtonGroup variant="tertiary"> <Button> <ThumbsUp /> <span className="text-xs font-semibold">2.4K</span> </Button> <Button isIconOnly> <ButtonGroup.Separator /> <ThumbsDown /> </Button> </ButtonGroup> <ButtonGroup variant="tertiary"> <Button> <Star className="size-3.5" /> Star </Button> <Button className="px-2"> <ButtonGroup.Separator /> <Chip color="accent" size="sm" variant="soft"> 104 </Chip> </Button> </ButtonGroup> <ButtonGroup variant="tertiary"> <Button> <Pin /> Pinned </Button> <Button isIconOnly> <ButtonGroup.Separator /> <ChevronDown /> </Button> </ButtonGroup> </div> </div> {/* Previous/Next Button Group */} <div className="flex flex-col gap-2"> <ButtonGroup variant="tertiary"> <Button> <ChevronLeft /> Previous </Button> <Button> <ButtonGroup.Separator /> Next <ChevronRight /> </Button> </ButtonGroup> </div> {/* Content Selection Button Group */} <div className="flex flex-col gap-2"> <ButtonGroup variant="tertiary"> <Button> <Picture /> Photos </Button> <Button> <ButtonGroup.Separator /> <Video /> Videos </Button> <Button isIconOnly aria-label="More options"> <ButtonGroup.Separator /> <Ellipsis /> </Button> </ButtonGroup> </div> {/* Text Alignment Button Group */} <div className="flex flex-col gap-2"> <ButtonGroup variant="tertiary"> <Button>Left</Button> <Button> <ButtonGroup.Separator /> Center </Button> <Button> <ButtonGroup.Separator /> Right </Button> </ButtonGroup> </div> {/* Icon-Only Alignment Button Group */} <div className="flex flex-col gap-2"> <ButtonGroup variant="tertiary"> <Button isIconOnly> <TextAlignLeft /> </Button> <Button isIconOnly> <ButtonGroup.Separator /> <TextAlignCenter /> </Button> <Button isIconOnly> <ButtonGroup.Separator /> <TextAlignRight /> </Button> <Button isIconOnly> <ButtonGroup.Separator /> <TextAlignJustify /> </Button> </ButtonGroup> </div> </div> ); } ``` ### Anatomy Import the ButtonGroup component and access all parts using dot notation.
- ```tsx import { ButtonGroup, Button } from '@heroui/react'; export default () => ( <ButtonGroup> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> ); ``` > **ButtonGroup** wraps multiple Button components together, applying consistent styling, spacing, and automatic border radius handling.
- It uses React Context to pass `size`, `variant`, and `isDisabled` props to all child buttons.
- ### Variants ```tsx import {Button, ButtonGroup} from "@heroui/react"; export function Variants() { return ( <div className="flex flex-col gap-6"> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Primary</p> <ButtonGroup variant="primary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Secondary</p> <ButtonGroup variant="secondary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Tertiary</p> <ButtonGroup variant="tertiary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Outline</p> <ButtonGroup variant="outline"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Ghost</p> <ButtonGroup variant="ghost"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col gap-2"> <p className="text-sm text-muted">Danger</p> <ButtonGroup variant="danger"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> </div> ); } ``` ### Sizes ```tsx import {Button, ButtonGroup} from "@heroui/react"; export function Sizes() { return ( <div className="flex flex-col gap-4"> <div className="flex flex-col items-start gap-2"> <p className="text-sm text-muted">Small</p> <ButtonGroup size="sm" variant="secondary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col items-start gap-2"> <p className="text-sm text-muted">Medium (default)</p> <ButtonGroup size="md" variant="secondary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> <div className="flex flex-col items-start gap-2"> <p className="text-sm text-muted">Large</p> <ButtonGroup size="lg" variant="secondary"> <Button>First</Button> <Button> <ButtonGroup.Separator /> Second </Button> <Button> <ButtonGroup.Separator /> Third </Button> </ButtonGroup> </div> </div> ); } ``` ### Orientation Use the `orientation` prop to arrange buttons horizontally or vertically.

CloudRaven applicability:

- Use this material when the app needs fast interface assembly with a coherent component system.

Prototype-to-production review:

- High fit for operational interfaces and starter portals.
- Define theming choices early if the product needs strong branding.

CloudRaven example paths:

- Assemble internal dashboards, onboarding flows, and admin surfaces quickly.
- Pair with Tailwind when the app needs both structured components and custom layout work.

Suggested retrieval tags:

- `ui-system`
- `react`
- `design-system`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/heroui-react/react-llms-components-txt-3a2ee0b1b3.md`
- Raw source: `knowledgebase/store/raw_html/heroui-react/react-llms-components-txt-3a2ee0b1b3.txt`
