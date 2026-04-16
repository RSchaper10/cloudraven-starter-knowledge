---
title: 5.4 - What's New - Basics - Handbook - Apache ECharts
source_url: https://echarts.apache.org/handbook/en/basics/release-note/5-4-0
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:22:44.022672+00:00
kind: extracted-doc
---

# 5.4 - What's New - Basics - Handbook - Apache ECharts

Source URL:

- https://echarts.apache.org/handbook/en/basics/release-note/5-4-0

Dependency:

- Apache ECharts

Collected at:

- 2026-04-16T03:22:44.022672+00:00

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

- 5.4 - What's New - Basics - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Apache ECharts 5.4.0 Features Intelligent Pointer Snapping Some interactive elements may be relatively small in charts, so sometimes it is difficult for users to click and do other operations accurately, especially on the mobile.
- Therefore, in Apache ECharts 5.4.0, we introduced the concept of "intelligent pointer snapping".
- See intelligent pointer snapping for details.
- Using Pie charts in more coordinate systems A very powerful feature of Apache ECharts is the combination of various chart types, coordinate systems, and components.

Extracted text:

5.4 - What's New - Basics - Handbook - Apache ECharts

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

Apache ECharts 5.4.0 Features

Intelligent Pointer Snapping

Some interactive elements may be relatively small in charts, so sometimes it is difficult for users to click and do other operations accurately, especially on the mobile. Therefore, in Apache ECharts 5.4.0, we introduced the concept of "intelligent pointer snapping".

See

intelligent pointer snapping

for details.

Using Pie charts in more coordinate systems

A very powerful feature of Apache ECharts is the combination of various chart types, coordinate systems, and components. In this version, we have added the coordinate systems option for pie charts.

Thus, pie charts can appear in the Cartesian coordinate systems,

calendar coordinate systems,

geographical coordinate systems,

and even with the Baidu Map and Gaode Map extension.

This greatly extends the flexibility of pie charts, allowing developers to create more combinations of chart effects using Apache ECharts.

Ukrainian Translation

In this release, we added the support of the Ukrainian language.

Now Apache ECharts supports 17 languages!

If you need to use a language other than English or Chinese, you need to call

echarts.registerLocale

to initialize the chart before initializing it, and then pass

opts.locale

to modify the chart language during

init

.

Gauge Label Rotation

In this version, we support text rotation of the Gauge series.

axisLabel.rotate

can be set to

'tangential' | 'radial' | number

. If it is of type

number

, it indicates the rotation angle of the label from -90 degrees to 90 degrees, with positive values being counterclockwise. In addition to this, it can also be the strings

'radial'

for radial rotation and

'tangential'

for tangential rotation.

Full Changelog

View the

Changelog

Contributors

Edit this page on GitHub

Ovilia
