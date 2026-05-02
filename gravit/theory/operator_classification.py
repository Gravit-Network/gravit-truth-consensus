# gravit/theory/operator_classification.py

"""
Theorem (Classification of Distributed Inference Operators)

All stable distributed belief update rules over simplex that satisfy:

- Markov consistency
- permutation invariance
- KL contraction
- locality

belong to the family:

T = W ∘ R_φ

where R_φ is exponential-family mirror descent update.
"""
