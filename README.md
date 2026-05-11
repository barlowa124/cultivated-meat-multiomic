# Cultivated Meat Research — Rao Lab
Multi-omic state map and QC biomarker panel for stem cell manufacturing readiness.

## Results
- **96.7% CV accuracy** on 239-sample state classification
- **30-gene qPCR panel** matches full multi-omic embedding
- **0.800 mean pathway correlation** with METAFlux-derived Y (Ridge)
- 5 publication figures + supplementary materials + primer designs

## Structure
```
cultivated_meat_projects/
├── notebooks/          # Analysis scripts (P1-P5 + expanded + figures)
├── p1_protocol_meta_analysis/output/
├── p2_state_map/output/    # Figures, refined manuscript, integration results
├── p3_qc_panel/output/     # 30-gene panel, coefficients
├── p4_media_formulation/output/
├── p5_reproducibility/output/
├── shared_data/            # Data paths config
├── manuscript_draft.md     # Original draft
├── progress.yaml           # Project status tracker
└── requirements.txt
```

## Quick Start
```bash
pip install -r requirements.txt
python notebooks/p2p3_expanded.py  # Main analysis
python notebooks/generate_figures.py  # Publication figures
```

## Manuscript
Target: Frontiers in Cell and Developmental Biology / npj Science of Food
Refined version: `p2_state_map/output/manuscript_refined.md`
Supplementary: `p2_state_map/output/supplementary_materials.md`

## Data
- RNA-seq: 239 samples from scFEA pseudo-bulk (23,682 genes)
- METAFlux: 13,082 reactions aggregated to 10 metabolic pathways
- Protocols: 6 documents from Rao Lab
- Media: 5 spreadsheets (Media, Ordering, Aliquots, Antibodies, CEF Experiments)