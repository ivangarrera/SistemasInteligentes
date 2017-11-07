class Node:
    def __init__(self, state, cost, action, value, parent):
        self.__state = state
        self.__cost = cost
        self.__action = action
        self.__value = value
        self.__parent = parent

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
