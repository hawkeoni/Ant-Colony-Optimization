import numpy as np

class Ant:

    def __init__(self, nodes, pher=0.6, alpha=1, beta=1):
        self.pher = pher
        self.length = 0
        self.alpha = alpha
        self.beta = beta
        self.nodes = nodes
        self.visited = np.random.randint(0, nodes, (1, ))

    @staticmethod
    def get_edges(graph, node):
        return  np.hstack((a[0:node, node], a[node, node + 1:]))

    def step(self, graph):
        current = self.visited[-1]
        probs = self.get_edges(graph.pheromone, current) ** self.alpha
        probs += 1 / self.get_edges(graph._matrix, current) ** self.beta
        probs[visited] = 0
        probs = probs / probs.sum()
        next_node = np.random.choice(np.arrange(0, nodes), p=probs)
        self.length += graph._matrix[current, next_node]
        self.visited.append(next_node)

    def backtrack(self, graph):
        begin = self.visited[-1]
        for next_node in self.visited[-2::-1]:
            graph.pheromone[begin][next_node] += self.pher / self.length
            begin = next_node




class Colony:

    def __init__(self, graph, size, vaporize):
        self.vaporize = vaporize
        self.size = size
        self.reassign()
        self.graph = graph

    def reassign(self):
        self._colony = [Ant(self.graph.nodes) for _ in range(self.size)]

    def _step(self):
        for ant in self._colony:
            ant.step()

    def _backtrack(self):
        for ant in self._colony:
            ant.backtrack(self.graph)

    def create_routes(self):
        for _ in range(self.graph.nodes - 1):
            self._step()

        rem_ph = self.graph.pheromone.copy()

        for _ in range(self.graph.nodes - 1):
            self._backtrack()

        self.graph.pheromone += -1 * rem_ph + rem_ph * (1 - self.vaporize)

