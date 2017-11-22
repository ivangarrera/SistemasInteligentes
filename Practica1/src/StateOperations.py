import hashlib
from copy import deepcopy
import State


class StateOperations:
    def __init__(self, terrain):
        self.terrain = terrain

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
                if self.terrain.is_valid_combination(current_combination, num_possible_movements,
                                               ground_to_transfer):
                    self.__get_combinations_of_ground(possible_movements, ground_to_transfer, num_possible_movements,
                                                      current_combination,
                                                      combinations, stage + 1)

                current_combination.pop()

    def __cartesian_prod_between_combinations_and_movements(self, possible_movements, combinations):
        cartesian = []
        if len(combinations) > 0:  # There is ground to transfer
            for movement in possible_movements:
                for combination in combinations:
                    cartesian.append((movement, combination))
        else:  # There isn't ground to transfer
            for movement in possible_movements:
                cartesian.append((movement, [0]))
        return cartesian

    def get_successors(self):
        current_combination = []
        combinations = []
        possible_movements = self.terrain.get_all_movement_possibles()
        ground_to_transfer = self.terrain.quantity_ground_to_transfer()
        self.__get_combinations_of_ground(possible_movements, ground_to_transfer, len(possible_movements),
                                          current_combination, combinations, 0)
        actions = self.__cartesian_prod_between_combinations_and_movements(possible_movements, combinations)
        suc = []
        cost = ground_to_transfer+1
        for action in actions:
            x_tractor, y_tractor = action[0]
            terrain = deepcopy(self.terrain.terrain_representation)
            h = self.terrain.h
            # Make the movement
            desigual = False
            if (terrain[self.terrain.x_tractor][self.terrain.y_tractor] != self.terrain.k):
                desigual = True
            for movement in action[1]:
                if movement != 0:
                    new_excess = movement[0]
                    new_x, new_y = movement[1]
                    # Update values
                    terrain[self.terrain.x_tractor][self.terrain.y_tractor] = terrain[self.terrain.x_tractor][self.terrain.y_tractor] - int(new_excess)
                    old_value = terrain[new_x][new_y]
                    terrain[new_x][new_y] = int(self.terrain.terrain_representation[new_x][new_y]) + int(new_excess)
                    new_value = terrain[new_x][new_y]
                    if(old_value == self.terrain.k and new_value != self.terrain.k):
                        h= h + 1
                    elif(old_value != self.terrain.k and new_value == self.terrain.k):
                        h = h - 1
            if (terrain[self.terrain.x_tractor][self.terrain.y_tractor] == self.terrain.k and desigual):
                h = h - 1
            s = State.State(self.terrain.rows, self.terrain.cols, x_tractor, y_tractor, self.terrain.k, self.terrain.max, h, terrain)
            suc.append((action, s, cost))
        return suc

    def get_successors_info(self, successors):
        print("Length of successors: {}".format(len(successors)))
        print("Original terrain: ")
        self.terrain.print_terrain()
        for successor in successors:
            print("New Terrain: ")
            successor[1].print_terrain()
            print("Applied action:\n{}\nWith a cost: {}".format(successor[0], successor[2]))

    def get_unique_representation(self):
        return hashlib.sha512(str(self.terrain).encode()).hexdigest()

    def check_h(self, state):
        h = 0
        for i in range(int(state.rows)):
            for j in range(int(state.cols)):
                if state.terrain_representation[i][j] != state.k:
                    h = h + 1
        return h


