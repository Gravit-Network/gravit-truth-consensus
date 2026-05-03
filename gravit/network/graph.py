import networkx as nx

def create_graph(N: int):
    return nx.erdos_renyi_graph(N, 0.1)
