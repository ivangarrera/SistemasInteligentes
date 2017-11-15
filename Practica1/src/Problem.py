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
                    values = file_lines[index + 1].split(" ")
                    if len(values) != int(config_line[4]):  # len(values) <- number of cols
                        correct = False

                    # Matrix values must be greater than 0 and values can't be greater than maximum
                    for value in values:
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

    def choose_option(self):
        while True:
            choice = input('From where do you want to load the data?\n1.- From file.\n2.- Random generated.\n')
            if choice == '1':
                if self.file_format_correct():
                    self.read_file(self.state)
                    break
                else:
                    print("File {} has not a valid format.".format(self.path))
                    exit(1)
            elif choice == '2':
                self.generate_terrain(self.state)
                break
            else:
                print("'"+choice+"' is not a valid option. Please, try again.")


    def generate_terrain(self, state):
        terrain_measures = input("Enter terrain measures (ROW-COL)")
        tractor_position = input("Where will be the tractor? (ROW-COL)")
        k = input("Enter the desired amount of ground in each cell")
        maximum = input("Enter the maximum amount of ground in each cell")

        # Create the terrain
        state.cols = int(terrain_measures[2])
        state.rows = int(terrain_measures[0])
        state.x_tractor = int(tractor_position[0])
        state.y_tractor = int(tractor_position[2])
        state.k = int(k)
        state.max = int(maximum)

        total = state.cols * state.rows * state.k


        # Fill the terrain with values
        state.terrain_representation = [[[] for i in range(int(state.cols))] for j in range(int(state.rows))]
        for i in range(int(terrain_measures[2])):
            for j in range(int(terrain_measures[0])):
                ran = random.randint(0, state.max)
                if total - ran >= 0:
                    total -= ran
                    state.terrain_representation[i][j] = ran
                else:
                    state.terrain_representation[i][j] = 0
                if i == state.cols  & j == state.rows & total < state.max:
                    state.terrain_representation[i][j] = total


        state.print_terrain()

    def read_file(self, state):
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

                # Fill the terrain with values
                state.terrain_representation = [[[] for i in range(int(state.cols))] for i in range(int(state.rows))]
                for i in range(int(row)):
                    row_values = list(map(int, file[i + 1].split(" ")))
                    print(row_values)
                    state.terrain_representation[i] = row_values
                state.print_terrain()

        except Exception as ex:
            print(ex.__str__())

    def successors(self, state):
        return StateOperations.StateOperations(state).get_successors()


    def goal_state(self, state):
        is_goal = True
        for i in range(int(state.rows)):
            for j in range(int(state.cols)):
                if state.terrain_representation[i][j] != state.k:
                    is_goal = False
        return is_goal

    def initial_state(self):
        return self.state


    def write_file(self, successors):
        try:
            with open("./successors.txt", "w") as f:
                f.write("Length of successors: {}\n".format(len(successors)))
                for successor in successors:
                    f.write("{}\n".format(str(successor)))
        except Exception as ex:
            print(ex.__str__())

