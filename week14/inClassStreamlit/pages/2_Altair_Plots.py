import streamlit as st

st.set_page_config(
  page_title="Altair Plots",
  page_icon=":1234:"
)
# note: this is different from how it looks on the "landing" page (Hello.py)
st.sidebar.header("Altair Plots")

st.title('Altair Plots')

# note here -- the imports don't "carry" from one 
#  page to the next, we have to re-import packages
#  and data! 
import altair as alt
import pandas as pd
mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'
df = pd.read_csv(mobility_url)

st.subheader("Simple plot and simple display")
scatters = alt.Chart(mobility_url).mark_point().encode(
    x = 'Mobility:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q',
                    scale=alt.Scale(scheme='sinebow'),
                    bin=alt.Bin(maxbins=5))
)
scatters

st.subheader('More complex layouts')
col1,col2 = st.columns([0.7, 0.25])
col1.altair_chart(scatters, theme='streamlit',
                    use_container_width=True) # for older version, same in README
                  # width='content') # for newer version of streamlit
col2.markdown("Here is some text on the side of the plot.")
col2.image('https://64.media.tumblr.com/49cca6608ce97d52e3d1d8c1b2b563cd/tumblr_inline_pmof1hYEgO1ud0rrx_640.jpg')

st.subheader('Dashboard')

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