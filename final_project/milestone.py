# CS5 Gold/Black: Final Project
# Filename: milestone.py
# Name: Paul Burke
# Problem description: Picobot using genetic algoritms

import random
import numpy as np
import time
import os
import regex as re

WIDTH = 25
HEIGHT = 25
NUM_STATES = 5

POP_SIZE = 200
NUM_GENS = 15
NUM_TRIALS = 5
NUM_STEPS = 2000

MT_PROB = 0.1
CO_PCNT = 0.1

ELITES_PER_GEN = int(POP_SIZE*CO_PCNT)
CO_PER_GEN = POP_SIZE-ELITES_PER_GEN

ST_CHOICES = list(range(NUM_STATES)) # [0,1,2,...,NUM_STATES]
MV_CHOICES = ["N", "E", "W", "S", "X"]
SURR_CHOICES = ["xxxx", "Nxxx", "NExx", "NxWx", "xxxS", "xExS", "xxWS", "xExx", "xxWx"] # create all possible surroundings without wildcards for empty room
# SURR_CHOICES = []
# for i in ["*", "x", "N"]: # create all possible surroundings
#     for j in ["*", "x", "E"]:
#         for k in ["*", "x", "W"]:
#             for l in ["*", "x", "S"]:
#                 SURR_CHOICES.append(f"{i}{j}{k}{l}")

# creates empty room map (0s in the middle, 1s, 2s, 3s around the edges)
MAP1 = np.array([1  if i in [0, HEIGHT-1] and j in [0, WIDTH-1] # corners
                    else 1 if i in [0, HEIGHT-1] # top and bottom
                    else 1 if j in [0, WIDTH-1] # sides
                    else 0 for i in range(HEIGHT) for j in range(WIDTH)]).reshape(HEIGHT, WIDTH) # empty space

# dict of chars to print
# DISP = {-2 : "\x1b[0;30;47m \x1b[0m", -1 : "\x1b[0;30;42m \x1b[0m", 0 : " ", 1 : "\x1b[0;30;44m \x1b[0m", 2 : "-", 3 : "+"}
DISP = {-2 : "\x1b[0;30;47m  \x1b[0m",
        -1 : "\x1b[0;30;42m  \x1b[0m",
        0 : "  ",
        1 : "\x1b[0;30;44m  \x1b[0m"}

