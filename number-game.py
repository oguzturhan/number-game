# A simple number guess game
# Do you wanna try?

import random
import os
import time

cont = 'y'
while cont == 'y':
    os.system('cls')
    print('I want to play a game...')
    live = int(input('How many lives do you want? :'))
    print('Now.. Guess the number in my mind.  It is between 0-100')
    number = random.randint(0, 100)
    counter = live
    for a in range(0,live):
        print(f'Lives :{counter}')
        guess = int(input('Guess :'))
        counter -= 1
        if guess == number:
            print(f'Congrats! Win!!! Correct number is: {guess}')
            break
        elif guess > number and counter > 0:
            os.system('cls')
            print('Enter smaller number!')
        elif guess < number and counter > 0:
            os.system('cls')
            print('Enter bigger number!')
        else:
            print('Game Over')
    cont = input('Do you want another game? y / n :')
print('Bye .....')    
time.sleep(3)
