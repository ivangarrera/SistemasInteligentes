import State
import StateOperations
import Problem


def main():
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    operations = Problem.Problem(0, 0, "./terrain.txt", terrain)
    operations.choose_option()
    state_operations = StateOperations.StateOperations(terrain)
    successors = state_operations.get_successors()
    state_operations.get_successors_info(successors)
    operations.write_file(successors)
    print(state_operations.get_unique_representation())

if __name__=="__main__":
    main()