# pylint: disable=missing-module-docstring
# This program is about guessing a random number

import random

def guessing_user(baseline_number):
    "This is function implements user guessing random number game"

    random_number = random.randint(1, baseline_number)
    guess = 0

    while guess != random_number :
        guess = int(input(f" Your turn. Guess this random number between 1 \
            and {baseline_number} : "))
        if guess < random_number :
            print("Uhh! Sorry, too low !")
        elif guess > random_number :
            print("Uhh! Sorry, too high!")

    print("Yayy !! You guessed it ;) ")


def guessing_computer(upbaseline) :
    "This function implements a game where a computer try to guess a number we had in mind"

    high = upbaseline
    low = 1
    correct = 'c'
    feedback = ''
    while feedback != correct :
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} a correct (C) number or too low (L) \
or too high (H) ? : ').lower()
        if high == low :
            guess = low
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yayy !! You nailed it, {guess} is the correct number ;)")
    print()


guessing_computer(100)

guessing_user(12)
