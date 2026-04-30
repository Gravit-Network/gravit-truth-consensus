# Canonical Theorem Set

---

## Theorem 1 — Fixed Point Existence & Uniqueness

For any strategy profile \( s \in [m,M]^{Nk} \), the operator:
\[
T(s)(p) = W \left( \frac{p \odot s}{\langle p, s \rangle} \right)
\]
admits a unique fixed point \( p^*(s) \in \mathrm{int}(\Delta^{k-1}) \).

---

## Theorem 2 — KL Contraction

Let \( \eta = \frac12 (m/M)^2 \). Then:
\[
\Phi(t+1) \le (1 - \gamma \eta)\Phi(t)
\]

---

## Theorem 3 — Byzantine Robustness

If Byzantine fraction \( \beta \) satisfies:
\[
\beta < \frac{\gamma \eta}{2\eta + \gamma}
\]

then:
- system converges to perturbed fixed point \( p^*_\beta \)
- with deviation \( O(\beta) \)

---

## Theorem 4 — Incentive Compatibility

Truthful reporting is the unique dominant-strategy equilibrium.

---

## Theorem 5 — Stability (Leave-One-Out)

\[
\|p^{(-v)} - p^*\|_1 \le \frac{2(M-m)}{m^2 \gamma N}
\]
