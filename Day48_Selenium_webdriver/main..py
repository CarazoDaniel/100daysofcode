from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')

events = {  n : {'time': event_dates[n].text,"name":event_names[n].text,} for n in range(len(event_names))}

print(events)
# driver.close() # to close the tab only
#driver.quit()