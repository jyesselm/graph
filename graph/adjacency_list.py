from typing import List, Iterator
from graph import base


class AdjacencyList(object):
    def __init__(self, is_dynamic=False):
        self._edges = {}
        self._nodes = {}
        self._index = 0
        self._is_dynamic = is_dynamic

    def clone(self):
        new_al = AdjacencyList(self._is_dynamic)
        new_al._nodes = self._nodes
        new_al._index = self._index
        for ni, n in self._nodes.items():
            new_al._edges[ni] = [None] * len(self.get_node_edges(ni))
        for ni, edges in self._edges.items():
            new_al._edges[ni] = [None] * len(edges)
        for ni, edges in self._edges.items():
            for e in edges:
                if e is None:
                    continue
                new_al._edges[e.node_i][e.edge_i] = base.Edge(e.node_i, e.node_j,
                                                              e.edge_i, e.edge_j)
                new_al._edges[e.node_j][e.edge_j] = base.Edge(e.node_i, e.node_j,
                                                              e.edge_i, e.edge_j)
        return new_al

    def __getitem__(self, ni):
        return self.get_node_data(ni)

    def __iter__(self) -> Iterator[base.Node]:
        return self._nodes.values().__iter__()

    def add_node(self, d, n_edges: int) -> int:
        self._nodes[self._index] = base.Node(d, self._index)
        self._edges[self._index] = [None] * n_edges
        self._index += 1
        return self._index - 1

    def add_edge(self, nie1: base.NodeIndexandEdge, nie2: base.NodeIndexandEdge):
        if self._is_dynamic:
            self._update_dynamic_edge(nie1)
            self._update_dynamic_edge(nie2)
        if not self.edge_index_empty(nie1.node_index, nie1.edge_index):
            raise ValueError("cannot add edge between {} {}, this edge is already filled".format(
                    nie1.node_index, nie2.node_index))
        if not self.edge_index_empty(nie2.node_index, nie2.edge_index):
            raise ValueError("cannot add edge between {} {}, this edge is already filled".format(
                    nie1.node_index, nie2.node_index))
        e = base.Edge(nie1.node_index, nie2.node_index, nie1.edge_index, nie2.edge_index)
        self._edges[nie1.node_index][nie1.edge_index] = e
        self._edges[nie2.node_index][nie2.edge_index] = e

    def remove_node(self, ni):
        edges = self.get_node_edges(ni)
        for e in edges:
            if e is None:
                continue
            self._edges[e.node_i][e.edge_i] = None
            self._edges[e.node_j][e.edge_j] = None
        self._edges.pop(ni)
        self._nodes.pop(ni)

    def remove_edge(self, nie1: base.NodeIndexandEdge, nie2: base.NodeIndexandEdge):
        if not self.edge_index_empty(nie1.node_index, nie1.edge_index):
            raise ValueError("cannot remove edge between {} {}, this edge is already empty".format(
                    nie1.node_index, nie2.node_index))
        if not self.edge_index_empty(nie2.node_index, nie2.edge_index):
            raise ValueError("cannot remove edge between {} {}, this edge is already empty".format(
                    nie1.node_index, nie2.node_index))
        self._edges[nie1.node_index][nie1.edge_index] = None
        self._edges[nie2.node_index][nie2.edge_index] = None

    # getters
    ###################################################################################
    def edge_index_empty(self, ni: int, ei: int) -> bool:
        if ni not in self._edges:
            raise ValueError("no nodes with index: {}".format(ni))
        if len(self._edges) < ei - 1:
            raise ValueError("no edge {} on node: {}".format(ei, ni))
        if self._edges[ni][ei] is None:
            return True
        else:
            return False

    def get_num_nodes(self) -> int:
        return len(self._nodes)

    def get_num_edges(self) -> int:
        n_edges = 0
        for ni, edges in self._edges.items():
            for e in edges:
                if e is not None:
                    n_edges += 1
        return int(n_edges / 2)

    def get_node_data(self, ni):
        if ni in self._nodes:
            return self._nodes[ni].data
        else:
            raise ValueError("unknown node: {}".format(ni))

    def get_node_edges(self, ni) -> List[base.Edge]:
        if ni in self._edges:
            return self._edges[ni]
        else:
            raise ValueError("unknown node: {}".format(ni))

    # private methods
    ###################################################################################
    def _update_dynamic_edge(self, nie: base.NodeIndexandEdge):
        edges = self._edges[nie.node_index]
        if len(edges) < nie.edge_index - 1:
            diff = nie.edge_index - 1 - len(edges)
            edges.extend([None] * diff)

    def _update_next_index(self):
        largest = 0
        for i, n in self._nodes.items():
            if i > largest:
                largest = i
        self._index = largest


class DirectedAdjacencyList(AdjacencyList):
    def __init__(self, is_dynamic=False):
        super().__init__(is_dynamic)
        self._parent = {}
