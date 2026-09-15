from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

#wait for the load

sleep(3)

try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")
    
sleep(3)

coockies = driver.find_element(by=By.ID, value="bigCookie")

item_ids = [f"product {i}" for i in range(18)]

wait_time = 3
timeout = time() + wait_time
five_min = time() + (60*6)

while True:
    coockies.click()
    
    # try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time
    
    
    
    if time() > five_min:
        try:
            coockies_element = driver.find_element(By.ID, value="cookiesPerSecond")
            print(f"final result: {coockies_element.text}")
        except NoSuchElementException:
            print("unable to count your coockies")
        break
    
    
    
    