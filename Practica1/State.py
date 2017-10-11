from copy import deepcopy
import Operations

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

    def __print_terrain(self):
        string = ""
        for i in range(len(self.terrain_representation)):
            for j in range(len(self.terrain_representation[i])):
                string += str(self.terrain_representation[i][j]) + " "
            string += "\n"
        print(string)

    def __is_possible_movement(self, movement):
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

    def __quantity_ground_to_transfer(self):
        ground_excess = int(self.terrain_representation[self.x_tractor][self.y_tractor]) - self.k
        if ground_excess < 0:
            ground_excess = 0
        return ground_excess

    def __get_all_movement_possibles(self):
        possibles = []
        for movement in movements:
            is_possible = self.__is_possible_movement(movement)
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

    def __is_valid_combination(self, combinations, num_possible_movements, ground_to_transfer):
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

    # Backtracking to get all the combinations
    def __get_combinations_of_ground(self, possible_movements, ground_to_transfer, num_possible_movements,
                                   current_combination, combinations, stage):
        if stage == num_possible_movements or ground_to_transfer == 0:
            if ground_to_transfer == 0:
                return
            copy = current_combination[:]  # Slicing to create a new object and no overwrite
            combinations.append(copy)
        else:
            for ground_value in range(ground_to_transfer + 1):
                current_combination.append((ground_value, possible_movements[stage]))
                if self.__is_valid_combination(current_combination, num_possible_movements,
                                             ground_to_transfer):
                    self.__get_combinations_of_ground(possible_movements, ground_to_transfer, num_possible_movements,
                                                    current_combination,
                                                    combinations, stage + 1)

                current_combination.pop()

    def __cartesian_prod_between_combinations_and_movements(self, possible_movements, combinations):
        cartesian = []
        if len(combinations) > 0:   # There is ground to transfer
            for movement in possible_movements:
                for combination in combinations:
                    cartesian.append((movement, combination))
        else:   # There isn't ground to transfer
            for movement in possible_movements:
                cartesian.append((movement, [0]))
        return cartesian

    def get_successors(self):
        current_combination = []
        combinations = []
        possible_movements = self.__get_all_movement_possibles()
        ground_to_transfer = self.__quantity_ground_to_transfer()
        self.__get_combinations_of_ground(possible_movements, ground_to_transfer, len(possible_movements),
                                        current_combination, combinations, 0)
        actions = self.__cartesian_prod_between_combinations_and_movements(possible_movements, combinations)
        suc = []
        cost = 1
        for action in actions:
            x_tractor, y_tractor = action[0]
            terrain = deepcopy(self.terrain_representation)
            # Make the movement
            for movement in action[1]:
                if movement != 0:
                    new_excess = movement[0]
                    new_x, new_y = movement[1]
                    # Update values
                    terrain[self.x_tractor][self.y_tractor] = self.k
                    terrain[new_x][new_y] = int(self.terrain_representation[new_x][new_y]) + new_excess
            s = State(self.rows, self.cols, x_tractor, y_tractor, self.k, self.max, terrain)
            suc.append((action, s, cost))
        return suc

    def get_successors_info(self, successors):
        print("Length of successors: {}".format(len(successors)))
        print("Original terrain: ")
        self.__print_terrain()
        for successor in successors:
            print("New Terrain: ")
            successor[1].__print_terrain()
            print("Applied action:\n{}\nWith a cost: {}".format(successor[0], successor[2]))


def main():
    operations = Operations.Operations()
    terrain = State(0, 0, 0, 0, 0, 0, 0)
    operations.read_file(terrain)
    successors = terrain.get_successors()
    terrain.get_successors_info(successors)
    operations.write_file(successors)
main()



