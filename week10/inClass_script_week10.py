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