# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# # Import exceptions
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# import os
# from time import sleep

# PROMISED_DOWN = 1000
# PROMISED_UP = 1000
# Y_EMAIL = ""
# Y_PASSWORD = ""
# Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
# TESTING_URL = "https://www.speedtest.net/"



# class InternetSpeedTwitterBot:
#     def __init__(self,driver_options):
#         self.driver = webdriver.Chrome(driver_options)
#         self.up = 0
#         self.down = 0

#     def get_internet_speed(self):
#         self.driver.get(TESTING_URL)
#         wait = WebDriverWait(self.driver, timeout=2)
#         sleep(3)
#         test_btn = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')))
#         test_btn.click()
#         sleep(240)
#         try:
#             pop_up_close_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button")
#             pop_up_close_button.click()
#         except NoSuchElementException:
#             print("no btn x")
            
#         speed = self.driver.find_elements(By.CLASS_NAME,"py-2 font-mono text-5xl MuiBox-root css-s31qlv")
#         self.up = speed[0].text
#         self.down = speed[1].text
#         print(speed)
#         print(f'{self.up}  ,   {self.down}')


#     def tweet_at_provider(self):
        # self.driver.get(Y_LOGIN_URL)
        # time.sleep(2)

        # self.driver.find_element(By.NAME, value="username").send_keys(Y_EMAIL)
        # password = self.driver.find_element(By.NAME, value="password")
        # password.send_keys(Y_PASSWORD)
        # password.send_keys(Keys.ENTER)

        # time.sleep(3)
        # tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Post text"]')
        # tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        # tweet_compose.send_keys(tweet)

        # time.sleep(2)
        # tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        # tweet_button.click()

        # time.sleep(2)
        # self.driver.quit()


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# bot = InternetSpeedTwitterBot(chrome_options)
# bot.get_internet_speed()
# #bot.tweet_at_provider()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = "your_email"
Y_PASSWORD = "copy_password_from_y_admin_dashboard"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


class InternetSpeedYBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, value=".start-button a").click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        time.sleep(2)

        self.driver.find_element(By.NAME, value="username").send_keys(Y_EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(Y_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Post text"]')
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        tweet_compose.send_keys(tweet)

        time.sleep(2)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedYBot()
bot.get_internet_speed()
bot.tweet_at_provider()