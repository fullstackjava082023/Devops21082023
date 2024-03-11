# a = 300
# b = 300
# # a>b a==b a<b
#
# if b > a:
#     print("b greater than a")
# elif b == a:
#     print("a equals b")
# else:
#     print("a greater then b")
#
#
# print("finish")

# x = 10
# if x < 5:
#     y = 20
#     print("x is greater than 5")
#     print(y)

# Ask user to input his car speed.
# If speed > 120 print “too fast”
# If speed < 80 print “too slow”
# Otherwise print “good driver”
#
# speed = float(input("enter your car speed"))
# if speed > 120:
#     print("too fast")
# elif speed < 80:
#     print("too slow")
# else:
#     print("good driver")


# Get two ages of two brothers as input
# For example:
# Tomer’s age and Dany’s age.
# If Tomer’s age is higher - print:
# “Tomer is an older brother”
# If Dany’s age is higher - print:
# “Dany is an older brother”
# If the ages are equal - print:
# “Tomer and Dany are twins!”

# danny_age = int(input("enter Danny's age "))
# tomer_age = int(input("enter Tomer's age "))
#
# if tomer_age > danny_age:
#     print("Tomer is an older brother")
# elif tomer_age < danny_age:
#     print("Dany is an older brother")
# # ages are equal
# else:
#     print("Tomer and Dany are twins!")
#
# Ask user to provide the number:
# If the number is Even :
# Print “Even”
# If the number is Odd :
# Print “Odd”
# Hint: use modulo

# number = int(input("Enter the number"))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Write a Python
# program to calculate the sum of three given input numbers.
# If the values are equal, return three times their sum.

# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))
# num3 = int(input("enter the third number: "))
#
# if num1 == num2 == num3:
#     print((num1 + num2 + num3)*3)
# else:
#     print(num1 + num2 + num3)

#     Input string  from the user:
#     if string is shorter than 20 characters  (len)  len(text) > 20
#     print     short  string
#     if it is between 20 and 50 print
#     normal  string
#     if it is more than 50
#       print  long string
# Try to rewrite it with shorthand if:
# message = input("enter the text ")
# # if len(message) < 20:
# #     print("short string")
# # elif 20 <= len(message) < 50:
# #     print("normal string")
# # else:
# #     print("long string")
#
# print("short string") if len(message) < 20 else print("normal string") if 20 <= len(message) < 50 else print("long string")

# Kg to Pounds converter
# Input from user K if he want to enter Kilograms and P if he want to input pounds
# Input the Weight
# Convert KG to Pounds or Pounds to KG depends on the input
# Output the converted weight
# 1 kg = 2.2p
# 1 p = 0.45kg
# mode = input("enter Mode (K/P) k-> kg to pd  p -> pd to KG: ")
# if mode == "K":
#     weight_kg = float(input("Enter the weight in KG: "))
#     print("your weight in Pound", weight_kg * 2.2)
# elif mode == "P":
#     weight_pd = float(input("Enter the weight in Pounds: "))
#     print("your weight in KG", weight_pd * 0.45)
# else:
#     print("input is wrong")

grade = int(input("enter the grade"))

if grade < 55:
    print("not good")
elif 55<= grade <= 64:
    print("still not good")
elif 65 <= grade <= 74:
    print("ok")
elif 75 <= grade <= 84:
    print("good")
elif 85 <= grade <= 94:
    print("very good")
else:
    print("perfect!")

