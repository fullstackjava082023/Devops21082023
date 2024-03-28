# 1
# Sum of List Elements: Given the list [1, 2, 3, 4, 5], calculate the sum of all elements.

# my_list = [1, 2, 3, 4, 5]

# print(sum(my_list))

# my_sum = 0
# for x in my_list:
#     my_sum += x
# print(my_sum)

# 6
# List Sorting: Given the list [5, 2, 8, 1, 9], sort the elements in ascending order.
# my_list = [5, 2, 8, 1, 9]
#  # [1,2,5,8,9]
# my_list.sort()
# print(my_list)

#7
# List Slicing: Given the list ['apple', 'banana', 'orange', 'grape', 'kiwi'],
# create a new list containing only the first and last elements.
# initial_list = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'cherry']
# new_list = [initial_list[0], initial_list[-1]]
# print(new_list)

#9
# List Element Frequency: Given the list ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# and element 'apple', calculate the frequency of occurrence of the element in the list.
initial_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# count = 0
# # we need some count variable which will be 0
# # for loop
# for element in initial_list:
#     if element == 'apple':
#         count += 1
# print(f"the count of apples is {count}")
# # check if element is 'apple'
# # if it is apple -> increase count + 1
print(initial_list.count('apple'))
