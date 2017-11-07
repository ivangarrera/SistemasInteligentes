import Node
import heapq

class Border:
    def __init__(self):
        self.__queue=[]

    def InsertNode(self, node):
        heapq.heappush(self.__queue, (node.get_value(), node))

    def Delete(self):
        return heapq.heappop(self.__queue)[1]

    def IsEmpty(self):
        return len(self.__queue)==0



