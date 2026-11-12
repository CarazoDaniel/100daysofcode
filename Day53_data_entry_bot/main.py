from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
list_of_prices = [price.replace("$",'') for price in list_of_prices]
list_of_prices = [price.replace("/mo",'') for price in list_of_prices]
list_of_prices = [price.replace(" 1 bd",'') for price in list_of_prices]
list_of_prices = [price.replace(" 1bd",'') for price in list_of_prices]

list_of_prices = [price.replace(" 2 bd",'') for price in list_of_prices]
list_of_prices = [price.replace(" 2bd",'') for price in list_of_prices]

list_of_prices = [price.replace(" 3 bd",'') for price in list_of_prices]
list_of_prices = [price.replace(" 3bd",'') for price in list_of_prices]

list_of_prices = [price.replace(",",'') for price in list_of_prices]


list_of_address = [address.getText().strip() for address in soup.find_all(name = "address")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, timeout=2)

count = len(list_of_address)

for index in range(count+1):
    sleep(2)
    driver.get(GOOGLE_FORM)
    
    inputs = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,".whsOnd.zHQkBf")))

    address_input = inputs[0]
    address_input.clear()
    address_input.send_keys(list_of_address[index])
    
    price_input = inputs[1]
    price_input.clear()
    price_input.send_keys(list_of_prices[index])
    
    link_input = inputs[2]
    link_input.clear()
    link_input.send_keys(list_of_links[index])
    
    submit_button = driver.find_element(By.CSS_SELECTOR, ".NPEfkd.RveJvd.snByac")
    submit_button.click()