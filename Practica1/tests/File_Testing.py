import unittest
import sys

sys.path.insert(0, "../src")

from FileOperations import FileOperations


class File_Testing(unittest.TestCase):
    fileoperations = FileOperations("../terrain.txt")

    def test_correct_format_path(self):
        self.assertIsInstance(self.fileoperations.path, str)

if __name__ == '__main__':
    unittest.main()