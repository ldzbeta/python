##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas
import random
import smtplib
today = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")

try:
    matches = birthdays[birthdays.day==today.day & birthdays.month==today.month] #for pandas
    for _,row in matches.iterrows():
        with open(f"letter_templates/letter_{random.randint(1,3).txt}") as letter_file:
            letter = letter_file.read ()
            letter=letter.replace("[name]", row.name[0].strip())

            with smtplib.SMTP("smtp.gmail.com") as connection :
                connection.starttls()
                connection.login(user="email",password="password")
                connection.sendmail(from_addr="email",to_addrs="email",msg=letter)
except:
    pass