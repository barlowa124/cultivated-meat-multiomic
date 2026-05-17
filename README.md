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