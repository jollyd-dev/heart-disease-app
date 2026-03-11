
import streamlit as st
import pickle
import pandas as pd

with open('heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Heart Disease Prediction App")
st.write("Enter patient details below")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.number_input("Sex (0=Female, 1=Male)", min_value=0, max_value=1, value=1)
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=250, value=120)
chol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fbs = st.number_input("Fasting Blood Sugar > 120 (0 or 1)", min_value=0, max_value=1, value=0)
restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2, value=1)
thalach = st.number_input("Maximum Heart Rate", min_value=50, max_value=250, value=150)
exang = st.number_input("Exercise Induced Angina (0 or 1)", min_value=0, max_value=1, value=0)
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
slope = st.number_input("Slope (0-2)", min_value=0, max_value=2, value=1)
ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4, value=0)
thal = st.number_input("Thal (0-3)", min_value=0, max_value=3, value=2)

if st.button("Predict"):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                              columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                                       "thalach", "exang", "oldpeak", "slope", "ca", "thal"])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: Heart disease risk detected")
    else:
        st.success("Prediction: No heart disease risk detected")
