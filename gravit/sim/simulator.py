# gravit/sim/simulator.py

import numpy as np
from gravit.core.agent import Agent
from gravit.core.generative import GenerativeModel
from gravit.core.consensus import build_gossip_matrix
from gravit.core.dynamics import GravitSystem
from gravit.math.metrics import kl


def run_simulation(N=50, K=10, beta=0.2, T=50):

    model = GenerativeModel(K)
    W = build_gossip_matrix(N)

    agents = []
    for i in range(N):
        honest = np.random.rand() > beta
        agents.append(Agent(K, honest))

    system = GravitSystem(agents, model, W, K)

    h_star = np.random.randint(K)
    truth = np.zeros(K)
    truth[h_star] = 1

    kl_trace = []

    for _ in range(T):
        P = system.step(h_star)
        avg = np.mean(P, axis=0)
        kl_trace.append(kl(avg, truth))

    return kl_trace
