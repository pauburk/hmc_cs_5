try:
    import pyglet
except:
    print("\n++++++++++++++++++++++\n\nimport pyglet failed!\n")
    print("Try installing with\n\n!pip install --upgrade --user pyglet\n\n")
    print("(The ! is only if you're currently in ipython.)\nYou may need to restart ipython.")
    print("\n\n++++++++++++++++++++++\n")
    import sys
    sys.exit(0)


from pyglet.window import key
from pyglet.window import mouse
import random

#
# try out importing the functions from hw9pr1
#
try:
    from hw9pr1 import randomCells, createBoard, next_life_generation

#
# Gamelife functions of Life functions!   We provide a set here...
#
except:
    print("hw9pr1 game of life functions not found...")
    print("Using pyglet's game of life functions...")


    def createOneRow(width):
        """ returns one row of zeros of width "width"...  
            You might use this in your createBoard(width, height) function """
        row = []
        for col in range(width):
            row += [0]
        return row

    def createBoard(width, height):
        """Returns a 2D array with "height" rows and "width" columns."""
        A = []
        for row in range(height):
            A += [createOneRow(width)]        # use the above function so that SOMETHING is one row!!
        return A

    def printBoard(A):
        """This function prints the 2D list-of-lists A."""
        for row in A:               # row is the whole row
            for col in row:         # col is the individual element
                print(col, end='')  # print that element
            print()
        print()

    def randomCells(width, height):
        """Returns a DEEP copy of the 2D array A."""
        newA = createBoard(width, height)

        for row in range(1, height - 1):
            for col in range(1, width - 1):
                newA[row][col] = random.choice([0,1])

        return newA

    def copy(A):
        """Returns a DEEP copy of the 2D array A."""
        height = len(A)
        width = len(A[0])
        newA = createBoard(width, height)

        for row in range(1, height - 1):
            for col in range(1, width - 1):
                newA[row][col] = A[row][col] # what should be here, in order to
                # copy each element of A into the corresponding spot in newA?

        return newA


    def countNeighbors(row, col, A):
        """ yay! """
        n = 0
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                n += A[r][c]
        return n - A[row][col]


    def next_life_generation(A):
        """Makes a copy of A and then advances one
        generation of Conway's Game of Life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
        """
        height = len(A)
        width = len(A[0])
        newA = copy(A)

        for row in range(1, height - 1):
            for col in range(1, width - 1):
                n = countNeighbors(row,col,A)
                #
                # Rules:   B3/S23
                #
                old_state = A[row][col]
                if old_state == 0:
                    if n in [3]: 
                        newA[row][col] = 1
                    else: 
                        pass
                if old_state == 1:
                    if n not in [2,3]: 
                        newA[row][col] = 0
                    else:
                        pass

                """
                Above are "Life's rules"
                """
                
                
        return newA


#
# pyglet-graphics for life
#


border = 2 # the value used in the array for border cells
dim = 30 # default sidelength of grid
x_size = 640 # the width of the window created
y_size = 480 # the height of the window created
width = 10 # the size in pixels of each block
x_pos = x_size//2 - dim*(width//2) # this is the coordinate of left-hand side of the game inside the window
y_pos = y_size//2 - dim*(width//2) # this is the coordinate of the right hand side of the game inside the window
x_hpos = x_size//2 + dim*(width//2) # this is the coordinate of the top side of the game inside the window
y_hpos = y_size//2 + dim*(width//2) # this is the coordinate of the bottom side of the game inside the window
border_color = (140, 140, 140) # the default color of the border cells
live_color = (0,0,0) # the default color of the alive cells
dead_color = (200,150,20) # the default color of the dead cells
speed = 0.5 # the default speed from frame to frame
running = False # program not running until activated with click outside
board = [] # initialize the board here
steps = 3 # default steps per click
steps_left = 3 # to track the steps when stepsPer is True
stepsPer = False # going a number of clicks per step is off by default
LIFE_SQUARES = []


def addBorder(lol): 
    """adds a border of 'border' to a list of lists"""
    lol = lol[1:-1]
    lol =[x[1:-1] for x in lol]
    dim = len(lol)
    topb = [border]*(dim+2)
    final = [topb]
    for x in lol:
        row =[border] + x + [border]
        final += [row]
    final += [topb]
    return final

def sideLength(new_dim):
    """changes the number of cells tall/wide the board is"""
    global dim
    dim = int(new_dim) 

def timePerStep(new_speed): 
    """change how long in seconds the plot is paused before going to next generation"""
    global speed
    speed = abs(new_speed)

