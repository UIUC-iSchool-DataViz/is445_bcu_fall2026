import streamlit as st

# following format of: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

page = st.navigation(
    [
        st.Page("app_pages/hello.py", title="Hello", icon="👋"),
        st.Page("app_pages/data_intro.py", title="Introduce Data", icon="📈"),
        st.Page("app_pages/widgets.py", title="Exploring Widgets", icon="🌍"),
        st.Page("app_pages/altair_plots.py", title="Altair Plots", icon="📊"),
        st.Page("app_pages/other_tools.py", title="Other Tools", icon="📊"),
    ]
)
page.run()


