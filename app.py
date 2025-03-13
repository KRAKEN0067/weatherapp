from flask import Flask, request, jsonify, redirect, render_template, url_for
import requests


app=Flask(__name__)

API_KEY = 'fdefa49a9beb466cb51123204251103'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'


@app.route('/', methods=['GET','POST'])
def get_weather():
    
        form_city = request.form.get('city')
        #city = request.args.get("city", form_city)
        url = f"{BASE_URL}?key={API_KEY}&q={form_city}&aqi=no"
        response = requests.get(url)
        weather_data = response.json()
        return render_template('index.html', data=weather_data)

@app.route('/data',methods=["GET", "POST"])
def data():
    
    city = request.args.get("city", "delhi")
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    weather_data = response.json()

    return weather_data
    




if __name__ == "__main__":
    app.run(debug=True)
