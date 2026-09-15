from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Import exceptions
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from time import sleep

TINDOG_URL = "https://app.100daysofpython.dev/services/tindog/u/yp-wYDk1TF0eVcTPZt3nWr7SkI2iTPdV"
ACCOUNT_EMAIL = "exampledoggy@newmail.com"
ACCOUNT_PASSWORD = "YourPasswordIsSafe"
ALLOWED_SWIPES = 20

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
#chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(TINDOG_URL)
wait = WebDriverWait(driver, timeout=2)

sleep(2)

login_btn = wait.until(ec.element_to_be_clickable((By.XPATH,"/html/body/header/button")))
login_btn.click()

sleep(2)

fb_btn =  wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="login-modal"]/div/div/div/button[1]')))
fb_btn.click()

sleep(2)

#switching window to log in

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = wait.until(ec.presence_of_element_located((By.ID,"email")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID,"pass")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/button")
submit_btn.click()
sleep(2)

driver.switch_to.window(base_window)

sleep(2)

allow_btn = wait.until(ec.presence_of_element_located((By.XPATH,'//button[text()="Allow"]')))
allow_btn.click()
sleep(2)
notif_btn = wait.until(ec.presence_of_element_located((By.XPATH,'//button[text()="Not interested"]')))
notif_btn.click()
sleep(2)
coockie_btn = wait.until(ec.presence_of_element_located((By.XPATH,'//button[text()="I Accept"]')))
coockie_btn.click()

sleep(5)

for count in range(ALLOWED_SWIPES):
    try:
        like = driver.find_element(By.XPATH,'//*[@id="like-button-container"]/form/button')
        like.click()
    except NoSuchElementException:
        count -= 1
        sleep(5)
    except ElementClickInterceptedException:
        sleep(2)
        count -= 1
        back_to_swipe = driver.find_element(By.XPATH,'/html/body/main/div[3]/a')
        back_to_swipe.click()
    sleep(5)
