import streamlit as st

st.set_page_config(
  page_title="Widget Exploration",
  page_icon=":1234:"
)
# note: this is different from how it looks on the "landing" page (Hello.py)
st.sidebar.header("Widget Exploration")

st.title('Widget Exploration')

# here -- this uses streamlit widgets
# don't have to import other things
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