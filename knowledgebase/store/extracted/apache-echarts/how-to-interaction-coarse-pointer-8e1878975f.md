---
title: Intelligent Pointer Snapping - Interaction - How To Guides - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/how-to/interaction/coarse-pointer
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:08.851072+00:00
kind: extracted-doc
---

# Intelligent Pointer Snapping - Interaction - How To Guides - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/how-to/interaction/coarse-pointer

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:23:08.851072+00:00

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

- Intelligent Pointer Snapping - Interaction - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Intelligent Pointer Snapping Some interactive elements may be relatively small in charts, so sometimes it is difficult for users to click and do other operations accurately, especially on the mobile.
- Therefore, in Apache ECharts TM 5.4.0, we introduced the concept of "intelligent pointer snapping".
- Starting from this version, by default, ECharts enables pointer snapping for mobile charts and disables it for non-mobile charts.
- If it needs to be enabled for all platforms, it can be achieved by setting opt.useCoarsePointer to true in init ; set to false is turned off for all platforms.

Extracted text:

Intelligent Pointer Snapping - Interaction - How To Guides - Handbook - Apache ECharts

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

Intelligent Pointer Snapping

Some interactive elements may be relatively small in charts, so sometimes it is difficult for users to click and do other operations accurately, especially on the mobile. Therefore, in Apache ECharts

TM

5.4.0, we introduced the concept of "intelligent pointer snapping".

Starting from this version, by default, ECharts enables pointer snapping for mobile charts and disables it for non-mobile charts.

If it needs to be enabled for all platforms, it can be achieved by setting

opt.useCoarsePointer

to

true

in

init

; set to

false

is turned off for all platforms.

Snapping Algorithm

When a mouse or touch event occurs, ECharts will determine whether it is intersecting with an interactive element based on the position of the mouse or touch. If it is, the element is the object to be interacted with, which is the same logic before this optimization. If not, find an element that is closest to the mouse or touch position within a certain range.

The default range is 44px (see

W3C standard

), developers can set this value through

opt.pointerSize

when

init

.

More specifically, ECharts will loop through different angles and different radii (within

opt.pointerSize

) around the mouse or touch position until it finds an element that intersects it. If found, the element is considered to be the interactive object.

That is, if an element is within the

opt.pointerSize

radius of the mouse or touch position, the closest intersected element is considered the interactive object.

Performance

As for the implementation, we first judge the intersection between the mouse or touch position and the AABB bounding box of all interactive elements, so as to quickly eliminate most of the elements that is not intersecting. Then, we perform an accurate path intersection judgment on the remaining elements. Therefore, from the perspective of user experience, there is hardly any perceivable performance loss.

For chart series with large-scale data (that is, bar charts, scatter charts, etc. with

large: true

enabled), the snapping will not be enabled.

Contributors

Edit this page on GitHub

Ovilia

plainheart
