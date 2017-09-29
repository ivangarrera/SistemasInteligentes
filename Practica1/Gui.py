import Terrain

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
                terrain_obj = Terrain.Terrain(row, col, tractor_x, tractor_y, k, max)
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
                string += terrain[i][j] + " "
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
        ground_excess = int(terrain[tractor_y][tractor_x]) - ground_desired_in_cell
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
        if len(combinations) > 0:
            for movement in possible_movements:
                for combination in combinations:
                    cartesian.append((movement, combination))
        else:
            for movement in possible_movements:
                cartesian.append((movement, 0))
        return cartesian

def main():
    gui = Gui()
    terrain, terrain_obj = gui.read_file()
    gui.print_terrain(terrain)

    possible = gui.get_all_movement_possibles(terrain, terrain_obj.get_xTractor(), terrain_obj.get_yTractor())
    current_combination = []
    combinations = []
    gui.get_combinations_of_ground(gui.quantity_ground_to_transfer(terrain, terrain_obj.get_xTractor(), terrain_obj.get_yTractor(),
                                                                   terrain_obj.get_GroundDesired()), len(possible),
                                   current_combination, combinations, 0)
    print(gui.cartesian_prod_between_combinations_and_movements(possible, combinations))

main()