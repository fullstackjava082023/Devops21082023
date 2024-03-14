import random
### rock paper scissors
# 0 - rock
# 1 - paper
# 2 - scissors
# computer move - random number between 0 to 2
computer_move = random.randint(0,2)
if computer_move == 0:
    verbal_computer_move = "Rock"
elif computer_move == 1:
    verbal_computer_move = "Paper"
else:
    verbal_computer_move = "Scissors"
# player move - input
player_move = int(input("Make a move 0/Rock, 1/Paper, 2/Scissors"))
if player_move == 0:
    verbal_player_move = "Rock"
elif player_move == 1:
    verbal_player_move = "Paper"
else:
    verbal_player_move = "Scissors"
print(f"The player choose: {verbal_player_move} and computer choose: {verbal_computer_move}")
# all draw options
if player_move == computer_move:
    print("The game ended in DRAW")
# all computer win options
elif (computer_move == 0 and player_move == 2) or (computer_move == 1 and player_move == 0) or (computer_move == 2 and player_move == 1):
    print("The game over COMPUTER wins!")
else:
    print("The game over PLAYER wins!")