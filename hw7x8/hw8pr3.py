# CS5 Gold/Black: Homework 8 Problem 3
# Filename: hw8pr3.py
# Name: Paul Burke
# Problem description: Pi from Pie

import random
import math


def dart():
    """ throws one dart between (-1,-1) and (1,1)
          returns True if it lands in the unit circle; otherwise, False
    """
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
        return True  # HIT (within the unit circle)
    else:
        return False # missed (landed in one of the corners)


def forPi(N):
    """
        throws N darts, estimating pi
    """
    num_hits = 0
    for i in range(N):
        if dart(): num_hits += 1
        print(f"{num_hits} hits out of {i+1} throws so that pi is {4*num_hits/(i+1)}")
    return 4*num_hits/(i+1)


def whilePi(error):
    """
        returns number of darts thrown to reach an acceptable estimate of pi
        abs(est_pi - math.pi) < error
    """
    c = 1 # counter
    num_hits = 0
    est_pi = 0
    while(abs(4*num_hits/c - math.pi) >= error):
        if dart(): num_hits += 1
        print(f"{num_hits} hits out of {c} throws so that pi is {est_pi}")
        c += 1

    return c


def forPi_np(N):
    n = [i for i in range(N) if dart()]
    return 4*len(n)/N

def whilePi_np(err):
    c = 1 # counter
    num_hits = 0
    est_pi = 0
    while(abs(4*num_hits/c - math.pi) >= err):
        if dart(): num_hits += 1
        c += 1
    return c

for N in [1, 10, 100, 1000]:
    print(f"Difference between estimation and real value for N = {N} : {abs(math.pi - forPi_np(N))}")
print()
for e in [1, 0.1, 0.01, 0.001]:
    print(f"Average throws to get below e = {e} : {whilePi_np(e)}")

print("\nforPi() is more efficient, it only runs a set number of times (whilePi() could technically run forever).")
print("But whilePi() is more accurate, it requires that the estimation be under a certain error.")
