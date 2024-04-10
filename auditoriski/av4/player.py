from searching_framework import Problem, astar_search


class Player(Problem):
    def __init__(self, initial):
        super().__init__(initial)

    def successor(self, state):
        successors = dict()

        person = state[0]
        lista = list(state[2][person][1])
        for rebro in lista:
            tmp = list(state[1])
            if rebro in tmp:
                tmp.remove(rebro)

            # (6, (2, 5, 7, 10, 11)),
            newGraf = list(state[2])

            personTuple = list(newGraf[person])
            tmpList = list(personTuple[1])
            tmpList.remove(rebro)
            personTuple[1] = tuple(tmpList)

            rebroTuple = list(newGraf[rebro])
            tmp1List = list(rebroTuple[1])
            tmp1List.remove(person)
            rebroTuple[1] = tuple(tmp1List)

            newGraf[person] = tuple(personTuple)
            newGraf[rebro] = tuple(rebroTuple)

            next_state = (rebro, tuple(tmp), tuple(newGraf))

            name = str(person) + "_TO_" + str(rebro)
            successors[name] = next_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

    def h(self, node):
        counter = 0

        graf = node.state[2]
        for rebro in graf[node.state[0]][1]:
            if rebro not in node.state[1]:
                counter += 1

        return counter

"""
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

if __name__ == '__main__':
    graf = (
        (0, (0, 0)),
        (1, (2, 5)),
        (2, (1, 6)),
        (3, (4, 7)),
        (4, (3, 8)),
        (5, (1, 6)),
        (6, (2, 5, 7, 10, 11)),
        (7, (3, 6, 8, 11)),
        (8, (4, 7)),
        (9, (10, 13)),
        (10, (6, 9, 11, 14)),
        (11, (6, 7, 10, 12, 15)),
        (12, (11, 16)),
        (13, (9, 14)),
        (14, (10, 13)),
        (15, (11, 16)),
        (16, (12, 15))
    )

    # CHOOSE START 6 7 10 11
    player = 6
    # CHOOSE COINS
    coins = (1, 16)

    send = (player, coins, graf)

    problem = Player(send)
    result = astar_search(problem)
    print(result.solution())
