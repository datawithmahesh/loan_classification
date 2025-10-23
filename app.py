# Loan Classification System (SVM)
import streamlit as st
import pandas as pd
import pickle as pk

# Page config
st.set_page_config(
    page_title="Loan Classification System",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load model
load_model = pk.load(open('Loan.pickle','rb'))

# --- Custom CSS ---
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(to right, #ffe259, #ffa751);
}

/* Title card */
.title-card {
    background: linear-gradient(to right, #36D1DC, #5B86E5);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-family: 'Arial Black', sans-serif;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Input box styling */
.stNumberInput, .stSelectbox, .stRadio {
    background: #ffffffcc;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 15px;
}

/* Predict button */
.stButton>button {
    background-color: #ff7e5f;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 25px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #feb47b;
}

/* Output card */
.output-card {
    background: linear-gradient(to right, #43e97b, #38f9d7);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* Footer */
.footer {
    text-align:center;
    color: #555;
    margin-top: 40px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# --- Title Section ---
st.markdown('<div class="title-card"><h1>💰 Loan Classification System</h1></div>', unsafe_allow_html=True)

# --- Image ---
st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg", use_container_width=True)

# --- Input Section ---
income = st.number_input("Enter your salary")
home_ownership = st.selectbox("Home Ownership", ["MORTGAGE", "OTHER", "OWN", "RENT"])
loan_amount = st.number_input("Enter your loan amount")
loan_intention = st.selectbox("Loan Intention", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL","PERSONAL", "VENTURE"])
interest_rate = st.number_input("Enter your loan interest rate")
loan_percent_income = st.number_input("Enter your loan percent income")
previous_loan_file = st.radio("Previous loan on file?", ["Yes", "No"])

# --- Mapping ---
previous_loan = {'Yes':True, 'No':False}

home_ownership_map = {"MORTGAGE":0, "OTHER":1, "OWN":2, "RENT":3}
loan_intention_map = {"DEBTCONSOLIDATION":0, "EDUCATION":1, "HOMEIMPROVEMENT":2, "MEDICAL":3,"PERSONAL":4,"VENTURE":5}

# --- Prediction ---
if st.button("Predict 🟢"):
    if income <= 0 or loan_amount <= 0 or interest_rate <= 0 or loan_percent_income <= 0:
        st.warning("⚠️ Please enter valid numeric values before predicting!")
    else:
        # proceed with creating df and predicting
        df = pd.DataFrame({
            'person_income':[income],
            'person_home_ownership': [home_ownership_map[home_ownership]],
            'loan_amnt': [loan_amount],
            'loan_intent':[loan_intention_map[loan_intention]],
            'loan_int_rate':[interest_rate],
            'loan_percent_income':[loan_percent_income],
            'previous_loan_defaults_on_file':[previous_loan[previous_loan_file]]
        })
        
        st.dataframe(df)
        result = load_model.predict(df)
        
        if int(result.tolist()[0]) == 1:
            st.markdown('<div class="output-card">🎉 Congratulations! You qualify for the loan.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="output-card">❌ Sorry! You are not qualified for the loan.</div>', unsafe_allow_html=True)






# # yo chai SVM ko loan data sets ko ho 

# import streamlit as st
# import pandas as pd
# import pickle as pk
# st.image("https://pianalytix.com/wp-content/uploads/2020/12/Salary-Prediction-Model-using-ML-1024x427.jpg&quot")

# # load model
# load_model= pk.load(open('Loan.pickle','rb'))

# #input data from user
# st.title("loan classification system")
# income = st.number_input("Enter your salary")
# home_ownership = st.selectbox("Home_Ownership =", ["MORTGAGE", "OTHER", "OWN", "RENT"])
# loan_amount = st.number_input("Enter your loan amount")
# loan_intention = st.selectbox("Loan_Intention =", ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL","PERSONAL", "VENTURE"])
# interest_rate = st.number_input("Enter your loan interest rate")
# loan_percent_income = st.number_input("Enter your loan percent income")
# previous_loan_file = st.radio("loan_file =", ["Yes", "No"])

# #mapping
# previous_loan = {'Yes':True, 'No':False}

# if home_ownership == "MORTGAGE":
#     home_ownership = 0
# elif home_ownership == "OTHER":
#     home_ownership = 1
# elif home_ownership == "OWN":
#     home_ownership = 2
# else:
#     home_ownership = 3


# if loan_intention == "DEBTCONSOLIDATION":
#     loan_intention = 0
# elif loan_intention== "EDUCATION":
#     loan_intention = 1
# elif loan_intention == "HOMEIMPROVEMENT":
#     loan_intention = 2
# elif loan_intention == "MEDICAL":
#     loan_intention = 3
# elif loan_intention == "PERSONAL":
#     loan_intention = 4
# else:
#     loan_intention = 5

# #person_income	person_home_ownership	loan_amnt	loan_intent	loan_int_rate	loan_percent_income	previous_loan_defaults_on_file	loan_status

# if st.button("predict"):
#     df = pd.DataFrame({
#         'person_income':[income],
#         'person_home_ownership': [home_ownership],
#         'loan_amnt': [loan_amount],
#         'loan_intent':[loan_intention],
#         'loan_int_rate':[interest_rate],
#         'loan_percent_income':[loan_percent_income],
#         'previous_loan_defaults_on_file':[previous_loan[previous_loan_file]]
#      })
#     st.dataframe(df)
#     result = load_model.predict(df)
#     print(type(result))    
#     if int(result.tolist()[0])== 1:
#         st.write("Congratulations!!, you got the loan")
#     else:
#         st.write("Sorry!!, you are not qualified for the loan")





# st.write("This model is done by Mahesh Thapa")


