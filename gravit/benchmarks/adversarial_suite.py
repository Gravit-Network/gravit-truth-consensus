# gravit/benchmarks/adversarial_suite.py

import numpy as np


class AdversarySuite:

    def __init__(self, K):
        self.K = K

    def random_attack(self):
        return np.random.dirichlet(np.ones(self.K))

    def targeted_attack(self, target):
        v = np.zeros(self.K)
        v[target] = 1.0
        return v

    def collusion_attack(self, n=5):
        base = np.ones(self.K) / self.K
        noise = np.random.normal(0, 0.05, self.K)
        return base + noise

def inject_adversaries(beliefs, beta, suite):

    N = len(beliefs)

    for i in range(N):
        if np.random.rand() < beta:
            beliefs[i] = suite.random_attack()

    return beliefs

def adversarial_stress_test(system, beta, T=50):

    suite = AdversarySuite(system.K)

    h_star = np.random.randint(system.K)

    history = []

    for t in range(T):

        P = system.step(h_star)
        P = inject_adversaries(P, beta, suite)

        avg = np.mean(P, axis=0)
        history.append(avg)

    return history

