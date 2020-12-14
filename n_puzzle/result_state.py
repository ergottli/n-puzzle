def back_n_forth(puzzle, size):
    puzzle = sorted(puzzle)
    for num in range(size):
        if num % 2 == 1:
            puzzle[num*size:num*size+size] = reversed(puzzle[num*size:num*size+size])

    return tuple(puzzle)


def zero_first_state(puzzle, size):
    puzzle = list(puzzle)
    for i in range(size*size):
        puzzle[i] = i
    return tuple(puzzle)


def zero_last_state(puzzle, size):
    puzzle = list(puzzle)
    for i in range(size*size - 1):
        puzzle[i] = i + 1
    puzzle[-1] = 0
    return tuple(puzzle)


def spiral_state(puzzle, size):
    ans = [0 for _ in range(size**2)]
    seen = [False for _ in range(size**2)]
    angle_r = [0, 1, 0, -1]
    angle_c = [1, 0, -1, 0]
    counter = 1
    r = c = angle_i = 0
    for _ in range(size**2):
        ans[r * size + c] = counter
        seen[r * size + c] = True
        cr, cc = r + angle_r[angle_i], c + angle_c[angle_i]
        if 0 <= cr < size and 0 <= cc < size and not seen[cr * size + cc]:
            r, c = cr, cc
        else:
            angle_i = (angle_i + 1) % 4
            r, c = r + angle_r[angle_i], c + angle_c[angle_i]
        counter = (counter + 1) % (size**2)
    return tuple(ans)


RES_STATE = {'back_n_forth': back_n_forth, 'snail': spiral_state, 'zero_first': zero_first_state,
             'zero_last': zero_last_state}
