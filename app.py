import streamlit as st
import pandas as pd
import pickle

# Load the model from disk
model = pickle.load(open('xgb_classifier.pkl', 'rb'))

# Streamlit page configuration
st.title('Start-up Succes Classification Prediction')

# User inputs via sidebar
avg_raised_amount_usd = st.sidebar.number_input("Average Raised Amount (USD)", min_value=0.0, value=0.0, step=1000.0)
avg_years_between_round = st.sidebar.number_input("Average Years Between Rounds", min_value=0.0, value=0.0, step=0.1)
funding_rounds = st.sidebar.number_input("Funding Rounds", min_value=0, value=0)
Industry_Group = st.sidebar.selectbox("Industry Group", ['Software', 'Travel', 'Biotechnology', 'Sustainability',
       'Manufacturing', 'Electronics', 'Mobile', 'Community',
       'Health Care', 'Shopping', 'Internet', 'Financial', 'Other',
       'Gaming', 'Education', 'Data', 'Services', 'Media', 'Sales',
       'Events', 'Real Estate', 'Sports', 'Advertising', 'Content',
       'Privacy', 'IT', 'Energy', 'Food', 'Design', 'Music', 'Unknown',
       'Science', 'Video', 'Administrative Services', 'Transportation',
       'Message', 'Consumer Goods', 'Clothing', 'Hardware', 'App',
       'Platforms', 'Artificial Intelligence', 'Agriculture', 'Goverment',
       'Navigation', 'Resource'])
continent = st.sidebar.selectbox("Continent", ['Americas', 'Europe', 'Asia', 'Africa', 'Oceania'])

# Prepare user inputs for prediction
input_data = pd.DataFrame([[avg_raised_amount_usd, avg_years_between_round, Industry_Group, funding_rounds, continent]],
                          columns=['avg_raised_amount_usd', 'avg_years_between_round', 'Industry_Group', 'funding_rounds', 'continent'])

# Make predictions
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

# Display user inputs and prediction results
st.write("## User Input Parameters")
st.write(input_data)

st.write("## Prediction")
st.write("Prediction (0 or 1):", prediction[0])
st.write("Prediction Probability (class 1): {:.2f}".format(prediction_proba[0][1]))
