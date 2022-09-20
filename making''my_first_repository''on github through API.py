import requests
import json

headers = {"Authorization": "token  52eebcb9a9ae320c10724a9093a5bb68c0c57442"} # generate token from https://github.com/settings/tokens
payload = {"description":"This is my first repository making through API.", "name": "MY_FIRST_REPOSITORY"} #describe name and small description about repository

response = requests.post("https://api.github.com/user/repos", json=payload,headers=headers)
print(response.status_code)
json_data = response.json()
print(json_data)
#patch request


payload = {"description":"Learning about requests!", "name":"learning-about-apis"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload, headers=headers)
status  = response.status_code
print(status)
