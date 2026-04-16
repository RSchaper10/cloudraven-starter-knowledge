# ECharts 6 Features - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/v6-feature

Dependency:

- Apache ECharts

Collected at:

- 2026-04-15T19:45:02.441791+00:00

Direct links in scope:

- https://echarts.apache.org/handbook/en/get-started
- https://echarts.apache.org/handbook/en/basics/download
- https://echarts.apache.org/handbook/en/basics/import
- https://echarts.apache.org/handbook/en/basics/help
- https://echarts.apache.org/handbook/en/basics/release-note/v6-feature
- https://echarts.apache.org/handbook/en/basics/release-note/v6-upgrade-guide
- https://echarts.apache.org/handbook/en/basics/release-note/v5-feature
- https://echarts.apache.org/handbook/en/basics/release-note/v5-upgrade-guide
- https://echarts.apache.org/handbook/en/basics/release-note/5-2-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-3-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-4-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-5-0
- https://echarts.apache.org/handbook/en/basics/release-note/5-6-0
- https://echarts.apache.org/handbook/en/concepts/chart-size
- https://echarts.apache.org/handbook/en/concepts/style
- https://echarts.apache.org/handbook/en/concepts/dataset
- https://echarts.apache.org/handbook/en/concepts/data-transform
- https://echarts.apache.org/handbook/en/concepts/axis
- https://echarts.apache.org/handbook/en/concepts/visual-map
- https://echarts.apache.org/handbook/en/concepts/legend

Captured summary:

- ECharts 6 Features - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 6 New Features Twelve years ago, ECharts was first released on GitHub, planting the seed for an open-source journey.
- From a simple charting tool to a visualization powerhouse supporting millions of developers; from a single front-end charting library to a comprehensive technology system covering mobile, large screens, and server-side rendering—over these 12 years, we've witnessed ECharts' continuous technical breakthroughs and have been delighted to see developers worldwide create countless stunning data stories with ECharts.
- Now, Apache ECharts 6.0 is officially released, bringing 12 major upgrades to take your data visualization to the next level.
- Feature Overview Twelve years of accumulation, all for more ultimate visual expression.

Extracted text:

ECharts 6 Features - What's New - Basics - Handbook - Apache ECharts

Get Started

Basics

Download ECharts

Import ECharts

Get Help

What's New

ECharts 6 Features

Migration from v5 to v6

5.0

Migration from v4 to v5

5.2

5.3

5.4

5.5

5.6

Concepts

Chart Container

Style

Dataset

Data Transform

Axis

Visual Mapping

Legend

Event and Action

How To Guides

Common Charts

Bar

Basic Bar

Stacked Bar

Bar Racing

Waterfall

Line

Basic Line

Stacked Line

Area Chart

Smoothed Line

Step Line

Pie

Basic Pie

Ring Style

Rose Style

Scatter

Basic Scatter

Custom Series

Common Components

Geo

SVG Base Map

Cross Platform

Server Side Rendering

Data

Dynamic Data

Label

Rich Text

Animation

Data Transition

Interaction

Drag

Intelligent Pointer Snapping

Best Practices

Canvas vs. SVG

Aria

Security Guidelines

Edit Handbook

Edit Guide

Apache ECharts 6 New Features

Twelve years ago, ECharts was first released on GitHub, planting the seed for an open-source journey.

From a simple charting tool to a visualization powerhouse supporting millions of developers; from a single front-end charting library to a comprehensive technology system covering mobile, large screens, and server-side rendering—over these 12 years, we've witnessed ECharts' continuous technical breakthroughs and have been delighted to see developers worldwide create countless stunning data stories with ECharts.

Now, Apache ECharts 6.0 is officially released, bringing 12 major upgrades to take your data visualization to the next level.

Feature Overview

Twelve years of accumulation, all for more ultimate visual expression. The core strength of Apache ECharts has always come from a deep understanding of developers' real challenges. When defining the direction for 6.0, the question was clear:

How can we make complex data presentation both powerful and elegant?

This drove us to evolve deeply around three core dimensions:

More professional visual presentation

: From a meticulously crafted default theme to intelligent dark mode switching, ensuring charts have a professional look and seamlessly integrate into modern applications.

Expanding the boundaries of data expression

: New chart types and features to handle complex scenarios and enable intuitive expression of deep data.

Unleashing freedom of composition

: From the revolutionary matrix coordinate system to reusable custom series and optimized axis labels—empowering developers to freely compose and turn creativity into unconstrained visual works.

We have made 12 upgrades across these three core dimensions. These are not just simple feature additions, but a solid foundation for building the next generation of data-driven applications. They all point to one goal:

to make ECharts powerful, reliable, and stable in the background, leaving the stage and spotlight for your creative expression.

Below, we introduce these twelve upgrades in detail:

More professional visual presentation

1. Brand New Default Theme

: Modern design language for professional data expression

2. Dynamic Theme Switching

: Seamless runtime theme switching for multi-theme scenarios

3. Dark Mode Support

: Automatically adapts to system dark/light mode for better UX

Expanding the boundaries of data expression

4. New Chord Chart

: Visualize complex relationships and distributions

5. New Beeswarm Chart

: Smartly expand overlapping data points into a honeycomb layout

6. New Scatter Jittering

: Add jitter to scatter plots for better readability of dense data

7. New Broken Axis

: Easily present data with large magnitude differences

