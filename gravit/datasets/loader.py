# gravit/datasets/loader.py

from gravit.datasets.crowdsourced_labels import CrowdSourcedDataset
from gravit.datasets.wiki_consensus import WikiConsensusDataset


def load_dataset(name):

    if name == "crowd":
        return CrowdSourcedDataset()

    if name == "wiki":
        return WikiConsensusDataset()

    raise ValueError("Unknown dataset")
