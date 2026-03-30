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
deals_message = ""

## completing IATA CODES for selected cities
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"],row["countryCode"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Searching price updates for flights
for row in sheet_data:
    row["searchPrice"] = flight_data.search_flight(DEPARTURE_CITY,row["iataCode"])
data_manager.destination_data = sheet_data
data_manager.update_flight_prices()
# adding city and price to the message for notification
for row in sheet_data:
    if row["searchPrice"] != "NA" and row["searchPrice"] <= row["lowestPrice"]:
        deals_message += f"How about {row['city']}, for {row['searchPrice']}\n"

#if there are modifications to the message (deals found), notifying clients that signed up

if deals_message != "":
    from notification_manager import NotificationManager
    notification_manager = NotificationManager()
    client_data = data_manager.get_contact_info()
    for row in client_data:
        notification_message = f"Hello {row['lastName']} {row['firstName']},\n In 2 weeks time, you could be enojying a vacation, the following deals are available:\n {deals_message}"
        notification_manager.send_email_notification(row['email'],notification_message)
    notification_manager.send_bot_notification(deals_message)