import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
# Get the latest conversion rate from USD to PHP

print(f"Current USD to PHP conversion rate: {data['rates']['PHP']}")

