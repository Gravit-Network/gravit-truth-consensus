import numpy as np
from core.gravit_engine import GravitEngine

class MarketState:
    def __init__(self, N: int, k: int):
        self.engine = GravitEngine(N, k)
        self.capitals = np.full(N, 1000.0)
        self.agents = {}
        self.signals = None
        self.history = []

    def register_agent(self, agent_id: int):
        idx = len(self.agents)
        self.agents[agent_id] = idx
        self.capitals[idx] = 1000.0

    def submit_signal(self, agent_id: int, signal: np.ndarray):
        idx = self.agents[agent_id]
        if self.signals is None:
            self.signals = np.zeros((self.engine.N, self.engine.k))
        self.signals[idx] = signal

    def execute_round(self):
        if self.signals is None:
            raise ValueError("No signals")
        p_star = self.engine.run_round(self.signals)
        self.history.append(p_star.copy())
        return p_star

    def settle(self, realized_h: int):
        rewards = np.log(self.signals[:, realized_h] + 1e-12)
        self.capitals += rewards * self.capitals / len(self.agents)
        return self.capitals
