# SoCG 2027 rewrite: review of the plan and status of the draft

Draft: `manuscript/socg27/main.tex` (compiled copy: `manuscript/pdf/socg27_main.pdf`).
Status date: 3 October 2026.

## 1. Venue and format

- **SoCG 2026 is closed.** Its paper deadline was 2 December 2025 and the conference took place in 2026. The next possible target is **SoCG 2027** (to be held in Bangalore). Its call had not been posted on 3 October 2026. Expected dates, based on the 2026 cycle: abstract registration around Tue 24 Nov 2026, papers around Tue 1 Dec 2026.
- The draft compiles with `lipics-v2021.cls` (LIPIcs v3.1.3, copied from dagstuhl-publishing/styles) with the `anonymous` option. SoCG uses a wrapper class, `socg-lipics-v2021.cls`, which is distributed with the call. When the 2027 call appears, swap the `\documentclass` line (see the comment at the top of `main.tex`) and recount lines.
- Line count: the main body ends at numbered line 371. That count includes the title, author block, ACM classes and keywords. The limit is 500 lines, and abstract, captions and the table count toward it. About 130 lines are free.

## 2. Assessment of the plan

The plan's strategy holds up. The paper is now about the geometric function Λ_k(n), the privacy machinery is labelled as known, and the promise class is moved to an appendix. I checked each sketched theorem and found no mathematical error. There were four gaps or weaknesses, and the draft fixes each one:

1. **Theorem 1 (reduction) is correct, and its proof is simpler than the sketch.** Subadditivity is not needed. The average Λ_k/k is non-increasing in k (Lemma 8), and that gives both directions directly. The lower-bound constant is 1/(8(1+e)), better than the plan's 1/(12(1+e)). On novelty: per-instance versions of this statement exist. Dong, Fang, Yi, Tao and Machanavajjhala (R2T, SIGMOD 2022) give an LP-truncation mechanism with down-sensitivity instance optimality, and node-DP edge counting is one of their examples. Fang, Dong and Yi (CCS 2022) is similar. The draft therefore labels Theorem 1 "known tools; new form" and does not claim it as new.
2. **The optimal algorithm in Theorem 1 needs the value Λ_k(n), which is unknown for the Euclidean norm.** The plan did not address this. The draft adds Remark 11: any upper bound λ ≥ Λ_k gives error 2λ. Theorem 12 adds an adaptive algorithm that needs no bound and costs a log factor.
3. **Theorem 2 alone would draw the same objection Reviewer C made** ("one application of the incidence bound"). The "open window" is an open problem, not a result. The draft therefore adds two new geometric results:
   - Λ_k(n) and I(n,k), the maximum number of incidences between n points and k unit circles, agree within a factor of 2 when k ≤ n/2 (Theorem 2). So the privacy cost is a classical incidence function.
   - **A classification over all norms on the plane (Theorem 3).** If the unit circle contains a segment, Λ_k = Θ(kn), and the Laplace mechanism is optimal. If the norm is strictly convex, Λ_k = O(n^{2/3}k^{2/3} + n). **For Valtr's norm ‖(x,y)‖ = |y| + √(x²+y²), this bound is attained at every k (new).** The map (x,y) ↦ (x, y + x²/2) sends upper unit arcs to line segments, so the Szemerédi–Trotter grid construction transfers at every aspect ratio. For almost all norms, Λ_k = Θ̃(n) (Alon–Bucić–Sauermann). As a result, the claim that "the Euclidean case is distinguished by arithmetic" is now a theorem, not a slogan.
4. **The quantifier in the 2026 results.** The Sawin and OpenAI bounds hold for *arbitrarily large* n, that is, infinitely many n, not all n. The iff is therefore stated with "infinitely many n". The iff is close to a tautology once Theorem 1 holds, so it sits inside Theorem 5 and is not the headline. The paragraph "What the separation does and does not say" states the small-ε caveat.

The plan's Theorem 4 (pseudo-circles) is folded into Theorem 3(2), with a self-contained proof: Lemma 17 (two translates of a strictly convex curve meet at most twice) plus Székely's crossing-number argument (Lemma 18).

## 3. The ten revisions the reviews require: where each is handled

