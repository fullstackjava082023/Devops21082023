

def switchMove(current_move):
    if current_move == "X":
        current_move = "O"
    else:
        current_move = "X"

def make_move():
    pass

def print_board():
    pass


def check_vertikal():
    pass


def check_horizontal():
    pass


def check_diagonal():
    pass


def check_win():
    check_vertikal()
    check_horizontal()
    check_diagonal()
    pass


def check_tekko():
    pass


def check_game_over():
    check_win()
    check_tekko()
    pass


board = [["_","_","_"],["_","_","_"],["_","_","_"]]    
current_move = "X"

while True:
    make_move()
    print_board()
    check_game_over()
    switchMove(current_move)
    