def permutations(n):
    ans = [[]]

    for i in range(n):
        local = []
        for arr in ans:
            for j in range(i + 1):
                local.append(arr[:j] + [i] + arr[j:])
        ans = local
    return ans


def get_length(g, path):
    length = 0
    for i in range(1, len(path)):
        length += g[path[i - 1], path[i]]
    return length


def get_shortest_path(graph):
    bestpath = 0
    bestlen = float('inf')
    for path in permutations(graph.nodes):
        curlen = get_length(graph, path)
        if curlen < bestlen:
            bestlen = curlen
            bestpath = path
    return bestpath, bestlen