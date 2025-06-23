import requests

create_user_url="https://pixe.la/v1/users"
user_params={
    "token":"unknownnwonknu",
    "username":"unknown1010",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.put(url=create_user_url,json=user_params)
print(response)
print(response.text)