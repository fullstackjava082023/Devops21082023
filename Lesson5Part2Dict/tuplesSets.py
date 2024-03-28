# fruits = ("apple", "banana", "cherry", "grape")
# green = fruits[0] # apple
# yellow = fruits[1] # banana
# red = fruits[2] #cherry
#
# green, yellow, red, blue = fruits
#
# print(green,yellow,red, blue)
# Define a list of tuples containing fruit names and their corresponding colors
# fruits = [
#     ("apple", "green"),
#     ("banana", "yellow"),
#     ("cherry", "red"),
#     ("strawberry", "red"),
#     ("raspberry", "red")
# ]
# For each tuple print : f"The {fruit} is {color}"
# E.G : The apple is green The banana is yellow….
# Use UNPACKING feature
# my_tuple = ("apple", "green")
# fruit, color = my_tuple
# print(f"The {fruit} is {color}")
# for i in fruits:
#     fruit, color = i   # i =('apple', 'green'), ("banana", "yellow"),
#     print(f"The {fruit} is {color}")
# for fruit, color in fruits:
#     print(f"The {fruit} is {color}")


# fruits = ("apple","blueberry", "banana", "cherry", "grape", "kiwi", "raspberry")
# # green, yellow , *rest = fruits
# # print(rest)
# first, sixth, *rest_fruits = fruits
# print(rest_fruits)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# green, *tropic, more, one_more, red = fruits
# print(tropic)
#
# We have a tuple with student and her grades:
# student_grades = ("Alice", 85, 43, 56, 78, 98)
# name, *grades = student_grades
# # grades = [85, 43, 56, 78, 98]
# # Need to calculate average of her grades using unpacking with *
# print("The average is :", sum(grades) / len(grades))


# product_info = ("Apple", "Fruit", 10, 50, 5)
#
# *product, price, weight, boxes = product_info
# print("The overall price of apples", price * weight * boxes)


####################SETS####################
#
# thisset = {"apple", "banana", "cherry", "apple", "apple", "banana"}
# print(thisset)
#
# thisset = {"apple", "banana", "cherry", "kiwi"}
# print(thisset)
# thislist = list(thisset)
# print(thislist)
# thisset = set(thislist)
# print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("mango")
# tropical = {"pineapple", "mango", "papaya", "banana"}
# thisset.update(tropical)
# # print(thisset)
# mylist = ["kiwi", "orange", "apple", "mango"]
# thisset.update(mylist)

# # thisset.remove('apple')
# thisset.discard('apple')
# # thisset.remove('apple')
# thisset.discard('apple')
# print(thisset)

# Remove duplicates from the input and print:
# Input 5 words from the client
# Remove duplicates using set:
# Print the set of inputs.

# create empty set -> set()
# 5 times get input from the user
# add input to the set -> its automatically removes duplicates
# print set
words = set()
for i in range(5):
    word = input("enter the word: ")
    words.add(word)
print(words)