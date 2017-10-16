import Nodo
import State

class NodoOperations:
    def __init__(self, terrain, succesors):
            self.terrain = terrain
            self.succesors = succesors

    def get_state(self):
        status = []
        tractor = []
        x = self.terrain.x_tractor
        y = self.terrain.y_tractor
        tractor.append(x)
        tractor.append(y)
        status.append(self.terrain.terrain_representation)
        status.append(tractor)
        return status

    def get_action(self):
        if (self.terrain.k - int(self.terrain.terrain_representation[self.terrain.x_tractor][self.terrain.y_tractor])) <= 0:
            return 0
        else:
            return self.terrain.k - int(self.terrain.terrain_representation[self.terrain.x_tractor][self.terrain.y_tractor])

    def cargar(self):
        no = Nodo.Nodo(self.get_state(), len(self.succesors), self.get_action(),0)
        print("Terreno "+str(no.get_terrain()))
        print("Accion "+str(no.get_action()))
        print("Coste total "+str(no.get_cost()))
        print("Valor "+str(no.get_value()))
