# CS5 Gold/Black: Homework 3 Problem 2
# Filename: hw3pr2.py
# Name: Paul Burke
# Problem description: Sleepwalking student

import random
from time import sleep
import numpy as np
import os
import math
import unicodedata # for getting widths of emojis


def print_room(grid, grid_disp, x, y):
    """
        prints room based on numpy array with integers corresponding
        to display characters for the player, spaces, and destinations
    """

    # prints top wall
    print("+", end="")
    for i in range(x+1):
        print("-", end="")
    print("+")

    # prints grid
    for row in grid:
        print("|", end=" ")
        for n in row:
            print("\b"*(grid_disp[n]["width"]-1) + grid_disp[n]["disp"], end="") # go back a space if the character is wide
        print("|")

    # prints bottom wall
    print("+", end="")
    for i in range(x+1):
        print("-", end="")
    print("+")


def rwsteps(grid, grid_disp, pos, dests, x, y, steps=1):
    """
        models a random walker in a 2d room who must reach one of the destinations

        rwsteps returns the number of steps the walker needed to reach
        a destination, as well as the destination reached
    """

    print_room(grid, grid_disp, x*2, y)

    sleep(0.1)

    for k, v in dests.items():
        if pos["x"] == v["x"] and pos["y"] == v["y"]:
            return [steps, v["desc"]]

    grid = set_loc(grid, pos, "0") # clear old position
    if random.choice(["x", "y"]) == "x":
        pos["x"] += random.choice([-1, 1])
    else:
        pos["y"] += random.choice([-1, 1])

    # stop at walls
    if pos["x"] >= x: pos["x"] = x-1
    if pos["y"] >= y: pos["y"] = y-1
    if pos["x"] < 0: pos["x"] = 0
    if pos["y"] < 0: pos["y"] = 0

    grid = set_loc(grid, pos, -1)
    steps += 1
    return rwsteps(grid, grid_disp, pos, dests, x, y, steps)


def set_loc(grid, dict, target):
    """
        changes the value in the numpy array to be target
    """
    grid[dict["y"], dict["x"]*2] = int(target)
    return grid


def get_dist(p1, p2):
    """
        gets the distance between p1 and p2 in the array, using the pythagorean theorem
    """
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )


