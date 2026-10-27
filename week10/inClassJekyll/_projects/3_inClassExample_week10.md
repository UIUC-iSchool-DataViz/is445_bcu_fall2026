---
name: In Class Notebook
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/lineplot.png
description: More Altair examples
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---


# In class

Adding in a simple lines plot with some dropdown interactivity.

<vegachart schema-url="{{ site.baseurl }}/assets/json/simpleLines.json" style="width: 100%"></vegachart>



<!-- these are written in a combo of html and liquid --> 

<div class="left">
{% include elements/button.html link="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_bcu_fall2026/blob/main/week09/inClass_week10.ipynb" text="The Analysis" %}
</div>

