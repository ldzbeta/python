import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()
shitty_endpoint = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.__user= os.environ["SHEETY_USRERNAME"]
        self.__password=os.environ["SHEETY_PASSWORD"]
        self.__autherization = HTTPBasicAuth(self.__user,self.__password)
        
    def get_destination_data(self):
        self.response = requests.get(url=shitty_endpoint,auth=self.__autherization)
        self.data = self.response.json()["prices"]
        return self.data
    
    def update_destination_codes(self):
        for item in self.data:
            config = {
                "price":{
                    "iataCode":item["iataCode"],
                }
            }
            response = requests.put(url=f"{shitty_endpoint}/{item["id"]}",json=config,auth=self.__autherization)
            # print(response.text)
            response.raise_for_status()
