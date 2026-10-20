# Evaluation of Kerr, "A simpler proof that there are no Landau–Siegel zeros": Final Report

**Paper evaluated:** Bryce Kerr, "A simpler proof that there are no Landau–Siegel zeros," arXiv:2610.21099v1 [math.NT], 15 October 2026, 6 pages.

**Evaluated for:** Arnoldo Miranda
**Date:** 18 October 2026
**Version:** v1

**Compiled from five working reports** (all in the same folder):

| Step | Content | File |
|---|---|---|
| 1 | Structure and foundation | "Step 1 - Kerr Landau-Siegel proof evaluation Step 1 18 Oct 2026 1708_v1.md" |
| 2 | Line-by-line audit, with derivations that fill the breaks | "Step 2 - Kerr Landau-Siegel proof evaluation Step 2 18 Oct 2026 1746_v1.md" |
| 3 | Machine recomputation, with scripts and output | "Step 3 - Kerr Landau-Siegel proof evaluation Step 3 18 Oct 2026 1752_v1.md" |
| 4 | Citations checked against the originals | "Step 4 - Kerr Landau-Siegel proof evaluation Step 4 18 Oct 2026 1758_v1.md" |
| 5 | Plausibility and context | "Step 5 - Kerr Landau-Siegel proof evaluation Step 5 18 Oct 2026 1805_v1.md" |

---

## Part I. Summary for a general reader

**The problem.** Dirichlet L-functions encode how prime numbers are distributed among residue classes. For about ninety years it has been an open question whether some of them could have a real zero extremely close to s = 1, a so-called Landau–Siegel zero. If such zeros do not exist, many results about primes and about class numbers of quadratic fields could be stated with explicit, computable constants, instead of the ineffective constants that Siegel's theorem of 1935 gives.

**The claim.** On 1 October 2026 a manuscript credited to OpenAI claimed to prove that such zeros do not exist. On 11 October William Banks posted a detailed, explicit version of that argument (arXiv:2610.15483). On 15 October Bryce Kerr posted the paper evaluated here, a shorter proof built on the same core idea.

**The standard used.** A proof must carry the reader from step to step with the reader supplying nothing, judged only by what is on the page. Its foundation (the results it assumes) must be stated up front. A step that is asserted but not carried out is a *break*. A step that is wrong as written is a *false step*, which is worse than a break.

**The verdict.**

1. **As written, the paper is not a complete proof by this standard.**
   - It never states its foundation.
   - It contains **1 false step**: the claim that the field K has degree four fails for one discriminant, q = 8. The repair is trivial, and both earlier write-ups avoid the problem.
   - It contains **32 breaks**: 7 substantive and 25 routine.
   - It has 3 notation defects.
   - It does not handle small conductors, and never names its constant.
2. **Above its unstated foundation, no mathematical error was found.**
   - Every break can be filled. This evaluation filled all of them, labeling that work as the evaluator's, not Kerr's.
   - Every number and identity in the paper was confirmed by machine.
   - Every citation (Masser 1981, Davenport 1980, Milne) supports what it is used for, once the bridging steps are supplied.
3. **The argument passes the standard plausibility tests.**
   - It uses the hypothetical zero in exactly the way a correct proof must. Without the zero the method falls well short of a contradiction.
   - Its uniformity in the conductor comes from the statement of a published theorem whose hypotheses the application meets exactly.
4. **Limits of this evaluation.**
   - Banks's write-up was prepared with Claude, Kerr's paper was prepared with ChatGPT, and this evaluation was done by Claude. The three written proofs share one idea. So none of this replaces review by expert number theorists and transcendence theorists.
   - The only named mathematician found publicly endorsing the argument is Banks.
   - No published refutation was found.

---

## Part II. Verdict by band

**Band 1** means shown in this evaluation or read directly in a named source. **Band 2** means the evaluator's reading, for an expert to check. **Band 3** means heuristic.

