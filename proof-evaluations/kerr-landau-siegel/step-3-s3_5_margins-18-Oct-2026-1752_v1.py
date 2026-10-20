"""Step 3, check 6: the margin chain and the two inequalities that carry the proof.

6a. 5/4 < 13/10 < 4/3, and the gaps 1/20 and 1/30.
6b. (9) implies (11), made rigorous for concrete N with exact lattice sums and an exact prime sum:
    since floor(i/p) > i/p - 1, sum_{p in S} E_p log p >= (Sum i) * sum_{p in S} log p / p - r * theta(Q).
    Under (9) the left side of (11) is therefore at least (13/10)(Sum i) log B - r theta(Q).
    We test  (13/10 Sum i - W) log(8 N sqrt3) - r theta(Q) - r log(32 r sqrt N) > 0,
    which covers every 3 <= |q| <= N (that is, every gamma >= 1), since the left side of (11)
    increases with B and the right side increases with |q|.
6c. The order of choices in my derivation C.9: gamma >= 90(C1+2), eps = 1/(160 C1 gamma) makes the
    bracket 1/30 - (1 + C1 + 13/20)/gamma - (16/9) C1 eps gamma at least 1/90 (exact fractions).
6d. log Q - (4/3) log N against -2 log log N.
"""
import math
from fractions import Fraction as Fr
from sympy import primerange

import importlib.util, pathlib
_here = pathlib.Path(__file__).resolve().parent
_src = sorted(_here.glob("*s3_1_lattice_sums*.py"))[-1]   # works with or without the dated file name
spec = importlib.util.spec_from_file_location("ls", _src)
ls = importlib.util.module_from_spec(spec); spec.loader.exec_module(ls)


def theta(Q):
    return sum(math.log(p) for p in primerange(2, int(Q) + 1))


def params(N):
    D = math.floor(0.5 * ((N - 1) / 3) ** (4 / 3))
    Q = D / math.log(N) ** 2
    return D, Q


def check6a():
    print("== 6a. Margin chain")
    a, b, c = Fr(5, 4), Fr(13, 10), Fr(4, 3)
    print(f"   5/4 < 13/10 < 4/3: {a < b < c};  13/10 - 5/4 = {b - a};  4/3 - 13/10 = {c - b}")


def check6b():
    print("\n== 6b. (9) implies (11), rigorous lower bound for the difference, worst case over 3 <= |q| <= N")
    print(f"{'N':>12} {'D':>12} {'Q':>10} {'difference / (W log B)':>24}  holds")
    Ns = sorted([10**k for k in range(2, 8)] + [2 * 10**k for k in range(2, 7)] + [5 * 10**k for k in range(2, 7)])
    for N in Ns:
        D, Q = params(N)
        if Q < 3:
            print(f"{N:>12} {D:>12} {Q:>10.1f} {'(Q < 3: Lemma 1 needs X >= 3)':>24}")
            continue
        r, W, Si, _ = ls.closed(D)
        logB = math.log(8 * N * math.sqrt(3))
        diff = (Fr(13, 10) * Si - W) * Fr(logB) - r * Fr(theta(Q)) - r * Fr(math.log(32 * r * math.sqrt(N)))
        print(f"{N:>12} {D:>12} {Q:>10.1f} {float(diff / (W * Fr(logB))):>24.6f}  {diff > 0}")


def check6c():
    print("\n== 6c. Parameter choices of C.9 close the decisive inequality (exact fractions)")
    for C1 in (Fr(1), Fr(10), Fr(1000), Fr(1, 10)):
        gamma = math.ceil(90 * (C1 + 2))
        eps = Fr(1, 1) / (160 * C1 * gamma)
        bracket = Fr(1, 30) - (1 + C1 + Fr(13, 20)) / gamma - Fr(16, 9) * C1 * eps * gamma
        print(f"   C1 = {str(C1):>5}: gamma = {gamma:>6}, eps = {float(eps):.3e}, bracket = {float(bracket):.6f}, >= 1/90: {bracket >= Fr(1, 90)}")


def check6d():
    print("\n== 6d. log Q versus (4/3) log N - 2 log log N")
    for N in (10**4, 10**6, 10**9, 10**12):
        D, Q = params(N)
        print(f"   N = {N:.0e}: log Q - (4/3)log N = {math.log(Q) - 4 / 3 * math.log(N):8.4f};  -2 log log N = {-2 * math.log(math.log(N)):8.4f}")


if __name__ == "__main__":
    check6a()
    check6b()
    check6c()
    check6d()
