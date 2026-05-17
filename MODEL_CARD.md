"""
# Model Card: 30-Gene QC Panel for Cultivated Meat Manufacturing-Readiness

## Model Overview
**Name:** Cultivated Meat 30-Gene qPCR Panel State Classifier  
**Version:** 1.0.0  
**Date:** 2026-05-15  
**Developer:** Rao Lab  
**License:** MIT  
**Repository:** https://github.com/barlowa124/cultivated-meat-multiomic

## Intended Use
- **Primary use:** Predict manufacturing-readiness state of cultivated muscle tissue from 30-gene qPCR expression values
- **States:** expansion_competent, committed, terminal
- **Users:** Bioprocess engineers, QA/QC scientists in cultivated meat manufacturing
- **Out-of-scope:** Not intended for human diagnostics, genetic screening, or food safety pathogen detection

## Model Architecture
- **Type:** Logistic Regression (primary) + Deep Neural Network (validation)
- **Input:** 30 normalized gene expression values (log TPM)
- **Output:** Class label + probability distribution over 3 states + confidence score
- **DNN architecture:** 30 → 64 (ReLU, dropout 0.2) → 32 (ReLU, dropout 0.2) → 3 (softmax)
- **Training:** 5-fold stratified cross-validation

## Training Data
- **Source:** scFEA pseudobulk TPM + MetaFlux metabolic flux (239 samples)
- **Labels:** K-means clustering (k=3) on PCA-reduced transcriptome + fluxome
- **State map:** expansion_competent (61), committed (86), terminal (92)
- **Preprocessing:** log1p transformation, variance filtering (top 75%), StandardScaler

## Performance
| Metric | Value |
|--------|-------|
| CV Accuracy (Logistic) | 96.7% ± 1.0% |
| CV Accuracy (DNN) | 96.2% ± 1.5% |
| Bootstrap Accuracy | 96.3% ± 0.8% |
| Bayesian Confidence | 97.9% |
| Cross-species (bovine) | 92.0% |
| Noise robustness (25% CV) | 94.2% |

## Ethical Considerations & Limitations
- **Species limitation:** Primary validation on bovine; porcine and human data are secondary
- **Platform limitation:** Trained on pseudobulk RNA-seq; qPCR validation pending
- **Batch effects:** Models trained on single dataset; external validation required
- **Bias:** Training data may not represent all cell lines, media formulations, or bioreactor types
- **Environmental:** Intended to reduce waste by predicting batch outcomes before harvest

## Explainability
- SHAP-based gene importance: MALAT1, LMNA, CTSA, C1QBP most influential
- Per-state expression profiles available in `shap_dnn_results.json`
- Linear model coefficients provide direct interpretability

## Deployment
- **API:** Flask REST endpoint at `/predict` (see `api/app.py`)
- **Dashboard:** Streamlit interactive interface (see `dashboard/app.py`)
- **Docker:** `docker build -t cultivated-meat-multiomic .`
- **Artifacts:** `api/model.pkl`, `api/scaler.pkl`, `api/model_metadata.json`

## Maintenance
- **Retraining frequency:** Every 6 months or upon accumulation of 50+ new labeled samples
- **Monitoring:** Track prediction confidence distribution; flag drift if mean confidence < 90%
- **Versioning:** Semantic versioning; major = architecture change, minor = retraining, patch = bugfix

## Citation
```
Rao Lab (2026). A 30-gene qPCR panel predicts manufacturing-readiness states 
in cultivated muscle tissue. GitHub: barlowa124/cultivated-meat-multiomic
```

## Contact
- **Issues:** https://github.com/barlowa124/cultivated-meat-multiomic/issues
- **Email:** [lab email]
