from Node import Node
from queue import Queue

class Graph:
    def __init__(self, grid=None):
        self.nodes = dict()
        if grid is not None:
            self.build(grid)

    def add(self, pos):
        self.nodes[pos] = Node(pos)
