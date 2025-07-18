import streamlit as st
import pandas as pd

st.set_page_config(page_title="File Uploader Demo", layout="centered")

st.title("Upload a File and Get Output")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of the File")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())
  
    st.text(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
else:
    st.info("Please upload a CSV file to get started.")
