import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Streamlit UI
st.title("Email Spam Classifier")
st.write("Enter an email or message below, and the model will predict whether it's spam or not.")

# User input
user_input = st.text_input("Your Message")

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict([user_input])[0]  # Get scalar value from array

    if prediction == 1:
        st.error("This message is **SPAM**. Be cautious before clicking links or replying.")
    else:
        st.success("This message is **NOT SPAM**. It seems safe.")
