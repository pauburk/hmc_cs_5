# CS5 Gold/Black: Homework 7 Problem 2
# Filename: hw7pr2.py
# Name: Paul Burke
# Problem description: Looping for a while...

import random
import time

def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests
print("==============================\nTesting fac()\n==============================")
print( "fac(0)   should be   1 :",  fac(0) )
print( "fac(5)   should be 120 :",  fac(5) )

def summer(L):
    """
        Results: returns sum of L
        Arguments:
            L = a list of integers
    """
    result = 0
    for i in L: result += i
    return result

# tests
print("==============================\nTesting summer()\n==============================")
print("summer([10,10,10,2,10]): should be 42 ==", summer([10,10,10,2,10]))
print("summer([10,10,10,2]): should be 32 ==", summer([10,10,10,2]))
print("summer([11, 11]): should be 22 ==", summer([11,11]))
print("summer([47]): should be 47 ==", summer([47]))
print("summer([ ]): should be 0 ==", summer([ ]))


def summedOdds(L):
    """
        Results: returns sum of odd numbers in L
        Arguments:
            L = a list of integers
    """
    result = 0
    for i in L:
        if i % 2 == 0:
            result += i
    return result

# tests
print("==============================\nTesting summedOdds()\n==============================")
print( "summedOdds([4, 5, 6])      should be 5 :",  summedOdds([4, 5, 6]) )
print( "summedOdds(range(3, 10))   should be 24 :",  summedOdds(range(3, 10)) )


def summedExcept(exc, L):
    """
        Results: returns sum of numbers in L except for exc
        Arguments:
            L = a list of integers
            exc = an integer
    """
    result = 0
    for i in L:
        if i != exc:
            result += i
    return result

# tests
print("==============================\nTesting summedExcept()\n==============================")
print( "summedExcept(5, [4, 5, 6])      should be 10 :",  summedExcept(5, [4, 5, 6]) )
print( "summedExcept(5, [5, 5, 5])      should be 0 :",  summedExcept(5, [5, 5, 5]) )


def untilARepeat(high):
    """
        Results: returns the number of guesses needed to get a repeat from 0-high
        Arguments:
            high = an integer
    """
    L = []
    while True:
        guess = random.choice(range(0, high))
        if guess in L: break
        L.append(guess)
    return len(L)

# tests
print("==============================\nTesting untilARepeat()\n==============================")
L = [untilARepeat(365) for i in range(10000)]
print(L)
print("Average :", sum(L)/len(L))
print("Max :", max(L))
print("Min :", min(L))
print("Does 42 exist? :", 42 in L)
print("Exactly 2 :", L.count(2))
print("Does 1 exist? :", 1 in L)
print("Does 142 exist? :", 142 in L)


def rs():
    """ one random step """
    return random.choice( [-1, 1] )


def rwalk(radius):
    """ random walk between -radius and +radius  (starting at 0 by deafult)  """
    totalsteps = 0              # starting value of totalsteps (_not_ final value!)
    start = 0                   # start location (_not_ the total # of steps)

    while True:                 # run "forever"  (really, until a return or break)
        if start == -radius or start == radius:
            return totalsteps   # phew!  return totalsteps  (stops the while loop)

        start = start + rs()
        totalsteps += 1         # addn totalsteps 1    (for all who miss Hmmm :-)

        # print("start:", start)  # to see what's happening / debugging

    # it can never get here!


print("==============================\nAnalyzing rwalk()\n==============================")

for i in [1000, 100000, 1000000]:
    t = time.time()
    L = [ rwalk(5) for x in range(i) ]
    print(f"Time taken for {i} iterations of rwalk(5) : {round(time.time() - t, 2)} seconds")
    print(f"Average : {sum(L)/len(L)}")

print()

for r in [5, 6, 7, 10]:
    L = [ rwalk(r) for x in range(10000) ]
    print(f"Average of rwalk({r}) over 10,000 iterations: {sum(L)/len(L)}")

print("\nBased on the above values, I would expect radius^2 steps before the random walker reaches the edge of the interval (-r, r).")
print("Based on the previous conclusion, I would expect that after N steps the random walker would be sqrt(N) units from the starting point.")
