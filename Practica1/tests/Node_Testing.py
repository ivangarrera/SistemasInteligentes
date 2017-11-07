import unittest
import sys
sys.path.insert(0, "../src")

from Node import Node


class Node_Testing(unittest.TestCase):

    node = Node("387becef34faaa2561d0a8747fc6912e3d554eae18df67f1dd19fad6dff9d749e2d5a5f4cc565776ab32c13bf9a77da75c7b6691a7ac06768626bcebe14a68af",
                2,
                ((1, 2), [(2, (2, 1)), (0, (2, 3)), (0, (3, 2)), (0, (1, 2))]),
                6,
                Node("387becef34faaa2561d0a8747fc6912e3d554eae18df67f1dd19fad6dff9d749e2d5a5f4cc565776ab32c13bf9a77da75c7b6691a7ac06768626bcebe14a68ad",
                     2, ((1, 2), [0]), 10, None))

    def test_if_correct(self):
        self.assertEqual(len(self.node.get_state()), 128)
        self.assertGreater(self.node.get_cost(), 0)
        self.assertIsInstance(self.node.get_action(), tuple)
        self.assertIsInstance(self.node.get_parent(), Node)

    def test_nodes_not_equal(self):
        self.assertNotEqual(self.node.get_state(), self.node.get_parent().get_state())


if __name__ == '__main__':
    unittest.main()