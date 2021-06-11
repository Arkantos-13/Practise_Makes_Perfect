# First we have to import our modules that we are going to use

import random
import string
import secrets

letters = string.ascii_letters + string.digits + string.punctuation

''''

The most common password generator in Python looks like this...
but let's just be honest guys, no one has passwords like this 
because it's impossible  to remember it 

'''''

k = int(input('How many passwords would you like to get?'))

length = int(input('How long would you like your password to be?'))


print('Your passwords are ready:')


def generator():
    for i in range(k):
        passwords = ' '
        for j in range(length):
            passwords += random.choice(letters)
        print(f'{i+1}: {passwords}')


generator()


# The output for the first generator looks like this:

''''

How many passwords would you like to get?  4
How long would you like your password to be? 13
Your passwords are ready:
1:  u4(4`Hif;(w>z
2:  U}f!]<<]W)]if
3:  {&|0`BA,s:Dr:
4:  XY*{~q7zHYy=l


''''


''''

But this is a really nice password generator because that can actually produce real 
passwords in combination with a secret word you type so you can really remember it

'''


password_user = input('Would you like your final password to have a special word inside? \n'
                      'If yes, then you can type it here: \n')

k = int(input('How many passwords would you like to get? \n'))

length = int(input('How long would you like your password to be? \n'))


def password_generator():
    print('Your passwords are ready: \n')
    for num in range(k):
        for _ in password_user:
            words = []
            words = [secrets.choice(letters) for i in range(length)]
            words[random.randint(1, length-1)] = password_user
            passwords = ''.join(words)

        print(f'{num+1}: {passwords}')

password_generator()

# The output for the last password generator looks like this:

''''

Would you like your final password to have a special word inside? 
If yes then you can type it here:STACK_OVERFLOW
How many passwords would you like to get?4
How long would you like your password to be?13
Your passwords are ready:
1: h:W})HSTACK_OVERFLOW/Hj>z5
2: g-?940STACK_OVERFLOWi6`'0)
3: SSvP|Ps|Wi7STACK_OVERFLOWW
4: MzE`X5c&gXSTACK_OVERFLOWR\

'''
