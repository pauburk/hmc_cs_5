# CS5 Gold/Black: Final Project
# Filename: milestone.py
# Name: Paul Burke
# Problem description: Picobot using genetic algoritms

import random
import numpy as np
import time
import os           # for file output
import regex as re  # for file output
import argparse     # for file output

"""!!ONLY WORKS WITH ODD DIMENSIONS!!"""
MAP = 2
WIDTH = 25          # width of map
HEIGHT = 25         # height of map
NUM_STATES = 5      # number of states

POP_SIZE = 200      # population size (# of programs)
NUM_GENS = 25       # number of generations (how many times we crossover/mutate the popluation)
NUM_TRIALS = 5      # number of trials (per evaluation, generate in random starting positions)
NUM_STEPS = 2000    # number of steps (per trial)

MT_PROB = 0.1       # probability of mutation
CO_PCNT = 0.1       # % of top programs to extract for crossover

ELITES_PER_GEN = int(POP_SIZE*CO_PCNT)      # number of top programs (elites) extracted per generation
CO_PER_GEN = POP_SIZE-ELITES_PER_GEN        # number of programs needed to make during crossover

ST_CHOICES = list(range(NUM_STATES)) # [0,1,2,...,NUM_STATES]
MV_CHOICES = ["N", "E", "W", "S", "X"]
surr_choices_empty = ["xxxx", "Nxxx", "NExx", "NxWx", "xxxS", "xExS", "xxWS", "xExx", "xxWx"] # create all possible surroundings without wildcards for empty room
surr_choices_diamond = ["xxxx", "NExx", "NxWx", "NxxS", "xEWx", "xExS", "xxWS", "NEWx", "NExS", "NxWS", "xEWS"] # create all possible surroundings without wildcards for diamond room
SURR_CHOICES = surr_choices_empty if MAP == 1 else surr_choices_diamond
# SURR_CHOICES = []
# for i in ["*", "x", "N"]: # create all possible surroundings
#     for j in ["*", "x", "E"]:
#         for k in ["*", "x", "W"]:
#             for l in ["*", "x", "S"]:
#                 SURR_CHOICES.append(f"{i}{j}{k}{l}")

# creates empty room map (0s in the middle, 1s, 2s, 3s around the edges)
MAP1 = np.array([1  if i in [0, HEIGHT-1] and j in [0, WIDTH-1] # corners
                    else 1 if i in [0, HEIGHT-1]                # top and bottom
                    else 1 if j in [0, WIDTH-1]                 # sides
                    else 0                                      # empty space
                    for i in range(HEIGHT) for j in range(WIDTH)]).reshape(HEIGHT, WIDTH)

