# gravit/theory/lower_bounds.py

"""
Theorem (Convergence Lower Bound)

Let γ be spectral gap of gossip graph.
Let η be likelihood boundedness constant.

Then any distributed Bayesian gossip system requires:

T ≥ Ω( (1 / (γ η)) log(1/ε) )

iterations to reach ε-accuracy.
"""
