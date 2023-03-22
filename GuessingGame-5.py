#  File: GuessingGame.py
#  Description: Allows the user to play a guessing game with 10 tries
#  Student's Name: Amber
#  Date Created: 2/23/20
#  Date Last Modified: 2/27/20

def main():

    secretNumber = 1458

    guessIsCorrect = False

    # Welcome the user and prompt the user to enter a guess
        
    print ("Welcome to the guessing game.  You have ten tries to guess my number.")

    for count in range (1,11):

        # prompt the user to enter a guess
        
        number = int(input("Please enter your guess: "))

        # verify that each guess is positive and less than 10000.
        while (number <= 0 or number >= 10000):
            print("Your guess must be between 0001 and 9999.")
            number = int(input("Please enter a valid guess: "))
                
        if (number == secretNumber) and (count == 1):
            # If the user has entered a correct guess
            print("That's correct!")
            print("Congratulations! You guessed it on the first try!")
            guessIsCorrect = True
            break
                
        elif (number == secretNumber):
            # If the user has entered a correct guess
            print("That's correct!\nCongratulations! You guessed it in",count,"guesses.")
            guessIsCorrect = True
            break
                
        elif (number < secretNumber):
            # If the user's guess is low
            print ("Your guess is too low.")
            print ("Guesses so far:",count)
            
                
        elif(number > secretNumber):
            #if user's guess is too high
            print("Your guess is too high.")
            print ("Guesses so far:",count)
            

    # If the guess was the user's tenth guess
    # Your program should then terminate
    if not guessIsCorrect:
        print("Game over: you ran out of guesses.")




main ()
