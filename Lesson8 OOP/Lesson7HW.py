
def readFromFile():
    # input from the user the file name
    fileName = input("enter the file you want to open ")
    # try to open the file and save it in the variable "file"
    try:
        file = open(fileName , "a")
        # print what we have inside the file
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("file was not found")

def main():
    readFromFile()
    # print("start")
    # try:
    #
    #     print("hello world")
    #     6/0
    # # more code comes here
    # except ZeroDivisionError:
    #     print("Zero division error happened")
    # file = open("file4.txt")
    # # file.write("Another text \n")
    # file.close()
    #
    # # data = file1.read()
    # # print(data)










if __name__ == '__main__':
    main()