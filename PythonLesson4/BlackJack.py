import random


player_score = 0

while player_score < 21:
    print(f"your current score is {player_score}")
    player_choice = input("do you want to continue the game?: (y/n) ")
    if player_choice == "y":
        random_number = random.randint(1, 10)
        player_score += random_number
    else:
        break
print(f"the players score is {player_score}")
if player_score == 21:
    print("the Player won!")
elif player_score > 21:
    print("the player lost!")
