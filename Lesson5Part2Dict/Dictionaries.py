# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])
#
# another_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "year": 2022
# }
# print(len(another_dict))
#
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
#
# user = dict(username = "Arja", age = 15, email = "noName@gmail.com" , password = "Valan Margulis")
# print(user)
# # print(user["Arja"])
# print(user.get("name"))

# User should input number like: 1234 or 2441
# The program should print the number in words:
# one two three four.
# Tip: create a dictionary with mapping digits to word (“2” : “Two”) ..
# number_dict = {
#     "2": "two"
# }
# take the input  -> as text (number) 23421
# iterate with loop on the number text
# for i in input:  -> 2,3,4,2,1
# for each digit (i) search the value in dictionary
#to search for the value number_dict.get(i) -> then print this.
# # 2132132 -> two one three...
# numbers_dictionary = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# number = input("enter the number only 1-4 allowed: ")
# #12312121
# for digit in number:
#     print(numbers_dictionary.get(digit),end= " ")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# x = thisdict.values()
# x = thisdict.items()
# print(x)

# Write a Python program that prompts the user to enter details
# about a car (brand, model, year) and stores them in a dictionary. Then, perform the following operations:
# Print all the keys in the dictionary.
# Print all the values in the dictionary.
# Print all the key-value pairs in the dictionary as tuples.
# Tip: use keys(), values() and items() functions
# brand = input("enter the brand: ")
# model = input("enter the model: ")
# year = input("enter the year: ")
# car = {
#     "brand": brand,
#     "model": model,
#     "year": year
# }
# car = dict(brand = brand, model=model, year=year)
# car = {
#     "brand": input("enter the brand: "),
#     "model": input("enter the model: "),
#     "year": input("enter the year: ")
# }
# print(car.keys())
# print(car.values())
# print(car.items())
#
# print(car.get("name"))


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# thisdict["color"] = "yellow"
#
# print(thisdict.get("color", "white"))
# print(thisdict)

# You have a shop of fruits with the prices:
product_inventory = {
    "apple": 0.99,
    "banana": 0.49,
    "orange": 0.79,
    "grape": 1.29,
    "watermelon": 2.99,
    "pineapple": 1.99
}

def calc_square(number):
   print(number * number)
print(calc_square(10))

cars = [["Volvo"],["Renault", "Peugeot", "Citroen"], ["Mercedes", "BMW", "Audi", "Wolkswagen"]]