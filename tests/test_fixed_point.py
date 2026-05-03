import numpy as np
import networkx as nx
from gravit.sim.config import Config
from gravit.sim.consensus import GravitConsensus

def test_fixed_point():
    config = Config(N=30, k=5, beta=0.0)
    config.T = 600
    G = nx.complete_graph(config.N)
    consensus = GravitConsensus(config)
    consensus.set_graph(G)
    consensus.p = np.random.dirichlet(np.ones(config.k), config.N)
    s_mid = float(0.5 * (config.m + config.M))
    s = np.full((config.N, config.k), s_mid, dtype=float)

    p_star, hist = consensus.run_until_convergence(s)
    assert np.abs(p_star.sum() - 1.0) < 1e-10
    assert hist[-1] < 1e-5
    print("✓ Fixed-point convergence verified")
