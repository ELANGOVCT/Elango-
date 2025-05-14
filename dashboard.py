import streamlit as st
import pandas as pd
import joblib

st.title("Quality Deviation Prediction Dashboard")

uploaded_file = st.file_uploader("Upload Batch Data CSV")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    model = joblib.load("model.pkl")
    predictions = model.predict(df)
    df["Prediction"] = predictions
    st.write("Predictions:")
    st.dataframe(df)
