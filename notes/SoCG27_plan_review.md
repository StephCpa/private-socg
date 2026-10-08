# SoCG 2027 rewrite: review of the plan and status of the draft

Draft: `manuscript/socg27/main.tex` (compiled copy: `manuscript/pdf/socg27_main.pdf`).
Status date: 7 October 2026.

## 1. Venue and format

- **SoCG 2026 is closed.** Its paper deadline was 2 December 2025 and the conference took place in 2026. The next possible target is **SoCG 2027** (to be held in Bangalore). Its call had not been posted on 3 October 2026. Expected dates, based on the 2026 cycle: abstract registration around Tue 24 Nov 2026, papers around Tue 1 Dec 2026.
- The draft compiles with `lipics-v2021.cls` (LIPIcs v3.1.3, copied from dagstuhl-publishing/styles) with the `anonymous` option. SoCG uses a wrapper class, `socg-lipics-v2021.cls`, which is distributed with the call. When the 2027 call appears, swap the `\documentclass` line and recount lines.
- Line count (after the 3 Oct verification pass): the main body ends at numbered line 408. Front matter (title, author block, ACM classes, keywords, DOI) takes about 8 of those lines. With `lipics-v2021.cls`, captions and table rows carry no line numbers; they add about 18 lines (Fig. 1 caption 3, Fig. 2 caption 4, Table 1 with caption 11). A SoCG-style count is therefore about 418 lines, against a limit of 500. Recount with `socg-lipics-v2021.cls` (v0.9) once the call is out; the class could not be downloaded from this environment.

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
  - R2T (SIGMOD 2022) exists with the cited authors, pages 759--772, and DOI 10.1145/3514221.3517844.

## 5. Still to do (authors)

1. **Writing protocol, item 1.** This draft was written with AI assistance. The manuscript now contains a visible disclosure describing the tools, purposes, and extent of author review. The authors should still confirm that the wording accurately reflects their own process before submission.
2. Check these against the sources:
   - the constants in the generalized exponential mechanism (Appendix B uses 4D·log(2K/β)/ε₁);
   - the exact form of Székely's crossing lemma for multigraphs;
   - the exact ABS statement for d = 2;
   - Zahl's exponent 295/197;
   - the reference for Erdős's n^{4/3}·log log n lower bound in ℝ³ (currently cited through Brass–Moser–Pach);
   - the bibliographic details of Zahl and the reference for the three-dimensional lower bound.
3. Literature search: is the bichromatic unit-distance function I(n,k) studied anywhere for √n ≪ k ≪ n? The draft says "we are not aware". Also check whether the Valtr extension to all k is already known; the draft labels it "new; extends Valtr".
4. Independent check of Theorem 3(3) and Lemma 17 by a co-author (plan Week 5).
5. Optional, if lines allow: Fig. 3 from the plan (the lower-bound path). Also optional: the finite top-k degree sums of the Sawin/Emmerich certificates.
6. A cold read by a computational geometer outside the project.
7. Prepare the arXiv full version. The final SoCG version may not contain an appendix.

## 6. Open research directions that would strengthen the paper

- Narrow the Euclidean window. Any upper bound below n^{2/3}k^{2/3} for some k < n must use Euclidean structure, because of Valtr's norm. Any lower bound above max{n, k·u(n)/n} needs unit circles that are richer than average.
- The instance-wise version (local minimax). This is developed in `manuscript/local_minimax_working.tex` and belongs in the full version or a follow-up paper.


## 7. Verification pass on the authors' five items (3 Oct 2026)

**1. Definition of Λ_k(n), centres, distinct circles, constants.** *Done in the draft.*
- Λ_k(n) sums the k largest degrees in G(P) over sets of at most n distinct points. The centres are therefore points of P.
- I(n,k) maximizes the number of pairs (b, r) ∈ B × R at unit distance. Here |B| ≤ n, and R is a set of exactly k centres anywhere in the plane, so the circles r + S are automatically distinct. B and R may intersect.
- Theorem 2 now states the full sandwich: max{n−1, 2k·u(n)/n, I(n−k, k)} ≤ Λ_k(n) ≤ I(n, k), and I(n, k) ≤ 2Λ_k(n) for k ≤ n/2. The constant 2 comes from splitting B into halves.

**2. Valtr construction.** *Done in the draft.*
- New Lemma 12 (Valtr grid) gives explicit coordinates for the 2A²B points p_ij and the AB² centres c_st.
- The lemma proves that ‖p_ij − c_st‖_V = 1 **if and only if** j = si + t. Hence there are *exactly* A²B² point–centre pairs at unit distance.
- The proof uses the identity ‖d‖_V = 1 ⟺ d_x² = 1 − 2|d_y|. Every point lies strictly above every centre (y ≥ 1/(4AB) − 1/8 versus y ≤ −1/8). This rules out incidences on the lower arcs and also shows that no point equals a centre.
- Point–point and centre–centre unit distances can occur (point–point ones do, for A ≥ 2). They only raise degrees, so the lemma states "exactly" only for point–centre pairs, and Theorem 3(3) uses "≥".
- The all-k proof (Appendix C) has three cases:
  - k < √n: by the star;
  - √n ≤ k ≤ ⌊n/2⌋: by the lemma, with explicit A and B;
  - k > ⌊n/2⌋: by monotonicity.

  This gives c = 1/222 for all n ≥ 8 and 1 ≤ k ≤ n.
