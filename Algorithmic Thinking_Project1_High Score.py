"""
Algorithmic thinking - Project 1 - Ali Baheri
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]), 4: set([1]),
             5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]),
             5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(num_nodes):
    """
    bulding a complete directed graph
    """
    complete_graph = {}
    set_nodes = set(range(num_nodes))
    
    for node in range(num_nodes):
        complete_graph[node] = set_nodes - set([node])

    return complete_graph


def compute_in_degrees(digraph):
    """
    calculating in-degree of nodes
    """
    in_degree = {}
    for key in digraph:
        in_degree[key] = 0
    for key in digraph:
        for dist in digraph[key]:
            in_degree[dist] += 1
    return in_degree


def in_degree_distribution(digraph):
    """
    calculating in-degree distribution
    """
    in_degree = compute_in_degrees(digraph)
    distribution = {}
    for key in in_degree:
        length = in_degree[key]
        if length in distribution:
            distribution[length] += 1
        else:
            distribution[length] = 1
    return distribution


print in_degree_distribution(EX_GRAPH2)
