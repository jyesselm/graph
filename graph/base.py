class Node(object):
    def __init__(self, data, index):
        self.__data = data
        self.__index = index

    @property
    def data(self):
        return self.__data

    @property
    def index(self):
        return self.__index


class NodeIndexandEdge(object):
    def __init__(self, node_index, edge_index):
        self.__node_index = node_index
        self.__edge_index = edge_index

    def __eq__(self, other):
        return (self.__node_index == other.__node_index and
                self.__edge_index == other.__edge_index)

    @property
    def node_index(self):
        return self.__node_index

    @property
    def edge_index(self):
        return self.__edge_index


class Edge(object):
    def __init__(self, node_i, node_j, edge_i, edge_j):
        self.__node_i = node_i
        self.__node_j = node_j
        self.__edge_i = edge_i
        self.__edge_j = edge_j

    def __eq__(self, other):
        return (
                self.__node_i == other.__node_i and self.__node_j == other.__node_j and
                self.__edge_i == other.__edge_i and self.__edge_j == other.__edge_j
        )

    def partner(self, index):
        if index == self.__node_i:
            return self.__node_j
        elif index == self.__node_j:
            return self.__node_i
        else:
            raise ValueError("index is not node_i or node_j")

    def end_index(self, index):
        if index == self.__node_i:
            return self.__edge_i
        elif index == self.__node_j:
            return self.__edge_j
        else:
            raise ValueError("index is not node_i and node_j")

    @property
    def node_i(self):
        return self.__node_i

    @property
    def node_j(self):
        return self.__node_j

    @property
    def edge_i(self):
        return self.__edge_i

    @property
    def edge_j(self):
        return self.__edge_j

