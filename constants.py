import pandas as pd

def get_api():
    return "c176203b80094939898102242240609"


if __name__ == "__main__":
    df = pd.read_json("http://api.weatherapi.com/v1/forecast.json?key=c176203b80094939898102242240609&q=london")
    print(df)