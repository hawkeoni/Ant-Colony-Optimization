from Generator import TSGraph
from Ant import Colony

import numpy as np


def testcase(graphsize, ants, vaporize=0.6, iterations=100):
    np.random.seed(3)
    g = TSGraph(graphsize)
    print(g._matrix)
    c = Colony(g, ants, vaporize)
    for i in range(iterations):
        c.create_routes()


testcase(5, 30)