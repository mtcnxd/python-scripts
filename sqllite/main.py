from DataBaseLite import DataBaseLite
import requests
import random
import time
import json

sqlite = DataBaseLite()

def get_weather_data():
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=20.957552894644706&lon=-89.58960415319825&"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

if __name__ == "__main__":
    sqlite.create_table()
    weather_data = get_weather_data()
    
    if weather_data is not None:
        for data in weather_data['properties']['timeseries']:
            data_time         = data['time']
            air_temperature   = data['data']['instant']['details']['air_temperature']
            relative_humidity = data['data']['instant']['details']['relative_humidity']
            wind_speed        = data['data']['instant']['details']['wind_speed']
            
            sqlite.insert_data(data_time, air_temperature, relative_humidity, wind_speed)

    data = sqlite.query_fetch_all()
    sqlite.close()

    for row in data:
        print(f"{row['id']} | The temperature at {row['time']} will be {row['temperature']} degrees and the relative humidity will be {row['humidity']}%")
        time.sleep(0.02)