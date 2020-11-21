import argparse
import sys
from result_state import RES_STATE
from heuristics_alghoritms import HEURISTICS


def validate_puzzle(puzzle, size):
    if len(puzzle) != size * size:
        print('Incorrect size of map')
        sys.exit()

    tup_puzzle = tuple(puzzle)

    if len(puzzle) != len(tup_puzzle):
        print('Doubles in the map')
        sys.exit()

    if set(tup_puzzle) != set(range(size*size)):
        print('Incorrect number in the map')
        sys.exit()

    return tup_puzzle


def parse_file(data):
    if len(data) == 0:
        print('Empty file')
        sys.exit()
    data = [row.split('#')[0] for row in data]   # del comments
    data = [row.split() for row in data if len(row) > 0]  # del empty row

    puzzle = []
    for row in data:
        for elem in row:
            if not elem.isdigit():
                print('all symbols in map must be numeric, you give: ', elem)
                sys.exit()
            puzzle.append(int(elem))
    size = puzzle[0]
    puzzle = puzzle[1:]
    validate_puzzle(puzzle, size)
    return puzzle, size


def parse_input():
    parser = argparse.ArgumentParser(description="n-puzzle 21-school Moscow")

    parser.add_argument('-f', help='heuristic function', choices=['manhattan', 'hamming'], default='hamming')
    parser.add_argument('-u', help='uniform cost', action='store_true')
    parser.add_argument('-g', help='greedy search', action='store_true')
    parser.add_argument('-s', help='solved state', default='snail', choices=list(RES_STATE.keys()))
    parser.add_argument('-v', help='visualizer', action='store')
    parser.add_argument('file', help='input file', type=argparse.FileType('r'))

    args = parser.parse_args()
    data = args.file.readlines()
    puzzle, size = parse_file(data)

    return args, tuple(puzzle), size
