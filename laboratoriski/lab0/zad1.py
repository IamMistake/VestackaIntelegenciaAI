# from searching_framework import # what do you need to solve this problem?
from searching_framework import Problem, breadth_first_graph_search

"""
5
6,9
2,7
9,5
2,3
4,3
4
4,6
6,5
3,3
6,8
"""

class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples
        self.size = 10
        self.possible_actions = (
            'ProdolzhiPravo',
            'SvrtiLevo',
            'SvrtiDesno'
        )
        self.directions = {
            'ProdolzhiPravo': 0,
            'SvrtiDesno': 1,
            'SvrtiLevo': -1
        }
        self.moves = (
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        )


    def successor(self, state):
        next = {}

        for action in self.possible_actions:
            next_state = self.generate_state(state, action)
            snake_head = next_state[0][0]

            if min(snake_head) < 0:
                continue

            if max(snake_head) >= self.size:
                continue

            if snake_head in self.red_apples:
                continue

            if snake_head in next_state[0][1:]:
                continue

            next[action] = next_state

        return next

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return len(state[2]) == 0

    def generate_state(self, state, action):
        direction = (state[1] + self.directions[action]) % 4
        move = self.moves[direction]
        snake_head = (state[0][0][0] + move[0], state[0][0][1] + move[1])
        snake_segments = list(state[0])
        apples = list(state[2])

        snake_segments.insert(0, snake_head)

        if snake_head in apples:
            apples.remove(snake_head)
        else:
            snake_segments.pop()

        return tuple(snake_segments), direction, tuple(apples)

if __name__ == '__main__':
    num_green_apples = int(input())
    green_apples_input = [tuple(map(int, input().split(',')))
                          for _ in range(num_green_apples)]
    green_apples = tuple((i, 9 - j) for i, j in green_apples_input)
    num_red_apples = int(input())
    red_apples_input = [tuple(map(int, input().split(',')))
                        for _ in range(num_red_apples)]
    red_apples = tuple((i, 9 - j) for i, j in red_apples_input)
    snake_segments = ((0, 2), (0, 1), (0, 0))
    initial_state = (snake_segments, 2, green_apples)

    game = Snake(initial_state, red_apples)
    solution = breadth_first_graph_search(game)
    print(solution.solution())