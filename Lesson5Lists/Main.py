# x = 5
# if x > 2:
#     pass
#
# print("biigger")

# x=0
# while x <= 100: # 100.. 102
#     x += 2
# print(x)

# for l in "jhon":#  l = j, h, o ,n
#     print(l, end=' ')
#     if l == 'o':
#         continue #go to the next iteration

# כתבו קטע קוד שמקבל 10 ערכים מהמשתמש ו מדפיס את הסכום של המספרים החיוביים בלבד
# sum = 0
# for i in range(10): # 0 , 1, 2, 3
#     number = float(input("Enter the number: ")) # 20
#     sum += number
# print(sum)

# כתבו תוכנית  שמק בלת 10 ערכים מהמשתמש ומדפיסה בסוף את סכום המספרים החיובים
# ושורה שמדפיסה את סכום המספרים השליליים
# sum_negative = 0
# sum_positive = 0
# for i in range(10):
#     number = int(input("Enter the number: "))
#     if number < 0: #-50
#         # to add to the sum of negatives
#         sum_negative += number #  -10 -50 = -60....
#     else:
#         sum_positive += number
# print(f"negative sum is {sum_negative} and positive sum is {sum_positive}")

# כתבו תוכנית שמקבלת מספר INT מהמשתמש ומדפיסה אותו הפוך לדוגמה אם אני מכניס את המפר
# 1556754 אראה בהדפסה 4576551
# text = "Game of thrones"
# reverse = text[::-1] #reverse the text
# print(reverse)
#
# num = input("Enter the number: ")
# reverse = num[::-1]
# print(reverse)
#
# input1 = input("enter first element: ")
# input2 = input("enter the second element: ")
# input3 = input("enter the third element: ")
#
# thisList = [input1, input2, input3]
# print(thisList)
#
#
# number = None
#
#
# numbers = [-1, -5 , -10 , -2]

#
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.append(tropical)
# print(thislist)
# print(thislist[3][1])

# Show the value and the index of the highest number from 5 inputs
# max_number = None
# index = 0
# for i in range(5): # 10, 20, 4,25
#     number = int(input("enter the number: "))
#     if max_number == None or number > max_number:
#         max_number = number
#         index = i
#
# print(max_number)
# print(index)
# numbers_list = []
# for i in range(5):
#     number = int(input("enter the number: "))
#     numbers_list.append(number)
# max_number = max(numbers_list)
# index = numbers_list.index(max_number)
# print(f"max number is {max_number} and the index is {index}")

# numbers = [10,2,3,-5,5,6,7]
# squares = []
# # for el in numbers:
# #     squares.append(el * el)
# for i in range(len(numbers)):
#     squares.append(numbers[i] ** 2)
# print(squares)

# thislist = ["apple", "banana", "cherry", "banana"]
#
# index = thislist.index("banana")
# thislist[index] = "watermelon"
# print(thislist)

# You have given a Python list.
# Write a program to find value 20 in the list,
# and if it is present, replace it with 200. Only update the first occurrence of an item.
# Given:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
# [5, 10, 15, 200, 25, 50, 20]

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index = list1.index(20) # -1
# if index != -1:
#     list1[index] = 200
#
# print(list1)

thislist = [100, 50, 65, 82, 23]

# thislist.sort(reverse=True)
# print(thislist)
# thislist.reverse()
# print(thislist)
# print(thislist[::-1])
# thislist2 = thislist.copy()
#
# thislist2.reverse()
# print(thislist)
# print(thislist2)


# list1 = [5, 10, 15, 5, 10, 23, 15, 15, 20, 25, 50, 20]
# unique_list = []
# #Write a program to remove duplicate from a list:
# # print the new list
# # 5,10,15,20,25,50
# # algorithm
# # create a new list of unique elements []
# # for each element in list1 if element not in unique list -> add it . else -> go next
# # append -> to add element to the list
# # to check if element in the list use "not in"
# for el in list1:
#     if el not in unique_list:
#         unique_list.append(el)
#
# print(unique_list)

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = []
# # print(list1[0] + ' ' + list2[0])
# # algorithm - for el1 in list1 -> for el2 in list2 ---> el1 + ' ' + el2
# for el1 in list1:
#     for el2 in list2:
#         list3.append(el1 + ' ' + el2)
# print(list3)

mytuple = ("Hello ", "take", "Sir")
list1 = ["Hello ", "take "]
print(mytuple[1])