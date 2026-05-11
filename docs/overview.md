# Project Overview

## Motivation

Cultivated meat production requires robust, quantitative quality control metrics to assess stem cell manufacturing readiness. Current approaches rely on subjective morphological assessment and endpoint assays that cannot provide real-time feedback for bioprocess optimization.

## Approach

We integrate:
- **RNA-seq transcriptomics** (425 samples across conditions)
- **METAFlux metabolic flux predictions** (239 samples with paired flux)
- **Cross-species validation** (bovine GSE173199, GSE240556; porcine GSE206914)
- **Machine learning** (PCA, K-means, L1 logistic regression, VAE, Bayesian GMM)

## Three Manufacturing Readiness States

1. **Expansion-competent** — High proliferative capacity, low differentiation markers
2. **Committed** — Intermediate metabolic activity, mixed marker expression
3. **Terminal** — High differentiation markers, low proliferative capacity

## 30-Gene qPCR Panel

The panel achieves 96.7% cross-validation accuracy matching the full multi-omic embedding, enabling routine batch triage at \$50-100 per assay with 4-6 hour turnaround.
