# CS5 Gold/Black: Homework 0 Problem 2d
# Filename: hw0pr2d.py
# Name: Paul Burke
# Problem description: RPS using data

import random
from itertools import cycle # for fake spinning wheel
import time # for timing the fake spinning wheel
from time import sleep # for fake spinning wheel


def rps():

    """This plays a data-driven game of rock-paper-scissors
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """

    defeaterOf =  { "rock":     "paper",
                    "paper":    "scissors",
                    "scissors": "rock" }

    the_choices = list(defeaterOf.keys())  # the list of keys

    # comments for after

    compwinComments = { "rock":     "I just knew you were going to pick scissors. Ez W.",
                        "paper":    "Fool! Didn't you know rock is chosen 35% of the time?? I win!",
                        "scissors": "Snip snap you lose!"  }

    comploseComments = { "rock":     "Well played! It's not often a mere human can beat me.",
                         "paper":    "Well, scissors is only thrown 29.6% of the time in competitions...",
                         "scissors": "Cheater! I demand a rematch."  }

    tieComment = "Tie! Heads I win tails you lose. Good luck!"

    departingComment = "Better luck next time..."

    # game

    user_in = input("\nChoose your weapon: ") # user's choice, into user
    user_in = user_in.lower() # makes the user's input lower case

    while user_in not in ["rock", "paper", "scissors", "r", "p", "s"]: # check that user input is valid
        print("Please enter a valid input.", end = " ")
        user_in = input("Choose your weapon: ")
        user_in = user_in.lower() # makes the user's input lower case

    if user_in == "r": user_in = "rock" # so I can type in "r" instead of "rock" when testing
    if user_in == "p": user_in = "paper"
    if user_in == "s": user_in = "scissors"

    comp_in = random.choice(the_choices)  # comp chooses from the_choices

    sleep(1)
    print('You chose', user_in)
    print('I chose', comp_in)

    # fake spinning wheel - the computer is "thinking" about who wins :)

    sleep(1)
    t = time.time()
    for frame in cycle(r'-\|/-\|/'):
        if time.time() - t > 3: # wait 3 seconds to stop spinning
            print('\rComputing: ', "Done.", sep='', end='', flush=True)
            break
        print('\rComputing: ', frame, sep='', end='', flush=True)
        sleep(0.2)

    # print results

    sleep(2)
    print()
    if comp_in == user_in:  # a tie!
        print(tieComment)
        print(departingComment)

    # if computer wins
    elif comp_in == defeaterOf[user_in]:  # notice the "look up" in defeaterOf
        print(compwinComments[comp_in])  # note the "look up" in compwinComments
        print(departingComment)

    else:
        print(comploseComments[comp_in]) # and, when needed, in comploseComments

    play_again = True if comp_in == "scissors" and user_in == "rock" else False # mandatory play again if the computer thinks you cheated
    return play_again


def main():
    pa = rps()
    sleep(2)
    while pa or input("Play again? (y/n) ") == "y":
        if not pa: sleep(1) # only wait if user says play again
        pa = rps()
        sleep(2)


main()
