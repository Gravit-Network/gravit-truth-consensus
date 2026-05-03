import numpy as np
def honest_scoring(p, m=0.1, M=2.0):
    N, k = p.shape
    return np.random.uniform(m, M, (N, k))
