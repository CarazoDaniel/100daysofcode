import os
import requests
from datetime import datetime

url = "https://pixe.la/v1/users"

PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_header = {
    "X-USER-TOKEN":PIXELA_TOKEN
}

# user_params = {
#     "token" : PIXELA_TOKEN,
#     "username": PIXELA_USER,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url=url, json=user_params)
FIRST_ID = "ralph1"
graph_params = {
    "id":FIRST_ID,
    "name":"Runna",
    "unit":"Km",
    "type":"float",
    "color":"momiji",
    "startOnMonday":True
}

#response = requests.post(url=f"{url}/{PIXELA_USER}/graphs",headers=pixela_header,json=graph_params)
today = datetime.now()

pixel_param={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2"
}
response = requests.post(url=f"{url}/{PIXELA_USER}/graphs/{FIRST_ID}",headers=pixela_header,json=pixel_param)
print(response.text)