| # | Revision | Where |
|---|---|---|
| 1 | Surrogate-agnostic statements; KNRS flow primary; g_D = f_D^frac | Lemma 9 and the sentence before Theorem 1; Appendix A (Props 13–14) |
| 2 | New geometric depth | Theorems 2, 3 (Valtr at every k), 5 |
| 3 | Promise class as a conditional result; the saturating family left open | Appendix D, last paragraph |
| 4 | Formal theorems by page 2; overview; provenance labels | Theorem 1 on p. 2; §2; Table 1 |
| 5 | De-jargoning | Banned-word list in the `.tex` header; a sweep found no hits |
| 6 | Breakthrough demoted to a theorem input | Used only in Theorem 5 and in related work |
| 7 | Post-2016 node DP, including arXiv:2602.15802 (local vs central) | §1 related work |
| 8 | Annulus: t ≤ r, and the t²/Δ² term otherwise | Appendix E (unified bound plus a necessity example); also now private on *all* inputs via g_D |
| 9 | Scoped optimality claims | Theorem 1 holds for all ε ∈ (0,1]; the promise class has its own range (App. D) |
| 10 | The 1/ε improvement in the abstract | Abstract, sentence 6 |

## 4. Verification done

- Every proof in the draft was re-derived by hand; see §2 for the constants.
- `notes/socg27_sanity_checks.py` checks four things numerically: the fractional bias lemma, top-k averaging, the tail ≤ max_j(Λ_j − jD) bound on random graphs, the exact incidence count A²B² of the Valtr construction (in rational arithmetic and in floating point), and that two translates of Valtr's unit circle cross at most twice.
- `latexmk -pdf` builds with no undefined references, citations or overfull boxes.
- Literature checks, via web search on 3 Oct 2026:
  - Sawin (arXiv:2605.20579): more than n^{1.014} unit distances for arbitrarily large n.
  - Alon et al. (arXiv:2605.20695): a sequence of sizes tending to infinity.
  - Alon–Bucić–Sauermann (arXiv:2302.09058): at most (d/2)·n·log₂ n for almost all norms on ℝ^d.
  - Valtr's norm and Ω(n^{4/3}) appear in Swanepoel's survey (arXiv:1702.00066).
  - arXiv:2602.15802 is "Local Node Differential Privacy" by Raskhodnikova, Smith, Wagaman and Zavyalov.
  - R2T (SIGMOD 2022) exists with the cited authors.

## 5. Still to do (authors)

1. **Writing protocol, item 1.** This draft was written with an AI assistant. The plan requires the authors to rewrite every main-body sentence themselves and to make a truthful AI-use statement if the 2027 call asks for one. There is a TODO at the top of `main.tex`.
2. Check these against the sources:
   - the constants in RS16 Theorem 1.4 (Appendix B uses 4D·log(2K/β)/ε₁);
   - the exact form of Székely's crossing lemma for multigraphs;
   - the exact ABS statement for d = 2;
   - Zahl's exponent 295/197;
   - the reference for Erdős's n^{4/3}·log log n lower bound in ℝ³ (currently cited through Brass–Moser–Pach);
   - the bibliographic details of R2T and Zahl (pages and DOI were left out rather than guessed).
3. Literature search: is the bichromatic unit-distance function I(n,k) studied anywhere for √n ≪ k ≪ n? The draft says "we are not aware". Also check whether the Valtr extension to all k is already known; the draft labels it "new; extends Valtr".
4. Independent check of Theorem 3(3) and Lemma 17 by a co-author (plan Week 5).
5. Optional, if lines allow: Fig. 3 from the plan (the lower-bound path). Also optional: the finite top-k degree sums of the Sawin/Emmerich certificates.
6. A cold read by a computational geometer outside the project.
7. Prepare the arXiv full version. The final SoCG version may not contain an appendix.

## 6. Open research directions that would strengthen the paper

- Narrow the Euclidean window. Any upper bound below n^{2/3}k^{2/3} for some k < n must use Euclidean structure, because of Valtr's norm. Any lower bound above max{n, k·u(n)/n} needs unit circles that are richer than average.
- The instance-wise version (local minimax). This is developed in `manuscript/local_minimax_working.tex` and belongs in the full version or a follow-up paper.
