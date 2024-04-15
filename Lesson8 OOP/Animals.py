class Animal():
    def say_something(self):
        print("Hi I am animal")

    def grow(self):
        print("growing")

    def walk(self):
        print("Walking")

class Cat(Animal):
    def say_something(self):
        # say something of animal
        super().say_something()
        print("Meow")

    def walk(self):
        print("I am cat")
        super().walk()

class Dog(Animal):
    def walk(self):
        print("The dog is walking")

    def say_something(self):
        print("Woof")

class Fish(Animal):
    pass


def main():
    animal1 = Animal()
    animal1.walk()
    dog1 = Dog()
    dog1.walk()
    cat1 = Cat()
    cat1.walk()
    # # dog1 = Dog()
    # # fish1 = Fish()
    # cat1.say_something() #Hi I am animal
    # # dog1.say_something() #woof
    # # fish1.say_something() #Hi I am animal Meow
    # # animal1 = Dog()
    # # animal1.say_something()
    # # cat2 = Fish()
    # # cat2.say_something()


if __name__ == '__main__':
    main()