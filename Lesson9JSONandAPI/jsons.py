import json

def read_json_from_file():
    with open("example.json") as json_file:
        content = json_file.read()
        # print(type(content))
        # convert json to python dictionary
        python_content = json.loads(content)
        print(python_content)
        # print(python_content["number"])
        print(python_content["nestedObject"]["key2"])

def extract_city_from_file():
    with open("john.json") as json_file:
        content = json_file.read()
        # print(type(content))
        # convert json to python dictionary
        python_content = json.loads(content)
        print(python_content)
        # print(python_content["number"])
        print(python_content["city"])

def text_json():
    with open("john.json") as test1:
        content = test1.read()
        test_python = json.loads(content)
        print(test_python["city"])

def extract_city():
    json_text = '{"name": "John", "age": 30, "city": "New York"}'
    # change json to dictionary
    dict = json.loads(json_text)
    print(dict["city"])


def main():
    # read_json_from_file()
    # extract_city()
    # extract_city_from_file()
    # text_json()
    # print(json.dumps({"name": "John", "age": 30}))
    # print(json.dumps(["apple", "bananas"]))
    # print(json.dumps(("apple", "bananas")))
    # print(json.dumps("hello"))
    # print(json.dumps(42))
    # print(json.dumps(31.76))
    # print(json.dumps(True))
    # print(json.dumps(False))
    # print(json.dumps(None))
    x = {
      "name": "John",
      "age": 30,
      "married": True,
      "divorced": False,
      "children": ("Ann","Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }
    # print(type(x))
    print(json.dumps(x))






if __name__ == '__main__':
    main()