import math

board = [' ']*9

player = 'X'
ai = 'O'

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(mark):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == mark:
            return True
    return False

def check_draw():
    return ' ' not in board

def minimax(is_ai):
    if check_win(ai):
        return 1
    if check_win(player):
        return -1
    if check_draw():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai
                score = minimax(False)
                board[i] = ' '
                if score > best:
                    best = score
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                score = minimax(True)
                board[i] = ' '
                if score < best:
                    best = score
        return best

def ai_turn():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = ai

print("Tic Tac Toe")
print("Positions: 0 to 8")

while True:
    print_board()
    move = int(input("Your move: "))
    if board[move] != ' ':
        print("Invalid move")
        continue

    board[move] = player

    if check_win(player):
        print_board()
        print("You win")
        break

    if check_draw():
        print_board()
        print("Draw")
        break

    ai_turn()

    if check_win(ai):
        print_board()
        print("AI wins")
        break
