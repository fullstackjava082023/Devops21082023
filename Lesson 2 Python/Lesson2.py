import math
import random

# ######################Home Work#############################
# Exercise 1: Print Address
# Write a Python program that prompts the user to enter city, house number, street and prints address nicely.
# print()
# input()
# variables -> save input
# we want 1. take 3 inputs from the user (city, house number , street)
# 2. to save the input in the variables 3. print that nicely
# city = input("enter the city ")
# house_nr = input("enter the house number ")
# street = input("enter the street ")
# print("Your address is: " + "City:" + city + " Street:" + street + " number:" + house_nr)
# Exercise 2: Reverse Order of Operations
# Write a Python program that accepts three numbers as input:
# 'a', 'b', and 'c'. The program should compute the result of the expression '(a + b) * c' and then print the result.
# a = int(input("enter a: "))
# b = int(input("enter b: "))
# c = int(input("enter c: "))
# # 5 , 10 ,2  -> "510" * "2"
# # we need to make a casting from text to numbers e.g from str to int
# print(type(a))
# print((a + b) * c)

# Exercise 3: BMI Calculator
# Write a Python program that asks the user to input their weight in kilograms and height in meters,
# calculates their Body Mass Index (BMI) using the formula BMI = weight / (height * height), and prints the BMI.
# int whole numbers 5 -10
# float floating point numbers 5.5 2.1223342, -45.344
# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# print(weight / (height * height))

# Exercise 4 : printing
# Write a Python program that prompts the user to enter  the text  and the number (n)
# Print "your text <n> times is :" + <text printed n times>
# Arja , 3 -> your text 3 times is : ArjaArjaArja
# text = input("Enter the text: ")
# n = int(input("Enter the number ")) #int
# print("your text", n, "times is:", text * n)
##############################################################################################
#
# text = '''I don't know asdfffffffffffffffffffffffffffffffffffffffffffffdsfsdfkljsdklfjsdlf;kjsd;flk
#     sjfk i want to move'''
#
# # print(text.title())
#
# cover = "harry a potter"
# # print(cover.title())
#
# print(cover[0])
# print(cover[6])
# print(cover[1])
#
# print(cover[-3])
# # print(cover[-23]) error
#
# print(cover[2:5])

# text = "HelloWorld123"
# print(text[2:7:2])
# # Output: loo
# print first three characters
# print(text[:3])
# print(text[-3:])
# # print every second char
# print(text[::2])
# # print every second char starting from 2
# print(text[1::2])
# Print the string in reverse order.
# print(text[::-1])

# name = "Arja"
# lastName = "Stark"
# age = 15
#
# # Arja [Stark] is a coder
# # message = name + " [" + surname + "]" + " is a coder"
# message = f"{name} [{lastName}] is a coder"
#
# # Arja [Stark] is a coder and her age is: 15 // with formatted string
# # message = f"{name} [{lastName}] is a coder and her age is: {age}"
#
# newMessage = f"{message} and her age is {age}"
# print(newMessage)

#
# text = "Liran Gabay love devops"
# print(text.replace("Liran", "zehavit"))

# # arja stark
# text = "Arja [Stark] is a coder"
# # ARJA STARK
# # arja stark
# # Arja Stark
# print(text.upper())
# # title()
# # upper()
# # lower()

# input number between 10 to 99 - print reversed number
# try to solve with % and //
# number = int(input("enter the number between 10 and 99 ")
# # number of tens
# tens = number // 10
# units = number % 10
# print(units * 10 + tens)
# 25
# print(number[1] + number[0])
# print(number[::-1])

# Input float number can be not natural like 4.1
# Print the closest even number which is higher than initial number.
# Example: input 4.1 -> output : 6
# 4.1  ->  4 -> +2 -> 6
#          5 + 1 -> 6
# 4%2 = 2-0 -> +2
# 5%2 = 2-1 ->  +1
# 4.1 -> int(4.1) -> 4
# number = float(input("enter any float number "))
# number = number//1
# print(number + 2 - (number % 2))
#
# years_finished_school = int(input("enter the number of years ago you finished the school "))
# print(years_finished_school >= 10)

# x = math.sqrt(64)
# print(x)
# print(math.pi)

# radius = float(input("Enter the radius of the circle "))
# # perimeter 2PiR
# perim = radius * 2 * math.pi
# # area PI*R^2
# area = math.pi * radius ** 2
# print(f"The perimeter is {perim} and the area is {area}")

#Random
random_number = random.random()
print(random_number)

random_one_to_hundred = random.randint(1,100)
print(random_one_to_hundred)