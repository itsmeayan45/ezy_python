import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("Hello Streamlit")

## Display a simple text
st.write("This is a simple text")

## create a simple dataframe
df=pd.DataFrame(
    {
        'First column':[1,2,3,4],
        'second column': [10,20,30,40]
    }
)

## display the dataframe

st.write("Here is the dataframe")
st.write(df)
## create a linechart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
