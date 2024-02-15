import requests
import json

response = requests.get('https://random-data-api.com/api/v2/users')
data = json.loads(response.text)

print(f"First Name: {data.get('first_name')}")
print(f"Last Name: {data.get('last_name')}")
print(f"Username: {data.get('username')}")
print(f"Email: {data.get('email')}")
