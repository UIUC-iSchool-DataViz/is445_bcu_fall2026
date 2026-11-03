# To access this in near-real time try: https://github.com/UIUC-iSchool-DataViz/is445_bcu_fall2026/blob/main/week10/inClass_script_week10.py

# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my fancy app!')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is some simple text')

st.header('Layout elements')
col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

st.header('Images')
st.image("https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da",
width=200, caption='Derpy corgi')

import numpy as np
img_data = np.random.random((200,400))
st.image(img_data, caption='Random data')

### Here will be altair things
st.subheader('Altair Practice')
mobility_url ='https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

import pandas as pd

df = pd.read_csv(mobility_url)

st.text('Showing the dataframe:')
df

import altair as alt

scatters = alt.Chart(mobility_url).mark_point().encode(
    x='Mobility:Q', 
    # y='Population:Q'
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q',scale=alt.Scale(scheme='sinebow'), 
    bin=alt.Bin(maxbins=5))
)
scatters

st.text('Building in some interactivity')

brush=alt.selection_interval(encodings=['x','y'])

chart1 = alt.Chart(mobility_url).mark_rect().encode(
    alt.X('Student_teacher_ratio:Q', bin=alt.Bin(maxbins=10)),
    alt.Y('State:O'),
    alt.Color("count()")
).properties(
    height=400
).add_params(
    brush
)

chart2 = alt.Chart(mobility_url).mark_bar().encode(
    alt.X('Mobility:Q', bin=True),
    alt.Y("count()")
).transform_filter(
    brush
)

chart = chart1 | chart2
chart

st.text('trying out Tab layout')

tab1, tab2 = st.tabs(['Mobility interactive', 'Scatter plot'])

with tab1:
    st.altair_chart(chart)
with tab2:
    st.altair_chart(scatters)


st.subheader('Quick Vega-editor copy')
# from numpy.random import default_rng as rng

# df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

df = pd.read_json('https://raw.githubusercontent.com/vega/vega-datasets/refs/heads/master/data/population.json')

st.vega_lite_chart(
    df,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
    alt="Scatter plot of a vs b sized by c",
)

# {
#   "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
#   "description": "A population pyramid for the US in 2000, created using stack. See https://vega.github.io/vega-lite/examples/concat_population_pyramid.html for a variant of this created using concat.",
#   "data": { "url": "data/population.json"},
#   "transform": [
#     {"filter": "datum.year == 2000"},
#     {"calculate": "datum.sex == 2 ? 'Female' : 'Male'", "as": "gender"},
#     {"calculate": "datum.sex == 2 ? -datum.people : datum.people", "as": "signed_people"}
#   ],
#   "width": 300,
#   "height": 200,
#   "mark": "bar",
#   "encoding": {
#     "y": {
#       "field": "age",
#       "axis": null, "sort": "descending"
#     },
#     "x": {
#       "aggregate": "sum", "field": "signed_people",
#       "title": "population",
#       "axis": {"format": "s"}
#     },
#     "color": {
#       "field": "gender",
#       "scale": {"range": ["#675193", "#ca8861"]},
#       "legend": {"orient": "top", "title": null}
#     }
#   },
#   "config": {
#     "view": {"stroke": null},
#     "axis": {"grid": false}
#   }
# }