# CS5 Gold/Black: Homework 0 Problem 2if
# Filename: hw0pr2if.py
# Name: Paul Burke
# Problem description: Interactive fiction game

import random
from time import sleep
import signal # for timeout


"""
    The Maze.

    Notes on how to "win" or "lose" this adventure:
    To win, always go left.
    To lose, go right.
"""

# timeout on input function
# from https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
def interrupted(signum, frame): # when time runs out
    print('Too slow! You need to decide faster.', end = " ")
    sleep(1)
    if input("Play again? (y/n) ") == "y":
        print()
        adventure(play_again = True, user_name = user_name)

signal.signal(signal.SIGALRM, interrupted)

def input_timeout(message):
    try:
            print(message, end = "")
            temp = input()
            return temp
    except:
            return


def adventure(play_again = False, user_name = "Parzival"): # so when you play again you don't get prompted for your name

    """
        This function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        Arguments: no arguments (prompted text doesn't count as an argument)
        Results: no results     (printing doesn't count as a result)
    """

    choices = []

    if not play_again:
        sleep(2)
        user_name = input("What do they call you, worthy adventurer? ")

    sleep(2)
    print("Welcome,", user_name + ", to the Labyrinth...")
    sleep(3)
    print("Your quest is to find the temple in the center of the labyrinth and escape with the treasure.")
    sleep(3)
    print("There is only one path which will not kill you.")

    sleep(3)
    print("You enter the maze, and are immediately confronted with a perpendicular corridor.")
    sleep(3)
    choices.append(input("Do you go left or right? (l/r) "))

    if choices[0] == "l":

        sleep(3)
        if input("Do you want to restart? You only get one chance. (y/n) ") == "y":
            print()
            adventure(play_again = True, user_name = user_name)

        sleep(3)
        print("May God go with you.")
        sleep(3)
        print("You walk down the corridor, though you think it is more like a tunnel.")
        sleep(3)
        print("You hear a low growling behind you, and look back. But it is too dark to make out anything.")
        sleep(4)

        # timeout

        signal.alarm(3) # timeout after 3 seconds
        ans = input_timeout("You hear a loud roar just as you reach an T. Quick! Do you go left, straight, or right? (l/s/r) ")
        signal.alarm(0) # disable the alarm after success

        if ans != None: # if quester input something
            choices.append(ans)
        else:
            sleep(2)
            if input("Play again? (y/n) ") == "y":
                print()
                adventure(play_again = True, user_name = user_name)

    else: # GAME OVER

        sleep(3)
        print("You quickly come to a room with 12 doors. When you enter, a hidden slab of stone crashes down behind you, blocking your way back.")
        sleep(4)
        print("Water starts filling the room. You can see that if you don't choose a door, you will drown.")
        sleep(4)

        # timeout

        ans = None # only continue if the quester input something

        signal.alarm(6) # timeout after 6 seconds
        ans = input_timeout("Which door do you choose? (1-12) ")
        signal.alarm(0) # disable the alarm after success

        if ans != None:
            sleep(2)
            print("The door doesn't open, and the water starts coming in faster!")

            sleep(2)
            signal.alarm(4) # timeout faster
            ans = input_timeout("Quick! Choose another door (1-12) ")
            signal.alarm(0) # disable the alarm after success

        if ans != None:
            sleep(2)
            print("This one doesn't open either! By now you are swimming. The doors are underwater.")

            sleep(2)
            signal.alarm(2) # timeout faster
            ans = input_timeout("You only have one more chance! You may still escape! Choose a door! ")
            signal.alarm(0) # disable the alarm after success

        if ans != None:
            sleep(2)
            print("When the last door won't open, you scream, forgetting you are underwater. The water bubbles into your mouth, choking you. A valiant attempt.")

        sleep(2)
        if input("Play again? (y/n) ") == "y":
            print()
            adventure(play_again = True, user_name = user_name)


    if len(choices) > 1 and choices[1] == "l":

        sleep(3)
        print("Whewww! That was a narrow escape! The growls fade into the distance.")
        sleep(4)
        print("You continue along this corridor for what seems like eternity.")
        sleep(4)
        print("Your legs feel like they are about to fall off when you reach an underground pool.")
        sleep(4)
        print("You can see the temple! It is on the other side of the water.")
        sleep(4)
        print("You also notice a path along the left-hand side of the pool. It looks very narrow, and you could easily fall into the water.")
        sleep(4)
        choices.append(input("Do you brave the treacherous path, or do you rest your weary legs and swim accross? (p/w) "))

    elif len(choices) > 1: # GAME OVER

        sleep(3)
        print("You escaped the monster! But...in your haste you run right into an abyss and break your neck.")
        sleep(1)
        if input("Play again? (y/n) ") == "y":
            print()
            adventure(play_again = True, user_name = user_name)


    if len(choices) > 2 and choices[2] == "p":

        sleep(3)
        print("Wow! You made it across along the path, but your legs collapse out from under you when you reach the far side.")
        sleep(4)
        print("After resting for a while, you stand up and continue into the temple.")
        sleep(4)
        print("The temple is piled with heaps of gold coins, goblets, swords, armour, precious stones, and jewelery!")
        sleep(4)
        print("You have a hard time deciding what to take with you in your rucksack, but eventually settle on some items.")
        sleep(4)
        print("You walk out the other side of the temple, your rucksack bulging.")
        sleep(4)
        print("The road forks. Both paths lead upwards, but you think you can smell something rotten emanating from the right path.")
        sleep(4)
        choices.append(input("Do you take the left or right path? (l/r) "))

    elif len(choices) > 2: # GAME OVER

        sleep(3)
        print("Your legs thank you for your wise decision.")
        sleep(4)
        print("But, only a quarter across the pool, you sense a stirring underneath you!")
        sleep(4)
        print("You swim faster, trying to reach the shore before whatever you had awoken rises from the depths.")
        sleep(4)
        print("But alas! A tentacled sea monster arises and proceeds to devour you. You attempt to fight it off with your sword, but to no avail.")
        sleep(1)
        if input("Play again? (y/n) ") == "y":
            print()
            adventure(play_again = True, user_name = user_name)


    if len(choices) > 3 and choices[3] == "l":

        sleep(3)
        print("Wise choice! After only a short walk, you emerge to the surface, bearing your rucksack full of treasure!")
        sleep(4)
        print("Congratulations! You live happily ever after, have three kids, and buy a large farm with the gold you have gained.")
        sleep(4)

    elif len(choices) > 3:

        sleep(3)
        print("You come accross the decaying body of a giant spider, and begin to feel uneasy.")
        sleep(4)
        print("You turn back, but clumsily stumble on a rock, making a loud noise.")
        sleep(4)
        print("You freeze and wait with baited breath...")
        sleep(4)
        print("But alas! An even bigger spider slowly emerges from a crack in the wall, and while you won the foot race at the village fair you can't outrun the spider! Your sword is no use.")
        sleep(4)
        print("Your last thought is of the decaying spider body which you know you will soon join.")
        sleep(1)
        if input("Play again? (y/n) ") == "y":
            print()
            adventure(play_again = True, user_name = user_name)



def main():
    adventure()


main()
