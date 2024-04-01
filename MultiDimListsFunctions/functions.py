def func1():
    print("func1")


def func2():
    print("func2")


# func2()
# func1()
# func2()

# Exercise:
# create a function which prints your name and surname
# call the function

# def print_name():
#     print("Arja Stark")
#
#
# print_name()

# def print_name(name, surname):
#     print(f"my name is {name} and my surname is {surname}")
#
#
# print_name("John", "Snow")
# print_name("Ned", "Stark")
#
# print_name("Robert",  "Baratheon" )


# Create a function which takes a two numbers as arguments
# Function calculates and prints the sum.
# Call the function with different arguments.
# def sum_numbers(a, b):
#     print(a + b)
#
#
# sum_numbers(5, 9)

# def divide(a, b):
#     print(a/b)
#
# divide(0,6)
# divide(b=6, a=0).


def greet_user(name):
    counter = 1
    print(f"hi there {name}")
    print("welcome on board")
    print(counter)
    counter += 1




greet_user("Arja")
greet_user("John")
greet_user("Ned")
# print(counter)