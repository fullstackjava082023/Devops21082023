import requests
from PIL import Image
from io import BytesIO
def get_todos():
    #json placeholder api
    # response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    # football api
    # response = requests.get('https://api.football-data.org/v4/competitions/')
    #game of thrones api
    #characters..
    # response = requests.get('https://thronesapi.com/api/v2/Characters/45')
    # continents
    # response = requests.get('https://thronesapi.com/api/v2/Continents')
    #download image of character 4
    response = requests.get('https://thronesapi.com/api/v2/Characters/8')
    json_response = response.json()
    # print(json_response["imageUrl"])
    # Send a GET request to the URL
    image = requests.get(json_response["imageUrl"])
    with open(f"{json_response['fullName']}.jpg", "wb") as f:
        # Write the binary content of the response to the file
        f.write(image.content)

    json_response = response.json()
    print(json_response)
    status = response.status_code
    print(status)
    # title = json_response["title"]
    # print(title)

def save_character_image(id):
    # get the character from the thrones API
    response = requests.get(f'https://thronesapi.com/api/v2/Characters/{id}')
    # extract the json from the response (python dictionary)
    json_response = response.json()
    # take the image url from the json respone:
    image_url = json_response["imageUrl"]
    # Send a GET request to the image URL to get the image from internet
    image = requests.get(image_url)
    # take character name from json_response
    character_name = json_response['fullName']
    # create a new filename based on the characters name
    image_file_name = f"{character_name}.jpg"
    # open file for write binary (when we write image and not text)
    with open(image_file_name, "wb") as f:
        # Write the binary content of the response to the file
        f.write(image.content)

def post_character(id):
    # Data to send in the POST request
    data = {
        "id": id,
        "firstName": "ilia",
        "lastName": "df",
        "fullName": "fsdfs",
        "title": "strisdng",
        "family": "fsd",
        "image": "strifsdng",
        "imageUrl": "strfsding"
    }
    response = requests.post('https://thronesapi.com/api/v2/Characters', json=data)
    print(response.status_code)





def randomFox():
    response = requests.get('https://randomfox.ca/floof/')
    json_response = response.json()
    image_link = json_response["image"]
    print(json_response)
    image = requests.get(image_link)
    im = Image.open(BytesIO(image.content))
    im.show()


def main():
    # get_todos()
    post_character(0)
    # randomFox()
    # extract_text()

def extract_text():
    import json
    json_text = '{"name": "John", "age": 30, "city": "New York"}'
    data = json.loads(json_text)
    print(data["city"])


if __name__ == '__main__':
    main()