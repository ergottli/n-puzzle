import math

# puzzle
#  2  7  8  1
#  5 11  3  9
# 12  6  4  15
# 13  10 14 0

# result_state
#  1  2  3  4
# 12 13 14  5
# 11  0 15  6
# 10  9  8  7

def manhattan(puzzle, result_state, size):
    res = 0
    for i in range(size*size):
        if puzzle[i] != 0 and puzzle[i] != result_state[i]:
            result_state_index = result_state.index(puzzle[i])
            horizontal_shift = abs(math.ceil(i / size) - math.ceil(result_state_index / size))
            vertical_shift = abs((i + size * horizontal_shift) - result_state_index)
            res += horizontal_shift + vertical_shift
    return res

def 
