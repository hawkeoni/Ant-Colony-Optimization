from Generator import TSGraph
from Ant import Colony
from utils import get_shortest_path


import numpy as np
import argparse


def ACO_shortest(graphsize, ants, **kwargs):
    g = TSGraph(graphsize)
    #print(g._matrix)
    c = Colony(g, ants, kwargs.get("vaporize", 0.6), tactics=kwargs.get("tactics", "simple"))
    for i in range(kwargs.get("iter", 100)):
        c.create_routes()
        c.print_result()
    return g


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ant Colony TS optimization')
    parser.add_argument('--size', type=int, default=5, help="TS graph size")
    parser.add_argument('--ants', type=int, default=1, help="Amount of ants")
    parser.add_argument('--tactics', type=str, default="simple", help="Tactics (default is simple, can be maxmin)")
    parser.add_argument('--vaporize', type=float, default=0.6, help="Vaporize rate")
    parser.add_argument('--iter', type=int, default=100, help="Iterations")
    parser.add_argument('--seed', type=int, default=0, help="Iterations")
    args = parser.parse_args()
    np.random.seed(args.seed)
    g = ACO_shortest(args.size, args.ants, iter=args.iter, vaporize=args.vaporize, tactics=args.tactics)
    if args.size < 10:
        bestpath, bestlen = get_shortest_path(g)
        print(bestpath, bestlen)
