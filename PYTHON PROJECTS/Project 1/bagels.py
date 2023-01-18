""" Project 1, Bagels: Deduce a secret three-digit number based on clues.
Practice using constants.
"""




import random

NUM_DIGITS = 3 # (!) Try to set this to 1 or 10
MAX_GUESSES = 10 # (!) Try to set this to 1 to 100


def main():
    print("""Bagels, a deductive logic game.
By Gabriel Nechifor

I am thinking of a {} - digit number with no repeted digits.
Try to guess what number it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position
    Fermi       One digit is correct and in the right position 
    Bagels      No digits are correct

For example, if the secret number was 248 and your guess was 843, 
the clues would be Fermi Pico""".format(NUM_DIGITS))

    while True: # Main game loop
        # This stores the secret number the player must to guess
        secretNum = getSecretNum()
        print("I am thinking about a number: ")
        print("You have {} guesses to get it.".format(MAX_GUESSES))
        
        numGuesses =  1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looking until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct so break out this loop.
            if numGuesses > MAX_GUESSES:
                print("You run out of guesses!")
                print("The answer was {}.".format(secretNum))

        # Ask the player if they want to play again.
        print("Do you want to play again? (YES or NO)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playng!!!")


def getSecretNum():
    """ Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789") # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """ Return a string with the pico, fermi, bagels clues for a guess
    and secret number pair"""
    if guess == secretNum:
        return "You got it!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # A correct digit is in incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels" # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original 
        # order doesn't give informational away.
        clues.sort()
        # Make a single string from the list of strings clues.
        return " ".join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()