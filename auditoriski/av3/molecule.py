from searching_framework import Problem, breadth_first_graph_search

class Molecule(Problem):
    def __init__(self, molecules):
        super().__init__(self.transformMolecule(molecules))
        self.moves = {
            "Right": (1, 0),
            "Left": (-1, 0),
            "Down": (0, 1),
            "Up": (0, -1)
        }
        self.matrix = (
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
            (1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1),
            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1),
            (1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        )

    def successor(self, state):
        next = {}

        for move in self.moves.keys():
            for ind in range(3):
                act_name = move + str(ind)

                next_state = list(state)

                atom = list(next_state[ind])
                if atom[0] < 0 or atom[0] >= len(self.matrix):
                    continue
                if atom[1] < 0 or atom[1] >= len(self.matrix[0]):
                    continue

                next_state[ind] = self.atomMove(atom, move, next_state, ind)

                if next_state == list(state):
                    continue

                next[act_name] = tuple(next_state)
                # print(act_name, next_state)

        return next

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # print(state)
        atom1, atom2, atom3 = state
        return atom1[0] + 1 == atom2[0] and atom2[0] + 1 == atom3[0] \
            and atom1[1] == atom2[1] and atom2[1] == atom3[1]

    def atomMove(self, atom, move, state, ind):
        tmp = self.moves.get(move, None) # 1 0
        # print("Atom", atom)
        # print("Matrix", self.matrix[atom[0]][atom[1]])
        if self.matrix[atom[0]][atom[1]] == 1:
            atom[0] -= tmp[0]
            atom[1] -= tmp[1]
        elif self.isValid(state, atom, ind):
            atom[0] -= tmp[0]
            atom[1] -= tmp[1]
        else:
            atom[0] += tmp[0]
            atom[1] += tmp[1]
            atom = self.atomMove(atom, move, state, ind)

        return tuple(atom)

    def transformMolecule(self, molecules):
        molecules = list(molecules)
        mol1 = list(molecules[0])
        mol2 = list(molecules[1])
        mol3 = list(molecules[2])

        mol1[0] += 1
        mol1[1] += 1
        mol2[0] += 1
        mol2[1] += 1
        mol3[0] += 1
        mol3[1] += 1

        return tuple(mol1), tuple(mol2), tuple(mol3)

    def isValid(self, state, atom, ind):
        for i in range(3):
            if ind != i:
                if state[i] == atom:
                    return True
        return False

""" example
2 6
7 2
2 1

2 1
7 2
2 6
"""
if __name__ == '__main__':
    atom_1 = tuple(map(int, input().split()))
    atom_2 = tuple(map(int, input().split()))
    atom_3 = tuple(map(int, input().split()))
    # i.e.:      atom_1,atom_2,atom_3 = \
    #   map( lambda _: map(int, input().split()), range(3) )

    problem = Molecule((atom_1, atom_2, atom_3))
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
        # actions, states = node.solution(), node.solve()
        # print(states[0])
        # for action, state1 in zip(actions, states[1:]):
        #     print(action, state1, sep="\n")
    else:
        print("Nema Resenie")

        # ['Down1', 'Down1', 'Down1', 'Right1', 'Right1', 'Right1', 'Right1', 'Up0', 'Up1', 'Up2', 'Right2']