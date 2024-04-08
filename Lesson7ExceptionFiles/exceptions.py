def firstExample():
    try:
        age = int(input("enter the age: "))
        risk = 2000/age
        print("the risk is: ", risk)
    except ValueError:
        print("enter correct input - only numbers allowed: ")
    except ZeroDivisionError:
        print("input zero not possible: ")

def divide():
    while True:
        try:
            numerator = float(input("enter the numerator: "))
            denominator = float(input("enter the denominator: "))
            print(numerator / denominator)
        except ZeroDivisionError:
            print("denominator cannot be 0 (zero division not allowed)")
        except ValueError:
            print("only float numbers are allowed (wrong input) ")
        #check if we want one more iteration
        one_more = input("do you want to continue? yes/no: ")
        if one_more == "no":
            break
    print("exit")

def average_score():
    try:
       total_score = int(input("Enter total score: "))
       num_students = int(input("Enter number of students: "))
       average_score = total_score / num_students
       print("Average score:", average_score)
    except ZeroDivisionError:
        print("number of students cannot be zero")
    except ValueError:
        print("number of students and total score must be numeric")
# What is doing this Python code snippet?
# What is the expected output of this code when executed in Python?
# What happens in the inner except block if a ZeroDivisionError occurs during the inner division in Python?
# What is the order of execution for the finally blocks when an exception is thrown in Python?
# If you remove the division by zero in the outer try block, what will be the output of the Python code?

def what_the_code_is_doing():
    try:
        print("Outer Try Block - Start")
        result = 10 / 5
        print("Result:", result)  # This line won't be reached.
        print("Outer Try Block - End")
    except ZeroDivisionError:
        print("Outer Catch Block (ZeroDivisionError)")
        try:
            print("Inner Try Block - Start")
            result = 20 / 0
            print("Result:", result)
            print("Inner Try Block - End")
        except ZeroDivisionError:
            print("Inner Catch Block (ZeroDivisionError)")
        finally:
            print("Inner Finally Block")
    finally:
        print("Outer Finally Block")

# Outer Try Block - Start
#"Result:",2)
#"Outer Try Block - End"

# Inner Finally Block
# Outer Finally Block

def raise_exception():
    x = 1
    try:
        if x < 0:
            raise ZeroDivisionError("Sorry, no numbers below zero")
    except ZeroDivisionError :
        print("value error happened")
    finally:
        print(x)


# Ask user to enter his weight.
# In case input <= 0 raise TypeError with the text: Only positive numbers are allowed
# If weight > 100 print too much
# If weight < 40 print too low
# If weight between 40 and 100 print -> good weight
def checking_weight():
    weight = float(input("enter your weight: "))
    if weight <= 0:
        raise TypeError("only positive numbers allowed")
    if weight < 40:
        print("too low")
    elif 40 <= weight <= 100:
        print("good weight")
    else:
        print("too big")




def main():
    # divide()
    # average_score()
    # try:
    #     l1 = [1, 2]
    #     print(l1[0]) # here we have error
    #     print("finished the code")
    # except IndexError:
    #     print("caught index error")
    # finally:
    #     print("this is always printed")
    # what_the_code_is_doing()
    # raise_exception()
    checking_weight()


if __name__ == '__main__':
    main()