import requests

url = "https://api.apilayer.com/fixer/convert?to=PLN&from=EUR&amount=10"

headers= {
  "apikey": "my_apikey"
}
apikey = "my_apikey"

from_currency = input("From: ")
to_currency = input("To: ")
amount = input("Amount: ")
while not from_currency or not to_currency or not amount:
    print("Enter fields correctly")
    from_currency = input("From: ")
    to_currency = input("To: ")
    amount = input("Amount: ")
while not amount.isdigit():
    print("Amount needs to have a numeric value")
    amount = input("Amount: ")

url = "https://api.apilayer.com/fixer/convert?" + f"to={to_currency}&from={from_currency}&amount={amount}&apikey={apikey}"
print(url)
response = requests.request("GET", url, headers=headers)
