import random
import os
import time

a = 0
cont = 'y'
while cont == 'y':
    os.system('cls')
    print('I want to play a game...')
    live = int(input('How many lives do you want? :'))
    print('Now.. Guess the number in my mind.  It is between 0-100')
    number = random.randint(0, 100)
    kalan = live
    for a in range(0,live):
        print(f'Lives :{kalan}')
        tahmin = int(input('Guess :'))
        kalan = kalan - 1
        if tahmin == number:
            print(f'Congrats! Win!!! Correct number is: {tahmin}')
            break
        elif tahmin > number and kalan > 0:
            os.system('cls')
            print('Enter smaller number!')
        elif tahmin < number and kalan > 0:
            os.system('cls')
            print('Enter bigger number!')
        else:
            print('Game Over')
    cont = input('Do you want another game? y / n :')
print('Bye .....')    
time.sleep(3)