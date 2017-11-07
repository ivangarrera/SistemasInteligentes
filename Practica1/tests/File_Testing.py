import unittest
import sys

sys.path.insert(0, "../src")

from FileOperations import FileOperations


class File_Testing(unittest.TestCase):
    fileoperations = FileOperations("../terrain.txt")

    def test_correct_format_path(self):
        self.assertIsInstance(self.fileoperations.path, str)

    def test_file_correct(self):
        self.assertTrue(self.fileoperations.file_format_correct())

if __name__ == '__main__':
    unittest.main()