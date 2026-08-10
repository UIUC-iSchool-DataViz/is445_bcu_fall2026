---
layout: week
visible: true
icon: undraw_good_doggy_4wfq.svg
notitle: true
examples:
  - filename: prepStreamlit
    type: iodide
    title: Prep Streamlit Files, Week 13
    description: In class notebook
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2025/tree/main/week13/prepStreamlit
  - filename: inClassStreamlit
    type: iodide
    title: In class Streamlit Files, Week 13
    description: Updating storage of Jekyll files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2025/tree/master/week13/inClassStreamlit
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is referring to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
---

# Guest Lecture from NCSA AVL on SciViz & More web dev with Altair and Jekyll

We talk a little bit about publishing and add in some Altair in Python/Jekyll.

## Extra files

Full corgi dataset available [here](corg/corgiData_countries_full_2020.json).



## Optional reading list

1. <a href="https://streamlit.io/">Streamlit docs</a> - in particular <a href="https://docs.streamlit.io/develop/api-reference/charts/st.pyplot">matplotlib plots</a>
2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a> 
3. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions/bindings_widgets.html#bindings-widgets">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a> 
4. <a href="https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148">This blog post for a walkthrough of deploying a Streamlit space on HuggingFace</a>