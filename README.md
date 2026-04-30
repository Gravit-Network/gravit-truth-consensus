# Gravit Truth Consensus System

A mathematical framework for decentralized consensus under strategic and adversarial conditions.

The system combines:
- entropy-based belief updates (KL geometry)
- gossip diffusion over graphs
- strictly proper scoring incentives
- robustness against Byzantine agents

---

## Core Idea

Each agent maintains a probability distribution over hypotheses.
Updates occur via two coupled mechanisms:

1. Local reweighting (Bayesian-style scoring update)
2. Gossip averaging over a communication graph

This induces a global nonlinear dynamical system with a unique fixed point under mild conditions.

---

## Main Results

### 1. Existence and Uniqueness
There exists a unique fixed point \( p^*(s) \in \mathrm{int}(\Delta^{k-1}) \).

### 2. Contraction
The system is contractive in KL divergence:
\[
\Phi(t+1) \le (1 - \gamma \eta)\Phi(t)
\]

### 3. Byzantine Robustness
For Byzantine fraction \( \beta \), the system converges if:
\[
\beta < \frac{\gamma \eta}{2\eta + \gamma}
\]

### 4. Incentive Compatibility
Truthful reporting is the unique dominant-strategy equilibrium under strictly proper logarithmic scoring.

### 5. Stability
Leave-one-out perturbations scale as:
\[
\|p^{(-v)} - p^*\|_1 = O(1/N)
\]

---

## Important Note

All convergence guarantees are proven entirely in KL geometry.

Hilbert-metric strengthening is not required for the main results.

---

## Simulation

Run:
```bash
cd simulations
pip install -r requirements.txt
python simulate.py
