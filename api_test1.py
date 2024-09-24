import requests
import json


def api_data():
    url = "http://api.open-notify.org/astros"

    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        txt = json.dumps(data,sort_keys=True,indent=4)
        print(txt)
    else:
        print("Failed to retrieve data")


api_data()
