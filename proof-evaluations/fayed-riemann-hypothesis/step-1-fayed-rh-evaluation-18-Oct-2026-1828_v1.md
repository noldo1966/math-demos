# Fayed, "A Simple Proof of the Riemann Hypothesis": evaluation, Step 1

**Document evaluated:** Hatem A. Fayed, "A Simple Proof of the Riemann Hypothesis," arXiv:2209.01890**v54** [math.GM], dated 7 October 2026 on the arXiv stamp and 8 October 2026 on the title page, 7 pages. This is the copy Arnoldo attached on 18 October 2026.

**Standard applied:** a proof must carry the reader from step to step with the reader supplying nothing, judged only by what is on the page. A false step is worse than a break.

**Files produced with this report (same folder):**
- "Step 1 - Fayed s1_fayed_lhopital 18 Oct 2026 1828_v1.py" (Python 3 with mpmath, 30-digit precision)
- "Step 1 - Fayed script output 18 Oct 2026 1828_v1.txt"

---

## 1. Verdict

**The paper does not prove the Riemann Hypothesis.** Its conclusion rests on one false step: the use of L'Hôpital's rule in equations (41) to (48).

- The rule's hypothesis fails.
- The quantity the paper analyzes can be computed exactly from the paper's own formulas, and it has the limit 0 for every σ₀. There is no contradiction.
- The step never uses that s₀ is a zero. Applied to an arbitrary complex number s with Re s ≠ ½, it would "prove" a contradiction there too.

Each of these points is enough on its own. The demonstrations follow in Section 3, and Section 4 gives a short version for presentation.

---

## 2. The argument as written

| Step | Equations | Content |
|---|---|---|
| 1 | (11) to (17) | Euler–Maclaurin to order 4. For u not an integer, Σ_{n≤⌊u⌋} n^{−s} = ζ(s) + u^{1−s}/(1−s) − B̄₁(u)/u^s − sB̄₂(u)/(2u^{s+1}) − s(s+1)B̄₃(u)/(6u^{s+2}) + O((1+\|t\|)⁴/u^{σ+3}). |
| 2 | (18) to (33) | Truncated Perron formula with T = u⁸, then the contour shifted to Re z = 1 − σ − η. Result (33): Σ_{n≤⌊u⌋} n^{−s} = (1/2π)∫_{−T}^{T} u^{1−σ−η+iy} ζ(1−η+i(t+y)) / (1−σ−η+iy) dy + u^{1−s}/(1−s) + O(u^{−(4−ε)}). This is valid on the "buffered domain" D, where the fractional part {u} lies in (½ + γ, 1 − γ). |
| 3 | (34), (35) | Combining 1 and 2 gives ζ(s) as the integral plus Bernoulli terms, for s and for 1 − s̄. |
| 4 | (36) to (38) | I(u, s) := u^{s+p}ζ(s) − u^{1−s̄+p}ζ(1−s̄), with 0 < p < 1. If s₀ is a zero, then I(u, s₀) = 0 **for every u**. Written out, I(u, s₀) = u^p·Φ(u) + (2σ₀−1)B̄₂(u)/(2u^{1−p}) + (B̄₃ term) + O(·), where Φ(u) is the integral of the difference of the two integrands. |
| 5 | (39) to (41) | The Bernoulli terms tend to 0, so lim u^pΦ(u) = 0. |
| 6 | (42) to (47) | **The false step.** "By applying Leibniz rule … and L'Hôpital rule," lim u^pΦ(u) = lim Φ(u)/u^{−p} is replaced by lim Φ′(u)/(−p u^{−p−1}). This is evaluated, using (34) and (35), as (1 − 2σ₀)u^p B̄₁(u)/(−p) plus terms tending to 0. |
| 7 | (48) | On D, B̄₁(u) = {u} − ½ ∈ (γ, ½ − γ) is positive. So the expression in 6 tends to −∞ if σ₀ < ½ and to +∞ if σ₀ > ½. That "contradicts" step 5 unless σ₀ = ½. |

---

## 3. The false step in detail

### 3.1 What L'Hôpital's rule requires

**L'Hôpital's rule (u → ∞).** Let f and g be differentiable on an interval (A, ∞), with g′(u) ≠ 0 there, and f(u) → 0 and g(u) → 0. **If** f′(u)/g′(u) → L as u → ∞ (L finite or ±∞), **then** f(u)/g(u) → L.

The proof uses Cauchy's mean value theorem. For A < u < v, f(u)/g(u) is approximated by f′(ξ)/g′(ξ) for some ξ ∈ (u, v), and v is then sent to ∞. The point ξ is not under our control: it can be **any** point beyond u. So the hypothesis must hold for **all** large u, not just along a chosen set.

The rule also gives nothing in reverse. If f/g → 0, f′/g′ need not have a limit at all.

### 3.2 Where the paper violates it

