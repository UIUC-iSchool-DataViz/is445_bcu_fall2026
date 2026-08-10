# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

# this was added to include a title and icon for the page
st.set_page_config(
  page_title="Hello",
  page_icon="👋"
)

# this sidebar was added to be able to support multi-page apps
st.sidebar.success("Select a Page")

st.title('This is my fancy multi-page app!')
st.write("Expand the sidebar to see other views of the data.")

