from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial_state, n_size, kutii):
        leans = [0 for _ in range(len(kutii))]
        super().__init__((initial_state[0], tuple(leans)))
        self.grid_size = n_size
        self.kutii = kutii
        self.moves = {
            "Gore": (0, 1),
            "Desno": (1, 0)
        }

    def successor(self, state):
        successors = {}

        coek = list(state[0])
        leans = list(state[1])
        for key in self.moves.keys():
            move = self.moves[key]
            new_coek = (coek[0] + move[0], coek[1] + move[1])
            if new_coek[0] not in range(self.grid_size) or new_coek[1] not in range(self.grid_size):
                continue
            if new_coek in self.kutii:
                continue
            new_coek = tuple(new_coek)

            sosedi = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1))
            for sosed in sosedi:
                tmp_sosed = (new_coek[0] + sosed[0], new_coek[1] + sosed[1])
                if tmp_sosed in self.kutii:
                    ind = self.kutii.index(tmp_sosed)
                    leans[ind] = 1

            successors[key] = (new_coek, tuple(leans))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for i in state[1]:
            if i == 0:
                return False
        return True
        # return state[1] == 0

"""
6
3
3,4
4,2
5,2
"""

if __name__ == '__main__':
    n = int(input())
    man_pos = [0, 0]
    n_boxes = int(input())
    boxes = list()
    for i in range(n_boxes):
        x, y = tuple(map(int, input().split(",")))
        boxes.append((x, y))

    sosedi = dict()
    for box in boxes:
        x = box[0]
        y = box[1]
        lista = list()
        lista.append((x - 1, y - 1))# dolu levo
        lista.append((x - 1, y))    # levo
        lista.append((x - 1, y + 1))# gore levo
        lista.append((x, y - 1))    # dolu
        lista.append((x, y + 1))    # gore
        lista.append((x + 1, y - 1))# desno dolu
        lista.append((x + 1, y))    # desno
        lista.append((x + 1, y + 1))# desno gore
        sosedi[box] = lista

    initial = (tuple(man_pos), n_boxes)

    kutija = Boxes(initial, n, boxes)
    result = breadth_first_graph_search(kutija)
    if result:
        print(result.solution())
    else:
        print("No Solution!")