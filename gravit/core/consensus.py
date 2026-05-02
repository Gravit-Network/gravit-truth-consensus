# gravit/core/consensus.py

import numpy as np


def build_gossip_matrix(N, p=0.3):
    W = np.random.rand(N, N)
    W = (W < p).astype(float)
    np.fill_diagonal(W, 1.0)
    W = W / W.sum(axis=1, keepdims=True)
    return W


def gossip(W, beliefs):
    return W @ beliefs
