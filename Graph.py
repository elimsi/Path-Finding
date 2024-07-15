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

    def BFS(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None
        queue = Queue()
        queue.put(start)
        parent = {start: None}
        while not queue.empty():
            current = queue.get()
            node = self.nodes[current]
            if current == end:
                break
            for neighbor in node.neighbors:
                if neighbor.pos not in parent:
                    parent[neighbor.pos] = current
                    queue.put(neighbor.pos)
        if end not in parent:
            return None
        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]
        path.reverse()
        return path

    def djikstra(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None
        queue = Queue()
        queue.put(start)
        parent = {start: None}
        distance = {start: 0}
        while not queue.empty():
            current = queue.get()
            node = self.nodes[current]
            if current == end:
                break
            for neighbor in node.neighbors:
                if neighbor.pos not in parent:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    queue.put(neighbor.pos)
                elif distance[current] + node.distance(neighbor) < distance[neighbor.pos]:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    queue.put(neighbor.pos)
        if end not in parent:
            return None
        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]
        path.reverse()
        return path

    def heuristic(self, pos, goal):
        return ((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)**0.5

    def A_star(self, start, end):
        import heapq
        if start not in self.nodes or end not in self.nodes:
            return None
        queue = [(0, start)]
        cost = {start: 0}
        parent = {start: None}
        while queue:
            _, current = heapq.heappop(queue)
            node = self.nodes[current]
            if current == end:
                break
            for neighbor in node.neighbors:
                new_cost = cost[current] + node.distance(neighbor)
                if neighbor.pos not in cost or new_cost < cost[neighbor.pos]:
                    cost[neighbor.pos] = new_cost
                    priority = new_cost + self.heuristic(neighbor.pos, end)
                    heapq.heappush(queue, (priority, neighbor.pos))
                    parent[neighbor.pos] = current
        if end not in parent:
            return None
        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]
        path.reverse()
        return path