| # | Finding | Band |
|---|---|---|
| 1 | The paper states no foundation up front. Fifteen outside results are used (two more are needed only on alternative routes); most are cited only where used, or not at all. | 1 |
| 2 | One false step (FS1, q = 8). | 1 |
| 3 | 32 breaks: 7 substantive, 25 routine. 3 notation defects. | 1 |
| 4 | Every break is fillable. The fills are in Step 2 Part C and Step 4 Sections 1.3, 1.4 and 3.3. | 1 |
| 5 | Every printed number and identity is confirmed by machine. | 1 |
| 6 | Lemma 6 (Masser) is true, and the application meets Masser's Theorem 1 as stated. The lemma as written is broader than the source. | 1 |
| 7 | Lemma 1 is fully supported by Davenport, p. 89. | 1 |
| 8 | The Frobenius congruences are true. Milne supports them only indirectly; Euler's criterion gives them in one line. | 1 |
| 9 | The theorem implies nothing known to be false. The unconditional core cannot produce a contradiction without the zero. | 2 |
| 10 | The constant c is effective in principle. Kerr does not compute it. | 2 |
| 11 | The three write-ups (OpenAI, Banks, Kerr) are not independent confirmations. | 3 |
| 12 | Base rate: claimed solutions to famous problems usually fail. This one has a short argument, a published import, and clean margins. | 3 |

---

## Part III. The argument in brief (Band 1)

Let χ = (q/·), with q a fundamental discriminant, and suppose L(β, χ) = 0 with (1 − β) log|q| < ε.

1. **Prime bias (Lemma 1).** The zero forces Σ_{p≤X, χ(p)=1} (log p)/p ≪ log|q| + (1 − β)(log X)². So almost all of the logarithmic mass of the primes up to |q|^{O(1)} sits on primes with χ(p) = −1.
2. **A rank-4 lattice in C³.** Put K = Q(√q, √2) and O = Z[√q, √2]. Let θ_n = n₁ + n₂√q + n₃√2 + n₄√(2q) for n ∈ {0, …, N − 1}⁴. The points (θ_n, σθ_n, στθ_n) form a rank-4 lattice box in C³.
3. **Frobenius substitution.** For χ(p) = −1, θ_n^p ≡ σθ_n or στθ_n (mod pO). So polynomials built from (x₁^p − x₂) or (x₁^p − x₃) take values divisible by high powers of p (Lemmas 2 and 4).
4. **Pigeonhole (Lemmas 3 and 5).** If the primes with χ(p) = −1 carry enough mass (more than (13/10) log B), there is a nonzero F of weighted degree at most D ≈ ½((N − 1)/3)^{4/3} that vanishes modulo P at every point. A size bound and the field norm then make it vanish exactly.
5. **Zero estimate (Lemmas 6 and 7, from Masser 1981).** No nonzero polynomial of degree below ((N − 1)/3)^{4/3} vanishes on that box, because µ(Γ) ≥ 4/3.
6. **Margin chain.** The pigeonhole needs 5/4. The paper asks for 13/10. The prime mass supplies 4/3. Choosing N = |q|^γ with γ large, then ε small, closes the gap of 1/30.

---

## Part IV. The false step

| | |
|---|---|
| **Statement** | "The field K has degree four and O has Z-basis 1, √q, √2, √(2q)" (page 1). |
| **Failure** | q = 8 is a fundamental discriminant, and √8 = 2√2, so K = Q(√2) has degree 2. Four later claims fail with it: the Z-basis; the count in Lemma 3 (273 distinct coefficients instead of 625 when U = 4); \|O/mO\| = m⁴; and the Q-independence of the coordinates of v (v₁ + 4v₄ = 0). All confirmed by machine (Step 3, check 5). No other q is affected. |
| **Consequence** | None for the theorem: the proof needs \|q\| large anyway. |
| **Repair** | Assume \|q\| > 8. |
| **Note** | The OpenAI manuscript ("except for one fixed quadratic field") and Banks (§1.5, "excluded when q ≥ 9") both avoid this. The false step is new to Kerr. |

