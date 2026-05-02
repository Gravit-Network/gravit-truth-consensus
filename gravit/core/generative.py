# gravit/core/generative.py

import numpy as np


class GenerativeModel:
    def __init__(self, K, noise=0.1):
        self.K = K
        self.noise = noise

    def sample_observation(self, h_star):
        base = np.eye(self.K)[h_star]
        noise = np.ones(self.K) / self.K
        probs = (1 - self.noise) * base + self.noise * noise
        return np.random.choice(self.K, p=probs)
