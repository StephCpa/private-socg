# Private SoCG paper materials

This repository collects the LaTeX sources, bibliography, compiled PDFs, and selected research notes for the paper on node-private counting in planar distance graphs.

## Contents

- `manuscript/socg27/main.tex`: SoCG 2027 rewrite in LIPIcs format (anonymous). It is organised around the top-degree mass Λ_k(n) of unit-distance graphs: the reduction from node-private counting, the link to unit-circle incidences, the classification over norms (including Valtr's norm), and the Euclidean window. `manuscript/pdf/socg27_main.pdf` is the compiled copy.
- `notes/SoCG27_plan_review.md`: review of the SoCG rewrite plan, a traceability table for the required revisions, verification log, and remaining author tasks.
- `notes/socg27_sanity_checks.py`: numerical checks for the lemmas and the Valtr construction in the SoCG draft.
- `manuscript/local_minimax_working.tex`: current working manuscript. It develops the local-minimax formulation, the geometric degree-tail bounds, and the node-private counting application.
- `manuscript/soda_submitted_frontloaded.tex`: anonymized frontloaded version submitted to SODA 2027.
- `manuscript/refs.bib`: bibliography shared by the manuscript sources.
- `manuscript/pdf/`: compiled PDFs corresponding to the two manuscript sources.
- `notes/`: selected research plans, revision notes, and earlier English drafts that provide provenance for the current manuscript.
- `assets/`: reserved for manuscript figures or other visual source files. The current paper is text and proof based and has no standalone figure source files.
- `data/`: reserved for experimental data. The current paper has no external dataset or experimental data files.

## Building the manuscripts

The SoCG draft builds from `manuscript/socg27/` with `latexmk -pdf main.tex`. It uses the bundled `lipics-v2021.cls`; replace it with `socg-lipics-v2021.cls` once the SoCG 2027 call is published (see the comment at the top of `main.tex`).

From `manuscript/`, a local LaTeX installation can compile either older source with:

```sh
latexmk -pdf local_minimax_working.tex
latexmk -pdf soda_submitted_frontloaded.tex
```

The bibliography file is referenced as `refs.bib`.

## Version note

The SoCG draft is a complete first version but has not yet passed the author rewrite, independent proof check and cold read listed in `notes/SoCG27_plan_review.md`. The local-minimax manuscript is a research working draft. The SODA file is retained as a historical submission artifact. Reviewer reports, rebuttal text, HotCRP content, temporary screenshots, and LaTeX build caches are intentionally excluded.
