from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import smtplib
import requests

import os
from dotenv import load_dotenv
load_dotenv()
from time import sleep

GOOGLE_FORM = os.environ["GOOGLE_FORM"]
ZILLOW_LINK = os.environ["ZILLOW_LINK"]

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(ZILLOW_LINK,headers=header)
item_site = response.text

soup = BeautifulSoup(item_site,'html.parser')

list = soup.find_all(name= "li", class_= "ListItem-c11n-8-84-3-StyledListCardWrapper")

#item_title = soup.find(name="span", class_= "a-size-large product-title-word-break", id= "productTitle").getText()

list_of_links = [ link['href'] for link in soup.find_all(name = "a" , class_="property-card-link", href = True)]

list_of_prices = [price.getText() for price in soup.find_all(name = "span" , class_="PropertyCardWrapper__StyledPriceLine")]
list_of_prices = [price.replace("+",'') for price in list_of_prices]

list_of_address = [address.getText() for address in soup.find_all(name = "address")]

print(list_of_address)
print(list_of_links)
print(list_of_prices)