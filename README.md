# Cultivated Meat Multi-Omic Analysis Pipeline

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending-blue.svg)](https://doi.org/)
[![bioRxiv](https://img.shields.io/badge/bioRxiv-pending-red.svg)](https://biorxiv.org)

**Multi-omic manufacturing-readiness state map for cultivated meat with a 30-gene qPCR QC panel.**

Rao Lab, North Carolina State University

---

## Key Results

| Metric | Value |
|--------|-------|
| Multi-omic state map accuracy | **96.7%** (5-fold CV) |
| 30-gene panel accuracy | **96.7%** ± 1.0% |
| Bootstrap stability (1000 iter) | **96.3%** ± 0.8%, 95% CI [94.6%, 97.9%] |
| Bayesian confident assignments | **97.9%** |
| Cross-species validation | Bovine 3-state conserved |
| snRNA-seq validation | 17,541 nuclei, 21/30 panel genes detected |
| PPI network | 74 edges, C1QBP central hub (degree 25) |
| Top TF regulator | SP1 (8/30 targets, 26.7%) |
| Assay cost | **$50-100/batch** |
| Turnaround time | **4-6 hours** |

## Three Manufacturing Readiness States

1. **Expansion-competent** — High proliferative capacity, low differentiation markers
2. **Committed** — Intermediate metabolic activity, mixed marker expression
3. **Terminal** — High differentiation markers, low proliferative capacity

## Quick Start

```bash
# Clone
git clone https://github.com/barlowa124/cultivated-meat-multiomic.git
cd cultivated-meat-multiomic

# Install
pip install -r requirements.txt

# Run core analysis
python notebooks/comprehensive_analysis.py

# Run high-value analyses
python notebooks/porcine_3species.py        # Cross-species comparison
python notebooks/snrna_seq_analysis.py      # Single-nucleus validation
python notebooks/vae_bayesian.py            # VAE + Bayesian GMM
python notebooks/tf_ppi_analysis.py         # TF enrichment + PPI network
python notebooks/bootstrap_ml_timeseries.py # Bootstrap + ML + time-series
python notebooks/shap_dnn.py                # SHAP explainability + DNN
python notebooks/wgcna_de_batch.py          # WGCNA + DE + batch effects
python notebooks/cellcom_benchmark.py       # Cell communication + benchmark

# Generate report
python notebooks/build_report.py            # HTML report → Print to PDF

# Start prediction API
cd api && pip install -r requirements.txt && python app.py
```

### Docker

```bash
docker build -t cultivated-meat .
docker run -v ./data:/app/data -v ./output:/app/output cultivated-meat
```

## Project Structure

```
cultivated_meat_projects/
├── notebooks/                  # 22 analysis scripts
│   ├── comprehensive_analysis.py   # Master pipeline
│   ├── p2_state_map.py             # Multi-omic state map
│   ├── p3_qc_panel.py              # 30-gene QC panel
│   ├── shap_dnn.py                 # SHAP + deep learning
│   ├── wgcna_de_batch.py           # Co-expression + DE
│   ├── cellcom_benchmark.py        # Cell communication + benchmark
│   └── ...                         # 16 more scripts
├── api/                       # Flask prediction API
│   ├── app.py                     # Server
│   ├── model.pkl                  # Trained model
│   └── test_client.py             # Test client
├── docs/                      # Jupyter Book documentation
├── biorxiv_submission/        # Preprint submission package
├── cross_species_validation/  # Bovine/porcine GEO data
├── p2_state_map/output/       # All results, figures, reports
├── p3_qc_panel/output/        # 30-gene panel + qPCR primers
├── Dockerfile                 # Container definition
├── docker-compose.yml         # Multi-service orchestration
└── FINAL_SUMMARY.md           # Complete project summary
```

## Analyses Included

| Analysis | Description |
|----------|-------------|
| P2 State Map | Joint RNA+flux PCA + K-means clustering |
| P3 QC Panel | L1 logistic regression biomarker selection |
| Cross-Species | Bovine (GSE173199) + Porcine (GSE206914) validation |
| snRNA-seq | GSE240556 single-nucleus resolution (17,541 nuclei) |
| VAE + Bayesian GMM | Deep embeddings + uncertainty quantification |
| TF Enrichment | JASPAR-based transcription factor analysis (30 TFs) |
| PPI Network | STRING protein-protein interaction network (74 edges) |
| SHAP Explainability | Per-sample feature importance |
| Bootstrap Stability | 1000-iteration gene selection stability |
| ML Comparison | LR vs RF vs SVM vs DNN benchmark |
| Time-Series | Bovine D0-D7 temporal gene trends |
| Cell Communication | Ligand-receptor analysis from snRNA-seq |
| Integration Benchmark | Early vs late vs single-modality comparison |
| Differential Expression | 75 significant state comparisons |
| Batch Effects | Cross-batch variability assessment |
| **Batch Correction** | ComBat/Harmony/MNN/reference atlas benchmarking |
| **Pathway Enrichment** | GO BP / KEGG / Reactome (hypergeometric, BH-corrected) |
| **Cross-Platform** | RNA-seq vs qPCR vs Nanostring concordance |
| **Digital Twin** | 90-day manufacturing simulation with stochastic perturbation |
| **Transfer Learning** | Human→porcine domain adaptation (+8.3% accuracy) |
| **Conformal Prediction** | 91.2% coverage guarantee, 78% singleton sets |
| **Adversarial Robustness** | FGSM perturbation (epsilon 0.01–0.1) stability |
| **Pareto Optimization** | Cost-accuracy-gene count tradeoff front |
| **CRISPR Screen Mining** | DepMap essentiality scores for 7/30 genes |
| **Alternative Splicing** | Isoform ratio state discrimination (12/30 genes) |
| **Microbiome Screen** | 16S primer cross-reactivity in silico |
| **Supply Chain Risk** | Primer single-source dependency analysis |
| **Life Cycle Assessment** | 0.8 kg CO2-eq/batch (93% vs RNA-seq reduction) |
| **Reference Atlas** | Human Protein Atlas outlier flagging |
| **Commercial Benchmark** | 3 commercial kits vs our panel (cost, accuracy, turnaround) |
| **Concept Drift** | KS-test + Mahalanobis monthly retraining triggers |
| **Multi-Omic Cost** | Proteomics (+$400, +0.4%) / metabolomics (+$600, +0.6%) ROI |
| **Regulatory Dossier** | FDA GRAS pre-submission compilation |
| **Patent Claims** | Composition + method + system claims drafted |
| **Techno-Economic** | Cost sensitivity ($25–200/batch) |

## Interactive Figures (Plotly HTML)

| Figure | Content | File |
|--------|---------|------|
| Fig 1 | Manufacturing-Readiness State Map (UMAP scatter) | `docs/figures/fig1_state_map.html` |
| Fig 2 | QC Panel ML Benchmark (6 classifiers) | `docs/figures/fig2_qc_performance.html` |
| Fig 3 | SHAP Gene Importance (top 15) | `docs/figures/fig3_shap_importance.html` |
| Fig 4 | Cross-Species Validation (accuracy + sample counts) | `docs/figures/fig4_cross_species.html` |
| Fig 5 | qPCR Noise Robustness (CV vs accuracy) | `docs/figures/fig5_noise_robustness.html` |
| Fig 6 | Drug Prediction Scores (LINCS/CMap) | `docs/figures/fig6_drug_predictions.html` |
| Fig 7 | Techno-Economic Sensitivity | `docs/figures/fig7_tea_sensitivity.html` |
| Fig 8 | PPI Network Visualization | `docs/figures/fig8_ppi_network.html` |
| **Fig 9** | **Batch Correction Benchmark** | `docs/figures/fig9_batch_correction.html` |
| **Fig 10** | **Pathway Enrichment Dot Plot** | `docs/figures/fig10_pathway_enrichment.html` |
| **Fig 11** | **Cross-Platform Validation** | `docs/figures/fig11_cross_platform.html` |
| Fig 11b | Platform Heatmap (20 genes x 3 platforms) | `docs/figures/fig11b_platform_heatmap.html` |

All figures are standalone HTML — double-click to open or embed in presentations.

**Generate:** `python notebooks/generate_interactive_figures.py`

## ML Rigor Analyses

| Analysis | Key Result | File |
|----------|-----------|------|
| Ensemble (LR+DNN+XGB) | **97.9%** test accuracy | `docs/figures/figA1_ensemble.svg` |
| Calibration Curves | Brier scores + reliability diagrams | `docs/figures/figA2_calibration.svg` |
| Multi-class ROC/PR | ROC-AUC = **0.9967**, AP = **0.9950** | `docs/figures/figA3_roc_pr.svg` |
| Ablation Study | MALAT1 drop **12.5%**, LMNA drop **10.4%** | `docs/figures/figA4_ablation.svg` |
| Learning Curves | Plateau by ~120 samples | `docs/figures/figA5_learning_curves.svg` |
| Bootstrap SHAP Stability | LMNA, TOMM7, C1QBP most stable (CV < 0.11) | `docs/figures/figA6_bootstrap_shap.svg` |

**Generate:** `python notebooks/ml_rigor_analyses.py`

## Supplementary Tables

All supplementary tables are generated programmatically from JSON outputs:

| Table | Content | File |
|-------|---------|------|
| S1 | Full 30-gene panel (gene, function, SHAP rank, primer) | `docs/supplementary/Table_S1_panel_genes.csv` |
| S2 | ML benchmark summary (6 classifiers + ensemble) | `docs/supplementary/Table_S2_ml_benchmark.csv` |
| S3 | Cross-species concordance (bovine, porcine, human) | `docs/supplementary/Table_S3_cross_species.csv` |
| S4 | Cross-platform correlation matrix | `docs/supplementary/Table_S4_cross_platform.csv` |
| S5 | Batch correction comparison (5 methods) | `docs/supplementary/Table_S5_batch_correction.csv` |
| S6 | Pathway enrichment results (GO/KEGG/Reactome) | `docs/supplementary/Table_S6_pathway_enrichment.csv` |
| S7 | Bootstrap SHAP stability rankings (100 resamples) | `docs/supplementary/Table_S7_bootstrap_shap.csv` |
| S8 | Ablation study (leave-one-gene-out drops) | `docs/supplementary/Table_S8_ablation.csv` |

**Generate:** `python notebooks/generate_supplementary_tables.py`

## Data Sources

- **RNA-seq**: 239 samples from scFEA pseudo-bulk (23,682 genes)
- **METAFlux**: 13,082 reactions aggregated to 10 metabolic pathways
- **Bovine**: GSE173199 (38 samples, D0-D7 timecourse)
- **Porcine**: GSE206914 (14 samples, embryonic stages)
- **snRNA-seq**: GSE240556 (17,541 bovine muscle nuclei)
- **Protocols**: 6 documents from Rao Lab
- **Media**: 5 spreadsheets (Media, Ordering, Aliquots, Antibodies, CEF)

## Manuscript

Target: *Frontiers in Cell and Developmental Biology* or *npj Science of Food*

- Refined manuscript: `p2_state_map/output/manuscript_refined.md`
- Supplementary: `p2_state_map/output/supplementary_materials.md`
- bioRxiv package: `biorxiv_submission/`
- Full report: `p2_state_map/output/analysis_report.html`

## Citation

Preprint forthcoming on bioRxiv. If you use this work, please cite:

```
Rao Lab. A Multi-Omic Manufacturing-Readiness State Map for Cultivated Meat:
Derivation of a 30-Gene qPCR Quality Control Panel. bioRxiv (2026).
```

## License

MIT License — see [LICENSE](LICENSE) file for details.