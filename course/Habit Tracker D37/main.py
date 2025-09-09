import requests
import datetime as dt
USERNAME="unknown1010"
TOKEN="unknownnwonknu"
GRAPH_ID="graph1"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":"unknownnwonknu",
    "username":"unknown1010",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"seconds",
    "type":"float",
    "color":"sora"
}

headers={
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

update_graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
date = dt.datetime.now().date().strftime('%Y%m%d')
# print(type(date))
update_graph_config={
    "date":date,
    "quantity":"3600"
}
response = requests.post(url=update_graph_endpoint,json=update_graph_config,headers=headers)
print(response.text)