# creates diamond room map
MAP2 = np.empty((HEIGHT, WIDTH))
MAP2[0] = [1 for _ in range(WIDTH)]
MAP2[HEIGHT-1] = [1 for _ in range(WIDTH)]
h2 = HEIGHT // 2 - 1 # half of the height - 1 (used for determining how many blue squares per row)
for r in range(1, HEIGHT-1):                            # for each row
    n = h2 - abs(h2 - r + 1)                            # get number of blue squares needed
    s = "1"*(25//2-n) + "0"*(n*2+1) + "1"*(25//2-n)     # create row of 0s and 1s
    l = [int(n) for n in s]                             # convert to list of ints
    MAP2[r] = l                                         # change that row in the np.array

# use only one map
MAP_CHOSEN = MAP1 if MAP == 1 else MAP2

# dict of chars to print for each value in the np.array map
DISP = {-2 : "\x1b[0;30;47m  \x1b[0m",  # color white (traveled)
        -1 : "\x1b[0;30;42m  \x1b[0m",  # color green (picobot)
        0 : "  ",                       # blank (not traveled)
        1 : "\x1b[0;30;44m  \x1b[0m"}   # color blue (walls)

class Program:
    """
        class for a Picobot program
        Methods:
            randomize()     randomize rules
            get_move()      returns the next move and state based on current state and surroundings
            mutate()        mutates one of the rules 5% of the time
            crossover()     crosses over self with other and returns a new Program
    """

    def __init__(self, rules=None):

        self.rules = rules if rules != None else {}

    def __repr__(self):

        string = ""
        for k in sorted(list(self.rules.keys())): # for rule
            string += f"{k[0]} {k[1]} -> {self.rules[k][0]} {self.rules[k][1]}\n" # add rule to string to return
        return string.strip() # get rid of the \n on the end

    def randomize(self):

        for st in ST_CHOICES:           # go through each state
            for surr in SURR_CHOICES:   # go through each surrounding
                while True:             # randomly generate next move and state, make sure there are no contradictions
                    self.rules[(st, surr)] = (random.choice(MV_CHOICES), random.choice(ST_CHOICES))
                    if self.rules[(st, surr)][0] not in surr: break

    def get_move(self, state, surroundings):

        return self.rules[(state, surroundings)]

    def mutate(self, p=MT_PROB):

        if np.random.uniform() < p: # mutate 5% of the time
            rand = random.choice(list(self.rules.keys()))                               # pick random rule
            valid_mvs = [mv for mv in MV_CHOICES if mv not in rand[1]]                  # get valid moves
            self.rules[rand] = (random.choice(valid_mvs), random.choice(ST_CHOICES))    # change that rule to random next move and choice

    def crossover(self, other):

        states = random.randint(NUM_STATES // 3, NUM_STATES - NUM_STATES // 3)              # ensure that crossover uses some of both self and other
        chosen_self_rules = {k:v for k, v in self.rules.items() if k[0] in range(states)}   # get rules from self
        chosen_other_rules = {k:v for k, v in other.rules.items() if k[0] in range(states, NUM_STATES)} # get rules from other
        new_rules = {**chosen_self_rules, **chosen_other_rules}                             # make new dict with chosen rules from self and other
        new_program = Program(new_rules) # create program with new rules
        return new_program


class World:
    """
        class for Picobot room
        Methods:
            get_surroundings()      returns current surroundings based on map and botX and botY
            step()                  moves Picobot one step forward, updates position, traveled cells, etc
            frac_visited_cells()    returns # cells visited / total # cells, used for fitness score
            get_current_rule()      gets the current state, surr, next move, and rule (printed in simulator)
            run()                   runs step() a set number of times
    """

    def __init__(self, map, program, botX=None, botY=None):

        self.map = np.copy(map)
        self.prog = program
        self.botX = random.randrange(1, WIDTH-1) if botX == None else botX # if botX not specified generate random location
        self.botY = random.randrange(1, HEIGHT-1) if botY == None else botY # same for botY
        while(map[self.botY][self.botX] == 1): # make sure botX and botY are valid (in diamond map bot could generate inside the map)
            self.botX = random.randrange(1, WIDTH-1)
            self.botY = random.randrange(1, WIDTH-1)
        self.map[self.botY][self.botX] = -1 # set picobot location
        self.state = 0 # starts at state 0

    def __repr__(self):

        string = ""
        for r in range(self.map.shape[0]): # go through each row
            for c in self.map[r]: # go through each value in each row
                string += DISP[c] # get the display character for that value (fancy colors!)
            string += "\n"
        return string.strip() # get rid of the \n on the end

    def get_surroundings(self):

        Y = self.botY
        X = self.botX
        surr = ""
        surr += "N" if self.map[Y-1][X] in [1,2] else "x" # if N blocked add N to string else add x
        surr += "E" if self.map[Y][X+1] in [1,2] else "x" # same
        surr += "W" if self.map[Y][X-1] in [1,2] else "x" # same
        surr += "S" if self.map[Y+1][X] in [1,2] else "x" # same
        return surr

    def step(self):

        surr = self.get_surroundings()
        move = self.prog.get_move(self.state, surr)
        self.map[self.botY][self.botX] = -2 # current location has been visited

        if move[0] == "N": self.botY -= 1   # move bot N
        if move[0] == "E": self.botX += 1   # move bot E
        if move[0] == "W": self.botX -= 1   # move bot W
        if move[0] == "S": self.botY += 1   # move bot S

        # check if out of bounds
        # returns the value because originally I had contradictions in my rules, not necessary anymore
        # in fact, this whole if/elif thing could be deleted but it doesn't matter
        if self.botX < 1:
            self.botX = 1
            return "W"
        elif self.botX > WIDTH-2:
            self.botX = WIDTH-2
            return "E"
        if self.botY < 1:
            self.botY = 1
            return "N"
        elif self.botY > HEIGHT-2:
            self.botY = HEIGHT-2
            return "S"

        self.map[self.botY][self.botX] = -1 # set new location
        self.state = move[1]

    def frac_visited_cells(self):

        num_visited_cells = (np.count_nonzero(self.map == -2)) + 1  # counts -2s in array (-2 means visited), + 1 for picobot square which is -1
        num_unvisited_cells = (np.count_nonzero(self.map == 0))     # counts 0s in array (0 means not visited)
        total_visitable_cells = num_visited_cells + num_unvisited_cells
        return num_visited_cells / total_visitable_cells

    def get_current_rule(self):

        surr = self.get_surroundings()
        move = self.prog.rules[(self.state, surr)]
        return self.state, surr, move[0], move[1] # return the rule to print in the simulation

    def run(self, steps):

        # fracs = [] # stop execution if picobot is "stuck"
        for _ in range(steps):
            self.step()
            # fracs.append(self.frac_visited_cells())
            # if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH]: break


def gen_pop(num):
    """
        generates population of random programs
    """

    progs = []              # list of programs
    for _ in range(num):
        P = Program()       # initialize new program
        P.randomize()       # randomize it
        progs.append(P)     # add it to the list
    return progs


def evaluate(program, trials=NUM_TRIALS, steps=NUM_STEPS):
    """
        evaluates program (returns a fitness score of % cells covered)
        evaluates NUM_TRIALS trials and NUM_STEPS steps, using the chosen map
    """

    fitness = 0                             # fitness score
    for _ in range(trials):                 # do NUM_TRIALS number of trials
        W = World(MAP_CHOSEN, program)      # make world with chosen map and the program being evaled
        W.run(steps)                        # run NUM_STEPS in that world
        fitness += W.frac_visited_cells()   # get the number of visited cells, add it to fitness
    return fitness/trials                   # divide by number of trials to get average fitness


def my_sort(l):
    """
        sorts list of tuples by first value, largest is at the front
    """
    l.sort(key=lambda x:x[0])
    l.reverse()
    return l


def main():
    """
        do the thing
    """

    # resize terminal window to fake animation
    os.system(f"printf '\e[8;{HEIGHT+4};{max(80, WIDTH*2+4)}t'")

    # use argparse to enter the output directory for the files to be written to
    help_str = """
        Creates Picobot program using genetic algorithms, outputs program and
        details from training into .txt files. Can simulate the best performing
        program.
    """
    ap = argparse.ArgumentParser(description=help_str)
    ap.add_argument("-o", "--outputdir",
                    help="""Path to the directory to output the run details
                            and final program in a .txt file.""",
                    type=str)

    args = ap.parse_args()
    outDir = args.outputdir

    # get next filename
    # so I can have new files output each time I run this code
    files = [fname for fname in os.listdir(outDir) if fname.startswith("GAPicobot")] # get all relevant files in outDir

    # get the number in those file names
    filenums = [0]
    for fname in files:
        digits = re.findall("\d+", fname)
        if len(digits) > 0:
            filenums.append(int(digits[0]))

    # set the new run number
    on_run = max(filenums)+1

    # set the two output file names, one for run details and one for the final program
    outFilename_training = os.path.join(outDir, f"GAPicobotTraining_{on_run}.txt")
    outFilename_program = os.path.join(outDir, f"GAPicobotProgram_{on_run}.txt")

    # print hyperparameters
    print(f"\nMap : MAP1 (empty)") if MAP == 1 else print(f"\nMap : MAP2 (diamond)")
    print(f"Width : {WIDTH}")
    print(f"Height : {HEIGHT}")
    print(f"Number of states : {NUM_STATES}")

    print(f"Population size : {POP_SIZE}")
    print(f"Number of generations : {NUM_GENS}")
    print(f"Number of trials : {NUM_TRIALS}")
    print(f"Number of steps per trial: {NUM_STEPS}")

    print(f"Probability of mutation : {MT_PROB}")
    print(f"% of programs extracted for crossover : {CO_PCNT}")

    print(f"# of programs extracted for crossover : {ELITES_PER_GEN}")
    print(f"# of programs created during crossover : {CO_PER_GEN}")

    # output hyperparameters to file
    with open(outFilename_training, "w") as fh:
        fh.write(f"GAPicobotTraining_{on_run}.txt\n\nHYPERPARAMETERS:")

        fh.write(f"\n\tMap : MAP1 (empty)") if MAP == 1 else fh.write(f"\n\tMap : MAP2 (diamond)")
        fh.write(f"\n\tWidth : {WIDTH}")
        fh.write(f"\n\tHeight : {HEIGHT}")
        fh.write(f"\n\tNumber of states : {NUM_STATES}")

        fh.write(f"\n\tPopulation size : {POP_SIZE}")
        fh.write(f"\n\tNumber of generations : {NUM_GENS}")
        fh.write(f"\n\tNumber of trials : {NUM_TRIALS}")
        fh.write(f"\n\tNumber of steps per trial: {NUM_STEPS}")

        fh.write(f"\n\tProbability of mutation : {MT_PROB}")
        fh.write(f"\n\t% of programs extracted for crossover : {CO_PCNT}")

        fh.write(f"\n\t# of programs extracted for crossover : {ELITES_PER_GEN}")
        fh.write(f"\n\t# of programs created during crossover : {CO_PER_GEN}")

    time.sleep(3)
    print("\nRunning genetic algoritms...")
    with open(outFilename_training, "a") as fh: fh.write("\n\n\nRunning genetic algoritms...")

    # time how long the genetic algorithms take to run
    start = time.time()

    PROGRAM_POP = gen_pop(POP_SIZE) # randomly generate POP_SIZE programs

    for gen in range(NUM_GENS): # iterate through each generation

        evals = [(evaluate(p), p) for p in PROGRAM_POP]     # evaluate each program
        evals = my_sort(evals)                              # sort the evaluations with a custom function to sort the list of tuples
        fitnesses = [e[0] for e in evals]                   # extract only the fitness scores
        avg_score = sum(fitnesses)/len(fitnesses)           # get average fitness score
        max_score = max(fitnesses)                          # get max fitness score

        string = f"\nGeneration {gen+1}/{NUM_GENS}:\n\tavg score = {avg_score:.4f}\n\tmax score = {max_score:.4f}" # output string for each generation
        with open(outFilename_training, "a") as fh: fh.write("\n" + string)
        print(string)

        elite_set = [evals[i][1] for i in range(ELITES_PER_GEN)] # get top CO_PCNT of programs
        elite_scores = [evals[i][0] for i in range(ELITES_PER_GEN)] # get top CO_PCNT of scores

        # optimize for better performing programs during crossover using p=select_probs in np.random.choice
        # the better programs will have a higher percentage of getting chosen for crossover
        select_probs = np.array(elite_scores) / np.sum(elite_scores)

        # generate child set using crossover
        child_set = []
        for _ in range(CO_PER_GEN):
            p1 = elite_set[np.random.choice(range(len(elite_set)), p=select_probs)]
            p2 = elite_set[np.random.choice(range(len(elite_set)), p=select_probs)]
            child_set.append(p1.crossover(p2))

        # mutate the child set
        for p in child_set:
            p.mutate()

        # reset the program population
        PROGRAM_POP = elite_set
        PROGRAM_POP += child_set


    # get the final evaluations and determine best score and corresponding program
    evals = [(evaluate(p), p) for p in PROGRAM_POP]
    evals = my_sort(evals)
    final_score = evals[0][0]
    final_program = evals[0][1]

    end = time.time()


    # output best score and time taken
    best_score_string = f"\n==============================\nBest fitness score = {final_score:.4f}"
    time_taken_string = f"Time taken = {end-start:.0f} seconds\n==============================\n"
    print(best_score_string)
    print(time_taken_string)
    with open(outFilename_training, "a") as fh:
        fh.write("\n" + best_score_string)
        fh.write("\n" + time_taken_string)

    # output final program to .txt file
    with open(outFilename_program, "w") as fh: fh.write(final_program.__repr__())

    time.sleep(3)

    # show simulation of the final program using the picobot simulator I built (if the user wants)
    show_sim = input("Do you want to see a simulation of the final program? (y/n) ")
    while show_sim.lower() not in ["y", "n"]: show_sim = input("Please enter a valid input. ") # get valid input

    if show_sim.lower() == "y":

        time.sleep(3)

        W = World(MAP_CHOSEN, final_program, WIDTH//2, HEIGHT//2) # set up world, start Picobot in the middle
        # fracs = [] # cutoff if program is repeating
        for i in range(NUM_STEPS):                                              # for each step
            print(f"\n{W}")                                                     # print world
            cur_st, surr, nxt_mv, nxt_st = W.get_current_rule()                 # get the current rules
            # fracs.append(W.frac_visited_cells())
            # print(f"Step : {i+1} (automatically stopped)") if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH] else print(f"Step : {i+1}")
            print(f"Step : {i+1}/{NUM_STEPS}")                                              # print step #
            print(f"Current rule : {cur_st} {surr} -> {nxt_mv} {nxt_st}")       # print current rule
            print(f"Percent of room covered : {W.frac_visited_cells():.4f}")    # print % of room covered
            # if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH]: break
            time.sleep(0.05)
            W.step()

    time.sleep(3)

    # resize terminal window to show full program
    os.system(f"printf '\e[8;{max(49, HEIGHT+4)};{max(80, WIDTH*2+4)}t'")

    # output final program
    print(f"\nFinal program (also exported to '{outFilename_program}'):\n")
    print(final_program)


main()
