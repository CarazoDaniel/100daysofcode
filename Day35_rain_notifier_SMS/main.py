import os
import requests
from twilio.rest import Client

TWILI_ACC = os.environ.get("TWILI_ACC")
DCA_PHONE = os.environ.get("DCA_PHONE")
TIWLI_AUTH = os.environ.get("TIWLI_AUTH")
OWM_KEY = os.environ.get("OWM_KEY")

api_key = OWM_KEY
account_sid = TWILI_ACC
auth_token = TIWLI_AUTH

client = Client(account_sid, auth_token)


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

count = 4
api_params ={
    "lat": 9.942369,
    "lon": -84.015112,
    "cnt": count,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=api_params)
response.raise_for_status()

data = response.json()
data = data["list"]
rain = False
for i in range(count):
     if int(data[i]["weather"][0]["id"]) < 700:
        rain = True

        
        
day_weather = data[0]["weather"][0]["id"]

if rain:
    print(rain)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='',
    content_variables='{"1":"It will rain today","2":"Do not forget your umbrella"}',
    to=f'whatsapp:+{DCA_PHONE}'
    )  