# Gravit Truth Consensus (GTC)

A Byzantine-robust distributed Bayesian inference system based on gossip dynamics and mirror descent.

---

## Overview

GTC is a distributed protocol for recovering latent truth from noisy and adversarial observations across a network of agents.

It combines:
- Bayesian multiplicative updates
- gossip consensus dynamics
- spectral graph mixing
- adversarial robustness modeling

---

## Key Features

- Distributed Bayesian inference
- Byzantine-robust consensus
- Provable exponential convergence
- Network-agnostic gossip dynamics
- Fully reproducible simulation framework

---

## Model

We assume a latent variable:

h* ∈ H

Each agent observes:

o_v ~ P(o | h*)

and maintains belief:

p_v(t) ∈ Δ^{k-1}

---

## Algorithm

1. Local Bayesian update
2. Gossip mixing via stochastic matrix W

---

## Theory

- Exponential convergence in KL divergence
- Contractive operator in probability simplex
- Byzantine robustness bounds

---

## Experiments

- Synthetic truth recovery
- Adversarial robustness testing
- Network topology analysis

---

## Installation

pip install -r requirements.txt

---

## Run experiment

python run_experiment.py

---

## License

Research use only
