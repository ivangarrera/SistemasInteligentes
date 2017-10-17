class Nodo:
    def __init__(self, terrain, cost, action, value):
        self.__terrain = terrain
        self.__cost = cost
        self.__action = action
        self.__value = value

    def get_terrain(self):
        return self.__terrain

    def get_cost(self):
        return self.__cost

    def get_action(self):
        return self.__action

    def get_value(self):
        return self.__value