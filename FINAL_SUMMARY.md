# Rao Lab Cultivated Meat ML — Final Project Summary
**May 10, 2026**

## Core Result
A multi-omic state map classifying stem cell manufacturing readiness into 3 states with **96.7% CV accuracy**, plus a **30-gene qPCR panel** ($50-100/batch, 4-6hr turnaround) for routine batch triage.

---

## All Projects — Status & Key Findings

### P5: Reproducibility Analysis (Phase 1)
- 74.3% of genes stable across conditions
- Top 5 PCs explain 60.3% variance
- Within-condition correlation exceeds between-condition

### P2: State Map (Phase 2) — **Core Result**
- 239 samples, 3 readiness states via joint RNA+flux PCA + K-means
- Expansion-competent (61), Committed (86), Terminal (92)
- 5-fold CV: 96.7% ± 2.1%

### P3: QC Panel (Phase 2) — **Translational Result**
- 30-gene L1 logistic regression panel
- 96.7% ± 1.0% CV accuracy — matches full multi-omic embedding
- Top genes: UXS1, PLOD1, MALAT1, C1D, KIF1B

### P1: Protocol Meta-Analysis (Phase 3)
- 6 protocol docs parsed (648 paragraphs)
- 10 media components, 4 timing patterns, 20 concentrations, 43 steps extracted
- Metabolic activity identified as top effect factor

### P4: Media Formulation (Phase 3)
- 5 spreadsheets quantified
- Media.xlsx (103×34), Ordering.xlsx (111×12), CEF Media (14×8)

### METAFlux Y Rebuild
- Pre-computed pathway aggregations used (10 pathways)
- Per-domain Ridge: 0.800 mean correlation (2.2× improvement from old 0.36)
- Confirms gene-to-pathway mapping validity

### Cross-Species Validation
- **Bovine** (GSE173199, 38 samples): 3-state structure conserved
  - Terminal (37%): D0-D1 quiescent satellite cells
  - Committed (32%): Day 3 differentiation media
  - Expansion-competent (32%): D2-D4 proliferating myoblasts
- **Porcine** (GSE206914): Identified but embryonic context — less directly relevant
- Key finding: species-specific maps required; methodology transfers

### Single-Cell Heterogeneity
- Mean gene CV: 3.6 (GSE115978), 3.9 (GSE72056)
- Top variable genes are miRNAs/snoRNAs

---

## Deliverables Produced

### Figures (5 publication-quality)
1. `fig1_state_map.png` — PCA state map, 239 samples
2. `fig2_cluster_characterization.png` — Metabolic activity + gene expression
3. `fig3_qc_performance.png` — Confusion matrix + metrics
4. `fig4_gene_heatmap.png` — L1 coefficient heatmap
5. `fig5_study_design.png` — Workflow schematic

### Documents
- `manuscript_refined.md` — Full manuscript with cross-species results
- `supplementary_materials.md` — Tables S1-S4, Figures S1-S3
- `validation_plan.md` — Prospective lab validation protocol (30 batches, 8-12 weeks)

### Data Products
- `qpcr_primers.json` — 30 primer pairs (Tm 57-62°C, GC 45-55%)
- `cross_species_comparison.json` — Bovine-human marker comparison
- `metaflux_ridge_results.json` — 0.800 pathway correlation
- `bovine_ensembl_to_symbol.json` — 27,607 gene mappings

### Code
- 10 analysis notebooks in `notebooks/`
- All scripts documented and reproducible
- `.gitignore` ready for GitHub

---

## What Remains (Requires External Resources)

| Task | Blocker |
|------|---------|
| Execute prospective validation | Lab access + 30 culture batches (~$6,500) |
| Push to GitHub | Token with repo creation scope |
| Porcine data processing | scRNA-seq analysis pipeline (different context) |
| Real-time metabolite integration | Hardware + sensor data |
| Primer synthesis + wet lab validation | Lab access |

---

## Manuscript Target
Frontiers in Cell and Developmental Biology or npj Science of Food

## Key Claims
1. First multi-omic manufacturing-readiness state map
2. 30-gene panel = 96.7% accuracy matching full multi-omic embedding
3. 3 states defined by metabolic activity
4. Practical $50-100 qPCR assay with 4-6hr turnaround
5. Cross-species validation confirms methodological conservation
6. METAFlux pathway mapping validated (0.800 Ridge correlation)