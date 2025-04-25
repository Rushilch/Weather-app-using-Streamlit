import pandas as pd

def get_api():
    return API_KEY


if __name__ == "__main__":
    df = pd.read_json("http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=london")
    print(df)
