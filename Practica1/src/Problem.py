import random
import State
import StateOperations

class Problem:

    def __init__(self, increase, depth_max, path, state):
        self.increase = increase
        self.depth_max = depth_max
        self.path = path
        self.state = state
        self.spaceState = StateOperations.StateOperations(self.state)

    def file_format_correct(self):
        """
        This method check if the format of the text file to load the program data, is correct.

        :return:
            True if the text file to load the program data is correct, False otherwise.
        """
        correct = True
        try:
            with open(self.path) as f:
                file_lines = f.read().splitlines()
                config_line = file_lines[0].split(" ")

                # Number of elements in first line must be 6
                if len(config_line) != 6:
                    correct = False

                # Config values must be greater than 0
                for value in config_line:
                    if int(value) < 0:
                        correct = False

                # x_tractor, y_tractor can't be greater or equal to rows and cols values
                if int(config_line[0]) >= int(config_line[5]) or int(config_line[1]) >= int(config_line[4]):
                    correct = False

                # Check number of rows and columns
                if len(file_lines) - 1 != int(config_line[5]):   # len(file_lines - 1) <- number of rows
                    correct = False

                for index in range(len(file_lines) - 1):   # Config line not included
                    values = file_lines[index + 1][1:].split(" ")
                    if len(values) != int(config_line[4]):  # len(values) <- number of cols
                        correct = False

                    # Matrix values must be greater than 0 and values can't be greater than maximum
                    for value in values:
                        if value == '':
                            correct = False
                        if int(value) < 0:
                            correct = False
                        if int(value) > int(config_line[3]):  # matrix_value > maximum
                            correct = False


        except Exception as ex:
            print(ex.__str__())
        return correct

    def get_Increase(self):
        return self.increase

    def set_Increase(self, increase):
        self.increase = increase

    def get_DepthMax(self):
        return self.depth_max

    def set_DepthMax(self, depth_max):
        self.depth_max = depth_max

    def generate_terrain(self,state):

        """
            This method generate a valid terrain randomly, with measures and values given via
            standard input
            main
            :return:
            None
            """

        while True:
            terrain_measures = input("Enter terrain measures (ROW-COL)")
            if terrain_measures[0].isnumeric() and terrain_measures[2].isnumeric():
                break
            else:
                print("Format is not valid : " + terrain_measures)
        while True:
            tractor_position = input("Where will be the tractor? (ROW-COL)")
            if tractor_position[0].isnumeric() and tractor_position[2].isnumeric():
                break
            else:
                print("Format is not valid : " + tractor_position)
        while True:
            k = input("Enter the desired amount of ground in each cell")
            if k.isnumeric():
                break
            else:
                print("Format is not valid : " + k)
        while True:
            maximum = input("Enter the maximum amount of ground in each cell")
            if maximum.isnumeric():
                break
            else:
                print("Format is not valid : " + maximum)

        # Create the initial state
        state.cols = int(terrain_measures[2])
        state.rows = int(terrain_measures[0])
        state.x_tractor = int(tractor_position[0])
        state.y_tractor = int(tractor_position[2])
        state.k = int(k)
        state.max = int(maximum)

        total = int(terrain_measures[2]) * int(terrain_measures[0]) * int(k)

        # Fill the terrain with values
        state.terrain_representation = [[[] for i in range(state.cols)] for j in range(state.rows)]
        for i in range(state.rows):
            for j in range(state.cols):
                if i == (int(terrain_measures[0]) - 1) and j == (int(terrain_measures[2]) - 1) and total < int(maximum):
                    state.terrain_representation[i][j] = total
                elif total < int(maximum):
                    state.terrain_representation[i][j] = random.randint(0, total)
                else:
                    state.terrain_representation[i][j] = random.randint(0, state.max)
                total -= state.terrain_representation[i][j]

        while total != 0:
            total = self.algoritm(total, state)

        self.check(state)
        state.print_terrain()

    def check(self, state):
        for i in range(state.rows):
            for j in range(state.cols):
                if state.terrain_representation[i][j] != state.k:
                    state.h += 1

    def algoritm(self, total, state):

        print("Algoritm " + str(total) + "\n")

        for i in range(state.rows):
            for j in range(state.cols):
                if total == 0:
                    break
                elif state.terrain_representation[i][j] == 0:
                    if total < state.max:
                        state.terrain_representation[i][j] = random.randint(0, total)
                    else:
                        state.terrain_representation[i][j] = random.randint(0, state.max)
                    total -= state.terrain_representation[i][j]
                elif state.terrain_representation[i][j] < state.max:
                    falta = state.max - state.terrain_representation[i][j] 
                    if falta <= total:
                        ran = random.randint(0, falta)
                    else:
                        ran = random.randint(0, total)
                    state.terrain_representation[i][j] += ran
                    total -= ran
        return total

    def read_file(self, state):
        """
        This method is used to read an external file, with the initial state configuration.

        :param state: State object reference, to fill its attributes.
        :return: None
        """
        try:
            with open(self.path) as f:
                file = f.read().splitlines()
                # Read configuration controls
                config = file[0].split(" ")
                tractor_x, tractor_y, k, maximum, col, row = config[0], config[1], config[2], config[3], config[4], \
                                                         config[5]
                # Create the terrain
                state.cols = int(col)
                state.rows = int(row)
                state.x_tractor = int(tractor_x)
                state.y_tractor = int(tractor_y)
                state.k = int(k)
                state.max = int(maximum)
                state.h = 0

                # Fill the terrain with values
                state.terrain_representation = [[[] for i in range(state.cols)] for j in range(state.rows)]
                for i in range(state.rows):
                    row_values = list(map(int, file[i + 1][1:].split(" ")))
                    state.terrain_representation[i] = row_values
                    for j in row_values:
                        if j != state.k:
                            state.h += 1
                state.print_terrain()

        except Exception as ex:
            print(ex.__str__())

    def successors(self, state):
        return StateOperations.StateOperations(state).get_successors()

    def goal_state(self, state):
        """
        This method is used to know if a state is the goal state or not. This is calculated
        using the heuristic.

        :param state: State object used to know if this object is the goal state.
        :return: True if the state parameter is the goal state. False otherwise.
        """
        return state.h == 0

    def initial_state(self):
        return self.state

    def write_file(self, successors, path):
        """
        This method writes the solution of the problem into an external file.

        :param successors: List with the necessaries successors to get a solution.
        :param path: St
        :return:
        """
        try:
            with open(path, "w") as f:
                f.write("Length of successors: {}\n".format(len(successors)))
                for successor in successors:
                    f.write("{}\n".format(str(successor)))
        except Exception as ex:
            print(ex.__str__())

