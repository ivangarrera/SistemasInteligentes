import unittest
import sys
sys.path.insert(0, "../src")

from Problem import Problem
from State import State
from StateOperations import StateOperations


class State_Testing(unittest.TestCase):
    terrain = State(0, 0, 0, 0, 0, 0, 0)
    operations = Problem(0, 0, "../terrain.txt", terrain)
    operations.read_file(terrain)
    state_operations = StateOperations(terrain)

    successors_length1 = 32


    def test_state_values_correct(self):
        not self.assertLess(0, self.terrain.rows)
        not self.assertLess(0, self.terrain.cols)
        not self.assertLess(0, self.terrain.k)
        not self.assertLess(0, self.terrain.max)
        not self.assertLess(0, self.terrain.x_tractor)
        not self.assertLess(0, self.terrain.y_tractor)
        not self.assertGreater( self.terrain.rows, self.terrain.x_tractor)
        not self.assertGreater(self.terrain.cols, self.terrain.y_tractor)

    def test_instance_cols_rows(self):
        self.assertIsInstance(self.terrain.rows, int)
        self.assertIsInstance(self.terrain.cols, int)

    def test_instance_max_groundDesired(self):
        self.assertIsInstance(self.terrain.k, int)
        self.assertIsInstance(self.terrain.max, int)

    def test_instance_tractor_position(self):
        self.assertIsInstance(self.terrain.x_tractor, int)
        self.assertIsInstance(self.terrain.y_tractor, int)

    def test_instance_terrainRepresentation(self):
        self.assertIsInstance(self.terrain.terrain_representation, list)

    def test_tractor_position_is_tuple(self):
        self.assertEqual(len(self.terrain.get_position_tractor()), 2)

    def test_length(self):
        successors = self.state_operations.get_successors()
        self.assertEqual(len(successors), self.successors_length1)

    def test_get_possible_movements(self):
        self.assertEqual(len(self.terrain.get_all_movement_possibles()), 4)

    def test_quantity_ground_to_transfer(self):
        self.assertGreater(self.terrain.quantity_ground_to_transfer(), 0)

    def test_stateOperation_instance(self):
        self.assertIsInstance(self.state_operations.terrain, State)

    def test_hash_format(self):
        self.assertEqual(len(self.state_operations.get_unique_representation()), 128)

if __name__ == '__main__':
    unittest.main()