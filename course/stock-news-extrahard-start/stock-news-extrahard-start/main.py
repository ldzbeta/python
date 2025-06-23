import requests
import datetime
# from twilio.rest import Client
import math

account_id =""
auth_token =""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_API_KEY="S5WZG7QKKRMDUDL9"
NEWS_API = "96d5296e6c054cec8e2851dd984fca8f"

stock_url = 'https://www.alphavantage.co/query'
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHAVANTAGE_API_KEY,
}

response = requests.get(stock_url,params=stock_params)
data = response.json()
data_list = [value for (key,value) in data.items()]
today=float(list(data["Time Series (Daily)"].items())[:2][0][1]["4. close"])
yesterday=float(list(data["Time Series (Daily)"].items())[:2][1][1]["4. close"])
# print(data_list)
# today = float(data_list[0]["4. close"])
# yesterday = float(data_list[1]["4. close"])
rate = ((today-yesterday)/today )*100 
if -5<=rate<=5:
    news_params={
        "qInTitle":"Tesla",
        "apiKey":NEWS_API
    }
    news_response = requests.get("https://newsapi.org/v2/everything",params=news_params)
    news_articles=news_response.json()["articles"][:3]
    
    message = "TSLA: "
    if rate>0:
        message+=f"🔺{math.floor(rate)}%\nHeadline: "
    else :
        message+=f"🔻{math.floor(rate)}%\nHeadline: "

    for article in news_articles:
        message+=article["title"]

    print(message)
#     client = Client(account_id,auth_token)
#     message = client.messages .create(body=message,from="sender's phone no",to="reciever")
# print(message.status)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

