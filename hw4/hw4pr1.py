# CS5 Gold/Black: Homework 4 Problem 1
# Filename: hw4pr1.py
# Name: Paul Burke
# Problem description: Binary <-> decimal conversions

def isOdd(N):
    """
        Results: returns True if n is odd; False if n is even
        Arguments:
            N = a number
    """
    return bool(N % 2)

# tests
print("==============================\nTesting isOdd()\n==============================")
print( "isOdd(42)    should be  False :", isOdd(42) )
print( "isOdd(43)    should be  True :", isOdd(43) )


def numToBinary(N):
    """
        Results: returns N in binary
        Arguments:
            N = a number in base 10
    """
    if N == 0:
        return ""
    elif N % 2 == 1:
        return numToBinary(int(N/2)) + "1"
    else:
        return numToBinary(int(N/2)) + "0"

# tests
print("==============================\nTesting numToBinary()\n==============================")
print( "numToBinary(0)      should be  '' :",  numToBinary(0) )
print( "numToBinary(1)      should be  '1' :",  numToBinary(1) )
print( "numToBinary(4)      should be  '100' :",  numToBinary(4) )
print( "numToBinary(10)     should be  '1010' :",  numToBinary(10) )
print( "numToBinary(42)     should be  '101010' :",  numToBinary(42) )
print( "numToBinary(100)    should be  '1100100' :",  numToBinary(100) )


def binaryToNum(S):
    """
        Results: returns S in decimal
        Arguments:
            S = a string in binary
    """
    if S == "":
        return 0
    elif S[-1] == "1":
        return 2*binaryToNum(S[:-1]) + 1
    else:
        return 2*binaryToNum(S[:-1]) + 0

print("==============================\nTesting binaryToNum()\n==============================")
print( "binaryToNum('')      should be  0 :",  binaryToNum('') )
print( "binaryToNum('1')      should be  1 :",  binaryToNum("1") )
print( "binaryToNum('100')      should be  4 :",  binaryToNum("100") )
print( "binaryToNum('1010')     should be  10 :",  binaryToNum("1010") )
print( "binaryToNum('101010')     should be  42 :",  binaryToNum("101010") )
print( "binaryToNum('1100100')    should be  100 :",  binaryToNum("1100100") )


def increment(S):
    """
        Results: returns the next largest binary number after S still using 8 chars
        Arguments:
            S = a string in binary
    """
    ans = numToBinary(int(binaryToNum(S))+1)
    return ("0"*(8-len(ans))+ans) if "0" in S else "00000000"

# tests
print("==============================\nTesting increment()\n==============================")
print( "increment('00101001')    should be  00101010 :", increment('00101001') )
print( "increment('00000011')    should be  00000100 :", increment('00000011') )
print( "increment('11111111')    should be  00000000 :", increment('11111111') )


def count(S, n):
    """
        Results: returns n counts up from S
        Arguments:
            S = a string in binary
            n = an integer
    """
    for i in range(n):
        print(S)
        S = increment(S)
    print(S)

# tests
print("==============================\nTesting count()\n==============================")
print("count('00000000', 4):")
count("00000000", 4)
print("count('11111110', 5)")
count("00000000", 4)


def numToTernary(N):
    """
        Results: returns N in ternary
        Arguments:
            N = a number in base 10
    """
    if N == 0:
        return ""
    elif N % 3 == 1:
        return numToTernary(int(N/3)) + "1"
    elif N % 3 == 2:
        return numToTernary(int(N/3)) + "2"
    else:
        return numToTernary(int(N/3)) + "0"

# tests
print("==============================\nTesting numToTernary()\n==============================")
print( "numToTernary(0)      should be  '' :",  numToTernary(0) )
print( "numToTernary(1)      should be  '1' :",  numToTernary(1) )
print( "numToTernary(4)      should be  '11' :",  numToTernary(4) )
print( "numToTernary(10)     should be  '101' :",  numToTernary(10) )
print( "numToTernary(42)     should be  '1120' :",  numToTernary(42) )
print( "numToTernary(100)    should be  '10201' :",  numToTernary(100) )


def ternaryToNum(S):
    """
        Results: returns S in decimal
        Arguments:
            S = a string in ternary
    """
    if S == "":
        return 0
    elif S[-1] == "1":
        return 3*ternaryToNum(S[:-1]) + 1
    elif S[-1] == "2":
        return 3*ternaryToNum(S[:-1]) + 2
    else:
        return 3*ternaryToNum(S[:-1]) + 0

print("==============================\nTesting ternaryToNum()\n==============================")
print( "ternaryToNum('')      should be  0 :",  ternaryToNum('') )
print( "ternaryToNum('1')      should be  1 :",  ternaryToNum("1") )
print( "ternaryToNum('11')      should be  4 :",  ternaryToNum("11") )
print( "ternaryToNum('101')     should be  10 :",  ternaryToNum("101") )
print( "ternaryToNum('1120')     should be  42 :",  ternaryToNum("1120") )
print( "ternaryToNum('10201')    should be  100 :",  ternaryToNum("10201") )


def numToBalancedTernary(N):
    """
        Results: returns N in balanced ternary
        Arguments:
            N = a number in base 10
    """
    if N == 0:
        return ""
    elif N % 3 == 1:
        return numToBalancedTernary(int(N/3)) + "0"
    elif N % 3 == 2:
        return numToBalancedTernary(int(N/3)) + "+"
    else:
        return numToBalancedTernary(int(N/3)) + "-"

# tests
print("==============================\nTesting numToBalancedTernary()\n==============================")
print( "numToBalancedTernary(0)      should be  '' :",  numToBalancedTernary(0) )
print( "numToBalancedTernary(1)      should be  '0' :",  numToBalancedTernary(1) )
print( "numToBalancedTernary(4)      should be  '00' :",  numToBalancedTernary(4) )
print( "numToBalancedTernary(10)     should be  '0-0' :",  numToBalancedTernary(10) )
print( "numToBalancedTernary(42)     should be  '00+-' :",  numToBalancedTernary(42) )
print( "numToBalancedTernary(100)    should be  '0-+-0' :",  numToBalancedTernary(100) )


def ternaryToBalancedNum(S):
    """
        Results: returns S in decimal
        Arguments:
            S = a string in balanced ternary
    """
    if S == "":
        return 0
    elif S[-1] == "0":
        return 3*ternaryToBalancedNum(S[:-1]) + 1
    elif S[-1] == "+":
        return 3*ternaryToBalancedNum(S[:-1]) + 2
    else:
        return 3*ternaryToBalancedNum(S[:-1]) + 0

print("==============================\nTesting binaryToNum()\n==============================")
print( "ternaryToBalancedNum('')      should be  0 :",  ternaryToBalancedNum('') )
print( "ternaryToBalancedNum('0')      should be  1 :",  ternaryToBalancedNum("0") )
print( "ternaryToBalancedNum('00')      should be  4 :",  ternaryToBalancedNum("00") )
print( "ternaryToBalancedNum('0-0')     should be  10 :",  ternaryToBalancedNum("0-0") )
print( "ternaryToBalancedNum('00+-')     should be  42 :",  ternaryToBalancedNum("00+-") )
print( "ternaryToBalancedNum('0-+-0')    should be  100 :",  ternaryToBalancedNum("0-+-0") )
