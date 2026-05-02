import numpy as np

class ByzantinePolicy:
    def corrupt(self, K):
        return np.random.dirichlet(np.ones(K))


def is_byzantine(beta):
    return np.random.rand() < beta
