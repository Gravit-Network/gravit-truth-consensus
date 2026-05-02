import numpy as np

class GenerativeModel:
    def __init__(self, K, noise=0.1):
        self.K = K
        self.noise = noise
        self.P = self._build_matrix()

    def _build_matrix(self):
        P = np.eye(self.K) * (1 - self.noise)
        P += self.noise / self.K
        return P

    def sample(self, h_star):
        return np.random.choice(self.K, p=self.P[h_star])
