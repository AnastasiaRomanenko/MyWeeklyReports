import requests
import json

response = requests.get('http://httpbin.co/anything')
data = json.loads(response.text)
print(data['ip'])
