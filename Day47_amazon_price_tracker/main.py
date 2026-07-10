import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv() 

email_account = os.environ["GMAIL_EMAIL"]
email_api_key = os.environ["GMAIL_API_KEY"]
smtp_address = os.environ["SMTP_ADDRESS"]
user_mail = os.environ["USER_MAIL"]


#to work with inputs
#item = input("paste the item link you wish to be tracked: ")
#target = float(input("set the thershold price you want to be notified for: "))

#brewery
#target=100
#URL="http://appbrewery.github.io/instant_pot/"

target = 157000
URL="https://www.amazon.com/Garmin-Forerunner%C2%AE-Smartwatch-Advanced-Training/dp/B0H1F27RNT?ref_=ast_sto_dp&th=1"

# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": 'en-US,en;q=0.9',
#     "Dnt": "1",
#     "Priority": "u=0, i",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "'Windows'",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
#     }

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL,headers=header)
item_site = response.text

soup = BeautifulSoup(item_site,'html.parser')
#breweery version
#attribute = soup.find(name= "span", class_= "a-offscreen",).getText()  
#item_title = soup.find(name="span", class_= "a-size-large product-title-word-break", id= "productTitle").getText()

#amz live version
attribute = soup.find(name= "span", class_= "a-offscreen").getText()
item_title = soup.find(name="span", class_= "a-size-large product-title-word-break", id= "productTitle").getText()

#item_price = float(attribute.split("$")[1])
item_price = float(attribute.split("CRC")[1].replace(',',''))
print(item_title)
print(item_price)

if item_price < target:
    with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=email_account, password=email_api_key)
            connection.sendmail(from_addr=email_account,
                            to_addrs=user_mail,
                            msg= f"Subject:Amazon Price Alert!\n\n{item_title} is now at {attribute}.\nUnder the set target of CRC{target}.\n If you still want to grab the item: {URL}".encode("utf-8"))