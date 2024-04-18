import string_manipulation as strings
from file_handling import read_file, write_to_file


def main():
    # print(strings.reverse_string("stam text"))
    # print(strings.is_palindrome("dadadadadad"))
    print(read_file("file.txt"))
    write_to_file("file2.txt", "hi from python")


if __name__ == '__main__':
    main()