import os
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv() 


class NotificationManager:
    def __init__(self):
        self.telegram_bot_chat_id = os.environ["BOT_CHAT_ID"]
        self.telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
        self._email_account = os.environ["GMAIL_EMAIL"]
        self._email_api_key = os.environ["GMAIL_API_KEY"]
    # telegram notifier 
    def send_bot_notification(self,custom_message):
        message = custom_message
        param_telegram = {
            "text" : message,
            "chat_id": self.telegram_bot_chat_id
        }
        tele_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        telegram_message = requests.post(url=tele_url,params=param_telegram)
        telegram_message.raise_for_status()
        
    def send_email_notification(self,notification_email,custom_message):
        """
        This is the email notifier, it takes a str with the expected message, and email str to send. This could construct a single message, but that adds extra steps of communication.
        """
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self._email_account, password=self._email_api_key)
            connection.sendmail(from_addr=self._email_account,
                            to_addrs=[notification_email],
                            msg= f"Subject:This is your 2 week flight deal notification!\n\n{custom_message}")

