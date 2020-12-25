from n_puzzle import parse_input
from n_puzzle import PuzzleSolver


if __name__ == "__main__":
    args, puzzle, size = parse_input()

    ps = PuzzleSolver(args, puzzle, size)
    ps.solve_npuzzle()
    ps.print_result()
