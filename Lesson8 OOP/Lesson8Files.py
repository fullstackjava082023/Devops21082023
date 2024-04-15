import os

# Create a function add_content_to_my_file(content):
# The function getting text as a content and adding that text to the file
# , which you created in the previous exercise.
# Use “a” option (to add content)
# Run the function with different text and see if content is added
# Don't forget to close the file after use.
# Call the function with different text as argument,
# your name, next time - your address, next time your phone.
# def add_content_to_my_file(content):
#     # open the file (file.txt) use append (a) parameter
#     # add content to the file
#     # use write to write to the file
#     # close the file

def add_content_to_my_file(content):
    # Open the file in append (a)
    # file = open("file.txt", "a")
    with open("file.txt", "a") as file:
        # Add the content to the file
        file.write(content)
    # file = (file.txt, "w \n")

# Write the function delete_my_file which
# will delete the file you created in the previous exercises.
# Try to call the function again when file already removed.

def delete_my_file():
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")
    else:
        print("file not found")


def main():
    delete_my_file()
    entries = os.listdir("myFolder")
    # os.system("rm -rf myFolder")
    # print(entries)
    # os.rmdir("myFolder")


    # add_content_to_my_file("content\n")
    # os.remove("file5.txt")

# def main():
#    # Define the file path
#    file_path = "example.txt"
#    # Open the file using 'with' in write mode
#    with open(file_path, "w") as file:
#        file.write("This is a simple example of using 'with' to open a file.\n")
#        file.write("The 'with' statement ensures the file is properly closed after use.\n")
#    # Open the file using 'with' in read mode
#    with open(file_path, "r") as file:
#        file_contents = file.read()
#    # Print the contents
#    print("File Contents:")
#    print(file_contents)


if __name__ == '__main__':
    main()