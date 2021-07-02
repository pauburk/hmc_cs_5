# CS5 Gold/Black: Final Project
# Filename: starter.py
# Name: Paul Burke
# Problem description: Picobot using genetic algoritms

import random
import numpy as np


WIDTH = 25
HEIGHT = 25
NUM_STATES = 5

ST_CHOICES = list(range(NUM_STATES)) # [0,1,2,...,NUM_STATES]
MV_CHOICES = ["N", "E", "W", "S", "X"]
SURR_CHOICES = ["xxxx", "Nxxx", "NExx", "NxWx", "xxxS", "xExS", "xxWS", "xExx", "xxWx"] # create all possible surroundings without wildcards for empty room
# SURR_CHOICES = []
# for i in ["*", "x", "N"]: # create all possible surroundings
#     for j in ["*", "x", "E"]:
#         for k in ["*", "x", "W"]:
#             for l in ["*", "x", "S"]:
#                 SURR_CHOICES.append(f"{i}{j}{k}{l}")

# creates empty room map (0s in the middle, 1s around the edges)
MAP1 = np.array([1 if i == 0 or i == WIDTH-1 or j == 0 or j == HEIGHT-1 else 0 for i in range(WIDTH) for j in range(HEIGHT)]).reshape(HEIGHT, WIDTH)

class Program:

    def __init__(self, rules=None):

        self.rules = rules if rules != None else {}

    def __repr__(self):

        string = ""
        for k in sorted(list(self.rules.keys())):
            string += f"{k[0]} {k[1]} -> {self.rules[k][0]} {self.rules[k][1]}\n"
        string = string.strip()
        return string

    def randomize(self):

        for st in ST_CHOICES:
            for surr in SURR_CHOICES:
                self.rules[(st, surr)] = (random.choice(MV_CHOICES), random.choice(ST_CHOICES))

    def getMove(self, state, surroundings):

        return self.rules[(state, surroundings)]

    def mutate(self):

        rand = random.choice(list(self.rules.keys()))
        valid_mvs = [mv for mv in MV_CHOICES if mv not in rand[1]]
        self.rules[rand] = (random.choice(valid_mvs), random.choice(ST_CHOICES))

    def crossover(self, other):

        states = random.randint(1, 3) # change to reflect numstates
        chosen_self_rules = {k:v for k, v in self.rules.items() if k[0] in range(states)}
        chosen_other_rules = {k:v for k, v in other.rules.items() if k[0] in range(states, NUM_STATES)}
        new_rules = {**chosen_self_rules, **chosen_other_rules}
        new_program = Program(new_rules)
        return new_program


# class World:
#
#     def __init__(self, width, height, map=1, program, botX, botY):
#
#         self.width = width
#         self.height = height
#         self.map = map if map in [1,2] else 1 # set map to be 1 or 2 if the input was correct, else default to 1
#         self.program = program
#         self.botX = botX
#         self.botY = botY
#
#     def __repr__(self):
#
#         w = self.width
#         h = self.height
#         map = MAP1 if self.map == 1 else MAP2
#
#
#         string = f"{st} {surr} -> {nxt_mv} {nxt_st}"
#         return string


p1 = Program()
p1.randomize()
print(p1)
print()

p2 = Program()
p2.randomize()
print(p2)
print()

p3 = p1.crossover(p2)
print(p3)
print()
