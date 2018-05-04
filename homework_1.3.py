# Tracy Otieno
# homework_1.3.py
# May 4, 2017
 
# Prints a tic tac toe board

#use of variables for less typing

t = "board"


def draw():
    # initialize an empty board
    t = ""

    #  a standard tic-tac-toe board has 5 rows so 
    for i in range(5):
        # switch between printing vertical and horizontal bars
        if i%2 == 0:
            t += "|    " * 4
        else:
            t += " --- " * 3
         
        t += "\n"

    print(t)

draw()
