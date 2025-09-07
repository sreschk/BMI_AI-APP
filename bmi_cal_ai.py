import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyD-KYL2Trc5oAos8Db1FIspL7IIc26w2v4")
model=genai.GenerativeModel(model_name="gemini-2.5-flash-lite")
st.title("AI BASED BMI CALCULATOR: KNOW YOUR HEALTH")

#BMI CALCULATOR
name = st.text_input("enter your name:")
wt = st.number_input("enter your weight:")
ht = st.slider("enter your height in cm:", 50,250)
age = st.number_input("Enter your age:")
gender = st.number_input("Enter your gender:")

bmi=round(wt/(ht/100)**2,2)

st.write(F"{name},your BMI is {bmi}")