The paper takes f(u) = Φ(u) and g(u) = u^{−p}. It computes f′/g′ only for u in D, the union of the intervals (M + ½ + γ, M + 1 − γ). On D, B̄₁(u) > 0, and the computed ratio has a single sign.

But D does not contain any interval (A, ∞). Between consecutive pieces of D lie the gaps [M + 1 − γ, M + 1 + ½ + γ]. In most of each gap, B̄₁(u) is **negative**, and there the paper's own formula (47) gives the opposite sign.

So f′/g′ has **no limit** as u → ∞. It swings between large positive and large negative values on every unit interval. The hypothesis of L'Hôpital's rule fails, and the rule tells us nothing about lim f/g.

**Why the gaps are covered by the same formula.** The buffer exists only to control the Perron error (24), which contains 1/log(u/⌊u⌋). With T = u⁸, that error stays below the main terms for all u except those within roughly u^{−6} of an integer. So (33) to (35), and therefore (47), hold on most of each gap as well. The script in Section 3.5 confirms this numerically at {u} = 0.2 and 0.4, which lie outside D.

### 3.3 The function the paper is differentiating, computed exactly

Equation (17), applied to s₀ and to 1 − s̄₀, gives the following for every non-integer u. This uses only the paper's own expansion; the derivation is mine.

  u^{s₀}[A(u,s₀) − ζ(s₀)] = −B̄₁(u) − s₀B̄₂(u)/(2u) − s₀(s₀+1)B̄₃(u)/(6u²) + O(u^{−3})

  u^{1−s̄₀}[A(u,1−s̄₀) − ζ(1−s̄₀)] = −B̄₁(u) − (1−s̄₀)B̄₂(u)/(2u) − (1−s̄₀)(2−s̄₀)B̄₃(u)/(6u²) + O(u^{−3})

Here A(u, s) := Σ_{n≤u} n^{−s} − u^{1−s}/(1−s). By (33), A(u, s) is the paper's integral term.

Subtract the second line from the first. The B̄₁ terms cancel, and (1−s̄₀) − s₀ = 1 − 2σ₀. This gives

  **Φ(u) = (1 − 2σ₀)·B̄₂(u)/(2u) + O(u^{−2}).**

(For a zero s₀ the bracketed ζ values are 0, so the left side is exactly Φ.) The two consequences:

- **f/g:** u^pΦ(u) = (1 − 2σ₀)B̄₂(u)u^{p−1}/2 + O(u^{p−2}) → 0, for **every** σ₀, because p < 1 and |B̄₂| ≤ 1/6. This agrees with step 5. There is nothing to contradict.
- **f′/g′:** Since B̄₂′ = 2B̄₁ between integers, Φ′(u) = (1 − 2σ₀)B̄₁(u)/u + O(u^{−2}). Dividing by g′(u) = −p u^{−p−1} gives exactly the paper's (47): (1 − 2σ₀)u^p B̄₁(u)/(−p) + o(1). This oscillates with amplitude growing like u^p.

So the paper's computation in (42) to (47) is **correct as arithmetic**. Its error is the inference in (48). It reads the derivative of an oscillating function, sampled on the half-periods where B̄₁ > 0, as the limit of the function itself.

### 3.4 Proves too much: the zero hypothesis is never used

Steps 6 and 7 use ζ(s₀) = ζ(1−s̄₀) = 0 only to identify Φ with (I − Bernoulli terms)/u^p. The calculation in Section 3.3 holds for **any** complex s once the ζ values are subtracted.

Define Ψ_s(u) := u^s[A(u,s) − ζ(s)] − u^{1−s̄}[A(u,1−s̄) − ζ(1−s̄)]. This is defined for every s, and Ψ_{s₀} = Φ at a zero. Then:

- lim u^pΨ_s(u) = 0, proved directly as above, for every s.
- On D, Ψ_s′/(−p u^{−p−1}) → ∓∞ whenever Re s ≠ ½, by the paper's own (42) to (47).

If the inference in (48) were valid, it would show that Re s = ½ for **every** complex number s, zero or not. That is absurd. So the inference is invalid, independently of any question about the zeros of ζ.

(At Re s = ½ we have 1 − s̄ = s, so Ψ_s ≡ 0 identically. On the critical line the argument is empty.)

### 3.5 Numerical confirmation

The script computes Ψ_s(u) and its exact derivative between integers, using partial sums and mpmath's ζ at 30 digits, with p = ½ and γ = 0.05. Excerpt for s = 0.3 + 14.1347i, which is **not** a zero:

