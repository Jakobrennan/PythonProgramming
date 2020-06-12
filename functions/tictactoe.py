
# global vars
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# instructions
def instructions():
    """Display game instructions"""
    print("""
    welcome to tic tac toe
    you vs the computer

    enter number between 0 - 8
    you number corresponds with where you want it places on the board layout
    below

            0  |  1  |  2
           ----+-----+----
            3  |  4  |  5
           ----+-----+----
            6  |  7  |  8

    prepare, we are about to start...
    """)

def ask_question(question):
    """ask simple questions"""
    response = None
    while response not in ("y", "n"):
        response = raw_input(str(question) + "(answer with 'y' or 'n')").lower()
    return response

def ask_number(question, low = 0, high = 8):
    """for number between range"""
    response = None
    while response not in range(low, high):
        response = int(raw_input(str(question) + "(answer within "+str(low)+" and " +str(high)+")").lower())
    return response

def pieces():
    """determine who goes first"""
    first = ask_question("do you want the first move?")
    if first == "y":
        print("\ntake the fist move")
        human = X
        computer = O
    else:
        print("\ngood luck")
        human = O
        computer = X
    return computer, human

def new_board():
    """generate new board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """display game board"""
    print("\n\t" + board[0] + "|" + board[1] + "|" + board[2])
    print("\t-------")
    print("\t" + board[3] + "|" + board[4] + "|" + board[5])
    print("\t-------")
    print("\t" + board[6] + "|" + board[7] + "|" + board[8])

def legal_move(board):
    """create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """determine game winner"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
        return None

def human_move(board, human):
    """get human move"""
    legal = legal_move(board)
    move = None
    while move not in legal:
        move = ask_number("what's your move?", 0, NUM_SQUARES)
        if move not in legal:
            print("\nalready occupied space")
    print("fine")
    return move

def computer_move(board, computer, human):
    """hangles computers move"""
    board = board[:] #copy of mutable variable
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("computer will pick move : ")
    # checks for win
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #undoes move
        board[move] = EMPTY
    #checks if human can win
    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #resets
        board[move] = EMPTY
    #no winners so makes move
    for move in BEST_MOVES:
        if move in legal_move(board):
            print(move)
            return move

def nex_move(turn):
    """chooses turn"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """congrats to winner"""
    if the_winner != TIE:
        print(the_winner + " WON!\n")
    else:
        print("it's a tie")

    if the_winner == computer:
        print("computer won, try again")
    elif the_winner == human:
        print("you beat a computer, well done")
    elif the_winner == TIE:
        print("because it's a tie, you should try again")

def main():
    instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = nex_move(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

main()
print("press any key")
