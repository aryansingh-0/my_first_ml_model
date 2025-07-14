# app.py
import streamlit as st
import joblib

# Load the model
model = joblib.load("model.pkl")

# Streamlit UI
st.title("Text Classifier")
st.write("Enter a sentence and the model will predict the class")

# User input
user_input = st.text_input("Your Text")

# Predict
if st.button("Predict"):
    prediction = model.predict([user_input])
    st.success(f"Prediction: {prediction[0]}")