- `notes/socg27_sanity_checks.py` §5 confirms the exact count, the disjointness and the vertical separation for all 1 ≤ A, B ≤ 5, using rational arithmetic.
- The norm is given explicitly as ‖(x,y)‖_V = |y| + √(x²+y²), with unit ball {|y| ≤ (1−x²)/2}. The text notes that this ball is a linear image of {|y| + x² ≤ 1}, the form in some descriptions of Valtr's norm, and that a linear change of coordinates does not change Λ_k.

**3. "Almost all norms".** *Done in the draft.*
- The text now quotes the quantifier of Alon–Bucić–Sauermann: outside a meagre subset of the space of norms on ℝ^d, every n points span at most (d/2)·n·log₂ n unit distances. These norms are called *generic*, and the text says this is a topological notion that says nothing about any particular norm.
- The sentence "Theorems 1 and 3 describe the worst possible privacy cost over all norms" is gone. In its place the text says:
  - parts (1) and (2) give an upper bound for every norm;
  - part (1) is tight for every norm with a segment;
  - part (3) shows only that strict convexity alone cannot give a better bound than (2);
  - part (4) concerns generic norms only.
- Corollary 4 now gives explicit constants for generic norms: (n−1)/(8(1+e)) ≤ err* ≤ 4n·log₂ n, for all n ≥ 2 and ε ∈ (0, 1]. err* is the minimax expected absolute error.

**4. Citations.** Primary sites (arXiv, Dagstuhl, author pages) were blocked from this environment, so the checks below rely on web-search results.

| Reference | Status | Action taken |
|---|---|---|
| Alon–Bucić–Sauermann | Statement confirmed. Published in *Geom. Funct. Anal.* 35(1), 2025, pp. 1–42 (pages from one search result) | Bib entry updated to the journal version |
| Raskhodnikova–Smith (FOCS 2016) | GEM guarantee and formal bibliographic record confirmed; the conference paper and extended version use different theorem numbering | Appendix B states the guarantee directly and cites RS16 without a version-dependent theorem number |
| R2T (Dong, Fang, Yi, Tao, Machanavajjhala) | Authors, title, SIGMOD 2022, pages 759--772, and DOI 10.1145/3514221.3517844 confirmed | DOI and pages added to the BibTeX entry |
| Valtr | "Manuscript, 2005" confirmed by two sources | Unchanged |
| KNRS13 flow statistic | Normalization not checked against the paper | Text changed to "one half of the maximum-flow value in the network of KNRS", which is proved in Prop. 13 regardless of how KNRS normalize |
| Székely 1997 | CPC 6(3):353–358 confirmed; the multigraph crossing lemma has the form c·e³/(m·n²) under a linear lower bound on e | The draft uses unspecified absolute constants |
| Zahl | O(n^{295/197+ε}) and IMRN 2019(20):6235–6284 confirmed | Volume, issue and pages added |
| Sawin; Alon et al. "Remarks" | Confirmed earlier, with the quantifier "arbitrarily large n" | Unchanged |

**5. Format, AI disclosure, anonymity.**
- Line count: about 418 lines under a SoCG-style count (see §1). Recount with the official class.
- AI disclosure: the Dagstuhl Publishing GenAI statement, which applies to LIPIcs, requires disclosure of substantive use. The disclosure goes in the manuscript (acknowledgments or before the references) and must state the type and purpose of use and the extent of human review.
  - The draft now has a visible paragraph, "Use of generative AI", before the references. It names Claude for this version and OpenAI Codex for earlier material, as disclosed in the SODA source.
  - The disclosure now states that the authors reviewed and revised the text, independently checked the mathematical claims and citations, and take responsibility for the manuscript; the authors should confirm this wording before submission.
  - It must **not** go into `\acknowledgements`, because the `anonymous` option hides that field.
- Anonymity: the PDF metadata shows "Anonymous author(s)". A text scan of the PDF finds no author names, repository names, SODA/rebuttal/HotCRP mentions or self-references. "SODA" appears only as a venue name in a bibliography entry. Internal author-review comments have been removed from `main.tex`.

## 8. Roadmap (as agreed on 3 Oct 2026)

- **SoCG 2027:** primary target for this geometric paper.
- **ICALP Track A, or the next SODA:** for the local-minimax theorem (`manuscript/local_minimax_working.tex`) once it matures.
- **PODS:** reserved for the version about quantized distances, thresholds and histograms.

**Overlap check:** Appendix E of the SoCG draft (grid points, separated annuli, histograms) overlaps with the planned PODS material. If both are submitted in the same cycle (SoCG around 1 Dec, PODS cycle 2 around 3–10 Dec 2026), drop Appendix E from the SoCG version or reduce it to a pointer. Concurrent submissions must not overlap.
