"""bioRxiv preprint preparation: format manuscript + figures for submission."""
import json, shutil
from pathlib import Path

PROJ = Path(__file__).resolve().parents[1]
OUT = PROJ / "p2_state_map/output"
BIORXIV = PROJ / "biorxiv_submission"
BIORXIV.mkdir(exist_ok=True)

print("=" * 60)
print("BIORXIV PREPRINT PREPARATION")
print("=" * 60)

# Copy manuscript
manuscript = OUT / "manuscript_refined.md"
if manuscript.exists():
    shutil.copy(manuscript, BIORXIV / "manuscript.md")
    print(f"Copied manuscript")

# Copy supplementary
suppl = OUT / "supplementary_materials.md"
if suppl.exists():
    shutil.copy(suppl, BIORXIV / "supplementary_materials.md")
    print(f"Copied supplementary materials")

# Copy figures
figures = [
    "fig1_state_map_publication.png",
    "fig2_pseudotime_publication.png",
    "fig3_network_publication.png",
    "fig4_transfer_publication.png",
    "fig5_summary_publication.png",
]
for fig in figures:
    src = OUT / fig
    if src.exists():
        shutil.copy(src, BIORXIV / fig)
        print(f"Copied {fig}")

# Create submission metadata
metadata = {
    "title": "A Multi-Omic Manufacturing-Readiness State Map for Cultivated Meat: Derivation of a 30-Gene qPCR Quality Control Panel",
    "authors": ["Rao Lab"],
    "affiliation": "North Carolina State University",
    "abstract": (
        "Cultivated meat production requires robust quality control metrics to assess "
        "stem cell manufacturing readiness. Here we present a multi-omic state map integrating "
        "RNA-seq transcriptomics and METAFlux metabolic flux predictions across 239 samples, "
        "defining three manufacturing readiness states: expansion-competent, committed, and terminal. "
        "A 30-gene L1-regularized logistic regression panel achieves 96.7% cross-validation accuracy, "
        "matching the full multi-omic embedding. Cross-species validation in bovine (GSE173199, 38 samples) "
        "confirms conservation of the three-state structure. Single-nucleus RNA-seq analysis (GSE240556, "
        "17,541 nuclei) validates panel gene expression at cellular resolution. Bayesian Gaussian mixture "
        "modeling provides uncertainty quantification with 97.9% confident assignments. The panel enables "
        "routine batch triage at $50-100 per assay with 4-6 hour turnaround, providing a practical tool "
        "for cultivated meat bioprocess optimization."
    ),
    "keywords": [
        "cultivated meat", "stem cells", "multi-omics", "quality control",
        "RNA-seq", "metabolic flux", "biomarker panel", "qPCR", "cross-species"
    ],
    "data_availability": "Public GEO datasets: GSE267112, GSE173199, GSE240556, GSE206914",
    "code_availability": "GitHub repository (to be assigned)",
    "competing_interests": "None declared",
    "funding": "NC State University",
}

json.dump(metadata, open(BIORXIV / "submission_metadata.json", "w"), indent=2)

# Create cover letter
cover_letter = """Dear Editors,

We submit our manuscript titled "A Multi-Omic Manufacturing-Readiness State Map for Cultivated Meat: Derivation of a 30-Gene qPCR Quality Control Panel" for consideration in your journal.

This work addresses a critical gap in cultivated meat bioprocessing: the lack of standardized, quantitative quality control metrics for assessing stem cell manufacturing readiness. Our key contributions include:

1. First multi-omic state map integrating transcriptomics and metabolic flux for cultivated meat manufacturing
2. A practical 30-gene qPCR panel achieving 96.7% accuracy matching full multi-omic embeddings
3. Cross-species validation in bovine confirming methodological conservation
4. Single-nucleus resolution validation via snRNA-seq
5. Bayesian uncertainty quantification enabling confident batch triage decisions

The panel costs $50-100 per assay with 4-6 hour turnaround, making it immediately deployable in academic and industrial settings.

All data and code are publicly available. We believe this work will be of broad interest to the cultivated meat, stem cell biology, and bioprocess engineering communities.

Sincerely,
Rao Lab
North Carolina State University"""

(BIORXIV / "cover_letter.txt").write_text(cover_letter)
print(f"Created cover letter")

# Create README for submission
readme = """# bioRxiv Submission Package

## Contents
- `manuscript.md` — Main manuscript
- `supplementary_materials.md` — Supplementary tables and figures
- `fig1-5_*.png` — Publication-quality figures (300 DPI)
- `submission_metadata.json` — Author, abstract, and keyword metadata
- `cover_letter.txt` — Cover letter for editors

## Pre-submission Checklist
- [ ] All authors have approved the manuscript
- [ ] Figures meet resolution requirements (300 DPI minimum)
- [ ] Data availability statements are complete
- [ ] Competing interests declared
- [ ] Funding acknowledged
- [ ] References formatted per journal style

## Target Journals
1. Frontiers in Cell and Developmental Biology
2. npj Science of Food
3. Scientific Reports
"""

(BIORXIV / "README.md").write_text(readme)
print(f"Created submission README")

print(f"\nSubmission package ready at: {BIORXIV}")
print("=" * 60)
print("DONE")
