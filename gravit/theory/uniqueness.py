# gravit/theory/uniqueness.py

"""
Theorem (Uniqueness of Contractive Bayesian Gossip Operator)

Let T be an operator over belief states such that:

1. T is permutation invariant over agents
2. T preserves simplex constraints
3. T is contractive in KL-divergence
4. T is locally decomposable over observations
5. T is linear in mixing step

Then T is equivalent (up to scaling) to:

T = W ∘ R

where:
- R is multiplicative Bayesian update
- W is doubly stochastic gossip matrix
"""
