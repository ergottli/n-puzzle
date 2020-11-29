from parser import parse_input
from result_state import RES_STATE
import sys
from heuristics import HEURISTICS, uniform_cost, heuristic_decorator
from a_search import a_search





def print_step(puzzle, score, size):
    i = 0
    print(score)
    while i < size**2:
        print(puzzle[i: i+ size])
        i = i + size
    print('\n\n')


if __name__ == '__main__':
    args, puzzle, size = parse_input()

    result_state = RES_STATE[args.s](puzzle, size)
    heuristic_func = HEURISTICS[args.f]
    if args.u:
        heuristic_func = uniform_cost
    heuristic_func = heuristic_decorator(heuristic_func, result_state, size)

    result = a_search(puzzle, result_state, heuristic_func, size)

    if not result:
        print(False)
    else:
        result, space, time = result
        for elem in result:
            print_step(elem, 0, size)
        print(space, time)

