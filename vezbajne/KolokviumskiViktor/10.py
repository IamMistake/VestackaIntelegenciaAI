import bisect

"""
Defining a class for the problem structure that we will solve with a search.
The Problem class is an abstract class from which we make inheritance to define the basic
characteristics of every problem we want to solve
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """Given a state, return a dictionary of {action : state} pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once.

        :param state: given state
        :return:  dictionary of {action : state} pairs reachable
                  from this state
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """Given a state, return a list of all actions possible
        from that state

        :param state: given state
        :return: list of actions
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """Given a state and action, return the resulting state

        :param state: given state
        :param action: given action
        :return: resulting state
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares
        the state to self.goal, as specified in the constructor. Implement
        this method if checking against a single self.goal is not enough.

        :param state: given state
        :return: is the given state a goal state
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from state1
        via action, assuming cost c to get up to state1. If the problem is such
        that the path doesn't matter, this function will only look at state2.
        If the path does matter, it will consider c and maybe state1 and action.
        The default method costs 1 for every step in the path.

        :param c: cost of the path to get up to state1
        :param state1: given current state
        :param action: action that needs to be done
        :param state2: state to arrive to
        :return: cost of the path after executing the action
        :rtype: float
        """
        return c + 1

    def value(self):
        """For optimization problems, each state has a value.
        Hill-climbing and related algorithms try to maximize this value.

        :return: state value
        :rtype: float
        """
        raise NotImplementedError


"""
Definition of the class for node structure of the search.
The class Node is not inherited
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create node from the search tree,  obtained from the parent by
        taking the action

        :param state: current state
        :param parent: parent state
        :param action: action
        :param path_cost: path cost
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node.

        :param problem: given problem
        :return: list of available nodes in one step
        :rtype: list(Node)
        """
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Return a child node from this node

        :param problem: given problem
        :param action: given action
        :return: available node  according to the given action
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Return the sequence of actions to go from the root to this node.

        :return: sequence of actions
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Return the sequence of states to go from the root to this node.

        :return: list of states
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node.

        :return: list of states from the path
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """We want the queue of nodes at breadth_first_search or
    astar_search to not contain states-duplicates, so the nodes that
    contain the same condition we treat as the same. [Problem: this can
    not be desirable in other situations.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Definitions of helper structures for storing the list of generated, but not checked nodes
"""


class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): Last In First Out Queue (stack).
        FIFOQueue(): First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Adds the item into the queue

        :param item: given element
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Adds the items into the queue

        :param items: given elements
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Returns the first element of the queue

        :return: first element
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the number of elements in the queue

        :return: number of elements in the queue
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Check if the queue contains the element item

        :param item: given element
        :return: whether the queue contains the item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element is returned first
     (as determined by f and order). This structure is used in
     informed search"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: sorting function, if order is min, returns the element
                      with minimal f (x); if the order is max, then returns the
                      element with maximum f (x).
        :param f: function f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


"""
Uninformed graph search
The main difference is that here we do not allow loops,
i.e. repetition of states
"""


def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
     If two paths reach a state, only use the best one.

    :param problem: given problem
    :param fringe: empty queue
    :return: Node
    """
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first.

    :param problem: given problem
    :return: Node
    """
    return graph_search(problem, FIFOQueue())

class Snake(Problem):
    board_size = (9, 9)

    def __init__(self, red_apples, green_apples):
        self.red_apples = tuple(red_apples)
        self.green_apples = tuple(green_apples)
        green_apples_booleans = tuple([1 for apple in green_apples])
        body_positions = [(0, 7), (0, 8), (0, 9)]

        # 1 = right, 2 = top, 3 = left, 4 = bottom
        direction = 4
        initial = (tuple(body_positions), direction, green_apples_booleans)
        # print(initial)

        super().__init__(initial)

    def goal_test(self, state):
        return sum(state[2]) == 0

    def determine_move_from_direction(self, direction):

        if direction == 1:
            return 1, 0
        elif direction == 2:
            return 0, 1
        elif direction == 3:
            return -1, 0
        else:
            return 0, -1

    def determine_next_direction(self, where, previous):

        if where == "pravo":
            return previous

        if where == "desno":
            if previous == 1:
                return 4
            if previous == 2:
                return 1
            if previous == 3:
                return 2
            if previous == 4:
                return 3

        if where == "levo":
            if previous == 1:
                return 2
            if previous == 2:
                return 3
            if previous == 3:
                return 4
            if previous == 4:
                return 1

    def move_and_grow(self, snake_body_position, next_head_position, new_state):

        add_part = False
        if next_head_position in self.green_apples:
            index_of_green_apple = self.green_apples.index(next_head_position)
            if new_state[2][index_of_green_apple] == 1:
                add_part = True
                apple_booleans = list(new_state[2])
                apple_booleans[index_of_green_apple] = 0
                new_state[2] = tuple(apple_booleans)

        snake_body_position.insert(0, next_head_position)

        if not add_part:
            snake_body_position = snake_body_position[:-1]

        new_state[0] = tuple(snake_body_position)

        return new_state

    def is_state_valid(self, new_state):
        snake_body_position = new_state[0]
        head_position = snake_body_position[0]

        if head_position in self.red_apples:
            return False

        if head_position in snake_body_position[1:]:
            return False

        return True

    def fast_check(self, head_position):
        if head_position is None:
            return False

        if head_position[0] < 0 or head_position[1] < 0:
            return False

        if head_position[0] > Snake.board_size[0] or head_position[1] > Snake.board_size[1]:
            return False

        return True

    def move_snake(self, state, where):

        new_state = list(state)
        new_direction = self.determine_next_direction(where, state[1])
        new_state[1] = new_direction

        # print("New state is", new_state)
        snake_body_position = new_state[0]
        next_move = self.determine_move_from_direction(new_direction)

        if snake_body_position[0] is None:
            return None

        next_head_position = snake_body_position[0][0] + next_move[0], snake_body_position[0][1] + next_move[1]

        if not self.fast_check(next_head_position):
            return None

        new_state = self.move_and_grow(list(snake_body_position), next_head_position, new_state)

        if not self.is_state_valid(new_state):
            return None

        return tuple(new_state)

    def successor(self, state):

        successors_states = dict()

        new_state = self.move_snake(state, "pravo")
        if new_state:
            successors_states["ProdolzhiPravo"] = new_state

        new_state = self.move_snake(state, "levo")
        if new_state:
            successors_states["SvrtiLevo"] = new_state

        new_state = self.move_snake(state, "desno")
        if new_state:
            successors_states["SvrtiDesno"] = new_state

        return successors_states

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    red_apples = []
    green_apples = []
    num_red_apples = int(input())
    for i in range(num_red_apples):
        red_apple = tuple(map(int, input().split(",")))
        red_apples.append(red_apple)

    num_green_apples = int(input())

    for i in range(num_green_apples):
        green_apple = tuple(map(int, input().split(",")))
        green_apples.append(green_apple)

    snake_problem = Snake(green_apples, red_apples)
    search = breadth_first_graph_search(snake_problem)
    # print(search)
    if search:
        print(search.solution())