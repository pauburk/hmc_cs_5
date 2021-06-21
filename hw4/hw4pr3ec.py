# CS5 Gold/Black: Homework 4 Problem 3 (extra credit)
# Filename: hw4pr3ec.py
# Name: Paul Burke
# Problem description: Extra credit looping and recursion

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


def increment(S, l):
    """
        Results: returns the next largest binary number after S still using l chars
        Arguments:
            S = a string in binary
            l = a number (integer)
    """
    ans = numToBinary(int(binaryToNum(S))+1)
    return ("0"*(l-len(ans))+ans) if "0" in S else "0"*l


def get_subsequences(S):
    """
        Results: returns a set of all possible subsequences of string S
        Arguments:
            s = a string
    """
    kod = "0"*len(S) # keep or discard
    subsequences = set()

    for i in range(2**len(S)): # go through each increment
        ss_list = [S[i] for i in range(len(S)) if kod[i] == "1"] # create each possible substring
        ss = ""
        ss = ss.join(ss_list)
        subsequences.add(ss)
        kod = increment(kod, len(S)) # go to next substring

    return subsequences


def LCS(S, T):
    """
        Results: returns the longest common subsequence that S and T share
        Arguments:
            S = a string
            T = a string
    """

    if len(S) == 0 or len(T) == 0:
        return ""
    else: # use it or lose it
        if S[0] == T[0]:
            return S[0] + LCS(S[1:], T[1:])
        else:
            r1 = LCS(S[1:], T)
            r2 = LCS(S, T[1:])
            return max([r1, r2], key=len)

# tests
print("==============================\nTesting LCS()\n==============================")
print("LCS('human', 'chimp')        should be  hm :", LCS('human', 'chimp'))
print("LCS('gattaca', 'tacgaacta')  should be  gaaca :", LCS('gattaca', 'tacgaacta'))
print("LCS('wow', 'whew')           should be  ww :", LCS('wow', 'whew'))
print("LCS('', 'whew')              should be  '' :", LCS('', 'whew'))
print("LCS('abcdefgh', 'efghabcd')  should be  'abcd' or 'efgh' :", LCS('abcdefgh', 'efghabcd'))


def loopyLCS(S, T):
    """
        Results: returns the longest common subsequence that S and T share
        Arguments:
            S = a string
            T = a string
        Notes:
            I used a binary approach to either use or not use a letter in the string, then compare all the possible sequences
            Probably not the fastest, but it works!
    """

    S_subsequences = get_subsequences(S)
    T_subsequences = get_subsequences(T)

    intersect = S_subsequences.intersection(T_subsequences) # find all subsequences which exist for both S and T
    intersect_list = list(intersect)

    return max(intersect_list, key=len) if intersect_list else "" # find the longest subsequence

# tests
print("==============================\nTesting loopyLCS()\n==============================")
print("loopyLCS('human', 'chimp')       should be  hm :", loopyLCS('human', 'chimp'))
print("loopyLCS('gattaca', 'tacgaacta') should be  gaaca :", loopyLCS('gattaca', 'tacgaacta'))
print("loopyLCS('wow', 'whew')          should be  ww :", loopyLCS('wow', 'whew'))
print("loopyLCS('', 'whew')             should be  '' :", loopyLCS('', 'whew'))
print("loopyLCS('abcdefgh', 'efghabcd') should be  'abcd' or 'efgh' :", loopyLCS('abcdefgh', 'efghabcd'))
