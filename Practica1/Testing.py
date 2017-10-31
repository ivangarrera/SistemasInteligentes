import unittest
import StateOperations
import State
import FileOperations

class Testing(unittest.TestCase):
    terrain = State.State(0, 0, 0, 0, 0, 0, 0)
    state_operations = StateOperations.StateOperations(terrain)

    successors_length1 = 32

    def test_length(self):
        operations = FileOperations.FileOperations("./terrain.txt")
        operations.read_file(self.terrain)
        successors = self.state_operations.get_successors()
        self.assertEqual(len(successors), self.successors_length1)

if __name__ == '__main__':
    unittest.main()