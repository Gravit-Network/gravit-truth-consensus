# Gravit Truth Consensus (GTC)

A distributed Bayesian consensus framework for robust truth inference under noise and adversarial corruption.

---

## Overview

Gravit Truth Consensus models truth inference as a contractive operator over probability simplices combining:

- Bayesian multiplicative updates
- Gossip-based consensus
- Spectral mixing over communication graphs

We provide:
- theoretical guarantees (uniqueness + convergence)
- adversarial robustness bounds
- real-world dataset evaluation
- baseline comparisons

---

## Installation

```bash
pip install -r requirements.txt
python scripts/run_experiment.py
python scripts/generate_figures.py
python scripts/benchmark.py
python scripts/build_submission.py
