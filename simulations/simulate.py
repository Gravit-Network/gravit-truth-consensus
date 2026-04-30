import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def run_simulation(G, beta=0.1, T=50, k=5):
    N = len(G)
    W = nx.to_numpy_array(G)
    W = W / W.sum(axis=1, keepdims=True)

    p = np.ones((N, k)) / k
    history = []

    for t in range(T):
        s = np.ones((N, k))
        byz = np.random.rand(N) < beta

        for i in range(N):
            if byz[i]:
                s[i] = np.random.uniform(0.1, 1.0, k)

        p = np.einsum('ij,jk->ik', W, p * s)
        p = p / p.sum(axis=1, keepdims=True)

        history.append(np.mean(np.sum(p, axis=1)))

    return history


G = nx.erdos_renyi_graph(50, 0.1)
h = run_simulation(G)

plt.plot(h)
plt.title("Consensus convergence")
plt.show()
