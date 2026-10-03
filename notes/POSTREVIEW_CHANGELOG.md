# Post-Review Rebuild

The submitted SODA files are unchanged. The rebuilt research draft is paper_soda_postreview.tex; paper_pods27_working.tex is an identical starting copy for a possible PODS submission.

## Substantive Changes

- Reframed the query as node-private exact-distance self-join counting.
- Made the prior KNRS flow surrogate \(g_D\) the primary mechanism and retained \(f_D\) as an integral \(b\)-matching interpretation.
- Proved \(f_D\le g_D\le U\) and \(g_D=f_D^{\mathrm{frac}}\), the degree-only fractional \(b\)-matching optimum.
- Added an early full add/remove local-minimax theorem based on the radius-\(h\) modulus \(\omega_h(P)\).
- Decomposed the local modulus into deletion and insertion profiles; the latter captures external circle occupancy and edges internal to newly inserted records.
- Identified \(\min_D\{\operatorname{tail}_D+tD\}\) with the sum of the largest \(t\) degrees and related it within a factor of two to deletion down sensitivity.
- Connected the insertion profile to the extremal unit-distance function \(u(t)\).
- Generalized the no-log tail proof to geometric graph classes satisfying the same uniform incidence estimate.
- Added verified 2020–2024 references on sensitivity preprocessing and node-private graph analysis.
- Corrected the separated-annulus statement for \(t>r\).

## Verification

- Both long drafts compile with latexmk using halt-on-error.
- The final logs contain no undefined references, citation warnings, overfull boxes, or underfull boxes.
- Both PDFs are 26 pages in the current article layout.
- Exhaustive computation over all 1,099 labeled graphs on at most five vertices verified the oracle/top-degree identity, the factor-two deletion bound, and the flow--fractional-\(b\)-matching equality for every tested threshold.

## Remaining Work Before PODS

- Obtain an independent proof audit of the local-minimax theorem and flow–LP equivalence.
- Convert to the official PODS format and place secondary proofs and the discrepancy direction in an appendix.
- Reduce the main text to 15 pages excluding references and the optional appendix.
- Strengthen the data-management motivation around private geometric self-joins without overstating the practical role of continuous exact equality.
- Decide by November 15 whether the strengthened theorem is sufficient for a top-tier resubmission.
