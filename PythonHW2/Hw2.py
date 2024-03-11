
# 5 find the rightmost digit and print
# 3456 -> 6
# number = int(input("Enter the number 4 digits at least "))
# # 3456 / 10  -> 345 remainder = 6
# print(number % 10)

# print the second digit from the right
# 3456 -> %100 -> 56 -> //10 -> 5
# print(number % 100 // 10)

# get the 3digits number print print the number of hundreds
# 121 -> 1  555 -> 5   652 -> 6
# number2 = int(input("Enter the number 3 digits exactly "))
# # 121 // 100 -> 1
# print(number2 // 100)

# get the number with two digits and print sum of the digits
# 58 -> 5 + 8 = 13
# 58 // 10 -> 5     58 % 10 -> 8
# number3 = int(input("Enter the number 2 digits exactly "))
# tens = number3 // 10
# units = number3 % 10
# print(tens + units)

# Get First Word: Write a program that takes a sentence as input and prints the first word of the sentence.
# "the weather is hot" -> place of the "space" -> 3 -> slice the sentence from 0 till 3
# message = input("please enter the sentence ")
# #find -> finds the index of the subtext inside the text
# index = message.find(" ")
# # returns first index of the " "
# print(message[:index])

# Replace First Occurrence:
# Write a program that takes a sentence and two words as input,
# and replaces the first occurrence of the first word with the second word in the sentence.
# Input sentence and words
# sentence = input("Enter a sentence: ")
# word1 = input("Enter first word: ") #old
# word2 = input("Enter second word: ") #new
# # Replace first occurrence
# # Hi I am Arja
# # Arja
# # John
# # Hi I am John
# print(sentence.replace(word1, word2, 1))

# 3. Reverse first word :
# Write a program that takes input sentence ,
# reverse the first word and print the sentence with first word reversed
# hello I am ilia -> olleh I am Ilia
# 0. input sentence
# 1. cut the first word
# 2. reverse it
# 3. replace original first word by reversed first word
# sentence = input("Enter a sentence: ")
# index = sentence.find(" ")
# word1 = sentence[:index] #save the first word
# reversedWord = word1[::-1] #reverse word
# print(sentence.replace(word1, reversedWord, 1))

# Exercise:
# you have a file path:
file_path = "G:/My Drive/Course Java/Pythonfile.txt"
# print only the file name (file.txt)
# find the last occurence of / (rfind)
# cut the sentence from the last / till the end
# index = file_path.rfind("/")
# print(file_path[index+1:])
#####################
# 1. reverse the path
# 2. find the first / (find)
# 3. slice the name of the file -> txt.elif
# 4. reverse the result -> file.txt
reversed_path = file_path[::-1]
index = reversed_path.find("/")
file_name = reversed_path[:index]
file_name_original = file_name[::-1]
print(file_name_original)

