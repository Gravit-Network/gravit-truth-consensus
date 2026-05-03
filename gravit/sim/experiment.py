import numpy as np
import networkx as nx
import os
from .config import Config
from .graph import get_metropolis_hastings_W
from .scoring import honest_scoring
from .byzantine import apply_byzantine
from .consensus import GravitConsensus
from .metrics import compute_phi, compute_avg_distance, entropy

def run_full_experiment(beta_list=[0.0, 0.1, 0.2, 0.3], runs=30):
    os.makedirs("results", exist_ok=True)
    results = []
    for beta in beta_list:
        run_data = []
        for r in range(runs):
            config = Config(N=50, k=5, beta=beta, seed=r)
            G = nx.erdos_renyi_graph(config.N, 0.1, seed=r)
            W = get_metropolis_hastings_W(G)
            consensus = GravitConsensus(config)
            consensus.set_graph(G)
            consensus.p = np.random.dirichlet(np.ones(config.k), config.N)
            s = honest_scoring(consensus.p, config.m, config.M)
            s = apply_byzantine(s, config.beta, strategy="constant", p_current=consensus.p)
            p_star, history_phi = consensus.run_until_convergence(s)
            final_phi = history_phi[-1]
            final_dist = compute_avg_distance(consensus.p, p_star)
            final_ent = entropy(p_star)
            run_data.append((final_phi, final_dist, final_ent))
        results.append({
            "beta": beta,
            "mean_phi": float(np.mean([x[0] for x in run_data])),
            "mean_dist": float(np.mean([x[1] for x in run_data])),
            "mean_entropy": float(np.mean([x[2] for x in run_data]))
        })
    with open("results/experiment_results.json", "w") as f:
        import json
        json.dump(results, f, indent=2)
    return results
