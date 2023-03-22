#  File: Deal.py
#  Description: Let's Make a Deal simulaiton 
#  Student's Name: Amber
#  Date Created: March 30, 2020
#  Date Last Modified: March 31, 2020


import random


def roll (n):
    return random.randint (1,n)

def runOneTrial ():
    prize = roll (3)
    guess = roll (3)
    view = 0
    newGuess = 0
    
    for i in range (1,4):
        if i != prize and i != guess:
            view = i
    
    for i in range (1,4):
        if i != view and i != guess:
            newGuess = i
            
    print (format(prize,'^6d'),format(guess,'^6d'),format(view,'^6d'),format(newGuess,'^8d'))

    if guess == prize:
        return 1
    return 0
        
    

def main ():

    x = int(input(" How many trials do you want to run? "))
    total = 0

    print ("")
    print (format(" Prize",'6s'),format("Guess",'6s'),format("View",'6s'),format("New Guess",'8s'))
    

    for i in range (0 , x + 1):
        total = runOneTrial() + total
        

    probability = (total/x)
    print ("")
    print (" Probability of winning if you switch =",format(probability,'3.2f'))
    print (" Probability of winning if you do not switch =", format(1 - probability,'3.2f'))
        
        
main ()

