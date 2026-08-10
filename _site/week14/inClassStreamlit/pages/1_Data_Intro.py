import streamlit as st

st.set_page_config(
  page_title="Introduction to Data",
  page_icon=":1234:"
)
# note: this is different from how it looks on the "landing" page (Hello.py)
st.sidebar.header("Introduction to Data")

st.title('Introduction to Data')

st.write("This is a placeholder were we could give some information about our data source.")
st.markdown("""This is just to practice another way of writing!  For example, maybe I want to include a URL to the data source I can use Markdown to do so [here is the link](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv).""")

# read in data with pandas
import pandas as pd

mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

df = pd.read_csv(mobility_url)

st.subheader("Quick table view of our dataframe")
st.write(df)

st.subheader("Quick simple plot of data values")

# using matplotlib to add plots
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
df['Graduation'].plot(kind='hist',ax=ax)
#plt.show() # typically this won't work with streamlit
st.pyplot(fig)
