import requests
import json
import pprint

url = "http://api.tvmaze.com/singlesearch/shows"
params = {"q": "Heart"}

response = requests.get(url,params)
if response.status_code == 200:
    data = json.loads(response.text)
    pprint.pprint(data)
