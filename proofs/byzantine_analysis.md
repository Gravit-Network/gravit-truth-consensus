# Byzantine Analysis

Let fraction of Byzantine nodes be \( \beta \).

Perturbation bound:
\[
\|\delta\|_1 \le 2\beta \frac{M-m}{m^2}
\]

Lyapunov recursion:
\[
\Phi(t+1) \le (1 - \gamma\eta)\Phi(t) + O(\beta)
\]

Threshold:
\[
\beta < \frac{\gamma\eta}{2\eta + \gamma}
\]
