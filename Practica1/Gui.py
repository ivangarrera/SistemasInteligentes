import Terrain
import random

movements = ["UP", "DOWN", "RIGHT", "LEFT"]

class Gui:
    def __init__(self):
        self.__initiated = True

    def read_file(self):
        try:
            with open("./terrain.txt") as f:
                file = f.read().splitlines()
                # Read configuration controls
                config = file[0].split(" ")
                tractor_x, tractor_y, k, maximum, col, row = config[0], config[1], config[2], config[3], config[4], config[5]
                # Create the terrain
                terrain_obj = Terrain.Terrain(row, col, tractor_x, tractor_y, k, maximum)
                terrain = terrain_obj.generate_terrain()
                # Fill the terrain with values
                for i in range(int(row)):
                    row_values = file[i+1].split(" ")
                    terrain[i] = row_values

            return terrain, terrain_obj

        except Exception as ex:
            print(ex.__str__())

    def print_terrain(self, terrain):
        string = ""
        for i in range(len(terrain)):
            for j in range(len(terrain[i])):
                string += str(terrain[i][j]) + " "
            string += "\n"
        print(string)

    """
    Coordinate system chosen
            y
            ^
            |
            |
            |---------> x
    """
    def is_possible_movement(self, terrain, tractor_x, tractor_y, movement):
        possible = False
        if movement == 'RIGHT':
            possible = tractor_x + 1 < len(terrain)
        elif movement == 'LEFT':
            possible = tractor_x - 1 >= 0
        elif movement == 'UP':
            possible = tractor_y - 1 >= 0
        elif movement == 'DOWN':
            possible = tractor_y + 1 < len(terrain[0])
        return possible

    def quantity_ground_to_transfer(self, terrain, tractor_x, tractor_y, ground_desired_in_cell):
        ground_excess = int(terrain[tractor_x][tractor_y]) - ground_desired_in_cell
        if ground_excess < 0:
            ground_excess = 0
        return ground_excess

    def get_all_movement_possibles(self, terrain, tractor_x, tractor_y):
        possibles = []
        for movement in movements:
            is_possible = self.is_possible_movement(terrain, tractor_x, tractor_y, movement)
            if is_possible:
                if movement == 'RIGHT':
                    possibles.append((tractor_x + 1, tractor_y))
                elif movement == 'LEFT':
                    possibles.append((tractor_x - 1, tractor_y))
                elif movement == 'UP':
                    possibles.append((tractor_x, tractor_y - 1))
                elif movement == 'DOWN':
                    possibles.append((tractor_x, tractor_y + 1))
        return possibles

    def is_valid_combination(self, combinations, ground_value, num_possible_movements, ground_to_transfer):
        sum = 0
        for value in range(len(combinations)):
            sum += combinations[value]
        if len(combinations) == num_possible_movements:
            if sum != ground_to_transfer:
                return False
            else:
                return True
        if sum <= ground_to_transfer:
            return True
        return False

    # Backtracking to get all the combinations
    def get_combinations_of_ground(self, ground_to_transfer, num_possible_movements, current_combination, combinations, stage):
        if stage == num_possible_movements or ground_to_transfer == 0:
            if ground_to_transfer == 0:
                return
            copy = current_combination[:]  # Slicing to create a new object and no overwrite
            combinations.append(copy)
        else:
            for ground_value in range(ground_to_transfer + 1):
                current_combination.append(ground_value)
                if self.is_valid_combination(current_combination, ground_value, num_possible_movements, ground_to_transfer):
                    self.get_combinations_of_ground(ground_to_transfer, num_possible_movements, current_combination,
                                                    combinations, stage + 1)
                current_combination.pop()

    def cartesian_prod_between_combinations_and_movements(self, possible_movements, combinations):
        cartesian = []
        if len(combinations) > 0:   # There is ground to transfer
            for movement in possible_movements:
                for combination in combinations:
                    cartesian.append((movement, combination))
        else:   # There isn't ground to transfer
            for movement in possible_movements:
                cartesian.append((movement, [0]))
        return cartesian

    def choose_one_action(self, possible_actions):
        index = random.randint(0, len(possible_actions) - 1)
        return possible_actions[index]

    def algorithm_is_applicable(self, terrain, ground_desired):
        applicable = False
        for row in terrain:
            for square in row:
                if square != ground_desired:
                    applicable = True
        return applicable

    def algorithm(self, terrain, terrain_obj):
        ground_desired = terrain_obj.get_GroundDesired()
        solving_steps = []
        # If the ground is not equal in all squares.
        while self.algorithm_is_applicable(terrain, ground_desired):

            x_tractor = terrain_obj.get_xTractor()
            y_tractor = terrain_obj.get_yTractor()
            self.print_terrain(terrain)
            print("Tractor is in {}".format((x_tractor, y_tractor)))
            current_combination = []
            combinations = []
            step = ""

            # Get all possible actions the tractor can do
            possible_movements = self.get_all_movement_possibles(terrain, x_tractor, y_tractor)
            ground_to_transfer = self.quantity_ground_to_transfer(terrain, x_tractor, y_tractor, ground_desired)
            self.get_combinations_of_ground(ground_to_transfer, len(possible_movements), current_combination, combinations, 0)
            possible_actions = self.cartesian_prod_between_combinations_and_movements(possible_movements, combinations)

            # Choose a random option and do it
            action_to_do = self.choose_one_action(possible_actions)
            new_position, ground_combination = action_to_do[0], action_to_do[1]
            print("Tractor will move to: {}\nGround combination is:".format(new_position, ground_combination))
            step += "{}, [".format(new_position)

            if len(possible_movements) == len(ground_combination):
                # Move the tractor to its new position
                terrain_obj.set_xTractor(new_position[0])
                terrain_obj.set_yTractor(new_position[1])
                # Update values of ground in the terrain
                for index in range(len(ground_combination)):
                    x_new, y_new = possible_movements[index][0], possible_movements[index][1]
                    print("{}->{}".format((x_new, y_new), ground_combination[index]))
                    step += "({}, {}), ".format(ground_combination[index], (x_new, y_new))
                    terrain[x_tractor][y_tractor] = ground_desired
                    terrain[x_new][y_new] = int(terrain[x_new][y_new]) + ground_combination[index]
                print("\n\n\n")
                step += "]"
            else: # There isn't ground to transfer
                print("{}->{}\n\n\n".format((new_position[0], new_position[1]), ground_to_transfer))
                step += "({}, {})]".format(ground_to_transfer, (new_position[0], new_position[1]))
                terrain_obj.set_xTractor(new_position[0])
                terrain_obj.set_yTractor(new_position[1])
            solving_steps.append(step)
        # Print the terrain final state
        self.print_terrain(terrain)
        return solving_steps

def main():
    gui = Gui()
    terrain, terrain_obj = gui.read_file()
    solving_steps = gui.algorithm(terrain, terrain_obj)
    try:
        with open("./solution.txt", 'w') as f:
            for step in solving_steps:
                f.write(step+"\n")
    except Exception as ex:
        print(ex.__str__())

main()