import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

item_link = "https://www.amazon.in/ASUS-Vivobook-Metallic-Windows-S3407CA-LY057WS/dp/B0F9YGSK6L/ref=s9_acsd_al_ot_c2_x_2_t?_encoding=UTF8&pf_rd_t="

my_email = os.environ.get("MY_EMAIL")
app_password = os.environ.get("APP_PASSWORD")
reciever = os.environ.get("RECIEVER")

headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Amz-Currency-Code": "INR" 
  }
# https://httpbin.org/headers

response = requests.get(url=item_link,headers=headers)
site_html = response.text


def amazonScrapper():
    soup = BeautifulSoup(site_html, "html.parser")
    product_title = soup.select_one(selector="#title #productTitle").getText().strip()
    price = soup.select_one(selector=".a-price .a-price-whole").getText()
    price = float("".join(price.split(",")))
    print(price,product_title)

def flipkartScrapper():
    soup = BeautifulSoup(site_html, "html.parser")
    product_title=soup.select_one(selector="VU-ZEz")
    price=soup.select_one(selector=".Nx9bqj .CxhGGd")
    price=float(price.replace('₹', '').replace(',', ''))
    print(price,product_title)

# target = 10000

# if price < target:
#     print("Triggering email service")
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=app_password)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs=reciever,
    #         message=f"subject:Amazon Offer\n\n Hey you have a new offer on {product_title} \n Link:{item_link}"
    #     )
