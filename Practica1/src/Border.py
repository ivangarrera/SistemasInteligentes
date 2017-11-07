<<<<<<< HEAD:Practica1/src/Border.py
=======
import Node

>>>>>>> 0866c5cb7c27220032799b467174a5274aed61c8:Practica1/Border.py
class Border:
    def __init__(self):
        self.__queue = []

    def InsertNode(self, node):
        i = 0
        while i < len(self.__queue) and node.get_value()<self.__queue[i].get_value():
            i += 1
        self.__queue.insert(i, node)

    def Delete(self):
        return self.__queue.pop(0)

    def IsEmpty(self):
        return len(self.__queue) == 0