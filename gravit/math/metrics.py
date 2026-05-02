import numpy as np

def kl(p, q):
    p = np.clip(p, 1e-12, None)
    q = np.clip(q, 1e-12, None)
    return np.sum(p * np.log(p / q))
