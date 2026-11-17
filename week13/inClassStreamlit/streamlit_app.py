import streamlit as st

# following along with: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

page = st.navigation(
  [
    st.Page("app_pages/hello.py", title="Hello", icon="👋"), 
    st.Page("app_pages/plots.py", title="Plots", icon="📈")
  ]
)
page.run()