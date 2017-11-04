import Node

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