import numpy as np
from gravit.core.agents import Agent
from gravit.core.consensus import build_stochastic_matrix
from gravit.core.dynamics import GravitSystem
from gravit.core.generative_model import GenerativeModel
from gravit.math.metrics import kl

np.random.seed(42)

def run(N=50, K=10, beta=0.2, T=50):

    model = GenerativeModel(K)
    W = build_stochastic_matrix(N)

    agents = []
    for i in range(N):
        honest = np.random.rand() > beta
        agents.append(Agent(K, honest))

    system = GravitSystem(agents, model, W, K)

    h_star = np.random.randint(K)
    truth = np.zeros(K)
    truth[h_star] = 1

    kl_trace = []

    for t in range(T):
        P = system.step(h_star)
        avg = np.mean(P, axis=0)

        kl_trace.append(kl(avg, truth))

    return kl_trace
