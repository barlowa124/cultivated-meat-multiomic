# Installation

## Requirements

- Python 3.10+
- 16GB+ RAM recommended
- CUDA-capable GPU optional (for VAE training)

## Dependencies

```bash
pip install -r requirements.txt
```

Key packages:
- `numpy`, `pandas`, `scipy` — Data processing
- `scikit-learn` — Machine learning
- `torch` — Deep learning (VAE)
- `anndata`, `scipy.sparse` — Single-cell data
- `matplotlib`, `seaborn` — Visualization

## Data

Public datasets are downloaded automatically or can be placed in:
- `cross_species_validation/` — Bovine and porcine GEO data
- Source data paths configured in `shared_data/data_paths.yaml`
