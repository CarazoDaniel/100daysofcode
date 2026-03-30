#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
import os
from dotenv import load_dotenv
load_dotenv()

DEPARTURE_CITY = os.getenv("DEPARTURE_CITY")
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_data = FlightData()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"],row["countryCode"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for row in sheet_data:
    row["searchPrice"] = flight_data.search_flight(DEPARTURE_CITY,row["iataCode"])
data_manager.destination_data = sheet_data
data_manager.update_flight_prices()
for row in sheet_data:
    if row["searchPrice"] != "NA" and row["searchPrice"] <= row["lowestPrice"]:
        from notification_manager import NotificationManager
        notification_manager = NotificationManager()
        notification_manager.send_notification(row['city'],row["searchPrice"])