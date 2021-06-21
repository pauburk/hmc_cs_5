# CS5 Gold/Black: Homework 3 Problem 1
# Filename: hw3pr1.py
# Name: Paul Burke
# Problem description: Function frenzy!


def mult(n, m):
    """
        Results: returns n*m without using the * operator
        Arguments:
            n = an integer
            m = an integer
        Notes: the if statements are used to get the signs correct
    """
    if n == 0 or m == 0:                # if either are 0
        return 0
    elif n > 0 and m > 0:               # if both are positive
        return n + mult(n, m-1)
    elif n > 0 and m < 0:               # if n is positive and m is negative
        return m + mult(n-1, m)
    elif n < 0 and m > 0:               # if n is negative and m is positive
        return n + mult(n, m-1)
    elif n < 0 and m < 0:               # if they are both negative
        return 0 - n + mult(n, m+1)

# tests
print("==============================\nTesting mult()\n==============================")
print( "mult(6, 7)           should be  42 :",  mult(6, 7) )
print( "mult(6, -7)          should be  -42 :",  mult(6, -7) )
print( "mult(-6, 7)          should be  -42 :",  mult(-6, 7) )
print( "mult(-6, -7)         should be  42 :",  mult(-6, -7) )
print( "mult(6, 0)           should be  0 :",  mult(6, 0) )
print( "mult(0, 7)           should be  0 :",  mult(0, 7) )
print( "mult(0, 0)           should be  0 :",  mult(0, 0) )


def dot(L, K):
    """
        Results: returns the dot product of the lists L and K; if len(L) != len(K) or lengths are 0 returns 0.0
        Arguments:
            L = list of numbers
            K = list of numbers
    """
    if len(L) != len(K):
        return 0
    elif len(L) == 0 and len(L) == 0:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

# tests
print("==============================\nTesting dot()\n==============================")
print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )


def ind(e, L):
    """
        Results: returns the index of the first occurence of e in L; if e DNE then returns len(L)
        Arguments:
            e = character
            L = string
    """

    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return 1
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])

# tests
print("==============================\nTesting ind()\n==============================")
print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration') )


def letterScore(let):
    """
        Results: returns the value of let as a Scrabble tile
        Arguments:
            let = single letter (capital or lower)
    """
    scores =  { 'a': 1,  'b': 3,  'c': 3,  'd': 2,  'e': 1,
                'f': 4,  'g': 2,  'h': 4,  'i': 1,  'j': 8,
                'k': 5,  'l': 1,  'm': 3,  'n': 1,  'o': 1,
                'p': 3,  'q': 10, 'r': 1,  's': 1,  't': 1,
                'u': 1,  'v': 4,  'w': 4,  'x': 8,  'y': 4,
                'z': 10   }
    let = let.lower()
    return scores[let] if let in scores else 0

# tests
print("==============================\nTesting letterScore()\n==============================")
print( "letterScore(\"a\") should be  1 :",  letterScore("a") )
print( "letterScore(\"q\") should be  10 :",  letterScore("q") )
print( "letterScore(\"w\") should be  4 :",  letterScore("w") )
print( "letterScore(\"4\") should be  0 :",  letterScore("4") )


def scrabbleScore(S):
    """
        Results: returns the value of S as a Scrabble word
        Arguments:
            S = a string of letters
    """
    scores =  { 'a': 1,  'b': 3,  'c': 3,  'd': 2,  'e': 1,
                'f': 4,  'g': 2,  'h': 4,  'i': 1,  'j': 8,
                'k': 5,  'l': 1,  'm': 3,  'n': 1,  'o': 1,
                'p': 3,  'q': 10, 'r': 1,  's': 1,  't': 1,
                'u': 1,  'v': 4,  'w': 4,  'x': 8,  'y': 4,
                'z': 10   }
    if len(S) > 0 and S[0].lower() in scores:
            return scores[S[0].lower()] + scrabbleScore(S[1:])
    else:
        return 0

# tests
print("==============================\nTesting scrabbleScore()\n==============================")
print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )


def convert(c):
        """
            Converts a single-character c from DNA
            nucleotide to its complementary RNA nucleotide
        """
        conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' } # dictionary with each conversion
        if c in conversion:        # is it a key?
            return conversion[c]   # if so, return its value
        else:                      # otherwise
            return ''              # return the empty string


def transcribe(S):
    """
        Results: returns the transcribed RNA from a given DNA sequence
        Arguments:
            S = a string
    """
    if len(S) > 0:
        return convert(S[0]) + transcribe(S[1:])
    else:
        return ""

# tests
print("==============================\nTesting transcribe()\n==============================")
print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!


def pigletLatin(s):
    """
        Results: returns the translation of s to piglet latin (see rules at the link below)
                 https://www.cs.hmc.edu/twiki/bin/view/CS5/FunctionFrenzyGold
        Arguments:
            s = a string
    """
    s = s.lower()
    if len(s) == 0 or s[0] in "aeiou":
        return s + "way"
    else:
        return s[1:] +  s[0] + "ay"

# tests
print("==============================\nTesting pigletLatin()\n==============================")
assert pigletLatin("hello") == "ellohay"
assert pigletLatin("goodbye") == "oodbyegay"
print( "pigletLatin('yoda')    should be 'odayay' :",  pigletLatin('yoda') )
print( "pigletLatin('one')    should be 'oneway' :",  pigletLatin('one') )
print( "pigletLatin('aloha')    should be 'alohaway' :",  pigletLatin('aloha') )


def get_starting_consonants(s):
    """
        Results: returns all starting consonants of s
        Arguments:
            s = a string
    """
    if len(s) == 0:
        return ""
    elif s[0] == "y" and s[1] in "aeiou":
        return s[0] # only return y because next letter is vowel
    elif s[0] not in "aeiouy":
        return s[0] + get_starting_consonants(s[1:])
    else:
        return ""


def pigLatin(s):
    """
        Results: returns the translation of s to pig latin (see rules at the link below)
                 https://www.cs.hmc.edu/twiki/bin/view/CS5/FunctionFrenzyGold
        Arguments:
            s = a string
        Notes:
            I treat all y's as consants if they are followed by a vowel and vowels if they are followed by a consonant
            If there are 2 y's in a row they both become vowels
    """
    s = s.lower()
    sc = get_starting_consonants(s)
    end = "ay" if len(sc) > 0 else "way" # ending is "ay" if there is a starting consonant and "way" if there is a starting vowel
    return s[max(len(sc), 0):] + sc + end

# tests
print("==============================\nTesting pigLatin()\n==============================")
print( "pigLatin('string')    should be 'ingstray' :",  pigLatin('string') )
print( "pigLatin('yttrium')    should be 'yttriumway' :",  pigLatin('yttrium') )
print( "pigLatin('yoohoo')    should be 'oohooyay' :",  pigLatin('yoohoo') )
print( "pigLatin('stymie')    should be 'ymiestay' :",  pigLatin('stymie') )
print( "pigLatin('yytest')    should be 'yytestway' :",  pigLatin('yytest') )
