# yo chai SVM ko loan data sets ko ho 

import streamlit as st
import pandas as pd
import pickle as pk
st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg&quot")

# load model
load_model= pk.load(open('Loan.pickle','rb'))

#input data from user
st.title("loan classification system")
income = st.number_input("Enter your salary")
home_ownership = st.selectbox("Home_Ownership =", ["MORTGAGE", "OTHER", "OWN", "RENT"])
loan_amount = st.number_input("Enter your loan amount")
loan_intention = st.selectbox("Loan_Intention =", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL","PERSONAL", "VENTURE"])
interest_rate = st.number_input("Enter your loan interest rate")
loan_percent_income = st.number_input("Enter your loan percent income")
previous_loan_file = st.radio("loan_file =", ["Yes", "No"])

#mapping
previous_loan = {'Yes':True, 'No':False}

if home_ownership == "MORTGAGE":
    home_ownership = 0
elif home_ownership == "OTHER":
    home_ownership = 1
elif home_ownership == "OWN":
    home_ownership = 2
else:
    home_ownership = 3


if loan_intention == "DEBTCONSOLIDATION":
    loan_intention = 0
elif loan_intention== "EDUCATION":
    loan_intention = 1
elif loan_intention == "HOMEIMPROVEMENT":
    loan_intention = 2
elif loan_intention == "MEDICAL":
    loan_intention = 3
elif loan_intention == "PERSONAL":
    loan_intention = 4
else:
    loan_intention = 5

#person_income	person_home_ownership	loan_amnt	loan_intent	loan_int_rate	loan_percent_income	previous_loan_defaults_on_file	loan_status

if st.button("predict"):
    df = pd.DataFrame({
        'person_income':[income],
        'person_home_ownership': [home_ownership],
        'loan_amnt': [loan_amount],
        'loan_intent':[loan_intention],
        'loan_int_rate':[interest_rate],
        'loan_percent_income':[loan_percent_income],
        'previous_loan_defaults_on_file':[previous_loan[previous_loan_file]]
     })
    st.dataframe(df)
    result = load_model.predict(df)
    print(type(result))    
    if int(result.tolist()[0])== 1:
        st.write("Congratulations!!, you got the loan")
    else:
        st.write("Sorry!!, you are not qualified for the loan")





st.write("This model is done by Mahesh Thapa")