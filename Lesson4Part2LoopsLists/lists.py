

cars = ["Nissan", "Toyota", "Audi", "Kia" , "Hyundai"]
# print(cars[1])  # Toyota
# print(cars) # "Nissan", "Toyota", "Audi"
# print(len(cars)) # 3


# print(type(cars))

# print(cars[-4])

# instead of nissan i want to put Mercedec
# cars[0] = "Mercedes"
# cars[2] = 1
# cars[2] = "Nissan"
# print(cars)

cars = ["Nissan", "Toyota", "Audi", "Kia", "Hyundai"]

# cars[1:3] = ["Skoda",  "Chevrolet" , "BMW"]
# cars[1:3] = ["Skoda"]
cars.insert(3, "Mitsubishi")

# cars.pop(2)
# last_car = cars.pop()
# # del cars[0]
# # del cars
# cars.clear()
# cars.insert(0,"nissan")
# print(cars)
# # print(last_car)
# for el in cars:
#     print(el)


# lst = [10,20,59]
# sum = 0
# for x in lst:
#     sum = sum + x
# print(sum)


# Write a program which will take number
# from the user and will print all numbers from 1 to that input number.
# Use For loop.
# example : input 10 -> output 1,2,3,4,5,6,7,8,9
#example of for loop in range

# number = int(input("enter the number: "))
# for i in range(1, number + 1):
#     print(i)

# print all even numbers from 1 to 100
# for x in range(1, 100, 2):
#   print(x)

# Write a program which will take number from the user and
# will print all numbers from 1 to that input number and backward till 1.
# input 6 ->   1,2,3,4,5,6,5,4,3,2,1
#
# number = int(input("enter the number: "))
# for i in range(1, number):
#     print(i)
# for i in range(number, 0,  -1):
#     print(i)


# Find if the input number is prime or not and print :
# If input is prime :
# Your number is prime.
# If not :
# Your number is not prime.
# Prime number is the number which can be divided only by itself and by 1.
# Use Break to make the code faster.
# number = int(input("enter the number: "))
# for x in range(2, number):
#     if number % x == 0:
#         print("not prime")
#         break
# else:
#     print("prime number")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
#
# for x in adj:
#   for y in fruits:
#     print(x, y)


for i in range(6):
  for j in range(0, 7-i):
    if j >= i:
      print(" ", end=" ")
    else:
      print("*", end = " ")
  print()
