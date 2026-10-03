# Paper 742: Post-SODA Revision Plan

## Status as of September 3, 2026

- The submitted SODA source and PDF remain untouched.
- A concise final response (SODA27_paper742_rebuttal_final.md) and an expanded backup (SODA27_paper742_rebuttal.md, 4,645 characters) are ready.
- The post-review paper now defines the KNRS flow surrogate first and proves \(f_D\le g_D\le U\). It also proves that \(g_D\) is exactly the degree-only fractional \(b\)-matching relaxation.
- The rebuilt paper has a new full add/remove local-minimax theorem, including separate deletion and insertion profiles. This is new post-submission work and must not be presented in the SODA response as if it appeared in the submitted paper.
- The annulus correction and four verified post-2016 node-privacy references have been incorporated.
- paper_pods27_working.tex is a clean 26-page research draft. It is not yet compliant with the PODS 15-page main-text limit; compression and appendix separation remain.

## Immediate: September 3-4, 2026

1. Confirm the HotCRP author-response character limit and whether the instructions permit only text. Do not upload a replacement PDF unless explicitly authorized.
2. Submit the anonymous response in `SODA27_paper742_rebuttal.md` after adapting it to the exact limit.
3. Do not submit overlapping results to another proceedings venue while SODA review remains active.

## Technical Rebuild

### 1. Remove the unsupported mechanism-novelty claim

- Define the KNRS flow surrogate \(g_D=v_{\mathrm{fl}}/2\) first.
- Prove explicitly that \(f_D\le g_D\le U\), both have sensitivity at most \(D\), and therefore the geometric tail analysis applies to both.
- Retain \(f_D\) only as an integral interpretation; a triangle with \(D=1\) shows strict inequality \(f_D=1<g_D=3/2\).
- State that generalized exponential selection and bounded-degree projection are prior machinery.

### 2. Make local minimaxity the main theorem

- Replace the promise class as the organizing principle by an instance-dependent risk benchmark.
- Define the full add/remove radius-\(h\) modulus
  \[
  \omega_h(P)=\max_{Q:\,d_{\mathrm{node}}(P,Q)\le h}|U(Q)-U(P)|.
  \]
- Strengthen the current deletion-only lower bound to a two-point group-privacy lower bound over the full node-edit ball.
- Relate the upper bound uniformly on a local ball to top-degree sums/down-sensitivity.
- Treat insertion effects through external circle occupancy and the unit-distance extremal function on newly inserted points.
- State all privacy-parameter restrictions explicitly, especially \(0<\varepsilon\le1\).

Status: completed in the research draft, subject to an independent proof audit before resubmission.

### 3. Recast the geometric contribution

- Present unit-distance counting as a node-private geometric self-join query.
- State the high-degree incidence lemma and the no-log tail corollary as the first geometric theorem.
- Make the unconditional, local-instance, and promise-class consequences separate corollaries.
- Consider generalization from unit circles to pseudo-circle or bounded-degree algebraic incidence families. This would materially strengthen the paper beyond a single application of the point-circle theorem.

Status: the unit-distance theorem, no-log proof, and abstract incidence-system extension are in the draft. A genuinely new non-circular application remains to be developed.

### 4. Rewrite for readability

- Put numbered formal main theorems on page 2.
- Replace compressed labels such as "near-regular many-distance-pair instances" with elementary graph descriptions.
- Remove claims that continuous exact-distance counting is a common applied location query.
- Reduce the 2026 unit-distance breakthrough to one related-work paragraph.
- Update central node-DP literature through 2026; distinguish it from local node DP.
- Keep the annulus theorem under \(t\le r\), and state the general-area alternative for \(t>r\).

Status: completed in the long draft. The PODS version still needs a 15-page main-text edit.

## Venue Decision

### Primary target: PODS 2027, Cycle 2

- Abstract deadline: December 3, 2026.
- Paper deadline: December 10, 2026.
- Reframe around private geometric self-join evaluation and responsible data management.
- Compress the self-contained main paper to 15 pages; move secondary proofs to the appendix.
- Go/no-go date: November 15. Submit only if the full local-minimax theorem or an equally substantive new result is complete.

### Alternatives

- ICALP 2027 Track A if the local-minimax theory becomes the clear central contribution and more development time is needed.
- Journal of Privacy and Confidentiality if no new theorem emerges; do not send the current contribution unchanged through another top-theory review cycle.
- Do not target PoPETs 2027 without a substantial real-world integration and evaluation component.
