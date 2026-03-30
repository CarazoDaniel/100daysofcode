import requests
import os
import html
#Stock names
STOCK = "AAPL"
NAME = "Apple"
STOCK1 = "PLTR"
NAME1 = "Palantir"
STOCK2 = "NVDA"
NAME2 = "Nvidia"


#get keys from the env variables
NEWS_KEY = os.environ.get("NEWS_KEY")
AVANTAGE_KEY = os.environ.get("AVANTAGE_KEY")

#Telegram
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_ID = os.environ.get("TELEGRAM_ID")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

vantage_params={
     "function": "TIME_SERIES_DAILY",
     "symbol": STOCK,
     "apikey": AVANTAGE_KEY
 }
VANTAGE_API = "https://www.alphavantage.co/query"

vantage_request = requests.get(f"{VANTAGE_API}", params= vantage_params)
vantage_request.raise_for_status()

data = vantage_request.json()
data = data["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]


yesterday_data = float(data_list[0]["4. close"])
before_yesterday_data = float(data_list[1]["4. close"])

price_delta = ((before_yesterday_data-yesterday_data)/yesterday_data) *100
abs_delta = abs(price_delta)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if abs_delta > 5:
    NEWS_API = "https://newsapi.org/v2/everything"
    news_params = {
        "qInTitle":NAME,
        "page": 3,
        "pageSize":3,
        "apiKey": NEWS_KEY,
    }
    news_request = requests.get(NEWS_API,params=news_params)
    news_request.raise_for_status()
    data = news_request.json()
    data = data["articles"]
    for arts in data:
        headline = arts["title"]
        description_text = html.unescape(arts["description"])
        
        message = f"{NAME}: {round(price_delta,3)}%\nHeadline: {headline}\nBrief: {description_text}"
        param_telegram = {
            "text" : message,
            "chat_id": TELEGRAM_ID
        }
        tele_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        telegram_message = requests.get(url= tele_url,params=param_telegram)
        telegram_message.raise_for_status()





## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 




# print(message.sid)


# Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