class Program:

    def __init__(self, rules=None):

        self.rules = rules if rules != None else {}

    def __repr__(self):

        string = ""
        for k in sorted(list(self.rules.keys())):
            string += f"{k[0]} {k[1]} -> {self.rules[k][0]} {self.rules[k][1]}\n"
        return string.strip()

    def randomize(self):

        for st in ST_CHOICES:
            for surr in SURR_CHOICES:
                while True:
                    self.rules[(st, surr)] = (random.choice(MV_CHOICES), random.choice(ST_CHOICES))
                    if self.rules[(st, surr)][0] not in surr: break

    def get_move(self, state, surroundings):

        return self.rules[(state, surroundings)]

    def mutate(self, p=MT_PROB):

        if np.random.uniform() < p:
            rand = random.choice(list(self.rules.keys()))
            valid_mvs = [mv for mv in MV_CHOICES if mv not in rand[1]]
            self.rules[rand] = (random.choice(valid_mvs), random.choice(ST_CHOICES))

    def crossover(self, other):

        states = random.randint(NUM_STATES // 3, NUM_STATES - NUM_STATES // 3)
        chosen_self_rules = {k:v for k, v in self.rules.items() if k[0] in range(states)}
        chosen_other_rules = {k:v for k, v in other.rules.items() if k[0] in range(states, NUM_STATES)}
        new_rules = {**chosen_self_rules, **chosen_other_rules}
        new_program = Program(new_rules)
        return new_program


class World:

    def __init__(self, map, program, botX=None, botY=None):

        self.map = np.copy(map)
        self.prog = program
        self.botX = random.randrange(1, WIDTH-1) if botX == None else botX
        self.botY = random.randrange(1, HEIGHT-1) if botY == None else botY
        self.map[self.botY][self.botX] = -1 # set picobot location
        # print(self.map)
        self.state = 0

    def __repr__(self):

        string = ""
        for r in range(self.map.shape[0]):
            for c in self.map[r]:
                string += DISP[c]
            string += "\n"
        return string.strip()

    def get_surroundings(self):

        Y = self.botY
        X = self.botX
        surr = ""
        surr += "N" if self.map[Y-1][X] in [1,2] else "x"
        surr += "E" if self.map[Y][X+1] in [1,2] else "x"
        surr += "W" if self.map[Y][X-1] in [1,2] else "x"
        surr += "S" if self.map[Y+1][X] in [1,2] else "x"
        return surr

    def step(self):

        surr = self.get_surroundings()
        move = self.prog.get_move(self.state, surr)
        self.map[self.botY][self.botX] = -2 # current location has been visited

        if move[0] == "N": self.botY -= 1
        if move[0] == "E": self.botX += 1
        if move[0] == "W": self.botX -= 1
        if move[0] == "S": self.botY += 1

        # check if out of bounds
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

        return (np.count_nonzero(self.map == -2) + 1) / ((HEIGHT-2)*(WIDTH-2))

    def get_current_rule(self):

        surr = self.get_surroundings()
        move = self.prog.rules[(self.state, surr)]
        return self.state, surr, move[0], move[1]

    def run(self, steps):

        # fracs = [] # stop execution if picobot is "stuck"
        for _ in range(steps):
            self.step()
            # fracs.append(self.frac_visited_cells())
            # if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH]: break


def gen_pop(num):

    progs = []
    for _ in range(num):
        P = Program()
        P.randomize()
        progs.append(P)
    return progs


def evaluate(program, trials=NUM_TRIALS, steps=NUM_STEPS):

    fitness = 0
    for _ in range(trials):
        W = World(MAP1, program)
        W.run(steps)
        fitness += W.frac_visited_cells()
    return fitness/trials


def working(self):
        """
        This method will set the current program (self) to a working
        room-clearing program. This is super-useful to make sure that
        methods such as step, run, and evaluateFitness are working!
        """
        POSSIBLE_SURROUNDINGS = ["NExx", "NxWx", "Nxxx", "xExS",
          "xExx", "xxWS", "xxWx", "xxxS", "xxxx"]
        POSSIBLE_MOVES = ['N', 'E', 'W', 'S']
        POSSIBLE_STATES = [0, 1, 2, 3, 4]
        for st in POSSIBLE_STATES:
            for surr in POSSIBLE_SURROUNDINGS:
                if st == 0 and ('N' not in surr):   val = ('N', 0)
                elif st == 0 and ('W' in surr):     val = ('E', 2)
                elif st == 0:                       val = ('W', 1)
                elif st == 1 and ('S' not in surr): val = ('S', 1)
                elif st == 1 and ('W' in surr):     val = ('E', 2)
                elif st == 1:                       val = ('W', 0)
                elif st == 2 and ('E' not in surr): val = ('E', 2)
                elif st == 2 and ('N' in surr):     val = ('S', 1)
                elif st == 2:                       val = ('N', 0)
                else:
                    stepdir = surr[0]
                    while stepdir in surr:
                        stepdir = random.choice(POSSIBLE_MOVES)
                    val = (stepdir, st)  # keep the same state
                self.rules[(st, surr)] = val


def my_sort(l): # sorts list of tuples by first value, largest is at the front
    l.sort(key=lambda x:x[0])
    l.reverse()
    return l


def main():

    # resize terminal window to fake animation
    os.system(f"printf '\e[8;{HEIGHT+4};{max(80, WIDTH*2+4)}t'")

    print(f"\nWidth : {WIDTH}")
    print(f"Height : {HEIGHT}")
    print(f"Number of states : {NUM_STATES}")

    print(f"Population size : {POP_SIZE}")
    print(f"Number of generations : {NUM_GENS}")
    print(f"Number of trials : {NUM_TRIALS}")
    print(f"Number of steps per trial: {NUM_STEPS}")

    with open(f"GAPicobotTraining_{1}.txt", "w") as fh:
        fh.write(f"GAPicobotTraining_{1}.txt\n\nHYPERPARAMETERS:")

        fh.write(f"\n\tWidth : {WIDTH}")
        fh.write(f"\n\tHeight : {HEIGHT}")
        fh.write(f"\n\tNumber of states : {NUM_STATES}")

        fh.write(f"\n\tPopulation size : {POP_SIZE}")
        fh.write(f"\n\tNumber of generations : {NUM_GENS}")
        fh.write(f"\n\tNumber of trials : {NUM_TRIALS}")
        fh.write(f"\n\tNumber of steps per trial: {NUM_STEPS}")

    time.sleep(3)
    print("\nRunning genetic algoritms...")
    with open(f"GAPicobotTraining_{1}.txt", "a") as fh: fh.write("\n\n\nRunning genetic algoritms...")

    start = time.time()

    PROGRAM_POP = gen_pop(POP_SIZE)
    # working(PROGRAM_POP[0])

    for gen in range(NUM_GENS):

        evals = [(evaluate(p), p) for p in PROGRAM_POP]
        evals = my_sort(evals)
        fitnesses = [e[0] for e in evals]
        avg_score = sum(fitnesses)/len(fitnesses)
        max_score = max(fitnesses)

        string = f"\nGeneration {gen+1}/{NUM_GENS}:\n\tavg score = {avg_score:.4f}\n\tmax score = {max_score:.4f}"
        with open(f"GAPicobotTraining_{1}.txt", "a") as fh: fh.write("\n" + string)
        print(string)

        elite_set = [evals[i][1] for i in range(ELITES_PER_GEN)] # get top CO_PCNT of programs
        elite_scores = [evals[i][0] for i in range(ELITES_PER_GEN)]

        select_probs = np.array(elite_scores) / np.sum(elite_scores) # optimize for better performing programs during crossover

        child_set = []
        for _ in range(CO_PER_GEN):
            p1 = elite_set[np.random.choice(range(len(elite_set)), p=select_probs)]
            p2 = elite_set[np.random.choice(range(len(elite_set)), p=select_probs)]
            child_set.append(p1.crossover(p2))

        for p in child_set:
            p.mutate()

        PROGRAM_POP = elite_set
        PROGRAM_POP += child_set

    evals = [(evaluate(p), p) for p in PROGRAM_POP]
    evals = my_sort(evals)
    final_score = evals[0][0]
    final_program = evals[0][1]

    end = time.time()


    best_score_string = f"\n==============================\nBest fitness score = {final_score:.4f}"
    time_taken_string = f"Time taken = {end-start:.0f} seconds\n==============================\n"
    print(best_score_string)
    print(time_taken_string)
    with open(f"GAPicobotTraining_{1}.txt", "a") as fh:
        fh.write("\n" + best_score_string)
        fh.write("\n" + time_taken_string)

    time.sleep(3)

    show_sim = input("Do you want to see a simulation of the final program? (y/n) ")
    while show_sim.lower() not in ["y", "n"]: show_sim = input("Please enter a valid input. ")

    if show_sim.lower() == "y":

        time.sleep(3)

        W = World(MAP1, final_program, WIDTH//2, HEIGHT//2)
        fracs = []
        for i in range(NUM_STEPS):
            print(f"\n{W}")
            cur_st, surr, nxt_mv, nxt_st = W.get_current_rule()
            # fracs.append(W.frac_visited_cells())
            # print(f"Step : {i+1} (automatically stopped)") if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH] else print(f"Step : {i+1}")
            print(f"Step : {i+1}")
            print(f"Current rule : {cur_st} {surr} -> {nxt_mv} {nxt_st}")
            print(f"Percent of room covered : {W.frac_visited_cells():.4f}")
            # if len(fracs) > max(WIDTH+5, HEIGHT+5) and fracs[-1] == fracs[-WIDTH]: break
            time.sleep(0.05)
            W.step()

    time.sleep(3)

    # resize terminal window to show full program
    os.system(f"printf '\e[8;{max(49, HEIGHT+4)};{max(80, WIDTH*2+4)}t'")

    # get next filename
    # files = [fname for fname in os.listdir() if fname.startswith("GApicobot_")]
    # filenums =

    print(f"\nFinal program (also exported to GAPicobotProgram_{1}.txt):\n")
    with open(f"GAPicobotProgram_{1}.txt", "w") as fh: fh.write(final_program.__repr__())
    print(final_program)


main()
