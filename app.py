import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

st.title("Renewable Energy Forecasting App")

st.write("Upload your renewable energy dataset to get predictions using the pre-trained model.")

# Loading saved model and scaler
model = joblib.load("energy_model.pkl")
scaler = joblib.load("scaler.pkl")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    if {"Wind", "Solar", "Hydro"}.issubset(data.columns):
        X = data[["Wind", "Solar", "Hydro"]]
        X_scaled = scaler.transform(X)

        y_pred = model.predict(X_scaled)

        st.write("### Predicted Energy Output")
        st.write(y_pred)

        if "Energy" in data.columns: 
            st.write("### Predictions vs Actual")
            fig, ax = plt.subplots()
            ax.plot(y_actual, label="Actual")
            ax.plot(y_pred, label="Predicted")
            ax.legend()
            st.pyplot(fig)
    else:
        st.error("Dataset must contain 'Wind', 'Solar', 'Hydro' columns.")
