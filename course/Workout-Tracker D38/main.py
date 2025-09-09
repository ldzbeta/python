import requests
from datetime import datetime
import os
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
nutrionix_endpoint = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{nutrionix_endpoint}/v2/natural/exercise"

# env APP_ID="c10b0f9e"
# API_KEY ="e45551ffe3e423ebd926395f1c595783"
# BEARER_TOKEN=""
# SHEETY_ENDPOINT = "https://api.sheety.co/2cc98b00ea690c04e8efd1f741a20da1/myWorkoutsPython/workouts"

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

print(APP_ID,API_KEY,BEARER_TOKEN,sheety_endpoint)
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Autherization": f"Bearer {BEARER_TOKEN}"
}
params={
    "query":input("Tell me which exercise you did? "),
    "weight_kg": 67,
    "height_cm": 175,
    "age": 18
}
response = requests.post(url=exercise_endpoint,json=params,headers=headers)
data=response.json()
# print(data)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

# response_sheety = requests.post(url=sheety_endpoint,json=sheety_config)
# response_sheety.raise_for_status()
print(sheet_response.text)