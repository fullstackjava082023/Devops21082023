import requests

def get_random_joke():
    # Define the API endpoint URL
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)
    json_response = response.json()
    # get the joke (value )
    joke = json_response["value"]
    print(joke)


def chuck_jokes(num):
    for i in range(num):
        get_random_joke()


def main():
    # get_random_joke()
    chuck_jokes(5)


if __name__ == '__main__':
    main()


