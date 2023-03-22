#  File: Handicap.py
#  Description: Calculates a bowler's average & handicap after 3 games
#  Student's Name: K. Amber Vasquez 
#  Student's UT EID: kav835
#  Course Name: CS 303E 
#  Unique Number: 50180 
#
#  Date Created: Feb 4, 2020
#  Date Last Modified:Feb 6, 2020

def main ():

    # Prompt the user to enter three bowling games
    game1 = int(input ( "Enter Game 1: "))
    game2 = int(input ( "Enter Game 2: "))
    game3 = int(input ( "Enter Game 3: "))
    print ()

    # Calculate the bowler's average 
    average = int ((game1 + game2 + game3) / 3)
    print ("The bowler's average is:",average)

    # Calculate the bowler's handicap
    handicap = int ((200 - average) * .80)
    print ( "The bowler's handicap is:",handicap)
    
main()
 
