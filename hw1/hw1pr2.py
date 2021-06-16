# CS5 Gold/Black: Homework 1 Problem 2
# Filename: hw1pr2.py
# Name: Paul Burke
# Problem description: First few functions!

def dbl(x):
    """
        Results: dbl returns twice its argument
        Arguments:
            x = a number (int or float)
    """
    return 2 * x


def tpl(x):
    """
        Results: tpl returns thrice its argument
        Arguments:
            x = a number (int or float)
    """
    return 3 * x


def sq(x):
    """
        Results: sq returns the square of its argument
        Arguments:
            x = a number (int or float)
    """
    return x * x


def interp(low, hi, frac):
    """
        Results: returns the float that is frac of the way between low and hi
        Arguments:
            low = a number (int or float)
            hi = a number (int or float)
            frac = a number (int or float)
    """
    return low + (hi-low)*frac


def checkends(s):
    """
        Results: returns True if s[0] == s[-1]; else False
        Arguments:
            s = a string
    """
    return s[0] == s[-1]


def has42(d):
    """
        Results: returns True if the key 42 is in d; else False
        Arguments:
            d = a dictionary
    """
    return 42 in d


def hasKey(k, d):
    """
        Results: returns True if k is in d; else False
        Arguments:
            k = anything that can be a key in a dictionary: numbers, strings, bools, lists, etcs
            d = a dictionary
    """
    return k in d


def flipside(s):
    """
        Results: returns a string whose first half is s's second half and whose second half is s's first half
        Arguments:
            s = a string
    """
    return s[len(s)//2:] + s[:len(s)//2]


def convertFromSeconds(s):
    """
        Results: returns [days, hours, minutes, seconds] converted from s seconds
        Arguments:
            s = an integer
    """
    return [s // (24*60*60),                    # days
            s % (24*60*60) // (60*60),          # hours
            s % (24*60*60) % (60*60) // 60,     # minutes
            s % (24*60*60) % (60*60) % 60]      # seconds
