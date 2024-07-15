import requests
import flask
import awscli
import selenium
import json


url = f"https://api.github.com/users/avielb/repos"
response = requests.get(url)
data = response.json()
formatted_json = json.dumps(data, indent=4)
#    print("API Response:")
#    print(api_key)
print(formatted_json)
# print(data)
if response.status_code == 200 and data['result'] == 'success':
    # print("github is up")

    for repo in data:
        if "devops" in str(repo["name"]).lower():
            print(repo["name"])
