import numpy as np

class LMSRMarketMaker:
    def __init__(self, b: float = 100.0):
        self.b = b
        self.q = None

    def initialize(self, k: int):
        self.q = np.zeros(k)

    def cost(self, q_new: np.ndarray) -> float:
        return self.b * np.log(np.sum(np.exp(q_new / self.b)))

    def price(self, h: int) -> float:
        if self.q is None:
            return 1.0 / self.q.shape[0]
        exp_q = np.exp(self.q / self.b)
        return exp_q[h] / np.sum(exp_q)

    def trade(self, delta_q: np.ndarray):
        self.q += delta_q

    def get_prices(self) -> np.ndarray:
        exp_q = np.exp(self.q / self.b)
        return exp_q / np.sum(exp_q)
