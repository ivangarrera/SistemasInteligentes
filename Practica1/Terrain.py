class Terrain:
    def __init__(self, rows, cols, x_tractor, y_tractor, k, max):
        self.__cols = cols
        self.__rows = rows
        self.__x_tractor = x_tractor
        self.__y_tractor = y_tractor
        self.__k = k
        self.__max = max
        self.__terrain_representation = [[[] for i in range(self.__rows)] for i in range(self.__cols)]

    def generate_terrain(self):
        return self.__terrain_representation