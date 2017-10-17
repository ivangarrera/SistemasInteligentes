
class FileOperations:
    def __init__(self):
        self.init = True

    def read_file(self, state):
        try:
            with open("./terrain.txt") as f:
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

