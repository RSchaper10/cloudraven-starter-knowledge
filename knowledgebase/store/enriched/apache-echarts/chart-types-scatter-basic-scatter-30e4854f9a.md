---
title: Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts | CloudRaven Enrichment
source_url: https://echarts.apache.org/handbook/en/how-to/chart-types/scatter/basic-scatter
target_id: apache-echarts
dependency: Apache ECharts
collected_at: 2026-04-16T03:23:02.396671+00:00
kind: enriched-doc
tags: charts, analytics, dashboards
---

# Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts | CloudRaven Enrichment

Source URL:

- https://echarts.apache.org/handbook/en/how-to/chart-types/scatter/basic-scatter

Dependency:

- Apache ECharts

Collection scope:

- Collect the starter handbook for charting work.

What this page is useful for:

- Basic Scatter - Scatter - Common Charts - How To Guides - Handbook - Apache ECharts Get Started Basics Download ECharts Import ECharts Get Help What's New ECharts 6 Features Migration from v5 to v6 5.0 Migration from v4 to v5 5.2 5.3 5.4 5.5 5.6 Concepts Chart Container Style Dataset Data Transform Axis Visual Mapping Legend Event and Action How To Guides Common Charts Bar Basic Bar Stacked Bar Bar Racing Waterfall Line Basic Line Stacked Line Area Chart Smoothed Line Step Line Pie Basic Pie Ring Style Rose Style Scatter Basic Scatter Custom Series Common Components Geo SVG Base Map Cross Platform Server Side Rendering Data Dynamic Data Label Rich Text Animation Data Transition Interaction Drag Intelligent Pointer Snapping Best Practices Canvas vs.
- SVG Aria Security Guidelines Edit Handbook Edit Guide Basic Scatter Chart Scatter Chart, a frequently used chart type, was constructed with several "points".
- These points sometimes represent the position of the value in the coordinate system (cartesian coordinate system, geo coordinate system, etc.), sometimes the size and color of items can be mapped to the value, represent high-dimensional data.
- Simple Example The following example is a basic scatter chart configuration with the x-axis as category and the y-axis as value: option = { xAxis: { data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] }, yAxis: {}, series: [ { type: 'scatter', data: [220, 182, 191, 234, 290, 330, 310] } ] }; option = { xAxis : { data : [ 'Sun' , 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' ] } , yAxis : { } , series : [ { type : 'scatter' , data : [ 220 , 182 , 191 , 234 , 290 , 330 , 310 ] } ] } ; live Scatter Chart in Cartesian Coordinate System In the previous case, the x-axis of the scatter chart is a discrete category axis and the y-axis is a continuous value axis.

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

- Extracted page: `knowledgebase/store/extracted/apache-echarts/chart-types-scatter-basic-scatter-30e4854f9a.md`
- Raw source: `knowledgebase/store/raw_html/apache-echarts/chart-types-scatter-basic-scatter-30e4854f9a.html`
