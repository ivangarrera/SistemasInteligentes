from sys import exit

import Problem
import State
import StateOperations
import Search_Algorithm


def main():
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    operations = Problem.Problem(0, 0, "../terrain.txt", terrain)
    operations.choose_option()
    state_operations = StateOperations.StateOperations(terrain)
    sol = Search_Algorithm.Search_Algorithm().search(operations, 'BFS', 9, 17)
    #successors = state_operations.get_successors()
    #state_operations.get_successors_info(successors)
    operations.write_file(sol)
    print(state_operations.get_unique_representation())



if __name__=="__main__":
    main()