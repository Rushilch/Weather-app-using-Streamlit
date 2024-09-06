from cProfile import label

import streamlit as st
import plotly.express as px
import pandas as pd
from pandas import read_csv

st.title("In search of happiness")

fieldx = st.selectbox(label="Field in X axis",
             options=['happiness', "gdp", "social_support", "life_expectancy",
                      "freedom_to_make_life_choices", "generosity", "corruption"])
fieldy = st.selectbox(label="Field in Y axis",
             options=["gdp",'happiness' ,"social_support", "life_expectancy",
                      "freedom_to_make_life_choices", "generosity", "corruption"])

st.header(f"{fieldx} vs {fieldy}")

df = read_csv("bonus/happy.csv")

datax = df[fieldx]
datay = df[fieldy]

figure = px.scatter(x=datax,
                    title=f"{fieldx} vs {fieldy}",
                    y=datay,
                    hover_name=df["country"],
                    labels={"x":fieldx,"y":fieldy}
                    )
st.plotly_chart(figure_or_data=figure)

