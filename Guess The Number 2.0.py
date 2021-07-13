"""
In this version of the game, the computer tries to find out secret number
"""


import random

#I used the module below, in order to convert 1 to 1st, 2 to 2st etc
import inflect

num = int(input('Please type an integer number as an upper bound: '))


def Computer_Choice(num):
    low = 1
    high = num
    choices = ''
    count = 1
    while choices != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low   # Or guess = high, it's the same

        choices = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()

        if choices == 'h':
            high = guess - 1
            count += 1
        elif choices == 'l':
            low = guess + 1
            count += 1

    num_to_letters = inflect.engine()

    print(f'The computer guessed your secret number {guess} correctly, in the {num_to_letters.ordinal(count)} guess')


Computer_Choice(num)
