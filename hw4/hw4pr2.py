# CS5 Gold/Black: Homework 4 Problem 2
# Filename: hw4pr2.py
# Name: Paul Burke
# Problem description: Conversions and compressions

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


def frontNum(S):
    """
        Results: returns the number of consecutive identical characters of S
        Arguments:
            S = a string
    """
    if len(S) < 2:
        return len(S)
    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1


def compress(S):
    """
        Results: returns the run-length encoding of S in binary
        Arguments:
            S = a string in binary
    """
    if len(S) == 0:
        return ""
    else:
        n = frontNum(S)
        return S[0] + ("0000000" + numToBinary(n))[-7:] + compress(S[n:])

# tests
print("==============================\nTesting compress()\n==============================")
print( "compress('0011')    should be  '0000001010000010' :",  compress('0011') )
print( "compress(64*'0')    should be  '01000000' :",  compress(64*'0') )
print( "compress('11111')   should be  '10000101' :",  compress('11111') )
Stripes = '0'*16 + '1'*16 + '0'*16 + '1'*16
CStripes = '00010000100100000001000010010000'
print( "compress(Stripes)==CStripes   should be  True :",  compress(Stripes)==CStripes )


def uncompress(S):
    """
        Results: returns binary string from compressed string S
        Arguments:
            S = a string in binary
    """
    if len(S) == 0:
        return ""
    else:
        return S[0]*binaryToNum(S[1:8]) + uncompress(S[8:])

# tests
print("==============================\nTesting uncompress()\n==============================")
print( "uncompress('10000101') should be  '11111' :",  uncompress('10000101') )
Stripes = '0'*16 + '1'*16 + '0'*16 + '1'*16
CStripes = '00010000100100000001000010010000'
print( "uncompress(CStripes)==Stripes should be  True :",  uncompress(CStripes)==Stripes )
