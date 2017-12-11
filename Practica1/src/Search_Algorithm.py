from Border import Border
from Node import Node


class Search_Algorithm():

    def __bounded_search(self, prob, strategy, max_depth):
        """
        Method required to do the bounded search. It uses a border, a queue of Nodes that
        have to be checked.

        :param prob: Problem Object, used to know if a Node is solution, and get successors.
        :param strategy: String, Strategy to follow, to get a solution
        :param max_depth: Integer, Maximum depth that the search tree must reach.
        :return: The solution, a list of successors to get the objective Node. If the algorithm
        doesn't find a solution, it returns None.
        """
        border = Border()
        closed_list = {}   # List needed to prune the tree
        initial_node = Node(prob.initial_state(), 0, None, 0, None, 0)
        border.InsertNode(initial_node)

        #closed_list[initial_node.get_state().__str__()] = initial_node.get_value()
        sol = False
        while not sol and not border.IsEmpty():
            actual_node = border.Delete()
            if strategy == 'BFS' or strategy == 'DFS':
                closed_list[actual_node.get_state().__str__()] = actual_node.get_cost()
            else:
                closed_list[actual_node.get_state().get_unique_representation()] = actual_node.get_value()

            if prob.goal_state(actual_node.get_state()):
                actual_node.get_state().print_terrain()
                sol = True
            else:
                if actual_node.get_depth() < max_depth:
                    successors_list = prob.successors(actual_node.get_state())
                    for successor in successors_list:
                        new_node = actual_node.create_node(successor, actual_node, strategy, max_depth,prob)
                        # Prune the tree
                        if strategy == 'BFS' or strategy == 'DFS':
                            if new_node.get_state().get_unique_representation() not in closed_list:
                                border.InsertNode(new_node)
                                closed_list[new_node.get_state().get_unique_representation()] = new_node.get_cost()
                            else:
                                if closed_list[new_node.get_state().get_unique_representation()] > new_node.get_cost():
                                    closed_list[new_node.get_state().get_unique_representation()] = new_node.get_cost()
                                    border.InsertNode(new_node)
                        else:
                            if new_node.get_state().get_unique_representation() not in closed_list:
                                border.InsertNode(new_node)
                                closed_list[new_node.get_state().get_unique_representation] = new_node.get_value()
                            else:
                                if closed_list[new_node.get_state().get_unique_representation()] > new_node.get_value():
                                    closed_list[new_node.get_state().get_unique_representation()] = new_node.get_value()
                                    border.InsertNode(new_node)



        if sol:
            print('El costo de la solución es: '+ str(actual_node.get_cost()))
            print('La profundidad es: ' + str(actual_node.get_depth()))
            return self.__create_solution(actual_node)
        else:
            return None

    def search(self, prob, strategy, max_depth, inc_depth):
        """
        This method is responsible for doing the search algorithm using the chosen strategy
        and returning the solution, if it exists.

        :param prob: Problem object
        :param strategy: Strategy to use in the search algorithm
        :param max_depth: Maximum depth the search tree must reach
        :param inc_depth: Increase necessary in the increase search
        :return: List with the Nodes to reach the solution.
        """
        if strategy != 'IT':
            inc_depth = max_depth
        actual_depth = inc_depth
        sol = None
        while not sol and actual_depth <= max_depth:
            sol = self.__bounded_search(prob, strategy, actual_depth)
            actual_depth += inc_depth
        return sol

    def __create_solution(self, actual_node):
        """
        Method used to create a list with the Nodes to reach the solution. The solution will be the
        parent of the solution node, the parent of the parent of the solution node, ..., until you reach
        the initial Node.

        :param actual_node: Solution Node.
        :return: List, with the Nodes to reach the solution.
        """
        action_list = []
        node_list = []

        while actual_node is not None:
            node_list.append(actual_node)
            action_list.append(actual_node.get_action())
            actual_node = actual_node.get_parent()
        node_list.reverse()
        action_list.reverse()
        for node in node_list:
            if node.get_action()!= None:
                print(node.get_action())
            node.get_state().print_terrain()
        action_list.pop(0)
        return action_list