| u | {u} | In D? | f/g = u^pΨ | Predicted (1−2σ)B̄₂u^{p−1}/2 | f′/g′ | Paper's (47) |
|---|---|---|---|---|---|---|
| 1000.2 | 0.2 | no | 4.24 × 10⁻⁵ | 4.22 × 10⁻⁵ | **+7.59** | +7.59 |
| 1000.75 | 0.75 | yes | −1.32 × 10⁻⁴ | −1.32 × 10⁻⁴ | **−6.33** | −6.33 |
| 10000.2 | 0.2 | no | 1.33 × 10⁻⁵ | 1.33 × 10⁻⁵ | **+24.0** | +24.0 |
| 10000.75 | 0.75 | yes | −4.17 × 10⁻⁵ | −4.17 × 10⁻⁵ | **−20.0** | −20.0 |

The small imaginary parts are omitted here; they are in the output file. The table shows three things:

- f/g → 0, and it matches the formula in Section 3.3.
- f′/g′ matches the paper's (47) and **changes sign within each unit interval**, with amplitude growing like √u.
- Inside D alone it heads to −∞, the paper's "contradiction", although s is not a zero.

The run with σ = 0.8 shows the mirror image. At the true zero ½ + 14.1347i, Ψ is identically 0, as noted above.

### 3.6 An elementary counterexample with the same structure

Take f(u) = 0.4·B̄₂(u)/(2u) and g(u) = u^{−1/2}. Then f/g = 0.2·B̄₂(u)u^{−1/2} → 0. But f′/g′ is about +63 at u = 100000.25 and about −63 at u = 100000.75, and it grows without bound. Restricted to {u} ∈ (0.55, 0.95), f′/g′ → −∞. Restricted to {u} ∈ (0.05, 0.45), it → +∞. Neither restriction says anything about lim f/g, which is 0.

This is the paper's step with ζ removed.

---

## 4. Short version for presentation

> In equations (41) to (48) the author writes lim_{u→∞} u^pΦ(u) as a 0/0 limit Φ(u)/u^{−p} and applies L'Hôpital's rule, evaluating the ratio of derivatives only on the "buffered domain" D = ⋃_M (M + ½ + γ, M + 1 − γ). L'Hôpital's rule requires the ratio of derivatives to converge as u → ∞ through **all** large u. It does not. The author's own formula (47) gives that ratio as (1 − 2σ₀)u^pB̄₁(u)/(−p), and B̄₁(u) = {u} − ½ changes sign on every unit interval, so the ratio oscillates between +∞ and −∞. Restricting to D keeps only one sign.
>
> In fact the author's expansions (17), (34) and (35) give Φ(u) = (1 − 2σ₀)B̄₂(u)/(2u) + O(u^{−2}) exactly, so u^pΦ(u) → 0 for every σ₀, and there is no contradiction.
>
> Finally, the argument never uses that s₀ is a zero: the same computation, applied to any complex s with Re s ≠ ½, would "prove" Re s = ½. The step proves too much, and the proof fails.

---

## 5. Other breaks (secondary; none affects the verdict)

| # | Location | Finding |
|---|---|---|
| R1 | Whole paper | No foundation stated up front. The truncated Perron formula (Apostol), the convexity bound (Titchmarsh), and the Euler–Maclaurin formula are cited only where used. |
| R2 | (30), (31), (43) | The convexity bound's implied constant is never shown to be uniform in t₀ and in x. "Similarly for the fourth integral" is an assignment. |
| R3 | (31) | The bound printed is weaker than the computation gives (u^{−6+4η+8ε} against the printed u^{−(4−ε)}), with no comment. Harmless. |
| R4 | (34), (35) | The O(u^{−(4−ε)}) error carried from (33) is dropped from the stated error term. Harmless for large u. |
| R5 | (24) | The buffer's role (keeping log(u/⌊u⌋) away from 0) is never related to the size of T. With T = u⁸ the buffer is almost unnecessary, which is exactly why (47) also holds off D (Section 3.2). |
| R6 | (42) | "The integrand is continuous and continuously differentiable within the buffered domain" is the wrong condition for differentiating under the integral: the limits ±u⁸ depend on u, and differentiability is needed on intervals, not on D. In fact Φ is smooth for all u > 0, but the paper does not say so. |
| R7 | Structure | The argument uses no arithmetic property of ζ: no Euler product, and the functional equation only through the pairing s₀ ↔ 1 − s̄₀. Davenport–Heilbronn-type functions have such pairings and zeros off the line. Section 3.4 already shows the method fails without needing this test. (Band 2) |
| R8 | Context | This is version 54 of the preprint, in the General Mathematics category. The "buffered domain" (10) appears designed to avoid the jumps of B̄₁ at integers; it is the device that hides the sign change. (Band 1 for the version and category; Band 2 for the reading of the buffer's purpose.) |

---

## 6. Method note

To evaluate the paper's integral without integrating up to T = u⁸, the script uses the paper's own equation (33), which identifies that integral with the partial sum minus u^{1−s}/(1−s) up to O(u^{−(4−ε)}). So the numbers test the paper's argument on its own terms.

The demonstration that the step is invalid does not depend on the numerics. Sections 3.1 to 3.4 establish it from the rule's hypothesis and the paper's own formulas.
