import os
import requests
from pprint import pprint
from datetime import datetime
amadeus_endpoint = "https://test.api.amadeus.com/vl"
city_search_endpoint = f"{amadeus_endpoint}/reference-data/locations/cities"
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
flight_endpoint = f"{amadeus_endpoint}/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key=os.environ["FLIGHT_API_KEY"]
        self._api_secret=os.environ["FLIGHT_API_SECRET"]
        self._token=self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)
        return response.json()["access_token"]

    def get_destination_code(self,city):
        params={
            "keyword":city,
            "max": "2",
            "include": "AIRPORTS",
        }
        headers = {"Authorization": f"Bearer {self._token}"}
        response = requests.get(url=city_search_endpoint,params=params,headers=headers)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        params={
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=flight_endpoint,params=params,headers=headers)

        return response.json()
