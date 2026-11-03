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