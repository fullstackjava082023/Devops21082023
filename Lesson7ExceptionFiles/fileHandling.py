
# create file in your project Write there:
# Hello world from the file
# Create the function open_my_file()
# The function should open that file by using the file path.
# The function should print the text of the file
# The function should close the file after use.
def open_my_file():
    # my_file = open("file.txt")
    my_file = open(r"C:\Users\Iliap\PycharmProjects\CoursePython\Lesson7ExceptionFiles\file.txt")
    # print(my_file.read())

    lines = my_file.readlines()
    print(len(lines))
    my_file.close()

def write_to_file():
    my_file = open("file2.txt", "w")
    my_file.write("New content")
    my_file.close()


def add_content_to_file(content):
    my_file = open("file.txt", "a")
    my_file.write(content)
    my_file.write(" ")
    my_file.close()


def main():
    # open_my_file()
    # write_to_file()
    add_content_to_file("Arja ")
    add_content_to_file("Winterfell ")
    add_content_to_file("no number ")





if __name__ == '__main__':
    main()