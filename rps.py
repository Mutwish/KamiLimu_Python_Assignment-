# Tracy Otieno
# homework_1.4.py
# May 4, 2017
 
# rock, paper, scissors
import random


a = input("Player 1:Choose rock, paper, or scissors:")
b = input("Player 2:Choose rock, paper, or scissors:")

def compare(a,b):
    if a == b:
        return("It's a tie!")
    elif a == 'rock':
        if b == 'scissors':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif a == 'scissors':
        if b == 'paper':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif a == 'paper':
        if b == 'rock':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(a, b))
   

    
