import numpy as np
import networkx as nx
import os
from .config import Config
from .scoring import honest_scoring
from .byzantine import apply_byzantine
from .consensus import GravitConsensus
from .metrics import compute_avg_distance, entropy

def run_full_experiment(
    beta_list=[0.0, 0.1, 0.2, 0.3],
    runs=30,
    homogeneous_scoring=False,
    complete_graph=False,
    er_p=0.1,
    T_override=None,
):
    os.makedirs("results", exist_ok=True)
    results = []
    for beta in beta_list:
        run_data = []
        for r in range(runs):
            config = Config(N=50, k=5, beta=beta, seed=r)
            if T_override is not None:
                config.T = int(T_override)
            if complete_graph:
                G = nx.complete_graph(config.N)
            else:
                G = nx.erdos_renyi_graph(config.N, er_p, seed=r)
            consensus = GravitConsensus(config)
            consensus.set_graph(G)
            consensus.p = np.random.dirichlet(np.ones(config.k), config.N)
            if homogeneous_scoring:
                s_mid = float(0.5 * (config.m + config.M))
                s = np.full((config.N, config.k), s_mid, dtype=float)
            else:
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
