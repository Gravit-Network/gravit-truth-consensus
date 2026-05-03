import numpy as np
from .operator import T
from .metrics import compute_phi

class GravitConsensus:
    def __init__(self, config):
        self.config = config
        self.W = None
        self.p = None

    def set_graph(self, G):
        self.W = get_metropolis_hastings_W(G)

    def run_round(self, s):
        self.p = T(self.p, s, self.W)
        return self.p

    def run_until_convergence(self, s, tol=1e-8):
        history = []
        for _ in range(self.config.T):
            self.run_round(s)
            p_star = self.p.mean(axis=0)
            phi = compute_phi(self.p, p_star)
            history.append(phi)
            if phi < tol:
                break
        return self.p.mean(axis=0), history
