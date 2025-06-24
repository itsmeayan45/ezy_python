import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")
name=st.text_input("Enter yout name:")

if name:
    st.write(f"Hello {name}")
age=st.slider("Select your age:",0,100,0)
st.write(f"Your age is {age}")
## import selectbox

options=['python','java','c++','javascript']
choice=st.selectbox("Choose your favourite Language:",options)
st.write(f"You have selected {choice}")
## import dataframe

data={
    "Name":["John","Jane","Jake","Jill"],
    "Age":[28,24,35,40],
    "City":["New York","Los Angeles","Chicago","Houston"]
}
df=pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

## upload button

uploaded_file=st.file_uploader("Choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)