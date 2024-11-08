#!/usr/bin/python3
"""N-Queens solution finder."""
import sys


def get_input():
    """Validates and retrieves board size from command line."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos1, pos2):
    """Checks if two queens threaten each other."""
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def build_solution(row, current_solution, solutions, n):
    """Backtracking function to place queens on the board."""
    if row == n:
        solutions.append(current_solution.copy())
        return
    for col in range(n):
        new_pos = [row, col]
        if all(not is_attacking(new_pos, queen) for queen in current_solution):
            current_solution.append(new_pos)
            build_solution(row + 1, current_solution, solutions, n)
            current_solution.pop()


def get_solutions(n):
    """Generates all valid N-Queens solutions."""
    solutions = []
    build_solution(0, [], solutions, n)
    return solutions


if __name__ == "__main__":
    n = get_input()
    solutions = get_solutions(n)
    for solution in solutions:
        print(solution)
