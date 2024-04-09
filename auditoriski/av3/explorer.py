from searching_framework import Problem, breadth_first_graph_search

class Explorer(Problem):
    def __init__(self, person, house):
        super().__init__((person, (2, 4, -1), (5, 1, 1)))
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

if __name__ == '__main__':

    person = tuple(map(int, input().split()))
    house = tuple(map(int, input().split()))
    problem = Explorer(person, house)
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
    else:
        print("Nema Resenie")

"""
1 2
7 4
"""