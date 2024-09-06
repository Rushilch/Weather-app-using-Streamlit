from cProfile import label

import streamlit as st
import plotly.express as px

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

dates=["2024-06-09","2024-07-09","2024-08-09"]
temperatures = [10,23,56]

temperatures= [days * i for i in temperatures]


figure = px.line(x=dates, y=temperatures, title="Prediction",)
st.plotly_chart(figure)