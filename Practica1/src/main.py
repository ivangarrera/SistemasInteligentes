from sys import exit

import Problem
import State
import StateOperations


def main():
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    operations = Problem.Problem(0, 0, "../terrain.txt", terrain)

    if operations.file_format_correct():
        operations.read_file(terrain)
        state_operations = StateOperations.StateOperations(terrain)
        successors = state_operations.get_successors()
        state_operations.get_successors_info(successors)
        operations.write_file(successors)
        print(state_operations.get_unique_representation())
    else:
        print("File {} has not a valid format.".format(operations.path))
        exit(1)



if __name__=="__main__":
    main()