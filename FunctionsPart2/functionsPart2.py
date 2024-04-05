
# def translate_with_emoji(phrase):
#     #extract the code to the function
#
#     emojis = {
#         ":)": "😊",
#         ":(": "😒",
#         ":D": "😁",
#     }
#     words = phrase.split(" ")
#     output = ''
#     for word in words:
#         output += f"{emojis.get(word, word)} "
#     # print(output)
#     return output
# ###########################################
#
# text = input("> ")
# # text = "hi its bad day :("
#
# # print(translate_with_emoji(text))
# result = translate_with_emoji(text)
#
# result = transalet_to_hebrew(result)
# success = sendEmail("arja@gmail.com", "john@gmail.com", "how are you?" , result)


# def add_comma(words):
#     print(words)
#
#
# add_comma(["Arja", "Stark", "good girl", "And john", "is a bad guy"])

# You have the list:
# list1 =[3, 3, 4, 5, 5, 6, 6, 7]
# Create a function which calculate sum of unique numbers
# The function gets a list as an argument and returns a sum of all unique numbers
# If number exists more than once it will not added to the sum for the second time.

list1 =[3, 3, 4, 5, 5, 6, 6, 7]
# list2 =[3, 5, 6, 6, 7, 20, 23,20,27]



def calculate_unique_sum(list_numbers):
    numbers_set = set(list_numbers)
    return sum(numbers_set)


result = calculate_unique_sum(list1)
print(result)
# print(calculate_unique_sum(list2))

# list_numbers
# listNumbers
# listNumbers
# list_numbers