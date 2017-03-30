import json
import os
import time

from pytz import timezone
import requests

CITIES = ('Sydney', 'Alicante')
API_KEY = os.environ.get('WEATHER_API')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q='

# API docs: http://openweathermap.org/current
URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'

rtime = lambda x: time.strftime("%H:%M:%S (%Z)", time.localtime(x))

def get_weather(cities=CITIES):
    fmt = 'In {} the weather is: {}, today sun rises at {} and sets at {}'

    output = []
    for city in cities:
        resp = requests.get(URL.format(city, API_KEY))
        info = resp.json()
        main = info["weather"][0]["main"]
        sunrise = rtime(info["sys"]["sunrise"])
        sunset = rtime(info["sys"]["sunset"])
        output.append(fmt.format(city, main, sunrise, sunset))

    return '\n'.join(output)


if __name__ == '__main__':
    print(get_weather())
