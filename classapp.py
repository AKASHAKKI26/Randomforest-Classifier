import streamlit as st
import pickle
import numpy as np

with open("ranf.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Heart Disease Prediction")

age = st.number_input("Age", min_value=1, max_value=120, value=45)

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    value=150
)

oldpeak = st.number_input(
    "Oldpeak",
    value=1.0
)

ca = st.selectbox(
    "Number of Major Vessels (ca)",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    [0, 1, 2, 3]
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1]
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

# Prediction
if st.button("Predict"):

    input_data = np.array([[ 
        age,
        cp,
        thalach,
        oldpeak,
        ca,
        thal,
        exang,
        slope
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease Detected")