
# numbers = [1,2,3,4]
# print(numbers)
#
# numbers2 = [1,2,3, [3,4]]
# print(numbers2)
#
# matrix = [[1,2,3], [23, 4,5], [6,7,8]]
# print(matrix)

# _ _ _
# _ _ _
# _ _ _

# board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
# print(board)

def print_board():
    print(board[0])  # 1
    print(board[1])  # 2
    print(board[2])  # 3

# # player X make move 0,1
# print_board()
# # player O make move 2,0
# print_board()
# # player X make move 2,1
# print_board()


# def greet():
#     print("hi from function")
#
#
# greet()
# greet()
# for row in board:
#     # row will hold the row
#     print(row)

# ['X', 'O', 'O']
# ['O', 'X', '_']
# ['_', 'X', 'X']

board = [["_", "X", "O"],
         ["X", "X", "_"],
         ["O", "X", "O"]]

#to check if there is a winner X? or O?
#checking if there is a winner in the row
#check if x in all 3 places
# check if o in all 3 places
# row = board[0] #["_", "X", "O"]

# def check_winner():
#     #check rows
#     for row in board:
#         if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
#             print("the winner is: X")
#         elif row[0] == 'O' and row[1] == 'O' and row[2] == 'O':
#             print("the winner is: O")
#     #check columns
#     for i in range(3): #i = 0, 1 ,2
#         if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
#             print("the winner is: X")
#         elif board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
#             print("the winner is: O")
#     #check diagonals
#
#
# check_winner()
#
# #3 inserting value to the board:
# board =  [["_", "_", "_"],
#           ["_", "_", "_"],
#           ["_", "_", "_"]]
#
#
# def make_move():
#     value = input("Enter the value: ")
#     row_index = int(input("Enter the row 0-2: "))
#     col_index = int(input("Enter the column 0-2: "))
#     #---------------2,2
#     # board[2][2] = value
#     if board[row_index][col_index] == '_':
#         board[row_index][col_index] = value
#     else:
#         print("the cell is not empty! try again")
#
#
# while True:
#     make_move()
#     # check_winner()
#     print_board()

# 4.Matrix Transpose: Write a script to transpose a given matrix.
# The transpose of a matrix is obtained by swapping the rows and columns.
# t_matrix = [[1,2,3] ,[4,5,6] , [7,8,9]]
# expected result after transpose:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    # [[1,2,3]
    # ,[4,5,6]
    # ,[7,8,9]]
    #
    # [[1, 4, 7],
    #  [2, 5, 8],
    #  [3, 6, 9]]

# t_matrix = [[1,2,3] ,[4,5,6] , [7,8,9]]
# # t_matrix[2][0] -> new_matrix[0][2]
# new_matrix =  [["_", "_", "_"],
#               ["_", "_", "_"],
#               ["_", "_", "_"]]
#
# for i in range(len(t_matrix)):
#     for j in range(len(t_matrix[i])):
#         new_matrix[j][i] = t_matrix[i][j]
#
#
# print(new_matrix)
# Arja
# 321772323 -> 3217723323
# 308456910 -> 3084569100
#

def create_new_id(old_id):
    digit = old_id[-1]
    place_from_end = int(old_id[-2])
    prefix = old_id[:-place_from_end]
    suffix = old_id[-place_from_end:]
    result = prefix + digit + suffix
    # return result


# old_number = input("enter old id: ")
# 3
# -->2
# old_id[-2] -> 3


# print(create_new_id("321772323"))
# new_generated_id = create_new_id(old_number)
# print(new_generated_id)


# def calc_square(number):
#    return number * number
#
# print(calc_square(10))

