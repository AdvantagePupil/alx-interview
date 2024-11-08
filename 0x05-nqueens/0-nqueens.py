#!/usr/bin/python3
import sys

def is_safe(queens, row, col):
    """Check if it's safe to place a queen at row, col."""
    for i in range(col):
        if queens[i] == row or abs(queens[i] - row) == abs(i - col):
            return False
    return True

def solve_nqueens(N):
    """Generate all solutions for the N-queens problem."""
    solutions = []
    queens = [-1] * N  # Initialize queens positions

    def backtrack(col):
        if col == N:
            solutions.append([[i, queens[i]] for i in range(N)])
            return
        for row in range(N):
            if is_safe(queens, row, col):
                queens[col] = row
                backtrack(col + 1)
                queens[col] = -1

    backtrack(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
