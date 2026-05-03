import numpy as np
class Config:
    def __init__(self, N=50, k=5, m=0.1, M=2.0, gamma=0.2, beta=0.1, T=100, seed=42):
        self.N = N
        self.k = k
        self.m = m
        self.M = M
        self.gamma = gamma
        self.beta = beta
        self.T = T
        self.seed = seed
        self.eta = 0.5 * (m / M)**2
        np.random.seed(seed)
