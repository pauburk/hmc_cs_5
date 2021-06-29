#
# hw6pr5.py -  Python!
#
#  Gold:   this is "Intro to loops"! (starter code below)
# Black:   this file is not used
#
# Name:
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1, n + 1):  # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
print("fac(0) should be 1:", fac(0))
print("fac(5) should be 120:", fac(5))
