def heuristic_decorator(func, result_state, size):
    def heuristic_wrapper(puzzle):
        return func(puzzle, result_state, size)

    return heuristic_wrapper


def uniform_cost(puzzle, result_state, size):
    return 0


def hamming_distance(puzzle, result_state, size):
    res = 0
    for i in range(size**2):
        if puzzle[i] != 0 and puzzle[i] != result_state[i]:
            res += 1
    return res


HEURISTICS = {'hamming': hamming_distance}
