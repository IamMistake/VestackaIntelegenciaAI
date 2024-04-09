from searching_framework import Problem, astar_search

class Farmer(Problem):
    def __init__(self):
        super().__init__(('w', 'w', 'w', 'w'), ('e', 'e', 'e', 'e'))

    def successor(self, state):
        successors = dict()

        if state[0] == 'w':
            for i in range(1, 4):
                next_state = list(state)
                if state[i] == 'w':
                    next_state[i] = 'e'
                    next_state[0] = 'e'

                if self.isValid(next_state):
                    continue

                name = "Farmerot_nosi_"
                if i == 1:
                    name += "Volk"
                elif i == 2:
                    name += "Jare"
                else:
                    name += "Zelka"

                successors[name] = tuple(next_state)
        else:
            name = "Farmerot_se_prefrla"
            next_state = list(state)
            next_state[0] = 'w'
            successors[name] = tuple(next_state)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        for i in range(0,4):
            if node.state[i] != self.goal[i]:
                counter += 1

        return counter

    def isValid(self, next_state):
        if next_state[1] == 'w' and next_state[2] == 'w':
            return True
        elif next_state[2] == 'w' and next_state[3] == 'w':
            return True
        else:
            return False

if __name__ == '__main__':
    farmer = Farmer()

    result = astar_search(farmer)
    print(result.solution())