# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my fancy app!')

st.header("This is a header")
st.subheader('This is a subheader')

st.text('This is some text.')


# 1. Layout elements
col1,col2 = st.columns(2)
col1.write('This is thing 1')
col2.write('This is thing 2')

# 2. Images
st.subheader('Images')
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da',
         width=200,
         caption='A thinly veiled excuse for a cute corg!')


import numpy as np

img_data = np.random.random((200,200))
st.image(img_data, 
         caption='Random numpy data')

st.header('Altair in Streamlit')
import altair as alt

mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

scatters = alt.Chart(mobility_url).mark_point().encode(
    x = 'Mobility:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q',
                    scale=alt.Scale(scheme='sinebow'),
                    bin=alt.Bin(maxbins=5))
)
scatters

st.markdown("""Add in altair charts with layout elements
 """)

col1,col2 = st.columns([0.7, 0.25])
col1.altair_chart(scatters, theme='streamlit',
                    use_container_width=True) # for older version, same in README
                  # width='content') # for newer version of streamlit
col2.markdown("Here is some text on the side of the plot.")
col2.image('https://64.media.tumblr.com/49cca6608ce97d52e3d1d8c1b2b563cd/tumblr_inline_pmof1hYEgO1ud0rrx_640.jpg')

# add in more things for Week 12
st.header('More with Pandas and Matplotlib')

# read in data with pandas
import pandas as pd
df = pd.read_csv(mobility_url)

st.write(df)

# using matplotlib to add plots
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df['Graduation'].plot(kind='hist',ax=ax)
#plt.show() # typically this won't work with streamlit
st.pyplot(fig)

st.write("""Note that I have added things to the requirements.txt file """)
st.code("""
streamlit==1.36.0
altair
pandas
matplotlib
""")

st.subheader('Quick example widget')

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars", key="feedback1")
if selected is not None:
  st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

st.write("""I'll update this example widget:""")

sentiment_mapping2 = ["one", "two", "three", "four", "five"]
selected2 = st.feedback("stars", key="feedback2") # for this version, need to specify separate keys
if selected2 is not None: # only run what is below if star is selected
  if selected2 < 1:
    st.markdown("Sorry you didn't want more stars :(")
  elif selected2 < 3:
    st.markdown("Glad you have chosen more stars")
  else:
    st.markdown("Hurray!  You like stars!")

st.subheader('Can also include Altair Dashboards')

brush = alt.selection_interval(encodings=['x','y'])

chart1 = alt.Chart(mobility_url).mark_rect().encode(
    alt.X("Student_teacher_ratio:Q", bin=alt.Bin(maxbins=10)),
    alt.Y("State:O"),
    alt.Color("count()")
).properties(
    height=400
).add_params(
    brush
)

chart2 = alt.Chart(mobility_url).mark_bar().encode(
    alt.X("Mobility:Q", bin=True, axis=alt.Axis(title='Mobility Score')),
    alt.Y("count()", axis=alt.Axis(title='Frequency'))
).transform_filter(
    brush
)

chart = chart1 | chart2
st.altair_chart(chart, theme='streamlit',
                width='stretch')
                    #use_container_width=True) 