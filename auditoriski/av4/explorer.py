from searching_framework import Problem, astar_search

class Explorer(Problem):
    def __init__(self, person, house):
        super().__init__(person)
        self.sizeX = 8
        self.sizeY = 6
        self.house = house
        self.moves = {
            "Right": (1, 0),
            "Left": (-1, 0),
            "Down": (0, -1),
            "Up": (0, 1)
        }

    def successor(self, state):
        next = {}

        for move in self.moves.keys():
            next_state = []

            next_state.append(self.personMove(list(state[0]), move))
            next_state.append(self.boxMove(list(state[1])))
            next_state.append(self.boxMove(list(state[2])))

            if (next_state[0][0] < 0 or next_state[0][0] >= self.sizeX):
                continue
            if (next_state[0][1] < 0 or next_state[0][1] >= self.sizeY):
                continue

            if (next_state[0][0] == next_state[1][0] and next_state[0][1] == next_state[1][1]):
                continue
            if (next_state[0][0] == next_state[2][0] and next_state[0][1] == next_state[2][1]):
                continue

            next[move] = tuple(next_state)

        return next

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.house

    def personMove(self, person, move):
        tmp = self.moves.get(move, None)
        person[0] = person[0] + tmp[0]
        person[1] = person[1] + tmp[1]
        return tuple(person)

    def boxMove(self, box):
        # (2, 5, -1), (5, 0, 1)
        box[1] = box[1] + box[2]
        if (box[1] == 0 and box[2] == -1):
            box[2] = 1
        elif (box[1] == self.sizeY - 1 and box[2] == 1):
            box[2] = -1

        return tuple(box)

    def h(self, node):
        print(node.state)
        x1, y1 = node.state[0]
        x2, y2 = self.house

        return abs(x1 - x2) + abs(y1 - y2)
"""
1 2
7 4
"""


if __name__ == '__main__':
    init = (0, 2)
    goal = (7, 4)
    obstacle1 = (2, 5, -1)  # down
    obstacle2 = (5, 0, 1)  # up
    # (x,y,(o1x,o1y,o1d),(o2x,ob2y,o2d))
    explorer = Explorer(((init[0], init[1]), obstacle1,
                         obstacle2), goal)

    result = astar_search(explorer)
    print(result.solution())