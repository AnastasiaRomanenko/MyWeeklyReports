import requests

response = requests.get('https://httpbin.co/anything')
print(response.text)