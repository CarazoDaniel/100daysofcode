from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Import exceptions
from selenium.common.exceptions import ElementClickInterceptedException
import os
from time import sleep

PROMISED_DOWN = 1000
PROMISED_UP = 1000
NANSTA_EMAIL = ""
NANSTA_PASSWORD = ""
NANSTA_LOGIN_URL = "https://app.100daysofpython.dev/services/share-a-naan/welcome"
NANFLUENCER_NAME = "elaineducasse"



class NanstaFollwingBot:
    def __init__(self,driver_options):
        self.driver = webdriver.Chrome(driver_options)
        self.up = 0
        self.down = 0

    def log_in(self):
        self.driver.get(NANSTA_LOGIN_URL)
        wait = WebDriverWait(self.driver, timeout=2)
        sleep(2)
        email_input = wait.until(ec.presence_of_element_located((By.XPATH,'/html/body/div/aside/div/form/input[1]')))
        email_input.clear()
        email_input.send_keys(NANSTA_EMAIL)

        password_input = self.driver.find_element(By.XPATH, '/html/body/div/aside/div/form/input[2]')
        password_input.clear()
        password_input.send_keys(NANSTA_PASSWORD)
        
        log_btn = self.driver.find_element(By.XPATH, '/html/body/div/aside/div/form/button')
        log_btn.click()

    def remove_pop_ups(self):
        
        info_btn = self.driver.find_element(By.XPATH, '//*[@id="popup-save-login"]/div/div[2]')
        info_btn.click()
        sleep(1)
        notifications_btn = self.driver.find_element(By.XPATH, '//*[@id="popup-notifications"]/div/button[2]')
        notifications_btn.click()
        
    def find_followers(self,to_follow):
        search_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/nav/button')
        search_btn.click()
        
        sleep(1)
        
        following_input = self.driver.find_element(By.XPATH, '/html/body/aside/div[2]/input')
        following_input.clear()
        following_input.send_keys(to_follow)
        
        sleep(1)
        
        following_btn = self.driver.find_element(By.XPATH, "/html/body/aside/div[4]/a")
        following_btn.click()
        
        sleep(2)
        
        followers_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')
        followers_btn.click()
        
        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)
        

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                # An "Unfollow?" dialog opened (you already follow this account).
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

bot = NanstaFollwingBot(chrome_options)
bot.log_in()
sleep(5)
bot.remove_pop_ups()
sleep(3)
bot.find_followers(NANFLUENCER_NAME)
sleep(3)
bot.follow()