---

## Part V. The breaks

**Severity.**
- *Substantive:* real work, a case, or a choice is missing.
- *Routine:* an expert supplies it in a line or two.

**Repairs.** "Repair" points to where this evaluation fills the break. Step 2 Part C is labeled C.n; Step 4 sections are labeled S4.n. All repairs are the evaluator's work.

### V.1 Substantive (7)

| # | Location | What is missing | Repair |
|---|---|---|---|
| B1 | Whole paper | No foundation stated up front. Fifteen outside results are needed, plus two on alternative routes (Part VI). | Part VI of this report |
| B2 | Theorem 1 | Small \|q\| is never handled, and c is never named. Closing this needs L(1, χ) ≠ 0 and the fact that zeros are isolated. | C.11 |
| B4 | Lemma 1 | "a straightforward consequence of [Davenport, (2), p. 89]" is an assignment, not a derivation. The derivation also needs Davenport's unnumbered ζ′/ζ bound on the same page. | C.1; confirmed against the source in S4.2 |
| B20 | Lemma 5 | The asymptotics for r, W and E_p are stated without derivation, and so is their uniformity in p. | C.8; confirmed by machine (Step 3, check 1) |
| B21 | Lemma 5 | "from which (11) follows" is not executed. The 1/20 margin must beat O(D³Q) and the other error terms, with a threshold independent of γ. | C.8; confirmed by machine for N = 200 to 10⁷ (Step 3, check 6b) |
| B26 | Proof of Theorem 1 | The order of quantifiers is inverted: ε appears before γ. | C.9 |
| B28 | Proof of Theorem 1 | The decisive inequality (9), with its 1/30 margin, is not executed. | C.9, with γ ≥ 90(C₁ + 2) and ε = 1/(160C₁γ); arithmetic confirmed in Step 3, check 6c |

### V.2 Routine (25)

| # | Location | What is missing | Repair |
|---|---|---|---|
| B3 | Theorem 1, Lemma 1 | That χ = (q/·) is primitive of conductor \|q\| | Standard fact (F13) |
| B5 | Number fields | The Z-basis of O (for q ≠ 8) | C.2 |
| B6 | Number fields | The embedding K ↪ C, the convention √(2q) := √2√q, and the existence of σ and τ | C.10 |
| B7 | Frobenius congruences | Assigned to Milne, Example 8.19. That example gives the Frobenius element, not the congruence modulo pO. | C.3 (Euler's criterion); S4.3 (four bridging steps) |
| B8 | (3), (4) | The "Hence" is not executed. | C.3 |
| B9 | Lemma 2 | Membership in L_D (where p > 8 is used), the ordering of monomials, and invertibility over O | C.4; confirmed by machine (Step 3, check 3) |
| B10 | Lemma 3 | The norm bound (1 + √2)(1 + √\|q\|) ≤ 8√\|q\| | C.5; the true maximum is 3.81 (Step 3, check 4) |
| B11 | Lemma 3 | Distinct choices give distinct coefficients. | C.5 |
| B12 | Lemma 4 | G ≡ 0 (mod p^{⌊i/p⌋}O) | C.6; confirmed by machine on 22,500 cases |
| B13 | Lemma 4 | k_p ≥ ⌊i/p⌋, the purpose of the hypothesis | C.6 |
| B14 | Lemma 4 | \|O/mO\| = m⁴ | C.6 |
| B15 | Lemma 4 | The Chinese remainder theorem step | C.6 |
| B16 | Lemma 5 | The pigeonhole inequality, with P cancelling | C.7 |
| B17 | Lemma 5 | ‖θ_n‖ ≤ B, and ‖σθ‖ = ‖θ‖ | C.7 |
| B18 | Lemma 5 | ‖F(point)‖ ≤ 2rH | C.7 |
| B19 | Lemma 5 | Integrality and multiplicativity of the norm, and \|N(α)\| ≤ ‖α‖⁴ | C.7 |
| B22 | Lemma 6 | Stated for arbitrary generators, but Masser's Theorem 1 assumes a basis. The equivalence of the two definitions of µ is not shown. Downgraded from substantive in Step 4. | S4.1.3 (µ equivalence); S4.1.4 (generator form, from Masser's Proposition); S4.1.5 (the application has a basis) |
| B23 | Lemma 7 | π injective on Z⁴ | Step 2, A34 |
| B24 | Lemma 7 | W is proper. | Step 2, A35 |
| B25 | Lemma 7 | Γ ∩ L = π(π⁻¹(L) ∩ Z⁴); rank equals dimension; additivity of rank | Step 2, A37 and A38 |
| B27 | Proof of Theorem 1 | Mertens and Lemma 1 combined; primes p ≤ 8 and p \| q | C.9 |
| B29 | Proof of Theorem 1 | F becomes a nonzero complex polynomial of the same degree. | C.10 |
| B30 | Proof of Theorem 1 | π(v) = 0, and the kernel has dimension 1 | C.10; confirmed symbolically (Step 3, check 2a) |
| B31 | Proof of Theorem 1 | Q-independence implies no rational subspace contains ker π. | C.10 |
| B32 | Proof of Theorem 1 | The final degree comparison: (M/3)^µ ≥ (M/3)^{4/3}, D < ((N − 1)/3)^{4/3}, and deg F ≤ D | C.10 |

