import numpy as np
from gravit.sim.config import Config
from gravit.sim.graph import get_metropolis_hastings_W
from gravit.sim.consensus import GravitConsensus
from gravit.sim.scoring import honest_scoring

def test_fixed_point():
    config = Config(N=30, k=5, beta=0.0)
    G = nx.erdos_renyi_graph(config.N, 0.1)
    W = get_metropolis_hastings_W(G)

    consensus = GravitConsensus(config)
    consensus.set_graph(G)
    consensus.p = np.random.dirichlet(np.ones(config.k), config.N)
    s = honest_scoring(consensus.p, config.m, config.M)

    p_star, _ = consensus.run_until_convergence(s)
    assert np.abs(p_star.sum() - 1.0) < 1e-10
    print("✓ Fixed-point convergence verified")
