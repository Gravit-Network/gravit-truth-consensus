# gravit/datasets/wiki_consensus.py

import numpy as np


class WikiConsensusDataset:
    """
    Models disagreement in knowledge graphs / wiki edits:
    - multiple conflicting sources
    - latent canonical truth
    """

    def __init__(self, N_nodes=500, K=10):
        self.N = N_nodes
        self.K = K

        self.truth = np.random.randint(K, size=N_nodes)

    def corrupt_sources(self, beta=0.2):
        sources = []

        for _ in range(5):
            s = self.truth.copy()

            mask = np.random.rand(self.N) < beta
            s[mask] = np.random.randint(0, self.K, mask.sum())

            sources.append(s)

        return np.array(sources), self.truth
