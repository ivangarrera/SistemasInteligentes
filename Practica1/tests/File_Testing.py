import unittest
import sys

sys.path.insert(0, "../src")

from Problem import Problem
from State import State


class File_Testing(unittest.TestCase):
    state = State(0, 0, 0, 0, 0, 0, 0)
    fileoperations = Problem(0, 0, "../terrain.txt", state)

    def test_correct_format_path(self):
        self.assertIsInstance(self.fileoperations.path, str)

    def test_file_correct(self):
        self.assertTrue(self.fileoperations.file_format_correct())

if __name__ == '__main__':
    unittest.main()