# gravit/benchmarks/stress_tests.py

import numpy as np


class AdversarialStress:

    def __init__(self, mode="random"):
        self.mode = mode

    def corrupt(self, K):
        if self.mode == "random":
            return np.random.dirichlet(np.ones(K))

        if self.mode == "targeted":
            v = np.zeros(K)
            v[np.random.randint(K)] = 1
            return v

        if self.mode == "collusion":
            base = np.ones(K) / K
            noise = np.random.normal(0, 0.1, K)
            return base + noise
