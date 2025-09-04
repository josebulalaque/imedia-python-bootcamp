import requests

# Send a GET request to a free joke API
site = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(site)

# Check if the request was successful
if response.status_code == 200:
    joke = response.json()
    print(joke['setup'])
    print(joke['punchline'])
else:
    print("Failed. Server said:", response.status_code)
