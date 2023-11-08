import urllib
from dataclasses import dataclass
import os
import requests

@dataclass
class WeatherInfo:
    caption: str
    temperature: float
    wind_direction: str
    wind_level: str

def get_city_weather(city: str) -> WeatherInfo:
    host = 'https://ali-weather.showapi.com'
    path = '/area-to-weather-date'
    encode_city = urllib.parse.quote_plus(city)
    query = f'area={encode_city}&needMoreDay=0&needIndex=0&need3HourForcast=0&needAlarm=0&needHourData=0' 
    url = host + path + '?' + query
    appcode = os.environ.get('appcode')

    cus_header = {'Authorization': 'APPCODE ' + appcode}
    response = requests.get(url, headers=cus_header)

     # Check if the cityname exists
    
    if response.status_code == 200:
     # Successful request with a valid cityname
        content = response.json()
        print(content)
        f1 = content['showapi_res_body']['f1']
        # Format the respnse as JSON
        profile = WeatherInfo(
            f1['day_weather'],
            f1['day_air_temperature'],
            f1['day_wind_direction'],
            f1['day_wind_power']
            )

        return profile
    
    elif response.status_code == 404:
        return None
    else:
        raise(SystemError("Weather service is down. Error:" + response.status_code))
