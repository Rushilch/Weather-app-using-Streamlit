import streamlit as st
import plotly.express as px
import backend


def get_fig():
    figure = px.line(x=date,
                     y=field,
                     title="Prediction",
                     labels={'x': "Date", 'y': option})
    st.plotly_chart(figure)



st.title("Weather prediction app")
place = st.text_input(label="Enter your location",
                      help="Enter the location of which weather should be forecasted",
                      placeholder="Hyderabad"
                      )

days = st.slider(label="Date ",
                 min_value=1,
                 max_value=10,
                 value=1,
                 step=1,
                 help="Select the number of days to be forecasted")
kind = 'temp_c'
option = st.selectbox(label="Select data to view",
                      options=["Temperature","Humidity","Feels Like","Sky"])
try:
    data = backend.get_data(place,days)

    st.header(f"{option} Prediction for {days} days in {place}")

    match option:
        case 'Temperature':
            kind = 'temp_c'
        case 'Humidity':
            kind = 'humidity'
        case 'Feels Like':
            kind = 'feelslike_c'
        case 'Precipitation':
            kind = 'precip_mm'
        case 'Sky':
            kind = 'condition'

    date,field,icon,text,date2,avgtemp = [],[],[],[],[],[]

    for i in range(days):
        icon.append(data[i]['day']['condition']['icon'])
        text.append(data[i]['day']['condition']['text'])
        avgtemp.append(data[i]['day']['avgtemp_c'])
        date2.append(data[i]['date'])
        for j in range(24):
            date.append(data[i]['hour'][j]['time'])
            field.append(data[i]['hour'][j][kind])

    if option !="Sky":
        get_fig()
    else:
        col3, empty_col, col4 = st.columns([2, 0.5, 2])
        with col3:
            for day in range(0,int(days/2)+1):
                st.subheader(date2[day])
                st.image(image="https:"+icon[day],caption=avgtemp[day],width=128)
                st.subheader(text[day])
                st.divider()

        with col4:
            for day in range(int(days/2)+1,days):
                st.subheader(date2[day])
                st.image(image="https:"+icon[day],caption=avgtemp[day],width=128)
                st.subheader(text[day])
                st.divider()
except:
    st.warning("Please enter a valid location")