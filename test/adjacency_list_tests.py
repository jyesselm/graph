import unittest

from graph import adjacency_list, base

class Unittest(unittest.TestCase):

    def test(self):
        al = adjacency_list.AdjacencyList()
        ni = al.add_node(0, 3)
        self.assertTrue(ni == 0)
        self.assertTrue(al.get_num_nodes() == 1)
        self.assertTrue(al[0] == 0)
        al.add_node(1, 3)
        al.add_edge(base.NodeIndexandEdge(0, 0), base.NodeIndexandEdge(1, 0))
        self.assertTrue(al.get_num_edges() == 1)
        al.remove_node(0)
        self.assertTrue(al.get_num_edges() == 0)
        ni = al.add_node(2, 3)
        vals = [1, 2]
        for i, n in enumerate(al):
            self.assertTrue(vals[i] == n.index)

    def test_copy(self):
        al = adjacency_list.AdjacencyList()
        al.add_node(0, 3)
        al.add_node(1, 3)
        al.add_edge(base.NodeIndexandEdge(0, 0), base.NodeIndexandEdge(1, 0))
        al2 = al.clone()
        self.assertTrue(al2.get_num_nodes() == 2)
        self.assertTrue(al2.get_num_edges() == 1)



    def test_complex_obj(self):
        al = adjacency_list.AdjacencyList()
        class Point(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y
        al.add_node(Point(1, 2), 3)
        self.assertTrue(al.get_node_data(0).x == 1)
        al.get_node_data(0).x = 10
        self.assertTrue(al.get_node_data(0).x == 10)


def main():
    unittest.main()


if __name__ == '__main__':
    main()