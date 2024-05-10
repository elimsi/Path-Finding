from math import sqrt

class Node:
    def __init__(self, pos, neighbors=None):
        self.pos = pos
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = set()
