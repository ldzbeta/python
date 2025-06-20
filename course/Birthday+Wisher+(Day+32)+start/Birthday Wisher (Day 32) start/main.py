import datetime as dt
from random import choice
import smtplib
now = dt.datetime.now()
day = now.weekday()

if day==1: # Tuesday
    with open("quotes.txt","r") as file:
        quotes=file.readlines()

    rand=choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="myemail@gmail.com",password="password")
        connection.sendmail(from_addr="myemail",to_addrs="reciever",msg=rand)