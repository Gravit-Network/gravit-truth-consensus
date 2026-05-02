# Gravit Truth Consensus (GTC)

Distributed Bayesian inference system with gossip-based consensus and Byzantine robustness.

## Installation

pip install -r requirements.txt

## Run experiment

python scripts/run_experiment.py

## Generate figures

python scripts/generate_figures.py

## Core idea

We model truth as latent variable h* and perform distributed inference via:
- Bayesian update
- gossip mixing
- adversarial robustness

## Structure

- core/: algorithm
- sim/: simulation
- scripts/: experiments
- math/: metrics
