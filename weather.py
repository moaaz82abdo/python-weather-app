import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather(city="cairo"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    return weather_data

    pprint(weather_data)
    
    
if __name__ == "__main__":
    print('\n***Get current weather conditions***\n'.upper())
    city = input('\nplease enter a city name\n')
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
    
   