def my_function(food):
    for x in food:
        print(x)

def calculate_unique_sum(list_numbers):
    numbers_set = set(list_numbers)
    return sum(numbers_set)


def main():
    fruits = ["apple", "banana", "cherry"]
    my_function(fruits)
    list1 = [3, 3, 4, 5, 5, 6, 6, 7]
    print(calculate_unique_sum(list1))




if __name__ == "__main__":
    main()














