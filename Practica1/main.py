import FileOperations
import State
import StateOperations

def main():
    operations = FileOperations.Operations()
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    operations.read_file(terrain)
    state_operations = StateOperations.StateOperations(terrain)
    successors = state_operations.get_successors()
    state_operations.get_successors_info(successors)
    operations.write_file(successors)

if __name__=="__main__":
    main()