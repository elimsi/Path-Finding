from Node import Node
from queue import Queue

class Graph:
    def __init__(self, grid=None):
        self.nodes = dict()
        if grid is not None:
            self.build(grid)

    def add(self, pos):
        self.nodes[pos] = Node(pos)

    def add_neighbor(self, pos1, pos2):
        if pos1 not in self.nodes:
            self.add(pos1)
        if pos2 not in self.nodes:
            self.add(pos2)
        self.nodes[pos1].neighbors.add(self.nodes[pos2])
        self.nodes[pos2].neighbors.add(self.nodes[pos1])

    def build(self, matrix):
        n, m = matrix.shape
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0),(-1, 1), (1, 1), (1, -1), (-1, -1)]
        for x in range(m):
            for y in range(n):
                if not matrix[y, x]:
                    continue
                self.add((x, y))
                for dx, dy in steps:
                    if not (0 <= x + dx < m and 0 <= y + dy < n):
                        continue
                    if not matrix[y + dy, x + dx]:
                        continue
                    self.add_neighbor((x, y), (x + dx, y + dy))