def setColor(onsq=None, offsq=None, bor=None):
    """
        changes the color of the cells, using rgb triples
        
        setColor( onsq = (0,0,0), offsq = (200,150,20), bor = (140, 140, 140) )
        
    """
    global border_color
    global live_color
    global dead_color
    if onsq == None:
        onsq = (0,0,0) # the default color of the alive cells
    if offsq == None:
        offsq = (200,150,20) # the default color of the dead cells
    if bor == None:
        bor = (140, 140, 140) # the default color of the border cells
    # offsq = eval(input("Enter rgb tuple for off squares    "))
    # while len(offsq) != 3 or type(offsq[0]) != int or type(offsq[1]) != int or type(offsq[2]) != int:
    #     offsq = eval(input("Enter rgb tuple for off squares    "))
    # onsq = eval(input("Enter rgb tuple for lit squares    "))
    # while len(onsq) != 3 or type(onsq[0]) != int or type(onsq[1]) != int or type(onsq[2]) != int:
    #     onsq = eval(input("Enter rgb tuple for off squares    "))
    # bor = eval(input("Enter rgb tuple for the border    "))
    # while len(bor) != 3 or type(bor[0]) != int or type(bor[1]) != int or type(bor[2]) != int:
    #     bor = eval(input("Enter rgb tuple for off squares    "))
    border_color = bor
    live_color = onsq
    dead_color = offsq

def start(initially_empty=False):
    """
    start holds all of the functions related to the window 
    when it is open. Running it opens the window and 
    jumpstarts all the rest of the functions.
    """
    global board
    global LIFE_SQUARES
    # y = input("Would you like a randomly generated board? (y/n)    ")
    # while y != 'y' and y != 'n': # catch people tryna get creative
    #     y = input("Please respond with 'y' or 'n'    ")
    if initially_empty == True:
        y = 'n'  # heads to the empty, else below
    else:
        y = 'y'  # heads to the non-empty, random (if), below:

    if y == 'y':
        board = randomCells(dim, dim) # use student function
        board = addBorder(board) # student function gives border of 0s, we want a different value
    else:
        board = createBoard(dim, dim) # student createboard function has no border
        board = addBorder(board)

    window = pyglet.window.Window(x_size,y_size) # create a window

    LIFE_SQUARES = [0]*(dim*dim) # create a list of rectangles for updating later
    for row in range(dim):
        for col in range(dim):
            x=row*width + x_pos
            y=col*width + y_pos
            if board[row][col] == 1:
                color=live_color
            elif board[row][col] == 0:
                color=dead_color
            elif board[row][col] == 2:
                color = border_color
            LIFE_SQUARES[row*dim + col] = pyglet.shapes.Rectangle(x=x,y=y,width=width,height=width,color=color) 

    label = pyglet.text.Label('Not running...',  #label for top
                            font_name='Times New Roman', 
                            font_size=18,
                            x=int(window.width*.5), y=int(window.height*.9),
                            anchor_x='center', anchor_y='center',
                            color=(255,255,255,255), align='center'
                            )
    global running
    running = False    # whether or not to start immediately

    def update_board(dt):
        """
        runs with every schedule update. It updates the
        board, if necessary, and then updates the list of rectangles
        """
        global board
        global running
        global LIFE_SQUARES

        if running:
            board = next_life_generation(board) #if its running, change the board
            board = addBorder(board)

            # update the rectangles...
            for row in range(dim):
                for col in range(dim):
                    x=row*width + x_pos
                    y=col*width + y_pos
                    if board[row][col] == 1:
                        color=live_color
                    elif board[row][col] == 0:
                        color=dead_color
                    elif board[row][col] == 2:
                        color = border_color
                    LIFE_SQUARES[row*dim + col].color = color # updates the list of rectangles


    @window.event
    def on_mouse_press(x, y, button, modifiers):
        """ handle mouse-press events! """
        global board
        global running
        global stepsPer
        global steps_left
        global steps
        global LIFE_SQUARES
        if x in range(x_pos, x_hpos) and y in range(y_pos, y_hpos): #change something on the board
            row = (x - x_pos)//width
            col = (y - y_pos)//width
            if board[row][col] != border:
                if board[row][col] == 1:
                    board[row][col] = 0
                else:
                    board[row][col] = 1
                # update rectangle!
                if board[row][col] == 1:
                    color=live_color
                elif board[row][col] == 0:
                    color=dead_color
                elif board[row][col] == 2:
                    color = border_color
                LIFE_SQUARES[row*dim + col].color = color # updates the list of rectangles
        else: #switch from running to not
            if stepsPer == True: #in stepsPer, reset steps_left
                running = True
                steps_left = steps
            else:
                if running==True:
                    running = False
                    label.text = "Not running..."
                else:
                    running = True
                    label.text = "Running..."

    @window.event
    def on_draw(): 
        """
        this function does the actual drawing
        """
        global LIFE_SQUARES
        window.clear() 
        label.draw()
        for rect in range(dim**2): #draw the board
            box = LIFE_SQUARES[rect]
            box.draw()

    pyglet.clock.schedule_interval(update_board, speed)
    pyglet.app.run()


#
# let's start!
#
print("\n\nRun start() to try it out!\n\n")



