import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("API Key is missing")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
            }
        else:
            return {"error": f"City not found or API error: {data.get('message', 'Unknown error')}"}
    except Exception as e:
        return {"error": "Failed to connect to Weather Service."}

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        try:
            weather_data = get_weather(city)
        except ValueError as ve:
            weather_data = {"error": str(ve)}
    
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=False) 