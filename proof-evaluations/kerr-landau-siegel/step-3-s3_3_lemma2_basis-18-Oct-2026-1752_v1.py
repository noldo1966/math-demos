"""Step 3, check 3: Kerr's Lemma 2. For p > 8 and ell in {2,3}, the polynomials
G_{ijk} = x1^v (x1^p - x_ell)^e x2^j x3^k (i = p e + v, 0 <= v < p) lie in L_D and the change of
basis from monomials is unitriangular when monomials are ordered by decreasing x1 exponent.
Also shows what goes wrong for p <= 8.
"""
from math import comb


def index_set(D):
    return [(i, j, k) for j in range(D // 8 + 1) for k in range(D // 8 + 1 - j)
            for i in range(D - 8 * (j + k) + 1)]


def expand_G(i, j, k, p, ell):
    e, v = divmod(i, p)
    out = {}
    for t in range(e + 1):
        mono = [v + p * (e - t), j, k]
        mono[ell - 1] += t
        out[tuple(mono)] = out.get(tuple(mono), 0) + comb(e, t) * (-1) ** t
    return out


def check(D, p, ell):
    idx = index_set(D)
    S = set(idx)
    outside = 0
    tri_ok = True
    for (i, j, k) in idx:
        G = expand_G(i, j, k, p, ell)
        for mono, c in G.items():
            if mono not in S:
                outside += 1
            elif mono != (i, j, k) and not mono[0] < i:
                tri_ok = False
        if G.get((i, j, k)) != 1:
            tri_ok = False
    return len(idx), outside, tri_ok


if __name__ == "__main__":
    print("== 3. Lemma 2: membership in L_D and unitriangularity")
    for p in (11, 13, 17, 19):
        for ell in (2, 3):
            for D in (20, 50, 100, 160):
                r, outside, tri = check(D, p, ell)
                print(f"   p={p:>2} ell={ell} D={D:>3}: r={r:>6}, monomials outside L_D: {outside}, unitriangular: {tri}")
    print("\n   Control: p <= 8 (Kerr requires p > 8)")
    for p in (3, 5, 7):
        r, outside, tri = check(60, p, 2)
        print(f"   p={p} ell=2 D=60: monomials outside L_D: {outside}")
