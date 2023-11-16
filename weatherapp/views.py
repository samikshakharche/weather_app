import os
from django.shortcuts import render, HttpResponse
import requests
import json
from datetime import datetime
from dotenv import main
main.load_dotenv


def index(request):
    return render(request, 'index.html')


def index(request):

    try:

        if request.method == 'POST':
            API_KEY = os.getenv('API_KEY')

            city_name = request.POST.get('city')

            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

            response = requests.get(url).json()

            current_time = datetime.now()

            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")

            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }

        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'index.html', context)

    except:
        return render(request, '404.html')
