import streamlit as st
import requests
import json

# URL of the FastAPI backend
api_url = "http://127.0.0.1:8000/diabetes_prediction"  # Replace with your actual API URL

# Function to get prediction from the API
def get_prediction(input_data):
    with st.spinner("Making prediction..."):
        # Send the data to the API and get the prediction
        response = requests.post(api_url, json=input_data)
        
        if response.status_code == 200:
            return response.text
        else:
            return "Error in prediction"

# Set page config and custom styles
st.set_page_config(page_title="Diabetes Prediction", page_icon="🍎", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            padding: 15px 32px;
        }
        .stButton>button:hover {
            background-color: #006F8E;
        }
        .stTextInput>div>input {
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
        }
        .stNumberInput>div>input {
            border-radius: 10px;
            padding: 10px;
            font-size: 18px;
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
        }
        .stSpinner {
            font-size: 18px;
            color: #008CBA;
        }
        .stAlert {
            background-color: #FFCCCC;
            border-left: 5px solid red;
            padding: 10px;
        }
        .stSuccess {
            background-color: #DFF2BF;
            border-left: 5px solid green;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Add title and description
st.title("Diabetes Prediction App 🍎")
st.markdown("""
    Welcome to the **Diabetes Prediction App**! This app uses machine learning to predict if a person has diabetes 
    based on certain health metrics. Fill out the form below to get the result!
""")

# Add an image for visual appeal
st.image("https://via.placeholder.com/800x300?text=Diabetes+Prediction", use_container_width=True)

# Create a form for input fields
with st.form(key="diabetes_form"):
    # Taking inputs
    pregnancies = st.number_input("Pregnancies", min_value=0, value=5)
    glucose = st.number_input("Glucose", min_value=0, value=166)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, value=72)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, value=19)
    insulin = st.number_input("Insulin", min_value=0, value=175)
    bmi = st.number_input("BMI", min_value=0.0, value=25.8)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.587)
    age = st.number_input("Age", min_value=0, value=51)

    # Submit button for prediction
    submit_button = st.form_submit_button("Predict Diabetes")

# If the user clicks the "Predict Diabetes" button
if submit_button:
    # Create a dictionary for the inputs
    input_data = {
        "pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree_function,
        "Age": age
    }

    # Get the prediction
    result = get_prediction(input_data)

    # Display prediction result with styled messages
    if "diabetic" in result.lower():
        st.markdown(f'<div class="stAlert"><strong>🚨 Result: The person is diabetic.</strong></div>', unsafe_allow_html=True)
        st.markdown("""
            Please consult with a healthcare provider for further action.
            Stay healthy, and take care of your well-being.
        """)
    else:
        st.markdown(f'<div class="stSuccess"><strong>✅ Result: The person is not diabetic.</strong></div>', unsafe_allow_html=True)
        st.markdown("""
            Great! Continue maintaining a healthy lifestyle with regular exercise and a balanced diet.
        """)

    # Display prevention tips
    st.markdown("### Diabetes Prevention Tips:")
    st.markdown("""
        - **Eat a balanced diet**: More vegetables, fruits, and whole grains.
        - **Exercise regularly**: Aim for at least 30 minutes of physical activity daily.
        - **Stay hydrated**: Drink plenty of water throughout the day.
        - **Check your blood glucose**: Regularly monitor your glucose levels and visit your healthcare provider.
    """)

    # Reset button to clear the form
    st.button("Reset Form", on_click=lambda: st.rerun())
