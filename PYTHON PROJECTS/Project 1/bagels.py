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
    Pico    One digit is correct but in the wrong position
    Fermi   One digit is correct and in the right position 
    Bagels  No digits are correct

For example, if the secret number was 248 and your guess was 843, 
the clues would be Fermi Pico""".format(NUM_DIGITS)
)