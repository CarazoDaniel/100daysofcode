##################### Extra Hard Starting Project ######################
from random import choice
import pandas
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
people = pandas.read_csv("./birthdays.csv")
birthdays = people.to_dict(orient="records")

email = "test@gmail.com"
pwd = ""
 
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.date.today()
day = now.day
month = now.month

for n in birthdays:
    if day == n["day"] and month == n["month"]:
        chosen_one = choice(range(1,4))
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        with open(f"./letter_templates/letter_{chosen_one}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", n["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=pwd)
            connection.sendmail(from_addr=email,
                            to_addrs=n["email"],
                            msg= f"Subject:Happy Birthday\n\n{letter}")

# 4. Send the letter generated in step 3 to that person's email address.




