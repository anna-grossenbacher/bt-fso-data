import json
import requests

url = "https://dam-api.bfs.admin.ch/hub/api/dam/events"
headers = {"accept": 'application/json'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json() #https://stackoverflow.com/questions/17518937/saving-a-json-file-to-computer-python
    with open("/workspaces/bt-fso-data/data/data_module1.json", "w") as f: #https://chat.openai.com/share/bc924175-726b-46c3-ba85-07ab1ef0b934
        json.dump(data, f)
else:
    print(f"Error: {response.status_code}")
