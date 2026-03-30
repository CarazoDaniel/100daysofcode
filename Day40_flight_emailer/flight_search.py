import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class FlightSearch:
    def __init__(self):
        self._air_labs_key = os.environ["AIR_LABS_KEY"]
        self._air_labs_url = os.environ["AIR_LABS_URL"]
        self.cities_params = {
        'api_key': self._air_labs_key,
        '_fields': 'name,city_code'
        }
        self.response = requests.get(url=self._air_labs_url,json=self.cities_params)
        self.response = self.response.json()
        
    def get_destination_code(self, city_name, country_code):
            
        try:
             for city in self.response["response"]:
                 if city["name"] == city_name and city["country_code"] == country_code:
                     code = city["city_code"]
                     print(code)
                     return(code)
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
    