def setup():
    """
        sets up the simulation
            * user input if they want to input things
            * or presets
            * or randomly generated stuff
            * you pick!
    """

    mode = input("Do you want to play Preset 1, Preset 2, or create your own simulation? (1/2/3) ")
    while mode not in ["1", "2", "3"]: mode = input("Please enter a valid mode. ")

    if mode == "1": # preset 1

        x = 20
        y = 20
        pos = {"x" : 10 , "y" : 10}

        dests = {}
        dests[1] = {'grid_num': 1, 'x': 9, 'y': 0, 'disp': '🎫', 'desc': 'to a movie', 'width': 2}
        dests[2] = {'grid_num': 2, 'x': 2, 'y': 15, 'disp': '🏖', 'desc': 'to the beach', 'width': 1}
        dests[3] = {'grid_num': 3, 'x': 3, 'y': 3, 'disp': '🛍', 'desc': 'shopping', 'width': 1}
        dests[4] = {'grid_num': 4, 'x': 6, 'y': 18, 'disp': '🏓', 'desc': 'play ping-pong', 'width': 2}
        dests[5] = {'grid_num': 5, 'x': 1, 'y': 9, 'disp': '🏟', 'desc': 'to a soccer game', 'width': 1}
        dests[6] = {'grid_num': 6, 'x': 16, 'y': 3, 'disp': '🎠', 'desc': 'to a carnival', 'width': 2}
        dests[7] = {'grid_num': 7, 'x': 13, 'y': 18, 'disp': '🍹', 'desc': 'out for lunch', 'width': 2}
        dests[8] = {'grid_num': 8, 'x': 17, 'y': 14, 'disp': '🏕', 'desc': 'camping', 'width': 1}
        dests[9] = {'grid_num': 9, 'x': 18, 'y': 9, 'disp': '💇', 'desc': 'get your hair cut', 'width': 2}

    elif mode == "2": # preset 2

        x = 40
        y = 20
        pos = {"x" : 5 , "y" : 10}

        dests = {}
        dests[1] = {'grid_num': 1, 'x': 39, 'y': 0, 'disp': '🎫', 'desc': 'to a movie', 'width': 2}
        dests[2] = {'grid_num': 2, 'x': 34, 'y': 8, 'disp': '🏖', 'desc': 'to the beach', 'width': 1}
        dests[3] = {'grid_num': 3, 'x': 33, 'y': 3, 'disp': '🛍', 'desc': 'shopping', 'width': 1}
        dests[4] = {'grid_num': 4, 'x': 36, 'y': 18, 'disp': '🏓', 'desc': 'play ping-pong', 'width': 2}
        dests[5] = {'grid_num': 5, 'x': 33, 'y': 12, 'disp': '🏟', 'desc': 'to a soccer game', 'width': 1}
        dests[6] = {'grid_num': 6, 'x': 36, 'y': 3, 'disp': '🎠', 'desc': 'to a carnival', 'width': 2}
        dests[7] = {'grid_num': 7, 'x': 33, 'y': 18, 'disp': '🍹', 'desc': 'out for lunch', 'width': 2}
        dests[8] = {'grid_num': 8, 'x': 37, 'y': 14, 'disp': '🏕', 'desc': 'camping', 'width': 1}
        dests[9] = {'grid_num': 9, 'x': 38, 'y': 9, 'disp': '💇', 'desc': 'get your hair cut', 'width': 2}

    else:

        # get x dimension; check that it's a number and greater than 5
        x = input("Enter your chosen x-dimension for the room (greater than 5). ")
        while not x.isnumeric() or int(x) <= 5: x = input("Please enter a valid x-dimension. ") if not x.isnumeric() else input("Please enter a valid x-dimension (if x > 5 the graphics won't work). ")
        x = int(x)

        # get y dimension; check that it's a number and greater than 5
        y = input("Enter your chosen y-dimension for the room (greater than 5). ")
        while not y.isnumeric() or int(y) <= 5: y = input("Please enter a valid y-dimension. ") if not y.isnumeric() else input("Please enter a valid y-dimension (if y > 5 the graphics won't work). ")
        y = int(y)

        x_start = int(x/2)
        y_start = int(y/2)

        pos = {"x" : x_start, "y" : y_start} # player always starts in the middle

        # get number of destinations; check that it's a number and that there is enough space for that many destinations
        num_dests = input(f"Enter your chosen number of destinations for this simulation (less than {min(10, int((x+y)/4+1))}). ")
        while not num_dests.isnumeric() or int(num_dests) < 1 or int(num_dests) > int((x+y)/4): num_dests = input("Please enter a valid number of destinations. ") if not num_dests.isnumeric() or int(num_dests) < 1 else input(f"Please enter a valid number of destinations (if num_dests > {min(10, int((x+y)/4+1))} the simulation becomes too complicated). ")
        num_dests = int(num_dests)

        # whether user wants to enter destinations
        random_gen = input("Do you want the (1) destinations and positions to be randomly generated, (2) just the positions, or (3) neither? (1/2/3) ")
        while not random_gen.lower() in "123": random_gen = input("Please enter a valid answer. ")

        if random_gen == "1": # if the user wants to have the computer generate random destinations and positions

            disp = ["🎫", "🏖", "🛍", "🏓", "🏟", "🎠", "🍹", "🏕", "💇"]
            desc = ["to a movie", "to the beach", "shopping", "play ping-pong", "to a soccer game", "to a carnival", "out for lunch", "camping", "get your hair cut"]

            # random order of destinations (for if user only picks 6 total)
            dest_IDs = list(range(10))[1:]
            random.shuffle(dest_IDs) # randomly shuffle list

            dests = {}
            for i in range(num_dests): # for each destination

                # generate positions for destinations
                while True:

                    x1 = random.randrange(0, x-1)
                    y1 = random.randrange(0, y-1)

                    # check that coordinates are not too close to the player's starting position
                    if get_dist((x1, y1), (x_start, y_start)) < (x+y)/6+2: continue

                    # check that coordinates are not too close to other destinations
                    cont = False
                    for k, v in dests.items():
                        if get_dist((x1, y1), (v["x"], v["y"])) < (x+y)/8: cont = True
                    if cont: continue

                    break # if it passes the tests

                # add it to dict of destinations
                num = dest_IDs[i]
                width = 2 if unicodedata.east_asian_width(disp[num-1]) == 'W' else 1 # if character is 2 spaces wide because of stupid emoji things
                dests[num] = {"grid_num" : num, "x" : x1, "y" : y1, "disp" : disp[num-1], "desc" : desc[num-1], "width" : width}


        elif random_gen == "2": # if the user wants to input destinations but not positions

            dests = {}
            for i in range(num_dests):

                # get the display character
                if i+1 in [1]:
                    char = input(f"Enter the {i+1}st destination display character. ")
                elif i+1 in [2]:
                    char = input(f"Enter the {i+1}nd destination display character. ")
                elif i+1 in [3]:
                    char = input(f"Enter the {i+1}rd destination display character. ")
                else:
                    char = input(f"Enter the {i+1}th destination display character. ")

                # check that it's only 1 long and that it hasn't previously been used
                while len(char) > 1 or char in [c for k, v in dests.items() for c in dests[k]["disp"]]: char = input("Please eneter a single character. ") if len(char) > 1 else input("Please eneter a unique character. ")

                desc = input(f"Enter the destination description. ")

                # generate positions for destinations
                while True:

                    x1 = random.randrange(0, x-1)
                    y1 = random.randrange(0, y-1)

                    # check that coordinates are not too close to the player's starting position
                    if get_dist((x1, y1), (x_start, y_start)) < x/3+1: continue

                    # check that coordinates are not too close to other destinations
                    cont = False
                    for k, v in dests.items():
                        if get_dist((x1, y1), (v["x"], v["y"])) < x/4: cont = True
                    if cont: continue

                    break # if it passes the tests

                width = 2 if unicodedata.east_asian_width(char) == "W" else 1 # if character is 2 spaces wide because of stupid emoji things
                dests[i+1] = {"grid_num" : i+1, "x" : x1, "y" : y1, "disp" : char, "desc" : desc, "width" : width}

        else: # if user wants to input everything

            dests = {}
            for i in range(num_dests):

                # get the display character
                if i+1 in [1]:
                    char = input(f"Enter the {i+1}st destination display character. ")
                elif i+1 in [2]:
                    char = input(f"Enter the {i+1}nd destination display character. ")
                elif i+1 in [3]:
                    char = input(f"Enter the {i+1}rd destination display character. ")
                else:
                    char = input(f"Enter the {i+1}th destination display character. ")

                # check that it's only 1 long and that it hasn't previously been used
                while len(char) > 1 or char in [c for k, v in dests.items() for c in dests[k]["disp"]]: char = input("Please eneter a single character. ") if len(char) > 1 else input("Please eneter a unique character. ")

                desc = input(f"Enter the destination description. ")

                # get x coordinate
                x1 = input(f"Enter the x-coordinate for this destination. ")
                while not x1.isnumeric() or not 0 <= int(x1) < x: x1 = input("Please enter a valid x-coordinate. ") if not x1.isnumeric() else input(f"Please enter an x-coordinate inside of the grid (0 to {x}). ")
                x1 = int(x1)

                # get y coordinate
                y1 = input(f"Enter the y-coordinate for this destination. ")
                while not y1.isnumeric() or not 0 <= int(y1) < y: y1 = input("Please enter a valid y-coordinate. ") if not y1.isnumeric() else input(f"Please enter an y-coordinate inside of the grid (0 to {y}). ")
                y1 = int(y1)

                width = 2 if unicodedata.east_asian_width(char) == "W" else 1 # if character is 2 spaces wide because of stupid emoji things
                dests[i+1] = {"grid_num" : i+1, "x" : x1, "y" : y1, "disp" : char, "desc" : desc, "width" : width}

    # create a dict for each thing which needs to be printed on the grid (player, spaces, destinations)
    grid_disp = dests.copy()
    grid_disp[0] = {"grid_num" : 0, "disp" : " ", "width" : 1}
    grid_disp[-1] = {"grid_num" : -1, "disp" : "🚶", "width" : 2}

    # resize terminal window to fake animation
    os.system(f"printf '\e[8;{y+3};{max(60, x*2+4)}t'")

    # create array of 0s to represent grid
    grid = np.array([0 for i in range(y*x*2)]).reshape(y, x*2)

    # -1 shows the player position
    grid = set_loc(grid, pos, -1)

    # 1,2,3,4,...,9 show the destination locations
    for k, v in dests.items():
        grid = set_loc(grid, v, v["grid_num"])

    return [grid, grid_disp, pos, dests, x, y]


def main():

    print("***WARNING!!! SOMETIMES THE PLAYER WILL EAT A DESTINATION INSTEAD OF REACHING IT (I DON'T KNOW WHAT HAPPENS)***")
    print("***ALSO!!! SOMETIMES THE PLAYER WILL APPEAR TO WALK ON TOP OF A DESTINATION. THAT IS BECAUSE SOME EMOJIS TAKE UP 2 SPACES AND IT ACTUALLY ONLY EXISTS IN THE FIRST ONE. SO THEY OVERLAP IN THE GRAPHICS BUT DON'T ACTUALLY TOUCH IN THE COORDINATES.***")

    grid, grid_disp, pos, dests, x, y = setup()

    steps, dest = rwsteps(grid, grid_disp, pos, dests, x, y)

    # resize terminal window so text and final map show
    os.system(f"printf '\e[8;{y+6};{max(60, x*2+4)}t'")

    print(f"\nYou decided to go to {dest} after {steps} steps!")


main()
