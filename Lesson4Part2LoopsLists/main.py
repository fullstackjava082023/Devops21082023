# input numbers till user input -1
# print count how many inputs he gave
# print sum
# print average

count = 0
sum = 0
while True:
    number = int(input("enter the number -1 to exit: "))
    if number == -1:
        break
    count += 1
    sum += number


print(f"count is {count}")
print(f"sum is {sum}")
print(f"the average is {sum/count}")
print("outside loop")