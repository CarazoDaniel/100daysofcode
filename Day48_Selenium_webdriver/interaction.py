from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="form button")

name.send_keys("goosfraba")
last_name.send_keys("Bear")
email.send_keys("new@amazon.com")

button.click()