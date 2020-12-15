from queue import PriorityQueue
from result_state import RES_STATE
from heuristics import HEURISTICS, uniform_cost, heuristic_decorator


class PuzzleSolver:

    def __init__(self, args, puzzle, size):
        self.args = args
        self.puzzle = puzzle
        self.size = size
        self.step_cost = 1
        self.result_state = RES_STATE[args.s](puzzle, size)
        self.result = 0
        if args.g:
            self.step_cost = 0
        if args.u:
            self.heuristic_func = heuristic_decorator(uniform_cost, self.result_state, self.size)
        else:
            self.heuristic_func = heuristic_decorator(HEURISTICS[args.f], self.result_state, self.size)

    def _create_new_state(self, puzzle, zero_index, move):
        elem = puzzle[move]
        new = list(puzzle)
        new[zero_index] = elem
        new[move] = 0
        return tuple(new)

    def possible_moves(self, puzzle):
    
        zero_index = puzzle.index(0)
        res = []
    
        if zero_index - self.size >= 0:
            new_state = self._create_new_state(puzzle, zero_index, zero_index - self.size)
            res.append(new_state)
    
        if zero_index + self.size < self.size**2:
            new_state = self._create_new_state(puzzle, zero_index, zero_index + self.size)
            res.append(new_state)
    
        if zero_index % self.size + 1 < self.size:
            new_state = self._create_new_state(puzzle, zero_index, zero_index + 1)
            res.append(new_state)
    
        if zero_index % self.size > 0:
            new_state = self._create_new_state(puzzle, zero_index, zero_index - 1)
            res.append(new_state)
    
        return res

    def _is_even_puzzle(self, puzzle, odd_start_correction):
        incorrect_pairs = odd_start_correction
        for i in range(len(puzzle)):
            for e in range(i+1, len(puzzle)):
                if puzzle[i] > puzzle[e]:
                    incorrect_pairs += 1
        return incorrect_pairs % 2 == 0

    def is_solvable(self):
        odd_start_correction = 0
        # Если длина стороны четна, добавляем к сумме инверсий стартовой комбинации номер строки с пустой ячейкой.
        if self.size % 2 == 0:
            odd_start_correction = (self.puzzle.index(0) + 1) // self.size
        #  Копируем значения стартовой и финальной комбинации, приводим к типу списка.
        start_state = list(self.puzzle)
        finish_state = list(self.result_state)
        #  Удаляем пустые ячейки. (В подсчете суммы инверсий они не участвуют).
        start_state.remove(0)
        finish_state.remove(0)
        #  Сравниваем четность инверсий стартовой и финальной комбинации.
        return self._is_even_puzzle(start_state, odd_start_correction) == self._is_even_puzzle(finish_state, 0)

    def solve_npuzzle(self):
        # Проверка на решаемость пазла.
        if not self.is_solvable():
            return False
        queue = PriorityQueue()  # Очередь с приоритетом из которой мы забираем следующую комбинацию.
        open_set = {}  # Словарь со всеми открытыми комбинациями. open_set[combination]=[g(n),h(n)].
        close_set = {}  # Словарь со всеми пройденными комбинациями. close_set[combination]=parent.

        # g(n) + h(n), g(n), current_combination, parent
        queue.put((0 + self.heuristic_func(self.puzzle), 0, self.puzzle, None))

        while not queue.empty():

            _, current_g, current_combination, parent = queue.get()

            if current_combination in close_set:
                continue

            if current_combination == self.result_state:
                path = [current_combination]
                # Восстанавливаем последовательность комбинаций от текущей до начальной.
                while parent:
                    path.append(parent)
                    parent = close_set[parent]
                # Разворачиваем последовательность, чтобы первым элементом была начальная комбинация.
                path.reverse()
                # Последовательность комбинаций, complexity in time, complexity in size.
                self.result = [path, len(open_set), len(close_set)]
                return

            close_set[current_combination] = parent
            # Устанавливаем g(n) для следующего шага.
            next_g = current_g + self.step_cost

            # Получаем все возможные комбинации, которые можно получить из текущей.
            steps = self.possible_moves(current_combination)

            for step in steps:
                if step in close_set:
                    continue
                if step in open_set:
                    prev_g, h = open_set[step]
                    if prev_g <= next_g:
                        continue
                else:
                    h = self.heuristic_func(step)
                open_set[step] = next_g, h
                # g(n) + h(n), g(n), current_combination, parent
                queue.put((next_g + h, next_g, step, current_combination))

        self.result = False
        return

    def print_result(self):
        if not self.result:
            print("Puzzle not solvable!")
            return
        if self.result == 0:
            print("There is no puzzle!")

        path, space, time = self.result
        if self.args.p:
            self._pretty_print(path)
        else:
            for step in path:
                print(step)
        print(f"Space complexity = {space}\nTime complexity = {time}\nSteps = {len(path) - 1}")

    def _pretty_print(self, path):
        for ind in range(len(path)):
            print(" " + "-" * (self.size * 2 + 1))
            i = 0
            while i < self.size ** 2:
                print("|", " ".join(map(str, path[ind][i:i + self.size])), "|")
                i = i + self.size
            print(" " + "-" * (self.size * 2 + 1))
            if ind + 1 != len(path):
                print(" " * self.size, "|", " " * self.size)
                print(" " * self.size, "v", " " * self.size)
            else:
                print()
