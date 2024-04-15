
#create class person with field name (it is in init function)
# and method talk which print "talk" and create instance of person with your name
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("my name is ", self.name)

    def sayHiToOther(self, otherName):
        # hello from "my name" to othername
        print(f"hello from {self.name}  to {otherName}")

class Student(Person):
    pass

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move(self):
        print("moved")

    def draw(self):
        print("draw")

class Glass:
   def __init__(self, color, price):
       self.color = color
       self.price = price



def main():
    student1 = Student("Rob")
    student1.sayHiToOther("John")
    # glass1 = Glass("green", 20)
    # glass1.price = 10
    # glass1.color = "yellow"
    # print(f"my color is {glass1.color} and my price is {glass1.price}")
    #
    #
    #
    # person1 = Person("John")
    # person1.talk()
    # print(person1.name)  # "Arja"
    # person2 = Person("Ned")
    # person2.name = "Arja"
    # person2.talk()
    # print(person2.name)
    #
    # person2.sayHiToOther("Liran")
    # # instance 1 of point
    # point1 = Point(10,20)
    # # print(point1.x)
    # # instance 2 of point
    # point2 = Point(2,5)
    # print(point2.x) # 2
    # print(point1.y) # 20
    # print(point2.y) # 5
    # p3 = Point(2.5, 3.5)
    # print(p3.y)



if __name__ == '__main__':
    main()