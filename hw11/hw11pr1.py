# CS5 Gold/Black: Homework 11 Problem 1
# Filename: hw11pr1.py
# Name: Paul Burke
# Problem description: Menus of options!

from math import *


def menu():
    """ prints menu"""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Quit")
    print()


def my_sum(L):
    """ returns sum of list"""
    sum = 0
    for i in L: sum += i
    return sum


def my_avg(L):
    """ returns avg of list"""
    return my_sum([i for i in L]) / len(L)


def my_min(L):
    """ returns min of L"""
    min = -1
    for i in L:
        if i < min or min == -1:
            min = i
    return min


def my_max(L):
    """ returns max of L"""
    max = -1
    for i in L:
        if i > max:
            max = i
    return max


def find_diff(L):
    """ returns indexes of items with largest gap in value going forward (small then large)"""
    ans = {"diff" : 0}
    for i in range(len(L)):
        for j in list(range(len(L)))[i:]:
            if L[j] - L[i] > ans["diff"]:
                ans["diff"] = L[j] - L[i]
                ans["i"] = i
                ans["j"] = j
    return ans


def main():

    L = [20, 10, 30]  # an initial list

    while True:     # the user-interaction loop
        menu()
        choice = input("Enter your choice: ")
        while not choice.isnumeric() or int(choice) not in [0,1,2,3,4,5,6,9]: choice = input("Please enter a valid choice. ") # get valid choice
        choice = int(choice)

        # run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # enter _something_

            #
            # "Clean and check" the user's input
            #
            try:
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]):
                    print("\nThat didn't seem like a list. Not changing L.")
                else:
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("\nI didn't understand your input. Not changing L.")

        elif choice == 1:  # Print current list

            print("\n{0: >4} : $ {1: >6}".format("Day", "Price"))
            for i in range(len(L)):
                print("{0: >4} : $ {1: >6}".format(i, round(float(L[i]), 2)))
            print()

        elif choice == 2: # average

            average = my_avg(L)
            print(f"\nThe average price is {round(average, 2)}\n")

        elif choice == 3: # standard deviation

            Lavg = my_avg(L)
            stdev = sqrt(my_sum([(L[i] - Lavg)**2 for i in range(len(L))])/len(L))
            print(f"\nThe st. deviation is {stdev}\n")

        elif choice == 4: # min

            min = my_min(L)
            print(f"\nThe min is {min} on day {L.index(min)}")

        elif choice == 5: # max

            max = my_max(L)
            print(f"\nThe max is {max} on day {L.index(max)}")

        elif choice == 6:

            ans = find_diff(L)
            print("Your TTS investment strategy is to:")
            print(f"  Buy on day {ans['i']} at price {L[ans['i']]}")
            print(f"  Sell on day {ans['j']} at price {L[ans['j']]}")
            print(f"  For a total profit of {ans['diff']}")


main()
