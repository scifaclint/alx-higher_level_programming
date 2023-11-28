#!/usr/bin/python3
"""N queens puzzle solver.

This module contains a program that solves the N queens problem of placing N
non-attacking queens on an N×N chessboard.

Attributes:
    number_of_instances (int): The number of Rectangle instances.

"""

import sys


def solve_nqueens(n):
    """Solve the N queens problem.

    This function solves the N queens problem using backtracking and prints
    every possible solution to the problem.

    Args:
        n (int): The number of queens and the size of the chessboard.

    Returns:
        None

    """
    if n < 4:
        print("N must be at least 4")
        return
    result = []
    cols = [0] * n
    place_queen(cols, 0, n, result)
    print_result(result, n)


def can_place(cols, ocuppied_rows, ocuppied_diagonals):
    """Check if a queen can be placed at the given position.

    Args:
        cols (list of int): The column indices where the queens are placed.
        ocuppied_rows (int): The number of occupied rows.
        ocuppied_diagonals (int): The number of occupied diagonals.

    Returns:
        bool: True if a queen can be placed at the given position,
        False otherwise.

    """
    for i in range(ocuppied_rows):
        if cols[i] == cols[ocuppied_rows] or \
                cols[i] - i == cols[ocuppied_rows] - ocuppied_rows or \
                cols[i] + i == cols[ocuppied_rows] + ocuppied_rows:
            return False
    return True


def place_queen(cols, start, end, result):
    """Place a queen in the given row.

    Args:
        cols (list of int): The column indices where the queens are placed.
        start (int): The starting row index.
        end (int): The ending row index (the size of the chessboard).
        result (list of list of int): The result list that
        contains all possible solutions.

    Returns:
        None

    """
    if start == end:
        result.append(cols[:])
        return
    for i in range(end):
        cols[start] = i
        if can_place(cols, start, end):
            place_queen(cols, start + 1, end, result)


def print_result(result, n):
    """Print the result.

    Args:
        result (list of list of int): The result list that
        contains all possible solutions.
        n (int): The number of queens and the size of the chessboard.

    Returns:
        None

    """
    for res in result:
        print("[", end="")
        for i in range(n):
            print("[{}, {}]".format(i, res[i]), end="")
            if i != n - 1:
                print(", ", end="")
        print("]")


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
solve_nqueens(n)
