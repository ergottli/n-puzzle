

def back_n_forth(puzzle, size):
    puzzle = sorted(puzzle)
    for num in range(size):
        if num % 2 == 1:
            puzzle[num*size:num*size+size] = reversed(puzzle[num*size:num*size+size])

    return tuple(puzzle)


RES_STATE = {'back_n_forth': back_n_forth}