import unittest

from graph import base

class Unittest(unittest.TestCase):

    def test_node(self):
        n = base.Node(5, 0)
        self.assertTrue(n.data == 5)
        self.assertTrue(n.index == 0)

    def test_node_ei(self):
        nei = base.NodeIndexandEdge(10, 0)
        self.assertTrue(nei.node_index == 10)
        self.assertTrue(nei.edge_index == 0)
        nei2 = base.NodeIndexandEdge(10, 0)
        self.assertTrue(nei == nei2)
        nei3 = base.NodeIndexandEdge(5, 0)
        nei4 = base.NodeIndexandEdge(10, 1)
        self.assertTrue(not nei == nei3)
        self.assertTrue(not nei == nei4)

    def test_edge(self):
        e = base.Edge(0, 1, 2, 3)
        self.assertTrue(e.partner(0) == 1)
        self.assertTrue(e.partner(1) == 0)
        self.assertTrue(e.end_index(0) == 2)
        self.assertTrue(e.end_index(1) == 3)
        with self.assertRaises(ValueError):
            e.partner(5)
        with self.assertRaises(ValueError):
            e.end_index(5)
def main():
    unittest.main()


if __name__ == '__main__':
    main()