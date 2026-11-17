import streamlit as st

# following along with: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

page = st.navigation(
  [
    st.Page("app_pages/hello.py", title="Hello", icon="👋"), 
    st.Page("app_pages/plots.py", title="Plots", icon=":material/show_chart:"),
    st.Page("app_pages/data_explore.py", title="Data", icon=":material/table_chart:"),
    st.Page("app_pages/widget_explore.py", title="Widgets", icon=":material/forms_add_on:")

  ]
)
page.run()