class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):


    def printname(self):
        super().printname()
        print("I am student")


def average_score():
    total_score = int(input("Enter total score: "))
    num_students = int(input("Enter number of students: "))
    average_score = total_score / num_students
    print("Average score:", average_score)


def add_content_to_my_file(content):
    my_file = open(r"C:\Users\Iliap\PycharmProjects\CoursePython\FunctionsPart2\stam.txt", "a")
    my_file.write(content)
    my_file.close()


def main():
    # Use the Person class to create an object, and then execute the printname method:

    x = Person("John", "Doe")
    y = Student("Arja", "stark")
    x.printname()
    y.printname()
    add_content_to_my_file("new content")


if __name__ == '__main__':
    main()