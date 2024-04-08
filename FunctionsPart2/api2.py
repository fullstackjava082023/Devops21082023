import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
json_response = response.json()
joke = json_response["value"]

print(joke)