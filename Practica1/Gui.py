import Terrain


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

gui = Gui()
terrain, terrain_obj = gui.read_file()
gui.print_terrain(terrain)
