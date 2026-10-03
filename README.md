# Private SoCG paper materials

This repository collects the LaTeX sources, bibliography, compiled PDFs, and selected research notes for the paper on node-private counting in planar distance graphs.

## Contents

- `manuscript/local_minimax_working.tex`: current working manuscript. It develops the local-minimax formulation, the geometric degree-tail bounds, and the node-private counting application.
- `manuscript/soda_submitted_frontloaded.tex`: anonymized frontloaded version submitted to SODA 2027.
- `manuscript/refs.bib`: bibliography shared by the manuscript sources.
- `manuscript/pdf/`: compiled PDFs corresponding to the two manuscript sources.
- `notes/`: selected research plans, revision notes, and earlier English drafts that provide provenance for the current manuscript.
- `assets/`: reserved for manuscript figures or other visual source files. The current paper is text and proof based and has no standalone figure source files.
- `data/`: reserved for experimental data. The current paper has no external dataset or experimental data files.

## Building the manuscripts

From `manuscript/`, a local LaTeX installation can compile either source with:

```sh
latexmk -pdf local_minimax_working.tex
latexmk -pdf soda_submitted_frontloaded.tex
```

The bibliography file is referenced as `refs.bib`.

## Version note

The local-minimax manuscript is a research working draft, not a claim that a SoCG-formatted submission is complete. The SODA file is retained as a historical submission artifact. Reviewer reports, rebuttal text, HotCRP content, temporary screenshots, and LaTeX build caches are intentionally excluded.
