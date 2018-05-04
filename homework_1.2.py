# Tracy Otieno
# homework_1.2.py
# May 4, 2017
 
# Prints a tic tac toe board

def draw():
    # initialize an empty board
    board = ""

    #  a standard tic-tac-toe board has 5 rows so 
    for i in range(5):
        # switch between printing vertical and horizontal bars
        if i%2 == 0:
            board += "|    " * 4
        else:
            board += " --- " * 3
         
        board += "\n"

    print(board)

draw()
