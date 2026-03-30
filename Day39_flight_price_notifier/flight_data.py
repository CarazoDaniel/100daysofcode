import os
import serpapi
from datetime import datetime,timedelta
from dotenv import load_dotenv
load_dotenv() 

class FlightData:
    def __init__(self):
        self.serp_endpoint = os.environ["SERPAPI_ENDPOINT"]
        self.serp_api_key = os.environ["SERPAPI_KEY"]
        self.date_of_travel = datetime.date(datetime.now()+timedelta(weeks=2))
        self.date_of_return = datetime.date(datetime.now()+timedelta(weeks=4))
        self.flight_data = {}
    
    def search_flight(self,departure,arrival):
        self.serpapi_params = {
            "engine":"google_flights",
            "hl":"en",
            "currency":"USD",
            "departure_id":departure,
            "arrival_id":arrival,
            "outbound_date": self.date_of_travel,
            "return_date": self.date_of_return
        }
        call = serpapi.Client(api_key=self.serp_api_key)
        results = call.search(self.serpapi_params)
        try:
            best_flights = results["best_flights"]
        except KeyError:
            print(f'No flights found from {departure} to {arrival}')
            return 'NA'
        return float(best_flights[0]["price"])
