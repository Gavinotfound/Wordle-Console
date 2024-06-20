import csv
from random import *


class color:
    ELOCATION = '\033[33;3m'
    ERROR = '\033[37m'
    CORRECT = '\033[32;1m'


print("\x1b[36;1m")
with open('valid-words.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    AL = list(csv_reader)
with open('word-bank.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    BR = list(csv_reader)
print('Loaded...')
CoW = list(choice(BR)[0])
f = 1  # Guess#
while f < 6:
    CoC = [0, 0, 0, 0, 0]
    print('Guess #', f)
    guess = input("Guess:")
    CL = 0
    for VW in AL:
        if guess == VW[0]:
            break
        else:
            CL += 1
            if CL == len(AL):
                guess = ""
    if len(guess) == 5:
        guess = list(guess)
        p = 1  # Character in Word (Current position)
        for i in guess:
            if type(i) is not str:
                print("Invalid")
            else:
                for j in CoW:
                    if i == j:
                        if guess.index(i) == CoW.index(j):
                            CoC[p - 1] = 2
                        else:
                            CoC[p - 1] = 1
                p += 1
        f += 1
        if CoC == [2, 2, 2, 2, 2]:
            print("You Win!")
            break
    else:
        print("Invalid")
    idiw = 0
    for k in guess:
        if k == CoW[idiw]:
            print('\033[32;1m', k, '\033[32;1m', end='')
        elif k in CoW:
            print('\033[33;3m', k, '\033[33;3m', end='')
        else:
            print('\033[37m', k, '\033[37m', end='')
        idiw += 1
    print("\x1b[36;1m")
print("The word was " + f"\033[32;1m{CoW[0] + CoW[1] + CoW[2] + CoW[3] + CoW[4]}\033[32;1m")
