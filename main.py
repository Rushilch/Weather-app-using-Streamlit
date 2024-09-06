import streamlit as st

st.title("Weather prediction app")

place = st.text_input(label="Enter your location",
                      help="Enter the location of which weather should be forecasted")

days = st.slider(label="Date ",
                 min_value=1,
                 max_value=5,
                 value=1,
                 step=1,
                 help="Select the number of days to be forecasted")

option = st.selectbox(label="Select data to view",
             options=["Temperature","Humidity","Pressure","Sky"])

st.header(f"{option} Prediction for {days} days in {place}")