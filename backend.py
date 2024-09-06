from constants import get_api
import pandas as pd

def get_data(place,days):
    api_key = get_api()
    place = place.replace(" ","_")
    url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={place}&days={days}&aqi=no&alerts=no"
    df = pd.read_json(url)
    return df["forecast"]["forecastday"]


if __name__ == '__main__':
    data = get_data("hyderabad", 10)
    print(data)
    for i in range(5 ): #days
        for j in range(24 ):#hours
            print(data[i]['hour'][j]['time'])
            print(data[i]['hour'][j]['temp_c'])