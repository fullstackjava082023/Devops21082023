import requests



def get_character_by_id(id):
    # Define the API endpoint URL
    api_url = f"https://thronesapi.com/api/v2/Characters/{id}"
    response = requests.get(api_url)
    json_response = response.json()
    # print(json_response)
    #get the full name
    full_name = json_response["fullName"]
    print(full_name)

def post_character(data):
    response = requests.post("https://thronesapi.com/api/v2/Characters", json=data)
    print(response.status_code)

def save_character_image(id):
    #get the character by id
    response = requests.get(f"https://thronesapi.com/api/v2/Characters/{id}")
    # get the json from responce as python dictionary
    json_response = response.json()
    # take the image url
    image_url = json_response["imageUrl"]
    #get the actual image from url:
    image = requests.get(image_url)
    # create image file name
    image_file_name = json_response["image"]
    with open(image_file_name, 'wb') as file:
        # write the binary content into the file
        file.write(image.content)


def main():

    save_character_image(51)
    # post_character(data)
    # get_character_by_id(35)


if __name__ == '__main__':
    main()