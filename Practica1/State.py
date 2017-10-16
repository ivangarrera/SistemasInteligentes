
movements = ["UP", "DOWN", "RIGHT", "LEFT"]

class State:

    """
        Coordinate system chosen
                y
                ^
                |
                |
                |---------> x
        """

    def __init__(self, rows, cols, x_tractor, y_tractor, k, max, terrain_representation = 0):
        self.cols = cols
        self.rows = rows
        self.x_tractor = x_tractor
        self.y_tractor = y_tractor
        self.k = k
        self.max = max
        if terrain_representation != 0:
            self.terrain_representation = terrain_representation

    def print_terrain(self):
        string = ""
        for i in range(len(self.terrain_representation)):
            for j in range(len(self.terrain_representation[i])):
                string += str(self.terrain_representation[i][j]) + " "
            string += "\n"
        print(string)

    def is_possible_movement(self, movement):
        possible = False
        if movement == 'RIGHT':
            possible = self.x_tractor + 1 < len(self.terrain_representation)
        elif movement == 'LEFT':
            possible = self.x_tractor - 1 >= 0
        elif movement == 'UP':
            possible = self.y_tractor - 1 >= 0
        elif movement == 'DOWN':
            possible = self.y_tractor + 1 < len(self.terrain_representation[0])
        return possible

    def quantity_ground_to_transfer(self):
        ground_excess = int(self.terrain_representation[self.x_tractor][self.y_tractor]) - self.k
        if ground_excess < 0:
            ground_excess = 0
        return ground_excess

    def get_all_movement_possibles(self):
        possibles = []
        for movement in movements:
            is_possible = self.is_possible_movement(movement)
            if is_possible:
                if movement == 'RIGHT':
                    possibles.append((self.x_tractor + 1, self.y_tractor))
                elif movement == 'LEFT':
                    possibles.append((self.x_tractor - 1, self.y_tractor))
                elif movement == 'UP':
                    possibles.append((self.x_tractor, self.y_tractor - 1))
                elif movement == 'DOWN':
                    possibles.append((self.x_tractor, self.y_tractor + 1))
        return possibles

    def is_valid_combination(self, combinations, num_possible_movements, ground_to_transfer):
        sum = 0
        for value in range(len(combinations)):
            sum += combinations[value][0]
        if len(combinations) == num_possible_movements and sum < self.max:
            for combination in combinations: # The ground mustn't be greater than maximum
                if int(self.terrain_representation[combination[1][0]][combination[1][1]]) + \
                        combination[0] > self.max \
                        and combination[0] != 0:
                    return False
            if sum != ground_to_transfer:
                return False
            else:
                return True
        if sum <= ground_to_transfer:
            return True
        return False





