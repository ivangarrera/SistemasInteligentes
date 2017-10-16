import FileOperations
import State
import StateOperations

def main():
    operations = FileOperations.FileOperations()
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    operations.read_file(terrain)
    state_operations = StateOperations.StateOperations(terrain)
    successors = state_operations.get_successors()
    state_operations.get_successors_info(successors)
    operations.write_file(successors)
    print(state_operations.get_unique_representation())

if __name__=="__main__":
    main()