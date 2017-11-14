import Node
import heapq
from itertools import count

class Border:
    def __init__(self):
        self.__queue=[]
        self._counter = count()

    def InsertNode(self, node):
        heapq.heappush(self.__queue, ((node.get_value(),next(self._counter)), node))

    def Delete(self):
        return heapq.heappop(self.__queue)[1]

    def IsEmpty(self):
        return len(self.__queue) == 0






