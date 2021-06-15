# CS5 Gold/Black: Problem 2c
# Filename: hw0pr2c.py
# Name: Paul Burke
# Problem description: RPS using control structures

import random
from itertools import cycle # for fake progress bar
from time import sleep # for fake progress bar


def progress(percent=0, width=30):

    """
        This creates a progress bar like below
        [#####                   ] 20%
    """

    left = width * percent // 100
    right = width - left
    print('\rComputing [', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


def rps():

    """
        This plays a game of rock-paper-scissors
        Arguments: none     (prompted text doesn't count as an argument)
        Results: none       (printing doesn't count as a result)
    """

    # inputs

    user_in = input("\nChoose your weapon: ")
    comp_in = random.choice(["rock", "paper", "scissors"])

    while user_in not in ["rock", "paper", "scissors", "r", "p", "s"]:
        print("Please enter a valid input.", end = " ")
        user_in = input("Choose your weapon: ")

    if user_in == "r": user_in = "rock" # so I can type in "r" instead of "rock" when testing
    if user_in == "p": user_in = "paper"
    if user_in == "s": user_in = "scissors"

    sleep(1)
    print("You chose", user_in)
    print("I chose", comp_in)

    # fake progress bar - the computer is "thinking" about who wins :)

    sleep(1)
    for i in range(101):
        progress(i)
        sleep(0.05)

    # print results

    sleep(2)
    print()
    if user_in == comp_in:
        print("Tie!")
        print("Better luck next time...")
    elif user_in == "paper" and comp_in == "rock" or user_in == "scissors" and comp_in == "paper" or user_in == "rock" and comp_in == "scissors":
        print("You win!")
        print("Congratulations!")
    else:
        print("I win!")
        print("Better luck next time...")


def main():
    rps()
    sleep(2)
    while input("Play again? (y/n) ") == "y":
        sleep(1)
        rps()
        sleep(2)


main()
