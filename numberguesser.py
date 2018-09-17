# Roshni Surpur
# 9/17/18
# this code is a guessing game, that makes user guess a number from 1-10

import random
import math

number=random.randint(0,10)
def guessing():
    guess=float(input("\nGuess the number between 0 and 10 \n"))
    if guess<=10:
        if guess==number:
            print("you win")
        elif guess>number:
            print("think lower")
            guessing()
        elif guess<number:
            print("think higher")
            guessing()
        else:
            print("error. try again")
            guessing()
    else:
        print("type a number under 10. ")
        guessing()
guessing()
