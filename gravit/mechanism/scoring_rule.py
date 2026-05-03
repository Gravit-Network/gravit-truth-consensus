import numpy as np

def log_scoring_reward(s_v: np.ndarray, realized_h: int) -> float:
    return np.log(s_v[realized_h] + 1e-12)
