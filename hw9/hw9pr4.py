# CS5 Gold/Black: Homework 9 Problem 4
# Filename: hw9pr4.py
# Name: Paul Burke
# Problem description: Read-it-and-Weep sequence


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


def next(term):
    """
        returns the next "read" term
    """
    term = str(term)
    ans = ""
    while True:
        n = frontNum(term)
        ans += f"{n}{term[0]}"
        term = term[n:]
        if len(term) == 0: break
    return int(ans)


def readit(n):
    """
        prints first n terms of the read-it-and-weep sequence
    """
    cur = "1"
    for i in range(n):
        print(cur)
        cur = next(cur)
