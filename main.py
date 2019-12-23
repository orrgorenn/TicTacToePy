import math

gameBoard = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

scoreForMM = {
    'X': 10,
    'O': -10,
    'tie': 0
}

ai = 'X'
human = 'O'
current_player = human

def print_board():
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print("- + - + -")
    print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print("- + - + -")
    print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
    print()

    if check_winner() == 'tie':
        print("It's a tie")
        exit(1)
    elif check_winner() == ai:
        print("You lost! LOSER!")
        exit(1)
    elif check_winner() == human:
        print("Congratz! you won!")
        exit(1)

def bestMoveForAi():
    global current_player
    # AI Player
    bestScore = -math.inf
    i = 0
    bestMove = 0
    while i < len(gameBoard):
        if gameBoard[i] == ' ':
            gameBoard[i] = ai
            score = minimax(gameBoard, 0, False)
            gameBoard[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
        i += 1
    gameBoard[bestMove] = ai
    current_player = human
    user_turn()

def user_turn():
    global current_player

    print_board()
    if current_player == human:
        pos = input("Choose your position (1-9): ")
        pos = int(pos)
        while pos < 1 or pos > 9 or gameBoard[pos - 1] != ' ':
            pos = int(input("Wrong place. Please choose again: "))
        gameBoard[pos - 1] = current_player
        current_player = ai
        bestMoveForAi()

def start_game():# Display initial board
    print_board()
    print("Let the games begin...\n")
    bestMoveForAi()

def check_winner():
    winner = None

    if gameBoard[0] == gameBoard[1] == gameBoard[2] != ' ':
        winner = gameBoard[0]
    if gameBoard[3] == gameBoard[4] == gameBoard[5] != ' ':
        winner = gameBoard[3]
    if gameBoard[6] == gameBoard[7] == gameBoard[8] != ' ':
        winner = gameBoard[6]
    if gameBoard[0] == gameBoard[3] == gameBoard[6] != ' ':
        winner = gameBoard[0]
    if gameBoard[1] == gameBoard[4] == gameBoard[7] != ' ':
        winner = gameBoard[1]
    if gameBoard[2] == gameBoard[5] == gameBoard[8] != ' ':
        winner = gameBoard[2]
    if gameBoard[0] == gameBoard[4] == gameBoard[8] != ' ':
        winner = gameBoard[0]
    if gameBoard[2] == gameBoard[4] == gameBoard[6] != ' ':
        winner = gameBoard[2]

    openSpots = 0
    for i in gameBoard:
        if i == ' ':
            openSpots += 1
    if winner == None and openSpots == 0:
        return 'tie'
    else:
        return winner

def minimax(board, depth, isMaximizing):
    result = check_winner()

    if result is not None:
        score = scoreForMM[result]
        return score

    if isMaximizing:
        bestScore = -math.inf
        i = 0
        while i < len(gameBoard):
            if gameBoard[i] == ' ':
                gameBoard[i] = ai
                score = minimax(gameBoard, depth + 1, False)
                gameBoard[i] = ' '
                bestScore = max(score, bestScore)
            i += 1
        return bestScore
    else:
        bestScore = math.inf
        i = 0
        while i < len(gameBoard):
            if gameBoard[i] == ' ':
                gameBoard[i] = human
                score = minimax(gameBoard, depth + 1, True)
                gameBoard[i] = ' '
                bestScore = min(score, bestScore)
            i += 1
        return bestScore

if __name__ == "__main__":
    start_game()