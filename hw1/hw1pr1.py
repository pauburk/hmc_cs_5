# CS5 Gold/Black: Homework 1 Problem 1
# Filename: hw1pr1.py
# Name: Paul Burke
# Problem description: Challenges with slicing and indexing

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

h = 'harvey'
m = 'mudd'
c = 'college'

print("Check out my crazy attempt for problems 9 and 10!")

# problem 0:  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]
print("\n0:", answer0)

# problem 1:  [7, 1]
answer1 = e[1:]
print("\n1:", answer1)

# problem 2:  [9, 1, 1]
answer2 = pi[-1:0:-2]
print("\n2:", answer2)

# problem 3:  [1, 4, 1, 5, 9]
answer3 = pi[1:]
print("\n3:", answer3)

# problem 4:  [1, 2, 3, 4, 5]
answer4 = e[-1::-2] + pi[::2]
print("\n4:", answer4)

# problem 5:  'hey'
answer5 = h[0] + h[4:6]
print("\n5:", answer5)

# problem 6:  'collude'
answer6 = c[:4] + m[1:3] + c[-1]
print("\n6:", answer6)

# problem 7:  'arveyudd'
answer7 = h[1:] + m[1:]
print("\n7:", answer7)

# problem 8:  'hardeharharhar'
answer8 = h[:3] + (h+m)[-2:3:-4] + 3*h[:3]
print("\n8:", answer8)

# problem 9:  'legomyego'
answer9 = c[3:6] + c[1] + (h+m)[6:4:-1] + (h+c+c[::-1])[4::7]
print("\n9:", answer9)

# problem 10:  'clearcall'
answer10 = c[:5:2] + h[1:3] + (c+h+c)[::8] + c[2]
print("\n10:", answer10)
