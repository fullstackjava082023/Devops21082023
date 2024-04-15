from camelcase.main import CamelCase

import api as mx


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def sayHiToOther(self,otherName):
        print(f"hi from {self.firstname} to {otherName}")


class Student(Person):


    def printname(self):
        super().printname()
        print("I am student")


class Animal():
    def say_something(self):
        print("hi i am animal")

class Cat(Animal):
    def say_something(self):
        super().say_something()
        print("meow")


def average_score():
    total_score = int(input("Enter total score: "))
    num_students = int(input("Enter number of students: "))
    average_score = total_score / num_students
    print("Average score:", average_score)


def add_content_to_my_file(content):
    my_file = open(r"C:\Users\Iliap\PycharmProjects\CoursePython\FunctionsPart2\stam.txt", "a")
    my_file.write(content)
    my_file.close()


class Point:

    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def move(self):
        print("moving")

    def draw(self):
        print("drawing")



def main():
    # Use the Person class to create an object, and then execute the printname method:
    x = Point(5, 20)
    x.draw()
    print(x.y)
    x = Person("John", "Doe")
    y = Student("Arja", "stark")
    x.printname()
    y.printname()
    add_content_to_my_file("new content")

    person1 = Person("Arja", "Stark")
    person1.sayHiToOther("John")

    cat1 = Cat()
    cat1.say_something()
    camelcase = CamelCase()
    print(camelcase.hump("how are yopu"))
    table1 = mx.Table()
    table1.who_am_i()


if __name__ == '__main__':
    main()