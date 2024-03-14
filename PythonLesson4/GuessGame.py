# Let’s write the script which gives user 3 times to guess the number which computer doing by random from 1 to 5.
# If user win : print “you won”
# If user loose : print “you loose”

import random

random_number = random.randint(1,5)
#1,2,3,4,5
i = 1
while i <= 3:
    print(f"guess number {i}")
    guess = int(input("guess the number from 1 to 5: "))
    if guess == random_number:
        print("You won!")
        break
    else:
        print("your guess was wrong try again")
    i += 1
else:
    print(f"You lost! the number was {random_number}")