### V.3 Notation defects (3)

| # | Defect |
|---|---|
| ND1 | c_{i,j,k} is reused for the coordinates in the G basis in Lemma 4. |
| ND2 | "Lattice" is used for a subgroup of Cⁿ that need not be discrete. |
| ND3 | γ is used both for the integer parameter and for the vectors γ₁, …, γ₄. |

---

## Part VI. The foundation the paper needs

Kerr does not list his foundation. This is the full list the argument uses.

| # | Result | Used in | On Kerr's page? |
|---|---|---|---|
| F1 | Davenport, *Multiplicative Number Theory*, 2nd ed., p. 89, Equation (2) | Lemma 1 | Cited |
| F2 | Frobenius congruences in O | (3), (4) | Cited (Milne, Example 8.19), indirectly |
| F3 | Euler's criterion; Kronecker = Legendre for odd p | F2 | Silent |
| F4 | Masser, Invent. Math. 63 (1981), Theorem 1 (p. 82) | Lemma 6 | Cited, without a theorem number |
| F5 | Mertens' estimate | Theorem 1 | Named |
| F6 | Chinese remainder theorem | Lemma 4 | Named |
| F7 | Field and ring facts about K and O: degree, basis, Galois group, norm | Throughout | Asserted or silent |
| F8 | Linear algebra over Q and C | Lemmas 2 and 7; kernel claim | Silent |
| F9 | Binomial theorem modulo p; Fermat | (3), (4) | Silent |
| F10 | Pigeonhole principle | Lemma 5 | Named |
| F11 | Chebyshev bound Σ_{p≤Q} log p ≪ Q | Lemma 5 | Silent |
| F12 | Properties of the embedding norm ‖·‖ | Lemmas 3 and 5 | Silent |
| F13 | (q/·) is primitive of conductor \|q\| | Lemma 1 | Silent |
| F14 | L(1, χ) ≠ 0; zeros of L(s, χ) are isolated | Small q (omitted) | Absent |
| F15 | Davenport, p. 89, the unnumbered bound −ζ′/ζ(σ) < 1/(σ − 1) + c₁ | Lemma 1 | Absent |
| F16 | Masser's Proposition (§2), needed only for Lemma 6's generator form | Lemma 6 as stated | Absent |
| F17 | [O_K : O] divides 32\|q\| (needed only on the Frobenius route) | (3), (4) via Milne | Absent |

