# #1:
# Creating a Dictionary
# Write a Python program that creates a dictionary representing a person's information.
#  The dictionary should include keys such as "name", "age", "gender", and "city".
#  user should input "name", "age", "gender", and "city".  - the program should create the dictionary
#  Print out the dictionary.
# name = input("Enter the name: ")
# age = input("Enter the age: ")
# gender = input("Enter the gender: ")
# city = input("Enter the city: ")
# my_info = {
#     "name" : name,
#     "age" : age,
#     "gender" : gender,
#     "city" : city,
# }
#
# print(my_info.get("city"))

# print(my_info)

# Student Gradebook:
# Create a dictionary representing a student's gradebook. The keys should be subject names, and the values should be the corresponding grades.
# Example:
# 	gradebook = {
#     "Math": 85,
#     "Science": 90,
#     "History": 75,
#     "English": 88
# }
# input mode from the user
# 1 = adding new subject and grade
# 2 = removing subject
# 3 = calculate grade average
# 4 = exit
# 5 = print the grades
gradebook = {
     "Math": 85,
     "Science": 90,
     "History": 75,
     "English": 88
}

while True:
    choice = input("Enter the mode: 1->Add new Subject, 2->Remove Subject, 3->calculate average, 4->exit, 5->print all: ")
    if choice == '1':
        # add new item
        new_subject = input("Enter the new subject: ")
        new_grade = int(input(f"enter the new grade for {new_subject}: "))
        gradebook[new_subject] = new_grade
    elif choice == '2':
        # remove subject
        subject_to_remove = input("select subject to remove: ")
        gradebook.pop(subject_to_remove)
    elif choice == '3':
        #calculate average
        sum_grades = sum(gradebook.values())
        number_of_grades = len(gradebook)
        print("the average =",  sum_grades/number_of_grades)
    elif choice == '4':
        print("Exit")
        break
    elif choice == '5':
        print(gradebook)
    else:
        print("wring choice enter between 1 and 5")
