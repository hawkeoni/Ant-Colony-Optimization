from Generator import TSGraph
from Ant import Colony

from utils import get_shortest_path

import numpy as np

np.random.seed(3)

def testcase(graphsize, ants, **kwargs):
    g = TSGraph(graphsize)
    print(g._matrix)
    c = Colony(g, ants, kwargs.get("vaporize", 0.6))
    for i in range(kwargs.get("iter", 100)):
        c.create_routes()
        c.print_result()
    return g, c





g = testcase(graphsize=9, 50)
bestpath, bestlen = get_shortest_path(g)
