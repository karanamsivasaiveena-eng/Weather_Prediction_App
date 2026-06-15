from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "660a5dcd09d62cc729b9e642e7a6bc4e"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None

    if request.method == 'POST':
        city = request.form['city']

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'wind': data['wind']['speed']
            }
        else:
            error = "City not found. Please try again."

    return render_template('index.html', weather=weather, error=error)

# Deployment-ready run block
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)