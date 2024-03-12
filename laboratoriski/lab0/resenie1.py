from searching_framework import Problem, breadth_first_graph_search

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
        next_states = {}

        for action in self.possible_actions:
            next_state = self.generate_state(state, action)
            snake_head = next_state[0][0]

            if min(snake_head) < 0:
                continue

            if max(snake_head) >= self.size:
                continue

            if snake_head in red_apples:
                continue

            if snake_head in next_state[0][1:]:
                continue

            next_states[action] = next_state

        return next_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
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