8. Enhanced Stock Trading Charts

: Improved label capabilities and more out-of-the-box trading charts

Unleashing freedom of composition

9. New Matrix Coordinate System

: Freely combine chart types and components like a table

10. Enhanced Custom Series

: Support npm publishing and dynamic registration for code reuse

11. New Custom Charts

: Violin, contour, stage, bar range, and line range charts

12. Axis Label Optimization

: Smarter default axis label layout to prevent overflow and overlap

With these upgrades, Apache ECharts 6.0 helps users create more charts more flexibly and conveniently, truly achieving "unlimited possibilities in charting"!

Feature Details

1. Brand New Default Theme

During the development of ECharts 6.0, we analyzed real user scenarios and found that over 70% of developers use the default theme. This made us realize: an excellent default theme should not only be aesthetically pleasing but also meet the general needs of various business scenarios.

The new theme system uses design tokens to reconstruct colors, spacing, and other design elements,

making different chart types and components more harmonious and consistent

.

Although the 6.0 theme has significant changes from 5.x, we provide a

v5.js

theme file for developers who want to use new features but keep the old style for quick migration.

2. Dynamic Theme Switching

In previous versions, changing a chart's theme required disposing of the chart instance and re-initializing, which could negatively impact user experience due to repeated animations. In the new version, we implemented

dynamic theme switching

(see documentation), significantly improving the user experience.

3. Dark Mode Support

With dynamic theme registration and switching, a typical scenario is

listening to the system's dark mode and dynamically adjusting the chart's theme

.

This is crucial for business scenarios supporting dark mode, ensuring the application interface matches the system theme and greatly enhancing user experience.

Here's how to listen for system dark mode and change the chart theme:

const

darkModeMediaQuery

=

window

.

matchMedia

(

'(prefers-color-scheme: dark)'

)

;

function

updateDarkMode

(

)

{

const

isDarkMode

=

darkModeMediaQuery

.

matches

;

for

(

const

chart

of

charts

)

{

chart

.

setTheme

(

isDarkMode

?

'dark'

:

'default'

)

;

}

}

darkModeMediaQuery

.

addEventListener

(

'change'

,

(

)

=>

{

updateDarkMode

(

)

;

}

)

;

4. New Chord Chart

Chord charts intuitively show flows and weights in complex relationship networks, ideal for scenarios like financial transactions and social networks. ECharts innovatively supports

using gradient colors from source and target nodes for edges, creating unique visual effects

. See

series-chord

.

5. New Beeswarm Chart

Traditional scatter plots can become overcrowded on category axes. Beeswarm charts use non-numeric axis offsets to

distribute points without overlap while preserving value axis accuracy

. Set

jitter

to a non-zero value and

jitterOverlap

to

false

to enable beeswarm charts.

6. New Scatter Jittering

Scatter jittering adds random offsets to non-data dimensions,

solving the problem of overly dense data points

.

Without jittering, it's hard to see the distribution when data is dense:

With jittering enabled, the densest range (6-8) becomes clear. Compared to beeswarm, scatter jittering offers better performance.

Set

jitter

to a non-zero value and

jitterOverlap

to

true

to enable scatter jittering.

7. New Broken Axis

Broken axis is a visualization technique for showing data with large magnitude differences. In ECharts 6.0, we innovatively implemented a

torn-paper effect for broken axes

, making the meaning more intuitive, and supporting click-to-expand to restore the real data ratio.

8. Enhanced Stock Trading Charts

ECharts 6.0 deeply optimizes for financial trading scenarios, enhancing label positioning relative to coordinate systems to help developers quickly build professional-grade trading analysis tools.

Below is a comprehensive stock trading chart using ECharts, combining

time-sharing, MACD, volume, order book, and depth chart

:

These examples help developers quickly meet financial trading needs. For example, displaying numbers in the four corners of the chart can be achieved with

relativeTo

.

9. New Matrix Coordinate System

The above example also uses the new matrix coordinate system in ECharts 6.0, which is very powerful. It can be used for covariance matrix charts:

Periodic table:

As a layout, it also allows developers to combine various chart types and components to create flexible and complex visualizations:

10. Enhanced Custom Series

Previously, using ECharts custom series meant developers had to write complex

renderItem

logic from scratch, and code reuse was limited to copy-pasting. Now, ECharts 6.0 brings a standardized, reusable solution:

Custom series registration

: Like theme registration, custom series can be dynamically registered and used as easily as built-in series. See

series-custom.renderItem

Official custom series project

: The official project at

https://github.com/apache/echarts-custom-series

provides multiple custom series, available via npm after the official release

Publish your own custom series

: Submit a pull request to the above project or publish to your own repo for code reuse

11. New Custom Charts

This release provides 6 practical custom charts in the custom series project. See

echarts-custom-series

for usage and documentation. Including

violin chart

:

Contour chart

:

Sleep stage chart

:

Segmented doughnut chart

:

Bar range chart

:

Line range chart

:

Unleash your creativity and join us in creating more custom charts!

12. Axis Label Optimization

In previous versions, axis labels and names in rectangular coordinate systems could easily overflow or overlap when data was long. Users couldn't always predict space needs as data changed. In this version, we've optimized the default strategies to prevent overflow and overlap.

Upgrade Guide

See the full

changelog

and

upgrade guide

.

Contributors

Edit this page on GitHub

plainheart

Ovilia
