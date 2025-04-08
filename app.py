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
'''
@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"

        try:
            response = requests.get(url)
            result = response.json()

            if "location" in result and "current" in result:
                data = result
            else:
                error = f"City '{city}' not found. Please try again."

        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template("index.html", data=data, error=error)
    '''

@app.route('/data',methods=["GET", "POST"])
def data():
    
    city = request.args.get("city", "delhi")
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    weather_data = response.json()

    return weather_data
    




if __name__ == "__main__":
    app.run(debug=True)
