<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diabetes Prediction App</title>
</head>
<body>
    <h1>Diabetes Prediction App 🍎</h1>
    <p>This app predicts if a person has diabetes based on health metrics. Fill in the form and get an instant prediction.</p>

 <h2>Features:</h2>
    <ul>
        <li>Input health data like glucose levels, BMI, insulin, etc.</li>
        <li>Prediction of whether the person is diabetic or not.</li>
        <li>Health tips after the prediction.</li>
    </ul>

   <h2>Technologies Used:</h2>
    <ul>
        <li>Frontend: Streamlit</li>
        <li>Backend: FastAPI</li>
        <li>Machine Learning: Scikit-learn</li>
    </ul>

   <h2>Project Setup:</h2>
    <h3>1. Clone the Repository:</h3>
    <pre>git clone https://github.com/yourusername/diabetes-prediction-app.git</pre>
    <h3>2. Install Dependencies:</h3>
    <pre>pip install -r requirements.txt</pre>
    <h3>3. Run FastAPI Backend:</h3>
    <pre>uvicorn backend:app --reload</pre>
    <h3>4. Run Streamlit App:</h3>
    <pre>streamlit run diabetes_prediction_app.py</pre>

  <h2>Usage:</h2>
    <ul>
        <li>Enter health metrics (Pregnancies, Glucose, Blood Pressure, etc.) in the form.</li>
        <li>Click "Predict Diabetes" to get the result.</li>
    </ul>
    ![image](https://github.com/user-attachments/assets/82d3da52-37e3-4318-a079-3babbb7b8de1)

</body>
</html>

