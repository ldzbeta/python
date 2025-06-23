import requests
from twilio.rest import Client
api_key = "dd62158f25118c01ddfd2ed03c879df1"
account_id =""
auth_token =""
params={
    "lat":75.25,
    "lon":11.56, 
    "appid":api_key,
    "cnt":4
}

response=requests.get("https://pro.openweathermap.org/data/2.5/forecast/hourly",params=params)
response.raise_for_status()
wheather_data = response.json()
will_rain = False
for hour_data in wheather_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain=True
        break

if will_rain :
     client = Client(account_id,auth_token)
     message = client.messages \
        .create(
            body="message",
            from="sender's phone no",
            to="reciever"
        )
print(message.status)
