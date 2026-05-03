import numpy as np

class Agent:
    def __init__(self, agent_id: int, capital: float):
        self.id = agent_id
        self.capital = capital

    def produce_signal(self, private_info: np.ndarray) -> np.ndarray:
        return np.clip(private_info, 0.1, 2.0)
