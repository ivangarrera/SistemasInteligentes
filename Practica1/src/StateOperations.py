import hashlib
from copy import deepcopy
import State


class StateOperations:
    def __init__(self, terrain):
        self.terrain = terrain


    def __get_combinations_of_ground(self, possible_movements, ground_to_transfer, num_possible_movements,
                                     current_combination, combinations, stage):
        """

        This method do a Backtracking to get all the possible combinations of ground the tractor can do
        when it's in a cell to go to another cell.

        :param possible_movements:  List, with movements the tractor can do in a cell
        :param ground_to_transfer:  Integer, number of ground the tractor can move to other cells
        :param num_possible_movements: Integer, number of movements the tractor can do in a cell
        :param current_combination: List, with the current combination the algorithm is generating
        :param combinations: List, with all the possible combinations the tractor can do
        :param stage:  Integer. This value allows the algorithm to stop.
        :return:
            the param combinations
        """
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
        """
        This method calculates all the possible movements the tractor can do when it's in a cell
        to go to all the other cells it can go.

        :param possible_movements: List, with the cells where the tractor can move
        :param combinations:  List, with the combinations the tractor can do to go to other cell
        :return:
            List, with the cartesian product between the possible_movements List and the
            combinations List
        """
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
        """
        This method return the successor list for a state. The format is:
        [[ action, next_state, cost ], ... ]

        :return:
            List, with all the successors of a state.
        """

        # Calculates all the possible actions the tractor can do when it is in a cell.
        current_combination = []
        combinations = []
        possible_movements = self.terrain.get_all_movement_possibles()
        ground_to_transfer = self.terrain.quantity_ground_to_transfer()
        self.__get_combinations_of_ground(possible_movements, ground_to_transfer, len(possible_movements),
                                          current_combination, combinations, 0)
        actions = self.__cartesian_prod_between_combinations_and_movements(possible_movements, combinations)

        suc = []

        #  Create the successors list
        for action in actions: # actions = [( (x,y), [ground_transfer, (x2, y2)]), ...]
            x_tractor, y_tractor = action[0]
            terrain = deepcopy(self.terrain.terrain_representation) # this copy avoids not to overwrite the original state
            h = self.terrain.h
            # Make the movement
            unequal = False
            if terrain[self.terrain.x_tractor][self.terrain.y_tractor] != self.terrain.k:
                unequal = True
            for movement in action[1]: # movement = [ground_transfer, (x2, y2)]
                if movement != 0:
                    new_excess = movement[0]
                    new_x, new_y = movement[1]
                    # Update values
                    terrain[self.terrain.x_tractor][self.terrain.y_tractor] = terrain[self.terrain.x_tractor][self.terrain.y_tractor] - int(new_excess)
                    old_value = terrain[new_x][new_y]
                    terrain[new_x][new_y] = int(self.terrain.terrain_representation[new_x][new_y]) + int(new_excess)
                    new_value = terrain[new_x][new_y]
                    if old_value == self.terrain.k and new_value != self.terrain.k:
                        h += 1
                    elif old_value != self.terrain.k and new_value == self.terrain.k:
                        h -= 1
            if terrain[self.terrain.x_tractor][self.terrain.y_tractor] == self.terrain.k and unequal:
                h -= 1

            s = State.State(self.terrain.rows, self.terrain.cols, x_tractor, y_tractor, self.terrain.k,
                            self.terrain.max, h, terrain)
            suc.append((action, s, ground_to_transfer + 1))
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
        """

        :return:
            String whose value is a terrain unique identifier
        """
        return hashlib.sha512(str(self.terrain).encode()).hexdigest()



