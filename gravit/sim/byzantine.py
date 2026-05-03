import numpy as np
def apply_byzantine(s, beta, strategy="constant", p_current=None):
    N, k = s.shape
    byz = np.random.rand(N) < beta
    if strategy == "constant":
        s[byz] = np.random.uniform(0.5, 1.5, (byz.sum(), k))
    return s
