import numpy as np
from gravit.math.metrics import kl


class GravitSystem:
    def __init__(self, agents, model, W, K):
        self.agents = agents
        self.model = model
        self.W = W
        self.K = K

        self.likelihood = np.eye(K) * 0.9 + 0.1 / K

    def step(self, h_star):
        N = len(self.agents)
        p_hat = np.zeros((N, self.K))

        for i, agent in enumerate(self.agents):
            obs = agent.observe(self.model, h_star)
            p_hat[i] = agent.update(obs, self.likelihood)

        return self.W @ p_hat
