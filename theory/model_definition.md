# Model Definition

Each agent \( v \) maintains belief \( p_v \in \Delta^{k-1} \).

Update per round:

## Step 1 — Local reweighting
\[
\hat{p}_v = \frac{p_v \odot s_v}{\langle p_v, s_v \rangle}
\]

## Step 2 — Gossip
\[
p_v \leftarrow \sum_u W_{vu} \hat{p}_u
\]

---

## Utility (game-theoretic layer)

\[
u_v = \alpha \mathbb{E}_{p^{(-v)}}[\log s_v(h)] - ck
\]
