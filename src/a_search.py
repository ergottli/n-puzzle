from collections import deque
from queue import PriorityQueue


def print_step(puzzle, score, size):
    i = 0
    print(score)
    while i < size**2:
        print(puzzle[i: i+ size])
        i = i + size
    print('\n\n')


def create_new_state(puzzle, zero_index, move):
    elem = puzzle[move]
    new = list(puzzle)
    new[zero_index] = elem
    new[move] = 0
    return tuple(new)


def possible_moves(puzzle, size):

    zero_index = puzzle.index(0)
    res = []

    if zero_index - size >= 0:
        new_state = create_new_state(puzzle, zero_index, zero_index - size)
        res.append(new_state)

    if zero_index + size < size**2:
        new_state = create_new_state(puzzle, zero_index, zero_index + size)
        res.append(new_state)

    if zero_index % size + 1 < size:
        new_state = create_new_state(puzzle, zero_index, zero_index + 1)
        res.append(new_state)

    if zero_index % size > 0:
        new_state = create_new_state(puzzle, zero_index, zero_index - 1)
        res.append(new_state)

    return res


def a_search(puzzle, res_state, heuristic_func, size, step_cost):
    queue = PriorityQueue()
    close_set = {}
    open_set = {}

    queue.put((0, puzzle, heuristic_func(puzzle), None))  # (current_score, (current_state, g, parent))
    #close_set[puzzle] = None  # key = current state, value = parent

    while not queue.empty():
        _, current_state, g, parent = queue.get()
        #print_step(current_state, current_score, size)

        if current_state in close_set:
            continue

        close_set[current_state] = parent

        if current_state == res_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = close_set[current_state]
            path.reverse()
            return path, len(open_set), len(close_set)

        steps = possible_moves(current_state, size)

        next_g = g + step_cost

        for step in steps:
            if step in close_set:
                continue
            if step in open_set:
                g, _ = open_set[step]
                if g <= next_g:
                    continue
            else:
                step_h = heuristic_func(step)
                open_set[step] = next_g, step_h
                queue.put((next_g + step_h, step, next_g, current_state))

    return False
