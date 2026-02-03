import smtplib
from random import choice
import datetime as dt

# determine the day
day_of_week = dt.datetime.now()
day_of_week = day_of_week.weekday()
if day_of_week == 3:

    # importing the quotes
    with open("./quotes.txt") as file:
        quotes = file.readlines()
        
    #sending the email

    email = "test@gmail.com"
    pwd = ""
    with  smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=email, password=pwd)
        connection.sendmail(from_addr=email,
                            to_addrs="hiall@hotmail.com",
                            msg= f"Subject:Hello world\n\n{choice(quotes)}")
        print("sent email motivation")
        