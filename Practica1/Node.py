class Node:
    def __init__(self, terrain, cost, action, value, parent):
        self.__terrain = terrain
        self.__cost = cost
        self.__action = action
        self.__value = value
        self.__parent = parent

    def get_terrain(self):
        return self.__terrain

    def get_cost(self):
        return self.__cost

    def get_action(self):
        return self.__action

    def get_value(self):
        return self.__value

    def get_parent(self):
        return self.__parent
