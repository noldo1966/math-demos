"""Step 3, checks 4 and 5.
4. Lemma 3 / Lemma 5 constant: (1 + sqrt 2)(1 + sqrt|q|) < 8 sqrt|q| for all |q| >= 3.
5. The q = 8 failure (false step FS1): K = Q(sqrt 8, sqrt 2) has degree 2, the four 'basis' elements
   are dependent over Q, Lemma 3's count fails, and v has rationally dependent coordinates.
"""
import math
import sympy as sp


def check4():
    print("== 4. Norm constant c(|q|) = (1+sqrt2)(1+sqrt|q|)/sqrt|q|  (needs < 8)")
    f = lambda x: (1 + math.sqrt(2)) * (1 + math.sqrt(x)) / math.sqrt(x)
    for x in (3, 4, 5, 8, 100, 10**6):
        print(f"   |q| = {x:>7}: c = {f(x):.6f}")
    x = sp.symbols("x", positive=True)
    fx = (1 + sp.sqrt(2)) * (1 + sp.sqrt(x)) / sp.sqrt(x)
    print("   derivative sign:", sp.simplify(sp.diff(fx, x)), "(negative, so the maximum is at |q| = 3)")
    print("   exact value at 3:", sp.nsimplify(fx.subs(x, 3)), "=", float(fx.subs(x, 3)))


def check5():
    print("\n== 5. q = 8")
    s8 = sp.sqrt(8)
    print("   sqrt(8) =", s8, "; lies in Q(sqrt 2), so [K:Q] =",
          sp.degree(sp.minimal_polynomial(sp.sqrt(2) + s8, sp.Symbol('t'))), "(primitive element sqrt2 + sqrt8 has degree 2)")
    basis = [1, s8, sp.sqrt(2), sp.sqrt(2) * s8]
    print("   'basis' 1, sqrt q, sqrt 2, sqrt q sqrt 2 =", basis)
    # coordinates in the Q-basis (1, sqrt 2)
    M = sp.Matrix([[1, 0], [0, 2], [0, 1], [4, 0]])
    print("   coordinates in (1, sqrt2):", M.tolist(), "-> rank", M.rank(), "(not 4)")
    print("   relation: 1*sqrt(q)sqrt(2) - 4*1 =", sp.simplify(basis[3] - 4 * basis[0]),
          "; sqrt q - 2 sqrt 2 =", sp.simplify(basis[1] - 2 * basis[2]))
    # Lemma 3 collision: distinct (u1..u4) giving the same coefficient
    u, w = (4, 0, 0, 0), (0, 0, 0, 1)
    cu = sum(ui * bi for ui, bi in zip(u, basis))
    cw = sum(wi * bi for wi, bi in zip(w, basis))
    print("   Lemma 3 collision: u =", u, "and u' =", w, "give c =", sp.simplify(cu), "and", sp.simplify(cw))
    # the count with U = 4: number of distinct c versus (U+1)^4
    U = 4
    vals = set()
    for u0 in range(U + 1):
        for u1 in range(U + 1):
            for u2 in range(U + 1):
                for u3 in range(U + 1):
                    vals.add((u0 + 4 * u3, 2 * u1 + u2))   # coordinates in (1, sqrt 2)
    print(f"   with 0 <= u_t <= {U}: {len(vals)} distinct coefficients, versus (U+1)^4 = {(U + 1) ** 4} claimed")
    v = [sp.sqrt(2) * s8, sp.sqrt(2), -s8, -1]
    print("   v =", [sp.simplify(t) for t in v], "; rational relation v1 + 4 v4 =", sp.simplify(v[0] + 4 * v[3]))


if __name__ == "__main__":
    check4()
    check5()
