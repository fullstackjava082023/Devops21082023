import requests
import faker

fake = faker.Faker()

def create_fake_country():
    url = 'http://localhost:5005/api/addCountry'
    data = {
        'name': fake.country()
    }
    response = requests.post(url, json=data)
    print(response.json())


def create_fake_airline():
    url = 'http://localhost:5005/api/addAirline'
    data = {
        'Name': fake.company(),
        'Country_Id': fake.random_digit()  #1-9
    }
    print(data)
    response = requests.post(url, json=data)
    print(response.json)


create_fake_airline()
create_fake_airline()