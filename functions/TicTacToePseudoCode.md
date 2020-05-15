# pseudo code for `tic tac toe` game

display instructions
generate board
decide who plays first
while no winners:
    if players turn:
        prompt move
        check move()
        update board()
    else:
        generate random move for computer


check move():
    are 3 places in a row()
        yes - return won
        no - break

    is spot already filled?:
        yes - you can't move there
        no - allow move

update board():

