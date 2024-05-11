from math import sqrt

class Node:
    def __init__(self, pos, neighbors=None):
        self.pos = pos
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)

    def distance(self, node):
        return sqrt(sum(pow(a - b, 2) for a, b in zip(self.pos, node.pos)))
