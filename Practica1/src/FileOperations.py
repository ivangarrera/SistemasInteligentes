
class FileOperations:
    def __init__(self, path):
        self.path = path

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
                    row_values = file[i + 1].split(" ")
                    state.terrain_representation[i] = row_values
        except Exception as ex:
            print(ex.__str__())

    def write_file(self, successors):
        try:
            with open("./successors.txt", "w") as f:
                f.write("Length of successors: {}\n".format(len(successors)))
                for successor in successors:
                    f.write("{}\n".format(str(successor)))
        except Exception as ex:
            print(ex.__str__())

