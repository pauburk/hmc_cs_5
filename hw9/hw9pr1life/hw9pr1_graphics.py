#
# This file needs much attention!  [summer 2017: too long ago!]
#

import matplotlib.pyplot as plt
import numpy as np
import random
from hw9pr1 import randomCells, createBoard, next_life_generation
from matplotlib.colors import LinearSegmentedColormap

border = 2        # The value used in the array for border cells
speed = 0.42      # In seconds between each step
cmap = 'Accent_r' # Default color scheme
dim = 12          # Default side length of grid
steps = 1         # Default steps per click
stepsPer = False  # Going a number of clicks per step is off by default
running = False   # Program not running until activated with click outside
                  # ..the grid

def onclick(event):
    """Handles clicks in plot window"""
    try:          # Light the cell if they clicked in the board
        xcoord = int(round(event.xdata))
        ycoord = int(round(event.ydata))
        if array[ycoord][xcoord] != border: # border cells don't change
                square = not array[ycoord][xcoord]
                array[ycoord][xcoord] = int(square)
                update(array)
    except:       # If click is outside board, change whether simulator
                  # ..is running
        global running
        if running:
            running = False
            plt.title('Not Running')
            update(array)
        else:
            running = True
            plt.title('Running')
            runsim()

def update(array):
    """Redraw the grid based on modifications to array."""
    ax.imshow(array, cmap = cmap)
    plt.draw()

def graph(array):
    """Set up initial plot given array."""

    ax.imshow(array, cmap = cmap)
    plt.title('Not Running')

    #fig.tight_layout()
    fig.canvas.mpl_connect('button_press_event', onclick) # Click listener

    sidelength = len(array)
    plt.ylim(-0.5, sidelength-0.5)
    plt.xlim(-0.5, sidelength-0.5)

    minor_ticks = np.arange(-0.5, sidelength-0.5, 1)
    ax.set_xticks(minor_ticks, minor = True)
    ax.set_yticks(minor_ticks, minor = True)
    ax.grid(which = 'minor')
    plt.tick_params(
        axis = 'both',
        which = 'major',
        bottom = False,
        left = False)

    plt.show(block = False) # block = False so code can run in background


def runsim():
    """Runs the simulator, updating the array and plot using Game of Life
      rules."""
    global array
    global running
    if stepsPer != True: # While the stepsPer mode is off
        while running:   # Running will be true until another click
            array = next_life_generation(array)
            array = replaceBorder(array)
                         # Student nextgen function leaves border as zeros
            update(array)
            plt.pause(speed) # Hold plot as-is for "speed" (in seconds)
    else:                # While stepsPer mode is on
        for step in range(steps):
                         # Steps is number of steps--so update that many times
            array = next_life_generation(array)
            array = replaceBorder(array)
            update(array)
            plt.pause(speed)
        running = False # Once done, the program is no longer running
        plt.title('Not Running')
        update(array)   # Update to reflect new title/status

def start():
    """Main function used to boot up the simulator."""
    yn = input("Would you like a randomly generated board? (y/n) ")
    while yn != 'y' and yn != 'n': # Catch people tryna get creative
        yn = input("Please respond with 'y' or 'n': ")
    if yn == 'y':
        board = randomCells(dim, dim) # Use student function
        board = replaceBorder(board)  # Student function gives border of zeros;
                                      # ..we want a different value
    else:
        board = createBoard(dim, dim) # Student createboard function has
                                      # ..no border
        board = addBorder(board)

    global fig
    global ax
    fig, ax = plt.subplots()          # Initialize plot

    global array
    array = board                     # Board acts more nicely if np array
    graph(np.array(array))            # Plot our board


def addBorder(lol):
    """Adds a border of 'border' to a list of lists."""
    dim = len(lol)
    topb = [border]*(dim + 2)
    final = [topb]
    for x in lol:
        row = [border] + x + [border]
        final += [row]
    final += [topb]
    return final

def replaceBorder(lol):
    """Replaces outermost cells in a list of lists with a border of 'border'."""
    dim = len(lol)
    lol = lol[1:-1]
    lol = [x[1:-1] for x in lol]
    return(addBorder(lol))


def setColor():
    """Queries the user for a new color scheme."""

    global cmap
    z = input("Name a matplotlib color scheme or hit enter to personalize: ")

    if z != '': # If the input was a string
        # Color options can be found at:
        # https://matplotlib.org/gallery/color/colormap_reference.html
        cmap = plt.cm.get_cmap(z)
        return

    offsq = eval(input("Enter RGB tuple for off squares [e.g., (0, 255, 0)]: "))
    onsq = eval(input("Enter RGB tuple for lit squares: "))
    bor = eval(input("Enter RGB tuple for the border: "))

    # Change values to be out of 1 instead of 256 because that's
    # how the matplotlib function wants it.
    offsq = tuple(val/256 for val in offsq)
    onsq = tuple(val/256 for val in onsq)
    bor = tuple(val/256 for val in bor)

    colors = [offsq, onsq, bor]
    cmap = LinearSegmentedColormap.from_list('my_list', colors, N = 3)

def timePerStep(new):
    """Change how long (in seconds) the plot is paused before going to
       the next generation."""
    global speed
    speed = new

def sideLength(new):
    """Change the number of cells tall and wide the board is."""
    global dim
    dim = int(new)

def stepsPerClick():
    """Toggle the 'go x number of steps each click' mode."""
    global stepsPer, steps
    if stepsPer:
        stepsPer = False # If on, turn it off
    else:                # If off turn it on and ask for a number of steps
                         # ..per click
        stepsPer = True
        steps = input('How many iterations would you like to run per click? ')
        steps = int(steps)
