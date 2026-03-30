import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES")
SHEETY_CLIENTS_ENDPOINT = os.getenv("SHEETY_CLIENTS")

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.contact_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        #pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
            
    def update_flight_prices(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "searchPrice": city["searchPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
    
    def delete_user(self,row):
        requests.delete(url=f'{SHEETY_CLIENTS_ENDPOINT}/{row}', auth=self._authorization)
    
    def get_contact_info(self):
        """
        This function will get the info from the clients sheet, and delete rows not containing a valid email, returning the 
        """
        import re
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        response = requests.get(url=SHEETY_CLIENTS_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.contact_data = data["clients"]
        row_number = 0
        row_id = 2
        for row in self.contact_data:
            if not(EMAIL_REGEX.fullmatch(row["email"])):
                self.delete_user(row_id)
                self.contact_data.pop(row_number)
            row_number +=1
            row_id +=1
        
        return self.contact_data


