from collections import deque


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


def a_search(puzzle, res_state, heuristic_func, size):
    queue = deque()
    close_set = {}
    open_set = {}

    queue.append((puzzle, heuristic_func(puzzle), None))  # (current_state, score)
    #close_set[puzzle] = None  # key = current state, value = parent

    while queue:
        current_state, current_score, parent = queue.popleft()
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
            return path

        steps = possible_moves(current_state, size)

        current_score += 1

        for step in steps:
            if step in close_set:
                continue
            if step in open_set:
                score = open_set[step]
                if score > current_score:
                    continue
            else:
                score = heuristic_func(step)
                open_set[step] = score

            queue.appendleft((step, score, current_state))

    return False
