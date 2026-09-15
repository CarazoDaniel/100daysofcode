from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import os


ACCOUNT_EMAIL = "drealicious@test.com"
ACCOUNT_PASSWORD = "testpassed"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, timeout=2)

login_btn = wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
login_btn.click()

email_input = wait.until(ec.presence_of_element_located((By.ID,"email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID,"password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.ID,"submit-button")
submit_btn.click()


wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

day_groups = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")

## counters
booked_count = 0
waitlist_count = 0
already_booked_count = 0

new_bookings = []
new_waitlists = []
booked_waitlisted = []

for day in day_groups:
    #get the day title
    day_title = day.find_element(By.TAG_NAME, "h2").text
    #check for tuesday
    if "Tue" in day_title or "Thu" in day_title:
        classes_in_day = day.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
        for each in classes_in_day:
            time = each.find_element(By.CSS_SELECTOR, "p[id^='class-time']").text
            if "6:00 PM" in time:
                name = each.find_element(By.CSS_SELECTOR, "h3[id^='class-name']").text
                button = each.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

                if button.text == "Booked":
                    print(f"Already booked: {name} on {day_title}")
                    already_booked_count +=1
                    booked_waitlisted.append(f"Already booked: {name} on {day_title}")
                elif button.text == "Waitlisted":
                    print(f"Already on waitlist: {name} on {day_title}")
                    already_booked_count +=1
                    booked_waitlisted.append(f"Already waitlisted: {name} on {day_title}")
                elif button.text == "Book Class":
                    # Book the class
                    button.click()
                    print(f"Managed to book: {name} {time} on {day_title}")
                    booked_count +=1
                    new_bookings.append(f"Booked {name} {time} on {day_title}")
                    
                elif button.text == "Join Waitlist":
                    # Join waitlist if class is full
                    button.click()
                    print(f"Waitlisted for: {name} on {day_title}")
                    waitlist_count +=1
                    new_waitlists.append(f"Waitlisted for:{name} {time} on {day_title}")
            
#print all stats     
print(f"BOOKING SUMMARY\n\nBOOKED:{booked_count}\nWAITLISTED:{waitlist_count}\nALREADY PROCESSED{already_booked_count}\nTOTAL PROCESSED:{booked_count+waitlist_count+already_booked_count}")
print(f"LIST OF CLASSES\n\n {new_bookings}\n{new_waitlists}\n{booked_waitlisted}")

driver.find_element(By.ID, "my-bookings-link").click()

try:
    booked_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking']")
    schedule_bookings = 0
    for card in booked_cards:
        name = card.find_element(By.CSS_SELECTOR,"h3").text
        time = card.find_element(By.CSS_SELECTOR,"p").text
        if ("6:00 PM" in time) and ("Tue" in time or "Thu" in time):
            schedule_bookings +=1
except NoSuchElementException:
    print("No Bookings")
    
try:
    waitlist_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist']")
    schedule_waits = 0
    for card in waitlist_cards:
        name = card.find_element(By.CSS_SELECTOR,"h3").text
        time = card.find_element(By.CSS_SELECTOR,"p").text
        if ("6:00 PM" in time) and ("Tue" in time or "Thu" in time):
            schedule_waits +=1
except NoSuchElementException:
    print("No waitlists")
    
print(f'bookings page shows {schedule_bookings} bookings done and {schedule_waits} waitlists')