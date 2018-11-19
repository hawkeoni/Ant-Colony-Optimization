import numpy as np

class Ant:

    def __init__(self, nodes, pher=0.6, alpha=0.6, beta=0.4):
        self.pher = pher
        self.length = 0
        self.alpha = alpha
        self.beta = beta
        self.nodes = nodes
        self.visited = np.random.randint(0, nodes, (1, ))
        #print("Ant %d is on node %d" % (id(self), self.visited[-1]))

    @staticmethod
    def get_edges(graph, node):
        return  np.hstack((graph[0:node, node], graph[node, node:]))

    def step(self, graph):
        current = self.visited[-1]
        probs = self.get_edges(graph.pheromone, current) ** self.alpha
        probs += 1 / self.get_edges(graph._matrix, current) ** self.beta
        probs[self.visited] = 0
        probs = probs / probs.sum()
        next_node = np.random.choice(np.arange(0, self.nodes), p=probs)
        self.length += graph[current, next_node]
        self.visited = np.append(self.visited, next_node)

    def backtrack(self, graph):
        begin = self.visited[-1]
        for next_node in self.visited[-2::-1]:
            i, j = min(begin, next_node), max(begin, next_node)
            graph.pheromone[i][j] += self.pher / self.length
            begin = next_node
        return self.length, self.visited




class Colony:

    def __init__(self, graph, size, vaporize):
        self.vaporize = vaporize
        self.size = size
        self.graph = graph
        self.reassign()
        self.best = float('inf')
        self.path = np.array([])

    def reassign(self):
        self._colony = [Ant(self.graph.nodes) for _ in range(self.size)]

    def _step(self):
        for ant in self._colony:
            ant.step(self.graph)
            #print("Ant %d is going to node %d" % (id(ant), ant.visited[-1]))

    def _backtrack(self):
        for ant in self._colony:
            yield ant.backtrack(self.graph)


    def create_routes(self):

        for step in range(self.graph.nodes - 1):
            #print("On step %d" % step)
            self._step()

        rem_ph = self.graph.pheromone.copy()
        backtracker = self._backtrack()
        for _ in range(len(self._colony)):
            length, path = next(backtracker)
            if length < self.best:
                self.best = length
                self.path = path

        self.graph.pheromone += -1 * rem_ph + rem_ph * (1 - self.vaporize)
        print("Best path is " + '->'.join(map(str, self.path)) + ' of length %d' % self.best)
        self.reassign()

