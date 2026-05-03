import networkx as nx
import numpy as np
def get_metropolis_hastings_W(G):
    N = len(G)
    deg = np.array([d for _, d in G.degree()])
    W = np.zeros((N, N))
    for u in range(N):
        for v in G.neighbors(u):
            W[u, v] = 1.0 / max(deg[u], deg[v])
        W[u, u] = 1.0 - np.sum(W[u])
    return W
