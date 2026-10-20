"""Step 3, check 1: the lattice sums r, W, Sum i, E_p of Kerr's Lemma 5.

Index set R_D = {(i,j,k) >= 0 : i + 8(j+k) <= D}.
Kerr states: r = D^3/384 + O(D^2), W = 5D^4/6144 + O(D^3), E_p = D^4/(1536p) + O(D^3)
uniformly in p. All arithmetic below is exact (Python integers and Fractions).
"""
from fractions import Fraction as Fr


def brute(D, p=None):
    r = W = Si = Ep = 0
    for j in range(D // 8 + 1):
        for k in range(D // 8 + 1 - j):
            for i in range(D - 8 * (j + k) + 1):
                r += 1
                W += i + j + k
                Si += i
                if p:
                    Ep += i // p
    return r, W, Si, Ep


def T(n):  # 0 + 1 + ... + n
    return n * (n + 1) // 2


def floor_sum(n, p):  # sum_{i=0}^{n} floor(i/p)
    a = n // p
    return p * a * (a - 1) // 2 + a * (n - a * p + 1)


def closed(D, p=None):
    r = W = Si = Ep = 0
    for s in range(D // 8 + 1):
        n = D - 8 * s          # i runs over 0..n
        mult = s + 1           # number of (j,k) with j+k = s
        r += mult * (n + 1)
        Si += mult * T(n)
        W += mult * (T(n) + s * (n + 1))
        if p:
            Ep += mult * floor_sum(n, p)
    return r, W, Si, Ep


def main():
    print("== 1a. Closed-form sums agree with brute-force enumeration")
    ok = True
    for D in range(0, 90):
        for p in (11, 13, 17, 29, 97):
            if closed(D, p) != brute(D, p):
                ok = False
                print("MISMATCH", D, p)
    print("   D = 0..89, p in {11,13,17,29,97}:", "all agree" if ok else "FAILED")

    print("\n== 1b. Normalized errors (should stay bounded if Kerr's O-terms are right)")
    print(f"{'D':>9} {'(r-D^3/384)/D^2':>18} {'(W-5D^4/6144)/D^3':>20} {'(Si-D^4/1536)/D^3':>20}")
    for D in (100, 1000, 10_000, 100_000, 1_000_000, 4_000_000):
        r, W, Si, _ = closed(D)
        er = Fr(r) - Fr(D**3, 384)
        eW = Fr(W) - Fr(5 * D**4, 6144)
        eS = Fr(Si) - Fr(D**4, 1536)
        print(f"{D:>9} {float(er / D**2):>18.6f} {float(eW / D**3):>20.6f} {float(eS / D**3):>20.6f}")

    print("\n== 1c. E_p: max over primes p <= D of |E_p - D^4/(1536 p)| / D^3  (uniformity in p)")
    from sympy import primerange
    for D in (500, 2000, 8000, 20000):
        worst = Fr(0)
        wp = None
        for p in primerange(11, D + 1):
            _, _, _, Ep = closed(D, p)
            e = abs(Fr(Ep) - Fr(D**4, 1536 * p)) / D**3
            if e > worst:
                worst, wp = e, p
        print(f"   D = {D:>6}: max normalized error {float(worst):.6f} (at p = {wp})")

    print("\n== 1d. Leading-constant ratios used in the margin chain")
    print("   (5/6144)/(1/1536) =", Fr(5, 6144) / Fr(1, 1536))


if __name__ == "__main__":
    main()
