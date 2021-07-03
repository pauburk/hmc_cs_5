# CS5 Gold/Black: Homework 3 Problem 2
# Filename: hw3pr2.py
# Name: Paul Burke
# Problem description: Sleepwalking student

import random
from time import sleep


def rwpos(pos, nsteps):
    """
        rwpos models a random walker that
        * starts at the int input, pos
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker
    """
    sleep(0.1)
    print('location is', pos)
    if nsteps == 0:
        return pos
    else:
        newpos = pos + rs()  # take one step
        return rwpos(newpos, nsteps-1)


def rwsteps(pos, low, high):
    """
        rwsteps models a random walker that
        * starts at the int input, pos
        * goes UNTIL reaching low or hi
          low will always be less than hi

        rwsteps returns the number of steps the
        walker needed to reach the lower or upper bound
    """

    left = pos
    right = high - pos

    if pos <= low:
        # show person in bed emoji
        print('\x1b[0;30;30m' + '\r🛌', ' ' * left, ' ', ' ' * right, '🛁' + '\x1b[0m', sep='', end='', flush=True)
    elif pos >= high:
        # show person in bathtub emoji
        print('\x1b[0;30;45m' + '\r🛏', ' ' * left, '  ', ' ' * right, '🛀' + '\x1b[0m', sep='', end='', flush=True) # add extra space because pos = high
    else:
        # hasn't arrived at bed or bath yet
        print('\x1b[0;30;45m' + '\r🛏', ' ' * left, '🚶', ' ' * right, '🛁' + '\x1b[0m', sep='', end='', flush=True)

    sleep(0.15)

    if pos <= low or pos >= high:
        return 0

    else:
        newpos = pos + random.choice([-1, 1])
        # newpos = pos + 1
        return 1 + rwsteps(newpos, low, high)


def main():

    print("***WARNING!!! IF HIGH - LOW < 8 GRAPHICS WILL NOT WORK***") # because I want to print Bed and Bathroom

    # input lower bound
    low = input("Lower bound? ")
    while not low.isnumeric(): low = input("Please enter a valid lower bound. ") # make sure low is a number
    low = int(low)

    # get higher bound
    high = input("Higher bound? ")
    # make sure high is a number and it fits the graphics limitations
    # this checks first if high is a number and then only if it is will it check the bounds
    while not high.isnumeric() or int(high) - int(low) < 8:
        if not high.isnumeric():
            high = input("Please enter a valid higher bound. ")
        else:
            high = input("Please enter a valid higher bound (if high - low < 8 the graphics won't work). ")
    high = int(high)

    # get starting position
    pos = input("Starting position? ")
    while not pos.isnumeric() or not low < int(pos) < high:
        if not pos.isnumeric():
            pos = input("Please enter a valid starting position. ")
        else:
            pos = input("Please enter a starting position between low and high. ")
    pos = int(pos)

    # account for if low is not 0
    high -= low
    pos -= low
    low = 0

    # print(f"Low : {low}\nHigh : {high}\nPos : {pos}")
    print('\x1b[0;30;45m' + 'Bed', ' ' * (high - low - 8), 'Bathroom' + '\x1b[0m')
    steps = rwsteps(pos, low, high)
    print(f"\nCompleted in {steps} steps.")


main()


"""
    How I got the highlight
    From https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
"""
# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(30,38):
#             s1 = ''
#             for bg in range(40,48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')
