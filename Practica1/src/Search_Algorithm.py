import Border
import Node


class Search_Algorithm():
    def bounded_search(self, prob, strategy, max_depth):
<<<<<<< HEAD
        b = Border()
        initial_node = Node(prob.initial_state, 0, None, 0, None, 0)
=======
        b = Border.Border()
        initial_node = Node.Node(prob.initial_state(), 0, None, 0, None, 0)
>>>>>>> f8a5f7697a19b625f654759e2c598ee383d88765
        b.InsertNode(initial_node)
        sol = False
        while not sol and not b.IsEmpty():
            actual_node = b.Delete()
            if prob.goal_state(actual_node.get_state()):
                sol = True
            else:
<<<<<<< HEAD
                sucessors_list = prob.sucessors(actual_node.get_state())
                for sucessor in sucessors_list:
                    n = actual_node.create_node(sucessor, actual_node, strategy, max_depth)
                    b.InsertNode(n)
=======
                if actual_node.get_depth()<max_depth:
                    successors_list = prob.successors(actual_node.get_state())
                    for successor in successors_list:
                        n = actual_node.create_node(successor, actual_node, strategy, max_depth)
                        b.InsertNode(n)
>>>>>>> f8a5f7697a19b625f654759e2c598ee383d88765
        if sol:
            return self.create_solution(actual_node)
        else:
            return None

    def search(self, prob, strategy, max_depth, inc_depth):
<<<<<<< HEAD
        if (strategy != 'IT'):
=======
        if (strategy != 'BFS'):
>>>>>>> f8a5f7697a19b625f654759e2c598ee383d88765
            inc_depth = max_depth
        actual_depth = inc_depth
        sol = None
        while not sol and actual_depth <= max_depth:
            sol = self.bounded_search(prob, strategy, actual_depth)
            actual_depth += inc_depth
        return sol

    def create_solution(self, actual_node):
        action_list = []
        while actual_node != None:
            action_list.append(actual_node.get_action())
            actual_node = actual_node.get_parent()
<<<<<<< HEAD
=======
        action_list.reverse()
>>>>>>> f8a5f7697a19b625f654759e2c598ee383d88765
        return action_list
