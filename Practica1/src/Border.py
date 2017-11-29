import heapq
from itertools import count

class Border:
    """
    Class needed to create the border. The border is a priority queue, based in a heap priority queue.
    The criteria to recover the Nodes from the border is the value of the node. If two nodes have the same
    value, the priority queue looks into counter field.
    """
    def __init__(self):
        self.__queue=[]
        self._counter = count()

    def InsertNode(self, node):
        """
        Insert the given node into the priority queue.
        :param node: Node to insert into de priority queue.
        :return:
        """
        heapq.heappush(self.__queue, ((node.get_value(), next(self._counter)), node))

    def Delete(self):
        """
        Return the corresponding node, looking at value field.
        :return: Node
        """
        return heapq.heappop(self.__queue)[1]

    def IsEmpty(self):
        """

        :return: True if the queue is empty. False otherwise.
        """
        return len(self.__queue) == 0






