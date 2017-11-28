import State
import Problem

class Node:
    def __init__(self, state, cost, action, value, parent, depth):
        self.__state = state
        self.__cost = cost
        self.__action = action
        self.__value = value
        self.__parent = parent
        self.__depth = depth

    def get_state(self):
        return self.__state

    def get_cost(self):
        return self.__cost

    def get_action(self):
        return self.__action

    def get_value(self):
        return self.__value

    def get_parent(self):
        return self.__parent

    def get_depth(self):
        return self.__depth

    def create_node(self, successor, actual_node, strategy, max_depth, prob):
        """

        :param successor: List with the next state, the action to get the next state and the cost
        :param actual_node: Node object which will be the parent of the new node
        :param strategy:  String. Search strategy, to calculate the node value
        :param max_depth:  Integer, necessary in DFS strategy to calculate the node value
        :param prob: Problem object
        :return:
            Node object
        """
        state = prob.initial_state()
        depth = actual_node.get_depth() + 1
        cost = actual_node.get_cost() + successor[2] # add the cost to arrive the successor

        if strategy == 'BFS':
            value = depth
        elif strategy == 'DFS' or strategy == 'IT':
            value = max_depth - depth
        elif strategy == 'UC':
            value = cost
        elif strategy == 'A*':
            value = state.h + cost

        return Node(successor[1], cost, successor[0], value, actual_node, depth)


