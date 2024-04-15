import greetings as gr
import mymodule as greet
import camelcase
import matplotlib.pyplot as plt
import random


# import ecommerce.shipping as ship_module
from greetings import how_are_you,say_good_bye
from ecommerce.shipping import send


# Install package camelcase : pip install camelcase
# Create a function : def convert_to_camelcase():
# The Function should ask user to input text and change it to the camelcase.
# (use camelcase module to do that)
# In Main call the function.
def convert_to_camelcase():
    text = input("Enter the text: ")
    c = camelcase.CamelCase()
    print(c.hump(text))

def create_random_plot():
    # X-axis
    x_values = list(range(0,10)) #[0,1,2,3,4,5...10]
    print(x_values)
    # random values for Y-axis
    y_values = []
    for i in range(0,10):
        y_values.append(random.randint(1,100))
    #Plot the data
    plt.plot(x_values, y_values)
    # adding title and labels to the plot
    plt.title("Random Data Line Graph")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    # show the plot
    plt.grid(True)
    plt.show()


def main():
    # numbers = [10, 20, 6, 2]
    # find_max(numbers)
    # greet.greeting("Cersei")
    # print(dir(gr))
    # table1 = greet.Table()
    # table1.who_am_i()
    # send()
    # convert_to_camelcase()
    create_random_plot()








if __name__ == '__main__':
    main()


