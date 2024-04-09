from searching_framework import Problem
from searching_framework import astar_search, greedy_best_first_graph_search, recursive_best_first_search

class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        next = {}
        ind = state.index('*')

        """
        * 1 2
        3 4 5
        6 7 8
        """

        if ind > 2:
            tmp = list(state)
            tmp[ind], tmp[ind-3] = tmp[ind-3], tmp[ind]
            tmp = ''.join(tmp)
            next["UP"] = tmp

        if ind < 6:
            tmp = list(state)
            tmp[ind], tmp[ind+3] = tmp[ind+3], tmp[ind]
            tmp = ''.join(tmp)
            next["DOWN"] = tmp

        if ind % 3 != 2:
            tmp = list(state)
            tmp[ind], tmp[ind+1] = tmp[ind+1], tmp[ind]
            tmp = ''.join(tmp)
            next["RIGHT"] = tmp

        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind-1] = tmp[ind-1], tmp[ind]
            tmp = ''.join(tmp)
            next["LEFT"] = tmp

        return next

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0

        for x, y in zip(node.state, self.goal):
            if x != y:
                counter += 1

        return counter


class Puzzle2(Puzzle):
    coordinates = {
        0: (0, 2), 1: (1, 2), 2: (2, 2),
        3: (0, 1), 4: (1, 1), 5: (2, 1),
        6: (0, 0), 7: (1, 0), 8: (2, 0)
    }

    @staticmethod
    def mhd(n, m):
        x1, y1 = Puzzle2.coordinates[n]
        x2, y2 = Puzzle2.coordinates[m]

        return abs(x1 - x2) + abs(y1 - y2)

    def h(self, node):
        sum_value = 0

        for x in '12345678':
            val = Puzzle2.mhd(node.state.index(x), int(x))
            sum_value += val

        return sum_value


if __name__ == "__main__":
    puzzle = Puzzle("*32415678", "*12345678")

    result1 = astar_search(puzzle)
    print(result1.solve())
    result2 = greedy_best_first_graph_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solution())

    puzzle2 = Puzzle2("*32415678", "*12345678")

    result4 = astar_search(puzzle2)
    print(result1.solve())
    result5 = greedy_best_first_graph_search(puzzle2)
    print(result2.solve())
    result6 = recursive_best_first_search(puzzle2)
    print(result3.solution())