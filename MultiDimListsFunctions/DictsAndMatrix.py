# Create program which can read emojis:
# Example :
# Input : hi today is the nice day :)
# Output: hi today is the nice day 😊
# Tip1:
# Use .split(‘ ‘) to split the words in the text - this will return list of words
# # Tip2:
# # To use emoji in windows use “command + .(dot)”
# emojis = {
#     ':)': '😊',
#     ':(': '😒',
#     ':D': '😂',
#     ':P': '😜',
#     ':-)': '😀'
# }
#
# text = input("Enter the text you can use emojis: ")
# words = text.split(" ")
# # print(words)
# new_text = ''
# for word in words:
#     new_text += emojis.get(word, word)
#     new_text += ' '
# print(new_text)

#
# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
#
# T.insert(2, [0,3,15,6,78])
# del T[3]
# del T[0]
#
# for r in T:
#    print(r)
#                          #   [5000, 6000, 7000]
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)     # [5000, 6000] -> 7000 -> [5000, 6000, 7000]
# print(list1)

# Ask user to enter elements for 2*2 matrix (numbers)
# Print the matrix: Tip use append method
# input 0,0 -> 1
# input 0,1 -> 12
# input 1,0 -> 3
# input 1,1 -> 4
# [[1,12],[3,4]]
#
# r1 = [1,12]
# r1.append(1)
# r1.append(12)
# r2 = [3,4]
# r2.append(3)
# r2.append(4)
# r3 = [r1, r2]
# print(r3)

# matrix = [[5,26], [2,59]]
#
# matrix[0][0] = int(input("enter the number in 0,0: "))
# matrix[0][1] = int(input("enter the number in 0,1: "))
# matrix[1][0] = int(input("enter the number in 1,0: "))
# matrix[1][1] = int(input("enter the number in 1,1: "))
# print(matrix)
# list1 = [[input("enter the number:"),input("enter the number:")],[input("enter the number:"),input("enter the number:")]]
# print(list1)

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# # calculate the sum of the matrix and print it
# # use loop inside loop
# # print(sum(matrix)) -> not working
# sum2 = 0
# for row in matrix:
#     sum2 += sum(row)
# print(sum2)

matrix = [['a', 'b', 'e'], ['c','d','f'], ['e','e','o']]
# write a program which find number of e inside the matrix and prints it.
# expected result 3
counter = 0
for row in matrix:
    for element in row:
        if element == 'e':
            counter += 1

print(counter)

#.count('e')