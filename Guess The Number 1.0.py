"""
In this version of the game, the user guesses a random number
"""

import random

# I used the module below, in order to convert 1 to 1st, 2 to 2st etc
import inflect


num = input('Please type an integer number as an upper bound: ')

def User_Guess(num):
    
    """
    We check if the upper bound is valid or not
    We just want an integer number
    """
    if num.isdigit():
        print('Let the game begin')
        num = int(num)
    else:
        print('You have to type a valid number! Try Again!')

        
    limits = random.randint(1, num)
    guess = None
    count = 1

    
    """
    Here we make and count the guesses each time
    """
    
    while guess != limits:
        guess = int(input(f'Please type the number of your choice, between 1 and {str(num)}: \n'))

        if guess == limits:
            print(f'\n You got the secret number right!')
            num_to_letters = inflect.engine()
        else:
            count += 1
            print('Please try again')

    print(f'\n You got it! On the {num_to_letters.ordinal(count)} guess')


User_Guess(num)
