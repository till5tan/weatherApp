# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = '484006a6e532caa8074e85bfb72ed286'

# Example list of 150 cities for weather forecast
cities = [
    'London', 'New York', 'Tokyo', 'Paris', 'Beijing', 'Sydney', 'Moscow', 'Dubai', 'Rio de Janeiro', 'Toronto',

    'Berlin', 'Astana', 'Los Angeles', 'Mumbai', 'Seoul', 'Shanghai', 'Singapore', 'Toronto', 'Almaty', 'Taipei',
    # Add more cities here...
]

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=484006a6e532caa8074e85bfb72ed286'
    response = requests.get(url)
    data = response.json()

    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
    }

    return weather

@app.route('/')
def index():
    weather_data = [get_weather(city) for city in cities]
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
