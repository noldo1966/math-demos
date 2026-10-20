"""Fayed, arXiv:2209.01890v54: numerical demonstration that the L'Hopital step (eqs. 41-48) fails.

Notation (the paper's, with one name added):
  A(u,s)   = sum_{n<=u} n^{-s} - u^{1-s}/(1-s)
             By the paper's own eq. (33), A(u,s) equals its integral term (1/2pi) * integral(...) up to
             O(u^{-(4-eps)}). So we can compute the paper's integral without evaluating it at T = u^8.
  Psi_s(u) = u^s [A(u,s) - zeta(s)] - u^{1-conj(s)} [A(u,1-conj(s)) - zeta(1-conj(s))]
             If s = s0 is a zero, then zeta(s0) = zeta(1-conj(s0)) = 0 and Psi_{s0}(u) is exactly the
             integral that the paper writes as the numerator in eq. (39): I(u,s0) = u^p * Psi + Bernoulli terms.
             For any other s, Psi_s is the same expression with the zeta values subtracted, and the
             paper's expansions (34), (35) give it the same asymptotics.
  f(u) = Psi_s(u),  g(u) = u^{-p}   (the paper's L'Hopital pair: lim u^p Psi = lim f/g)

What the script shows:
  (1) f/g = u^p Psi_s(u) -> 0 for every s (zero or not), matching (1-2 sigma) B2bar(u) u^{p-1} / 2.
  (2) f'/g' = Psi_s'(u) / (-p u^{-p-1}) matches the paper's eq. (47), (1-2 sigma) u^p B1bar(u)/(-p),
      and OSCILLATES in sign with growing amplitude: +infinity on half of each unit interval,
      -infinity on the other half. Restricted to the paper's 'buffered domain' it has one sign.
  (3) Hence the paper's reasoning, which never uses that s is a zero except to name Psi, would
      'prove' sigma = 1/2 for every complex s: it proves too much.
"""
import mpmath as mp

mp.mp.dps = 30
P = mp.mpf("0.5")          # the paper's p, any 0 < p < 1
GAMMA_BUF = mp.mpf("0.05")   # the paper's buffer gamma


def B1bar(u):
    return u - mp.floor(u) - mp.mpf(1) / 2


def B2bar(u):
    x = u - mp.floor(u)
    return x * x - x + mp.mpf(1) / 6


class Partial:
    """Cache partial sums sum_{n<=m} n^{-s} for the two exponents s and 1-conj(s)."""

    def __init__(self, s, M):
        self.s, self.s2 = s, 1 - mp.conj(s)
        self.S1, self.S2 = [mp.mpc(0)], [mp.mpc(0)]
        a = b = mp.mpc(0)
        for n in range(1, M + 1):
            a += mp.power(n, -self.s)
            b += mp.power(n, -self.s2)
            self.S1.append(a)
            self.S2.append(b)
        self.z1, self.z2 = mp.zeta(self.s), mp.zeta(self.s2)

    def psi(self, u):
        m = int(mp.floor(u))
        s, s2 = self.s, self.s2
        t1 = mp.power(u, s) * (self.S1[m] - self.z1) - u / (1 - s)
        t2 = mp.power(u, s2) * (self.S2[m] - self.z2) - u / (1 - s2)
        return t1 - t2

    def dpsi(self, u):
        # exact derivative between integers (partial sums are constant there)
        m = int(mp.floor(u))
        s, s2 = self.s, self.s2
        d1 = s * mp.power(u, s - 1) * (self.S1[m] - self.z1) - 1 / (1 - s)
        d2 = s2 * mp.power(u, s2 - 1) * (self.S2[m] - self.z2) - 1 / (1 - s2)
        return d1 - d2


def report(label, s, Ms=(100, 1000, 10000)):
    sigma = mp.re(s)
    print(f"\n=== {label}: s = {mp.nstr(s, 12)}   (sigma = {mp.nstr(sigma, 6)}, zeta(s) = {mp.nstr(mp.zeta(s), 6)})")
    pr = Partial(s, max(Ms) + 2)
    print(f"{'u':>12} {'{u}':>6} {'in D?':>6} {'u^p*Psi (=f/g)':>26} {'(1-2sig)B2bar u^(p-1)/2':>26}"
          f" {'f prime/g prime':>26} {'paper eq.(47)':>22}")
    for M in Ms:
        for frac in (mp.mpf("0.20"), mp.mpf("0.40"), mp.mpf("0.75"), mp.mpf("0.90")):
            u = M + frac
            inD = (mp.mpf(1) / 2 + GAMMA_BUF < frac < 1 - GAMMA_BUF)
            fg = mp.power(u, P) * pr.psi(u)
            pred_fg = (1 - 2 * sigma) * B2bar(u) * mp.power(u, P - 1) / 2
            ratio = pr.dpsi(u) / (-P * mp.power(u, -P - 1))
            pred = (1 - 2 * sigma) * mp.power(u, P) * B1bar(u) / (-P)
            print(f"{mp.nstr(u, 8):>12} {mp.nstr(frac, 2):>6} {str(bool(inD)):>6} "
                  f"{mp.nstr(fg, 6):>26} {mp.nstr(pred_fg, 6):>26} {mp.nstr(ratio, 6):>26} {mp.nstr(pred, 6):>22}")


def counterexample():
    print("\n=== Elementary counterexample with the same structure (no zeta at all)")
    print("f(u) = c*B2bar(u)/(2u), g(u) = u^{-p}, c = 1 - 2*sigma = 0.4")
    c = mp.mpf("0.4")
    for M in (10, 1000, 100000):
        for frac in (mp.mpf("0.25"), mp.mpf("0.75")):
            u = M + frac
            fg = c * B2bar(u) / (2 * u) / mp.power(u, -P)
            df = c * (B1bar(u) / u - B2bar(u) / (2 * u * u))
            dg = -P * mp.power(u, -P - 1)
            print(f"   u = {mp.nstr(u, 9):>10}:  f/g = {mp.nstr(fg, 6):>12}   f'/g' = {mp.nstr(df / dg, 6):>12}")


if __name__ == "__main__":
    rho1 = mp.zetazero(1)                      # 0.5 + 14.1347...i, a true zero
    report("True zero (sigma = 1/2)", rho1)
    report("Off the line, NOT a zero (sigma = 0.3)", mp.mpc("0.3", "14.134725141734693790457251983562"))
    report("Off the line, NOT a zero (sigma = 0.8)", mp.mpc("0.8", "21.0"))
    counterexample()
