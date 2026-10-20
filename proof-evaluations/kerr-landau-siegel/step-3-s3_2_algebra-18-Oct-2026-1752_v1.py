"""Step 3, check 2: the algebra of Kerr's paper.

(a) Symbolic: (theta, sigma theta, sigma tau theta) = sum n_j gamma_j; det(gamma_1,gamma_2,gamma_3)
    = 4 sqrt(2q); pi(v) = 0; rank of pi is 3.
(b) Exact arithmetic in O = Z[sqrt q, sqrt 2] with basis (1, sqrt q, sqrt 2, sqrt q sqrt 2):
    the Frobenius congruences, equations (3) and (4), and the Lemma 4 divisibility
    G_{ijk}(theta, sigma theta, sigma tau theta) = 0 mod p^{floor(i/p)} O.
"""
import random
import sympy as sp
from sympy.functions.combinatorial.numbers import jacobi_symbol
from sympy import primerange

# ---------- (a) symbolic -------------------------------------------------------
a, b = sp.symbols("a b")          # a = sqrt q, b = sqrt 2, sqrt(2q) := a*b
n1, n2, n3, n4 = sp.symbols("n1:5")
theta = n1 + n2 * a + n3 * b + n4 * a * b
sig = {a: -a, b: b}               # sigma
tau = {a: a, b: -b}               # tau
sig_theta = theta.subs(sig, simultaneous=True)
sigtau_theta = theta.subs(tau, simultaneous=True).subs(sig, simultaneous=True)
g1 = sp.Matrix([1, 1, 1])
g2 = sp.Matrix([a, -a, -a])
g3 = sp.Matrix([b, b, -b])
g4 = sp.Matrix([a * b, -a * b, a * b])
lhs = sp.Matrix([theta, sig_theta, sigtau_theta])
rhs = n1 * g1 + n2 * g2 + n3 * g3 + n4 * g4


def symbolic():
    print("== 2a. Symbolic identities (a = sqrt q, b = sqrt 2, sqrt(2q) := ab)")
    print("   sigma tau sends a, b, ab to:",
          [sp.simplify(x.subs(tau, simultaneous=True).subs(sig, simultaneous=True)) for x in (a, b, a * b)])
    print("   (theta, sigma theta, sigma tau theta) - sum n_j gamma_j =", list(sp.expand(lhs - rhs)))
    M3 = sp.Matrix.hstack(g1, g2, g3)
    print("   det(gamma_1, gamma_2, gamma_3) =", sp.factor(M3.det()))
    M = sp.Matrix.hstack(g1, g2, g3, g4)
    v = sp.Matrix([a * b, b, -a, -1])
    print("   pi(v) = M v =", list(sp.expand(M * v)))
    print("   rank of M for a = sqrt(5), b = sqrt(2):", M.subs({a: sp.sqrt(5), b: sp.sqrt(2)}).rank())


# ---------- (b) exact arithmetic in O ------------------------------------------
class O:
    """Element u0 + u1 a + u2 b + u3 ab with a^2 = q, b^2 = 2; coefficients mod m (or exact if m None)."""

    def __init__(self, c, q, m=None):
        self.q, self.m = q, m
        self.c = [x % m for x in c] if m else list(c)

    def __mul__(s, t):
        q = s.q
        x0, x1, x2, x3 = s.c
        y0, y1, y2, y3 = t.c
        c0 = x0 * y0 + q * x1 * y1 + 2 * x2 * y2 + 2 * q * x3 * y3
        c1 = x0 * y1 + x1 * y0 + 2 * (x2 * y3 + x3 * y2)
        c2 = x0 * y2 + x2 * y0 + q * (x1 * y3 + x3 * y1)
        c3 = x0 * y3 + x3 * y0 + x1 * y2 + x2 * y1
        return O([c0, c1, c2, c3], q, s.m)

    def __sub__(s, t):
        return O([x - y for x, y in zip(s.c, t.c)], s.q, s.m)

    def pow(s, e):
        r = O([1, 0, 0, 0], s.q, s.m)
        base = s
        while e:
            if e & 1:
                r = r * base
            base = base * base
            e >>= 1
        return r

    def zero(s):
        return all(x == 0 for x in s.c)


def sigma(c):
    return [c[0], -c[1], c[2], -c[3]]


def sigtau(c):
    return [c[0], -c[1], -c[2], c[3]]


def frobenius(qs, pmax=400, trials=20, seed=1):
    print("\n== 2b. Frobenius congruences mod pO, and equations (3), (4)")
    rnd = random.Random(seed)
    total = fails = 0
    for q in qs:
        for p in primerange(3, pmax):
            if q % p == 0:
                continue
            chi = jacobi_symbol(q % p, p)
            two = jacobi_symbol(2, p)
            sq = O([0, 1, 0, 0], q, p).pow(p)
            s2 = O([0, 0, 1, 0], q, p).pow(p)
            if not (sq - O([0, chi, 0, 0], q, p)).zero() or not (s2 - O([0, 0, two, 0], q, p)).zero():
                fails += 1
            total += 1
            if chi == -1:
                for _ in range(trials):
                    n = [rnd.randrange(0, 10**6) for _ in range(4)]
                    th = O(n, q, p).pow(p)
                    target = sigma(n) if two == 1 else sigtau(n)
                    total += 1
                    if not (th - O(target, q, p)).zero():
                        fails += 1
    print(f"   q in {qs}, odd p < {pmax}, p not dividing q: {total} congruences checked, {fails} failures")


def lemma4_divisibility(qs, D=40):
    print("\n== 2c. Lemma 4: G_ijk(theta, sigma theta, sigma tau theta) = 0 mod p^floor(i/p) O")
    total = fails = 0
    rnd = random.Random(7)
    for q in qs:
        for p in primerange(11, 30):
            if q % p == 0 or jacobi_symbol(q % p, p) != -1:
                continue
            ell = 2 if jacobi_symbol(2, p) == 1 else 3
            for _ in range(5):
                n = [rnd.randrange(0, 50) for _ in range(4)]
                x1 = O(n, q)
                x2 = O(sigma(n), q)
                x3 = O(sigtau(n), q)
                xl = x2 if ell == 2 else x3
                for i in range(0, D + 1):
                    for j in range(0, 3):
                        for k in range(0, 3):
                            if i + 8 * (j + k) > D:
                                continue
                            e, v = divmod(i, p)
                            G = x1.pow(v) * (x1.pow(p) - xl).pow(e) * x2.pow(j) * x3.pow(k)
                            mod = p**e
                            total += 1
                            if any(c % mod for c in G.c):
                                fails += 1
    print(f"   q in {qs}, p in 11..29 with chi(p) = -1, D = {D}: {total} cases, {fails} failures")


if __name__ == "__main__":
    symbolic()
    QS = [-3, -4, 5, -7, -8, 12, 13, -15, 21, -23, 28, -31, 33, 40, -43, 60, -67, 88, 105, -163]
    frobenius(QS)
    lemma4_divisibility([-3, 5, -7, 13, -23, 40])
