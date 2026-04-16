---
title: <page url="/docs/react/getting-started/animation"> | CloudRaven Enrichment
source_url: https://heroui.com/react/llms-patterns.txt
target_id: heroui-react
dependency: HeroUI React
collected_at: 2026-04-16T03:20:47.938323+00:00
kind: enriched-doc
tags: ui-system, react, design-system
---

# <page url="/docs/react/getting-started/animation"> | CloudRaven Enrichment

Source URL:

- https://heroui.com/react/llms-patterns.txt

Dependency:

- HeroUI React

Collection scope:

- Collect the official HeroUI React LLM exports for guides, components, and patterns.

What this page is useful for:

- <page url="/docs/react/getting-started/animation"> # Animation **Category**: react **URL**: https://www.heroui.com/docs/react/getting-started/animation **Source**: https://raw.githubusercontent.com/heroui-inc/heroui/refs/heads/v3/apps/docs/content/docs/react/getting-started/(handbook)/animation.mdx > Add smooth animations and transitions to HeroUI v3 components HeroUI components support multiple animation approaches: built-in CSS transitions, custom CSS animations, and JavaScript libraries like Framer Motion.
- ## Built-in Animations HeroUI components use data attributes to expose their state for animation: ```css /* Popover entrance/exit */ .popover[data-entering] { @apply animate-in zoom-in-90 fade-in-0 duration-200; } .popover[data-exiting] { @apply animate-out zoom-out-95 fade-out duration-150; } /* Button press effect */ .button:active, .button[data-pressed="true"] { transform: scale(0.97); } /* Accordion expansion */ .accordion__panel[aria-hidden="false"] { @apply h-[var(--panel-height)] opacity-100; } ``` **State attributes for styling:** * `[data-hovered="true"]` - Hover state * `[data-pressed="true"]` - Active/pressed state * `[data-focus-visible="true"]` - Keyboard focus * `[data-disabled="true"]` - Disabled state * `[data-entering]` / `[data-exiting]` - Transition states * `[aria-expanded="true"]` - Expanded state ## CSS Animations **Using Tailwind utilities:** ```tsx // Pulse on hover <Button className="hover:animate-pulse"> Hover me </Button> // Fade in entrance <Alert className="animate-fade-in"> Welcome message </Alert> // Staggered list <div className="space-y-2"> <Card className="animate-fade-in animate-delay-100">Item 1</Card> <Card className="animate-fade-in animate-delay-200">Item 2</Card> </div> ``` **Custom transitions:** ```css /* Slower accordion */ .accordion__panel { @apply transition-all duration-500; } /* Bouncy button */ .button:active { animation: bounce 0.3s; } @keyframes bounce { 50% { transform: scale(0.95); } } ``` ## Framer Motion HeroUI components work seamlessly with Framer Motion for advanced animations.
- **Basic usage:** ```tsx import { motion } from 'framer-motion'; import { Button } from '@heroui/react'; const MotionButton = motion(Button); <MotionButton whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }} > Animated Button </MotionButton> ``` **Entrance animations:** ```tsx <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }} > <Alert> <Alert.Title>Welcome!</Alert.Title> </Alert> </motion.div> ``` **Layout animations:** ```tsx import { AnimatePresence, motion } from 'framer-motion'; function Tabs({ items, selected }) { return ( <div className="flex gap-2"> {items.map((item, i) => ( <Button key={i} onPress={() => setSelected(i)}> {item} {selected === i && ( <motion.div layoutId="active" className="absolute inset-0 bg-accent" transition={{ type: "spring", bounce: 0.2 }} /> )} </Button> ))} </div> ); } ``` ## Render Props Apply dynamic animations based on component state: ```tsx <Button> {({ isPressed, isHovered }) => ( <motion.span animate={{ scale: isPressed ?
- 1.05 : 1 }} > Interactive Button </motion.span> )} </Button> ``` ## Accessibility **Respecting motion preferences:** HeroUI automatically respects user motion preferences using Tailwind's `motion-reduce:` utility.

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

- Extracted page: `knowledgebase/store/extracted/heroui-react/react-llms-patterns-txt-434c89fdec.md`
- Raw source: `knowledgebase/store/raw_html/heroui-react/react-llms-patterns-txt-434c89fdec.txt`
