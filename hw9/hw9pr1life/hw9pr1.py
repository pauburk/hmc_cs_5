# CS5 Gold/Black: Homework 9 Problem 1
# Filename: hw9pr1.py
# Name: Paul Burke
# Problem description: Game of Life

import random
import numpy as np


def diagonalize(arr):
    """
        Modifies board to have diagonal strip of "on" cells only in the interior
    """

    for row in range(1, arr.shape[0] - 1):
        for col in range(1, arr.shape[1] - 1):
            if row == col: arr[row][col] = 1

    return arr

def innerCells(arr):
    """
        Modifies board to turn all interior cells on
    """

    for row in range(1, arr.shape[0] - 1):
        for col in range(1, arr.shape[1] - 1):
            arr[row][col] = 1

    return arr

def randomCells(arr):
    """
        Modifies board to turn all interior cells randomly on or off
    """

    for row in range(1, arr.shape[0] - 1):
        for col in range(1, arr.shape[1] - 1):
            if random.choice([0, 1]) == 0: arr[row][col] = 1

    return arr

def copy(arr):
    return arr.copy()

def innerReverse(arr):
    """
        Modifies board to flip the states of the inner cells
    """

    for row in range(1, arr.shape[0] - 1):
        for col in range(1, arr.shape[1] - 1):
            arr[row][col] = 0 if arr[row][col] == 1 else 1

    return arr


def print_board(arr):
    """
        prints arr nicely
    """
    for row in arr:
        for col in row:
            print(col, end="")
        print()


def countNeighbors(row, col, arr):
    """
        counts "on" cells in 8 grid around arr[row][col]
    """
    sum = 0
    for r in [row-1, row, row+1]:
        for c in [col-1, col, col+1]:
            if arr[r][c] == 1:
                sum += 1
    sum -= arr[row, col]
    return sum

def next_life_generation(arr):
    """
        Makes a copy of A and then advances one
        generation of Conway's Game of Life within
        the *inner cells* of that copy.
        The outer edge always stays at 0.
    """

    bring_to_life = []
    kill_off = []

    for row_idx in range(1, arr.shape[0]-1):
        for col_idx in range(1, len(arr[row_idx])-1):
            if arr[row_idx][col_idx] == 0 and countNeighbors(row_idx, col_idx, arr) == 3:
                bring_to_life.append([row_idx, col_idx])
            elif arr[row_idx][col_idx] == 1 and countNeighbors(row_idx, col_idx, arr) not in [2, 3]:
                kill_off.append([row_idx, col_idx])

    for idx in bring_to_life:
        arr[idx[0]][idx[1]] = 1

    for idx in kill_off:
        arr[idx[0]][idx[1]] = 0

    return arr


def setup():

    width = 10
    height = 10
    board = np.zeros((height, width)).astype(int)

    return board


def main():

    board = setup()
    board[4][5] = 1
    board[5][5] = 1
    board[6][5] = 1
    print_board(board)
    print()
    board = next_life_generation(board)
    print_board(board)


main()
