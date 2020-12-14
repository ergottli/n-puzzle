import math


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


def manhattan(puzzle, result_state, size):
	res = 0
	for i in range(size**2):
		if puzzle[i] != 0 and puzzle[i] != result_state[i]:
			result_state_index = result_state.index(puzzle[i])
			horizontal_shift = abs(math.ceil(i / size) - math.ceil(result_state_index / size))
			vertical_shift = abs((i + size * horizontal_shift) - result_state_index)
			res += horizontal_shift + vertical_shift
	return res


def result_state_matching(result_state, size):
	rc = dict()
	for i in range(size**2):
		# key - result_state element
		# value - [<element row>, <element column>, <element index>]
		rc[result_state[i]] = [int(math.floor(i / size)), int(math.floor(i % size)), i]
	return rc


def linear_conflict(puzzle, result_state, size):
	puzzle_matrix = [[puzzle[i + (j * size)] for i in range(size)] for j in range(size)]
	rc = result_state_matching(result_state, size)
	res = 0
	for row in range(size):
		for col in range(size - 1):
			if col + 1 < size:
				cur_res_state = rc[puzzle_matrix[row][col]]
				next_res_state = rc[puzzle_matrix[row][col+1]]
				if cur_res_state[0] == next_res_state[0] and cur_res_state[2] > next_res_state[2]:
					res += 2

	for col in range(size):
		for row in range(size - 1):
			if row + 1 < size:
				cur_res_state = rc[puzzle_matrix[row][col]]
				next_res_state = rc[puzzle_matrix[row+1][col]]
				if (cur_res_state[1] == next_res_state[1] and cur_res_state[2] > next_res_state[2]):
					res += 2
	return res


HEURISTICS = {'hamming': hamming_distance,'manhattan': manhattan, "linear_conflict": linear_conflict}