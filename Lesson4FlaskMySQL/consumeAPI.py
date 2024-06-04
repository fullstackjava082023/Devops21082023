import requests

url = 'http://localhost:5005/api/addCountry'
data = {
    'name': 'Slovakia'
}
response = requests.post(url, json=data)
print(response.json())
