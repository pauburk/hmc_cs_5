# CS5 Gold/Black: Homework 9 Problem 2
# Filename: hw9pr2.py
# Name: Paul Burke
# Problem description: Jotto and Caesar!

def encipher(S, n):
    """
        enciphers string S by incrementing each character in S n times forward into the alphabet
        keeps capitalization
        uses ord() and chr() instead of dictionary
    """
    S_enc = ""
    for char in S:
        i = ord(char[0]) # get ascii index
        if 65 <= i and i <= 90: # uppercase
            i += n
            if i > 90: i = 65 + i - 91
        elif 97 <= i and i <= 122: # lowercase
            i += n
            if i > 122: i = 97 + i - 123
        S_enc += chr(i) # convert back to char, add to encoded string
    return S_enc

# tests
print("==============================\nTesting encipher()\n==============================")
print("encipher('xyza', 1)                                      should be 'yzab' :", encipher('xyza', 1))
print("encipher('Z A', 1)                                       should be 'A B' :", encipher('Z A', 1))
print("encipher('*ab?', 1)                                      should be '*bc?' :", encipher('*ab?', 1))
print("encipher('This is a string!', 1)                         should be 'Uijt jt b tusjoh' :", encipher('This is a string!', 1))
print("encipher('Caesar cipher? I prefer Caesar salad.', 25)     should be 'Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.' :", encipher('Caesar cipher? I prefer Caesar salad.', 25))


def get_score(char, group):
    """
        returns the scrabble score or probability of c (upper or lower case)
        return 0 if c is not a letter
    """
    scores =    {
                "scrabble" : {  'e':1,
                                't':1, 'a':1, 'o':1, 'i':1,
                                'n':1, 'h':4, 's':1, 'r':1,
                                'd':2, 'l':1, 'u':1, 'm':3,
                                'c':3, 'w':4, 'f':4, 'y':4,
                                'g':2, 'p':3, 'b':3, 'v':4,
                                'k':5, 'x':8, 'j':8, 'q':10,
                                'z':10, '-':0
                            },
                "probability" : {   'e':0.1017,
                                    't':0.0737, 'a':0.0661, 'o':0.0610, 'i':0.0562,
                                    'n':0.0557, 'h':0.0542, 's':0.0508, 'r':0.0458,
                                    'd':0.0369, 'l':0.0325, 'u':0.0228, 'm':0.0205,
                                    'c':0.0192, 'w':0.0190, 'f':0.0175, 'y':0.0165,
                                    'g':0.0161, 'p':0.0131, 'b':0.0115, 'v':0.0088,
                                    'k':0.0066, 'x':0.0014, 'j':0.0008, 'q':0.0008,
                                    'z':0.0005, '-':1
                                }
                }

    char = char.lower()
    return scores[group][char] if char in scores[group] else scores[group]["-"]


def decipher(S):
    """
        deciphers S using either scrabble of probability values (default is scrabble)
    """
    iterations = [encipher(S, i) for i in range(26)]
    scrabble_scores = [[sum([get_score(c, "scrabble") for c in S]), S] for S in iterations]
    # print(f"{S} deciphered is '{min(scrabble_scores)[1]}' using scrabble values (score of {min(scrabble_scores)[0]})")
    # probability_scores = [[sum([get_score(c, "probability") for c in S]), S] for S in iterations]
    # print(f"{S} deciphered is '{max(probability_scores)[1]}' using probability values (score of {round(max(probability_scores)[0], 3)})")
    return min(scrabble_scores)[1]

# tests
print("==============================\nTesting decipher()\n==============================")
print("decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.')                                        should be 'Caesar cipher? I prefer Caesar salad.' :", decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
print("decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.')     should be 'An education is what remains after we forget everything we have learned.' :", decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))


def jscore(S, T):
    """
        returns the "jotto score" of S compared with T
    """
    if len(S) == 0 or len(T) == 0:
        return 0
    elif S[0] in T:
        return 1 + jscore(S[1:], T.replace(S[0], "", 1))
    else:
        return 0 + jscore(S[1:], T)

print("==============================\nTesting jscore()\n==============================")
print("jscore('diner', 'syrup')             should be 1 :", jscore('diner', 'syrup'))
print("jscore('geese', 'elate')             should be 2 :", jscore('geese', 'elate'))
print("jscore('gattaca', 'aggtccaggcgc')    should be 5 :", jscore('gattaca', 'aggtccaggcgc'))
print("jscore('gattaca', '')                should be 0 :", jscore('gattaca', ''))
