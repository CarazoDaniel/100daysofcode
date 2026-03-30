import os
import requests
from dotenv import load_dotenv
load_dotenv() 


class NotificationManager:
    def __init__(self):
        self.telegram_bot_chat_id = os.environ["BOT_CHAT_ID"]
        self.telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        
    def send_notification(self,city,price):
        message = f"There is a flight under a price you set! get a 2 week vacation in 2 weeks in {city} for {price}"
        param_telegram = {
            "text" : message,
            "chat_id": self.telegram_bot_chat_id
        }
        tele_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        telegram_message = requests.post(url=tele_url,params=param_telegram)
        telegram_message.raise_for_status()
