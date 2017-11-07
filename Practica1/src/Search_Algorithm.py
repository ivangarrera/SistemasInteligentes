import Border
import Node


class Search_Algorithm():
    def bounded_search(self, prob, strategy, max_depth):
        b = Border()
        initial_node = Node(prob.initial_state, 0, None, 0, None, 0)
        b.InsertNode(initial_node)
        sol = False
        while not sol and not b.IsEmpty():
            actual_node = b.Delete()
            if prob.goal_state(actual_node.get_state()):
                sol = True
            else:
                sucessors_list = prob.sucessors(actual_node.get_state())
                for sucessor in sucessors_list:
                    n = actual_node.create_node(sucessor, actual_node, strategy, max_depth)
                    b.InsertNode(n)
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
        return action_list
