import Border
import Node


class Search_Algorithm():

    def bounded_search(self, prob, strategy, max_depth):
        b = Border.Border()
        closed_list = []    # List needed to prune the tree
        initial_node = Node.Node(prob.initial_state(), 0, None, 0, None, 0)
        b.InsertNode(initial_node)
        sol = False
        while not sol and not b.IsEmpty():
            actual_node = b.Delete()
            closed_list.append(actual_node.get_state().__str__())
            if prob.goal_state(actual_node.get_state()):
                actual_node.get_state().print_terrain()
                sol = True
            else:
                if actual_node.get_depth() < max_depth:
                    successors_list = prob.successors(actual_node.get_state())
                    for successor in successors_list:
                        n = actual_node.create_node(successor, actual_node, strategy, max_depth,prob)
                        # Prune the tree
                        if n.get_state().__str__() not in closed_list:
                            b.InsertNode(n)
                            closed_list.append(n.get_state().__str__())
        if sol:
            return self.create_solution(actual_node)
        else:
            return None

    def search(self, prob, strategy, max_depth, inc_depth):
        if (strategy != 'IT'):
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
        action_list.reverse()
        action_list.pop(0)
        return action_list
