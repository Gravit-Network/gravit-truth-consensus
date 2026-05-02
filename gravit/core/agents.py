import numpy as np

def normalize(x):
    x = np.clip(x, 1e-12, None)
    return x / np.sum(x)


class Agent:
    def __init__(self, K, honest=True):
        self.K = K
        self.honest = honest
        self.belief = np.ones(K) / K

    def observe(self, model, h_star):
        if self.honest:
            return model.sample(h_star)
        else:
            return np.random.randint(self.K)

    def update(self, obs, likelihood):
        self.belief = normalize(self.belief * likelihood[obs])
        return self.belief
