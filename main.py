import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('logistic_regression_model_final.pkl')

# Define the input features
st.title('Current Payment Prediction')
st.write("Enter the details below to get the predicted Current Payment.")

# Input fields
opening_balance = st.number_input("Opening Balance", min_value=0.0)
opening_arrears = st.number_input("Opening Arrears", min_value=0.0)
opening_total_due = st.number_input("Opening Total Due", min_value=0.0)
opening_acc_age = st.number_input("Opening Account Age", min_value=0)
delinquency_stage = st.number_input("Delinquency Stage", min_value=0)
total_account_age = st.number_input("Total Account Age", min_value=0)
previous_payment = st.number_input("Previous Payment", min_value=0.0)
previous_payment_amount = st.number_input("Previous Payment Amount", min_value=0.0)
payment_amount = st.number_input("Payment Amount", min_value=0.0)
director_status = st.number_input("Director Status", min_value=0)
contact_score = st.number_input("Contact Score", min_value=0)
credit_risk = st.number_input("Credit Risk", min_value=0)

# Create a DataFrame with the input features
input_data = pd.DataFrame({
    'Opening_Balance': [opening_balance],
    'Opening_Arrears': [opening_arrears],
    'Opening_Total_Due': [opening_total_due],
    'Opening_acc_age': [opening_acc_age],
    'Delinquency Stage': [delinquency_stage],
    'Total Account Age': [total_account_age],
    'Previous_Payment': [previous_payment],
    'Previous_Payment_Amount': [previous_payment_amount],
    'Payment_Amount': [payment_amount],
    'Director_Status': [director_status],
    'Contact_Score': [contact_score],
    'Credit_Risk': [credit_risk]
})

# Add a Predict button
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.write("Prediction: Will not make the payment (0)")
    else:
        st.write("Prediction: Will make the payment (1)")
