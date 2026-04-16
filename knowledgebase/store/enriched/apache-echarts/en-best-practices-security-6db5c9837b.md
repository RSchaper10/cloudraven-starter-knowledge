---
title: Security Guidelines - Best Practices - Handbook - Apache ECharts | CloudRaven Enrichment
source_url: https://echarts.apache.org/handbook/en/best-practices/security
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:11.608535+00:00
kind: enriched-doc
tags: charts, analytics, dashboards
---

# Security Guidelines - Best Practices - Handbook - Apache ECharts | CloudRaven Enrichment

Source URL:

- https://echarts.apache.org/handbook/en/best-practices/security

Dependency:

- Apache ECharts

Collection scope:

- Collect the starter handbook for charting work.

What this page is useful for:

- Security Guidelines - Best Practices - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Security Guidelines Overview ECharts aims to provide rich and flexible visualization capabilities.
- Although the vast majority of its APIs do not require special security considerations, sereval APIs are exceptions.
- For example, the option tooltip.formatter accepts a raw HTML string, allowing full control over the component's content and layout; the option title.link uses the provided URL string directly without automatic sanitization.

CloudRaven applicability:

- Use this material for dashboards and data storytelling views.

Prototype-to-production review:

- Best fit when charts directly support user decisions.
- Plan responsive behavior and export needs early.

CloudRaven example paths:

- Render operational metrics dashboards for internal teams.
- Turn collected activity data into chart-driven reports.

Suggested retrieval tags:

- `charts`
- `analytics`
- `dashboards`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/apache-echarts/en-best-practices-security-6db5c9837b.md`
- Raw source: `knowledgebase/store/raw_html/apache-echarts/en-best-practices-security-6db5c9837b.html`
