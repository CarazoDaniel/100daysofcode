import requests
import html
from datetime import datetime

X_APP_ID = "app_e2b410fc13df473ab0161971"
X_APP_KEY = ""

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY
}

query_params = {
    "query": input("Tell me what you did: "),
    "weight_kg": 72,
    "height_cm": 173,
    "age": 32, 
    "gender": "male"
}

response = requests.post(url=url, headers=headers, json=query_params)
data = response.json()


now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

url_sheety = ''

shee_header = {
    "Authorization"
}

for excersise in data["exercises"]:
    shee_params = {
        "workout": {
            "date":date,
            "time":time,
            "exercise": excersise["name"].title(),
            "duration": excersise["duration_min"],
            "calories": excersise["nf_calories"]
        }
    }

    new_response = requests.post(url=url_sheety, headers=shee_header,json=shee_params)
    print(new_response.text)
