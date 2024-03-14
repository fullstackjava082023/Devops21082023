################## Lesson 4 ###################

##### Hazara #####################
# Growing - print only when second number higher than first
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num2 > num1:
#     print("Growing")
# else:
#     print("Not Growing")

# Even Odd - input number print Even if its even print Odd if it is odd
# if else, modulo
# number = int(input("Enter the number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Salary Raise - raise salary by 10%, if > 6000 -> raise salary only by 5%
# salary = int(input("Enter your salary"))
# if salary * 1.1 > 6000:
#     print("your new salary is ", salary * 1.05)
# else: # <= 6000
#     print("your new salary is ", salary * 1.1)

# Mas Ahnasa
# 23000 -> 10%
# 23000 -> 20%
# 74000 -> 30%
# 100000 -> 40%
# >>> -> 50%
# 250000 ->  23000 ->10% ->  2300m
# 250000-23000 = 227000
# 227000 -> 23000 -> 20% -> 4600m
# 227000-23000 = 204000
# 204000 -> 74000 -> 30% -> 22200m
# 204000 - 74000 = 130000
# 130000 -> 100000 -> 40% -> 40000M
# 130000- 100000 = 30000
# 30000 -> 50 % -> 15000M
# 84000.MAS ahnasa
# 250000 - 84000 = 166000Netto
salary = int(input("Enter the salary: "))
mas = 0

if salary < 23000:
    mas = salary * 0.1
elif salary < 46000:
    mas = 23000 * 0.1 + (salary - 23000) * 0.2
elif salary < 120000:
    mas = 23000 * 0.1 + 23000 * 0.2 + (salary - 46000) * 0.3
elif salary < 220000:
    mas = 23000 * 0.1 + 23000 * 0.2 + 74000 * 0.3 + (salary - 120000) * 0.4
else:
    mas = 23000 * 0.1 + 23000 * 0.2 + 74000 * 0.3 + 100000 * 0.4 + (salary - 220000) * 0.5

print(f"The tax amount is: {mas}")