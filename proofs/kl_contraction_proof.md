# KL Contraction Proof

Using three-point identity of negative entropy:

\[
D_{KL}(R(p)\|R(q)) \le D_{KL}(p\|q) - \eta \|p-q\|_1^2
\]

Gossip step:

\[
D_{KL}(Wp \| Wq) \le (1 - \gamma) D_{KL}(p\|q)
\]

Composition:

\[
D_{KL}(T(p)\|T(q)) \le (1 - \gamma\eta) D_{KL}(p\|q)
\]
