from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Guess by adding your name to /guess/name</h1>"
    
@app.route("/guess/<guess>")
def guess_name(guess):
    
    response_gender = requests.get("https://api.genderize.io", params={"name": guess}).json()
    
    response_age = requests.get("https://api.agify.io", params={"name": guess}).json()

    age_guess = response_age["age"]
    gender_guess = response_gender['gender']
    
    return render_template("gender.html", guess_name= guess, age = age_guess, gender = gender_guess)                 

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
