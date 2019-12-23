import random

gameBoard = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]

winner = None
current_player = 'X'
game_not_over = True

def print_board():
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print("- + - + -")
    print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print("- + - + -")
    print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
    print()

def handle_turn(player):
    if player == 'O':
        pos = input("Choose your position (1-9): ")
        pos = int(pos)
        while pos < 1 or pos > 9 or gameBoard[pos - 1] != ' ':
            pos = int(input("Wrong place. Please choose again: "))
    elif player == 'X':
        pos = random.randint(0, 9)
        while gameBoard[pos - 1] != ' ':
            pos = random.randint(0, 9)
    gameBoard[pos - 1] = player
    print_board()

def flip_player():
    global current_player

    if (current_player == 'X'):
        current_player = 'O'
    else:
        current_player = 'X'

def start_game():
    global winner

    # Display initial board
    print_board()
    print("Let the games begin...\n")
    while game_not_over:
        handle_turn(current_player)
        is_game_over()
        flip_player()
    if winner is not None:
        print("Congratulations! " + winner + " won!")
    else:
        print("GAME OVER - A Tie...")

def check_winner():
    global winner

    if gameBoard[0] == gameBoard[1] == gameBoard[2] != ' ':
        winner = gameBoard[0]
        return True
    if gameBoard[3] == gameBoard[4] == gameBoard[5] != ' ':
        winner = gameBoard[3]
        return True
    if gameBoard[6] == gameBoard[7] == gameBoard[8] != ' ':
        winner = gameBoard[6]
        return True
    if gameBoard[0] == gameBoard[3] == gameBoard[6] != ' ':
        winner = gameBoard[0]
        return True
    if gameBoard[1] == gameBoard[4] == gameBoard[7] != ' ':
        winner = gameBoard[1]
        return True
    if gameBoard[2] == gameBoard[5] == gameBoard[8] != ' ':
        winner = gameBoard[2]
        return True
    if gameBoard[0] == gameBoard[4] == gameBoard[8] != ' ':
        winner = gameBoard[0]
        return True
    if gameBoard[2] == gameBoard[4] == gameBoard[6] != ' ':
        winner = gameBoard[2]
        return True
    return False

def check_full_board():
    for i in gameBoard:
        if i == ' ':
            return False
    return True

def check_tie():
    if check_winner() == False and check_full_board() == True:
        return True
    return False

def is_game_over():
    global game_not_over
    game_not_over = not (check_tie() or check_winner())

if __name__ == "__main__":
    start_game()