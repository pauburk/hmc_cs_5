# CS5 Gold/Black: Homework 8 Problem 4
# Filename: hw8pr4.py
# Name: Paul Burke
# Problem description: List comprehensions

import math
from math import *

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

# printing tests
print("==============================\nTesting lc_mult(), lc_idiv(), lc_fdiv()\n==============================")
print( "lc_mult(4)   should be [0, 2, 4, 6] :", lc_mult(4) )
print( "lc_idiv(4)   should be [0, 0, 1, 1] :", lc_idiv(4) )
print( "lc_fdiv(4)   should be [0.0, 0.5, 1.0, 1.5] :", lc_fdiv(4) )

# assertion tests
assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:


def unitfracs(N):
    """
        returns a list of evenly-spaced left-hand endpoints in the unit interval [0, 1)
    """
    return [x/N for x in range(N)]

# tests
print("==============================\nTesting unitfracs()\n==============================")
print( "unitfracs(4)   should be [0.0, 0.25, 0.5, 0.75] :", unitfracs(4) )
print( "unitfracs(5)   should be [0.0, 0.2, 0.4, 0.6, 0.8] :", unitfracs(5) )
print( "unitfracs(10)  should be [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] :", unitfracs(10) )


def scaledfracs(low, hi, N):
    """
        returns a list of N evenly-spaced left-hand endpoints in the interval [low, hi)
    """
    return [low + (hi-low)*x for x in unitfracs(N)]

# tests
print("==============================\nTesting scaledfracs()\n==============================")
print( "scaledfracs(10, 30, 5)  should be [10.0, 14.0, 18.0, 22.0, 26.0] :", scaledfracs(10, 30, 5) )
print( "scaledfracs(41, 43, 8)  should be [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75] :", scaledfracs(41, 43, 8) )
print( "scaledfracs(0, 10, 4)   should be [0.0, 2.5, 5.0, 7.5] :", scaledfracs(0, 10, 4) )


def sqfracs(low, hi, N):
    """
        returns the same as scaledfracs() except each value is squared
    """
    return [x**2 for x in scaledfracs(low, hi, N)]

# tests
print("==============================\nTesting sqfracs()\n==============================")
print( "sqfracs(4, 10, 6)   should be [16.0, 25.0, 36.0, 49.0, 64.0, 81.0] :", sqfracs(4, 10, 6) )
print( "sqfracs(0, 10, 5)   should be [0.0, 4.0, 16.0, 36.0, 64.0] :", sqfracs(0, 10, 5) )


def f_of_fracs(f, low, hi, N):
    """
        returns the same as scaledfracs() except each value is squared
    """
    return [f(x) for x in scaledfracs(low, hi, N)]

# tests
print("==============================\nTesting f_of_fracs()\n==============================")
print( "f_of_fracs(dbl, 10, 20, 5)  should be [20.0, 24.0, 28.0, 32.0, 36.0] :", f_of_fracs(dbl, 10, 20, 5) )
print( "f_of_fracs(sq, 4, 10, 6)    should be [16.0, 25.0, 36.0, 49.0, 64.0, 81.0] :", f_of_fracs(sq, 4, 10, 6) )
print( "f_of_fracs(sin, 0, pi, 2)   should be [0.0, 1.0] :", f_of_fracs(sin, 0, pi, 2) )


def integrate(f, low, hi, N):
    """
        returns integral of f from low to hi using N steps
    """
    return sum([f(x) for x in scaledfracs(low, hi, N)])*(hi-low)/N

# tests
print("==============================\nTesting integrate()\n==============================")
print( "integrate(dbl, 0, 10, 4)                should be 75.0 :", integrate(dbl, 0, 10, 4) )
print( "integrate(dbl, 0, 10, 1000)             should be 100.0 :", integrate(dbl, 0, 10, 1000) )
print( "integrate(sq, 0, 3, 1000000)            should be 9.0 :", integrate(sq, 0, 3, 1000000) )
print( "integrate(math.sin, 0, math.pi, 1000)   should be 2.0 :", integrate(math.sin, 0, math.pi, 1000) )


"""Q1.

    When we are approximating the integral using a left-side Riemann sum, we
    will always end up with an approximation less than the actual integral,
    because the rectangles drawn will always have a little gap between the
    top-right or top-left vertex and the function (depends on whether the
    function currently has a positive or negative slope). Basically, the flat
    top of a non-zero width rectangle can't match the curve or sloped arc of
    the function.

    The fuction f(x) = -x + 12. Because the rectangles would be created with
    the height equal to y, the top of each rectangle would extend over the
    negatively sloped line.

"""

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

# tests
print("==============================\nTesting integrate(c)\n==============================")
print( "integrate(c, 0, 2, 2)       should be 3.732 :", integrate(c, 0, 2, 2) )
print( "integrate(c, 0, 2, 20)      should be 3.228 :", integrate(c, 0, 2, 20) )

"""Q2.

    We know that A = pi*r^2, and if we have a circle with radius 2 we can
    simplify to A = pi*4, so pi = A/4. When we calculate the integral from
    0 to 2 of a semi-circle with radius 2 and centered at the origin, we are
    effectively calculating 1/4 of the circle's area (integrals are area
    under the curve), or A/4, which equals pi. The values 3.732 and 3.228 are
    approaching 3.14.

"""