---

## Part VII. Citation findings (Band 1)

| Source | Kerr's use | Finding |
|---|---|---|
| **Masser 1981, Theorem 1** (read in full, Sections 1 to 5) | Lemma 6 | **True but over-cited.** Masser assumes a basis; Kerr allows any generators. The two definitions of µ are equivalent (S4.1.3). The generator form is true, by Masser's Proposition plus a rerun of his §5 (S4.1.4), but Masser does not state it. Kerr's application has a basis because rank Γ = 4, so Theorem 1 applies as stated (S4.1.5). The key uniformity, a bound (M/n)^µ with no constant depending on the points, is in Masser's statement. |
| **Davenport 1980, p. 89** (2nd ed.; Arnoldo's images match the 1980 file word for word) | Lemma 1 | **Fully supported.** Equation (2) holds for σ > 1 and any primitive χ, with q ≥ 3 and t ≥ 0 allowed. The unnumbered ζ′/ζ bound, also needed, is on the same page. Davenport keeps a single zero's term himself on p. 90. |
| **Milne, *Algebraic Number Theory*, v3.03, Example 8.19, p. 274** (the "ANTe6" file) | (3), (4) | **Correct in substance, indirect.** Milne gives the Frobenius element (p, K/Q) = (d/p), not a congruence modulo pO. Bridging needs four steps, including [O_K : O] dividing 32\|q\| (S4.3). Euler's criterion does it in one line. Aside: Milne, p. 275 has a typographical error ("−1 if p ≡ 1 mod 4" should read 3 mod 4); it does not affect Kerr. |

---

## Part VIII. Machine checks (Band 1)

Five Python scripts with exact arithmetic, run with Python 3 and sympy 1.14.0. Script names and full output are in the folder, all dated "18 Oct 2026 1752_v1".

| Check | Result |
|---|---|
| r, W, Σ i up to D = 4,000,000 | Leading constants 1/384, 5/6144, 1/1536 confirmed; normalized errors settle at 0.0703, 0.0254, 0.0221 |
| E_p, every prime 11 ≤ p ≤ D, for D up to 20,000 | Error/D³ at most 0.0012: uniform in p |
| Symbolic identities | Point identity, det = 4√(2q), and π(v) = 0 all confirmed |
| Frobenius congruences | 17,496 checked across 20 discriminants, 0 failures |
| Lemma 4 divisibility | 22,500 cases, 0 failures |
| Lemma 2 basis | Unitriangular for p ∈ {11, 13, 17, 19}; fails for p ≤ 8, as the paper's hypothesis requires |
| Lemma 3 constant | Maximum 3.81 < 8 |
| q = 8 | Confirmed on four counts |
| "(9) implies (11)" | Holds at all 15 grid points from N = 200 to 10⁷ |
| Order of choices (C.9) | Bracket ≥ 1/90 for C₁ ∈ {1/10, 1, 10, 1000} |

---

## Part IX. Plausibility and context (Step 5)

1. **No overreach (Band 2).** The algebraic core holds without any zero. It says primes with χ(p) = −1 cannot carry more than about 39/40 of the log-mass up to Q, and in the limit the requirement tends to 15/16.
   - Without a zero they carry about 1/2 (Band 3). Even using split primes as well, which the method could do (checked), the mass reaches only about 3/4.
   - The exponent 4/3 is best possible (Masser, p. 82).
   - So the method needs the zero to reach a contradiction, as a correct argument must.
2. **Genuine L-function needed (Band 1).** The argument uses the Euler product (Davenport) and genuine Frobenius congruences. It cannot be run on Davenport–Heilbronn-type functions.
3. **Effectivity (Band 2).** Every constant in Kerr's argument is computable, but Kerr does not compute c. Banks gives explicit constants for the OpenAI argument: δ₀ = 3.0 × 10⁻³ for q ≥ 10¹⁰. Smaller q rely on a computation by Lu, Zaman and Zhao that Banks says he has not verified.
   - An effective c would give an effective Siegel theorem and effective class number bounds of order √q / log q. The second of these is a standard deduction (Band 2) that I have not checked against a source.
4. **Kerr against OpenAI and Banks (Band 1).** Kerr replaces the interpolation determinant with pigeonhole, and the self-contained interpolation lemma with Masser's theorem. The paper is shorter on the page but rests on a heavier foundation, and it has more breaks than Banks's text.
5. **Relation to the Quasi-Riemann Hypothesis evaluation (Band 2).** That was a separate OpenAI paper of 199 pages, built on Patterson's cubic theta function. This argument does not depend on it. The 7/8 result would imply this one; the converse does not hold.
6. **Outside reaction (Band 3).**
   - Banks is the only named mathematician found publicly endorsing the argument.
   - No refutation was found.
   - Public criticism of OpenAI's 6 October release concerns how it was released, not this proof.

---

## Part X. Questions for the author, in priority order

1. State the foundation up front. State Lemma 6 for a basis, or cite Masser's Proposition for the generator form, and note that rank Γ = 4 supplies the basis (B1, B22).
2. Correct "The field K has degree four" for q = 8, or assume |q| > 8 (FS1).
3. Derive Lemma 1 on the page, including the unnumbered ζ′/ζ bound and the conductor fact (B4, F13, F15).
4. Fix the order of quantifiers (γ, then ε, then q₀) and carry out the inequality with the 1/30 margin (B26, B28).
5. Derive the asymptotics for r, W and E_p, and carry out "(9) implies (11)" (B20, B21).
6. Close the small-|q| case and name c. Say whether c is effective (B2).

---

## Part XI. Sources

**Primary, read in full:**
- B. Kerr, "A simpler proof that there are no Landau–Siegel zeros," [arXiv:2610.21099v1](https://arxiv.org/html/2610.21099v1), 15 October 2026.
- W. D. Banks, "On the OpenAI proof that Landau–Siegel zeros do not exist," [arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1), 11 October 2026.
- OpenAI, "Uniform exclusion of Landau–Siegel zeros," manuscript dated 1 October 2026, 9 pages.
- D. W. Masser, "On polynomials and exponential polynomials in several complex variables," *Inventiones Mathematicae* 63 (1981), 81 to 95. doi:10.1007/BF01389194.
- H. Davenport, *Multiplicative Number Theory*, 2nd edition, revised by H. L. Montgomery, Graduate Texts in Mathematics 74, Springer, 1980, pp. 88 to 90.
- J. S. Milne, *Algebraic Number Theory*, version 3.03 (May 29, 2011), §8, pp. 270 to 275.

**Secondary, read through fetch summaries (Band 3):**
- [VibeMathed, the Landau–Siegel zero problem](https://vibemathed.com/problem/landau-siegel-zeros)
- [36kr](https://eu.36kr.com/en/p/4031090627858820)
- [AHM statement, Terence Tao's blog, 7 October 2026](https://terrytao.wordpress.com/2026/10/07/ahm-statement-on-openais-october-6-release-of-mathematical-documents/)
- [Fortune, 7 October 2026](https://fortune.com/2026/10/07/openai-math-controversy-solutions-370-outstanding-challenges-published-criticisms-celebration/)
- [AI Signal](https://aisignal.day/en/openai-math-722-2026/)
- [J. D. Lichtman on X](https://x.com/jdlichtman/status/2111790096911679634) (search snippet only)

**Could not be read:**
- The arXiv abstract page for 2610.21099 (rate-limited), so no check was possible for a revised version after v1.
- The *Science* article "AI edges closer to solving the Riemann hypothesis" (fetch error).
