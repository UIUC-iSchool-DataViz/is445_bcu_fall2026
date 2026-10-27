---
name: Week 10 In Class
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/lineplot.png
description: Altair and Data Sizes
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---


# In class -- Week 10

This will explore different ways of doing the same plot with different plot sizes.

## Using the dataframe in the plot

<vegachart schema-url="{{ site.baseurl }}/assets/json/altair_mobility_dataframe.json" style="width: 100%"></vegachart>

## Using data URL

<vegachart schema-url="{{ site.baseurl }}/assets/json/altair_mobility_url.json" style="width: 100%"></vegachart>

## Using dataframe subset

<vegachart schema-url="{{ site.baseurl }}/assets/json/altair_mobility_subset.json" style="width: 100%"></vegachart>


<!-- these are written in a combo of html and liquid --> 

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_bcu_fall2026/blob/main/week10/inClass_week11.ipynb" text="The Analysis" %}
</div>

